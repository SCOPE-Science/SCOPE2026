# Sharp strong-repulsion upper constant for the regularized three-boson s-wave multiplier
## Finding
For the scale-invariant homogeneous s-wave charge form of the regularized three-boson zero-range model, define
\[
S_\gamma(k)=\frac{\sqrt{3}}{2}+\gamma\frac{\sinh(\pi k/2)}{k\cosh(\pi k/2)}-4\frac{\sinh(\pi k/6)}{k\cosh(\pi k/2)},
\]
with the continuous value at \(k=0\), and set \(\gamma_c=4/3-\sqrt{3}/\pi\). The exact strong-repulsion threshold for the global maximum is
\[
\gamma_0=\frac{52}{27}.
\]
For every \(\gamma\ge\gamma_0\),
\[
\sup_{k\in\mathbb R}S_\gamma(k)=S_\gamma(0)=\frac{\pi}{2}(\gamma-\gamma_c),
\]
and \(S_\gamma(k)<S_\gamma(0)\) for every finite \(k\ne0\). For every \(\gamma<\gamma_0\), zero is not even a local maximizer. Hence, for \(\gamma\ge52/27\), the best constant in
\[
\phi_0^0(g)\le C\lVert g^\sharp\rVert_2^2
\]
is exactly \(C=\frac{\pi}{2}(\gamma-\gamma_c)\).

## Assumptions and scope
The object is the homogeneous \(\lambda=0\), s-wave component \(\phi_0^0\) obtained from the diagonal, off-diagonal and singular regularizing pieces in the model of Basti, Cacciapuoti, Finco and Teta. Their Mellin transform satisfies \(\lVert g^\sharp\rVert_2=\lVert\xi\rVert_{\dot H^{1/2}}\), and their equations (3.15)--(3.17) identify \(\phi_0^0\) with multiplication by \(S_\gamma\). The statement does not concern the bounded regularization remainder, the full \(\Phi^\lambda\), or the complete Hamiltonian norm.

## Proof
Write \(t=\pi |k|/6\). For \(t>0\), evenness of the symbol gives
\[
S_\gamma(k)-\frac{\sqrt{3}}{2}
=\frac{\pi}{6t\cosh(3t)}\bigl(\gamma\sinh(3t)-4\sinh t\bigr).
\]
At \(\gamma_0=52/27\), the desired inequality \(S_{\gamma_0}(k)\le S_{\gamma_0}(0)\) is equivalent, after multiplication by positive factors, to
\[
52\sinh(3t)-108\sinh t\le48t\cosh(3t).
\]
Using \(\sinh(3t)=3\sinh t+4\sinh^3t\), this becomes
\[
F(t):=3t\cosh(3t)-3\sinh t-13\sinh^3t\ge0.
\]
A second use of the triple-angle identity rewrites
\[
F(t)=3t\cosh(3t)-\frac{13}{4}\sinh(3t)+\frac{27}{4}\sinh t.
\]
Its power series is
\[
F(t)=\sum_{n=0}^\infty
\frac{3^{2n+1}(8n-9)+27}{4(2n+1)!}t^{2n+1}.
\]
The coefficients for \(n=0\) and \(n=1\) vanish, whereas every coefficient with \(n\ge2\) is strictly positive. Thus \(F(t)>0\) for every \(t>0\). Therefore \(S_{52/27}(k)<S_{52/27}(0)\) whenever \(k\ne0\).

For larger coupling, set
\[
A(k)=\frac{\sinh(\pi k/2)}{k\cosh(\pi k/2)}.
\]
For \(k\ne0\), \(A(k)<\pi/2=A(0)\) because \(\tanh x<x\) for \(x>0\). Since \(S_\gamma\) is affine in \(\gamma\),
\[
S_\gamma(k)-S_\gamma(0)
=\bigl(S_{52/27}(k)-S_{52/27}(0)\bigr)
+\left(\gamma-\frac{52}{27}\right)\left(A(k)-\frac{\pi}{2}\right)<0
\]
for every \(\gamma\ge52/27\) and finite \(k\ne0\). The continuous endpoint value is
\[
S_\gamma(0)=\frac{\sqrt{3}}{2}+\frac{\pi\gamma}{2}-\frac{2\pi}{3}
=\frac{\pi}{2}(\gamma-\gamma_c).
\]

Sharpness of the threshold follows from the expansion
\[
S_\gamma(k)=S_\gamma(0)+\frac{\pi^3(52-27\gamma)}{648}k^2+O(k^4).
\]
If \(\gamma<52/27\), the quadratic coefficient is positive, so arbitrarily small nonzero \(k\) have larger symbol value than \(k=0\). Finally, because \(\phi_0^0\) is the multiplication form by the continuous symbol \(S_\gamma\), its optimal upper constant is the essential supremum of that symbol. Normalized Mellin profiles supported in shrinking neighborhoods of zero approach the sharp constant, while exact equality would require a nonzero \(L^2\) profile supported on the measure-zero set \(\{0\}\).

## Verification
The algebraic reduction was checked independently from the published multiplier. The accompanying checker evaluates the exact threshold identity, the Taylor coefficient, the positive-series coefficients of \(F\), and dense numerical stress tests of the global inequality for representative couplings on both sides of \(52/27\). Those finite tests are corroborative only; the proof above is analytic and global.

## Relationship to prior work
Basti, Cacciapuoti, Finco and Teta diagonalize the homogeneous partial-wave form and give the exact multiplier \(S_\ell\); their Lemma 3.5 uses it to prove the lower-bound mechanism needed for stability when \(\gamma>\gamma_c\), while Proposition 3.1 gives a non-sharp continuity estimate for the full charge form. Ferretti and Teta later write the same s-wave multiplier explicitly and use its value at zero to prove instability for \(\gamma<\gamma_c\); their position-space estimate deliberately sacrifices accuracy and does not identify the multiplier supremum. The inspected sources do not state the strong-repulsion global-maximum threshold \(52/27\), the exact upper constant above that threshold, or the associated maximizing-frequency transition.

## Limitations
The theorem is restricted to the homogeneous s-wave multiplier. It does not give the sharp upper constant for \(\gamma<52/27\), where the global maximum moves away from zero, and it does not claim a sharp norm-equivalence constant for the full inhomogeneous form or Hamiltonian. The literature search cannot exclude an unindexed equivalent calculation using different Mellin conventions.

## References
1. G. Basti, C. Cacciapuoti, D. Finco, A. Teta, *Three-Body Hamiltonian with Regularized Zero-Range Interactions in Dimension Three*, arXiv:2107.07188; Annales Henri Poincare 24 (2023), 223--276, doi:10.1007/s00023-022-01214-9.
2. D. Ferretti, A. Teta, *Some Remarks on the Regularized Hamiltonian for Three Bosons with Contact Interactions*, arXiv:2207.00313; in *Quantum Mathematics I* (2023), doi:10.1007/978-981-99-5894-8_8.
