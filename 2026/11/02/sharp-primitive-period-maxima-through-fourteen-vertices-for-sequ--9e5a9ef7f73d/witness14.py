#!/usr/bin/env python3
"""Independent direct 106-step witness replay; standard library only."""
N = 14
EDGES = ((0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(2,7),(2,8),
         (3,9),(3,10),(5,11),(6,12),(11,13))


def step(state):
    for v in range(N):
        k = sum((state >> w) & 1 for a,b in EDGES for w in (
            ([b] if a==v else [a] if b==v else [])))
        current = (state >> v) & 1
        if current == 0 and k >= 1: state |= 1 << v
        elif current == 1 and k < 2: state &= ~(1 << v)
    return state


def main():
    start = 4
    orbit = []
    state = start
    while state not in orbit:
        orbit.append(state)
        state = step(state)
    assert state == start and len(orbit) == 106, (state, len(orbit))
    with open('witness14_trace.txt','w',encoding='ascii') as f:
        f.write('n=14, one sweep is vertices 0..13, up=1, down=3, closed neighborhood\n')
        f.write('tree_edges=' + repr(EDGES) + '\n')
        for i, val in enumerate(orbit): f.write(f'{i:03d} {val:05d} {val:014b}\n')
        f.write(f'106 {state:05d} {state:014b} return\n')
    print('WITNESS14_OK: 106 distinct states, exact return at time 106')

if __name__=='__main__':main()
