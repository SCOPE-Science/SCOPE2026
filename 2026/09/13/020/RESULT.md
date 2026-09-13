# Abnormal corank 3, degenerate Goh matrix, and normal-abnormal status of the X1-line in the free rank-2 step-4 Carnot group

## Context

Let H be the free step-4 rank-2 Carnot group: the simply connected 8-dimensional nilpotent Lie group with growth vector (2,3,5,8), left-invariant distribution D = span{X1, X2} declared orthonormal. Let gamma*(t) = exp(t X1), 0 <= t <= 1, from the identity with constant control u* = (1,0). Let E be the L^2 endpoint map. The admitted target conjunction asserted: (i) gamma* is abnormal; (ii) dE at u* has corank exactly 1; (iii) the Goh second-order matrix has the stated rank defect; (iv) this Goh-rank witness certifies short-time length minimality up to an explicit T* > 0. Route (b) allows instead exhibiting a normal lift of gamma* or an explicit strictly shorter competitor.

## Definitions

Free rank-2 step-4 Lie algebra h: Witt homogeneous dimensions 2, 1, 2, 3 (sum 8). Hall basis: weight 1: X1, X2; weight 2: X12 = [X1,X2]; weight 3: X112 = [X1,X12], X212 = [X2,X12]; weight 4: X1112 = [X1,X112], X2112 = [X2,X112] = [X1,X212] (Jacobi), X2212 = [X2,X212]. Endpoint-map image formula: Im(dE_{u*}) = span_{s in [0,1]} {Ad_{gamma*(s)} X1, Ad_{gamma*(s)} X2}. Abnormal means dE singular; corank = 8 - dim(Im dE). Abnormal-lift space is the annihilator of Im(dE). In rank 2 the Goh second-order matrix is the 1x1 skew matrix [G(t)] with G(t) = p(t)([X1,X2]). Normal lift means covector p0 with multiplier nu = -1 whose Hamiltonian controls reproduce u*.

## Result

In the free step-4 rank-2 Carnot group, gamma*(t) = exp(t X1) is abnormal but dE at control (1,0) has corank exactly 3, not 1: its image is span{X1, X2, X12, X112, X1112}. Every abnormal lift has vanishing Goh matrix (rank 0), so no Goh-rank witness certifies minimality; moreover gamma* admits the explicit normal lift p0 = X1^* giving (H1,H2) = (1,0), hence is normal-abnormal (not strictly abnormal). The target conjunction as stated is therefore DISPROVED via sanctioned route (b).

## Proof / evidence

ad_X1 acts by X2 -> X12 -> X112 -> X1112 -> 0, X212 -> X2112 -> 0, with ad_X1^4 = 0 (step 4). Hence Ad_{exp(sX1)} = e^{s ad_X1} gives Ad X1 = X1 and Ad X2 = X2 + s X12 + (s^2/2) X112 + (s^3/6) X1112. Sampling s = 0, 1/3, 2/3, 1 yields a Vandermonde system in {X2, X12, X112, X1112}; with X1 the span is exactly the 5-dimensional space above, so corank = 8 - 5 = 3. Verified in exact rational arithmetic (sympy asserts rank 5 and vanishing X212/X2112/X2212 columns). The annihilator is 3-dimensional (duals to X212, X2112, X2212), so clause (i) holds. For every annihilator vector, p(t)(X1) = p(t)(X2) = 0 and G(t) = p(t)(X12) = 0 identically because Ad_{exp(-tX1)} X12 = X12 - t X112 + (t^2/2) X1112 stays in the image. Hence the Goh matrix is the zero matrix of rank 0 along every abnormal lift; clauses (iii)-(iv) fail. With p0 = X1^*, H1(t) = p0(Ad_{exp(-tX1)} X1) = 1 and H2(t) = p0(X2 - t X12 + (t^2/2) X112 - (t^3/6) X1112) = 0, so normal Hamiltonian maximization gives u = (1,0) = u*. This is the sanctioned route-(b) normal lift; gamma* is normal-abnormal, not strictly abnormal.

## Limitations

Minimality or non-minimality of gamma* itself is not decided: no strictly shorter competitor is exhibited or needed for this route-(b) disproof, and short-time minimality via the normal lift is left open. Correctness rests on the Hall-basis/Jacobi presentation and standard endpoint-map/Adjoint formulas; sign conventions (e.g. [X1,X2] vs [X2,X1]) should be checked by the reader but do not change dimensions. No claim about uniformity of T* or other Carnot groups.

## Reproducibility

Run `python3 verify_corank_goh.py` (exact rational sympy, no numerics): asserts image rank 5 / corank 3 with vanishing columns 4, 6, 7; nullspace dimension 3 with H1 = H2 = Goh = 0 on each basis vector; normal lift H1 = 1, H2 = 0. Expected log in run_output.txt.

## References

- E. Le Donne, G. Leonardi, R. Monti, D. Vittone, Extremal curves in nilpotent Lie groups, arXiv:1207.3985 (abnormal varieties, corank, Goh condition, adjoint integration).
- Y. Sachkov, Sub-Riemannian geodesics on the free Carnot group with growth vector (2,3,5,8), arXiv:1404.7752 (models, product rule, PMP Sec. 4 abnormal/normal systems).
- Yu. L. Sachkov, E. F. Sachkova, The structure of abnormal extremals in a sub-Riemannian problem with growth vector (2,3,5,8), Sbornik: Mathematics 211(10):1460-1485 (2020).
- L. Rifford, Sub-Riemannian Geometry and Optimal Transport (PMP/adjoint background); A. Agrachev, D. Barilari, U. Boscain, Comprehensive Introduction to Sub-Riemannian Geometry (endpoint map, Goh conditions).
