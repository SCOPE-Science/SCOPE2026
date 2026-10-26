# Sharp kernel-testing constant for quadratic Hardy Hankel symbols

## Finding
For nonzero \(\psi(z)=az+bz^2\), with \(a,b\in\mathbb C\), define the Hardy-space Hankel operator \(H_{\bar\psi}:H^2(\mathbb D)\to H^2_-\) and the normalized Szegő kernels \(k_w(\zeta)=\sqrt{1-|w|^2}/(1-\bar w\zeta)\). The exact optimal uniform strong-kernel-testing estimate on this entire two-coefficient family is
\[
\boxed{\ \sup_{|w|<1}\|H_{\bar\psi}k_w\|\ \ge\ \frac{5}{3\sqrt3}\,\|H_{\bar\psi}\|\ }.\tag{1}
\]
The constant \(5/(3\sqrt3)\) cannot be increased. Equality in (1) holds precisely when \(b\ne0\) and \(|a|/|b|=1/\sqrt6\). For such an extremizer, a maximizing kernel has radius \(|w|=1/\sqrt6\), with its phase chosen so that \(a\) and \(bw\) have the same argument. Equivalently, on quadratic analytic symbols the Garsia seminorm is at least \(5/(3\sqrt3)\) times the Nehari/Hankel norm, and the coefficient-modulus equality class is complete.

## Assumptions and scope
Throughout, \(H^2\) is the complex Hardy space on \(\mathbb D\), \(H^2_-=L^2(\mathbb T)\ominus H^2\), and \(H_{\bar\psi}f=P_-(\bar\psi f)\). The infimum over all nonzero pairs \((a,b)\in\mathbb C^2\setminus\{(0,0)\}\) of the quotient \(\sup_w\|H_{\bar\psi}k_w\|/\|H_{\bar\psi}\|\) is exactly \(5/(3\sqrt3)\). This concerns the ordinary operator norm, **not** the Hilbert–Schmidt norm or an unrestricted-symbol inequality. The zero symbol is excluded because the quotient is undefined. Both pure monomials have quotient one. No claim is made about cubic or general rational symbols.

## Proof
**1. Two-dimensional Hankel reduction.** Relative to the domain basis \(1,z,z^2,\ldots\) and codomain basis \(z^{-1},z^{-2},\ldots\), the only nonzero corner of \(H_{\bar\psi}\) is
\[
\begin{pmatrix}\bar a&\bar b\\\bar b&0\end{pmatrix}.
\]
If \(b\ne0\), put \(t=|a|/|b|\) and \(\Lambda=(t+\sqrt{t^2+4})/2\). Since the two singular values are the absolute values of the eigenvalues of \(\begin{psmallmatrix}t&1\\1&0\end{psmallmatrix}\), the exact operator norm is \(\|H_{\bar\psi}\|=|b|\Lambda\). Indeed the Gram matrix has trace \(|a|^2+2|b|^2\) and determinant \(|b|^4\); its largest eigenvalue is \(|b|^2\Lambda^2\), independently of the coefficient phases. For \(b=0\), the Hankel operator has rank one and its norm is attained by \(k_0=1\), giving quotient one.

**2. Exact kernel profile.** For \(w\in\mathbb D\),
\[
\|H_{\bar\psi}k_w\|^2=(1-|w|^2)\bigl(|a+bw|^2+|b|^2\bigr).
\]
At each fixed radius \(r=|w|\), select the phase of \(w\) to align \(a\) and \(bw\). Thus, with \(F_t(r)=(1-r^2)((t+r)^2+1)\),
\[
\sup_{|w|<1}\|H_{\bar\psi}k_w\|^2=|b|^2\max_{0\le r\le1}F_t(r).
\]
When \(t>0\), the derivative is
\[
F_t'(r)=2(t-t^2r-3tr^2-2r^3),\qquad F_t''(r)=-2(t^2+6tr+6r^2)<0
\]
for \(r\ge0\). Hence the unique maximizing radius is the unique root in \((0,1)\) of \(2r^3+3tr^2+t^2r-t=0\). If \(t=0\), then \(F_0(r)=1-r^4\) has maximum one at \(r=0\).

**3. A universal sharp certificate.** Let \(q=\Lambda^{-1}\) and \(\tau=q^2\), so \(0<\tau\le1\), \(t=\Lambda-\Lambda^{-1}=(1-\tau)/\sqrt\tau\). At the explicit admissible test radius \(r=q/2=\sqrt\tau/2\),
\[
\frac{F_t(q/2)}{\Lambda^2}
=\left(1-\frac\tau4\right)\left(1+\frac{\tau^2}4\right)
=\frac{25}{27}+\frac{(8-3\tau)(3\tau-2)^2}{432}\ge\frac{25}{27}.
\]
Because \(8-3\tau>0\) on \((0,1]\), equality in the certificate is possible only at \(\tau=2/3\). Taking positive square roots proves (1), including the pure-monomial cases.

**4. Sharpness and all equality cases.** If \(\tau=2/3\), then \(\Lambda=\sqrt{3/2}\) and \(t=1/\sqrt6\); the test radius \(r=q/2\) equals \(t\). Here
\[
F_t'(t)=2t(1-6t^2)=0.
\]
The strict concavity in Step 2 shows that this radius is the actual global maximizer, not merely a witness. Consequently the squared kernel-to-operator norm quotient is exactly \(25/27\). Conversely, if the quotient equals \(5/(3\sqrt3)\), the lower certificate forces \(\tau=2/3\) and hence \(t=1/\sqrt6\). Complex phases do not affect the two norms; maximizing kernels align \(a\) with \(bw\). This proves the complete equality classification.

For the concrete symbol \(\psi(z)=z/\sqrt6+z^2\), the norm is \(\sqrt{3/2}\), while the largest kernel norm is \(5/(3\sqrt2)\), establishing the displayed ratio exactly.

## Verification
Run `python3 verify.py` (Python standard library only). The checker evaluates the exact rational certificate identity at 250 rational values, tests operator norms and complex-phase kernel formulas over 1,600 randomized coefficient configurations, checks the cubic critical equation, and confirms the extremal parameters. The recorded execution completed with **9,853** supplementary finite checks. The identities and inequalities in Steps 1–4 provide the proof for *all* complex coefficients; numerical testing is not used as a substitute for the universal argument.

## Relationship to prior work
Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm* (arXiv:2609.33242v1, September 27, 2026), §1 and Problem 1 in §2, sets up the exact distinction between the Garsia norm \(\|\psi\|_G\) and the Hankel/Nehari norm \(\|\psi\|_*\). It explicitly notes that suitable symbols of the form \(az+z^2\) give a strict inequality, but does **not** provide the optimum uniform testing ratio on this entire family or its complete equality parameters. That paper's identity between Garsia seminorm and normalized-kernel testing is used here with attribution.

Brevig–Seip, *Maximal norm Hankel operators* (arXiv:2301.07937), studies minimal and maximal norms relative to symbol norms, which are different extremal comparisons. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm* (arXiv:2404.05565), studies G-extremal functions and geometric extreme points; the sharp ratio between the Garsia and Hankel norms for quadratic symbols is distinct. Prior qualitative classifications of polynomial-symbol and finite-rank Hankel operators obeying the strong reproducing kernel thesis identify cases of **equality to one**, rather than the smallest **positive norm ratio** and its mixed-symbol optimizer. Those qualitative results alone do not imply the numerical constant or extremizer in (1).

## Limitations
The sharp constant is specific to analytic symbols with only the first two nonconstant Taylor coefficients. It is not asserted to hold for higher-degree polynomials or general BMOA symbols. An explicit proof and supplementary computations are provided; independent mathematical validation and exhaustive historical priority certification have not been performed. A concealed equivalent numerical estimate in older work, or in uninspected portions of related papers, remains a residual literature-priority risk.

## References
1. K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242v1 (first submitted 2026-09-27), especially §1, Eq. (4), and §2, Problem 1. https://arxiv.org/html/2609.33242v1
2. O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, arXiv:2301.07937 (2023); *Journal of Mathematical Analysis and Applications* 529 (2024), 127221. https://arxiv.org/abs/2301.07937
3. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565 (2024); *Journal of Functional Analysis* 288 (2025), 110833. https://arxiv.org/abs/2404.05565
4. F. F. Bonsall, *Boundedness of Hankel matrices*, *Journal of the London Mathematical Society* 29 (1984), 289–300. https://doi.org/10.1112/jlms/s2-29.2.289
