# Odd-multiple rigidity for one-frequency Carathéodory–Fejér augmentation
## Finding
For integers \(m\ge 3\) and \(n\ge 2\) with \(n\ne m\), set
\[
\mathcal M_{m,n}=\sup\left\{a\in\mathbb R:\exists b,c\in\mathbb R,\ 1+a\cos\theta+b\cos(m\theta)+c\cos(n\theta)\ge0\ \text{for every }\theta\in\mathbb R\right\}.
\]
Then
\[
\mathcal M_{m,n}=\sec\!\left(\frac{\pi}{2m}\right)
\quad\Longleftrightarrow\quad
n\equiv m\pmod{2m}.
\]
For every other distinct auxiliary frequency,
\[
\mathcal M_{m,n}>\sec\!\left(\frac{\pi}{2m}\right).
\]
Equivalently, adding one extra cosine harmonic to the singleton frequency \(m\) fails to improve its sharp first coefficient exactly when the added frequency is an odd multiple \(3m,5m,\ldots\).

## Assumptions and scope
All coefficients are real and the polynomial is required to be nonnegative on the full circle, not merely on a finite grid. The integer \(m\) satisfies \(m\ge3\); the auxiliary frequency satisfies \(n\ge2\) and \(n\ne m\). The theorem classifies equality with the singleton optimum but does not give a closed formula for the strictly larger value outside the resonance class.

Put
\[
\alpha=\frac{\pi}{2m},\qquad C=\cos\alpha,\qquad S=\sin\alpha.
\]
The singleton problem allowing only frequencies \(1\) and \(m\) has sharp first coefficient \(\sec\alpha\).

## Proof
Define
\[
P_m(\theta)=1+\sec\alpha\cos\theta+\frac{(-1)^m}{m}\tan\alpha\cos(m\theta).
\]
We first prove directly that \(P_m\ge0\) and determine its zero set.

Write \(\theta=\pi+x\), let \(y=\cos x\), and let \(T_m\) be the Chebyshev polynomial with \(T_m(\cos x)=\cos(mx)\). Since \(T_m(C)=0\) and \(T_m'(C)=m/S\),
\[
C P_m(\pi+x)
=C-y+\frac{S}{m}T_m(y)
=\frac{S}{m}\left(T_m(y)-T_m(C)-T_m'(C)(y-C)\right).
\]
It therefore suffices to show that the tangent line to \(T_m\) at \(C\) is globally supporting on \([-1,1]\).

Let \(x_0=\cos(\pi/m)=\cos(2\alpha)\). On \([x_0,1]\), \(T_m\) is strictly convex. Indeed, if \(y=\cos t\) with \(0<t<\pi/m\), then
\[
T_m'(y)=m\frac{\sin(mt)}{\sin t}.
\]
The derivative of the ratio with respect to \(t\) has numerator
\[
m\cos(mt)\sin t-\sin(mt)\cos t.
\]
For \(0<t<\pi/(2m)\), strict convexity of \(\tan\) on \((0,\pi/2)\) gives \(\tan(mt)>m\tan t\), so this numerator is negative. For \(\pi/(2m)\le t<\pi/m\), one has \(\cos(mt)\le0\), \(\sin(mt)>0\), and \(\cos t>0\), so it is again negative. Because \(dy/dt=-\sin t<0\), this proves \(T_m''(y)>0\). Hence \(T_m\) lies strictly above its tangent at \(C\) on \([x_0,1]\) except at \(C\).

For \(y\le x_0\), use \(T_m(y)\ge-1\). The tangent line is at most \(m(x_0-C)/S\), and
\[
m(C-x_0)>S.
\]
To see this, note
\[
C-\cos(2\alpha)=2\sin(3\alpha/2)\sin(\alpha/2),
\qquad
S=2\sin(\alpha/2)\cos(\alpha/2).
\]
Thus it is enough that \(m\sin(3\alpha/2)>\cos(\alpha/2)\). Since \(3\alpha/2=3\pi/(4m)\le\pi/4\), the chord bound \(\sin u\ge2u/\pi\) on \([0,\pi/2]\) gives \(m\sin(3\alpha/2)\ge3/2>1\ge\cos(\alpha/2)\). Therefore the supporting inequality is strict on \([-1,x_0]\).

Consequently \(P_m(\theta)\ge0\) for every \(\theta\), with equality exactly at
\[
\theta=\pi-\alpha\quad\text{or}\quad\theta=\pi+\alpha\pmod{2\pi}.
\]
At either contact point, \(\cos(m\theta)=0\) and \(\cos\theta=-C\). Hence every nonnegative polynomial of the singleton form \(1+a\cos\theta+b\cos(m\theta)\) satisfies \(1-aC\ge0\), so \(a\le\sec\alpha\). The explicit \(P_m\) attains the bound.

Now admit the frequency \(n\). At both contact points,
\[
\cos(n(\pi\pm\alpha))=(-1)^n\cos(n\alpha).
\]
This common value vanishes exactly when
\[
\cos\left(\frac{n\pi}{2m}\right)=0,
\]
which is equivalent to \(n=m(2k+1)\), or \(n\equiv m\pmod{2m}\). In that resonance case, evaluation at either contact annihilates both free higher harmonics and still gives \(a\le\sec\alpha\); the singleton extremizer with the \(n\)-coefficient set to zero attains equality.

Suppose instead that
\[
q=(-1)^n\cos(n\alpha)\ne0.
\]
Define
\[
R(\theta)=\cos\theta+\frac{2C}{q}\cos(n\theta).
\]
At each zero of \(P_m\), one has \(R=C>0\). By continuity there are neighborhoods of the two zeros on which \(R>0\). On the compact complement, \(P_m\) has a strictly positive minimum while \(R\) is bounded. Therefore, for all sufficiently small \(\varepsilon>0\),
\[
P_m(\theta)+\varepsilon R(\theta)\ge0
\qquad\text{for every }\theta.
\]
Its first-harmonic coefficient is \(\sec\alpha+\varepsilon\), proving strict improvement outside the odd-multiple resonance class.

## Verification
The proof above is analytic and covers every permitted \((m,n)\). The bundled script `artifacts/verify.py` independently checks the explicit singleton extremizer, its two contact points, the resonance criterion, and representative strict perturbations on bounded parameter ranges. The finite sampling performed by that script is corroborative only and is not used to infer the universal theorem.

## Relationship to prior work
Kolountzakis and Révész formulate the support-restricted Carathéodory–Fejér quantity \(M(H)\) for nonnegative cosine polynomials and its discrete counterpart; this is the direct framework containing the present problem. Their inspected formulation, comparison principles, and listed special cases do not state the all-parameter classification above for two allowed higher frequencies.

Neuwirth determines exact Sidon constants for three characters and obtains a related secant constant in a different extremal problem. That theorem concerns complex three-term uniform norms versus coefficient \(\ell^1\)-norms; it neither imposes nonnegativity nor gives the odd-multiple equality/strictness criterion here.

Krenedits and Révész extend Carathéodory–Fejér extremal problems to locally compact Abelian groups and explain reductions to cyclic problems. That broader structural theory supplies context but does not, in the inspected material, imply the present two-frequency resonance classification.

Two nearby exact calculations were also compared: the continuous support \(\{1,3,5\}\) case and the fixed support with higher frequencies \(\{3,4\}\). They concern isolated supports. The present theorem instead gives a complete infinite classification of when one arbitrary added frequency changes the singleton optimum.

## Limitations
The theorem determines exactly the no-improvement frequencies but not the exact value of \(\mathcal M_{m,n}\) in the strict regime. The originality comparison cannot rule out an equivalent statement hidden in older cosine-polynomial or positive-definite-sequence terminology; that is the main residual bibliographic risk. No claim is made for complex coefficients, non-even trigonometric polynomials, or simultaneous augmentation by more than one new higher frequency.

## References
1. S. Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145v1, first submitted 2001-02-19.
2. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1, first submitted 2003-02-17.
3. S. Krenedits and S. Gy. Révész, *The Carathéodory–Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1, first submitted 2013-03-30.
4. S. Gy. Révész, *The Least Possible Value at Zero of Some Nonnegative Cosine Polynomials and Equivalent Dual Problems*, Journal of Fourier Analysis and Applications, Kahane special issue (1995); inspected as historical comparison, with no electronic first-public date assigned here.
