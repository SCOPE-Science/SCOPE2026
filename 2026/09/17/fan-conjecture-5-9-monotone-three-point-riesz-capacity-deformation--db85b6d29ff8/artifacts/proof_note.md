# Resolving Fan's Step-2 monotonicity conjecture for three-point Riesz capacity

## Statement

Qiuling Fan, *Riesz capacity ratios with negative exponents*, arXiv:2609.11186v1 (2026), Conjecture 5.9:

Let \(r\ge 2\), let \(B=e^{i\phi}\), \(C=e^{-i\phi}\) with
\(\phi\in(\pi/2,2\pi/3]\), and let \(A=e^{i\psi}\) with
\(\psi\in[0,2\pi-3\phi]\). Then \(BC\) is the longest side. The conjecture
states that the Riesz \((-r)\)-capacity of \(\{A,B,C\}\) is maximized at the
right endpoint \(\psi=2\pi-3\phi\), where \(AC=BC\).

The argument below proves the stronger statement that the energy
\(U_r(\{A,B,C\})\), and hence the capacity \(C_r=U_r^{1/r}\), is
nondecreasing throughout the interval.

## Proof

Put
\[
a=\frac{\phi-\psi}{2},\qquad b=\frac{\phi+\psi}{2}.
\]
Then \(a+b=\phi\), \(b-a=\psi\), and
\[
0<a\le b\le \pi-\phi\le \frac{\pi}{2}.
\]
The side lengths are
\[
x=AB=2\sin a,\qquad y=AC=2\sin b,\qquad c=BC=2\sin\phi,
\]
with \(x\le y\le c\).

Write
\[
X=x^r,\qquad Y=y^r,\qquad Z=c^r,\qquad D=X+Y-Z.
\]

By the Clark--Laugesen three-point formula quoted as Fan's Lemma 5.7,
\[
U_r=
\begin{cases}
Z/2,&D\le0,\\[2mm]
\dfrac{2XYZ}{4XY-D^2},&D>0.
\end{cases}
\]

Thus the energy is constant on the two-point branch \(D\le0\).
On the three-point branch define
\[
H=\frac{D^2}{XY}.
\]
Then
\[
U_r=\frac{2Z}{4-H},
\]
so it suffices to prove that \(H\) is nondecreasing.

Differentiate with respect to \(\psi\):
\[
\frac{X'}X=-\frac r2\cot a,\qquad
\frac{Y'}Y=\frac r2\cot b,\qquad
D'=\frac r2(Y\cot b-X\cot a).
\]
Hence
\[
\frac1r\frac{d}{d\psi}\log H
=
\frac{Y\cot b-X\cot a}{D}
+\frac{\cot a-\cot b}{2}.
\]
Multiplication by the positive factor \(2D\sin a\sin b\) shows that
the sign is the sign of
\[
(Y-X)\sin(a+b)-Z\sin(b-a)
=(Y-X)\sin\phi-Z\sin\psi. \tag{1}
\]

Normalize
\[
u=\frac{\sin a}{\sin\phi},\qquad
v=\frac{\sin b}{\sin\phi}.
\]
Because \(b\le\pi-\phi\le\pi/2\),
\[
0<u\le v\le1.
\]
The condition \(D>0\) is exactly
\[
u^r+v^r>1. \tag{2}
\]
Also,
\[
v^2-u^2
=\frac{\sin^2b-\sin^2a}{\sin^2\phi}
=\frac{\sin(a+b)\sin(b-a)}{\sin^2\phi}
=\frac{\sin\psi}{\sin\phi}. \tag{3}
\]
After dividing (1) by \(\sin^{r+1}\phi>0\), the needed sign inequality is
therefore
\[
v^r-u^r\ge v^2-u^2. \tag{4}
\]

### Power-difference lemma

For \(r\ge2\), if \(0\le u\le v\le1\) and \(u^r+v^r\ge1\), then
\[
v^r-u^r\ge v^2-u^2.
\]

For \(r=2\) there is equality. Assume \(r>2\), put \(q=r/2>1\),
\(s=u^2\), \(t=v^2\). We need
\[
t^q-s^q\ge t-s,\qquad s^q+t^q\ge1.
\]
Let \(\alpha=1/q\in(0,1)\), \(A=s^q\), \(B=t^q\). Then
\(0\le A\le B\le1\), \(A+B\ge1\), and the target becomes
\[
B-A\ge B^\alpha-A^\alpha. \tag{5}
\]

For fixed \(A\), define
\[
\Phi_A(B)=B-A-B^\alpha+A^\alpha.
\]
For \(B\ge1/2\),
\[
\Phi_A'(B)=1-\alpha B^{\alpha-1}\ge0,
\]
because \(\alpha2^{1-\alpha}\le1\). (For example,
\(\log\alpha\le\alpha-1\) and \(\log2<1\).)

If \(A\ge1/2\), then \(B\ge A\) and
\(\Phi_A(B)\ge\Phi_A(A)=0\).

If \(A\le1/2\), the condition \(A+B\ge1\) gives \(B\ge1-A\), so
\[
\Phi_A(B)\ge \Phi_A(1-A)
=1-2A-(1-A)^\alpha+A^\alpha=:F(A).
\]
On \(0\le A\le1/2\),
\[
F(0)=F(1/2)=0,
\]
and
\[
F''(A)
=\alpha(\alpha-1)\left(A^{\alpha-2}-(1-A)^{\alpha-2}\right)<0
\]
for \(0<A<1/2\). Thus \(F\) is concave with zero endpoint values, hence
\(F(A)\ge0\). This proves (5), and therefore the lemma.

Returning to the geometric problem, (2) and the lemma imply (4).
Hence \(H'\ge0\), and therefore \(U_r'\ge0\), wherever \(D>0\).
For \(r>2\) and \(\psi>0\), the inequality is strict on the three-point
branch.

At a branch boundary \(D=0\), the three-point formula reduces continuously to
\(U_r=Z/2\). A positive branch cannot later return to \(D=0\): inside such a
branch \(U_r>Z/2\) and is nondecreasing, so it cannot reach the boundary value
\(Z/2\) again. Therefore the two-point branch, if present, is an initial
constant interval followed by a terminal nondecreasing three-point branch.
Consequently \(U_r\), and hence \(C_r=U_r^{1/r}\), is globally nondecreasing
in \(\psi\).

The maximum is attained at \(\psi=2\pi-3\phi\), where \(AC=BC\).
This proves Fan's Conjecture 5.9.

## Corollary: odd regular polygons

Fan states immediately after Conjecture 5.9 that Conjecture 5.6 follows by
combining Step 2 (Conjecture 5.9) with the already proved symmetric Step 1
(Lemma 5.8), after reducing obtuse/right triangles to the two-point branch.
Thus the above theorem completes Fan's stated proof scheme for the odd regular
polygon equilibrium formula for every odd \(N\ge3\) and \(r>2\).

Primary source:
https://arxiv.org/abs/2609.11186
https://arxiv.org/html/2609.11186
