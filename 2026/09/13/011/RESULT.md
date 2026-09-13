# Disproof of SF6: no forward-closed expanding cube droplet for forward-2 bootstrap on the 6D torus

## Context

The admitted target SF6 concerns the 6-dimensional torus T_n^6 = (Z/nZ)^6 with the forward-2 rule: a healthy vertex x becomes infected iff at least 2 of its 6 forward neighbours x+e_1,...,x+e_6 are already infected (infected stay infected; initial set i.i.d. Bernoulli(p)). SF6 is a conjunction of (1) a two-sided sharp window: explicit 0 < f_minus < f_plus with f_plus/f_minus <= 1.25 and f_minus > lam_std(6,2) such that P_p(full percolation) -> 0 when p (log n)^5 <= f_minus and -> 1 when p (log n)^5 >= f_plus as n -> infinity; and (2) a forward-droplet mechanism: an explicitly specified forward-closed droplet cube of side s(n) = floor(F log n) for explicit F > 0 (closed under forward steps, expanding deterministically layer-by-layer in the +e_i directions) covers T_n^6 with conditional probability >= 1 - n^{-2} above the window while absent w.h.p. below it, with directed isoperimetric cost matching the window. Scope: fixed d = 6, n -> infinity, p = p(n) -> 0. A complete TARGET resolution is a rigorous proof of the full conjunction or a rigorous disproof via an explicit infinite violating sequence.

## Definitions

Cube: C(c,s) = { x : for all i, (x_i - c_i) mod n < s }, 0 <= s <= n, so |C| = s^6; empty iff s = 0, proper nonempty iff 1 <= s <= n-1. Forward-closed: S satisfies x in S ==> x + e_i in S for every i. Bootstrap closure [C]: the set obtained by iterating the forward-2 rule starting from C alone. Sterile: [C] = C (zero deterministic growth).

## Result

Theorem (TARGET disproof of SF6). For every explicit F > 0, with s(n) = floor(F log n), no side-s(n) cube droplet on T_n^6 satisfies the conjoined SF6 droplet specification for all large n. Hence the full SF6 conjunction is false, deterministically and uniformly in p, along every sequence n_k -> infinity (e.g. n_k = k with arbitrary p_k, e.g. p_k = 1/2). The probabilistic window clause is untouched: refuting one conjunct refutes the conjunction.

Lemma A. The only forward-closed subsets of T_n^6 are empty and the full torus. Hence every side-s cube with 1 <= s <= n-1 is not forward-closed.

Lemma B (sterility). Let 1 <= s <= n-1 and C = C(c,s). No vertex outside C has >= 2 forward neighbours in C. Hence C gains zero vertices in one forward-2 step and [C] = C: no deterministic layer-by-layer expansion whatsoever.

## Proof / evidence

Lemma A proof: the forward orbit of any x, {x + (a_1,...,a_6)} with all a_i >= 0, is the whole torus since each coordinate reaches every residue by repeated +1 steps mod n. A nonempty forward-closed set contains a full orbit, hence equals T_n^6. Explicit cube witness: v = c + (s-1,...,s-1) lies in C but v + e_1 has first coordinate c_1 + s (mod n), outside [c_1, c_1+s), so v + e_1 is not in C. The s = 0 droplet is vacuously closed but covers nothing.

Lemma B proof: let x not in C and M(x) = { j : (x_j - c_j) mod n >= s }, nonempty. For y = x + e_i to lie in C every coordinate must lie in its interval. If |M(x)| >= 2, for each j in M(x) with j != i coordinate j is unchanged and still missed, so x + e_i is not in C for every i (zero forward neighbours in C). If M(x) = {j}, for every i != j coordinate j is still missed, so only x + e_j can possibly lie in C; hence at most one forward neighbour in C. In all cases x has <= 1 < 2 forward neighbours in C, so the rule never infects outside C from C alone; induction gives [C] = C. This covers wrapped corners and the singleton case.

Side-length bound: for fixed F > 0, s(n) = floor(F log n) < n for all large n since log n <= 2 sqrt(n), so F log n < n when n > 4F^2; take N_0(F) = max(2, ceil(4F^2)+1); also s(n) >= 1 once n > e^{1/F}. So every candidate droplet is eventually empty or a proper cube, never the full torus.

SF6 refutation: fix F > 0, n >= N_0(F). If s(n) = 0 the droplet is empty (expands to nothing, covers nothing, and being always present cannot be absent w.h.p. below the window). If 1 <= s(n) <= n-1, Lemma A gives non-closedness and Lemma B gives [C] = C != T_n^6: the required first deterministic layer is empty, so conditional covering via that mechanism is 0, not >= 1 - n^{-2}. Thus no tuple (f_minus, f_plus, F) satisfies the full specification. Computational confirmation: output/artifacts/verify_droplet_lemmas.py brute-forces the torus and confirms forward orbits equal the full torus and zero growers (max <= 1 forward neighbour outside) for cubes (d=6,n=5,s=3) at unwrapped and wrapped corners, (6,4,2), (6,3,1) singleton, and (2,6,2); all checks pass. The argument in fact works for every d >= 2 and r >= 2.

## Limitations

Fixed d = 6, n -> infinity per target scope. The disproof targets the SF6 conjunction via its droplet clause and makes no claim about the true critical window or scaling of forward-2 percolation alone. Cube means the standard product-of-intervals droplet; every translated/wrapped placement is covered.

## Reproducibility

Run `python3 output/artifacts/verify_droplet_lemmas.py` with Python 3 and no extra dependencies; expected output reports |T|, |C|, max_forward_nbrs_outside = 1, growers = 0 for each case and ends with ALL CHECKS PASSED.

## References

J. Balogh, B. Bollobas, R. Morris, Bootstrap percolation in three dimensions, Ann. Probab. 2009; Bootstrap percolation in high dimensions, arXiv:0907.3097. H. Duminil-Copin, R. Morris, The sharp threshold for bootstrap percolation in all dimensions, Trans. AMS. A. Holroyd, Sharp metastability threshold for 2D bootstrap percolation, Probab. Theory Relat. Fields 2003. J. Gravner, A. Holroyd, R. Morris, A sharper threshold for bootstrap percolation in two dimensions. R. Cerf, E. Cirillo, Finite size scaling in 3D bootstrap percolation. I. Hartarsky, U-bootstrap percolation: critical probability, Ann. Inst. Henri Poincare 2021.
