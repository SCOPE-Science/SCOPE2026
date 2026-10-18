# Exact Mahler-volume interpolation for equilateral bounded-Lipschitz norms

## Finding

For every integer \(n\geq2\) and \(\lambda\geq0\), equip the real functions on an \(n\)-point equilateral metric space with the norm
\[
 N_\lambda(x)=\max_i|x_i|+\lambda(\max_i x_i-\min_i x_i),\qquad x\in\mathbb R^n.
\]
Write \(s=1+2\lambda\), and let \(B_{n,s}\) be its unit ball. The polar, the two volumes, and their affine-invariant product are given *exactly* by
\[
 B_{n,s}^{\circ}=\{y\in\mathbb R^n:\ \|y\|_1\leq s,\ |\sum_{i=1}^ny_i|\leq1\},
 \qquad |B_{n,s}|=\frac{2^n}{s^{n-1}},
\]
\[
 |B_{n,s}^{\circ}|=\frac{2^n s^n}{n!}\,P_n(1/s),\qquad
 \frac{n!}{4^n}|B_{n,s}|\,|B_{n,s}^{\circ}|=sP_n(1/s),
\]
where the *explicit polynomial* \(P_n\) is
\[
 P_n(a)=\frac{n}{2^{2n-2}}\sum_{j=0}^{n-1}\binom{n-1}{j}^{\!2}
 \int_0^a(1+t)^j(1-t)^{n-1-j}\,dt\quad(0\leq a\leq1).
\]
(The integrals are finite polynomial antiderivatives, hence this is an exact polynomial expression in \(a\).)

For \(n=2\), the normalized product is exactly \(1\) for every \(s\geq1\). For every \(n\geq3\), it is *strictly increasing* in \(s\in[1,\infty)\), starts at \(1\), and approaches the sharp, unattained value
\[
 C_n=\frac{n}{4^{n-1}}\binom{2n-2}{n-1}\sim\sqrt{n/\pi}.
\]
For each fixed finite \(s\geq1\), the normalized product converges to \(s\) as \(n\to\infty\). In particular, at \(s=3\) the normalized products for dimensions \(3\) and \(4\) are \(10/9\) and \(11/9\), respectively.

The terminal coefficient \(C_n\) is *not claimed as new in isolation*: it coincides, after normalization and a dimension shift, with the known volume product of the anchored equilateral Lipschitz-free space computed in Alexander–Fradelizi–García-Lirola–Zvavitch, Section 5.2, Claim 5 [3]. The new result is the full finite-parameter bounded-Lipschitz interpolation, its polar and volume formulas, and strictness throughout the family.

## Assumptions and scope

Throughout, \(n\geq2\) is an integer, \(\lambda\geq0\) is real, and the finite metric is \(d(i,j)=1\) whenever \(i\ne j\). The norm uses the *sum* \(\|x\|_\infty+\lambda\operatorname{Lip}(x)\), not the maximum of those two terms, and functions are not constrained to vanish at a basepoint. Lebesgue volumes and polars use the standard Euclidean pairing in all \(n\) coordinates. For \(s=1\), the norm is \(\ell_\infty^n\) and the product is the cube–crosspolytope value \(4^n/n!\). The parameter \(s=\infty\) is only a limit, not a norm within the statement.

## Proof

**1. Vertex and polar descriptions.** Set \(m=\min_i x_i\), \(M=\max_i x_i\), \(c=(M+m)/2\), and \(r=(M-m)/2\). Then \(r\geq0\) and exactly
\[
 N_\lambda(x)=|c|+sr.
\]
At fixed \(m,M\), every coordinate lies in \([m,M]\), and the vector is a convex combination of the sign-pattern vectors whose entries are among \(m,M\), with at least one of each if \(m<M\). The admissible pairs \((c,r)\) form the triangle \(|c|+sr\leq1\), \(r\geq0\). Therefore
\[
 B_{n,s}=\operatorname{conv}\left(\{\mathbf1,-\mathbf1\}\cup
 \{\sigma/s:\sigma\in\{-1,1\}^n\text{ is nonconstant}\}\right).
\]
Its polar imposes \(|\sum_i y_i|\leq1\) and \(|\sum_i\sigma_i y_i|\leq s\) for each nonconstant sign vector. These are equivalent to the displayed polar inequalities: they follow immediately from \(\|y\|_1\leq s\); conversely, if the sign vector maximizing \(\sum_i\sigma_i y_i=\|y\|_1\) is nonconstant, that constraint gives the \(\ell_1\) bound, while if all nonzero \(y_i\) have the same sign, the mass constraint gives \(\|y\|_1\leq1\leq s\). Zeros do not affect this dichotomy.

**2. The primal volume.** Almost every vector has unique minimum and maximum coordinates. Integrating first with respect to these extrema gives
\[
 |B_{n,s}|=n(n-1)\iint_{m<M}\mathbf1_{\{|(m+M)/2|+s(M-m)/2\leq1\}}
 (M-m)^{n-2}\,dm\,dM.
\]
Changing to \((c,r)\), with Jacobian \(2\), yields
\[
 n(n-1)2^n\int_0^{1/s}r^{n-2}(1-sr)\,dr=2^n/s^{n-1}.
\]

**3. Exact diagonal-slab density.** Let \(Y\) be uniform in the crosspolytope \(\{y:\|y\|_1\leq1\}\), and \(T=\sum_iY_i\). Its density is the even polynomial
\[
 q_n(t)=\frac{n}{2^{2n-1}}\sum_{j=0}^{n-1}\binom{n-1}{j}^{\!2}
 (1+t)^j(1-t)^{n-1-j}\qquad(-1\leq t\leq1).
\]
We justify the nonstandard section identity rather than assume it. Write \(d=n-1\), \(a=(1+t)/2\), \(b=(1-t)/2\) for \(0\leq t\leq1\), and \(\Delta=\operatorname{conv}(e_1,\ldots,e_n)\) in the affine hyperplane \(\sum_i z_i=1\). The slice \(\{y:\sum_i y_i=t,\|y\|_1\leq1\}\) is \(a\Delta-b\Delta\): for an arbitrary point, add common nonnegative mass to its positive and negative parts to make the respective totals \(a,b\).

Define coarea-normalized slice volume as the density for the sum coordinate (ordinary section volume divided by \(\sqrt n\)). For any \(a\geq b\geq0\), putting \(u=a-b\), \(d=n-1\), its value can be computed by partitioning into coordinate sign orthants:
\[
 V_n(a,b)=\frac{u^d}{d!}+\sum_{k=1}^{n-1}
 \frac{\binom nk}{(k-1)!(n-k-1)!}
 \int_0^b(u+v)^{k-1}v^{n-k-1}\,dv.
\]
Indeed, in an orthant with \(k\) positive and \(n-k\) negative coordinates, the total negative mass \(v\) ranges from \(0\) to \(b\), and the positive mass is \(u+v\). The first term counts the positive orthant at zero negative mass (the limiting slice with no negative coordinates).

Expanding in powers of \(u\) and \(b\), the coefficient of \(u^h b^{d-h}\) for \(0\leq h<d\) is
\[
 \frac1{h!(d-h)}\sum_{k=h+1}^d\frac{\binom{d+1}{k}}{(k-1-h)!(d-k)!}
 =\frac{\binom{2d-h}{d-h}}{h!(d-h)!},
\]
by Vandermonde's identity; the coefficient of \(u^d\) is \(1/d!\). The binomial expression
\[
 \frac1{d!}\sum_{j=0}^d\binom dj^2(u+b)^jb^{d-j}
\]
has exactly the same coefficients, since \(\sum_{j=h}^d\binom dj^2\binom jh=\binom dh\binom{2d-h}{d-h}\). Thus
\[
 V_n(a,b)=\frac1{(n-1)!}\sum_{j=0}^{n-1}\binom{n-1}j^2a^jb^{n-1-j}.
\]
The \(\ell_1\)-ball has volume \(2^n/n!\). Dividing \(V_n((1+t)/2,(1-t)/2)\) by this volume proves the stated density \(q_n(t)\). Hence \(P_n(a)=\Pr(|T|\leq a)=\int_{-a}^a q_n(t)\,dt\). The polar identity and scaling by \(s\) give
\[
 |B_{n,s}^{\circ}|=|sB_1^n|\,\Pr(|T|\leq1/s)
 =\frac{2^ns^n}{n!}P_n(1/s),
\]
and multiplication by the primal volume gives the product formula.

**4. Strict monotonicity and exact limit.** The slices of any convex body by parallel hyperplanes have concave \((n-1)\)-st root of their volume by Brunn–Minkowski. Consequently \(q_n(t)\) is nonincreasing on \([0,1]\), because it is even. In dimension \(n\geq3\), the simplex \(\Delta\) has affine dimension at least two and is not a translate and positive dilate of \(-\Delta\); strict Brunn–Minkowski gives \(q_n(0)>q_n(1)\). Since \(q_n\) is a polynomial, it cannot be constant on a nontrivial subinterval without being constant everywhere. Hence \(q_n\) is strictly decreasing between any two distinct points of \([0,1]\). Since
\[
 sP_n(1/s)=\frac{1}{a}\int_{-a}^a q_n(t)\,dt,\qquad a=1/s,
\]
this expression is strictly increasing as \(s\) increases whenever \(n\geq3\). For \(n=2\), direct substitution gives \(q_2(t)=1/2\), hence the product is constant.

The limiting ratio as \(s\to\infty\) equals \(2q_n(0)\). The Vandermonde sum \(\sum_j\binom{n-1}{j}^2=\binom{2n-2}{n-1}\) gives \(C_n\). The central-binomial asymptotic yields \(C_n\sim\sqrt{n/\pi}\). Finally, for uniform \(Y\) in \(B_1^n\), sign symmetry and elementary beta integration give \(\mathbb E T^2=2n/((n+1)(n+2))\). Chebyshev's inequality implies \(P_n(1/s)\to1\) for each fixed finite \(s\), establishing the high-dimensional limit. The known anchored-equilateral endpoint comparison is explained below.

## Verification

The included standalone `verify.py` uses exact rational arithmetic. For dimensions \(2\) through \(11\), it compares the signed-orthant slice integration with the binomial formula on six rational input pairs and checks that the slab probability is normalized. For dimensions \(2\) through \(9\), it independently computes polar volumes through signed-orthant exclusion integrals and compares them with the slab polynomial at five rational parameters. It also checks the planar constant case and the three-dimensional \(s=3\) example, reporting `PASS 117 exact-rational checks`. Execute `python verify.py` with the Python standard library. Finite arithmetic verifies identities at tested instances; universal statements follow from the displayed analytic proof.

## Relationship to prior work

Hille–Theewis [1] define the bounded-Lipschitz norm \(\|f\|_\infty+\operatorname{Lip}(f)\), study extreme and norming finite-space functions, and in Section 6 analyze finite metric constraints. Their work motivates this polyhedral family but does not calculate its parameterized polar volumes or Mahler product. Their earlier paper [2] develops computations for Fortet–Mourier norms and discusses the dual Dudley norm; it does not supply this volume-profile theorem.

Alexander–Fradelizi–García-Lirola–Zvavitch [3], Section 5.2, Claim 5, calculate the volume product of the *anchored Lipschitz-free space* over an equilateral metric. Their result is exactly the **terminal coefficient** \(C_n\) here after the natural dimension shift and normalization. This known endpoint is explicitly excluded from the novelty claim. The spaces and norms in the interior are different: [3] uses functions vanishing at a basepoint and their Lipschitz seminorm, while this theorem uses all \(n\) real function coordinates and the sum of the supremum and a weighted Lipschitz seminorm. The single anchored endpoint and general polytope results of [3] do not imply the exact finite-parameter formula or strict monotonicity without additional calculation. Kim [4] studies Mahler products near Hanner polytopes; those local bounds do not determine this full parameter family.

## Limitations

This result is confined to finite equilateral metrics, the real scalar field, nonnegative weights, and the *sum*-form bounded-Lipschitz norm. No extremal property is asserted among all metric spaces, all Banach norms, or all symmetric convex bodies; in particular nothing is claimed about the general Mahler conjecture. The limiting anchored-equilateral coefficient is previously known [3]. The result has undergone self-review only; independent audit has not been performed.

## References

[1] S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500 (initial public version 2023-05-15), especially Sections 1 and 6, https://arxiv.org/abs/2305.08500.

[2] S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet–Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234 (2022), especially Sections 1 and 6, https://arxiv.org/abs/2206.12234.

[3] M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019), especially Section 5.2, Claim 5, https://arxiv.org/abs/1911.10642.

[4] J. Kim, *Minimal volume product near Hanner polytopes*, arXiv:1212.2544 (2012), https://arxiv.org/abs/1212.2544.
