# Sharp rank-two Gaussian resolvent-sketch small-ball law with elliptic spectral constant

## Finding
Let \(S\in\mathbb R^{n\times n}\) be a fixed real matrix of **rank exactly two**, with singular values \(a\ge c>0\), and take independent \(n\times k\) standard real Gaussian probing matrices \(\Omega_L,\Omega_R\), for \(n,k\ge2\). Set \(Z=\Omega_L^{\mathsf T}S\Omega_R\). Then
\[
\boxed{\Pr(\|Z\|_F\le\varepsilon)\sim \frac{C_k J(a,c)}{(ac)^k}\varepsilon^{2k-1}\quad(\varepsilon\downarrow0),}
\]
where
\[
C_k=\frac{\pi\Gamma((k-1)/2)}{2^{k+1}\Gamma(k-1)\Gamma(k/2)\Gamma(k+1/2)},
\qquad
J(a,c)=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{\sqrt{\cos^2\theta/a^2+\sin^2\theta/c^2}}.
\]
The constant is strictly positive and finite. Equivalently, defining the complete elliptic integral \(K(u)=\int_0^{\pi/2}(1-u\sin^2\theta)^{-1/2}\,d\theta\), one has
\[J(a,c)=\frac{2c}{\pi}K\!\left(1-\frac{c^2}{a^2}\right).\]
In the equal-singular-value case \(a=c=d\), the prefactor is \(C_k/d^{2k-1}\), and the first examples are \(C_2=\pi/6\), \(C_3=1/15\), \(C_4=\pi/840\). In particular the rank-two probability decays with exponent exactly \(2k-1\), without a logarithm. This establishes analytically the rank-two real-Gaussian exponent suggested by numerical experiments in [1].

## Assumptions and scope
All Gaussian entries are independent, centered, and have variance one. Both probing matrices are sampled independently. The singular values \(a,c\) and the integer block width \(k\ge2\) remain fixed as the threshold \(\varepsilon>0\) decreases; no simultaneous rank, dimension, block-width, or condition-number limit is asserted. The norm is the Frobenius norm, and computations and probabilities concern exact real arithmetic. The orientation of the two singular-vector pairs is arbitrary; orthogonal invariance removes their influence.

## Proof
**1. Gaussian reduction and singular-value measure.** An SVD of \(S\) and orthogonal invariance show that \(Z\) has the distribution of \(G^{\mathsf T}DH\), where \(D=\operatorname{diag}(a,c)\) and \(G,H\) are independent \(2\times k\) matrices with iid standard real Gaussian entries. Write \(X=DG\). If its ordered positive singular values are \(s_1>s_2>0\) and its orthogonal left-singular frame is \(U=(u_1,u_2)\), the change of variables from \(X\) to the real \(2\times k\) SVD gives the joint measure
\[
\frac{(ac)^{-k}}{\Gamma(k-1)}(s_1s_2)^{k-2}(s_1^2-s_2^2)
\exp\!\left[-\tfrac12\{s_1^2q(u_1)+s_2^2q(u_2)\}\right]ds_1\,ds_2\,d\mu(U),
\]
where \(q(u)=u_1^2/a^2+u_2^2/c^2\) and \(\mu\) is Haar probability on orthogonal frames. The SVD normalization is fixed by the isotropic case \(a=c=1\): in polar variables \(s_1=r\cos\phi\), \(s_2=r\sin\phi\), \(0<\phi<\pi/4\), the radial integral is \(2^{k-1}\Gamma(k)\), the angular integral is \(1/[2^{k-1}(k-1)]\), and their product is \(\Gamma(k-1)\). This also confirms that no frame-volume factor is missing.

**2. Conditional Gaussian norm and threshold rescaling.** Conditionally on \(X\), right-side orthogonal invariance yields
\[\|X^{\mathsf T}H\|_F^2\ \stackrel d=\ s_1^2V_1+s_2^2V_2,\]
where \(V_1,V_2\) are independent \(\chi^2_k\) random variables. Set \(s_2=\varepsilon t\), and let \(F_k\) be the \(\chi^2_k\) CDF. Then, for positive fixed \(s_1,t,V_2\),
\[\varepsilon^{-k}F_k\!\left(\frac{\varepsilon^2(1-t^2V_2)_+}{s_1^2}\right)\longrightarrow\frac{(1-t^2V_2)_+^{k/2}}{2^{k/2}\Gamma(k/2+1)s_1^k}.\]
The bound \(F_k(x)\le x^{k/2}/[2^{k/2}\Gamma(k/2+1)]\) for nonnegative \(x\) supplies domination. The remaining scaled SVD factor is \(\varepsilon^{k-1}(s_1t)^{k-2}(s_1^2-\varepsilon^2t^2)\), so the total small-threshold power is \(\varepsilon^{2k-1}\).

**3. Dominated convergence.** Since \(q(u)\ge a^{-2}\) and \(0<s_2<s_1\), after applying the CDF bound and dividing by \(\varepsilon^{2k-1}\), the nonnegative integrand is bounded by a constant times
\[e^{-s_1^2/(2a^2)}t^{k-2}(1-t^2V_2)_+^{k/2}.\]
It is integrable over \(s_1>0\), \(t>0\), the frame distribution, and \(V_2\), because
\[\mathbb E(V_2^{-(k-1)/2})=2^{-(k-1)/2}\sqrt\pi/\Gamma(k/2)<\infty\quad(k\ge2).\]
The contribution of the ordering restriction \(t<s_1/\varepsilon\) is handled by its indicator, which tends to one at all fixed positive \(s_1,t\). Therefore the dominated-convergence limit equals
\[
\frac{(ac)^{-k}}{\Gamma(k-1)2^{k/2}\Gamma(k/2+1)}
\int e^{-s_1^2q(u_1)/2}ds_1\,d\mu(U)
\int_0^\infty t^{k-2}\mathbb E(1-t^2V_2)_+^{k/2}dt.
\]

**4. Exact evaluation.** Integrating \(s_1\) gives \(\sqrt{\pi/(2q(u_1))}\); the Haar average of \(q(u_1)^{-1/2}\) is precisely \(J(a,c)\). For fixed \(V_2>0\), the substitution \(y=t^2V_2\) gives
\[\int_0^\infty t^{k-2}(1-t^2V_2)_+^{k/2}dt=\tfrac12 V_2^{-(k-1)/2}\mathrm B((k-1)/2,k/2+1).\]
Substituting the negative chi-square moment and the beta/gamma identities yields exactly
\[\frac{(ac)^{-k}\pi\Gamma((k-1)/2)J(a,c)}{2^{k+1}\Gamma(k-1)\Gamma(k/2)\Gamma(k+1/2)},\]
proving the claim. The elliptic representation follows by factoring out \(c^{-2}\) from \(q\) and shifting the angular variable.

## Verification
The included standalone `verify.py` evaluates the gamma coefficients, independently quadratures the Haar angular integral and compares it with the complete elliptic integral, checks homogeneity and the ordered-SVD density normalization, and performs a reproducible finite-threshold direct Gaussian simulation. These are finite numerical checks of supporting identities, not replacements for the proof of the universal asymptotic. Run `python verify.py` with Python 3, NumPy, and SciPy. The simulation operates at a fixed positive threshold and is **not** extrapolated into a proof of the limit.

## Relationship to prior work
Shao and Nakatsukasa [1] study two-sided Gaussian block probing of resolvents in rational-approximation nonlinear eigensolvers. Their Theorem 2.7 supplies an upper small-ball bound; the discussion and experiments describe a sharper rank-two exponent of \(2k-1\), which they do not prove as an exact asymptotic. The present result identifies that exponent for every fixed real rank-two residue and computes its full leading constant, including dependence on the two nonzero singular values. Existing general Gaussian-product singular-value inequalities and small-ball bounds address broader but different quantities and do not by themselves identify the exact constant for this Frobenius-norm event. Exact earlier coverage by specialized product-Wishart or Gaussian bilinear-form work cannot be excluded without an exhaustive historical review.

## Limitations
Only rank exactly two, independent **real** Gaussian probes, fixed width \(k\ge2\), fixed positive singular values, and vanishing threshold are proved. The theorem does not cover complex Gaussian probes, arbitrary higher rank, a rank-dependent or dimension-dependent asymptotic, structured sketches, floating-point effects, global eigenvalue-error probability, or complete rational-approximation convergence. The probability law is nonasymptotic only as an integral over Gaussian variables; no explicit finite-threshold error bound is claimed. Independent mathematical audit and exhaustive priority confirmation have not occurred.

## References
[1] Nian Shao and Yuji Nakatsukasa, *Convergence analysis of a nonlinear eigensolver based on rational approximation of the resolvent*, arXiv:2607.10377, first posted 2026-07-11. See Gaussian block-probing construction, Theorem 2.7, and rank-two numerical discussion.
[2] Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications (2024), DOI:10.1137/23M1565413, background on randomized eigensolvers, without a claim that it proves the displayed rank-two law.
