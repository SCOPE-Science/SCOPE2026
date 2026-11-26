# Exact finite-angle Ritz-vector law and logarithmic mean-angle penalty for a square Gaussian sketch

## Finding

Let \(A=\operatorname{diag}(0,a,b)\) with \(a,b>0\). For \(0<\theta<\pi/2\), write \(s=\sin\theta\), \(c=\cos\theta\), and let \(W=[(c,0,s)^{\mathsf T},e_2]\). Draw a \(3\times2\) matrix \(\Omega\) of independent standard circular complex Gaussian entries and form the pencil \(\Omega^*AWy=\mu\Omega^*Wy\). Use the eigenvalue branch starting from \(0\) as \(\theta\downarrow0\), not a closest-eigenvalue selection from the computed spectrum. Let \(\widehat v=Wy/\|Wy\|_2\) for this branch.

Set \(\beta=bs^2\), \(\gamma=bsc\) and \(q=\gamma^2/((a-\beta)^2+\gamma^2)\in(0,1]\). If \(S=1-|e_1^*\widehat v|^2\), the exact finite-angle law and mean are
\[
 S\stackrel d=s^2+c^2\frac{qV}{U+qV},\qquad U,V\text{ independent unit exponentials},
\]
\[
 \Pr\{(S-s^2)/c^2\le z\}=\frac{z}{q+(1-q)z}\quad(0\le z\le1),\qquad
 \mathbb ES=s^2+c^2\Phi(q),
\]
\[
 \Phi(q)=\frac{q(q-1-\log q)}{(1-q)^2}\quad(0<q<1),\qquad \Phi(1)=\frac12.
\]
In particular, the normalized angle excess is uniform at the resonance \(a=bs^2\). For fixed \(a,b>0\),
\[
 \mathbb ES=2(b/a)^2\theta^2\log(1/\theta)+O(\theta^2).
\]
On the same trial space the ordinary Hermitian Ritz branch near zero has eigenvector \((c,0,s)^{\mathsf T}\) with squared sine \(s^2\sim\theta^2\). The exact law explains why the randomized vector may have a small angle with high probability while its expected squared sine exceeds the deterministic baseline by a logarithmic factor.

## Assumptions and scope

The target is the simple lowest eigenvalue of the stated diagonal matrix. The projected pencil is square with respect to the trial dimension. The sketch, trial plane and normalized eigenvector are as above; no oversampling, symmetrization, truncation or residual-based rejection is used. All statements concern exact arithmetic. At a deterministic compressed eigenvalue tie \(\beta=a\), the ordinary compressed eigenvector is not unique; the small-angle comparison concerns only the branch where \(\beta\ne a\) near zero. The random pencil has simple roots almost surely at each stated angle, including that resonance.

## Proof

The kernel of \(\Omega^*\) is almost surely a unitarily invariant complex line, represented by a vector \(K=(K_1,K_2,K_3)^{\mathsf T}\) of independent standard circular complex Gaussian coordinates. At the non-spectator root write the unnormalized Ritz vector as \((c,\eta,s)^{\mathsf T}\). The projected eigen-equation is exactly that
\[
 (-\mu c,(a-\mu)\eta,(b-\mu)s)^{\mathsf T}\in\operatorname{span}K.
\]
Eliminating the proportionality factor gives
\[
 \mu=\frac{bsK_1}{sK_1-cK_3},\qquad
 \eta=-\frac{bscK_2}{(a-b)sK_1-acK_3}.
\]
For fixed \(\theta\), both denominators are nonzero almost surely. The first also certifies nonsingularity of \(\Omega^*W\): its singularity would mean the null line lies in the trial plane, i.e. \(sK_1-cK_3=0\). The other compressed eigenvalue is exactly \(a\), since \(e_2\) is a true eigenvector; equality of the two roots would make the second denominator zero. For a single fixed sketch, \(K_3\ne0\) almost surely, so the displayed non-spectator root tends to zero as \(\theta\downarrow0\).

The linear form \((a-b)sK_1-acK_3\) is independent of \(K_2\), and has variance \((a-b)^2s^2+a^2c^2=(a-\beta)^2+\gamma^2\). Thus \(|\eta|^2\stackrel d=qV/U\). Normalization of \((c,\eta,s)^{\mathsf T}\) gives the asserted law for \(S\). The ratio of unit exponentials has CDF \(x/(1+x)\) for \(x\ge0\), giving the CDF on \([0,1]\). Integrating its complement, \(q(1-z)/[q+(1-q)z]\), over that interval gives \(\Phi(q)\); for \(q=1\) the integral is \(1/2\). Since \(q=(b/a)^2\theta^2+O(\theta^4)\) and \(\Phi(q)=-q\log q+O(q)\), the stated mean-angle penalty follows. Finally, \(W^*AW=\operatorname{diag}(\beta,a)\) supplies the deterministic comparison.

## Verification

The included `verify.py` (Python 3, NumPy and mpmath) checks the analytic expectation integral and resonance, and compares direct compressed Gaussian pencils with the CDF and mean at several angles. Its finite statistics are consistency checks; the exact vector law and logarithmic asymptotic follow from the proof. The program also checks the known eigenvalue tail as a diagnostic of the branch and sketch.

## Relationship to prior work

Shao [1] establishes high-probability convergence for the square Gaussian pencil. The general spectator-subspace law in [2] already gives \(\Pr(|\mu-\beta|>t)=\gamma^2/(t^2+\gamma^2)\) and \(\mathbb E|\mu|^2=\infty\) here, by taking spectator \(e_2\) and residual norm \(\gamma\). The oversampling law in [3] gives another direct specialization to the same eigenvalue tail. These eigenvalue facts are background, not part of the new claim. A more general first-order joint error law [4] describes limiting, normalized errors as the trial plane approaches a true eigenvector. Such a weak limit alone does not recover the finite-angle normalized eigenvector law or the expected squared sine: its heavy tail requires controlling the finite-angle saturation. The distinction here is the exact finite-angle eigenvector statistic and its mean asymptotic in the stated geometry, not priority for the Gaussian quotient identity or for the pencil itself.

## Limitations

No claim is made for other trial spaces, higher dimensions, alternative branch selectors, refined Rayleigh quotients, real sketches or oversampling. An equivalent special-case angle law in unexamined literature remains possible.

## References

1. N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, [arXiv:2604.01037v1](https://arxiv.org/html/2604.01037v1), Algorithm 1 and Theorem 2.
2. *Three independent Gaussian Ritz sketches recover the exact residual mean-square scale*, [Resultary record 6cfe0d1021ce](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-three-independent-gaussian-ritz-sketches-recover-the-exact-resid--6cfe0d1021ce), Proof steps 1–2.
3. *Sharp real–complex Gaussian oversampling thresholds for sketched Ritz moments*, [Resultary record ec7a4a7d4b05](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-sharp-real-complex-gaussian-oversampling-thresholds-for-sketched--ec7a4a7d4b05).
4. *Sharp joint complex-Cauchy error law for two-dimensional randomized Rayleigh–Ritz*, [Resultary record 629c63caaa73](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-joint-complex-cauchy-error-law-for-two-dimensional-randomi--629c63caaa73).
