# The sharp \(\sqrt{2}\) ceiling for Birkhoff-restricted angular distortion

## Finding

Let \(X\) be any real Banach space of dimension at least two. For nonzero vectors \(x,y\), define the angular and skew-angular distances by
\[
\alpha[x,y]=\left\|\frac{x}{\|x\|}-\frac{y}{\|y\|}\right\|,\qquad
\beta[x,y]=\left\|\frac{x}{\|y\|}-\frac{y}{\|x\|}\right\|.
\]
Write \(x\perp_B y\) when \(\|x+\lambda y\|\geq\|x\|\) for every real \(\lambda\). The Birkhoff-restricted Dehghan--Rooin invariant is
\[
\operatorname{DR}_B(X)=\sup_{\substack{x,y\ne0\\x\perp_B y}}
 \frac{\alpha[x,y]}{\beta[x,y]}.
\]
Its **sharp universal range** is
\[
\boxed{1\leq\operatorname{DR}_B(X)\leq\sqrt{2}.}
\]
The upper coefficient is **attained** on both real planes \(\ell_\infty^2\) and \(\ell_1^2\); in particular the previously stated universal upper bound \(2\) is not sharp.

More precisely, for unit vectors \(u\perp_B v\), set
\[
Q(u,v,t)=\frac{\|u-v\|}{\|t u-t^{-1}v\|},\qquad t>0.
\]
Then \(Q(u,v,t)=\sqrt{2}\) **if and only if**
\[
\boxed{t=2^{-1/2}\quad\text{and}\quad\|u-2v\|=1.}
\]
The second condition is equivalent to the entire segment \(\{u-sv:0\leq s\leq2\}\) lying on the unit sphere. In particular every finite-dimensional *strictly convex* real space of dimension at least two satisfies \(\operatorname{DR}_B(X)<\sqrt{2}\).

## Assumptions and scope

The underlying scalars are real, no smoothness, reflexivity, or finite-dimensionality is required for the sharp universal upper bound. The Birkhoff condition ensures the skew-angular denominator cannot vanish: if \(t u=t^{-1}v\), the two nonzero directions would be linearly dependent, impossible for a Birkhoff pair. The strict-convexity consequence is asserted only in finite dimension, where the profile supremum is attained; nonattained suprema in infinite dimensions are not classified.

## Proof

**1. Reduction and orthogonality bounds.** By scaling the nonzero input vectors, the angular/skew-angular quotient is exactly \(Q(u,v,t)\), where \(\|u\|=\|v\|=1\), \(u\perp_B v\), and \(t>0\) (the elementary scale-profile identity of [1, Theorem 2.2 and Corollary 2.4]). Write
\[
D=t u-t^{-1}v,\qquad d=\|D\|,\qquad n=\|u-v\|.
\]
Since \(u\perp_B v\), \(d=t\|u-t^{-2}v\|\geq t\). The reverse triangle inequality also yields \(d\geq|t-t^{-1}|\). Thus \(d>0\) and \(n\leq2\).

**2. Small scales.** For \(0<t\leq1\) the identity
\[
u-v=tD+(1-t^2)u
\]
gives \(n\leq td+(1-t^2)\), hence
\[
Q(u,v,t)\leq t+\frac{1-t^2}{\max\{t,t^{-1}-t\}}
=\begin{cases}
2t,&0<t\leq2^{-1/2},\\
t^{-1},&2^{-1/2}\leq t\leq1.
\end{cases}
\]
The right-hand side is at most \(\sqrt{2}\) and is strictly smaller for every \(t\ne2^{-1/2}\) in this interval.

**3. Large scales.** For \(t\geq1\), use
\[
u-v=t^{-1}D-(1-t^{-2})v.
\]
Consequently
\[
Q(u,v,t)\leq t^{-1}+\frac{1-t^{-2}}d
\leq2t^{-1}-t^{-3}
\leq\frac{4\sqrt{6}}9<\sqrt{2}.
\]
The penultimate maximum occurs at \(t=\sqrt{3/2}\), as differentiation shows. Parts 2--3 prove the upper bound.

**4. Equality and sharpness.** Equality can occur only at \(t=2^{-1/2}\). There \(d=2^{-1/2}\|u-2v\|\), and \(n\leq d/\sqrt{2}+1/2\). Equality \(n/d=\sqrt{2}\), together with \(d\geq2^{-1/2}\), forces \(d=2^{-1/2}\) and \(n=1\), equivalently \(\|u-2v\|=1\). Conversely, if \(\|u-2v\|=1\), convexity gives \(\|u-v\|\leq1\); Birkhoff orthogonality gives \(\|u-v\|\geq1\), so \(n=1\) and \(Q(u,v,2^{-1/2})=\sqrt{2}\). The same convexity and orthogonality inequalities show that the complete segment \(u-sv\), \(0\leq s\leq2\), has norm one.

For \(X=\ell_\infty^2\) take \(u=(1,1)\), \(v=(0,1)\), with the first-coordinate functional witnessing \(u\perp_B v\). For \(X=\ell_1^2\), take \(u=(1,0)\), \(v=(1/2,1/2)\), with the norm-one functional \(f(a,b)=a-b\) witnessing \(u\perp_B v\). In both cases \(\|u\|=\|v\|=\|u-2v\|=1\), so the upper bound is attained.

For the lower bound, any norm-one functional attaining its norm at \(u\in S_X\) has a nontrivial kernel. Choose \(v\in S_X\) in that kernel; then \(u\perp_B v\), and \(Q(u,v,1)=1\).

**5. Strictly convex finite-dimensional case.** The unit Birkhoff-pair set is compact because the unit sphere is compact and the orthogonality inequality is closed. Uniformly for such pairs, \(Q\leq 2/t\) as \(t\to\infty\), while \(Q\leq2/(t^{-1}-t)\) as \(t\downarrow0\). Therefore its supremum occurs for a finite positive \(t\). The equality criterion would provide distinct unit vectors \(u\) and \(u-2v\) whose midpoint \(u-v\) is again unit, contradicting strict convexity. Thus the supremum is strictly smaller than \(\sqrt{2}\).

## Verification

Run `python3 verify.py` using only the Python standard library. The deterministic script checks two exact extremal configurations, 11,340 finite smooth \(\ell_p^2\) Birkhoff profiles, and 4,999 values of the analytic piecewise bound. Its output reports PASS. These finite checks corroborate algebraic identities and endpoints; the inequalities for every \(t>0\) and every real Banach space are proved analytically above, independently of numerical experiments.

## Relationship to prior work

Du, Hu, Zhang, and Liu [1] introduce exactly this Birkhoff-restricted angular/skew-angular invariant and derive its normalized scale profile. Their Proposition 2.5 gives \(1\leq\operatorname{DR}_B(X)\leq2\) and presents the upper value \(2\) as sharp through planar renorming examples (Example 4.4). The universal bound \(\sqrt{2}\), its exact attainment in the square and diamond planes, and the pointwise equality criterion are not consequences of the stated bound or examples: in fact the new bound precludes the proposed sharpness at \(2\). The earlier Fu--Li invariant [2] takes a supremum over *unrestricted* pairs and can be larger, so its universal bound does not yield the present sharper coefficient. Fu--Li's Massera--Schäffer invariant [3] tests a different Birkhoff-geometric ratio. Related polyhedral constants in other geometric comparisons do not determine this angular/skew-angular quotient.

## Limitations

The theorem establishes the optimal universal coefficient and pointwise equality, but does not classify all infinite-dimensional Banach spaces with a nonattained supremum \(\sqrt{2}\). The literature-priority review is not an exhaustive historical proof of novelty: an equivalent inequality could occur under a different normalization or as an implicit lemma in earlier work. The full journal text of [2] and [3] was not available for complete comparison; only bibliographic records and abstracts were inspected. No independent scientific audit has been performed.

## References

[1] J. Du, T. Hu, W. Zhang, Q. Liu, *A Birkhoff-Orthogonal Dehghan--Rooin Type Constant in Banach Spaces*, arXiv:2609.27754v1, original publicly indexed date 2026-08-15, https://arxiv.org/abs/2609.27754 .

[2] Y. Fu, Y. Li, *Geometric constant for quantifying the difference between angular and skew angular distances in Banach spaces*, Annals of Functional Analysis **15** (2024), DOI: 10.1007/s43034-024-00341-0.

[3] Y. Fu, Y. Li, *The Massera--Schäffer inequality related to Birkhoff orthogonality in Banach spaces*, Filomat **38** (2024), 5247--5259, DOI: 10.2298/FIL2415247F.
