"""Invariant table for all 51 order-32 reps. Quick: no Aut enumeration."""
import numpy as np, sys, pickle, json, time
sys.path.insert(0, '.')
import toolkit as K

d = pickle.load(open('reps32.pkl', 'rb'))
Ts = [np.array(T, dtype=int) for T, s in d]
assert len(Ts) == 51
rows = []
t0 = time.time()
for k, T in enumerate(Ts):
    n = T.shape[0]
    assert n == 32
    e = K.find_identity(T)
    inv = K.inverses(T, e)
    ab = K.is_abelian(T)
    Z = K.center(T, e)
    gd = K.derived_order(T, e, inv)
    cl = 1 if ab else K.nilpotency_class(T, e, inv)
    fr, phisize = K.frattini_rank(T, e, inv)
    ords = K.el_orders(T, e, inv)
    prof = {str(int(o)): int(np.sum(ords == o)) for o in sorted(set(ords.tolist()))}
    # gamma3 and class-2 quotient derived size
    if ab or cl <= 2:
        g3size, qd = 1, gd
    else:
        S = K.lower_central_series(T, e, inv)
        g3 = S[2]
        g3size = len(g3)
        # quotient Q=G/g3 mult on cosets; derived size of Q
        Sg = set(g3.tolist())
        reps, seen = [], set()
        for a in range(n):
            if a in seen:
                continue
            reps.append(a)
            for s in Sg:
                seen.add(int(T[a, s]))
        rix = {r: i for i, r in enumerate(reps)}
        def qr(a):
            for r in reps:
                if int(T[int(inv[a]), r]) in Sg:
                    return rix[r]
            raise ValueError
        m = len(reps)
        Q = np.zeros((m, m), dtype=int)
        for i, a in enumerate(reps):
            for j, b in enumerate(reps):
                Q[i, j] = qr(int(T[a, b]))
        eq = K.find_identity(Q)
        invq = K.inverses(Q, eq)
        qd = K.derived_order(Q, eq, invq)
    rows.append(dict(idx=k, abelian=bool(ab), klass=int(cl), derived=int(gd),
                     center=int(len(Z)), frat_rank=int(fr), phi_size=int(phisize),
                     order_profile=prof, gamma3_size=int(g3size),
                     class2quot_derived=int(qd)))
    print(k, 'ab' if ab else 'na', cl, gd, len(Z), fr, g3size, qd, flush=True)
print('TABLE_TIME', round(time.time() - t0, 1))
json.dump(rows, open('table.json', 'w'), indent=0)
from collections import Counter
print('class:', Counter(r['klass'] for r in rows))
print('derived:', Counter(r['derived'] for r in rows))
print('center:', Counter(r['center'] for r in rows))
print('frat:', Counter(r['frat_rank'] for r in rows))
print('abelian:', sum(1 for r in rows if r['abelian']))
print('TABLE_DONE')
