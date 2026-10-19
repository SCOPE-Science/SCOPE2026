# An exact equilibrium-fold staircase for a sine-driven three-dimensional flow

## Finding

Consider the real autonomous flow
\[
\dot x=ax-kyz,\qquad \dot y=b\sin x+xz,\qquad \dot z=gxy-cz+d,
\]
with six strictly positive real parameters \(a,b,c,d,g,k\). Keep \(a,c,d,g,k\) fixed and vary the sine amplitude \(b>0\). The complete number and positions of *all* real equilibria are governed by one explicit threshold per sine half-wave.

Set \(P=ag/k\), \(A=\sqrt{P/c}=\sqrt{ag/(ck)}\), and
\[
s(u)=\sqrt{d^2+4cPu^2},\qquad
z_-(u)=\frac{d-s(u)}{2c},\qquad
z_+(u)=\frac{d+s(u)}{2c}\quad(u>0).
\]
For each integer \(m\geq0\), write \(I_m=(m\pi,(m+1)\pi)\) and define
\[
B_m(u)=\begin{cases}
-u z_-(u)/\sin u,&m\text{ even},\\
-u z_+(u)/\sin u,&m\text{ odd},
\end{cases}\qquad u\in I_m.
\]
Both formulas are positive on their stated intervals. The function \(B_0\) is strictly increasing from zero to infinity. For each \(m\geq1\), \(B_m\) diverges at both endpoints and has exactly one nondegenerate minimum \(T_m=B_m(u_m)>0\) at a point \(m\pi<u_m<(m+1/2)\pi\).

The full equilibrium set consists of the central point \((0,0,d/c)\) and, for each positive root \(u\in I_m\) of \(B_m(u)=b\), the two points
\[
\left(\pm u,\;\pm\frac{au}{kz_m(u)},\;z_m(u)\right),
\qquad z_m=z_-\ (m\text{ even}),\quad z_m=z_+\ (m\text{ odd}),
\]
with the two signs taken together. There is exactly one positive root in \(I_0\). Each \(I_m\) with \(m\geq1\) contributes zero, one or two positive roots as \(b<T_m\), \(b=T_m\), or \(b>T_m\), respectively. Thus the exact number of distinct equilibria is
\[
N(b)=3+2\sum_{m=1}^{\infty}\bigl(\mathbf 1_{\{b=T_m\}}+2\mathbf 1_{\{b>T_m\}}\bigr).
\]
The sum has finitely many nonzero terms for every finite \(b\). At \(b=T_m\), the two sign-related equilibria have nondegenerate quadratic folds in the equilibrium equation as functions of \(b\); their Jacobians have a zero eigenvalue. No general assertion about the other eigenvalues or nonlinear flow stability at a fold is made.

Let \(L_m=(m+1/2)\pi\) and \(D=d/(2c)\). The thresholds have the precise large-half-wave laws
\[
u_m=L_m-\frac{2}{L_m}+O(L_m^{-2}),\qquad
T_m=A L_m^2+(-1)^{m+1}D L_m+O(1).
\]
Consequently the *global* equilibrium census obeys the asymptotic law
\[
N(b)=\frac{4}{\pi\sqrt A}\sqrt b+O(1)
=\frac4\pi\left(\frac{ck}{ag}\right)^{1/4}\sqrt b+O(1)
\qquad(b\to\infty).
\]
In particular, the equilibrium count is unbounded as the sine forcing increases, but finite for every fixed amplitude.

At the originating publication's displayed parameters \((a,b,c,d,g,k)=(3/2,10,4,2,4,2)\), the theorem gives *exactly three* equilibria: the central one, and a sign-symmetric pair with \(u\approx2.59333620464930\), \(y\approx-0.96777520259\) at positive \(x\), and \(z\approx-2.00976647085\). The decimal values are illustrations, not the basis of the census.

## Assumptions and scope

All six parameters are strictly positive. The phase space is \(\mathbb R^3\); there is no artificial coordinate truncation, bounded-attractor restriction or assumed periodicity. The theorem classifies zeros of the vector field, not periodic trajectories, chaotic attractors, or the stability types away from the explicitly stated zero-eigenvalue folds. Threshold equality is included exactly. The asymptotic is taken with \(a,c,d,g,k\) fixed.

## Proof

**1. Algebraic reduction and reflection.** If an equilibrium has \(x=0\), the third equation forces \(z=d/c\) and the first then forces \(y=0\). If \(x\neq0\), the first equation forces \(z\neq0\) and \(y=ax/(kz)\). Substituting in the third gives
\[
cz^2-dz-Px^2=0,
\]
whose two roots are exactly \(z_\pm(|x|)\). The second equation gives \(z=-b\sin x/x\), so \(x\) cannot be a nonzero integer multiple of \(\pi\). For \(x>0\), positive sine requires \(z=z_-<0\), while negative sine requires \(z=z_+>0\). This is precisely the equation \(B_m(x)=b\) on \(I_m\). The vector field is equivariant under \((x,y,z)\mapsto(-x,-y,z)\), so every positive root produces exactly the stated sign pair and there are no further equilibria.

**2. Unique minimum on every later lobe.** Put \(N_-(u)=u(-z_-(u))\) and \(N_+(u)=u z_+(u)\). Direct differentiation, using \(s(u)^2=d^2+4cPu^2\), gives the exact elasticities
\[
\frac{uN_-'(u)}{N_-(u)}=2+\frac d{s(u)}=:E_-(u),\qquad
\frac{uN_+'(u)}{N_+(u)}=2-\frac d{s(u)}=:E_+(u).
\]
Thus \(E_-\in(2,3)\) decreases, \(E_+\in(1,2)\) increases, and on each half-wave
\[
\frac{uB_m'(u)}{B_m(u)}=E_m(u)-u\cot u.
\]
On \((0,\pi)\), \(u\cot u<1<E_-(u)\), so \(B_0'>0\). Moreover \(B_0(u)\sim (ag/(kd))u^2\) near zero and \(B_0(u)\to\infty\) as \(u\uparrow\pi\).

For \(u\geq\pi\), set \(H(u)=u\cot u\). On every open half-wave,
\[
H'(u)=\frac{\sin u\cos u-u}{\sin^2u}\leq\frac12-u.
\]
Since \(E_+'(u)>0\) and \(0<-E_-'(u)= (d/s(u))(1-d^2/s(u)^2)/u<1/u\), it follows that \(H-E_m\) is strictly decreasing on every \(I_m\) with \(m\geq1\): its derivative is at most \(1/2-u+1/u<0\). Meanwhile \(H\) decreases from \(+\infty\) to \(-\infty\) across each such interval. The equation \(H(u)=E_m(u)\) therefore has exactly one solution \(u_m\). It lies to the left of the midpoint because \(E_m>0\), whereas \(H\) vanishes at the midpoint. The derivative of \(\log B_m\) changes strictly from negative to positive at \(u_m\), and the derivative of \(H-E_m\) is nonzero there. Thus \(B_m''(u_m)>0\). Its endpoint limits are \(+\infty\) because \(N_\pm\) are positive and smooth away from zero. This proves every count, including threshold equality.

**3. Regularity and quadratic fold.** At a noncentral equilibrium, the Jacobian of the pair \((\dot x,\dot z)\) with respect to \((y,z)\) has determinant
\[
\det\begin{pmatrix}-kz&-ky\\gx&-c\end{pmatrix}=k(2cz-d)=\pm k s(|x|)\neq0.
\]
Consequently the other two equilibrium equations eliminate \((y,z)\) smoothly near each such point. The remaining scalar equation on a chosen positive half-wave is exactly \(\sin u\,(b-B_m(u))=0\). At \((u_m,T_m)\) its partial derivative with respect to \(u\) vanishes, its second \(u\)-derivative is \(-\sin(u_m)B_m''(u_m)\neq0\), and its derivative with respect to \(b\) is \(\sin(u_m)\neq0\). Hence these are genuine nondegenerate quadratic equilibrium folds and the full linearization is singular. Reflection gives the negative partner. This conclusion does not require assuming that the other two eigenvalues avoid the imaginary axis.

**4. Threshold and counting asymptotics.** The square-root expansion yields
\[
N_\pm(u)=A u^2\pm D u+O(1),\qquad
E_\pm(u)=2+O(u^{-1}).
\]
For \(L_m=(m+1/2)\pi\), write \(u_m=L_m+\delta_m\). The unique-minimum equation \(u_m\cot u_m=E_m(u_m)\) first shows \(\delta_m=O(L_m^{-1})\), using monotonicity and the boundedness of \(E_m\), and then expansion of \(\cot(L_m+\delta_m)=-\tan\delta_m\) gives \(\delta_m=-2/L_m+O(L_m^{-2})\). Since \(|\sin u_m|=1+O(L_m^{-2})\), substitution into \(B_m=N_m/|\sin u|\) gives \(T_m=A L_m^2+(-1)^{m+1}D L_m+O(1)\). In particular, \(T_m\to\infty\). The number of indices \(m\geq1\) with \(T_m<b\) is \((\pi\sqrt A)^{-1}\sqrt b+O(1)\). Indeed \(T_m=A\pi^2m^2+O(m)\), so all possibly undecided indices are within a bounded distance of \(\sqrt{b/A}/\pi\). Equality indices are likewise confined to that bounded window. Substitution in the exact census proves \(N(b)=4(\pi\sqrt A)^{-1}\sqrt b+O(1)\).

**5. Exact baseline census.** For \((a,c,d,g,k)=(3/2,4,2,4,2)\), \(A=\sqrt3/2>4/5\) and \(D=1/4\). The first positive sine lobe always gives one positive root. On any negative sine lobe with \(u\geq7/2\), the inequality \(N_+(u)\geq Au^2+Du>10\) rules out a root at \(b=10\). On \(\pi<u<7/2\), \(|\sin u|\leq u-\pi<1/2\) and \(N_+(u)>Au^2>(4/5)\cdot9=36/5\), hence \(B_m(u)>72/5>10\). For all positive sine lobes beyond the first, \(u\geq2\pi>6\) and \(N_-(u)\geq Au^2-Du>(4/5)\cdot36-(1/4)\cdot6>10\); the lower bound is increasing for \(u\geq6\). Therefore no other lobe contributes, and the total count is exactly three.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. Running `python3 verify.py` evaluates branch minima by bisection, checks the equilibrium equations for the source parameters, and checks representative lobe thresholds and higher-amplitude equilibrium counts. In the recorded run it reported `PASS: 260 finite consistency checks` and a positive equilibrium abscissa of approximately `2.59333620464930`. This script does not certify uniqueness on the continuum, the asymptotics, or the exact parameter boundaries; those follow from the proof above. No interval-arithmetic or independent formal proof certificate is claimed.

## Relationship to prior work

R. Ramar, *Design of a New Chaotic System with Sine Function: Dynamic Analysis and Offset Boosting Control* (2023), introduces precisely the vector field above in its equation (2), with the displayed baseline parameters, and studies numerically observed attractors, Lyapunov exponents and parameter dependence. Its equilibrium discussion treats the central point; it does not derive the half-wave minimum curves, the all-positive-parameter equilibrium census, the quadratic fold sequence, or its asymptotic growth law. Those conclusions are not obtained by applying its linearization at the central point. Sine-controlled multiscroll and hyperbolic-sine jerk systems studied elsewhere concern different vector fields; their equilibrium counts do not imply this system's branchwise formula. The underlying one-variable monotonicity and fold techniques are classical; the claimed contribution is their exact synthesis and global classification for this specific motivated flow.

## Limitations

The parameter space excludes zero and negative coefficients. No statement is made about bounded or unbounded trajectories, existence of attractors, topological entropy, or the nonlinear stability of fold points. A quadratic fold in the equilibrium *equation* is not automatically a dynamical saddle-node normal form with precisely one algebraically simple zero eigenvalue; that stronger statement is not asserted. Numerically displayed equilibria are illustrative only. Literature coverage is finite, and an equivalent treatment under different parameter names may exist.

## References

[1] R. Ramar (2023), *Design of a New Chaotic System with Sine Function: Dynamic Analysis and Offset Boosting Control*, **Chaos Theory and Applications** 5(2), 118–126. DOI: 10.51537/chaos.1223766. Primary full text: https://dergipark.org.tr/en/download/article-file/2850554. Earliest listed public posting: 2023-07-28.

[2] Q. Lai and collaborators (2017/2018), *A new chaotic system with multiple attractors: Dynamic analysis, circuit realization and S-box design*, **Entropy** 20, 12. The precursor flow quoted in [1] has different nonlinear terms and does not carry the specific sine-amplitude half-wave equations above.
