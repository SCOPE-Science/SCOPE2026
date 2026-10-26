# Exact positive-to-oscillatory relaxation transition in a three-state Gibbs shift

## Finding

For positive energy penalties \(a,b,r\) and every inverse temperature \(\beta>0\), consider the mixing nearest-neighbor symbolic system with states \(0,1,2\), permitted transitions \(00,01,11,12,20,21\), and energy \(a\) on \(01\), \(b\) on \(20\), \(r\) on \(11\), and zero on \(00,12,21\). Its equilibrium Markov chain has a unique sharp *relaxation-mode transition*, independent of temperature:

\[
\boxed{\begin{array}{ll}
 r<(a+b)/2 &: \text{the slowest nonstationary eigenvalue is positive},\\
 r>(a+b)/2 &: \text{the slowest nonstationary eigenvalue is negative},\\
 r=(a+b)/2 &: \text{the two nonstationary eigenvalues have equal modulus}.
\end{array}}
\]

The sign classification is exact for every \(\beta>0\), not merely asymptotic. At the transition, if \(s=\exp[-\beta(a+b)/2]\), the transfer eigenvalues are exactly
\[
1+s,\quad \sqrt{1-s},\quad-\sqrt{1-s},
\]
its equilibrium one-state marginal is \((1,1+s,1)/(3+s)\), and the sub-Perron spectral radius of the equilibrium Markov chain is \(\sqrt{1-s}/(1+s)\).

The transition coincides with competition between the maximizing fixed point and maximizing period-two orbit. In the critical low-temperature window \(r_\beta=(a+b)/2+\xi/\beta\), where \(\xi\in\mathbb R\) is fixed, the equilibrium measures converge to \(L(\xi)\delta_{0^\infty}+[1-L(\xi)]\nu_{12}\), with \(\nu_{12}\) the uniform orbit measure on the alternating two-cycle and
\[
 L(\xi)=\frac12\left(1-\frac{e^{-\xi}}{\sqrt{e^{-2\xi}+8}}\right).
\]
Writing \(\rho_\beta\) for the largest modulus of the two nonstationary eigenvalues of the normalized equilibrium transition matrix,
\[
\lim_{\beta\to\infty}e^{\beta(a+b)/2}(1-\rho_\beta)
=\begin{cases}
\sqrt{e^{-2\xi}+8}/2,&\xi\le0,\\
\bigl(3e^{-\xi}+\sqrt{e^{-2\xi}+8}\bigr)/4,&\xi\ge0.
\end{cases}
\]
Thus the spectral relaxation profile has a sharp change of formula at the same point as the exact all-temperature mode switch, even though the equilibrium phase-weight profile is continuous.

## Assumptions and scope

The one- or two-sided vertex shift on \(\{0,1,2\}\) has adjacency matrix
\[
 A=\begin{pmatrix}1&1&0\\0&1&1\\1&1&0\end{pmatrix}.
\]
Its graph is strongly connected and has loops, hence \(A\) is primitive. The nearest-neighbor potential is minus the specified edge energy. Define \(u=e^{-\beta a}\), \(v=e^{-\beta b}\), \(w=e^{-\beta r}\), and \(s=\sqrt{uv}=e^{-\beta(a+b)/2}\). All four quantities lie strictly between zero and one. The weighted transfer matrix is
\[
 W=\begin{pmatrix}1&u&0\\0&w&1\\v&1&0\end{pmatrix}.
\]
Let \(\lambda_+\) be its Perron eigenvalue and \(h\) a positive right Perron eigenvector. The associated equilibrium transition matrix is \(P_{ij}=W_{ij}h_j/(\lambda_+ h_i)\). Here the *slowest nonstationary eigenvalue* means the eigenvalue of \(P\), other than \(1\), of maximal absolute value. At equality there are two such eigenvalues with opposite signs.

The window result considers \(a,b\) fixed and \(r_\beta\) dependent on \(\beta\); the potential therefore changes with temperature. This is distinct from a fixed-potential zero-temperature limit. For negative \(\xi\), take sufficiently large \(\beta\) to ensure \(r_\beta>0\).

## Proof

**Exact reduction and three real roots.** A determinant expansion gives
\[
 p(x)=\det(xI-W)=(x-1)(x^2-wx-1)-s^2.
\]
It depends on the two bridge penalties only through their sum. Furthermore, \(p(-1)=-2w-s^2<0\), \(p(0)=1-s^2>0\), \(p(1)=-s^2<0\), and \(p(x)\to\infty\) as \(x\to\infty\). Therefore the three simple real roots are uniquely located at \(\lambda_{\rm n}\in(-1,0)\), \(\lambda_{\rm m}\in(0,1)\), and \(\lambda_+\in(1,\infty)\), respectively. Primitivity makes \(\lambda_+\) the Perron root. The stochastic matrix \(P\) is similar to \(W/\lambda_+\), so its nonstationary eigenvalues are \(\lambda_{\rm m}/\lambda_+\) and \(\lambda_{\rm n}/\lambda_+\).

**Sharp mode switch.** By Vieta,
\[
 \lambda_{\rm m}+\lambda_{\rm n}=1+w-\lambda_+.
\]
The characteristic polynomial has precisely one root larger than \(1\); consequently \(p(1+w)>0\), \(=0\), or \(<0\) according as \(1+w>\lambda_+\), \(=\lambda_+\), or \(<\lambda_+\). The exact identity
\[
 p(1+w)=w^2-s^2
\]
shows that \(\lambda_{\rm m}>|\lambda_{\rm n}|\), equality, or \(\lambda_{\rm m}<|\lambda_{\rm n}|\) exactly when \(w>s\), \(w=s\), or \(w<s\). Because exponentiation reverses inequalities between positive penalties, the respective conditions are \(r<(a+b)/2\), equality, or \(r>(a+b)/2\). At equality, direct polynomial division yields
\[
 p(x)=(x-1-s)(x^2-1+s),
\]
proving all asserted closed-form eigenvalues and the exact sub-Perron spectral radius.

**Stationary law and bridge-gauge universality.** Put \(d=\lambda_+-1>0\). From the left/right Perron equations one obtains the stationary marginal
\[
(\pi_0,\pi_1,\pi_2)=\frac{\bigl(s^2,\lambda_+d^2,(\lambda_+-w)d^2\bigr)}{s^2+d^2(2\lambda_+-w)}.
\]
For example, choose right Perron coordinates proportional to \((1,d/u,(\lambda_+-w)d/u)\) and left Perron coordinates proportional to \((1,\lambda_+d/v,d/v)\); their componentwise products give the formula. The transition matrix is explicitly
\[
P=\begin{pmatrix}
1/\lambda_+&d/\lambda_+&0\\
0&w/\lambda_+&(\lambda_+-w)/\lambda_+\\
s^2/[\lambda_+d(\lambda_+-w)]&1/[\lambda_+(\lambda_+-w)]&0
\end{pmatrix}.
\]
These expressions are independent of the asymmetry between \(a\) and \(b\). Indeed a positive diagonal gauge \(D=\operatorname{diag}(1,s/u,s/u)\) conjugates \(W\) to the corresponding matrix with both bridging weights equal to \(s\), without changing \(P\). At \(w=s\), substitution of \(\lambda_+=1+s\) gives \(\pi=(1,1+s,1)/(3+s)\).

**Critical window and relaxation scale.** Let \(r_*=\tfrac12(a+b)\), \(s=e^{-\beta r_*}\), and \(r_\beta=r_*+\xi/\beta\). Then \(w=s\tau\), where \(\tau=e^{-\xi}>0\). Substituting \(x=1+s z\) into \(p(x)=0\), dividing by \(s^2\), and letting \(s\to0\), the two near-one roots satisfy the limiting quadratic
\[
 2z^2-\tau z-1=0.
\]
Its simple roots are \(d_\pm=(\tau\pm\sqrt{\tau^2+8})/4\). Continuity of these simple roots or the implicit-function theorem gives
\[
 \lambda_+=1+s d_++O(s^2),\qquad
 \lambda_{\rm m}=1+s d_-+O(s^2).
\]
Vieta then gives \(\lambda_{\rm n}=-1+s\tau/2+O(s^2)\). Insert \(\lambda_+\) and \(d=s d_++O(s^2)\) into the exact marginal expression to obtain
\[
 \pi_0\to\frac{1}{1+2d_+^2}
 =\frac12\left(1-\frac{\tau}{\sqrt{\tau^2+8}}\right),\qquad
\pi_1,\pi_2\to\frac{1-\pi_0}{2}.
\]
The limiting transition matrix sends \(0\to0\), \(1\to2\), and \(2\to1\) deterministically, so convergence of its finite-dimensional cylinder probabilities gives the stated mixture of the fixed-point and alternating-orbit measures.

Finally,
\[
\begin{aligned}
1-\lambda_{\rm m}/\lambda_+&=s\sqrt{\tau^2+8}/2+O(s^2),\\
1-|\lambda_{\rm n}|/\lambda_+&=s(3\tau+\sqrt{\tau^2+8})/4+O(s^2).
\end{aligned}
\]
Their leading coefficients are equal precisely at \(\tau=1\): solving \(3\tau=\sqrt{\tau^2+8}\) gives \(\tau=1\). Taking their minimum establishes the claimed critical-window spectral profile. The previously proved exact comparison establishes the mode switch even at finite \(\beta\).

## Verification

Run `python3 verify.py` from the directory containing the supplied standalone checker. It checks \(42\) rational combinations of \(s,w\) for the exact characteristic identity, crossing sign and finite-temperature stationary equations; it additionally checks \(15\) critical-window parameter instances for consistency with the analytical limits. Expected output: `VERIFY_OK rational_parameter_cases=42 crossover_cases=15`. The rational identities are exact; the numerical root calculations have finite precision. Neither finite test is used as a proof of the universal classification.

## Relationship to prior work

The zero-temperature selection of Gibbs states for *fixed* locally constant potentials is classical. Chazottes, Gambaudo and Ugalde (2009) provide a renormalization algorithm, while Garibaldi and Thieullen (2012), especially Section 6.1 and Figure 5, explicitly classify three-state fixed-potential systems with a fixed-point ground component and a period-two ground component. Thus the existence of the competing phases and the fixed-potential limiting mixture are **not claimed as new**. Jenkinson and Pollicott's 2026 proof of Brémont's convergence theorem supplies a recent thermodynamic-formalism motivation but establishes neither a subleading spectral-mode threshold nor the joint temperature-parameter spectral crossover.

The specific result here is the **exact, temperature-independent switching of the dominant nonstationary eigenvalue between positive and negative real modes**, its closed-form equality case, and the associated spectral crossover. Those statements concern the non-Perron spectrum, which is not determined by the cited equilibrium-weight classifications. The critical-window measure is included for interpretation, not asserted to be independently novel.

## Limitations

This result is restricted to the stated three-state primitive graph and positive penalties. A negative dominant nonstationary eigenvalue is a statement about spectral relaxation and need not dominate every particular observable's correlation function if that observable has zero projection onto its eigenmode. The critical-window estimates hold for fixed real \(\xi\) as \(\beta\to\infty\), not uniformly over an unbounded range of \(\xi\). The exact finite-temperature classification does not require such a limit. Earlier equivalent coverage under alternate Markov-chain terminology cannot be excluded without independent literature review; no independent audit is claimed.

## References

- O. Jenkinson and M. Pollicott, *An elementary proof of Brémont's theorem on the convergence of equilibrium measures at temperature zero*, arXiv:2610.19990v1, first posted 14 October 2026, https://arxiv.org/abs/2610.19990.
- J.-R. Chazottes, J.-M. Gambaudo and E. Ugalde, *Zero-temperature limit of one-dimensional Gibbs states via renormalization: the case of locally constant potentials*, arXiv:0903.1212, https://arxiv.org/abs/0903.1212.
- E. Garibaldi and P. Thieullen, *Description of Some Ground States by Puiseux Techniques*, Journal of Statistical Physics 146 (2012), 125–180, DOI:10.1007/s10955-011-0357-x, Section 6.1, https://www.math.u-bordeaux.fr/~pthieull/Recherche/Publications/Garibaldi_Thieullen2012_01.pdf.
