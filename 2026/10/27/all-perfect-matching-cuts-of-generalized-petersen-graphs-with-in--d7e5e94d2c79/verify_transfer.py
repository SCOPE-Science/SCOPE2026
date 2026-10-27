"""Exact finite-state certificate for balanced perfect 2-colorings of GP(n,2).

A column records the two binary colors (outer in bit 0, inner in bit 1).
An arc shifts a four-column window and enforces both local degree rules
at the middle column of the resulting five-column window.
"""


def valid_five(cols):
    outer = [c & 1 for c in cols]
    inner = [(c >> 1) & 1 for c in cols]
    x = int(outer[1] != outer[2]) + int(outer[3] != outer[2]) + int(inner[2] != outer[2])
    y = int(inner[0] != inner[2]) + int(inner[4] != inner[2]) + int(outer[2] != inner[2])
    return x == y == 1


adj = []
for state in range(256):
    cols = [(state >> (2 * j)) & 3 for j in range(4)]
    dest = []
    for last in range(4):
        if valid_five(cols + [last]):
            dest.append((state >> 2) | (last << 6))
    adj.append(tuple(dest))
assert sum(map(len, adj)) == 160

# Elementary Tarjan strongly connected components: no third-party library.
count = 0
low = [-1] * 256
entry = [-1] * 256
on_stack = [False] * 256
stack = []
components = []


def visit(v):
    global count
    entry[v] = low[v] = count
    count += 1
    stack.append(v)
    on_stack[v] = True
    for w in adj[v]:
        if entry[w] < 0:
            visit(w)
            low[v] = min(low[v], low[w])
        elif on_stack[w]:
            low[v] = min(low[v], entry[w])
    if low[v] == entry[v]:
        component = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            if w == v:
                break
        components.append(tuple(sorted(component)))


for v in range(256):
    if entry[v] < 0:
        visit(v)
assert sum(map(len, components)) == 256
cyclic = []
for comp in components:
    if len(comp) > 1 or comp[0] in adj[comp[0]]:
        cyclic.append(comp)
cyclic.sort(key=lambda c: (len(c), c))
expected = [(85,), (170,), (13, 55, 112, 195, 220), (35, 60, 143, 200, 242)]
expected.sort(key=lambda c: (len(c), c))
assert cyclic == expected, (cyclic, expected)
for comp in cyclic:
    inside = set(comp)
    assert all(sum(w in inside for w in adj[v]) == 1 for v in comp)
    assert all(sum(v in adj[w] for w in comp) == 1 for v in comp)
print('states=256 arcs=160 cyclic_scc_sizes=1,1,5,5')
print('cyclic_state_sets=' + str(cyclic))
for n in list(range(5, 31)) + [35, 50, 100, 101]:
    num = sum(len(comp) for comp in cyclic if n % len(comp) == 0)
    assert num == 2 + (10 if n % 5 == 0 else 0)
    print(f'n={n} labeled_colorings={num} matching_cut_edge_sets={num // 2}')
print('TRANSFER_VERIFIED')
