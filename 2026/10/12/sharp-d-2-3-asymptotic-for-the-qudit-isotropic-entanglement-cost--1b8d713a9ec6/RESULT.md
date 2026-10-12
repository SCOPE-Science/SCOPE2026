# Sharp \(d^{-2/3}\) asymptotic for the qudit isotropic entanglement-cost certificate gap
## Finding
For integer \(d\ge3\), let
\[
\rho_{p,d}=(1-p)\Phi^{(d)}+p\frac{I}{d^2},\qquad \eta_d=1-d^{-2},
\]
and let \(U_d(p)=E_{\mathrm F}(\rho_{p,d})\) and \(B_d\) be the cubic-norm lower bound of Fang. Define the maximum certified interval width
\[
G_d=\max_{0\le p\le1}\left[U_d(p)-B_d(1-2\eta_d p)\right].
\]
Then
\[
\lim_{d\to\infty}d^{2/3}G_d=\frac{3}{\ln2}.
\]
Moreover, with
\[
u_d=(d-1)^{1/3}+(d-1)^{-1/3},\qquad
p_d^*=\frac{1-(u_d-1)^{-2}}{\eta_d},
\]
one has
\[
d^{2/3}(1-p_d^*)\longrightarrow1
\]
and
\[
d^{2/3}\left[U_d(p_d^*)-B_d(1-2\eta_d p_d^*)\right]\longrightarrow\frac{3}{\ln2}.
\]
Thus the constant in the published upper bound is attained asymptotically by the transition between the nonlinear and affine branches of the cubic-norm certificate.

## Assumptions and scope
All logarithms denoted \(\log\) are base two and \(\ln\) is natural. The statement concerns the gap between two rigorous bounds on the entanglement cost, not the unknown true regularization gap. The source formulas used are the explicit cubic-norm envelope, the isotropic entanglement-of-formation formula, and the uniform large-dimension upper bound. The branch formula for \(U_d\) is needed only for sufficiently large \(d\).

## Proof
Put \(x=d-1\) and
\[
u_d=x^{1/3}+x^{-1/3}=x^{1/3}(1+x^{-2/3}).
\]
Fang's transition point is
\[
c_{*,d}=2(u_d-1)^{-2}-1.
\]
Choose \(p_d^*\) so that \(1-2\eta_dp_d^*=c_{*,d}\). This gives
\[
p_d^*=\frac{1-(u_d-1)^{-2}}{\eta_d},
\]
and hence
\[
1-p_d^*=\frac{(u_d-1)^{-2}-d^{-2}}{\eta_d}=d^{-2/3}(1+o(1)).
\]
Therefore \(d^{2/3}(1-p_d^*)\to1\).

Write
\[
s_d=3\log u_d,
\qquad
\kappa_d=\frac{d^2-1}{d(d-2)}\log(d-1).
\]
At \(c_{*,d}\), the affine branch of the cubic-norm certificate gives
\[
B_d(c_{*,d})=\log d-s_d\eta_dp_d^*.
\]
Also \(1-p_d^*\sim d^{-2/3}\), whereas
\[
1-p_{\mathrm L,d}=1-\frac{(d-2)^2}{d^2-1}\sim\frac4d.
\]
Thus \(p_d^*<p_{\mathrm L,d}\) for all sufficiently large \(d\), and the affine branch of isotropic entanglement of formation applies:
\[
U_d(p_d^*)=\log d-\kappa_dp_d^*.
\]
Consequently
\[
U_d(p_d^*)-B_d(c_{*,d})
=p_d^*(s_d\eta_d-\kappa_d).
\]
Now
\[
s_d=\log x+3\log(1+x^{-2/3}),
\]
while
\[
\eta_d=\frac{x(x+2)}{(x+1)^2},
\qquad
\kappa_d=\frac{x(x+2)}{x^2-1}\log x.
\]
Hence
\[
s_d\eta_d-\kappa_d
=3\eta_d\log(1+x^{-2/3})
-\frac{2x(x+2)}{(x+1)^2(x-1)}\log x.
\]
The second term is \(O((\log x)/x)=o(x^{-2/3})\), while
\[
3\eta_d\log(1+x^{-2/3})
=\frac{3}{\ln2}x^{-2/3}+o(x^{-2/3}).
\]
Since \(p_d^*\to1\) and \(d^{2/3}x^{-2/3}\to1\), this proves
\[
\liminf_{d\to\infty}d^{2/3}G_d\ge\frac{3}{\ln2}.
\]
Fang's Corollary 13 proves
\[
\limsup_{d\to\infty}d^{2/3}G_d\le\frac{3}{\ln2}.
\]
The two bounds coincide, proving the limit.

## Verification
The proof is symbolic and uses only displayed formulas from the cited sources plus elementary asymptotics. The accompanying script `artifacts/verify_asymptotic.py` evaluates the witness gap and the published global upper bound over increasing dimensions, checks that the witness is below the bound, checks entry into the affine entanglement-of-formation branch, and confirms numerical convergence toward \(3/\ln2\). These finite calculations corroborate but do not replace the limit proof.

## Relationship to prior work
Fang derives the exact cubic-norm envelope and defines \(G_d\), then proves the one-sided estimate
\[
\limsup_{d\to\infty}d^{2/3}G_d\le\frac{3}{\ln2}.
\]
The source does not provide a matching lower sequence or assert equality of the limit. The witness above uses the source's own branch-transition point \(c_{*,d}\) to supply the missing lower asymptotic. Terhal and Vollbrecht provide the isotropic entanglement-of-formation input; their result predates the cubic-norm certificate and therefore does not compare the two bounds defining \(G_d\).

## Limitations
The result does not determine the exact entanglement cost of qudit isotropic states for \(d\ge3\), does not prove that the true entanglement-cost saving is of order \(d^{-2/3}\), and does not identify an exact finite-\(d\) maximizer of \(G_d\). It only establishes the sharp large-\(d\) asymptotic of the width of the certified interval formed by the two specified bounds.

## References
1. K. Fang, *Entanglement cost of quantum depolarization*, arXiv:2610.00187v1 (2026), especially Proposition 12, equations (67), (71)–(78), and Corollary 13, equations (97)–(103).
2. B. M. Terhal and K. G. H. Vollbrecht, *The Entanglement of Formation for Isotropic States*, arXiv:quant-ph/0005062v1; Phys. Rev. Lett. 85, 2625–2628 (2000).
