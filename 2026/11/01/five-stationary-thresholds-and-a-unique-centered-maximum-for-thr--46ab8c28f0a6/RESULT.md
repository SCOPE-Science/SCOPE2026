# Five stationary thresholds and a unique centered maximum for three-Hermite half-line concentration

## Finding

Let \(h_0,h_1,h_2\) be the first three normalized Hermite functions on \(\mathbb R\). Set
\[
 A(t)_{jk}=\int_t^\infty h_j(x)h_k(x)\,dx\quad(0\le j,k\le2),
 \qquad V(t)=\operatorname{tr}\!\bigl(A(t)(I_3-A(t))\bigr).
\]
The function \(V\) is even and has **exactly five stationary points**: \(0\), \(\pm\alpha\), and \(\pm\beta\), with \(0<\alpha<1<\beta<129/100\). Here \(\alpha\) and \(\beta\) are the two positive roots of the explicit equation
\[
 \operatorname{erf}(t)=\frac{e^{-t^2}}{\sqrt\pi}\,
 \frac{t(8t^6+12t^4+14t^2+1)}{4t^4+3}.
\]
The origin is the **unique global maximum**, with exact value
\[
 V(0)=\frac34-\frac{3}{2\pi}.
\]
The points \(\pm\alpha\) are strict local minima, while \(\pm\beta\) are strict secondary local maxima. Numerically, \(\alpha\approx0.665872610694\), \(\beta\approx1.282889686562\), \(V(\alpha)\approx0.203271109849\), and \(V(\beta)\approx0.259802098140\); the central value is approximately \(0.272535170724\). The assertion is for **all real thresholds**, not a sampled or asymptotic regime.

## Assumptions and scope

Use the physicists' normalized Hermite functions
\[
 h_0(x)=\pi^{-1/4}e^{-x^2/2},\qquad
 h_1(x)=\sqrt2\,x h_0(x),\qquad
 h_2(x)=\frac{2x^2-1}{\sqrt2}\,h_0(x).
\]
Then \(A(t)\) is a real symmetric positive contraction. It is the exact three-dimensional Hermite fiber of horizontal half-plane concentration on the **full order-three** polyanalytic Fock space under the standard Fourier–Hermite fiber realization [1–3]. The variable \(t\) is the Hermite integration threshold; the corresponding physical half-plane coordinate may involve a normalization-dependent affine rescaling. This theorem describes the finite fiber invariant \(V(t)\), **not** the trace of an infinite-dimensional Toeplitz operator.

## Proof

**Step 1: Explicit matrix and variance.** Put \(E(t)=\operatorname{erf}(t)\), \(w(t)=e^{-t^2}/\sqrt\pi\), and \(F(t)=(1-E(t))/2\). Elementary Gaussian tail integrations give the exact matrix
\[
 A(t)=F(t)I_3+w(t)
 \begin{pmatrix}
 0&1/\sqrt2&t/\sqrt2\\
 1/\sqrt2&t&t^2+1/2\\
 t/\sqrt2&t^2+1/2&t^3+t/2
 \end{pmatrix}.
\]
The trace of the displayed polynomial matrix is \(P(t)=t(2t^2+3)/2\), and the trace of its square is
\[
 Q(t)=\frac{(2t^2+1)(2t^4+5t^2+6)}4.
\]
Consequently
\[
 V(t)=\frac34(1-E(t)^2)+w(t)E(t)P(t)-w(t)^2Q(t).
\]
Because \(h_j(-x)=(-1)^j h_j(x)\), the matrix \(A(-t)\) is conjugate to \(I_3-A(t)\) by the diagonal parity matrix. Hence \(V(-t)=V(t)\). Direct differentiation, using \(E'=2w\) and \(w'=-2tw\), yields
\[
 V'(t)=\frac{w(t)}2\Big[w(t)t(8t^6+12t^4+14t^2+1)
  -E(t)(4t^4+3)\Big]. \tag{1}
\]

**Step 2: Exactly two positive stationary thresholds.** For \(t\ge0\) define
\[
 L(t)=\frac{E(t)}{w(t)}=2e^{t^2}\int_0^t e^{-u^2}\,du,\qquad
 R(t)=\frac{t(8t^6+12t^4+14t^2+1)}{4t^4+3},
\]
and \(H(t)=e^{-t^2}(L(t)-R(t))\). Equation (1) shows that, for \(t>0\), \(\operatorname{sgn}V'(t)=-\operatorname{sgn}H(t)\). Since \(L'=2+2tL\), an exact rational differentiation gives
\[
 H'(t)=\frac{e^{-t^2}}{(4t^4+3)^2}p(t^2),\qquad
 p(z)=64z^6+144z^4-32z^3-36z^2-120z+15. \tag{2}
\]
The coefficient sequence of \(p\) has exactly two sign changes. Moreover \(p(0)>0\), \(p(1/4)<0\), and \(p(1)>0\). Descartes' rule of signs, combined with these strict evaluations, proves that \(p\) has exactly two simple positive zeros, one in \((0,1/4)\) and one in \((1/4,1)\); there are no other positive zeros. Thus \(H\) first strictly increases, then strictly decreases, then strictly increases on the positive half-line. We have \(H(0)=0\) and
\[
 H(1)=e^{-1}(L(1)-5)<0,
\]
because \(L(1)=2e\int_0^1e^{-u^2}\,du<2\cdot3\cdot(1-1/3+1/10)=23/5<5\). Finally \(H(t)\to\sqrt\pi\) as \(t\to\infty\); here \(e^{-t^2}R(t)\to0\). The monotonicity pattern therefore forces exactly two positive zeros \(\alpha\) and \(\beta\), with \(0<\alpha<1<\beta\). Their derivative sign pattern is strictly negative, positive, negative on \((0,\alpha)\), \((\alpha,\beta)\), \((\beta,\infty)\), respectively. This proves all local classifications and the complete stationary-point count after reflection.

**Step 3: The central maximum dominates the side peaks.** At any positive stationary threshold, \(E=wR\); substituting in \(V\) gives
\[
 V(t)=\frac34-w(t)^2U(t),\qquad
 U(t)=\frac34R(t)^2-P(t)R(t)+Q(t)
 =\frac{64t^{14}+192t^{12}+432t^{10}+400t^8+348t^6+36t^4+69t^2+27}{2(4t^4+3)^2}.
\]
A direct rational factorization, using \(p\) from (2), is
\[
 \frac{d}{dt}\bigl(e^{-2t^2}U(t)\bigr)
 =-\frac{te^{-2t^2}(8t^6+12t^4+18t^2-3)p(t^2)}{(4t^4+3)^3}<0\qquad(t>1). \tag{3}
\]
We give an exact, reproducible rational certificate that \(\beta<129/100\) and \(e^{-2(129/100)^2}U(129/100)>3/2\); therefore (3) implies \(e^{-2\beta^2}U(\beta)>3/2\), which is the desired strict inequality \(V(\beta)<V(0)\).

To specify that certificate without floating point assumptions, write \(x=129/100\), \(z=x^2\), \(y=2z<4\), and, with rational arithmetic, define
\[
 I_- =\sum_{j=0}^{11}\frac{(-1)^j x^{2j+1}}{j!(2j+1)},\qquad
 B_- =\sum_{j=0}^{5}\frac{z^j}{j!},\qquad
 B_+=\sum_{j=0}^{12}\frac{y^j}{j!}+\frac75\frac{y^{13}}{13!}.
\]
The alternating series for \(\int_0^x e^{-u^2}du\) bounds it below by \(I_-\); the positive exponential series gives \(e^z>B_-\); and the geometric tail estimate \(y/14<2/7\) gives \(e^y<B_+\). The exact rational inequalities
\[
 2 B_- I_- >R(x),\qquad 2U(x)>3B_+
\]
are checked by `checker.py` using `fractions.Fraction` only. The first gives \(H(x)>0\); the zero structure and \(x>1\) imply \(\beta<x\). The second gives \(e^{-2x^2}U(x)>3/2\). Together with (3), this proves \(V(\beta)<V(0)\). Since \(V(t)\to0\) as \(|t|\to\infty\), the unique global maximizer is \(t=0\), where \(Q(0)=3/2\) and \(V(0)=3/4-3/(2\pi)\).

## Verification

Execute `python checker.py` from this package with Python 3, SymPy and SciPy available. It symbolically verifies the displayed matrix trace and square trace, the differentiated variance, the rational identity (2), the closed form for \(U\), and the factored derivative (3). It verifies both strict rational inequalities at \(x=129/100\) exactly and independently checks the matrix entries by numerical Gaussian quadrature at seven thresholds; it also reports numerical approximations of the two roots. Finite quadrature and root-finding are supplementary only: the all-real classification follows from the written sign, root-count, and rational-certificate arguments.

## Relationship to prior work

Sánchez-Nungaray et al. [1], Section 3, Theorem 4, establish the general Hermite-matrix symbol for horizontally invariant poly-Fock Toeplitz operators. Arroyo Neri et al. [2], Section 3, extend the fiber framework to Lagrangian-invariant symbols. Lee-Guzmán et al. [3] establish the full polyanalytic Fock Fourier–Hermite decomposition. The present assertion concerns a different subsequent question: the **complete global extrema of the trace projection defect for precisely three half-line Hermite modes**, including a strict comparison of the central and secondary peaks. In the analogous two-mode model the central threshold is instead a local minimum with two off-center global maxima; the three-mode reversal is not inferred by those general fiber representations.

## Limitations

The result is only for the first three consecutively indexed Hermite modes and the half-line cutoff, under the explicit normalization above. It gives no extremum classification for four or more modes or disconnected masks. The numerical root locations are illustrative approximations, not rational enclosures beyond the strict bounds proved here. The claim concerns a finite fiber rather than a trace-class global Toeplitz operator. Equivalence to an earlier finite-GUE/determinantal point-process variance calculation remains a possible historical-priority risk; no independent external mathematical audit has been performed.

## References

[1] A. Sánchez-Nungaray, C. González-Flores, R. R. López-Martínez and J. L. Arroyo-Neri, *Toeplitz Operators with Horizontal Symbols Acting on the Poly-Fock Spaces*, Journal of Function Spaces **2018**, Article 8031259, first published 16 July 2018. DOI: 10.1155/2018/8031259.

[2] J. L. Arroyo Neri, A. Sánchez-Nungaray, M. Hernández Marroquin and R. R. López-Martínez, *Toeplitz Operators with Lagrangian Invariant Symbols Acting on the Poly-Fock Space of \(\mathbb C^n\)*, Journal of Function Spaces **2021**, Article 9919243, first published 25 November 2021. DOI: 10.1155/2021/9919243.

[3] E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez and A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410v1, submitted 7 September 2023.
