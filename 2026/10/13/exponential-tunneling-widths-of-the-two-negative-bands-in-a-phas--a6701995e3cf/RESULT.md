# Exponential tunneling widths of the two negative bands in a phase-twisted square quantum graph
## Finding
For the equilateral square quantum graph of Exner--Tater with edge length \(\ell>0\), vertex coupling \(U=e^{i\mu}R\), and fixed \(0<\mu<\pi/2\), set
\[t=\tan(\mu/2),\qquad u=\tan(\mu/2+\pi/4)=\frac{1+t}{1-t}.\]
As \(\ell\to\infty\), the negative spectrum consists of exactly two Bloch bands, one near \(-t^2\) and one near \(-u^2\). Writing \(Q=\cos\theta_1+\cos\theta_2\in[-2,2]\), their energies have the uniform expansions
\[E_t(Q)=-t^2-2t^2Qe^{-t\ell}+O(\ell e^{-2t\ell}),\]
\[E_u(Q)=-u^2+2u^2Qe^{-u\ell}+O(\ell e^{-2u\ell}).\]
Consequently their energy widths are
\[W_t(\ell)=8t^2e^{-t\ell}+O(\ell e^{-2t\ell}),\qquad W_u(\ell)=8u^2e^{-u\ell}+O(\ell e^{-2u\ell}).\]
The exact normalized secular equation contains the quasimomentum term \(4Q\kappa(1+\kappa^2)\sin(2\mu)^{-1}(e^{-\kappa\ell}-e^{-3\kappa\ell})\). Hence the \(O(e^{-2\kappa\ell})\) remainder printed in Eq. (26) of the source is not uniform in quasimomentum; the generic first correction is of order \(e^{-\kappa\ell}\). The asymptotics are for fixed \(\mu\) and are not asserted uniformly as \(\mu\to0\) or \(\mu\to\pi/2\).

## Assumptions and scope
Consider the periodic square metric graph and the coupling convention of Exner and Tater, with the coupling length scale normalized to one, edge length \(\ell>0\), and \(U=e^{i\mu}R\) for fixed \(0<\mu<\pi/2\). Negative energy is written as \(-\kappa^2\) with \(\kappa>0\), and \(Q=\cos\theta_1+\cos\theta_2\in[-2,2]\). The limit is \(\ell\to\infty\) at fixed \(\mu\). No uniformity at the endpoint phases is claimed.

## Proof
The source gives the negative-energy secular equation \(P(\kappa,Q;\ell)=\sum_{j=0}^4 c_j\kappa^j=0\), where
\[
\begin{aligned}
c_0=c_4&=\sin(2\mu)\sinh^2(\kappa\ell),\\
c_2&=-\sin(2\mu)\bigl(1+3\cosh(2\kappa\ell)\bigr),\\
c_1&=-2\bigl(2\cos(2\mu)\cosh(\kappa\ell)-Q\bigr)\sinh(\kappa\ell),\\
c_3&=2\bigl(2\cos(2\mu)\cosh(\kappa\ell)+Q\bigr)\sinh(\kappa\ell).
\end{aligned}
\]
Put \(s=\sin(2\mu)\), \(c=\cos(2\mu)\), and \(y=e^{-\kappa\ell}\). Multiplying the secular equation by \(4e^{-2\kappa\ell}/s\) gives the exact identity
\[
0=F(\kappa)+\frac{4Q\kappa(1+\kappa^2)}{s}(y-y^3)-2(1+\kappa^2)^2y^2+B(\kappa)y^4,
\]
where
\[
F(\kappa)=\kappa^4+1-6\kappa^2+4\kappa(\kappa^2-1)\cot(2\mu),
\]
and
\[
B(\kappa)=\kappa^4+1-6\kappa^2-4\kappa(\kappa^2-1)\cot(2\mu).
\]
Thus the first quasimomentum-dependent correction is proportional to \(e^{-\kappa\ell}\), not \(e^{-2\kappa\ell}\).

With \(t=\tan(\mu/2)\), the polynomial \(F\) factors as
\[
F(\kappa)=\frac{(\kappa-t)(1+t\kappa)((t-1)\kappa+t+1)((t+1)\kappa+1-t)}{t(t^2-1)}.
\]
Its positive roots are the simple roots \(t\) and \(u=(1+t)/(1-t)\). The source proves that the negative spectrum has at most two bands. The implicit-function theorem applied uniformly for \(Q\in[-2,2]\) therefore yields, for all sufficiently large \(\ell\), one band near each positive root and no additional negative band.

At the first root,
\[
\frac{4t(1+t^2)}{sF'(t)}=-t,
\]
while at the second root,
\[
\frac{4u(1+u^2)}{sF'(u)}=u.
\]
Since replacing \(e^{-\kappa\ell}\) by \(e^{-r\ell}\) at a root \(r\in\{t,u\}\) incurs an error \(O(\ell e^{-2r\ell})\), solving the exact normalized equation gives
\[
\kappa_t(Q)=t+tQe^{-t\ell}+O(\ell e^{-2t\ell}),
\]
\[
\kappa_u(Q)=u-uQe^{-u\ell}+O(\ell e^{-2u\ell}),
\]
uniformly for \(Q\in[-2,2]\). Squaring and inserting the negative sign gives the two energy expansions in the finding. For large \(\ell\), the derivative with respect to \(Q\) keeps its leading sign, so the band edges occur at \(Q=\pm2\); subtracting them gives the stated widths.

## Verification
The algebra can be checked directly by expanding the hyperbolic functions in powers of \(e^{-\kappa\ell}\). The accompanying checker evaluates the exact normalized secular equation, locates the two fiber roots at \(Q=\pm2\), and verifies convergence of the measured band widths to the two leading formulas. The numerical checks are corroborative; the proof is the exact normalization and implicit-function argument above.

## Relationship to prior work
Exner and Tater identify the same two limiting negative-energy centers and state that the negative bands shrink to them for large \(\ell\). Their Eq. (26) records a quasimomentum-dependent remainder as \(O(e^{-2\kappa\ell})\). Direct normalization of their printed coefficients (22) instead produces an explicit \(e^{-\kappa\ell}\) term unless \(Q=0\). The present result resolves the leading fiber splitting and gives the exact exponential widths. Earlier and later preferred-orientation quantum-graph papers located in the comparison search concern different lattices or positive/high-energy spectral behavior and do not supply these two negative-band width laws.

## Limitations
The expansion is pointwise in fixed \(0<\mu<\pi/2\); constants are not claimed uniform as \(\mu\) approaches either endpoint. It addresses the two negative Bloch bands in the large-edge-length regime and does not modify claims about the positive spectrum. The source discrepancy is identified from the printed secular coefficients; no claim is made about unpublished derivations or author intent.

## References
1. P. Exner and M. Tater, “Quantum graphs: self-adjoint, and yet exhibiting a nontrivial \(\mathcal{PT}\)-symmetry,” Physics Letters A 416 (2021), 127669; arXiv:2108.04708v1.
2. P. Exner and J. Pekař, “Spectral properties of hexagonal lattices with the \(-R\) coupling,” arXiv:2409.03538v1.
