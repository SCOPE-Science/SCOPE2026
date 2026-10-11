# Exact doubled-harmonic Carathéodory–Fejér family
## Finding
For every integer \(m\ge2\), define
\[
M_m=\sup\left\{a\in\mathbb R:\exists b,c\in\mathbb R,\ 1+a\cos\theta+b\cos(m\theta)+c\cos(2m\theta)\ge0\ \text{for every }\theta\in\mathbb R\right\}.
\]
Then
\[
M_m=\frac{3}{1+2\cos(2\pi/(3m))}.
\]
Moreover the extremizer is unique. Put
\[
\delta=\frac{2\pi}{3m},\qquad u=\cos\delta,\qquad A=\frac{3}{1+2u},\qquad q=\frac{2A\sin\delta}{m\sqrt3}.
\]
Then the unique extremizing polynomial is
\[
P_m(\theta)=1+A\cos\theta+(-1)^mB\cos(m\theta)+C\cos(2m\theta),
\]
where
\[
B=\frac{2(A-1)+q}{3},\qquad C=\frac{A-1-q}{3}.
\]
Equivalently, if \(\psi:\mathbb Z\to\mathbb R\) is positive definite, \(\psi(0)=1\), and
\[
\operatorname{supp}\psi\subseteq\{0,\pm1,\pm m,\pm2m\},
\]
then
\[
\psi(1)\le \frac{3}{2\bigl(1+2\cos(2\pi/(3m))\bigr)},
\]
and equality determines the real even sequence uniquely.

## Assumptions and scope
The integer satisfies \(m\ge2\). Coefficients are real, the constant coefficient is normalized to \(1\), and nonnegativity is required on the entire circle rather than on a finite grid. The distinguished coefficient is that of the first harmonic; the only free higher harmonics are \(m\) and \(2m\).

The case \(m=2\) reduces to the previously known sparse support \(\{1,2,4\}\) and gives \(M_2=3/2\). The theorem here is the uniform all-\(m\) formula and uniqueness statement.

## Proof
Set \(\theta_0=\pi-\delta\). For every feasible polynomial
\[
P(\theta)=1+a\cos\theta+b\cos(m\theta)+c\cos(2m\theta),
\]
we have
\[
\cos(m\theta_0)=\frac{(-1)^{m+1}}2,\qquad \cos(2m\theta_0)=-\frac12.
\]
Consequently the free higher coefficients cancel in the positive combination
\[
P(\pi)+2P(\theta_0)=3-a(1+2u)\ge0.
\]
Therefore \(a\le A\).

It remains to prove that the stated polynomial with \(a=A\) is nonnegative. By evenness it is enough to take \(0\le\theta\le\pi\), write \(\theta=\pi-\phi\), and put \(y=\cos(m\phi)\). Define the quadratic
\[
R(y)=1-C+By+2Cy^2
\]
and the function
\[
g(y)=A\cos\!\left(\frac1m\arccos y\right),\qquad -1\le y\le1.
\]
If \(s=\arccos(\cos(m\phi))\) and \(\psi=s/m\), then \(0\le\psi\le\phi\le\pi\). Hence \(\cos\psi\ge\cos\phi\), and
\[
P_m(\pi-\phi)=R(y)-A\cos\phi\ge R(y)-g(y).
\]

The chosen coefficients make \(R\) the quadratic Hermite interpolant of \(g\) with a simple node at \(1\) and a double node at \(-1/2\):
\[
R(1)=g(1)=A,
\]
\[
R(-1/2)=g(-1/2)=Au,
\]
and
\[
R'(-1/2)=g'(-1/2)=q.
\]
Indeed \(B+C=A-1\) and \(B-2C=q\), while \(A(u+1/2)=3/2\).

Let \(\alpha=1/m\). For \(-1<y\le1\), the standard hypergeometric expansion is
\[
\cos(\alpha\arccos y)={}_2F_1\!\left(-\alpha,\alpha;\frac12;\frac{1-y}{2}\right).
\]
For every nonconstant term of this series the coefficient
\[
\frac{(-\alpha)_n(\alpha)_n}{(1/2)_n n!}
\]
is negative, because \(0<\alpha<1\). Three derivatives with respect to \(y\) contribute the factor \((-1/2)^3\), so
\[
g^{(3)}(y)>0\qquad(-1<y<1).
\]
The Hermite remainder formula therefore gives, for \(-1<y\le1\),
\[
g(y)-R(y)=\frac{g^{(3)}(\xi)}6 (y-1)(y+1/2)^2\le0
\]
for some \(\xi\) between the interpolation nodes and \(y\). Continuity extends the inequality to \(y=-1\). Thus \(R(y)\ge g(y)\) on \([-1,1]\), and the preceding reduction yields \(P_m(\theta)\ge0\) for every real \(\theta\). This attains the upper bound.

For uniqueness, equality in the upper certificate forces both \(P(\pi)=0\) and \(P(\theta_0)=0\). Since \(\theta_0\) is an interior zero of a nonnegative smooth periodic function, also \(P'(\theta_0)=0\). With \(a=A\), the zero equations reduce to \(B+C=A-1\), while the derivative equation gives \(B-2C=q\). These two independent linear conditions uniquely recover the coefficients above.

## Verification
The analytic upper certificate uses two nonnegative evaluations and cancels both free higher harmonics exactly. The lower construction is an all-\(m\) Hermite-majorization argument; finite sampling is not used as a proof.

The bundled script `artifacts/verify.py` recomputes the coefficient formulas for \(2\le m\le200\), checks the two contact zeros and the derivative contact, checks the dual cancellation identity, verifies the Hermite interpolation identities, and scans both the circle polynomial and the quadratic majorant inequality. It also checks that \(m=2\) gives the known coefficients \(7/12\) and \(-1/12\).

## Relationship to prior work
Kolountzakis and Révész formulate the prescribed-support Carathéodory–Fejér problem and its equivalent positive-definite-sequence version, and their paper records several exactly solved support families. The inspected full text does not state the doubled-harmonic family \(\{m,2m\}\). Révész's earlier duality paper gives a broad minimax framework but does not numerically determine this family. Krenedits and Révész later extend the general reduction to locally compact Abelian groups; that structural reduction likewise does not supply the formula above.

The special case \(m=2\), namely the support \(\{1,2,4\}\), is already covered by an exact sparse-support result and is not claimed as new in isolation. A separate resonance result for augmenting the singleton \(m\)-th harmonic by one frequency implies only that the choice \(2m\) strictly improves the singleton constant; it does not determine the sharp value or extremizer. The present theorem gives the exact value and unique extremizer simultaneously for every \(m\ge2\).

## Limitations
The theorem treats the specific doubled-harmonic family \(\{1,m,2m\}\) with real even coefficients. It does not evaluate arbitrary two-element higher-frequency supports, nor does it assert an analogous formula when additional harmonics are allowed.

The originality comparison covered the directly relevant prescribed-support papers, a general duality source, exact semantic searches for the family and its positive-definite reformulation, and the nearest known sparse special cases. A residual literature risk remains that the same family may appear in older or poorly indexed cosine-polynomial literature under different notation.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1, first public version 2003-02-17; Canadian Journal of Mathematics 58 (2006), 401–418, DOI 10.4153/CJM-2006-017-8.
2. Sz. Gy. Révész, *Some trigonometric extremal problems and duality*, Journal of the Australian Mathematical Society 50 (1991), 384–390, DOI 10.1017/S1446788700032985.
3. S. Krenedits and S. Gy. Révész, *The Carathéodory-Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1, first public version 2013-03-30.
