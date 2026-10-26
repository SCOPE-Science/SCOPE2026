# Dimension-uniform Frobenius-discriminant census of smooth quadric pencils over odd finite fields

## Finding

Fix an odd prime power \(q\) and an integer \(n\geq 3\), and put \(k=\mathbf F_q\) and \(N=n(n+1)/2\). Consider the two-dimensional \(k\)-subspaces \(W\subset \operatorname{Sym}^2(k^n)^\vee\), or pencils of quadrics on \(\mathbf P^{n-1}_k\). Call \(W\) *admissible* if **every** one of its \(q+1\) rational projective members is geometrically nonsingular and if its common intersection \(X_W\) is geometrically smooth of codimension two.

For each partition \(\lambda\vdash n\) with no part equal to one, write \(m_d\) for the multiplicity of part \(d\), and
\[
 I_d(q)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e},\qquad
 S_\lambda(q)=\prod_{d\ge2}\binom{I_d(q)}{m_d}.
\]
The expression \(I_d(q)\) is the number of monic irreducible degree-\(d\) polynomials over \(k\). For an admissible pencil, the degree-\(n\) determinant of the pencil has \(n\) distinct geometric roots, none rational; their Frobenius cycle partition is \(\lambda\). **The exact number of admissible pencils with partition \(\lambda\)** is
\[
 \boxed{\displaystyle
   A_{n,\lambda}(q)=\frac{|\operatorname{GL}_n(\mathbf F_q)|}
   {|\operatorname{GL}_2(\mathbf F_q)|}\prod_{d\ge2}\binom{I_d(q)}{m_d}.}
\]
Consequently, writing \(S_n(q)\) for the number of monic, squarefree, root-free polynomials of degree \(n\),
\[
 \boxed{\displaystyle A_n(q)=\frac{|\operatorname{GL}_n(\mathbf F_q)|}{|\operatorname{GL}_2(\mathbf F_q)|}\,S_n(q),\qquad
 \sum_{n\ge0}S_n(q)z^n=\frac{1-qz^2}{(1-qz)(1+z)^q}.}
\]
Here \(|\operatorname{GL}_r(\mathbf F_q)|=\prod_{i=0}^{r-1}(q^r-q^i)\). Relative to all pencils in the \(N\)-dimensional space of quadratic forms, the admissible proportion tends, for fixed \(n\) and odd prime powers \(q\to\infty\), to \(D_n/n!\), where \(D_n\) is the number of fixed-point-free permutations of \(n\) letters.

For example, when \(n=4,q=3\), there are exactly \(10,614,240\) admissible genus-one complete intersections in \(\mathbf P^3_{\mathbf F_3}\), split as \(9,097,920\) of Frobenius type \((4)\) and \(1,516,320\) of type \((2,2)\). For \(n=3\), the formula gives \(1,872\) over \(\mathbf F_3\) and \(124,000\) over \(\mathbf F_5\); these two small-field counts have previously been obtained independently and are not claimed as new. The claim concerns *linear pencils with fixed ambient coordinates*, not projective-isomorphism classes.

## Assumptions and scope

The characteristic is odd, and \(n\ge3\). A geometrically nonsingular member means a smooth quadric hypersurface over an algebraic closure, equivalently a nonsingular associated symmetric matrix. Geometric smoothness of the base locus means that the Jacobian of the two generating equations has rank two at every geometric common zero; this is a smooth codimension-two complete intersection (possibly zero-dimensional for \(n=3\)). The determinant factorization type records Frobenius orbits of the *geometric singular members* of the pencil, not the splitting type of the quadrics themselves and not the rational-point counts of the intersection. No assertion is made in characteristic two.

## Proof

**1. Discriminant and geometric smoothness.** Because every rational member is nonsingular, choose an ordered basis \((Q_0,Q_1)\) with invertible symmetric matrix \(B_0\) for \(Q_0\); let \(B_1\) represent \(Q_1\), and put \(T=B_0^{-1}B_1\). The characteristic polynomial \(f(t)=\det(tI-T)\) is monic of degree \(n\), and \(\det(tB_0-B_1)=\det(B_0)f(t)\). The projective pencil has no rational singular member exactly when \(f\) has no root in \(k\), since the member at infinity has matrix \(B_0\).

We prove that the common intersection is geometrically smooth exactly when \(f\) is squarefree. Over an algebraic closure, if \(f\) is squarefree then \(T\) has distinct eigenvalues. Its eigenlines are pairwise orthogonal for the nondegenerate symmetric form \(B_0\), hence each eigenline is anisotropic and in an eigenbasis \(B_0\) and \(B_1\) are diagonal with nonzero diagonal entries in \(B_0\). A point where the two gradients are dependent must be an eigenvector of \(T\), so cannot simultaneously satisfy both quadric equations. Conversely, if an eigenvalue \(\alpha\) is repeated, then either its eigenspace has dimension at least two, in which case that eigenspace contains an isotropic vector over the algebraic closure; or it has a nontrivial Jordan chain \((T-\alpha I)v=u\), \((T-\alpha I)u=0\). In the latter case self-adjointness gives \(B_0(u,u)=B_0((T-\alpha I)v,u)=B_0(v,(T-\alpha I)u)=0\). In either case an isotropic eigenvector is a singular geometric point of the complete intersection. The desired equivalence follows. It also shows that admissible pencils are precisely those whose monic characteristic polynomial is squarefree and root-free.

**2. Uniform fiber of the characteristic-polynomial map.** Fix any monic squarefree polynomial \(f\in k[t]\) of degree \(n\). There is one similarity class of \(n\)-by-\(n\) matrices \(T\) with characteristic polynomial \(f\), represented by multiplication by \(t\) on the etale algebra \(L=k[t]/(f)\). Its centralizer in \(\operatorname{GL}_n(k)\) is \(L^\times\), so it has \(|\operatorname{GL}_n(k)|/|L^\times|\) matrices. Fix such a \(T\). The invertible symmetric matrices \(B_0\) with \(B_0T=T^{\mathsf T}B_0\) correspond bijectively to nondegenerate symmetric bilinear forms \(b\) on \(L\) with \(b(tx,y)=b(x,ty)\). As the trace pairing of a finite etale algebra is nondegenerate, these are precisely \(b_c(x,y)=\operatorname{Tr}_{L/k}(cxy)\), for unique \(c\in L^\times\). There are exactly \(|L^\times|\) such forms. Taking \(B_1=B_0T\) gives a bijection with ordered pairs of symmetric matrices \((B_0,B_1)\) realizing \(f\), so their number is **exactly** \(|\operatorname{GL}_n(k)|\), independently of the factorization of \(f\).

**3. Passage from bases to pencils.** A change of ordered generators of a pencil acts on the roots of its determinant binary form by a projective linear fractional transformation defined over \(k\), so commutes with Frobenius and preserves the cycle partition \(\lambda\). Thus this partition is intrinsic to the pencil, not a choice of basis. Each admissible pencil has exactly \(|\operatorname{GL}_2(k)|=(q^2-1)(q^2-q)\) ordered bases. Every such basis has nonsingular first member, since *all* rational members are nonsingular. Therefore dividing the ordered-pair count by \(|\operatorname{GL}_2(k)|\) counts each admissible pencil once. A squarefree root-free monic polynomial has a unique factorization into distinct monic irreducibles of degrees at least two. Choosing \(m_d\) degree-\(d\) factors among \(I_d(q)\) possibilities gives \(S_\lambda(q)\), proving the factorization-type formula and the total.

**4. Generating function and limit.** The Euler product for monic polynomials yields \(\prod_{g\text{ monic irreducible}}(1+z^{\deg g})=(1-qz^2)/(1-qz)\). Removing the \(q\) linear factors divides by \((1+z)^q\). For fixed \(n\), the factor-count formula gives
\[
 \frac{S_n(q)}{q^n}\longrightarrow
 \sum_{\substack{\lambda\vdash n\\ m_1=0}}\prod_{d\ge2}\frac{1}{d^{m_d}m_d!}=\frac{D_n}{n!}.
\]
The total number of all pencils in an \(N\)-dimensional space is \((q^N-1)(q^N-q)/|\operatorname{GL}_2(k)|\). Since \(2N=n(n+1)\), dividing the exact counts shows that the admissible proportion has the same limit.

## Verification

The script `check_pencils.py` independently enumerates every two-dimensional subspace of ternary quadratic forms over \(\mathbf F_3\) and \(\mathbf F_5\), tests nonsingularity of every rational member, and recovers \(1,872\) of \(11,011\) pencils over \(\mathbf F_3\), and \(124,000\) of \(508,431\) pencils over \(\mathbf F_5\). It separately enumerates root-free squarefree monic quartics over \(\mathbf F_3,\mathbf F_5,\mathbf F_7\) and checks the factorization formulas. The second program, `check_quadric4.cpp`, independently enumerates all \(3^{10}=59,049\) symmetric four-by-four matrices \(B_1\) for each of the two Witt classes of a fixed invertible \(B_0\) over \(\mathbf F_3\). It finds \(12,096\) admissible second matrices for a split \(B_0\) and \(15,120\) for a nonsplit \(B_0\); multiplying by the respective counts \(21,060\) and \(16,848\) of first matrices gives \(509,483,520\) ordered pairs, hence \(10,614,240\) pencils. These programs test special finite fields; the proof above establishes the assertion in every odd characteristic and dimension \(n\ge3\). Exact run output and commands appear in `VERIFICATION.md`.

## Relationship to prior work

Segre-Weierstrass theory classifies regular pencils by elementary divisors; Fevola, Mandelshtam and Sturmfels revisit that classification over \(\mathbf C\) and study geometric strata, but do not derive the odd-finite-field dimension-uniform counting and Frobenius factorization formulas here. Pott, Schmidt and Zhou compute counts of matrix pairs constrained by the three ranks of \(B_0\), \(B_1\), and \(B_0+B_1\); this does not impose nonsingularity on every \(\mathbf F_q\)-rational pencil member or geometric smoothness of the base. The earlier individual census values for ternary quadrics over \(\mathbf F_3\) and \(\mathbf F_5\) are recovered rather than separately claimed. Leep and Schueller study nonsingular quadratic pencils and their associated hyperelliptic function fields, but full-text comparison of that older paper was not possible; overlap with an unindexed quantitative corollary remains a priority risk. The distinct contribution proposed here is the simultaneous all-dimension, all-odd-field, exact Frobenius-partition formula and its derangement-density limit.

## Limitations

The formula counts linear two-spaces of quadratic equations with coordinates fixed, not isomorphism classes of complete intersections or incidence-refined moduli points. The proof relies on odd characteristic; neither trace-form parametrization as quadratic forms nor the discriminant-smoothness equivalence is asserted in characteristic two. The finite programs provide independent checks only in the stated small fields. The absence of a matching indexed formula does not rule out earlier unindexed derivations; Leep--Schueller full text was not available for an exhaustive comparison.

## References

1. Claudia Fevola, Yelena Mandelshtam, Bernd Sturmfels, *Pencils of Quadrics: Old and New*, arXiv:2009.04334, first public version 9 September 2020; Sections 1--2. https://arxiv.org/abs/2009.04334
2. Alexander Pott, Kai-Uwe Schmidt, Yue Zhou, *Pairs of Quadratic Forms over Finite Fields*, Electronic Journal of Combinatorics **23** (2016), P2.8; Theorem 2 and Sections 1--4. https://doi.org/10.37236/4072
3. David B. Leep, Laura Mann Schueller, *Pencils of quadratic forms and hyperelliptic function fields*, Journal of Algebra **227** (2000), 532--548. https://doi.org/10.1006/jabr.1999.8168 (abstract inspected; complete text unavailable).
