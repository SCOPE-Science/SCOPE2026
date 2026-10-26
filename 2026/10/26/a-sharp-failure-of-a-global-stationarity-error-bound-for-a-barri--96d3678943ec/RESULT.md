# A sharp failure of a global stationarity error bound for a barrier-induced gap

## Finding

For any fixed parameter \(r>0\), define the one-dimensional reference function
\[
\phi_r(t)=\begin{cases}-r\bigl(\log(1-|t|)+|t|\bigr),&|t|<1,\\+\infty,&|t|\geq1.\end{cases}
\]
Its Fenchel conjugate is \(\phi_r^*(s)=|s|-r\log(1+|s|/r)\). Set
\(f(x)=x^2/2\), \(g(x)=\sin x-x^2/2\), and \(F=f+g=\sin x\). At every \(x_n=2\pi n\), \(n\geq1\), the geometry-specific gap satisfies
\[
D_{\phi_r^*}\bigl(f'(x_n),-g'(x_n)\bigr)
=r\left[t_n-\log(1+t_n)\right]\sim\frac{r}{2x_n^2}\longrightarrow0,
\qquad t_n=\frac{1}{r+x_n-1},
\]
while the Euclidean stationarity residual is \(|F'(x_n)|=1\). Therefore no global error-bound function \(\omega\) with \(\omega(s)\to0\) as \(s\downarrow0\) can satisfy \(|F'(x)|\leq\omega(D_{\phi_r^*}(f'(x),-g'(x)))\) for all \(x\) in this problem class.

## Assumptions and scope

The smooth term \(f\) has globally 1-Lipschitz gradient. The regularizer \(g\) is smooth and nonconvex. It is prox-bounded with threshold 1 because, for \(0<\gamma\leq1\),
\[
g(x)+\frac{x^2}{2\gamma}=\sin x+\left(\frac{1}{2\gamma}-\frac12\right)x^2
\]
is bounded below, whereas for \(\gamma>1\) it is unbounded below. The total objective \(F(x)=\sin x\) is bounded below by \(-1\). The reference function is even, \(r\)-strongly convex on its effective domain, and has gradient magnitude diverging at the boundary. This is a deterministic, zero-noise example; it tests the pointwise relation between the stated gap and Euclidean stationarity, not the trajectory of a particular algorithm.

## Proof

For \(s>0\), solving \(s=\phi_r'(t)=rt/(1-t)\) gives \(t=s/(r+s)\). Substitution into the Fenchel transform yields \(\phi_r^*(s)=s-r\log(1+s/r)\); evenness gives the formula for all real \(s\). Thus, for positive \(u,v\), \((\phi_r^*)'(v)=v/(r+v)\).

At \(x_n=2\pi n\), \(f'(x_n)=x_n\) and \(-g'(x_n)=x_n-1>0\). Direct substitution into the Bregman divergence gives
\[
\begin{aligned}
D_{\phi_r^*}(x_n,x_n-1)
&=\phi_r^*(x_n)-\phi_r^*(x_n-1)-(\phi_r^*)'(x_n-1)\\
&=r\left[\frac{1}{r+x_n-1}-\log\left(1+\frac{1}{r+x_n-1}\right)\right].
\end{aligned}
\]
For \(t\downarrow0\), \(t-\log(1+t)=t^2/2+O(t^3)\), proving the asserted asymptotic decay. On the other hand, \(F'(x)=\cos x\), so \(|F'(x_n)|=1\) for every \(n\). If a global error bound \(\omega\) with \(\omega(s)\to0\) at zero existed, its right-hand side along \(x_n\) would tend to zero while its left-hand side remained one, a contradiction.

## Verification

The conjugate and gap formula are obtained analytically; no numerical fitting or finite-enumeration inference is used. The asymptotic uses the Taylor expansion of \(\log(1+t)\) at zero. The prox-boundedness threshold follows directly from the displayed quadratic coefficient. The counterexample proves failure of a uniform pointwise gap-to-residual error bound under these assumptions. It does not prove that any particular algorithm generates the sequence \((x_n)\), nor does it refute a convergence theorem stated only in the geometry-specific gap.

## Relationship to prior work

Oikonomidis et al. introduce the same Bregman gap \(D_{\phi^*}(\nabla f(x),-\widetilde\nabla g(x))\) for proximal preconditioned stochastic methods and explicitly note that their analysis does not generally yield rates for standard stationarity measures. Their barrier example has \(\nabla\phi^*(s)=s/(r+|s|)\), which gives the conjugate used here. The present result supplies an explicit smooth, lower-bounded composite objective and an exact sequence showing why a global conversion to Euclidean stationarity cannot be assumed from the stated general hypotheses alone. Yamashita, Takahashi, and Takeda analyze a different Bregman-proximal stationarity residual under a convex nonsmooth term; their result does not imply an error bound for this distinct conjugate-Bregman gap with a nonconvex prox-bounded term.

## Limitations

This is a metric-separation example, not an algorithm-trajectory counterexample. It establishes that additional assumptions—such as a bounded range of the two gradient arguments or a separate error-bound condition—are needed for a uniform conversion from this gap to Euclidean stationarity. It makes no claim that such assumptions are necessary for every individual problem or that the source paper's algorithm fails to converge in its stated gap.

## References

1. K. Oikonomidis, J. Quan, K. Antonakopoulos, A. Silveti-Falls, V. Cevher, and P. Patrinos, “Constrained Stochastic Spectral Preconditioning Converges for Nonconvex Objectives,” arXiv:2605.11850v1, first public 2026-05-12. Relevant material: Example 2.3, Section 4.1, Remark 4.6, and the definition of the gap.
2. Y. Yamashita, S. Takahashi, and A. Takeda, “Accelerated Bregman Proximal Gradient Methods from Dual Geometric Perspectives,” arXiv:2609.34773v1, first public 2026-09-28. Relevant material: Sections 1–2 and the nonconvex stationarity discussion; its residual is not the same gap used here.
3. R. T. Rockafellar, *Convex Analysis*, Princeton University Press, 1970, for the Fenchel conjugacy framework.
