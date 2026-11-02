# Cut-information geometry of Gaussian Brownian endpoint bridges

## Finding

Let \(B\) be a standard Brownian bridge on \([0,1]\), let \((Y_0,Y_1)\) be an independent centered Gaussian endpoint vector with covariance
\[
C=\begin{pmatrix}a&c\\c&b\end{pmatrix}\succeq0,
\]
and put \(X_s=B_s+(1-s)Y_0+sY_1\). For an interior cut \(0<t<1\), define the *conditional path information* (in natural logarithm units)
\[
\mathcal I_C(t)=I\bigl(\sigma(X_s:0\le s\le t);\sigma(X_s:t\le s\le1)\mid X_t\bigr).
\]
This is conditional mutual information between the full continuous left and right paths, not merely a finite-dimensional proxy.

**Exact finite formula.** If \(C\) is positive definite and \(\Delta=ab-c^2>0\), then
\[
\boxed{\displaystyle
\mathcal I_C(t)=-\frac12\log\left(1-
\frac{(\Delta-c)^2}
{\bigl(b+\Delta(1-t)/t\bigr)\bigl(a+\Delta t/(1-t)\bigr)}\right).}
\]
It is identically zero precisely for \(\Delta=c\). Otherwise its unique maximum occurs at
\[
\boxed{\displaystyle t_*={\sqrt a\over\sqrt a+\sqrt b}},
\qquad
\boxed{\displaystyle \max_{0<t<1}\mathcal I_C(t)
=-\frac12\log\left(1-\left({\Delta-c\over\Delta+\sqrt{ab}}\right)^2\right).}
\]
In particular, the maximizing cut is independent of the endpoint cross-covariance \(c\).

**Hard endpoint classification.** If \(C\) is singular, \(\mathcal I_C(t)=+\infty\) at every interior cut exactly when \(c\ne0\) (equivalently, the two nonconstant endpoint values are deterministically linked). Every other singular case has \(\mathcal I_C(t)=0\) at every cut. Thus the information profile is zero for precisely the Markov members of the entire positive-semidefinite endpoint family, finite and positive for its non-Markov positive-definite members, and infinite for its non-Markov singular members.

**Cut-gluing interpretation.** Let \(P_C\) be the law of \(X\) on continuous paths. For a cut \(t\), make \(Q_{C,t}\) by drawing \(X_t\) from its original marginal and, conditional on it, drawing the two adjacent path pieces independently from their original conditional marginal laws. Then
\[
\boxed{D_{\mathrm{KL}}(P_C\Vert Q_{C,t})=\mathcal I_C(t).}
\]
When this divergence is finite, \(Q_{C,t}\) is the unique relative-entropy closest law among all continuous-path laws that factor into independent left and right pieces conditional on the cut value. This is a *single-cut* gluing property; no claim is made that \(Q_{C,t}\) is Markov simultaneously at every time.

## Assumptions and scope

A standard Brownian bridge is the mean-zero continuous Gaussian process with covariance \(\min(s,u)-su\), pinned at both endpoints. The Gaussian endpoint vector may be degenerate. All independent objects are defined on a common probability space; sigma-fields are taken with their completed regular conditional distributions on Polish continuous-path spaces. Conditional mutual information is defined as the expected Kullback–Leibler divergence between the conditional joint left/right law and the product of its conditional marginal laws; it may be infinite. The time cut always satisfies \(0<t<1\). The optimizer assertion requiring uniqueness is restricted to \(C\succ0\) and \(\Delta\ne c\). Logs are natural. The ordinary bridge-plus-random-endpoints construction is the family considered here, distinct from the null-space pseudoinverse Gaussian family in the accompanying operator classifications.

## Proof

**1. Two path segments reduce exactly to two endpoint variables.** Fix \(0<t<1\) and write \(Z=X_t\). The continuous left segment includes \(Y_0=X_0\) and \(Z\); the continuous right segment includes \(Y_1=X_1\) and \(Z\). Subtract the affine interpolant on each side:
\[
R^-_s=X_s-\left(1-{s\over t}\right)Y_0-{s\over t}Z\quad(0\le s\le t),
\]
\[
R^+_s=X_s-{1-s\over1-t}Z-{s-t\over1-t}Y_1\quad(t\le s\le1).
\]
Because the affine endpoint term in \(X\) disappears under this subtraction, these are precisely the residuals obtained by conditioning the underlying Brownian bridge at time \(t\). Standard Gaussian conditioning gives two independent Brownian bridges of durations \(t\) and \(1-t\), jointly independent of \((Y_0,Y_1,B_t)\), hence independent of \((Y_0,Y_1,Z)\). The transformations from each full path piece to the corresponding pair (endpoint, residual), conditional on \(Z\), are measurable bijections. The chain rule and independent-noise invariance of conditional mutual information therefore give the exact identity
\[
\mathcal I_C(t)=I(Y_0;Y_1\mid Z).
\tag{1}
\]
This argument covers continuous paths without taking an unproved infinite-mesh limit.

**2. Conditional Gaussian precision.** We have the scalar observation model
\[
Z=(1-t)Y_0+tY_1+\xi,
\qquad \xi=B_t\sim N(0,t(1-t)),
\]
with \(\xi\) independent of the endpoints. If \(C\succ0\), the posterior precision matrix of \(Y=(Y_0,Y_1)^\top\) given \(Z\) is
\[
J_t=C^{-1}+{1\over t(1-t)}
\begin{pmatrix}1-t\\t\end{pmatrix}
\begin{pmatrix}1-t&t\end{pmatrix}
=\begin{pmatrix}
 b/\Delta+(1-t)/t&1-c/\Delta\\
 1-c/\Delta&a/\Delta+t/(1-t)
\end{pmatrix}.
\]
For a nonsingular bivariate Gaussian, the squared correlation computed from its precision matrix is \(J_{01}^2/(J_{00}J_{11})\); its mutual information equals \(-\tfrac12\log(1-\rho^2)\). Thus (1) gives the displayed exact expression. Positive definiteness of \(J_t\) ensures \(0\le\rho^2<1\). The information is zero exactly when \(1-c/\Delta=0\), namely \(\Delta=c\).

**3. Global cut optimization.** Put \(r=(1-t)/t>0\). The information is strictly increasing in
\[
\rho^2(r)={ (\Delta-c)^2\over (b+\Delta r)(a+\Delta/r)},
\]
provided \(\Delta\ne c\). The denominator expands to
\[
ab+\Delta^2+\Delta(ar+b/r).
\]
Since \(a,b,\Delta>0\), the arithmetic-geometric mean inequality gives \(ar+b/r\ge2\sqrt{ab}\) with equality *only* at \(r=\sqrt{b/a}\). This proves unique maximization at \(t_*=\sqrt a/(\sqrt a+\sqrt b)\). At that cut, the denominator is \((\Delta+\sqrt{ab})^2\), proving the maximum formula. If \(\Delta=c\), \(\rho^2=0\) for all \(t\), so there is intentionally no unique optimum.

**4. Complete treatment of singular endpoint matrices.** For a singular positive-semidefinite \(2\times2\) matrix, either \(c=0\) and at most one endpoint has positive variance, or \(c\ne0\) and there is a nondegenerate scalar Gaussian \(G\) with \(Y_0=v_0G,Y_1=v_1G\) for constants \(v_0v_1\ne0\). In the first case one endpoint variable is deterministic, and (1) yields zero. In the second case, \(Z=((1-t)v_0+tv_1)G+\xi\), with independent \(\xi\) of strictly positive variance \(t(1-t)\). Therefore \(\operatorname{Var}(G\mid Z)>0\) for every interior \(t\), even if the Gaussian signal coefficient vanishes. Conditionally on \(Z\), the joint law of \((Y_0,Y_1)\) is supported on the line \(v_1Y_0=v_0Y_1\), whereas the product of its two non-atomic conditional marginals assigns that line probability zero. The conditional relative entropy is infinite. This proves the singular dichotomy. Together with the known Markov characterization \(\Delta=c\) in the nonsingular case, it also establishes the claimed zero/finite/infinite classification.

**5. Exact Markov-gluing information cost.** Let \(L=(X_s)_{0\le s\le t}\), \(R=(X_s)_{t\le s\le1}\), and \(Z=X_t\); their path spaces are standard Borel and admit regular conditional distributions. By definition, \(Q_{C,t}\) has \(P_Z\) as its cut law and conditional product \(P_{L\mid Z}\otimes P_{R\mid Z}\). Thus the chain rule for relative entropy gives
\[
D(P_C\Vert Q_{C,t})
=\int D(P_{L,R\mid Z=z}\Vert P_{L\mid Z=z}\otimes P_{R\mid Z=z})P_Z(dz)
=\mathcal I_C(t).
\]
For any alternative single-cut-factorized \(Q\) (which necessarily has some cut law \(Q_Z\) and product conditional laws), KL disintegration adds three nonnegative terms: \(D(P_Z\Vert Q_Z)\) and the respective expected divergences of the two conditional marginals, over and above \(\mathcal I_C(t)\). Consequently \(Q_{C,t}\) uniquely attains the minimum when \(\mathcal I_C(t)<\infty\). If the minimum is infinite, no claim of a unique projection is made.

## Verification

Run `python verify.py` from the directory containing this file. It uses only Python's standard library and exact rational arithmetic for the substantive identities. The independently written checker compares the posterior-precision expression with the three-point conditional-covariance calculation; checks that two *sampled path pieces* (one interior point on each side plus their endpoints) have exactly the same Gaussian information ratio as the endpoints alone; tests the global optimizing cut over a rational grid and the closed-form optimum; and checks the noise-positive singular boundary. Its deterministic output is:

```
PASS 10704 exact-rational assertions
Example C=I, maximal conditional path information (nats): 0.143841036226
Unique maximizing cut for (a,b)=(1,4): 1/3
```

The finite tests do not prove a statement about infinite paths. The analytical Brownian bridge disintegration, Gaussian posterior precision, AM–GM inequality, singular-support argument, and KL chain rule do that. As a simple analytic example, for \(C=I_2\) the unique maximizing cut is \(t=1/2\) and its information is \(-\tfrac12\log(3/4)\) nats.

## Relationship to prior work

Raket's October 24, 2026 *Bestiary of Brownian Processes* provides the starting Brownian boundary-condition catalogue, nonlocal endpoint couplings, and the conditional split example in Section 6.1. His October 27, 2026 *Brownian covariances on an interval* subsequently identifies the complete bridge-plus-endpoints representation and independently characterizes Markov members by \(\det C=c\) (Proposition 3.2); that qualitative criterion is **not** claimed as new. The present theorem supplies the full *conditional path-information profile*, a sharp universal optimizing cut, the singular finite/infinite transition, and the exact KL cost of a single-cut independent gluing, none of which is stated in that paper. The proof uses standard Gaussian mutual-information identities and the Markov splitting of a conditioned Brownian bridge; the new step is their complete information-theoretic synthesis and optimization across the classified endpoint family.

Kholkin, Butakov, Burnaev, Gushchin and Korotin's InfoBridge work proves a path-level KL identity for differently coupled endpoint measures and studies generic mutual-information estimation by diffusion bridges, but does not give the conditional left/right path statistic or its optimizer for Raket's endpoint covariance cone. Schröfl and Floerchinger's Gaussian-field analysis treats Gaussian spatial mutual information and relative entropy for other boundary geometries, including non-touching subregions, rather than this conditional cut and sharp optimization. Baker's classical work concerns generic covariance-operator mutual information; only the abstract was accessible in this review, so unobserved direct precedent remains a priority risk.

## Limitations

The formula applies to Raket's *ordinary* Brownian endpoint-covariance class; it is not asserted for the distinct null-space pseudoinverse Gaussian family or non-Gaussian endpoints. The conditional mutual-information statistic concerns a single deterministic time cut; it is not entropy production, ordinary unconditional past/future mutual information, or a global distance to all Markov process laws. Singular non-Markov endpoint distributions give infinite KL, which does not mean that every weaker probability metric diverges. Independent historical-priority validation has not been performed. Exact-rational finite tests do not constitute infinite-dimensional certificates.

## References

1. L. L. Raket, *A Bestiary of Brownian Processes: A Field Guide to Boundary Conditions and Conditioning*, arXiv:2610.33747v1, first posted 2026-10-24, especially Sections 3, 4, and 6.1. https://arxiv.org/html/2610.33747v1
2. L. L. Raket, *Brownian covariances on an interval: a complete endpoint classification*, arXiv:2610.36762v1, first posted 2026-10-27, especially Theorem 2.1 and Proposition 3.2. https://arxiv.org/html/2610.36762v1
3. S. Kholkin, I. Butakov, E. Burnaev, N. Gushchin and A. Korotin, *InfoBridge: Mutual Information estimation via Bridge Matching*, arXiv:2502.01383, especially Sections 2 and 4.1 and Appendix B.4. https://arxiv.org/html/2502.01383v4
4. M. Schröfl and S. Floerchinger, *Relative Entropy and Mutual Information in Gaussian Statistical Field Theory*, *Annales Henri Poincaré* 26 (2025), 3233–3319, online 2024-12-17, especially Section 4.3. https://doi.org/10.1007/s00023-024-01522-2
5. C. R. Baker, *Mutual Information for Gaussian Processes*, *SIAM Journal on Applied Mathematics* 19 (1970), 451–458. https://doi.org/10.1137/0119044
