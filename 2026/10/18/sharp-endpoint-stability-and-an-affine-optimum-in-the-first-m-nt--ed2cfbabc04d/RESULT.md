# Sharp endpoint stability and an affine optimum in the first Müntz projection

## Finding

For every real \(\alpha>0\), let \(P_\alpha\) be the \(L^2(0,1;dt)\)-orthogonal projector onto the two-dimensional Müntz space \(V_\alpha=\operatorname{span}\{1,t^\alpha\}\). Its extensions to complex \(L^\infty(0,1)\) and \(L^1(0,1)\) have the same exact operator norm \(\mathcal L(\alpha)\), given by
\[
\mathcal L(\alpha)=
\begin{cases}
\displaystyle \frac{2(\alpha+1)}{\alpha}\left(\frac{\alpha+1}{2\alpha+1}\right)^{1/\alpha}-1,&0<\alpha\le1,\\[6pt]
\displaystyle 1+2(2\alpha+1)^{-1/\alpha},&\alpha\ge1.
\end{cases}
\]
The two expressions agree at \(\alpha=1\). The left branch is strictly decreasing and the right branch is strictly increasing, so the ordinary affine space is the **unique most stable two-term power space**:
\[
\mathcal L(\alpha)\ge\mathcal L(1)=\frac53,
\qquad \text{equality precisely for }\alpha=1.
\]
The Lebesgue function attains its maximum exclusively at the left endpoint for \(0<\alpha<1\), exclusively at the right endpoint for \(\alpha>1\), and at both endpoints for \(\alpha=1\).

Writing \(k_\alpha(t)=K_\alpha(t,t)\) for the diagonal of its reproducing kernel, the sharp Christoffel peak has a matching endpoint switch but contrasting growth:
\[
\max_{0\le t\le1}k_\alpha(t)=
\begin{cases}
(1+1/\alpha)^2,&0<\alpha\le1,\\
2(\alpha+1),&\alpha\ge1.
\end{cases}
\]
In particular, \(\mathcal L(\alpha)\sim 2/(e\alpha)\) as \(\alpha\downarrow0\) while \(\mathcal L(\alpha)\to3\) as \(\alpha\to\infty\). The Christoffel peak grows like \(\alpha^{-2}\) and \(2\alpha\), respectively. Thus the diagonal kernel height and the uniform projection amplification have different orders in both singular regimes.

## Assumptions and scope

The measure on \([0,1]\) is unweighted Lebesgue probability measure; \(\alpha\) is an arbitrary **positive real** exponent (not the collapsed \(\alpha=0\) space). Functions and projectors may be real or complex. All \(L^p\) operator norms use the same underlying measure. For each \(\alpha\), \(P_\alpha\) has a continuous-kernel representative for bounded data. Endpoint maxima refer to the continuous Lebesgue function on \([0,1]\), which also determines the essential-supremum operator norm because endpoint values are approached from the interior. No result is asserted for more than two Müntz monomials, for a weighted measure, or for a discrete sampled least-squares projector.

## Proof

**1. Exact kernel and endpoint reduction.** Set
\[
m=\int_0^1t^\alpha\,dt=\frac1{\alpha+1},\qquad
v=\int_0^1(t^\alpha-m)^2\,dt
=\frac{\alpha^2}{(2\alpha+1)(\alpha+1)^2}>0.
\]
The functions \(1\) and \((t^\alpha-m)/\sqrt v\) form an orthonormal basis for \(V_\alpha\), so
\[
K_\alpha(x,y)=1+\frac{(x^\alpha-m)(y^\alpha-m)}v,
\qquad (P_\alpha f)(x)=\int_0^1K_\alpha(x,y)f(y)\,dy.
\]
For \(\Lambda_\alpha(x)=\int_0^1|K_\alpha(x,y)|\,dy\), the usual kernel bound gives
\(\|P_\alpha\|_{L^\infty\to L^\infty}=\max_{0\le x\le1}\Lambda_\alpha(x)\): the reverse inequality follows by taking the measurable datum \(f(y)=\operatorname{sgn}K_\alpha(x,y)\) for any fixed \(x\), then approaching the endpoint in the output if necessary. Symmetry of the real kernel and integral-operator duality give the identical \(L^1\to L^1\) norm.

The map \(u\mapsto\int_0^1|1+(u-m)(y^\alpha-m)/v|\,dy\) is convex on \([0,1]\), and \(u=x^\alpha\) ranges over all of this interval. Therefore
\(\mathcal L(\alpha)=\max\{\Lambda_\alpha(0),\Lambda_\alpha(1)\}\).

**2. Both exact endpoint masses.** Substitution in the kernel yields
\[
K_\alpha(0,y)=\frac{\alpha+1}{\alpha^2}\left[(\alpha+1)-(2\alpha+1)y^\alpha\right],
\quad
K_\alpha(1,y)=\frac{\alpha+1}{\alpha}\left[(2\alpha+1)y^\alpha-1\right].
\]
Define
\[
h_0=\left(\frac{\alpha+1}{2\alpha+1}\right)^{1/\alpha},
\qquad h_1=(2\alpha+1)^{-1/\alpha}.
\]
The first endpoint kernel changes sign once at \(y=h_0\), from positive to negative; the second changes sign once at \(y=h_1\), from negative to positive. Since both endpoint kernels integrate to \(1\), integrating the negative pieces gives
\[
\Lambda_\alpha(0)=2\frac{\alpha+1}{\alpha}h_0-1,
\qquad \Lambda_\alpha(1)=1+2h_1.
\]
These also provide explicit sign-type bounded inputs attaining each endpoint Lebesgue value.

**3. Strict switch at the affine exponent.** The function \(h_1=(1+2\alpha)^{-1/\alpha}\) is strictly increasing: its logarithmic derivative equals
\[
\frac{\log(1+2\alpha)-2\alpha/(1+2\alpha)}{\alpha^2}>0,
\]
since \(\log(1+s)>s/(1+s)\) for \(s>0\). Thus \(\Lambda_\alpha(1)\) strictly increases with \(\alpha\).

To study the other endpoint, write \(t=1/\alpha>0\) and
\[
\frac{\Lambda_\alpha(0)+1}{2}
=(1+t)\left(\frac{1+t}{2+t}\right)^t.
\]
Its logarithmic derivative with respect to \(t\) is
\[
\frac2{t+2}+\log\frac{t+1}{t+2}
=2z+\log(1-z)>0,
\qquad z=\frac1{t+2}\in(0,1/2).
\]
The strict positivity follows from \(g(0)=0\), \(g'(z)=(1-2z)/(1-z)>0\) for \(g(z)=2z+\log(1-z)\). Hence \(\Lambda_\alpha(0)\) strictly *decreases* in \(\alpha\).

At \(\alpha=1\), both endpoint expressions are \(5/3\); their opposite monotonicities show \(\Lambda_\alpha(0)>\Lambda_\alpha(1)\) for \(\alpha<1\), and the reverse for \(\alpha>1\). This proves the piecewise norm formula and unique minimizing exponent.

There are no interior maximizers. Indeed the convex function in \(u\) above has value \(1\) at \(u=m\), strictly below both endpoint values. On each of the intervals \([0,m]\) and \([m,1]\), any non-endpoint value is bounded by a *strict* convex combination of \(1\) and the respective outer endpoint value, so it is smaller than the global endpoint maximum. This proves the full location classification, including the two-endpoint case at \(\alpha=1\).

**4. Christoffel contrast and limits.** Because \(K_\alpha(t,t)=1+(t^\alpha-m)^2/v\), its maximum also occurs at an endpoint. Explicitly,
\[
K_\alpha(0,0)=\frac{(\alpha+1)^2}{\alpha^2},
\quad K_\alpha(1,1)=2(\alpha+1).
\]
Their order reverses precisely at \(\alpha=1\), giving the stated peak. Finally,
\(\alpha^{-1}\log((\alpha+1)/(2\alpha+1))\to-1\) as \(\alpha\downarrow0\), while \(\alpha^{-1}\log(2\alpha+1)\to0\) as \(\alpha\to\infty\). Substitution gives \(\mathcal L(\alpha)\sim2/(e\alpha)\) and \(\mathcal L(\alpha)\to3\). The diagonal limits follow directly from the two elementary formulas.

## Verification

Run `python3 verify_muntz.py` from the extracted package. The checker independently evaluates the moment/variance identities, the two endpoint kernels, the integrated absolute masses, interior convexity bounds, the Christoffel endpoints, and the monotonicity inequalities for an explicit deterministic range of exponents and evaluation points. These tests are checks of algebra and numerical integration, not a replacement for Steps 1–4, which prove the claims for every real \(\alpha>0\). All formulas are reproducible without external data.

## Relationship to prior work

Classical Müntz orthogonalization supplies explicit bases for general real-power polynomial systems (Milovanović, 1999). Hilbertian Müntz embeddings and their compactness/Schatten properties were studied by Noor and Timotin (2011). Cohen and Migliorati (2016) treat general least-squares stability through the Christoffel diagonal and sampling; their bounds concern discretely sampled reconstruction rather than the present exact deterministic \(L^\infty\) projector norm. The affine \(\alpha=1\) value is elementary and is **not** presented as new in isolation. The separate contribution is the full exponent-dependent Lebesgue norm, strict endpoint and optimality classification, and its asymptotic contrast with the Christoffel height.

## Limitations

This is a two-dimensional exact model, not a general theorem about many-term Müntz approximation or optimal random sampling. The elementary orthogonal basis is known; the issue addressed is the sharp endpoint norm and its global parameter optimum. Historical priority is subject to the possibility of a differently formulated formula in older projection-constant or Müntz literature. One potentially relevant 2005 monograph chapter on projection types could not be inspected in full; its available abstract concerns Banach-space projection types and does not settle this precise comparison. No independent scientific audit has been performed.

## References

1. G. V. Milovanović, *Müntz Orthogonal Polynomials and Their Numerical Evaluation*, in *Applications and Computation of Orthogonal Polynomials*, ISNM 131 (1999), 179–194. Author-hosted full text: https://www.mi.sanu.ac.rs/~gvm/radovi/BC16.pdf.
2. S. W. Noor and D. Timotin, *Embeddings of Müntz spaces: the Hilbertian case*, arXiv:1110.5422v1, publicly posted 2011-10-25. https://arxiv.org/abs/1110.5422.
3. A. Cohen and G. Migliorati, *Optimal weighted least-squares methods*, arXiv:1608.00512v1, publicly posted 2016-08-01. https://arxiv.org/abs/1608.00512.
4. V. Gurariy and W. Lusky, *Geometry of Müntz Spaces and Related Questions*, Lecture Notes in Mathematics 1870 (2005), chapter *Projection Types and the Isomorphism Problem for Müntz Spaces*. DOI:10.1007/11551621_10 (full chapter not inspected).
