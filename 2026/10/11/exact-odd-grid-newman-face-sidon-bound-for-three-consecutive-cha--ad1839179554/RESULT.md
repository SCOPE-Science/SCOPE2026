# Exact odd-grid Newman-face Sidon bound for three consecutive characters
## Finding
For every odd integer \(N\ge5\), let \(\zeta_N=e^{2\pi i/N}\) and define
\[
C_N^{\mathrm{New}}=\sup_{a,b,c\ge0,\ (a,b,c)\ne(0,0,0)}\frac{a+b+c}{\max_{k\in\mathbb Z_N}|a+b\zeta_N^k-c\zeta_N^{2k}|}.
\]
This is the coefficient \(\ell^1\)-to-sampled-supremum ratio restricted to the real sign face \((+,+,-)\) containing the classical continuous extremizer after translation.

Put
\[
\alpha=\frac{\pi}{2N},\qquad T=\sin\alpha\cos(2\alpha),\qquad D=\sin(2\alpha)\cos\alpha,
\]
and
\[
w=-\sin\alpha\sin(3\alpha)=T^2-D^2.
\]
Let \(R_N\in(0,1)\) be the unique root of
\[
D^2R^4+T(1-w)R^3+T(1+w)R-T^2=0.
\]
Define
\[
p=\frac{T(1-R_N^2)}{R_N},\qquad s=\frac1{1+p},\qquad M_N=s^2\bigl(1+p^2+w(1-R_N^2)\bigr).
\]
Then
\[
C_N^{\mathrm{New}}=M_N^{-1/2}.
\]
In particular, if \(S_N(\{0,1,2\})\) denotes the unrestricted finite-cyclic Sidon constant, then
\[
S_N(\{0,1,2\})\ge C_N^{\mathrm{New}}.
\]
Moreover,
\[
C_N^{\mathrm{New}}=\sqrt2+\frac{3\sqrt2\,\pi^2}{16N^2}+O(N^{-4}).
\]

## Assumptions and scope
The modulus \(N\) is odd and at least \(5\). The character set is the consecutive triple \(\{0,1,2\}\) on \(\mathbb Z_N\). Coefficients are restricted to the canonical real sign face
\[
a+bz-cz^2,\qquad a,b,c\ge0.
\]
The ratio is homogeneous, so the proof normalizes \(a+b+c=1\). The result is an exact theorem for this face and therefore an explicit lower bound for the unrestricted finite-cyclic Sidon constant. No equality with the unrestricted odd-order Sidon constant is asserted.

The sign face is not an arbitrary slice: Newman's continuous extremizer for \(\{0,1,2\}\), written by Neuwirth as \(1+2i z+z^2\), becomes \(1+2z-z^2\) after translating the circle variable by \(-\pi/2\).

## Proof
Normalize \(a+b+c=1\), and put
\[
s=a+c,\qquad d=a-c,\qquad b=1-s.
\]
For \(z=e^{i\theta}\) and \(x=\cos\theta\), multiplication by \(e^{-i\theta}\) gives
\[
|a+bz-cz^2|^2=s^2+b^2+2bdx-(s^2-d^2)x^2=:q(x).
\]
Thus \(q\) is a concave quadratic whenever \(a,c>0\).

Let \(u<0<v\) be the two adjacent values of \(\cos(2\pi k/N)\) that straddle zero. Write
\[
t=\frac{u+v}{2},\qquad T=|t|,\qquad D=\frac{v-u}{2},\qquad w=uv=T^2-D^2.
\]
For odd \(N\), elementary regular-polygon geometry gives exactly
\[
T=\sin\alpha\cos(2\alpha),\qquad D=\sin(2\alpha)\cos\alpha,
\]
with \(\alpha=\pi/(2N)\), and hence \(w=-\sin\alpha\sin(3\alpha)\).

Consider
\[
F(R)=D^2R^4+T(1-w)R^3+T(1+w)R-T^2.
\]
Because \(D,T>0\), \(-1<w<0\), and
\[
F'(R)=4D^2R^3+3T(1-w)R^2+T(1+w)>0
\]
for \(R>0\), while \(F(0)<0<F(1)\), there is a unique \(R_N\in(0,1)\) with \(F(R_N)=0\).

Let \(\sigma=\operatorname{sgn}(t)\), put
\[
r=\sigma R_N,\qquad p=\frac{T(1-R_N^2)}{R_N},\qquad s=\frac1{1+p},\qquad d=rs,
\]
and define
\[
a=\frac{s+d}{2},\qquad b=1-s,\qquad c=\frac{s-d}{2}.
\]
All three coefficients are positive. The identity
\[
pr=t(1-r^2)
\]
says that the vertex of \(q\) is exactly \(t\). Hence
\[
q(u)=q(v)=M_N=s^2\bigl(1+p^2+w(1-R_N^2)\bigr).
\]
Since \(u\) and \(v\) are adjacent sampled cosines and \(t\) is their midpoint, every other sampled cosine lies at least as far from the vertex. Concavity therefore gives \(q(x)\le M_N\) at every grid point. This proves attainment.

It remains to prove optimality on the whole sign face. Reflect the pair \(u,v\) if necessary so that its midpoint is \(T>0\), and write the reflected endpoints as
\[
\ell=T-D<0<h=T+D.
\]
For the candidate above, set
\[
\lambda=\frac{(D+T)(DR_N^2+T)}{2DT(1+R_N^2)}.
\]
The strict increase of \(F\) also gives \(R_N^2<T/D\): indeed
\[
F\!\left(\sqrt{T/D}\right)=\frac{T^{3/2}(D+T)\bigl(1-(D-T)^2\bigr)}{D^{3/2}}>0.
\]
Therefore \(0<\lambda<1\), since
\[
1-\lambda=\frac{(D-T)(T-DR_N^2)}{2DT(1+R_N^2)}.
\]

For arbitrary normalized \(a,b,c\ge0\), the sampled maximum is at least
\[
\max\{q(\ell),q(h)\}\ge \lambda q(\ell)+(1-\lambda)q(h)=:L(a,c).
\]
Put
\[
X=\lambda\ell+(1-\lambda)h,\qquad Y=\lambda\ell^2+(1-\lambda)h^2.
\]
After eliminating \(b=1-a-c\), the Hessian of \(L\) in \((a,c)\) is
\[
4\begin{pmatrix}1-X&1-Y\\1-Y&1+X\end{pmatrix}.
\]
Its determinant is \(16(2Y-X^2-Y^2)>0\). To see this, note that each point \((x,x^2)\) with \(-1<x<1\) lies strictly inside the disk
\[
X^2+(Y-1)^2\le1,
\]
and \((X,Y)\) is a strict convex combination of the two distinct endpoint points. Thus \(L\) is strictly convex.

The displayed value of \(\lambda\) makes the first-order condition in the \(d\)-direction vanish. The remaining first-order condition reduces exactly to \(F(R_N)=0\). Hence the constructed coefficients are the unique minimizer of \(L\) on the normalized sign face. Consequently every normalized \((a,b,c)\) satisfies
\[
\max_k|a+b\zeta_N^k-c\zeta_N^{2k}|^2\ge M_N,
\]
and the constructed coefficients attain equality. This proves \(C_N^{\mathrm{New}}=M_N^{-1/2}\).

For the asymptotic law, substitute \(\alpha=\pi/(2N)\) into the defining equation. The unique small root has
\[
R_N=\alpha-\frac{\alpha^3}{6}+O(\alpha^5),
\]
which yields
\[
p=1-3\alpha^2+O(\alpha^4),\qquad M_N=\frac12-\frac{3\alpha^2}{4}+O(\alpha^4).
\]
Therefore
\[
C_N^{\mathrm{New}}=\sqrt2+\frac{3\sqrt2}{4}\alpha^2+O(\alpha^4)
=\sqrt2+\frac{3\sqrt2\,\pi^2}{16N^2}+O(N^{-4}).
\]

## Verification
The proof is analytic for every odd \(N\ge5\). The accompanying `artifacts/verify.py` reconstructs the unique root, the coefficients, the two active samples, and the convex dual weight for every odd \(N\) from \(5\) through \(1001\). It checks the exact formula numerically, positivity of the convex certificate, stationarity, and deterministic pseudorandom sign-face competitors. It reports

`VERIFY_OK odd_N=5..1001 random_per_N=40 asymptotic_tail_maxerr=6.699e-06`

The finite replay is corroborative only. It is not used to infer the all-modulus theorem.

## Relationship to prior work
Neuwirth proves the continuous-circle three-frequency Sidon problem exactly. In particular the continuous Sidon constant of \(\{0,1,2\}\) is \(\sqrt2\), and his account records the Newman extremizer \(1+2i z+z^2\), equivalent by translation to the sign face used here. That continuous result does not determine the maximum after replacing the full circle by an odd finite root-of-unity grid.

A published finite-cyclic result determines the unrestricted Sidon constant for every even \(N\ge4\), namely \(\sqrt{1+\sec^2(\pi/N)}\), and explicitly leaves odd orders untreated. Another published result solves the all-\(N\) finite-grid phase minimax when all three coefficient moduli are fixed equal; it explicitly does not treat variable magnitudes. The present theorem instead optimizes magnitudes exactly on the canonical Newman sign face for every odd \(N\ge5\). Neither of those statements implies the root equation, the optimizing unequal magnitudes, or the displayed odd-grid lower-bound asymptotic.

## Limitations
The result does not prove the unrestricted Sidon constant for odd cyclic groups. In particular, possible complex-phase competitors outside the Newman sign face are not ruled out. The exact formula is therefore stated as a sharp face constant and a rigorous lower bound for the unrestricted constant. Numerical agreement with unrestricted optimization is not part of the theorem.

The originality comparison found no equivalent restricted-face formula, but older finite interpolation or crest-factor literature could encode the same two-contact optimization under different terminology.

## References
1. Stefan Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145, first public version 2001-02-19; primary MSC 42A05.
2. *Exact Sidon constant of three consecutive characters on even cyclic groups*, published-finding corpus record `2026/10/4/SCOPE-exact-sidon-constant-of-three-consecutive-characters-on-even-cyc--b76331aa4281`.
3. *Exact finite-grid phase minimum for the consecutive unimodular trinomial*, published-finding corpus record `2026/10/4/SCOPE-exact-finite-grid-phase-minimum-for-the-consecutive-unimodular-t--49933ee8abec`.
