from collections import defaultdict

def allocation(q, a, n, protected):
    protected = set(protected)
    assert len(protected) == a
    marks = [None] * n
    for symbol, user in enumerate(sorted(protected)):
        marks[user] = symbol
    remaining = [u for u in range(n) if u not in protected]
    assert len(remaining) == a * (q - a)
    for k in range(q - a):
        for u in remaining[k*a:(k+1)*a]:
            marks[u] = a + k
    return tuple(marks)

def classes(marks):
    out = defaultdict(list)
    for u, x in enumerate(marks):
        out[x].append(u)
    return {x: tuple(us) for x, us in out.items()}

def verify(q, a, horizon=6):
    n = a * (q - a + 1)
    first = allocation(q, a, n, range(a))
    states = [(first, None, None)]
    # Each state stores the current allocation and the previous allocation/broadcast.
    for _ in range(horizon):
        nxt_states = []
        for marks, prev_marks, prev_x in states:
            C = classes(marks)
            valid = [x for x, us in C.items() if len(us) >= 2]
            for x in valid:
                if prev_marks is not None:
                    for u in range(n):
                        assert not (prev_marks[u] == prev_x and marks[u] == x)
                nxt = allocation(q, a, n, C[x])
                nxt_states.append((nxt, marks, x))
        states = nxt_states
    return True

if __name__ == "__main__":
    for q in range(2, 7):
        for a in range(1, q):
            n = a * (q - a + 1)
            verify(q, a)
            print(f"q={q} a={a} n={n}: PASS")
