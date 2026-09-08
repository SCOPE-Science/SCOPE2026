# Exact diversity / min-degree solver for intersecting 3-graphs (stdlib only)
import sys, time, itertools

class Solver:
    def __init__(self, n, miss_targets, deg_targets):
        self.n = n
        self.E0 = 0b111  # fixed edge {0,1,2}
        self.pool = []
        for a, b, c in itertools.combinations(range(n), 3):
            m = (1 << a) | (1 << b) | (1 << c)
            if m == self.E0:
                continue
            if m & self.E0 == 0:
                continue
            self.pool.append(m)
        self.P = len(self.pool)
        self.conf = []
        for i, T in enumerate(self.pool):
            self.conf.append([j for j, U in enumerate(self.pool) if j != i and T & U == 0])
        self.cons_members = []
        self.cons_target = []
        for v in range(n):
            if miss_targets[v] > 0:
                base = 0 if (self.E0 >> v) & 1 else 1
                mem = [i for i, T in enumerate(self.pool) if not (T >> v) & 1]
                self.cons_members.append(mem)
                self.cons_target.append(miss_targets[v] - base)
        for v in range(n):
            if deg_targets[v] > 0:
                base = 1 if (self.E0 >> v) & 1 else 0
                mem = [i for i, T in enumerate(self.pool) if (T >> v) & 1]
                self.cons_members.append(mem)
                self.cons_target.append(deg_targets[v] - base)
        self.C = len(self.cons_target)
        self.tri_cons = [[] for _ in range(self.P)]
        for c, mem in enumerate(self.cons_members):
            for i in mem:
                self.tri_cons[i].append(c)
        self.status = bytearray(self.P)
        self.have = [0] * self.C
        self.openct = [len(mem) for mem in self.cons_members]
        self.trail = []
        self.nodes = 0
        self.solutions = []
        self.collect = False
        self.sol_limit = 10 ** 9
        self.deadline = None

    def snapshot(self):
        return len(self.trail)

    def undo(self, snap):
        while len(self.trail) > snap:
            e = self.trail.pop()
            if e[0] == 's':
                self.status[e[1]] = 0
            else:
                _, c, dh, do = e
                self.have[c] -= dh
                self.openct[c] += do

    def do_include(self, i):
        if self.status[i] == 1:
            return True
        if self.status[i] == 2:
            return False
        self.status[i] = 1
        self.trail.append(('s', i))
        for c in self.tri_cons[i]:
            self.have[c] += 1
            self.openct[c] -= 1
            self.trail.append(('h', c, 1, 1))
            if self.have[c] + self.openct[c] < self.cons_target[c]:
                return False
        for j in self.conf[i]:
            if self.status[j] == 1:
                return False
            if self.status[j] == 0:
                self.status[j] = 2
                self.trail.append(('s', j))
                for c in self.tri_cons[j]:
                    self.openct[c] -= 1
                    self.trail.append(('h', c, 0, 1))
                    if self.have[c] + self.openct[c] < self.cons_target[c]:
                        return False
        return True

    def do_exclude(self, i):
        if self.status[i] == 2:
            return True
        if self.status[i] == 1:
            return False
        self.status[i] = 2
        self.trail.append(('s', i))
        for c in self.tri_cons[i]:
            self.openct[c] -= 1
            self.trail.append(('h', c, 0, 1))
            if self.have[c] + self.openct[c] < self.cons_target[c]:
                return False
        return True

    def force(self):
        changed = True
        while changed:
            changed = False
            for c in range(self.C):
                if self.have[c] + self.openct[c] == self.cons_target[c] and self.openct[c] > 0:
                    for i in self.cons_members[c]:
                        if self.status[i] == 0:
                            if not self.do_include(i):
                                return False
                            changed = True
        return True

    def pick_branch(self):
        best = -1; bestdef = 0
        for c in range(self.C):
            d = self.cons_target[c] - self.have[c]
            if d > bestdef and self.openct[c] > 0:
                bestdef = d; best = c
        if best < 0:
            return -1
        for i in self.cons_members[best]:
            if self.status[i] == 0:
                return i
        return -1

    def dfs(self):
        if self.deadline and time.time() > self.deadline:
            raise TimeoutError()
        self.nodes += 1
        if not self.force():
            return False
        i = self.pick_branch()
        if i < 0:
            for c in range(self.C):
                if self.have[c] < self.cons_target[c]:
                    return False
            if self.collect and len(self.solutions) < self.sol_limit:
                self.solutions.append([t for t in range(self.P) if self.status[t] == 1])
            return True
        snap = self.snapshot()
        found = False
        if self.do_include(i):
            if self.dfs():
                found = True
                if not self.collect:
                    return True
        self.undo(snap)
        snap = self.snapshot()
        if self.do_exclude(i):
            if self.dfs():
                found = True
                if not self.collect:
                    return True
        self.undo(snap)
        return found

    def run(self, collect=False, sol_limit=10**9, time_limit=None):
        self.collect = collect
        self.sol_limit = sol_limit
        for c in range(self.C):
            if self.cons_target[c] <= 0:
                continue
            if self.openct[c] < self.cons_target[c]:
                return False
        if time_limit:
            self.deadline = time.time() + time_limit
        try:
            return self.dfs()
        except TimeoutError:
            return None

def edges_of(sol_idx, pool):
    return [0b111] + [pool[i] for i in sol_idx]

def diversity(n, edges):
    m = len(edges)
    deg = [0]*n
    for T in edges:
        for v in range(n):
            if (T >> v) & 1:
                deg[v] += 1
    return m - max(deg), m, deg

def is_intersecting(edges):
    for a in range(len(edges)):
        for b in range(a+1, len(edges)):
            if edges[a] & edges[b] == 0:
                return False
    return True

if __name__ == "__main__":
    n = int(sys.argv[1]); t = int(sys.argv[2])
    tl = float(sys.argv[3]) if len(sys.argv) > 3 else None
    s = Solver(n, [t]*n, [0]*n)
    r = s.run(time_limit=tl)
    print("n=", n, "t=", t, "pool=", s.P, "result=", r, "nodes=", s.nodes)
