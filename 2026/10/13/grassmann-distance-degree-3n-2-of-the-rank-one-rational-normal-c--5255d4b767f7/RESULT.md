# Grassmann-distance degree \(3n-2\) of the rank-one rational-normal-curve model

## Finding

For each integer \(n\ge2\), let \(\mathcal C_n\subset\operatorname{pGr}(1,n+1)\) be the image of the rational normal curve under the symmetric orthogonal-projection chart. Then its Grassmann-distance degree, in the cut-locus-excised sense of Friedman--Hoşten--Rosana, is
\[
\boxed{\operatorname{GDdeg}(\mathcal C_n)=3n-2.}
\]
For generic rank-one projection data, the ordinary critical equations have \(4n-2\) simple solutions, of which exactly \(n\) lie in the algebraic cut locus and exactly \(3n-2\) remain. The Euclidean-distance degree \(4n-2\) agrees with the single-block specialization of Theorem 2.2 of Friedman--Hoşten--Rosana; the exact Grassmann-distance count is the assertion here.

## Assumptions and scope

Work over \(\mathbb C\), with the standard nondegenerate symmetric bilinear form on \(\mathbb C^{n+1}\), and fix any integer \(n\ge2\). Write
\[
v_n(t)=(1,t,\ldots,t^n)^{\mathsf T},\qquad S_n(t)=\sum_{j=0}^{n}t^{2j}.
\]
The model is the image of the regular embedding
\[
t\longmapsto P_n(t)=\frac{v_n(t)v_n(t)^{\mathsf T}}{S_n(t)}
\]
on the open subset of \(\mathbb P^1\) where \(S_n\ne0\), with the usual extension at \(t=\infty\) (there \(P_n\) projects to the final coordinate vector). In particular \(P_n^2=P_n\), \(P_n^{\mathsf T}=P_n\), and \(\operatorname{tr}P_n=1\). Distinct parameter values define distinct projective lines, and the rational normal parametrization is immersive; hence \(\mathcal C_n\) is smooth, irreducible, and has Zariski-dense real points.

Generic data means a general vector \(a=(a_0,\ldots,a_n)\in\mathbb C^{n+1}\) with \(a^{\mathsf T}a\ne0\), defining an arbitrary projection \(Q=aa^{\mathsf T}/(a^{\mathsf T}a)\in\operatorname{pGr}(1,n+1)\). The vector \(a\) is **not** constrained to lie on the rational normal curve. The algebraic cut locus is the set where \(\operatorname{rank}(P_n(t)Q)<1\), equivalently \(v_n(t)^{\mathsf T}a=0\). We count distinct complex smooth-model stationary points away from this cut locus, as in Definition/Proposition 4.2 of the initiating paper.

## Proof

Set \(A(t)=\sum_{j=0}^n a_jt^j\) and \(S(t)=S_n(t)\). For the above projection data,
\[
\operatorname{tr}(P_n(t)Q)=\frac{A(t)^2}{S(t)(a^{\mathsf T}a)}.
\]
The nonzero scalar divisor \(a^{\mathsf T}a\) is constant in \(t\). The numerator of the derivative of the remaining quotient factors as
\[
\frac{d}{dt}\frac{A(t)^2}{S(t)}
=\frac{A(t)W(t)}{S(t)^2},\qquad
W(t)=2S(t)A'(t)-S'(t)A(t).
\]
The roots of \(A\) are precisely the cut points, so the non-cut stationary points in the finite chart are the roots of \(W\) where \(AS\ne0\).

The polynomial \(S(t)=(t^{2n+2}-1)/(t^2-1)\) has \(2n\) distinct complex roots: all \((2n+2)\)-nd roots of unity apart from \(1\) and \(-1\). For general \(a\), the polynomial \(A\) has degree \(n\), is squarefree, and is coprime to \(S\). Therefore at a root of \(A\) one has \(W=2SA'\ne0\), and at a root of \(S\) one has \(W=-S'A\ne0\). Neither cut points nor missing isotropic points are roots of \(W\).

The leading terms of \(2SA'\) and \(S'A\) in degree \(3n-1\) cancel. The next coefficient is \(-2a_{n-1}\), so
\[
\deg W=3n-2
\]
when \(a_{n-1}\ne0\). This same condition shows that the parameter value at infinity is not stationary: in the local coordinate \(u=1/t\) the rational objective has expansion
\[
\frac{A(t)^2}{S(t)}=a_n^2+2a_na_{n-1}u+O(u^2),
\]
whose linear term is nonzero for general \(a\) with \(a_n a_{n-1}\ne0\).

It remains to rule out repeated roots of \(W\). On the open set \(S(t)\ne0\), at each fixed \(t\) the equations \(W(t)=0\) and \(W'(t)=0\) impose two independent linear conditions on \(a\). Indeed the evaluation map from coefficients of degree-\(n\) polynomials to the three jets \((A(t),A'(t),A''(t))\) is surjective for \(n\ge2\); the coefficient of \(A''(t)\) in \(W'(t)\) equals \(2S(t)\ne0\), while that coefficient in \(W(t)\) is zero. The incidence locus of pairs \((a,t)\) satisfying these two equations therefore has dimension at most \(n\), strictly smaller than the \(n+1\)-dimensional coefficient space. Its projection has proper Zariski closure, so a general \(a\) yields no repeated roots of \(W\) on \(S\ne0\). Because \(W\) never vanishes at a root of \(S\), all \(3n-2\) roots are simple and non-cut. This proves the formula for every \(n\ge2\).

For comparison, the rational map \(t\mapsto A(t)^2/S(t)\) has degree \(2n\). Riemann--Hurwitz gives total ramification \(4n-2\); its \(n\) simple zeros of \(A\) contribute one each, and the remaining \(3n-2\) simple ramification points are exactly the non-cut stationary points just counted. This is a consistency check, not a replacement for the generic-transversality argument.

## Verification

The self-contained `verify.py` executes exact polynomial arithmetic over the prime field of order \(1000003\). For each \(2\le n\le20\), it constructs one coefficient vector \(a\) and checks the degree \(3n-2\), squarefreeness of \(A,S,W\), and pairwise coprimality needed to separate cut roots and missing poles. The program returned `VERIFY_OK`. This finite collection of examples corroborates the formulas but does not establish the universal theorem; that follows from the symbolic argument above. No external packages are necessary.

## Relationship to prior work

Friedman, Hoşten and Rosana introduce GD degree for general projection-Grassmannian models and determine the ED degree of rational-normal-scroll ruling curves (their Theorem 2.2). Its one-block specialization gives \(4n-2\). Their Definition/Proposition 4.2 mandates removing the algebraic cut locus for GD degree, but the inspected discussion does not compute this rank-one rational-normal-curve GD family. Friedman, Rosana and Sturmfels introduce and calculate GD invariants for models in the Grassmannian of lines, i.e. rank-two projection data, without this rank-one model-specific count. The formula here is not claimed as a general theorem about every projection-Grassmannian curve.

## Limitations

The statement assumes \(\mathbb C\), ordinary nonisotropic rank-one projection charts, generic data in the *ambient* rank-one projection Grassmannian, and integers \(n\ge2\). It does not count nongeneric or real critical points separately, solve the global real minimization problem, or apply to higher-rank models. Computational tests over a finite field do not prove universality. Exhaustive bibliographic novelty or independent validation is not asserted.

## References

1. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1 (first submitted 1 October 2026), Sections 1, 2 (Theorem 2.2), and 4 (Definition/Proposition 4.2), https://arxiv.org/html/2610.02018v1.
2. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (30 January 2026), Sections 1, 3, and 4, https://arxiv.org/html/2601.22843v1.
