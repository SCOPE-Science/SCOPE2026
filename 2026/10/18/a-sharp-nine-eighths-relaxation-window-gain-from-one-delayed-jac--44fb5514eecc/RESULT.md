# A sharp nine-eighths relaxation-window gain from one delayed Jacobi message

## Finding

For any real symmetric positive definite \(2\times2\) matrix \(A\) with a nonzero off-diagonal entry, compare three fixed round-based weighted-Jacobi communication protocols: both off-diagonal messages are current, exactly one is one round stale, or both are one round stale. Every round updates **both** coordinates simultaneously; each coordinate always reads its own current value. Let the common relaxation be \(\beta>0\), and let the normalized coupling be
\[
0<r=\frac{|A_{12}|}{\sqrt{A_{11}A_{22}}}<1.
\]
Convergence to the unique solution from **every** finite initial error history is equivalent to the following sharp strict inequalities:
\[
\begin{array}{c|c}
\text{current/current}&0<\beta<\displaystyle\frac{2}{1+r}\\[4pt]
\text{one stale/current}&0<\beta<\displaystyle\frac{4}{1+\sqrt{1+8r^2}}\\[4pt]
\text{stale/stale}&0<\beta<\displaystyle\frac{2}{1+r}.
\end{array}
\]
Either choice of the single stale direction has the same threshold. The middle threshold is strictly larger than the other two for every \(0<r<1\), but delaying **both** off-diagonal messages loses this gain. Define the ratio of the middle admissible upper bound to the synchronized upper bound as
\[
R(r)=\frac{2(1+r)}{1+\sqrt{1+8r^2}}.
\]
Then
\[
1<R(r)\le\frac98,
\qquad R(r)=\frac98\ \Longleftrightarrow\ r=\frac27.
\]
At the maximizing coupling, the synchronous and two-delayed ceilings are \(14/9\), whereas the one-delayed ceiling is \(7/4\). For instance, at \(\beta=5/3\), exactly the one-delayed protocol converges universally. At \(\beta=1\), by contrast, the three exact asymptotic factors are \(r\), \(r^{2/3}\), and \(r^{1/2}\), so the additional stability window must not be confused with faster convergence at an equal standard relaxation.

## Assumptions and scope

Let \(A=\begin{psmallmatrix}a&c\\c&b\end{psmallmatrix}\), with \(a,b>0\), \(ab>c^2\), \(c\ne0\), and an arbitrary right-hand side. Write the exact solution as \(x_*\). Diagonal scaling of the error by \(\operatorname{diag}(\sqrt a,\sqrt b)\), followed when necessary by a sign change in the second coordinate, conjugates the normalized error coupling to \(\begin{psmallmatrix}1&r\\r&1\end{psmallmatrix}\). Thus let \(u_k,v_k\) denote those normalized errors. Set \(q=1-\beta\) and \(s=\beta r>0\).

The **current/current** protocol is
\[
u_{k+1}=q u_k-sv_k,\qquad v_{k+1}=q v_k-su_k.
\]
The **one-stale** protocol (second coordinate's message to the first coordinate is one round old) is
\[
u_{k+1}=q u_k-sv_{k-1},\qquad v_{k+1}=qv_k-su_k.
\]
The **stale/stale** protocol is
\[
u_{k+1}=q u_k-sv_{k-1},\qquad v_{k+1}=qv_k-su_{k-1}.
\]
All initial values required by these recurrences are arbitrary real numbers; each history is then followed deterministically. No random sampling, changing delays, asynchronous write ordering within a round, communication cost model, or floating-point error is assumed. “Converges universally” means both normalized errors tend to zero for every such history, not monotone norm contraction in every round. The endpoint \(r=0\) is excluded because no messages then matter, and \(r=1\) is excluded by positive definiteness.

## Proof

**1. Characteristic matrices.** The current/current update has eigenvalues \(q+s\) and \(q-s\). With \(q=1-\beta\) and \(s=\beta r\), both eigenvalue moduli are below one exactly when \(0<\beta<2/(1+r)\).

On the state \((u_k,v_k,v_{k-1})\), the one-stale companion matrix is
\[
C_1=\begin{pmatrix}q&0&-s\\-s&q&0\\0&1&0\end{pmatrix},
\qquad \det(zI-C_1)=z(z-q)^2-s^2.
\]
This type of augmented matrix for one delayed direction is a known modeling device; novelty is not claimed for the matrix itself.

For \(0<\beta\le1\), the quantity \(q\) lies in \([0,1)\). If any root \(z\) satisfied \(|z|\ge1\), then
\[
|z|\,|z-q|^2\ge(1-q)^2=\beta^2>\beta^2r^2=s^2,
\]
contradicting its characteristic equation. Hence this whole regime is stable.

For \(\beta>1\), write \(d=\beta-1>0\). The characteristic polynomial becomes \(F(z)=z(z+d)^2-s^2\). It is strictly negative on the negative real axis, satisfies \(F(0)=-s^2<0\), and is strictly increasing on the positive axis. Thus it has one positive real root \(p>0\) and one nonreal conjugate pair. The positive root obeys \(p<1\), since
\[
F(1)=\beta^2(1-r^2)>0.
\]
Vieta's product gives squared modulus \(s^2/p=(p+d)^2\) for each nonreal root, so the pair have modulus \(p+d\). Therefore universal stability holds exactly when \(p+d<1\). If \(\beta\ge2\), this is impossible. If \(1<\beta<2\), set \(t=2-\beta=1-d>0\). Monotonicity of \(F\) gives
\[
p+d<1\ \Longleftrightarrow\ p<t
\ \Longleftrightarrow\ F(t)>0
\ \Longleftrightarrow\ 2-\beta-\beta^2r^2>0.
\]
The positive solution of the strict quadratic inequality is \(\beta<4/(1+\sqrt{1+8r^2})\). At equality the conjugate pair has modulus one; beyond it their modulus exceeds one, so the condition is necessary as well as sufficient. All finite-dimensional linear recurrences converge for every initial history if and only if their companion spectral radii are below one; a unit or expanding eigenmode gives a real nonconvergent history.

**2. Both messages delayed.** Introduce sum and difference \(w_k=u_k+v_k\), \(d_k=u_k-v_k\). Their recurrences are
\[
w_{k+1}=q w_k-s w_{k-1},\qquad d_{k+1}=q d_k+s d_{k-1}.
\]
Their polynomials are \(z^2-qz+s\) and \(z^2-qz-s\). The latter has two real roots of opposite signs, and its negative root reaches \(-1\) exactly when \(1+q-s=2-\beta(1+r)=0\). For \(0<\beta<2/(1+r)\), the quadratic Schur conditions apply to both factors: \(s<1\), \(1-q-s=\beta(1-r)>0\), \(1+q-s=2-\beta(1+r)>0\), and \(1+q+s=2-\beta(1-r)>0\). Both factors are therefore Schur stable. At and beyond the endpoint the negative root of the difference mode is at or outside the unit circle. This proves the stale/stale ceiling.

**3. Sharp universal gain.** Write \(H=\sqrt{1+8r^2}\). Since \(0<r<1\), \(H<1+2r\), which follows upon squaring from \(4r(1-r)>0\). Hence \(R(r)>1\). For the upper bound observe the exact square identity
\[
81(1+8r^2)-(7+16r)^2=8(7r-2)^2\ge0.
\]
Thus \(H\ge(7+16r)/9\), giving
\[
R(r)=\frac{2(1+r)}{1+H}\le
\frac{2(1+r)}{1+(7+16r)/9}=\frac98.
\]
Equality holds precisely at \(r=2/7\). The numbers \(14/9\) and \(7/4\) follow by substitution. At \(\beta=7/4\) the one-stale characteristic polynomial factors exactly as
\[
\left(z-\frac14\right)\left(z^2+\frac74z+1\right),
\]
whose complex pair lies on the unit circle. At \(\beta=1\), the three characteristic spectra yield factors \(r\), \(r^{2/3}\), and \(\sqrt r\), respectively. This also shows how admissible-parameter enlargement and fixed-parameter speed can point in opposite directions.

## Verification

Run `python verify.py` with Python, NumPy and SymPy. The standalone script reconstructs all three companion characteristic polynomials, the sharp square identity and endpoint factorization symbolically; it also compares actual companion matrices with direct delayed updates. It checks spectral radii on rationally specified coupling grids on each side of the three stability frontiers and checks the \(\beta=1\) factors. The executed program returned `PASS: 104 symbolic and numerical comparisons`. Its finite tests check the algebra and witnesses; the universal thresholds and maximizing ratio follow from the proof above.

## Relationship to prior work

Carson and Ma (2026) develop a broad asynchronous Jacobi/randomized Gauss–Seidel framework and give expected convergence-rate bounds with communication delays. Their principal analysis indexes one coordinate update at a time and assumes randomly selected coordinates. The result here instead fixes simultaneous two-coordinate rounds, three deterministic message-age patterns, and an exact overrelaxation phase diagram; those exact if-and-only-if bounds are not consequences of the cited stated expected-rate theorem.

Wolfson-Pou and Chow (2018) establish the **already-known qualitative fact** that some asynchronous Jacobi schedules may converge when synchronous Jacobi does not. No generic claim of asynchronous advantage is being made here. Moga and Dubois (1995/1996) even explicitly print an augmented three-state matrix for a one-stale-link numerical example. That matrix representation is prior art. Their inspected example and discussion do not state the specific three-protocol positive-definite relaxation phase diagram, its strict one-edge/two-edge contrast, or the sharp \(9/8\) maximization. These distinctions—not the companion-matrix technique—are the scope of the assessed contribution. Related 2025 semi-iterative/Chebyshev literature was only available at abstract level; an unnoticed stronger equivalent statement remains a bibliographic risk.

## Limitations

The theorem concerns exactly two variables, constant relaxation, a fixed one-round lag per specified directed message, simultaneous round-boundary commits, and exact arithmetic. It does not establish stability under arbitrary time-varying delay patterns with the same maximum age, nor guaranteed acceleration per wall-clock second or on larger matrices. Unit-circle boundary modes can fail to converge even though the underlying SPD matrix remains nonsingular. A previous derivation of the same precise overrelaxation thresholds under another terminology could supersede the originality claim; the older augmented-matrix calculation is explicitly acknowledged.

## References

1. Erin Carson and Yuxin Ma, *Asynchronous Jacobi and randomized Gauss–Seidel methods in shared and distributed memory: A unified convergence-rate analysis* (first public 2026-09-14), arXiv:2609.15605, https://arxiv.org/abs/2609.15605 .
2. Jordi Wolfson-Pou and Edmond Chow, *Convergence Models and Surprising Results for the Asynchronous Jacobi Method*, 2018, https://faculty.cc.gatech.edu/~echow/pubs/IPDPS18.pdf .
3. Adrian Moga and Michel Dubois, *Performance of Asynchronous Linear Iterations with Random Delays*, technical report CENG 95-06 (1995); conference 1996, https://ceng.usc.edu/techreports/1995/Dubois%20CENG%2095-06.pdf .
4. Jordi Wolfson-Pou and Edmond Chow, *Asynchronous Semi-iterative Methods and the Asynchronous Chebyshev Method with Multigrid Preconditioning*, SIAM Journal on Scientific Computing (2025), https://doi.org/10.1137/24M1669669 .
