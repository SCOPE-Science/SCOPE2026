# Rate-disorder invariance of shot-noise plateau crossings in sequential transport

## Finding

Let \(n\ge2\) be any integer and let \(\rho_0,\ldots,\rho_{n-1}>0\) be arbitrary real transition rates, with no equality or separation assumptions. For the event train of marked returns \(n-1\to0\) on the stationary unidirectional Markov ring, the Poisson-normalized current spectrum \(F(\omega)\) crosses its plateau \(F=1\) at exactly

\[
N_{\mathrm{cross}}=\left\lfloor\frac n2\right\rfloor-1
\]

distinct finite strictly positive frequencies. Every crossing is transversal (simple) and the sign of \(F(\omega)-1\) alternates across successive crossings, starting negative near zero. The result holds even for arbitrarily heterogeneous positive rates; therefore a counted number \(r\) determines the number of stages, within this model, to be \(2r+2\) or \(2r+3\), without knowing the rates.

## Assumptions and scope

The continuous-time Markov chain has the state set \(\{0,1,\ldots,n-1\}\), and from state \(j\) it jumps only to the next cyclic state \(j+1\pmod n\), at exponential rate \(\rho_j>0\). It is irreducible and initially stationary. Only transitions \(n-1\to0\) are marked and counted; these events form a stationary renewal process because every such transition resets to state \(0\). The waiting time is a sum of independent exponentials with rates \(\rho_0,\ldots,\rho_{n-1}\).

For \(\omega>0\), define the Poisson-normalized continuous current spectrum by the standard stationary renewal expression

\[
F(\omega)=\frac{1-|\phi(\omega)|^2}{|1-\phi(\omega)|^2},\qquad
\phi(\omega)=\prod_{j=0}^{n-1}\frac{\rho_j}{\rho_j+i\omega}.
\]

This normalization means that the high-frequency plateau is \(1\). The stationary mean marked event rate is \(\bar J=(\sum_j1/\rho_j)^{-1}\). Define \(P(s)=\prod_j(s+\rho_j)\) and \(R=\prod_j\rho_j=P(0)>0\). Direct substitution gives

\[
F(\omega)=\frac{|P(i\omega)|^2-R^2}{|P(i\omega)-R|^2}\quad(\omega>0).
\]

The denominator is strictly positive for positive frequency. At zero frequency the continuous limit is \(F(0)=(\sum_j\rho_j^{-2})/(\sum_j\rho_j^{-1})^2<1\), since \(n\ge2\) and all summands are strictly positive. The \(n=1\) case is excluded: its events are exactly Poissonian and the spectrum is identically \(1\).

## Proof

**1. Plateau-crossing identity.** Algebraically,

\[
F(\omega)-1=\frac{2R(\operatorname{Re}P(i\omega)-R)}{|P(i\omega)-R|^2}.
\]

Thus plateau crossings are precisely zeros of \(\operatorname{Re}P(i\omega)-R\), and the signs coincide. Write

\[
P(s)-R=sH(s),\qquad H(s)=\frac{P(s)-R}{s}.
\]

Here \(H\) is a real monic polynomial of degree \(n-1\) with \(H(0)=P'(0)=R\sum_j1/\rho_j>0\). For real \(\omega>0\),

\[
\operatorname{Re}P(i\omega)-R=-\omega\operatorname{Im}H(i\omega).
\]

**2. Strict stability of the quotient polynomial.** For every complex \(s\) with \(\operatorname{Re}s\ge0\) and \(s\ne0\), every factor has \(|s+\rho_j|>\rho_j\). Therefore \(|P(s)|>R\), so \(P(s)-R\ne0\). Since the root of \(P(s)-R\) at \(s=0\) is simple by \(P'(0)>0\), all zeros of \(H\) lie strictly in the open left half-plane. In particular \(H(i\omega)\ne0\) at every real \(\omega\).

**3. Strict phase rotation.** List the \(n-1\) roots of \(H\), with multiplicity, as \(z_k\) where \(\operatorname{Re}z_k<0\). Because \(H\) is monic,

\[
H(i\omega)=\prod_{k=1}^{n-1}(i\omega-z_k).
\]

The real polynomial \(H\) has \(H(0)>0\). Define the unique continuous lifted phase \(\Theta(\omega)=\arg H(i\omega)\) for \(\omega\ge0\), normalized by \(\Theta(0)=0\). Each factor \(i\omega-z_k\) lies strictly in the right half-plane. Differentiating the continuously lifted argument factor-by-factor gives the strictly positive derivative

\[
\Theta'(\omega)=\sum_{k=1}^{n-1}
\frac{-\operatorname{Re}z_k}{(\omega-\operatorname{Im}z_k)^2+(\operatorname{Re}z_k)^2}>0.
\]

Every factor's continuous argument approaches \(\pi/2\) as \(\omega\to\infty\), and their arguments sum to zero at \(\omega=0\) (because real roots contribute zero and nonreal roots occur in conjugate pairs). Hence

\[
\lim_{\omega\to\infty}\Theta(\omega)=\frac{(n-1)\pi}2,
\qquad 0<\Theta(\omega)<\frac{(n-1)\pi}2\quad(\omega>0).
\]

**4. Count, simplicity, and alternation.** Since \(H(i\omega)\ne0\),

\[
F(\omega)-1=-\frac{2R\omega|H(i\omega)|}{|P(i\omega)-R|^2}
\sin\Theta(\omega).
\]

Its finite positive zeros are exactly the unique frequencies satisfying \(\Theta(\omega)=k\pi\), for positive integers \(k\) with \(k\pi<(n-1)\pi/2\). There are precisely \(\lfloor n/2\rfloor-1\) such integers. At each crossing \(\Theta'>0\) and the prefactor never vanishes, so the zero is simple and the sign flips. At small \(\omega>0\), \(\Theta>0\) is small and \(F-1<0\). This proves every assertion.

**5. Explicit small-stage specializations.** Write \(e_j\) for the degree-\(j\) elementary symmetric polynomial in all the rates. For \(n=4\), the unique crossing is \(\omega=\sqrt{e_2}\). For \(n=5\), it is \(\omega=\sqrt{e_3/e_1}\). For \(n=6\), the two squared crossing frequencies are the positive roots of \(x^2-e_2x+e_4=0\), namely \(x=(e_2\pm\sqrt{e_2^2-4e_4})/2\). The theorem guarantees both distinct and positive for all strictly positive rate choices.

## Verification

The accompanying executable \(\texttt{CHECK.py}\) computes the normalized spectrum in two mathematically separate ways: (i) from products of exponential waiting-time transforms and (ii) from the resolvent of the finite Markov generator \(Q\), using \(F(\omega)=1+2\operatorname{Re}[\rho_{n-1}(i\omega I-Q)^{-1}_{0,n-1}]\). It also forms the exact real-part crossing polynomial through elementary symmetric functions, numerically locates all its roots, checks strict sign changes and compares with the predicted count. On its specified deterministic inputs, the checker passed 2,221 assertions over \(n=2,\ldots,11\), including six unequal-rate profiles per size. These are reproducibility checks, **not** a finite substitute for the all-integer, all-positive-rate proof above.

Run from the extracted directory with \(\texttt{python CHECK.py}\) using Python 3 and NumPy. No network connection is required.

## Relationship to prior work

Tobias Brandes, *Waiting Times and Noise in Single Particle Transport*, arXiv:0802.2233v1 (15 February 2008), derives the general waiting-time/noise relation (Eq. (21)) and the arbitrary-positive-rate sequential ring waiting-time transform (Eq. (55), Section III.C). Consequently the renewal spectrum and the physical ring itself are prior art. The manuscript then develops special electron-dot and uniform-rate large-ring examples; it does **not** present this exact all-size, arbitrary-rate plateau-crossing count in the examined full text. The contribution assessed here is the rate-disorder invariant number of simple crossings, its strict sign alternation, and the Hurwitz-phase proof.

The mathematical mechanism is related to classical Hermite–Biehler root interlacing for Hurwitz-stable polynomials. This is acknowledged as a general existing method, not claimed as new. The significant application-specific point is that the quotient polynomial \(H(s)=(\prod_j(s+\rho_j)-\prod_j\rho_j)/s\) is strictly Hurwitz for all positive rates and therefore enforces the precise spectral count. A previous treatment of identical stage rates gives the homogeneous special case; that result does not itself establish invariance under arbitrarily unequal rates. Further equivalent analyses in phase-type renewal or current-noise literature may exist.

## Limitations

The theorem assumes finite positive exponential transition rates, a single unidirectional ring, stationary event sampling, and counting exactly one reset transition. Other marked transitions, bidirectional or branched networks, nonexponential sojourns, and nonrenewal currents need not obey the same count. The theorem gives **numbers and qualitative signs** of plateau crossings, not a closed expression for their locations at general stage number. Numerical checks are supporting evidence only. Literature priority is subject to independently assessing broader renewal and Hurwitz-polynomial work; no independent scientific audit has been performed.

## References

1. T. Brandes, *Waiting Times and Noise in Single Particle Transport*, arXiv:0802.2233v1, 15 February 2008, https://arxiv.org/abs/0802.2233. Especially Eq. (21) and Section III.C, Eq. (55).
2. M. T. Ho, A. Datta, and S. P. Bhattacharyya, *Generalizations of the Hermite–Biehler theorem: The complex case*, Linear Algebra Appl. **320** (2000), 23–36, https://doi.org/10.1016/S0024-3795(00)00191-9. This is mathematical background, not a claimed independent transport classification.
3. E. Barkai, R. S. Eisenberg, and Z. Schuss, *Bidirectional shot noise in a singly occupied channel*, Phys. Rev. E **54** (1996), 1161, https://doi.org/10.1103/PhysRevE.54.1161. Only its published abstract was accessible for the present comparison; this limited inspection does not rule out related observations in its full text.
