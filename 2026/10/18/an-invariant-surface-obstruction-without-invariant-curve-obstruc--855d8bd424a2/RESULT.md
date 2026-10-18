# An invariant-surface obstruction without invariant-curve obstructions in non-projective toric threefolds

## Finding
For every integer \(a\geq4\), let \(X_a=Z''_{13}(a,2,0,0)\) be the smooth complete toric threefold with rays and maximal cones specified below. Then \(X_a\) is non-projective and

1. \(K_{X_a}\cdot B\ne0\) for **every torus-invariant irreducible curve** \(B\subset X_a\);
2. the torus-invariant surface \(S=V(\rho_7)\) is \(\operatorname{Bl}_{p}(\mathbb P^1\times\mathbb P^1)\), and with the standard pullback ruling classes \(F_1,F_2\) and exceptional curve \(E\),
   \[(-K_{X_a})|_S\equiv F_1+2F_2-3E;\]
3. the strict transform \(C\subset S\) of a general irreducible bidegree-\((1,1)\) curve through \(p\) is **not torus invariant** and has \(K_{X_a}\cdot C=0\);
4. the canonical bundle \(\omega_{X_a}\) is not tensor-generating, with an obstructing invariant surface but no obstructing invariant curve.

This gives infinitely many non-projective examples answering negatively the invariant-curve-only possibility raised in Question 6.6 of Ito–Zeng–Zeng. The general phenomenon of non-invariant degree-zero curves is not new; the contribution is its explicit occurrence uniformly in this four-parameter toric construction while all eighteen invariant-curve tests pass.

## Assumptions and scope
Work over \(\mathbb C\), and let \(a\in\mathbb Z\) satisfy \(a\geq4\). Write \(N=\mathbb Z^3\). The eight primitive ray generators of \(\Sigma_a\) are
\[
\begin{aligned}
v_1&=(1,1,2),&v_2&=(1,0,0),&v_3&=(0,-1,0),&v_4&=(0,0,-1),\\
v_5&=(-1,a,0),&v_6&=(0,1,0),&v_7&=(0,0,1),&v_8&=(-1,0,1).
\end{aligned}
\]
Its twelve maximal cones, denoted by their ray indices, are
\[
124,\ 234,\ 345,\ 456,\ 146,\ 167,\ 127,\ 237,\ 358,\ 568,\ 378,\ 678.
\]
These are the rays and cones of Construction 6.1 in Ito–Zeng–Zeng at \((a,b,c,d)=(a,2,0,0)\). Their Remark 6.2 establishes that these data give a smooth complete toric variety for all integral parameters, non-projective when \(b\ne0\) and \(a\ne c\), as here. The same conclusions may be obtained from the unimodular cone determinants and the known fan construction.

For a two-cone \(\tau=\operatorname{cone}(v_i,v_j)\), write \(V(ij)\) for its invariant rational curve. The integer \((-K_{X_a})\cdot V(ij)\) is the corresponding anticanonical degree. The criterion for tensor-generation used below is Theorem 4.4 of Ito–Zeng–Zeng: on a proper toric variety, a line bundle is not tensor-generating if and only if some irreducible complete curve has degree zero against it.

## Proof
**1. Every invariant curve has nonzero canonical degree.** Each two-cone \(ij\) belongs to two maximal cones \(ijk\) and \(ijl\). The unique primitive wall relation is
\[v_k+v_l+\alpha v_i+\beta v_j=0,\]
where \(\alpha,\beta\in\mathbb Z\) because adjacent triples are unimodular. The standard smooth-toric wall-intersection formula gives
\[(-K_{X_a})\cdot V(ij)=2+\alpha+\beta.\]
Substitution of the eight rays yields the complete eighteen-wall table:

| Wall \(ij\) | Anticanonical degree | Wall \(ij\) | Anticanonical degree |
|:--:|:--:|:--:|:--:|
| \(12\) | \(2\) | \(14\) | \(-1\) |
| \(16\) | \(2\) | \(17\) | \(3\) |
| \(23\) | \(2\) | \(24\) | \(3\) |
| \(27\) | \(-1\) | \(34\) | \(a+2\) |
| \(35\) | \(1-a\) | \(37\) | \(1\) |
| \(38\) | \(a+1\) | \(45\) | \(2\) |
| \(46\) | \(3-a\) | \(56\) | \(a+1\) |
| \(58\) | \(2\) | \(67\) | \(-2\) |
| \(68\) | \(1-a\) | \(78\) | \(2\) |

For every integer \(a\geq4\), no table entry is zero. Every torus-invariant irreducible curve corresponds to one of these walls, proving assertion 1.

**2. Identify an invariant surface.** Let \(S=V(\rho_7)\). The star fan of \(\rho_7\) lives in \(N/\mathbb Z v_7\cong\mathbb Z^2\); its cyclically ordered primitive rays are
\[(1,1),\quad(1,0),\quad(0,-1),\quad(-1,0),\quad(0,1).\]
The ray \((1,1)\) subdivides the cone spanned by \((1,0)\) and \((0,1)\) in the fan of \(\mathbb P^1\times\mathbb P^1\). Hence \(S\) is its toric blow-up at the fixed point \(p\). Let \(F_1,F_2\) be pullbacks of the two ruling-divisor classes, numbered so that \(F_1\) is the class of the boundary curve associated with \(v_8\) and \(F_2\) the class associated with \(v_3\). Let \(E\) be the exceptional curve associated with \(v_1\). The intersection products are
\[F_1^2=F_2^2=0,\quad F_1\cdot F_2=1,\quad E^2=-1,\quad F_1\cdot E=F_2\cdot E=0.\]

Put \(L=(-K_{X_a})|_S\). The boundary curves \(F_1,F_2,E\) are the threefold's \(V(78),V(37),V(17)\), so the wall table gives
\[L\cdot F_1=2,\qquad L\cdot F_2=1,\qquad L\cdot E=3.\]
These degrees determine the numerical class \(L\equiv F_1+2F_2-3E\). On this smooth rational toric surface, numerical and integral Picard equivalence coincide, so this is also a linear equivalence. This proves assertion 2.

**3. A non-invariant degree-zero curve.** A general bidegree-\((1,1)\) curve \(C_0\subset\mathbb P^1\times\mathbb P^1\) passing through \(p\) is smooth and irreducible. Its strict transform \(C\subset S\) has class
\[[C]=F_1+F_2-E.\]
It is not torus invariant (a general bidegree-\((1,1)\) curve is not an invariant boundary component). Direct intersection gives
\[
(-K_{X_a})\cdot C=L\cdot C=2+1-3=0,
\]
and hence \(K_{X_a}\cdot C=0\). The toric derived Kleiman criterion quoted above implies that \(\omega_{X_a}\) is not tensor-generating, proving assertions 3–4.

**4. The invariant surface is genuinely obstructing.** In local coordinates \((s,t)\) at \(p\), sections of \(mL\), for any positive integer \(m\), are bihomogeneous polynomials of bidegree \((m,2m)\) vanishing to order at least \(3m\) at \(p\). Every monomial has local total degree at most \(3m\), with equality only for \(s^m t^{2m}\). Consequently,
\[h^0(S,mL)=1\quad\text{for every }m\ge1.\]
Likewise \(h^0(S,-mL)=0\) because the pushforward under the blow-down would have negative bidegree. Thus neither \(L\) nor \(-L\) is big; \(S\) is an obstructing invariant subvariety even though none of the eighteen invariant curves obstructs. Equivalently, the hyperplane criterion fails at \(\rho_7\), since
\[v_7=(v_1+v_3+v_8)/3,\]
and all three rays on the right share maximal cones with \(\rho_7\). This finishes the proof.

## Verification
The attached `verify.py` is a standalone Python standard-library checker. It reconstructs the eighteen walls from the twelve maximal cones, computes integer wall relations by exact three-by-three determinants, and checks the displayed formulas against actual ray coordinates for \(56\) integral values of \(a\). It separately tests large positive parameter values, the star fan and convex-combination witness, the surface intersection-degree identity, and the monomial count underlying \(h^0(S,mL)=1\) for \(1\le m\le30\). Its success message starts `VERIFY_OK`.

The universal statements for all \(a\ge4\) and all positive \(m\) are proved by the symbolic wall formulas, the fan computation, and the bidegree argument; finite checks are not used as proofs of these quantified statements.

## Relationship to prior work
Ito–Zeng–Zeng (2026), Theorem 4.4 and Corollary 3.6, give the general derived curve criterion and toric fan hyperplane test. Their Construction 6.1 supplies these fans, Theorems 6.3 and 6.4 solve two **different** one-parameter subfamilies where the obstructions, when present, occur along invariant curves; Question 6.6 asks about the full family and specifically whether all obstructions are of that invariant-curve type. Their Example 4.5 already shows on \(\mathbb P^1\times\mathbb P^1\) that an arbitrary line bundle can have a non-invariant degree-zero curve despite having nonzero degree on every invariant curve. Their Remark 7.6 gives a general toric threefold construction of higher-dimensional obstructions. None of those statements supplies the above infinite, non-projective **canonical-bundle** subfamily in \(Z''_{13}\) with its exact wall table, restricted divisor, and explicit obstructing curve.

Fujino–Sato (2024) studied projectivity and birational properties of the same four-parameter fan construction. Their projectivity criterion, cited in Ito–Zeng–Zeng's Remark 6.2, implies non-projectivity here. No priority is claimed for the fan definition, the projectivity criterion, the general tensor-generation criteria, or the general possibility of non-invariant obstruction curves.

## Limitations
This is a negative answer to the invariant-curve-only part of Question 6.6, **not** a classification of tensor-generating parameter quadruples. The explicit curve \(C\) depends on a general choice and need not be preserved by the big torus. Nothing is asserted about Fourier–Mukai partners, autoequivalence groups, or whether other varieties in the four-parameter family have obstructing invariant curves. The priority comparison did not include a full-text reading of the older Fujino–Sato preprint; an implicit earlier computation in fan literature remains possible. Independent mathematical validation has not been performed.

## References
1. Daigo Ito, Michael R. Zeng, Xiangru Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279v1 (first publicly posted 2026-10-15); especially Corollary 3.6, Theorem 4.4, Example 4.5, Construction 6.1, Remark 6.2, Question 6.6, and Remark 7.6. https://arxiv.org/html/2610.22279v1
2. Osamu Fujino and Hiroshi Sato, *On non-projective complete toric varieties*, arXiv:2412.02392 (2024). Cited for the source fan's projectivity classification; full text not materially inspected here. https://arxiv.org/abs/2412.02392
3. David A. Cox, John B. Little, Henry K. Schenck, *Toric Varieties*, American Mathematical Society, 2011. Standard toric wall-intersection and star-fan constructions.
