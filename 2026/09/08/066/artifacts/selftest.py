import sys
sys.path.insert(0, '.')
from hoch import betti_table

# C5: edges 01,12,23,34,40. Known: pd=3, reg(S/I)=2 (Jacques: reg I=3),
# beta_24 = 5 (5 induced 2-path complements), beta_35 = 1 (top C5 class).
n = 5
E5 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
b = betti_table(n, E5, 32003)
print('C5:', sorted(b.items()))
pd = max(i for (i, j) in b if not (i == 0 and j == 0))
reg = max(j - i for (i, j) in b)
print('pd', pd, 'reg', reg)
assert b.get((1, 2)) == 5, 'beta12 must equal #edges'
assert b.get((2, 3)) == 5, 'C5 linear strand beta23=5'
assert b.get((3, 5)) == 1, 'C5 top class'
assert pd == 3 and reg == 2, (pd, reg)
bq = betti_table(n, E5, 32003, rankfn='qq')
assert bq == b, 'Fp vs QQ mismatch on C5'
print('C5 Fp==QQ ok')

# P5 path -> reg = indmatch = 2
Epath = [[0, 1], [1, 2], [2, 3], [3, 4]]
b2 = betti_table(n, Epath, 32003)
pd2 = max(i for (i, j) in b2 if not (i == 0 and j == 0))
reg2 = max(j - i for (i, j) in b2)
print('P5:', sorted(b2.items()))
print('pd', pd2, 'reg', reg2)
assert reg2 == 2, reg2

# K5: I = all 10 quadrics, S/I has reg 1, pd 4 (Eagon-Northcott: linear strand
# beta_i,i+1 = i*C(5,i+1))
EK5 = [[i, j] for i in range(5) for j in range(i + 1, 5)]
bk = betti_table(n, EK5, 32003)
pdk = max(i for (i, j) in bk if not (i == 0 and j == 0))
regk = max(j - i for (i, j) in bk)
print('K5:', sorted(bk.items()))
print('pd', pdk, 'reg', regk)
assert regk == 1 and pdk == 4, (pdk, regk)
assert bk.get((1, 2)) == 10, bk
print('K5 linear resolution ok; alternating total-Betti sum =',
      sum((1 if i % 2 == 0 else -1) * v for (i, j), v in bk.items()))

# C7: reg(S/I) = floor((7+1)/3) = 2
E7 = [[i, (i + 1) % 7] for i in range(7)]
b7 = betti_table(7, E7, 32003)
pd7 = max(i for (i, j) in b7 if not (i == 0 and j == 0))
reg7 = max(j - i for (i, j) in b7)
print('C7:', sorted(b7.items()))
print('pd', pd7, 'reg', reg7)
assert reg7 == 2, reg7
eul = sum((1 if i % 2 == 0 else -1) * v for (i, j), v in b7.items())
assert eul == 0, eul  # alternating total-Betti sum vanishes (I != 0)
b7q = betti_table(7, E7, 32003, rankfn='qq')
assert b7q == b7, 'Fp vs QQ mismatch on C7'
print('SELFTEST OK')
