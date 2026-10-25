# A sharp all-smooth net of plane cubics in characteristic three

## Finding

Over \(k=\mathbf F_3\), the maximum \(k\)-vector-space dimension of a subspace \(W\subset H^0(\mathbf P^2_k,\mathcal O(3))\) for which **every nonzero \(k\)-rational section cuts out a geometrically smooth plane cubic** is exactly **three** (projective linear-system dimension two). An explicit maximal example is \(W=\langle F,G,H\rangle_k\), where

\[
\begin{aligned}
F&=-X^3+XZ^2+Y^2Z,\\
G&=X^3-X^2Z+YZ^2+XY^2,\\
H&=Z^3-X^2Y+Y^2Z-Y^3.
\end{aligned}
\]

All thirteen members indexed by \([a:b:c]\in\mathbf P^2(\mathbf F_3)\) are geometrically smooth plane curves of genus one, and this example is geometrically basepoint-free.

## Assumptions and scope

The coefficient field is \(k=\mathbf F_3\), the ambient plane is \(\mathbf P^2_k\), and \(X,Y,Z\) are homogeneous coordinates. A member is **geometrically smooth** if its base change to an algebraic closure of \(k\) is nonsingular. The all-smooth condition quantifies over the thirteen \(k\)-rational projective coefficient vectors, **not** over all coefficient vectors after extending \(k\). The conclusion concerns plane cubics and does not classify all maximal nets.

## Proof

**Linear independence.** The coefficient of \(XZ^2\) is nonzero only in \(F\); that of \(XY^2\) is nonzero only in \(G\); that of \(Z^3\) is nonzero only in \(H\). Thus \(F,G,H\) are linearly independent over \(k\). The coefficient parameters can be normalized by setting their first nonzero coordinate to one, giving exactly \((3^3-1)/(3-1)=13\) distinct members.

**Algebraic smoothness certificate.** For every normalized \((a,b,c)\), let \(f=aF+bG+cH\). On each standard affine chart \(T=1\) for \(T\in\{X,Y,Z}\), dehomogenize \(f\) and take its two affine partial derivatives. Exact Gröbner-basis division over \(k\), using lexicographic order, gives the **unit ideal** for the three generated polynomials on each chart, for all thirteen members. The script `verify_groebner.py` performs these \(13\times3=39\) certificate computations and asserts the reduced Gröbner basis is \((1)\) in every case. By the weak Nullstellensatz, a unit ideal on each chart excludes singular points over the algebraic closure. Every plane cubic is then geometrically smooth, and, by the plane-curve genus formula, has genus \((3-1)(3-2)/2=1\).

**Geometric basepoint-freeness.** On each affine chart, the dehomogenizations of \(F,G,H\) generate the unit ideal (three further exact Gröbner-basis calculations in `verify_groebner.py`). Thus no geometric point is a simultaneous zero of all three generators.

**Upper bound.** For any rational point \(P\in\mathbf P^2(k)\), first-jet evaluation from a vector space \(U\subset H^0(\mathbf P^2_k,\mathcal O(3))\) maps into the three-dimensional space of value and two affine first derivatives at \(P\). If \(\dim_k U\ge4\), a nonzero element lies in its kernel, hence defines a cubic singular at \(P\). Therefore no all-smooth system has vector dimension exceeding three. The displayed system attains the bound.

## Verification

Run `python verify_groebner.py` with SymPy (exact coefficient modulus three) and `python verify_finite_fields.py` with Python 3. The first program prints `PASS` after all 39 smoothness and 3 base-locus chart checks; its complete deterministic output is `groebner_output.txt`. It additionally enumerates rational points on the thirteen curves and obtains their respective point counts \((4,4,2,3,4,1,4,7,5,6,7,3,2)\) in its listed coefficient order.

The second program does not invoke a Gröbner-basis implementation: it independently evaluates all cubic gradients on every point of the projective planes over \(\mathbf F_3\), \(\mathbf F_9\), and \(\mathbf F_{27}\). This finite-extension test is **exhaustive for plane cubic singularities**, not merely a bounded heuristic: a geometrically integral singular cubic has exactly one singular geometric point (arithmetic genus one), hence a rational singular point; a line-plus-conic cubic has a singular intersection of degree at most two; and a cubic consisting geometrically of lines has a singular point defined over an extension of degree at most three, because Frobenius permutes its at most three distinct lines. Repeated line factors only strengthen the conclusion. Thus any singular cubic over \(\mathbf F_3\) has a singular point over one of these three extensions. The independently computed output is `finite_field_output.txt`.

## Relationship to prior work

Asgarli–Ghioca–Reichstein [1] give a general construction of maximal-dimension all-smooth linear systems provided the ground characteristic does **not** divide \(\gcd(d,n+1)\). At degree \(d=3\), plane dimension \(n=2\), and characteristic three, their hypothesis fails. Their general upper bound remains applicable; the present explicit net supplies attainment in this omitted characteristic and smallest field. Asgarli–Ghioca [2] treat pencils, not maximal nets. Asgarli–Ghioca [3] distinguish geometric irreducibility from geometric smoothness and repeat the maximal smooth plane-cubic existence result with the condition \(p\ne3\); their constructed higher-dimensional systems with irreducible members do not imply smoothness of all thirteen members of a net. The geometric-irreducibility and Galois-orbit results of [4] likewise do not imply this stronger assertion.

## Limitations

The verification concerns the thirteen rational members, not every member over field extensions. It does not classify all all-smooth cubic nets, compute their projective equivalence classes, or assert publication priority over unindexed work. The algebraic proof is independently reproducible but has not been independently audited.

## References

1. Asgarli, Ghioca, Reichstein, Linear families of smooth hypersurfaces over finitely generated fields, arXiv:2207.00918 (2022). https://arxiv.org/abs/2207.00918
2. Asgarli, Ghioca, Smoothness in pencils of hypersurfaces over finite fields, arXiv:2203.07169 (2022). https://arxiv.org/abs/2203.07169
3. Asgarli, Ghioca, Linear system of geometrically irreducible plane cubics over finite fields, arXiv:2407.18104 (first posted 2024-07-25). https://arxiv.org/abs/2407.18104
4. Asgarli, Ghioca, Reichstein, Linear systems of hypersurfaces passing through a Galois orbit, arXiv:2310.10361 (2023). https://arxiv.org/abs/2310.10361
