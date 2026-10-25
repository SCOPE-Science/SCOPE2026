# Exact phase stiffness of the cut–conjugate gap across pitch in path groups

## Finding

Let \(G=\mathbb R\oplus\mathbb R^n\oplus\mathbb R^n\), \(n\ge2\), be the step-two Carnot group with the path-geometry structure and the normalization of Návrat–Zalabová. For a unit-speed normal geodesic with parameters \(\rho>0\), \(\sigma>0\), and phase \(\alpha\in S^1\), use rescaled time \(\tau=t\rho/(2\sqrt{1+\sigma^2})\), so that the cut time is \(\tau_{\mathrm{cut}}=\pi\). In a local real lift of the phase, the first conjugate time has the exact phase-stiffness law

\[
\tau_{\mathrm{conj}}(\sigma,\alpha)=\pi+\kappa(\sigma)\alpha^2+O_\sigma(|\alpha|^3),\qquad \alpha\to0,
\]

where

\[
\kappa(\sigma)=\frac{2\pi\sigma^2}{1+4\sigma^2}.
\]

The same expansion holds near \(\alpha=\pi\), with \(\alpha^2\) replaced by \((\alpha-\pi)^2\). The coefficient is strictly increasing for \(\sigma>0\), starts at \(0\), and tends to \(\pi/2\) as \(\sigma\to\infty\). At \(\sigma=0\), the Heisenberg limit has \(\tau_{\mathrm{conj}}=\pi\) for every phase. Thus the formula quantifies how the conjugate-time branch opens quadratically away from the two exceptional phases for every positive pitch, not just in the small-pitch limit.

## Assumptions and scope

The group, metric, normal-geodesic parameters, and factorized exponential map are those in Návrat–Zalabová, arXiv:2404.01831v1, Sections 3–4. The pitch parameter is \(\sigma\ge0\), the phase is \(\alpha\in S^1\), and the rescaled time is \(\tau=t\rho/(2\sqrt{1+\sigma^2})\). The expansion is local in phase for each fixed \(\sigma>0\); its remainder is uniform when \(\sigma\) ranges over a compact subset of \((0,\infty)\). The \(\sigma=0\) Heisenberg limit is stated separately. No global monotonicity of the conjugate time in pitch is claimed.

## Proof

The factorized exponential-map Jacobian in the source has the form

\[
J_4=\frac{256\sigma}{\rho^9}f(\tau,\alpha)\bigl(A(\tau,\alpha)\sigma^2+B(\tau,\alpha)\bigr),
\]

where \(f(\tau,\alpha)>0\) for \(\tau>0\), and

\[
\begin{aligned}
A(\tau,\alpha)&=\tau^2(\sin\tau-\tau\cos\tau)^2\\
&\quad-(\tau^2-\sin^2\tau)^2\cos^2(\tau+\alpha),\\
B(\tau,\alpha)&=\tfrac12\sin\tau(\sin\tau-\tau\cos\tau)f(\tau,\alpha),\\
f(\tau,\alpha)&=\tau^2-\tau\sin\tau\cos\tau\\
&\quad-2\sin\tau(\sin\tau-\tau\cos\tau)\cos^2(\tau+\alpha).
\end{aligned}
\]

For fixed \(\sigma>0\), set \(F(\tau,\alpha)=A(\tau,\alpha)\sigma^2+B(\tau,\alpha)\). At \(\tau=\pi\), direct substitution gives

\[
f(\pi,\alpha)=\pi^2,\qquad A(\pi,\alpha)=\pi^4\sin^2\alpha,\qquad B(\pi,\alpha)=0.
\]

At the exceptional phase \(\alpha=0\), we have \(F(\pi,0)=0\). Differentiating the displayed formulas yields

\[
\partial_\tau A(\pi,0)=-2\pi^3,\qquad \partial_\tau B(\pi,0)=-\tfrac12\pi^3,
\]

and hence

\[
\partial_\tau F(\pi,0)=-\tfrac12\pi^3(1+4\sigma^2)\ne0.
\]

Also, since \(F(\pi,\alpha)=\pi^4\sigma^2\sin^2\alpha\),

\[
\partial_\alpha F(\pi,0)=0,\qquad \partial_{\alpha\alpha}F(\pi,0)=2\pi^4\sigma^2.
\]

The implicit-function theorem therefore gives a unique smooth root branch \(\tau=\tau(\alpha)\) near \(\alpha=0\). Differentiating \(F(\tau(\alpha),\alpha)=0\), the first derivative vanishes at zero, and the second derivative is

\[
\tau''(0)=-\frac{\partial_{\alpha\alpha}F(\pi,0)}{\partial_\tau F(\pi,0)}=\frac{4\pi\sigma^2}{1+4\sigma^2}.
\]

Taylor's theorem gives

\[
\tau(\alpha)=\pi+\frac12\tau''(0)\alpha^2+O_\sigma(|\alpha|^3)
=\pi+\frac{2\pi\sigma^2}{1+4\sigma^2}\alpha^2+O_\sigma(|\alpha|^3).
\]

The same computation at \(\alpha=\pi\), using the local coordinate \(\beta=\alpha-\pi\), gives the same coefficient because \(\sin^2(\pi+\beta)=\sin^2\beta\) and the corresponding \(\partial_\tau F\) has the same value. For each fixed positive pitch, the source proves there is no conjugate point before \(\tau=\pi\) and that equality with the cut time occurs exactly at the exceptional phases \(0,\pi\). The nearby root branch is therefore the first conjugate-time branch for phases sufficiently close to either exceptional phase. At zero pitch the geodesics reduce to the Heisenberg case, where cut and conjugate times coincide for every phase.

Finally,

\[
\kappa'(\sigma)=\frac{4\pi\sigma}{(1+4\sigma^2)^2}>0\quad(\sigma>0),\qquad \lim_{\sigma\downarrow0}\kappa(\sigma)=0,\qquad \lim_{\sigma\to\infty}\kappa(\sigma)=\frac\pi2.
\]

This proves the stated pitch profile.

## Verification

The coefficient is obtained analytically from the explicit Jacobian factorization, not from numerical fitting. The values of \(A\), \(B\), \(\partial_\tau A\), and \(\partial_\tau B\) at \((\tau,\alpha)=(\pi,0)\) were checked by direct differentiation and symbolic expansion. The implicit-function theorem applies because \(\partial_\tau F(\pi,0)=-\pi^3(1+4\sigma^2)/2\) is nonzero for every fixed \(\sigma\ge0\); for \(\sigma=0\), the Heisenberg equality is handled directly. The monotonicity and limiting values of \(\kappa\) follow by elementary differentiation. No global formula for the conjugate time is claimed.

## Relationship to prior work

Návrat–Zalabová explicitly determine the cut time and cut locus for path-geometry Carnot groups. Their Proposition 4.2 and Theorem 4.3 give the cut time and cut locus; Lemma 4.3 proves \(\tau_{\mathrm{conj}}\ge\pi\) and, for positive pitch, equality exactly at \(\alpha=0,\pi\); the \(\sigma=0\) Heisenberg limit has equality for all phases. Remark 4.3 gives an implicit Jacobian equation and the coarse upper bound \(\tau_{\mathrm{conj}}<\tau_0\), where \(\tan\tau_0=\tau_0\) and \(\tau_0\) is the least positive root beyond \(\pi\). The inspected sections do not state the exact phase-stiffness coefficient \(2\pi\sigma^2/(1+4\sigma^2)\) or its monotone saturation across pitch. The present result is a local refinement, not a new cut-locus description or global conjugate-time classification.

## Limitations

The phase expansion is local near \(\alpha=0,\pi\) and uses the source's canonical pitch and rescaled-time parameters. The error constant may depend on fixed \(\sigma\); uniformity is asserted only on compact pitch intervals bounded away from infinity. No global monotonicity of the conjugate-time function, higher-order phase coefficient, or extension to other Carnot groups is established. Literature searches cannot prove universal novelty; the claim is a focused quantitative refinement of a published implicit equation, and independent audit has not been performed.

## References

1. A. Návrat and L. Zalabová, “Sub-Riemannian optimal synthesis for Carnot groups with the structure of a path geometry,” arXiv:2404.01831v1, first posted 2 April 2024, especially Proposition 4.2, Theorem 4.3, Lemma 4.3, Remark 4.3, and the Jacobian calculation in Section 4.3. https://arxiv.org/abs/2404.01831
2. A. Montanari and D. Morbidelli, “On the sub-Riemannian cut locus in a model of free two-step Carnot group,” arXiv:1608.06431; *Calculus of Variations and Partial Differential Equations* 56 (2017), Paper No. 36. This is related context for cut-time analysis in a different group. https://arxiv.org/abs/1608.06431
