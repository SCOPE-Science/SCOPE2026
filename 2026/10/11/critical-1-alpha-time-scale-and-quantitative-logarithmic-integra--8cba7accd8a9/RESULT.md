# Critical \(1/\alpha\) time scale and quantitative logarithmic-integral limit for nonlinear relaxation
## Finding
Let \(C>0\), \(\alpha>0\), and let \(y_\alpha:[0,\infty)\to[0,1)\) be the increasing solution of
\[
\dot y_\alpha=C(1-y_\alpha^\alpha),\qquad y_\alpha(0)=0.
\]
Define
\[
L(y)=\int_0^y\frac{ds}{-\log s},\qquad
G_\alpha(y)=\alpha\int_0^y\frac{ds}{1-s^\alpha},\qquad 0\le y<1,
\]
with the integrand of \(L\) extended by zero at \(s=0\). Then \(L\) is strictly increasing from \([0,1)\) onto \([0,\infty)\), and for every \(0\le y<1\)
\[
L(y)\le G_\alpha(y)\le L(y)+\alpha y.
\]
Moreover, if \(D_\alpha(y)=G_\alpha(y)-L(y)\), then \(D_\alpha\) extends continuously to \(y=1\) and
\[
\sup_{0\le y\le1}\left|\frac{D_\alpha(y)}{\alpha}-\frac y2\right|\longrightarrow0
\qquad(\alpha\downarrow0).
\]
For any real \(p\), set \(Y_{\alpha,p}(\tau)=y_\alpha(\tau/\alpha^p)\). For every fixed \(\tau>0\),
\[
Y_{\alpha,p}(\tau)\longrightarrow
\begin{cases}
0,&p<1,\\
L^{-1}(C\tau),&p=1,\\
1,&p>1.
\end{cases}
\]
The convergence is uniform on \(0\le\tau\le T\) for \(p<1\), uniform on \(0\le\tau\le T\) for \(p=1\), and uniform on \(\delta\le\tau\le T\) for \(p>1\) whenever \(0<\delta<T\). At the critical scale \(p=1\), writing \(Y(\tau)=L^{-1}(C\tau)\), one has the non-asymptotic bracket
\[
L^{-1}((C\tau-\alpha)_+)\le Y_{\alpha,1}(\tau)\le L^{-1}(C\tau),
\]
and, for every \(0<\tau_0<T\), the first correction
\[
Y_{\alpha,1}(\tau)=Y(\tau)-\frac{\alpha}{2}Y(\tau)(-\log Y(\tau))+o(\alpha)
\]
uniformly for \(\tau\in[\tau_0,T]\). Thus the logarithmic-integral dynamics occur at the critical accelerated time \(t=\tau/\alpha\); on fixed time intervals the original unscaled response converges uniformly to zero.

The function \(L\) is the positive branch \(-\operatorname{li}\) on \((0,1)\), so the critical limit satisfies
\[
\dot Y=-C\log Y,\qquad Y(0)=0
\]
in the continuous inverse-function sense. The theorem therefore separates three genuinely different time regimes rather than assigning the logarithmic-integral dynamics to fixed physical time.

## Assumptions and scope
The statement assumes \(C>0\) and \(\alpha>0\), with the physical solution constrained to \([0,1)\). The parameter \(p\) is any real number and the rescaled time variable is \(\tau\ge0\). The supercritical-time limit \(p>1\) is asserted locally uniformly only away from \(\tau=0\), because every member of the family satisfies \(Y_{\alpha,p}(0)=0\) whereas the limiting profile equals \(1\) at every fixed \(\tau>0\).

No assertion is made here for negative exponents, for perturbations of the scalar vector field, or for joint limits in which \(C\) also varies with \(\alpha\).

## Proof
Separation of variables gives the exact implicit relation
\[
\int_0^{y_\alpha(t)}\frac{ds}{1-s^\alpha}=Ct.
\]
For \(s\in(0,1)\), put \(x=-\log s>0\) and \(u=\alpha x\). The elementary inequalities
\[
\frac{u}{1+u}\le1-e^{-u}\le u
\]
follow respectively from \(e^u\ge1+u\) and \(e^{-u}\ge1-u\). Taking reciprocals and multiplying by \(\alpha\) yields
\[
\frac1{-\log s}\le\frac{\alpha}{1-s^\alpha}\le\frac1{-\log s}+\alpha.
\]
Integration from \(0\) to \(y\) proves
\[
L(y)\le G_\alpha(y)\le L(y)+\alpha y.
\]
Since \(-\log s\sim1-s\) as \(s\uparrow1\), \(L(y)\to\infty\), while \(L\) is continuous and strictly increasing; hence \(L^-1\) exists on \([0,\infty)\).

For the first-order potential correction, write \(s=e^{-x}\). Then
\[
\frac{D_\alpha(y)}{\alpha}
=\int_{-\log y}^\infty q(\alpha x)e^{-x}\,dx,
\qquad
q(u)=\frac1{1-e^{-u}}-\frac1u.
\]
The preceding inequalities give \(0\le q(u)\le1\), and Taylor expansion at \(u=0\) gives \(q(u)\to1/2\). Dominated convergence therefore gives
\[
\int_0^\infty\left|q(\alpha x)-\frac12\right|e^{-x}\,dx\to0.
\]
Every tail integral is bounded by this same quantity, so uniformly for \(0\le y\le1\),
\[
\frac{D_\alpha(y)}{\alpha}=\frac y2+o(1).
\]
This also proves that \(D_\alpha\) has a finite continuous extension at \(y=1\).

Now set \(Y_{\alpha,p}(\tau)=y_\alpha(\tau/\alpha^p)\). Multiplying the separated relation by \(\alpha\) gives exactly
\[
G_\alpha(Y_{\alpha,p}(\tau))=C\tau\alpha^{1-p}.
\]
If \(p<1\), the right side tends to zero and the upper comparison with \(L^-1\) forces \(Y_{\alpha,p}\to0\), uniformly on bounded \(\tau\)-intervals. If \(p=1\), the comparison gives
\[
L^-1((C\tau-\alpha)_+)\le Y_{\alpha,1}(\tau)\le L^-1(C\tau),
\]
which gives uniform convergence on bounded intervals by uniform continuity of \(L^-1\). If \(p>1\), the right side tends to infinity. For any \(r<1\), \(G_\alpha(r)\to L(r)<\infty\); hence \(Y_{\alpha,p}(\tau)>r\) for all sufficiently small \(\alpha\), uniformly when \(\tau\ge\delta>0\). Letting \(r\uparrow1\) proves the third regime.

Finally fix \(0<\tau_0<T\). The critical-scale bracket keeps \(Y_{\alpha,1}\) and \(Y\) inside a compact subinterval of \((0,1)\). Since
\[
L(Y(\tau))-L(Y_{\alpha,1}(\tau))=D_\alpha(Y_{\alpha,1}(\tau))
=\frac\alpha2Y(\tau)+o(\alpha)
\]
uniformly there, the mean-value theorem and \(1/L'(y)=-\log y\) give
\[
Y_{\alpha,1}(\tau)=Y(\tau)-\frac\alpha2Y(\tau)(-\log Y(\tau))+o(\alpha),
\]
uniformly on \([\tau_0,T]\).

## Verification
The proof uses only the exact separated-variable identity and the elementary inequality \(u/(1+u)\le1-e^{-u}\le u\). As a numerical stress check, direct high-precision quadrature at \(\alpha\in\{1,0.3,0.1,0.03,0.01}\) and \(y\in\{0.01,0.2,0.8,0.99}\) satisfied the two-sided potential bound. At \(y=0.6\), the ratios \((G_\alpha-L)/\alpha\) were approximately \(0.36944,0.32245,0.30755,0.30227,0.30076\), approaching the predicted limit \(0.3\). These computations are checks only; no numerical evidence is used in the proof.

The proof does not claim a uniform first-order state expansion through \(\tau=0\), and it does not claim uniform convergence to \(1\) at \(\tau=0\) in the \(p>1\) regime.

## Relationship to prior work
arXiv:2609.31748v1 studies exactly \(\dot y=C(1-y^\alpha)\), gives the separated primitive, and states in its Theorem 9 that the \(\alpha\to0\) limit is logarithmic-integral dynamics. Its displayed l'Hôpital calculation, however, evaluates \((1-y^\alpha)/\alpha\), not the unscaled vector field. The present result keeps the original normalization fixed and identifies the critical time scale explicitly.

The earlier open-access paper by Mrazík, Mareš, and Friess, DOI:10.1007/s11071-024-10370-y, explicitly distinguishes the divided equation \(y'=k(1-y^\beta)/\beta\) from the rescaled equation \(y'=k(1-y^\beta)\). It notes the constant small-\(\beta\) limit of the latter and the logarithmic-integral limit of the former, so that qualitative distinction is prior work. The new content here is the complete power-time-scale trichotomy, the exact non-asymptotic inverse-function bracket, and the uniform first-order correction at the critical scale. Targeted full-text and published-finding searches did not locate those statements or a stronger result implying them.

The published correction DOI:10.1007/s11071-024-10485-2 concerns an unrelated typesetting error in the thermodynamic equation and does not address the singular limit.

## Limitations
The originality comparison is limited to the inspected same-object papers, their correction, targeted web searches, and the published-finding index queries recorded in the review package. An equivalent quantitative singular-perturbation estimate could exist in older or unindexed literature under different normalization terminology. The theorem is scalar and deterministic; it does not address robustness under additive forcing, parameter noise, or coupled relaxation systems.

## References
1. L. Mrazík, “Exact Integration and Invertibility Completeness of the Nonlinear Relaxation Equation,” arXiv:2609.31748v1 (first public 2026-09-23).
2. L. Mrazík, J. Mareš, K. Friess, “Nonlinear step responses and how to find them,” Nonlinear Dynamics, DOI:10.1007/s11071-024-10370-y.
3. L. Mrazík, J. Mareš, K. Friess, “Correction: Nonlinear step responses and how to find them,” DOI:10.1007/s11071-024-10485-2.
