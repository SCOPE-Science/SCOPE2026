# An exact thermal phase transition for covariance-fidelity Schmidt-number certification
## Finding
Consider the equal-temperature two-mode squeezed thermal state \(\rho_{\mathrm{TMST}}(r,\beta)\) and the optimized covariance-only fidelity witness introduced for this family in Ref. [1]. Put
\[
u=\operatorname{coth}(\beta/2),\qquad \beta_c=\log(2+\sqrt{3})\approx1.3169578969.
\]
Then the fidelity certificate has an exact temperature transition. If \(0<\beta\le\beta_c\), its optimized fidelity lower bound is exactly zero for every finite squeezing \(r\ge0\). Hence that certificate cannot prove Schmidt number larger than \(1\), no matter how large the squeezing is. By contrast, the entanglement-of-formation certificate computed from the same covariance matrix proves Schmidt number growing like \((e/(4u))e^{2r}\), so the failure is a property of the covariance-to-fidelity conversion rather than a lack of high-dimensional information in the measured second moments.

If \(\beta>\beta_c\), the optimized fidelity lower bound approaches a positive constant and the same fidelity certificate eventually proves an exponentially growing Schmidt number. Writing
\[
a_\beta=\frac{1}{\sqrt2\sinh(\beta/2)},
\]
its asymptotic certified dimension is
\[
K_{\mathrm{fid}}(r,\beta)\sim C_\beta e^{2r},\qquad C_\beta=\frac{u}{4}\left[-\log\!\left(1-(1-a_\beta)^2\right)\right].
\]
Thus \(\beta_c\) is the exact all-squeezing boundary between complete failure and exponential growth for this particular covariance-fidelity certificate.

## Assumptions and scope
The state is exactly the symmetric two-mode squeezed thermal family of Ref. [1], with equal inverse temperatures \(\beta>0\), real squeezing \(r\ge0\), and the covariance convention of that paper. The target family is the paper's pure two-mode squeezed-vacuum family and the target squeezing is optimized exactly as in its Eq. (50). The statement concerns the paper's lower fidelity bound and the Schmidt-number witness constructed from that lower bound; it does not claim that the physical state is separable when the bound vanishes.

For the comparison with entanglement of formation, the same covariance matrix is used and the asymptotic statement concerns \(r\to\infty\) at fixed finite \(\beta\). Logs are natural logs, as in Ref. [1]. The paper's older linear Gaussian Schmidt-number witnesses [2] and newer phase-space methods [3] are different witness families and are not bounded by the transition proved here.

## Proof
Ref. [1], Eqs. (50)--(52), gives
\[
s_{\mathrm{opt}}=\frac12\operatorname{arsinh}(u\sinh(2r))
\]
and
\[
\widetilde R_{\mathrm{opt}}^2=u\cosh(2r)\left(ue^{2r}-e^{2s_{\mathrm{opt}}}\right).
\]
Set \(C=\cosh(2r)\) and \(S=\sinh(2r)\). Since \(e^{\operatorname{arsinh}x}=x+\sqrt{1+x^2}\),
\[
e^{2s_{\mathrm{opt}}}=uS+\sqrt{1+u^2S^2}.
\]
Using \(e^{2r}=C+S\) and rationalizing gives
\[
\widetilde R_{\mathrm{opt}}^2
=uC\left(uC-\sqrt{1+u^2S^2}\right)
=\frac{uC(u^2-1)}{uC+\sqrt{1+u^2S^2}}.
\]
Because \(u>1\), one has \(\sqrt{1+u^2S^2}<uC\). Therefore
\[
\widetilde R_{\mathrm{opt}}^2>\frac{u^2-1}{2}
\]
for every finite \(r\). Also \(\sqrt{1+u^2S^2}/(uC)\to1\), so
\[
\lim_{r\to\infty}\widetilde R_{\mathrm{opt}}^2=\frac{u^2-1}{2}=\frac{1}{2\sinh^2(\beta/2)}.
\]
The limiting value equals \(1\) exactly when
\[
\sinh(\beta/2)=\frac{1}{\sqrt2},
\]
which is equivalent to \(\beta=\log(2+\sqrt3)\). Hence for \(0<\beta\le\beta_c\), \(\widetilde R_{\mathrm{opt}}>1\) at every finite \(r\), and Ref. [1], Eq. (51), gives \(\widetilde F_{\mathrm{opt}}=0\).

For \(\beta>\beta_c\), let \(a_\beta=1/(\sqrt2\sinh(\beta/2))<1\). Then
\[
\widetilde F_{\mathrm{opt}}\longrightarrow (1-a_\beta)^2=:F_\infty>0.
\]
Ref. [1], Eq. (53), is a geometric sum:
\[
B_k=1-\tanh^{2k}(s_{\mathrm{opt}}).
\]
Its strict witness condition \(\widetilde F_{\mathrm{opt}}>B_k\) is therefore equivalent to
\[
k<\frac{\log(1-\widetilde F_{\mathrm{opt}})}{\log(\tanh^2s_{\mathrm{opt}})}.
\]
Since the certified Schmidt number is one larger than the largest admissible \(k\), the integer lower bound is the ceiling displayed in the finding. Further,
\[
s_{\mathrm{opt}}=r+\frac12\log u+o(1),\qquad
\log(\tanh^2s_{\mathrm{opt}})=-\frac{4}{u}e^{-2r}+o(e^{-2r}),
\]
which yields the coefficient \(C_\beta\).

Finally, Ref. [1], Eqs. (40) and (54), gives
\[
\log\operatorname{SN}(\rho_{\mathrm{TMST}})\ge h(ue^{-2r}).
\]
For \(z\downarrow0\), the explicit function in its Eq. (33) satisfies
\[
h(z)=1-\log(4z)+o(1).
\]
Consequently
\[
\exp h(ue^{-2r})\sim\frac{e}{4u}e^{2r},
\]
which proves the same-covariance separation on both sides of \(\beta_c\).

## Verification
The algebraic identity for \(\widetilde R_{\mathrm{opt}}^2\), the exact value of \(\beta_c\), the geometric reduction of \(B_k\), and both large-squeezing coefficients are checked in `artifacts/verify.py`. The script compares the source form and the rationalized form at representative points on both sides of the threshold and verifies convergence of the two asymptotic ratios. These finite checks corroborate the analytic argument; they are not used as a proof of the all-parameter inequalities.

## Relationship to prior work
Ref. [1] introduces the covariance-fidelity method, derives the exact finite-parameter formulas used above, and compares several certification methods numerically. Its displayed examples include a very noisy case and show that fidelity-based certification can be weak, but it does not identify an all-squeezing critical inverse temperature, prove the exact boundary \(\log(2+\sqrt3)\), invert the TMSV threshold to a closed integer formula, or derive the exponential rates above and below the boundary. Full-text searches of Ref. [1] found no asymptotic theorem or occurrence of the critical constant.

Ref. [2] develops a broader class of Gaussian Schmidt-number witnesses based on covariance matrices and explicitly treats squeezed thermal states, but it is a different witness construction and does not imply a limitation of the covariance-to-fidelity lower bound introduced in Ref. [1]. Ref. [3] uses infinite-dimensional Bloch-operator covariances and likewise does not analyze the Ref. [1] fidelity conversion. The new statement is therefore a method-specific sharp phase diagram, not a claim that no covariance-based witness can certify entanglement above the corresponding temperature.

## Limitations
The threshold is specific to the optimized lower fidelity bound of Ref. [1] for equal-temperature TMST states and TMSV targets. It is not a thermodynamic phase transition, not an entanglement threshold of the state, and not a limitation on exact-fidelity, linear-Gaussian, EoF, or phase-space Schmidt-number witnesses. The asymptotic formulas keep \(\beta\) fixed while \(r\to\infty\). No optimality claim is made among all possible moment-based or experimentally accessible witnesses.

## References
[1] Ida Mishra, Simon Morelli, Kl\u00e1ra Baksov\u00e1, Phila Rembold, and Nicolai Friis, "Certification of high-dimensional entanglement in continuous-variable systems," arXiv:2610.03113v1 (first public 2026-10-02), especially Eqs. (33), (40), and (50)--(54).

[2] Farid Shahandeh, Jan Sperling, and Werner Vogel, "Operational Gaussian Schmidt-number witnesses," Phys. Rev. A 88, 062323 (2013), arXiv:1309.6508.

[3] Shuheng Liu, Jiajie Guo, Matteo Fadel, Qiongyi He, Marcus Huber, and Giuseppe Vitagliano, "Entanglement Dimensionality of Continuous Variable States From Phase-Space Quasi-Probabilities," arXiv:2509.02743v1 (2025).
