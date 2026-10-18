# Exact normal-moment growth and the quenched–annealed separation in a coupled logistic predator map

## Finding

For the predator-free logistic boundary of the Lee–Chan–Im–Chan–Cheang Type-2 map, the natural chaotic probability has an *exact* parameter-dependent normal Lyapunov exponent and an exact \(2\times2\) transfer description of every second moment. At the centered coupling \(a=b/2\), the entire normal product telescopes, giving its second and fourth moments for every positive integer time. An open parameter region has negative almost-sure normal exponent and *positive* mean-square growth exponent. This distinction cannot be read from a single finite Lyapunov plot.

For \(a=b/2\) and \(2\sqrt2<b<4\), the two growth exponents are exactly
\[
 \chi=\log(b/4)<0,\qquad \lim_{n\to\infty}\frac{\log\mathbb E(Q_n^2)}n=\log(b^2/8)>0.
\]
The specific admissible example \((a,b)=(3/2,3)\) has rates \(\log(3/4)\) and \(\log(9/8)\), respectively.

## Assumptions and scope

Fix arbitrary real \(a>0\), \(b>0\), \(c>0\), and consider the polynomial map on \(\mathbb R^2\)
\[
 F_{a,b,c}(x,y)=\bigl(4x(1-x)-cxy,\;y(-a+bx+ay)\bigr).
\]
This is the published Type-2 map, with parameters \(\mu_0=4\), \(\mu_1=c\), \(\nu_0=a\), \(\nu_1=b\). The line \(y=0\) is invariant, and its \(x\)-dynamics on \([0,1]\) is \(L(x)=4x(1-x)\). The probability
\[
 d\mu(x)=\frac{dx}{\pi\sqrt{x(1-x)}}\quad (0<x<1)
\]
is invariant and mixing under \(L\). Let \(x_k=L^k(x_0)\), and define the normal derivative cocycle, *not* a nonlinear predator orbit, by
\[
 Q_0(x_0)=1,\qquad Q_n(x_0)=\prod_{k=0}^{n-1}(b x_k-a)\quad(n\ge1).
\]
This product is the lower-right diagonal entry in the derivative of \(F_{a,b,c}^n\) on \(y=0\), since the Jacobian there is upper triangular. Every expectation below is with respect to \(\mu\). All logarithms are natural. Values of \(x_0\) giving an exact zero of a factor are an at-most-countable set and do not alter the measure-theoretic statements.

**Exact almost-sure exponent.** For \(\mu\)-almost every \(x_0\), the limit \(\chi(a,b)=\lim_{n\to\infty}\log|Q_n(x_0)|/n\) exists and equals
\[
 \chi(a,b)=\begin{cases}
 \log(b/4),&0<a\le b,\\
 \log\!\left(\dfrac{a-b/2+\sqrt{a(a-b)}}2\right),&a>b.
 \end{cases}
\]
For \(0<b<4\), this exponent is negative, zero, or positive according as \(a\) is less than, equal to, or greater than \((1+b/4)^2\). For \(b=4\), it vanishes for \(0<a\le4\) and is positive for \(a>4\); for \(b>4\) it is positive for every \(a>0\).

**Exact mean-square spectrum.** Put \(A=b/2-a\), \(B=-b/2\) and
\[
 M=\begin{pmatrix}A^2+B^2/2&AB\\B^2/2&AB\end{pmatrix},\qquad
 \tau=A^2+AB+B^2/2.
\]
For every integer \(n\ge0\),
\[
 \mathbb E_\mu Q_n^2=(M^n)_{11}.
\]
The mean-square exponential rate exists for all positive parameters and is \(\log\rho_+(a,b)\), where
\[
 \rho_+(a,b)=\frac{\tau+\sqrt{\tau^2-4A^3B}}2.
\]

**Centered parameter line and moments.** If \(a=b/2\), then for every \(n\ge0\),
\[
 \mathbb E_\mu Q_n^2=\left(\frac{b^2}{8}\right)^n,\qquad
 \mathbb E_\mu Q_n^4=\left(\frac b4\right)^{4n}
 \frac{2^{3n+1}+2^n}{3}.
\]
The quenched–mean-square discordance for \(2\sqrt2<b<4\) persists under sufficiently small independent perturbations of \(a\) and \(b\), by continuity of both strict exponent inequalities. The coupling parameter \(c>0\) is arbitrary throughout.

## Proof

**1. Conjugacy and normal derivative.** The measurable, two-to-one semiconjugacy \(x=\sin^2(\pi t)\), with \(t\in\mathbb R/\mathbb Z\), sends circle doubling \(t\mapsto2t\pmod1\) to \(L\) and sends normalized Lebesgue measure to \(\mu\). The derivative of the second map component at \(y=0\) in the normal direction is \(m(x)=bx-a\). Thus, on the doubling circle,
\[
 m(t)=A+B\cos(2\pi t),\qquad
 Q_n(t)=\prod_{k=0}^{n-1}\bigl(A+B\cos(2\pi 2^k t)\bigr).
\]
This identification is exact for the triangular boundary derivative and does not presume the nonlinear perturbed trajectory remains on the boundary.

**2. Quenched exponent.** The function \(\log|A+B\cos(2\pi t)|\) is integrable even if it has isolated zeros. Birkhoff's theorem for the ergodic doubling map therefore gives the almost-sure exponent equal to its integral. The standard logarithmic-cosine integral reads
\[
 \frac1{2\pi}\int_0^{2\pi}\log|A+B\cos\theta|\,d\theta
 =\begin{cases}
 \log(|B|/2),&|A|\le|B|,\\
 \log((|A|+\sqrt{A^2-B^2})/2),&|A|>|B|.
 \end{cases}
\]
Here \(|A|\le|B|\) exactly when \(0<a\le b\). On the complementary range \(a>b\), \(|A|=a-b/2\) and \(A^2-B^2=a(a-b)\). The stated formula follows. For \(a>b\), the second expression increases strictly with \(a\), and its unique zero is \(a=(1+b/4)^2\) if \(0<b<4\). At the boundary \(a=b\), the exponent is \(\log(b/4)\), yielding all listed sign regimes including the \(b=4\) degeneracy.

**3. Transfer closure for second moments.** The doubling Perron operator on periodic integrable functions is \((\mathcal Lf)(t)=[f(t/2)+f((t+1)/2)]/2\). Write \(C(t)=\cos(2\pi t)\) and \(w=A+BC\). Direct trigonometric multiplication and Fourier selection give the *exact identities*
\[
 \mathcal L(w^2)=A^2+B^2/2+(B^2/2)C,
 \qquad \mathcal L(w^2C)=AB+AB C.
\]
Consequently the two-dimensional space spanned by \(1,C\) is invariant under \(g\mapsto\mathcal L(w^2g)\), and its coefficient matrix is \(M\). Repeated application and integration of the constant coefficient establish \(\mathbb E Q_n^2=(M^n)_{11}\). The characteristic polynomial of \(M\) is \(z^2-\tau z+A^3B\).

For \(A<0\), all entries of \(M\) are strictly positive, so Perron–Frobenius theory gives a simple positive dominant root and a strictly positive leading coefficient for the first component. For \(A>0\), \(B<0\) implies \(\det M=A^3B<0\), so the two real eigenvalues have opposite signs; the positive one has the strictly larger absolute value because \(\tau=(A+B/2)^2+B^2/4>0\), and its coefficient in \((M^n)_{11}\) is \((M_{11}-\lambda_-)/(\lambda_+-\lambda_-)>0\). When \(A=0\), \(M\) has eigenvalues \(B^2/2,0\) and the moment formula is immediate. Thus the logarithmic second-moment growth rate is always \(\log\rho_+\).

**4. Exact resonance and fourth moment.** On \(a=b/2\), \(w(t)=-(b/2)\cos(2\pi t)\). Repeated use of \(\sin(2u)=2\sin u\cos u\) gives, away from the removable exceptional denominator set,
\[
 Q_n(t)=(-b/4)^n\frac{\sin(2^{n+1}\pi t)}{\sin(2\pi t)}.
\]
The identity extends continuously to the exceptional points. Put \(N=2^n\) and \(\vartheta=2\pi t\). The quotient \(\sin(N\vartheta)/\sin\vartheta\) equals the sum of \(N\) exponentials \(\sum_{j=0}^{N-1}e^{i(N-1-2j)\vartheta}\). Orthogonality yields its squared Haar norm \(N\). For the fourth power, the number of ordered solutions of \(j+k=\ell+m\) with all indices in \(\{0,\ldots,N-1\}\) equals
\[
 N^2+2\sum_{q=1}^{N-1}q^2=\frac{2N^3+N}{3}.
\]
Multiplying by \((b/4)^{2n}\) and \((b/4)^{4n}\), respectively, gives both exact moment formulas. Their exponential rates at \(a=b/2\) are \(\log(b/4)\) almost surely and \(\log(b^2/8)\) in the second moment. Strict opposite signs hold precisely for \(2\sqrt2<b<4\). Continuous dependence of \(\chi\) and \(\rho_+\) on positive \((a,b)\) proves a genuine open two-parameter discordance set.

## Verification

The accompanying standalone Python standard-library script `verify.py` multiplies finite Fourier polynomials with exact rational coefficients; it checks the transfer representation independently against direct Fourier integration, and checks second and fourth centered-line moments through seven iterates. It also performs deterministic numerical quadrature spot checks of the logarithmic integral. Run with `python verify.py`. The check reports 59 exact rational assertions and 6 numerical integration comparisons. Those finite checks corroborate, but do not replace, the infinite-time conjugacy, transfer and Fourier-counting proofs above.

## Relationship to prior work

Lee, Chan, Im, Chan and Cheang introduce the two-dimensional polynomial system and study fixed-point eigenvalues, iteration plots, approximate Lyapunov exponents and extinction regimes. Their Type-2 equation directly supplies the invariant logistic boundary, but the inspected complete open manuscript does not derive this boundary's parameter-exact normal cocycle, the finite-dimensional moment matrix, the centered-line fourth moments or the open discordance region. Classical full-chaos logistic semiconjugacy, Jensen's cosine integral, Perron transfer and finite Fourier orthogonality are established ingredients and are not themselves claimed new. Other known coupled-logistic maps with a multiplicative non-offset normal factor concern different transverse laws and do not imply the current two-parameter expressions.

## Limitations

The conclusions describe the *linear normal derivative* along the exactly invariant predator-free boundary and integration against its chaotic invariant probability. They are not theorems of global extinction of the nonlinear predator population, of a positive ecological state space for all initial conditions, or of convergence for every base orbit. Exceptional boundary orbits may have different exponents. Mean-square growth does not contradict almost-sure decay because rare large products dominate moments. The external literature comparison establishes best-known originality, not a proof of exhaustive priority; a general transfer-operator result could subsume the computation when specialized.

## References

1. W. S. Lee, H. F. Chan, K. I. Im, K. I. Chan, and U. H. Cheang, *Predator Extinction arose from Chaos of the Prey: the Chaotic Behavior of a Homomorphic Two-Dimensional Logistic Map in the Form of Lotka-Volterra Equations*, arXiv:2301.11669 (initial public version 27 January 2023), https://arxiv.org/abs/2301.11669 ; full open manuscript https://arxiv.org/html/2301.11669v2 .
2. P. Collet and J.-P. Eckmann, *Iterated Maps on the Interval as Dynamical Systems*, Birkhäuser (1980), for the classical logistic/doubling framework.
3. A. Boyarsky and P. Góra, *Laws of Chaos: Invariant Measures and Dynamical Systems in One Dimension*, Birkhäuser (1997), for the classical invariant-measure and transfer-operator framework.
