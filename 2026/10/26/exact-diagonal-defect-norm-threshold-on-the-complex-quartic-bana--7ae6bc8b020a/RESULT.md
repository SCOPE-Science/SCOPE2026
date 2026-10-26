# Exact diagonal defect-norm threshold on the complex quartic Banach plane

## Finding

Let \(X=\ell_4^2(\mathbb C)\). For every diagonal strict contraction \(D=\operatorname{diag}(\lambda,\mu)\), with \(a=|\lambda|\), \(b=|\mu|\) and \(0\le a,b<1\), define the square-root norm defect
\[
\Delta_D(x)=\bigl(\|x\|_4^2-\|Dx\|_4^2\bigr)^{1/2}.
\]
Then the following is a necessary and sufficient condition for \(\Delta_D\) to be a norm:
\[
\boxed{\min\{a,b\}\ge(\max\{a,b\})^2.}
\]
In particular, nonzero rank-one diagonal strict contractions never have norm-valued square-root defects, while a full two-dimensional family of genuinely unequal, nonzero diagonal contractions does. For example, \(a=9/10\), \(b=17/20\) satisfies the criterion, whereas \(a=9/10\), \(b=4/5\) fails. By the general norm-defect criterion of Jana--Pal--Roy, this also describes precisely which of these strict contractions admit an isometric dilation in their Banach \(2\)-sum sense.

## Assumptions and scope

The scalar field is complex. The norm is \(\|(z_1,z_2)\|_4=(|z_1|^4+|z_2|^4)^{1/4}\), and the only operators classified are complex diagonal operators of norm less than one. The phenomenon concerns the specific square-root of a *difference of squared norms*, not the fourth-root of a difference of fourth powers. Interchanging coordinates does not change the criterion; assume below that \(a\ge b\). The result on the defect norm itself also holds over the reals. The dilation interpretation uses the definition in the cited Banach-space dilation papers, with a \(2\)-direct-sum dilation space; no assertion is made about other definitions of dilation.

## Proof

Assume \(a\ge b\), so the asserted condition is \(b\ge a^2\). If \(a=b=0\), the defect is just the original norm. Hence for sufficiency suppose \(0<b\le a<1\) and \(b\ge a^2\). Write
\[
S(t)=\sqrt{1+t^4},\quad R(t)=\sqrt{a^4+b^4t^4},\quad g(t)=\sqrt{S(t)-R(t)}\qquad(t>0).
\]
The strict contraction gives \(S>R>0\). Direct differentiation gives the exact identity
\[
g(t)g''(t)=3t^2\bigl(S^{-3}-a^4b^4R^{-3}\bigr)
-\frac{t^6(b^4-a^4)^2}{(S-R)S^3R^3}.
\]
Consequently \(g''(t)\ge0\) is equivalent, after multiplication by positive factors, to
\[
3(R^3-a^4b^4S^3)(S-R)\ge t^4(b^4-a^4)^2.\tag{1}
\]
Put \(u=a^2\), \(v=b^2\), and \(q=R/S\). From the weighted-average identity
\[
q^2=\frac{u^2+v^2t^4}{1+t^4}
\]
we have \(v<q<u\) unless the weights coincide. Dividing (1) by \(S^4=(1+t^4)^2\) and using
\[
\frac{t^4(u^2-v^2)^2}{(1+t^4)^2}=(u^2-q^2)(q^2-v^2)
\]
reduces the convexity condition to
\[
3(q^3-u^2v^2)(1-q)\ge(u^2-q^2)(q^2-v^2).\tag{2}
\]
Our hypothesis \(b\ge a^2\) is \(v\ge u^2\), hence
\[
0<u^2\le v\le q\le u<1.
\]
As \(v\le q\) and \(u^2\le v\),
\[
q^3-u^2v^2\ge q^2(q-u^2)\ge q^2(q-v).
\]
Also \(u^2-q^2\le q(1-q)\) and \(q+v\le2q\), so
\[
(u^2-q^2)(q^2-v^2)\le2q^2(1-q)(q-v).
\]
The left-hand side of (2) is at least \(3q^2(1-q)(q-v)\), which dominates its right-hand side. Therefore \(g''\ge0\) for all positive \(t\). At \(a=b\), the defect is the positive multiple \(\sqrt{1-a^2}\,\|x\|_4\) of the original norm, so it is also convex.

The positive-quadrant function \(N(s,t)=\Delta_D(s,t)=s g(t/s)\), for \(s,t>0\), is the *perspective* of \(g\) and hence is convex; continuity extends convexity to the quadrant boundary. It is coordinatewise increasing. Indeed, differentiating \(\Delta_D(s,t)^2=\sqrt{s^4+t^4}-\sqrt{a^4s^4+b^4t^4}\) with respect to \(s>0\), its sign is that of
\[
\frac1{\sqrt{s^4+t^4}}-\frac{a^4}{\sqrt{a^4s^4+b^4t^4}}.
\]
This is nonnegative because \(b\ge a^2\) implies \(b^4\ge a^8\) and \(a^4\ge a^8\). The derivative with respect to \(t\) is nonnegative using \(a\ge b^2\), which follows from \(a\ge b\) and \(b<1\). Since \(N\) is convex, one-homogeneous and increasing on the nonnegative quadrant, for arbitrary \(z,w\in\mathbb C^2\) we have
\[
N(|z+w|)\le N(|z|+|w|)\le N(|z|)+N(|w|),
\]
where modulus is coordinatewise. Positivity and definite homogeneity follow from \(\|D\|<1\). Thus \(\Delta_D\) is a norm.

For necessity, recall that every absolute norm on \(\mathbb C^2\) is coordinatewise nondecreasing: changing the sign (or phase) of one coordinate is an isometry, so the contractive coordinate projection is their average, and convexity also gives all intermediate moduli. If \(a>b>0\) but \(b<a^2\), an expansion near the second coordinate axis gives
\[
\Delta_D(t,1)^2=1-b^2+\tfrac12\bigl(1-a^4/b^2\bigr)t^4+O(t^8)
\quad(t\downarrow0).
\]
The fourth-order coefficient is negative, contradicting coordinatewise monotonicity. If \(b=0<a\), the analogous expansion is
\[
\Delta_D(t,1)^2=1-a^2t^2+O(t^4)<\Delta_D(0,1)^2
\quad(t\downarrow0).
\]
Thus the only possible norm-valued case is \(b\ge a^2\). This proves necessity and completes the classification.

## Verification

The proof uses elementary differentiation, an explicit algebraic substitution and the perspective characterization of convex functions. Its sharp failure direction is an analytic one-coordinate perturbation of the coordinate axis, not numerical extrapolation. A standalone standard-library checker in `check.py` cross-checks the exact substitution identity for rational parameters, the sufficient inequalities, and numerical triangle inequalities for boundary/interior examples; these finite checks are supplementary, not an infinite proof. The two explicit test cases exhibit opposing sides of the sharp boundary.

## Relationship to prior work

Jana, Pal and Roy established the general equivalence between norm-valued square-root defects and the associated Banach isometric-dilation criterion. Jana and Pal's later paper uses this criterion for pairs of strict contractions, but neither inspected treatment gives the present sharp two-parameter criterion for nonzero anisotropic diagonal operators on \(\ell_4^2\). Published work on scalar-coordinate \(\ell_p\)-sum contractions establishes nonexistence for the rank-one corner when \(p>2\), which is consistent with our necessary condition but does not imply the newly identified positive region \(0<a^2\le b<a<1\). The result is a class-specific evaluation of the established abstract criterion, not a new general dilation theorem.

## Limitations

Only diagonal operators on the two-dimensional quartic space are classified. We neither assert an analogous threshold in other exponents or dimensions, nor determine a more general dilation theory. Novelty has been compared with identifiable published work and searchable research records, but an older unpublished or differently phrased equivalent classification cannot be ruled out by search alone; independent audit has not been performed. Numerical checks are nonexhaustive.

## References

1. Swapan Jana and Sourav Pal, *On a minimal Andô dilation for a pair of strict contractions*, arXiv:2603.26321, first posted 27 March 2026, https://arxiv.org/abs/2603.26321; version 2 full text https://arxiv.org/html/2603.26321v2.
2. Swapan Jana, Sourav Pal and Saikat Roy, *A dilation theoretic approach to Banach spaces*, arXiv:2407.15112, first posted 21 July 2024, https://arxiv.org/abs/2407.15112.
3. *Sharp scalar-defect thresholds on \(\ell_p\)-sums*, public research record dated 11 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-scalar-defect-thresholds-on-ell-p-sums--95939122362e (record summary used for the rank-one overlap comparison; the full text was not inspected).
