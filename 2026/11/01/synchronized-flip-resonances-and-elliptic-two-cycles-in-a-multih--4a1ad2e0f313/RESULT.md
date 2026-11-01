# Synchronized flip resonances and elliptic two-cycles in a multiharmonic kicked rotor

## Finding

Consider the area-preserving multiharmonic standard map of Cetin, Tirnakli and Boghosian. For every integer \(W\geq2\), the \(2W\) explicit zero-kick fixed points separate into three spectral classes with two **exact** flip parameters. The origin flips at \(K_0=8/[W(W+1)]\), while the other \(W-1\) initially elliptic points flip **simultaneously** at \(K_1=8/W\). Each flip produces one, and locally only one, primitive period-two orbit on the supercritical side; these newborn orbits are linearly elliptic. Their amplitudes and two-step traces have explicit asymptotics, including a first-order return-trace coefficient common to all \(W-1\) simultaneous resonances.

Precisely, write
\[
S_W(x)=\sum_{j=1}^{W}\sin(jx),\qquad
F_{W,K}(x,p)=(x+P,P)\pmod{2\pi},\quad P=p-KS_W(x).
\]
The distinguished fixed points are \((0,0)\), \((q_m,0)\), and \((r_n,0)\), where
\[
q_m=\frac{2\pi m}{W}\quad(1\le m\le W-1),\qquad
r_n=\frac{2\pi n}{W+1}\quad(1\le n\le W).
\]
They are all distinct. They are **all** fixed points whenever \(KW<2\pi\); for larger parameters no claim of exhaustiveness is made. The \(r_n\) are hyperbolic for every \(K>0\). The origin is linearly elliptic for \(0<K<K_0\) and hyperbolic for \(K>K_0\); every \(q_m\) is linearly elliptic for \(0<K<K_1\) and hyperbolic for \(K>K_1\). Equalities have trace \(-2\), so are nonhyperbolic.

For fixed \(W\), put \(\Delta=K-K_0\). As \(\Delta\downarrow0\), the new origin-centered two-cycle is
\[
( -h,-2h)\longleftrightarrow(h,2h),\quad
h=\sqrt{\frac32}\,\sqrt\Delta+O_W(\Delta^{3/2}),\quad
\operatorname{tr}(DF_{W,K}^2)=2-4W(W+1)\Delta+O_W(\Delta^2).
\]
For the \(m\)-th simultaneous transition, put \(\Delta=K-K_1\), \(\theta_m=\pi m/W\), and
\[
B_m=(2W+3)+3(2W+1)\cot^2\theta_m>0.
\]
The newborn orbit, in a common local lift, is
\[
(t_m-h_m,-2h_m)\longleftrightarrow(t_m+h_m,2h_m),
\]
with
\[
h_m=\sqrt{\frac{3}{2B_m}}\sqrt\Delta+O_{W,m}(\Delta^{3/2}),\quad
t_m=q_m-\frac W2\cot\theta_m\,h_m^2+O_{W,m}(h_m^4),
\]
and
\[
\operatorname{tr}(DF_{W,K}^2)=2-4W\Delta+O_{W,m}(\Delta^2).
\]
Thus each newborn orbit has return trace strictly between \(-2\) and \(2\) for sufficiently small \(\Delta>0\). For each stated fixed point there are no nontrivial two-cycles in a sufficiently small neighborhood on the subcritical side, and exactly one geometrically distinct small two-cycle on the supercritical side. The neighborhoods and size of the parameter interval may depend on \(W\) and \(m\).

As a concrete exact census, at \(W=50\), \(K=1/10\), the torus has exactly \(100\) fixed points: \(49\) linearly elliptic and \(51\) hyperbolic. This parameter is an illustration, not a claim about invariant islands or global ergodicity.

## Assumptions and scope

All positions and momenta lie on \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\). The parameter \(K\) is strictly positive and \(W\) is an integer at least two. The terms *elliptic* and *hyperbolic* refer only to linearized eigenvalues: a real determinant-one matrix with trace in \((-2,2)\) is elliptic, whereas trace outside \([-2,2]\) is hyperbolic. No KAM stability or positive-area island statement is inferred from ellipticity. The local period-two statements concern the canonical lift near the zero-momentum fixed point and hold as \(K\) approaches the indicated threshold at fixed \(W\). The parameter \(K\) is not assumed uniformly small as \(W\to\infty\).

## Proof

**1. Fixed-point census and slopes.** For \(0<x<2\pi\), the finite trigonometric identity is
\[
S_W(x)=\frac{\sin(Wx/2)\sin((W+1)x/2)}{\sin(x/2)}.
\]
Its zeros give the \(2W\) stated distinct positions, including the continuously extended root at the origin. A torus fixed point must satisfy \(P\equiv p\equiv0\pmod{2\pi}\), hence \(KS_W(x)\in2\pi\mathbb Z\). When \(KW<2\pi\), the elementary bound \(|S_W(x)|\le W\) forces \(S_W(x)=0\), proving exhaustiveness in that range. The slopes at the respective roots, obtained by differentiating the finite product or sum, are
\[
S'_W(0)=\frac{W(W+1)}2,\qquad S'_W(q_m)=\frac W2,
\qquad S'_W(r_n)=-\frac{W+1}{2}.
\]
The Jacobian is
\[
DF=\begin{pmatrix}1-KS'_W(x)&1\\-KS'_W(x)&1\end{pmatrix},\quad
\det DF=1,\quad\operatorname{tr}DF=2-KS'_W(x).
\]
The displayed spectral assertions and two flip thresholds follow immediately. At the threshold a Jacobian trace of \(-2\) is not called elliptic or hyperbolic.

**2. Exact reduction of any local two-cycle.** Let \(q\) be one of the positive-slope roots, and select a small neighborhood excluding modular-winding changes. If a primitive two-cycle has angular coordinates \(t-h\) and \(t+h\) with \(h>0\), then the angle update forces respective momenta \(-2h\) and \(2h\). The kick updates are equivalent to the two equations
\[
S_W(t+h)+S_W(t-h)=0,
\qquad\frac{S_W(t+h)-S_W(t-h)}{2h}=\frac4K.
\tag{1}
\]
Conversely, any small \(h>0\) and \(t\) solving (1) give the claimed cycle by direct substitution. Interchanging the two points changes the sign of \(h\), so \(h>0\) counts each orbit once.

**3. Local analytic branching.** Set
\[
a=S'_W(q)>0,\qquad b=S''_W(q),\qquad c=S'''_W(q),\quad
A=\frac c6-\frac{b^2}{2a}.
\]
By the analytic implicit-function theorem, the first equation in (1) has a unique even analytic solution \(t=t(h^2)\) near \((q,0)\), with
\[
t=q-\frac{b}{2a}h^2+O(h^4).
\]
Substitution into the second equation of (1) gives
\[
\frac4K=a+A h^2+O(h^4).
\tag{2}
\]
At the origin, \(a=W(W+1)/2\), \(b=0\), \(c=-a^2\), hence \(A=-a^2/6<0\). At \(q_m\), direct differentiation of the finite sine sum yields
\[
a=\frac W2,\quad b=\frac{W^2}{2}\cot\theta_m,\quad
c=-\frac{W^2}{4}\bigl(2W+3+3\cot^2\theta_m\bigr),
\]
so
\[
A=-\frac{W^2}{24}\bigl[(2W+3)+3(2W+1)\cot^2\theta_m\bigr]
=-\frac{W^2B_m}{24}<0.
\]
Writing \(K_c=4/a\) and \(\Delta=K-K_c\), (2) and the implicit-function theorem in \(h^2\) give
\[
h^2=-\frac{a^2}{4A}\Delta+O(\Delta^2).
\tag{3}
\]
The strict negativity of \(A\) proves that this analytic branch has \(h^2>0\) precisely for small positive \(\Delta\), establishing local existence and uniqueness on one side, and local absence on the other. Substituting the two explicit expressions for \(A\) yields the amplitude and center formulas in the finding.

**4. Return-trace expansion and ellipticity.** Define \(z_\pm=K S'_W(t\pm h)\). Multiplying the two derivative matrices gives the exact identity
\[
\operatorname{tr}(DF^2)=2-2(z_-+z_+)+z_-z_+.
\]
Using the center expansion and \(K=4/a-4Ah^2/a^2+O(h^4)\), this becomes
\[
\operatorname{tr}(DF^2)=2+\frac{32A}{a}h^2+O(h^4)
=2-8a\Delta+O(\Delta^2).
\tag{4}
\]
Since \(a>0\) and every return derivative has determinant one, sufficiently small \(\Delta>0\) gives strict linear ellipticity. For the origin, \(8a=4W(W+1)\); at every \(q_m\), \(8a=4W\), independent of \(m\).

**5. Exact illustrative count.** For \(W=50\) and \(K=1/10\), \(KW=5<2\pi\), so there are no nonzero-winding fixed points. The thresholds are \(K_0=8/(50\cdot51)\) and \(K_1=8/50\), and \(K_0<1/10<K_1\). The origin and all \(50\) negative-slope roots are hyperbolic; the remaining \(49\) roots are elliptic. This proves the asserted counts.

## Verification

The standalone program `verify.py`, run with Python 3 and the `sympy` and `mpmath` packages, performs exact symbolic checks of the coefficient cancellations and \(345\) algebraic/high-precision tests across \(W\in\{2,3,4,7,50\}\). The tests reconstruct local two-cycles by solving the **original** trigonometric equations, evaluate the full map twice, verify derivative formulas and the elliptic return traces. They are independent finite checks of algebra and numerical implementation, not proofs of the quantified infinite theorem. The proof above supplies the universal argument for all integer \(W\ge2\).

## Relationship to prior work

Cetin, Tirnakli and Boghosian (2022) introduce precisely the finite-sum kicked-rotor family, observe its \(W\)-well structure, and study phase portraits, Lyapunov color maps, and limit distributions. Their mathematical definitions and Results/Discussion sections do not state the simultaneous exact flip thresholds, the complete local two-cycle branching law, or the common first-order return-trace coefficient. The earlier \(z\)-generalized map of Tirnakli, Tsallis and Cetin (2019) replaces the kick by one harmonic \(\sin(zx)\); it is a different family and does not imply the multiple-root coefficient \(B_m\). General period-doubling normal-form theory anticipates local square-root branching under nondegeneracy, but does not supply these family-wide coefficients, root multiplicities, or synchronized return-trace law. The claimed contribution is this explicit structural specialization, not a new general bifurcation mechanism.

## Limitations

The result concerns fixed points and **local** primitive two-cycles near two flip parameters. It does not classify all periodic orbits, nonzero-winding fixed points for general \(K\), nonlinear stability, KAM islands, global chaos, or statistical mechanics. The asymptotic remainders are for fixed \(W\); they need not be uniform in \(W\). Linear ellipticity alone does not ensure nonlinear orbital stability. An unindexed earlier calculation or a specialized treatment of the same multiharmonic family might already contain these formulas, so publication-priority verification remains limited to the inspected material.

## References

1. K. Cetin, U. Tirnakli and B. M. Boghosian, “A generalization of the standard map and its statistical characterization,” *Scientific Reports* **12**, 8575 (published May 20, 2022), doi:10.1038/s41598-022-12213-5; https://www.nature.com/articles/s41598-022-12213-5.
2. U. Tirnakli, C. Tsallis and K. Cetin, “Dynamical robustness of discrete conservative systems: Harper and generalized standard maps,” arXiv:1910.12138 (first public October 26, 2019); https://arxiv.org/abs/1910.12138.
3. P. A. Glendinning and D. J. W. Simpson, “Normal Forms, Differentiable Conjugacies, and Elementary Bifurcations of Maps,” *SIAM Journal on Applied Mathematics* **83**, 816–836 (2023), doi:10.1137/22M1503701; https://epubs.siam.org/doi/abs/10.1137/22M1503701.
