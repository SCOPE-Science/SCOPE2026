# Twenty points in the 12x12 lattice with all triangle areas >= 1.0: a grid-restricted Heilbronn record

## Context
The Heilbronn triangle problem asks for the maximum minimal triangle area among n points in a region. Continuous optima in the unit square are proved only to n=9 and tabulated heuristically to n~35 (Friedman), with asymptotic upper bounds (Cohen-Pohoata-Zakharov improving Komlos-Pintz-Szemeredi) for large n. The lattice-restricted variant on small grids is exactly checkable by integer arithmetic but has no published minimal-determinant >=2 table for 12x12 at n~20. The no-three-in-line problem (Prellberg: 2n collinear-free points for n<=60, so 24 points on 12x12) forbids only zero area (det==0) and does not address unimodular area-0.5 triangles (det==1). By Pick-type quantization all lattice triangle areas lie in 0.5*Z, so eliminating both det==0 and det==1 (doubled area D>=2) is the first structural step above collinear-free.

## Definitions
Let G12 = {0,...,11}^2 (144 lattice points). For distinct p,q,r in G12 define doubled area D(p,q,r) = |det(q-p, r-p)| in Z>=0 (exact integer; Euclidean area = D/2). For S subset G12, |S|=20, define D(S) = min over C(20,3)=1140 triples, A(S)=D(S)/2, M(12,20)=max_{|S|=20} A(S). Define H(S) = size of largest T subset S in strictly convex position with no point of S strictly inside conv(T) (empty convex subset; vertices in S).

## Result
**Theorem (lower-bound configuration). M(12,20) >= 1.0.** Witness S* (20 points):
```
0 1
0 3
1 7
1 10
2 0
2 3
3 6
3 9
4 0
4 2
7 9
7 11
8 2
8 5
9 8
9 11
10 1
10 4
11 8
11 10
```
Exact audit over all 1140 triples: **D(S*) = 2, A = 1.0, #det==0 = 0, #det==1 = 0, #det==2 = 34, #det==3 = 42.** Hence no three collinear and no area-0.5 triangle. This beats parabola/Prellberg-type collinear-free baselines which achieve only D=1 (e.g. parabola mod 11 has six det==1 triples; random 20-sets have 10-30 collinear and 16-34 unimodular triples). This is existence (lower bound); optimality and D>=3 remain open.

Secondary: **H(S*) = 6**, witness {(0,1),(0,3),(1,7),(2,3),(3,6),(3,9)} (6 hull vertices, verified empty). No empty convex 7-set exists (exhaustive over C(20,7)=77520), hence no larger empty convex set by monotonicity.

## Proof / Evidence
Enumeration with Python integers (no floats). For each of 1140 index triples i<j<k compute a=|(xj-xi)*(yk-yi)-(xk-xi)*(yj-yi)|; track minimum and counts n0 (#a==0), n1 (#a==1), c2 (#a==2), c3 (#a==3). Range/duplicates checked: all points in {0..11}^2, 20 distinct. Two independent expression orders agree (shoelace difference form and matrix form qx*(ry-py)+rx*(py-qy)+px*(qy-ry)); auditor re-executed both plus full histogram. Rerun `python3 output/artifacts/verify_S_star.py output/artifacts/S_star.txt` gives `n=20 total_triples=1140 D=2 A=1.0 n0=0 n1=0 c2=34 c3=42; PASS` in ~0.014 s plus hist_0_10 {0:0,1:0,2:34,3:42,4:36,5:4,6:44,7:10,8:38,9:18,10:46}.

Full exact histogram (doubled area:count): 2:34 3:42 4:36 5:4 6:44 7:10 8:38 9:18 10:46 11:8 12:26 13:18 14:28 15:18 16:42 17:14 18:36 19:22 20:22 21:22 22:28 23:18 24:26 25:8 26:20 27:22 28:16 29:18 30:14 31:20 32:10 33:12 34:22 35:4 36:16 37:22 38:6 39:14 40:4 41:24 42:8 43:14 44:18 45:10 46:6 47:20 48:2 49:6 50:6 51:8 52:10 53:10 54:12 55:12 56:2 57:20 58:6 59:10 60:6 61:8 62:2 63:4 65:2 66:2 67:4 68:8 69:2 70:4 71:14 72:6 73:8 74:6 78:2 79:2 80:4 81:4 83:2 84:2 87:2 90:4 92:2 94:2 98:2 100:4; total 1140, min 2, max 100. (Corrects DRAFT tail beyond det=10 which listed 11:15/12:53/max109-scale from a different seed set.)

H certificate: since D>=2 no three of S* collinear, strict convexity is equivalent to |hull(T)|=|T| and no S*-point lies on a hull edge (would be collinear). Exhaustive descending check with exact orientation predicates (sign of det) rules out all 7-sets; witness above shows 6 attainable. Monotonicity: any empty convex k>7 contains an empty convex 7-subset (subsets of strictly convex sets are strictly convex; conv(subset) subset conv(parent) contains no S-point), so H<=6.

Search (existence route, not part of proof): simulated annealing with pure lexicographic objective (n0,n1), cost=n0*1e6+n1*1e3, single-point relocation (~171 triples recomputed per move), geometric cooling T0=1.5->T1=0.01 over 60000 steps/seed; best-improvement single-swap polish. Pure (n0,n1) found D>=2 in 5/96 seeds (seeds 6,11,26,124,151) at ~0.5 s each; seed-11 chosen as S* (fewest det-2 triples, 34). Methodological note: including c2/c3 penalties trapped ILS at (0,1) local optimum (60 iters x8 workers, never escaped).

## Limitations
- Existence/lower bound only; no upper bound on M(12,20); D>=3 open (32-seed probe minimizing (n0,n1,c2) found none; distance >=34 det-2 triples).
- Stochastic search is not non-existence proof; per-cell best-found gaps are not lower bounds on minima.
- H certificate is exhaustive conditional on orientation-predicate code; witness independently rechecked by two implementations.
- Originality scope: explicit verifiable configuration + benchmark only; no general theorem about all n,m.

## Reproducibility
Artifacts: `output/artifacts/S_star.txt` (coordinates, one 'x y' per line), `output/artifacts/verify_S_star.py` (one-file verifier). Command: `python3 output/artifacts/verify_S_star.py output/artifacts/S_star.txt` (<1 s, deterministic; seeded RNG affects only search, not verification). Total search compute <2 h laptop-class CPU per draft logs (search scripts/sweep JSONs not required to recheck S*).

## References
- E. Friedman, The Heilbronn Problem for Squares (continuous configurations to n~35, proved to n=9) — https://erich-friedman.github.io/packing/heilbronn/
- T. Prellberg, Constraint Satisfaction Programming for the No-three-in-line Problem (2n points for n<=60) — https://arxiv.org/abs/2602.07751v1
- A. Cohen, C. Pohoata, D. Zakharov, A new upper bound for the Heilbronn triangle problem (2023) — https://arxiv.org/abs/2305.18253v1
- Empty pentagon/hexagon and large convex holes in random sets — https://arxiv.org/abs/1111.5656v1
