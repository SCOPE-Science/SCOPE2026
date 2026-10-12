# Exact state-count positivity thresholds for classical RK4 on pure-birth chains
## Finding
Consider the unit-rate pure-birth continuous-time Markov chain on \(N\ge 2\) states, with the last state absorbing. In row-generator convention,
\[
Q_N=P_N-I,
\]
where \(P_N\) sends each nonabsorbing state to its successor and fixes the absorbing state. Apply one classical explicit fourth-order Runge--Kutta step of size \(x\ge0\) to the linear Kolmogorov equation. Its end-step matrix is
\[
R_4(xQ_N),\qquad
R_4(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}.
\]

Because \(Q_N\mathbf 1=0\), every row of \(R_4(xQ_N)\) sums to one. The matrix is entrywise nonnegative, and hence row-stochastic, exactly on
\[
0\le x\le X_N,
\]
where
\[
X_2=\rho_2,\qquad
X_3=\rho_3,\qquad
X_4=\frac43,\qquad
X_N=1\quad(N\ge5).
\]
Here \(\rho_2\) and \(\rho_3\) are the unique positive roots
\[
\rho_2^3-4\rho_2^2+12\rho_2-24=0,
\qquad
\rho_3^3-3\rho_3^2+6\rho_3-6=0,
\]
with
\[
\rho_2=2.7852935634052816\ldots,
\qquad
\rho_3=1.5960716379833215\ldots.
\]

For a common birth rate \(\lambda>0\) and physical timestep \(\Delta t\), replace \(x\) by \(\lambda\Delta t\). Thus the sharp end-step positivity bound is
\[
\lambda\Delta t\le X_N.
\]

The thresholds strictly decrease through the first five states and then stabilize at \(1\). In particular, five states are the first pure-birth dimension that realizes the radius \(1\) of absolute monotonicity of the RK4 stability polynomial. This statement concerns the final RK4 update matrix only; it does not assert positivity of the internal stages.

## Assumptions and scope
The generator is the homogeneous pure-birth chain with one absorbing endpoint and a common positive birth rate. The result is exact arithmetic and concerns entrywise nonnegativity of the one-step transition approximation \(R_4(\Delta t Q_N)\).

The chain is intentionally canonical: it is the directed path with an absorbing terminal state. No claim is made for arbitrary continuous-time Markov generators of the same dimension, nonuniform birth rates, nonlinear systems, floating-point arithmetic, or positivity of the internal RK4 stages.

For \(N=1\), \(Q_1=0\) and the end-step map is the identity for every timestep, so the nontrivial classification begins at \(N=2\).

## Proof
Write
\[
E_m(-x)=\sum_{\ell=0}^{m}\frac{(-x)^\ell}{\ell!}.
\]
Since \(Q_N=P_N-I\), binomial expansion of the degree-four stability polynomial gives
\[
R_4\!\left(x(P_N-I)\right)
=\sum_{j=0}^{4}a_j(x)P_N^j,
\qquad
a_j(x)=\frac{x^j}{j!}E_{4-j}(-x).
\]
Explicitly,
\[
a_0=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24},
\]
\[
a_1=x\left(1-x+\frac{x^2}{2}-\frac{x^3}{6}\right),
\]
\[
a_2=\frac{x^2}{4}\left(x^2-2x+2\right),
\qquad
a_3=\frac{x^3}{6}(1-x),
\qquad
a_4=\frac{x^4}{24}.
\]
The coefficient \(a_0\) is strictly positive for every \(x\ge0\), because
\[
24a_0=(x^2-2x)^2+8(x^2-3x+3)>0.
\]
Also \(a_2>0\) for \(x>0\), while the signs of \(a_1\) and \(a_3\) produce the relevant boundaries.

For two states, \(P_2^j=P_2\) for every \(j\ge1\). Hence the first row of the RK4 map is
\[
(a_0,1-a_0).
\]
Now
\[
a_0-1=\frac{x}{24}\left(x^3-4x^2+12x-24\right).
\]
The cubic
\[
g_2(x)=x^3-4x^2+12x-24
\]
has
\[
g_2'(x)=3x^2-8x+12>0
\]
for every real \(x\), so it has one real root \(\rho_2\). Since \(g_2(2)<0<g_2(3)\), that root lies in \((2,3)\), and \(1-a_0\ge0\) exactly for \(0\le x\le\rho_2\).

For three states, the first two nontrivial rows are
\[
(a_0,a_1,a_2+a_3+a_4),
\qquad
(0,a_0,1-a_0).
\]
The remaining tail satisfies
\[
a_2+a_3+a_4
=
\frac{x^2}{24}\left(3x^2-8x+12\right)>0.
\]
Moreover,
\[
a_1=-\frac{x}{6}\left(x^3-3x^2+6x-6\right).
\]
The cubic
\[
g_3(x)=x^3-3x^2+6x-6
\]
has
\[
g_3'(x)=3\bigl((x-1)^2+1\bigr)>0,
\]
so its unique real root is \(\rho_3\). Since \(g_3(4/3)=-26/27<0\) and \(g_3(2)=2>0\),
\[
\frac43<\rho_3<2<\rho_2.
\]
Therefore the three-state map is nonnegative exactly for \(0\le x\le\rho_3\).

For four states, the first row is
\[
(a_0,a_1,a_2,a_3+a_4),
\]
and
\[
a_3+a_4=\frac{x^3}{24}(4-3x).
\]
All earlier entries are nonnegative for \(0\le x\le4/3\), because \(4/3<\rho_3<\rho_2\). The absorbing entry becomes negative immediately for \(x>4/3\). Thus \(X_4=4/3\).

Finally suppose \(N\ge5\). For \(0\le x\le1\), each coefficient \(a_j(x)\) is nonnegative, so
\[
R_4(xQ_N)=\sum_{j=0}^4 a_j(x)P_N^j
\]
is a convex combination of row-stochastic matrices and is therefore row-stochastic. For \(x>1\), the first-row entry leading to state \(4\) in one-based indexing, namely the state reached after exactly three births, equals
\[
a_3=\frac{x^3}{6}(1-x)<0,
\]
because \(P_N^0,P_N^1,P_N^2,P_N^3,P_N^4\) reach distinct states from the first state when \(N\ge5\). Hence \(X_N=1\) for every \(N\ge5\).

For comparison with general linear positivity theory, the stability polynomial itself has radius of absolute monotonicity exactly \(1\). Indeed,
\[
R_4'''(z)=1+z,
\]
so the radius cannot exceed \(1\), while at \(z=-1\) the values of \(R_4\) and all its derivatives through order four are nonnegative. Thus the five-state pure-birth chain is the first member of this family whose sharp end-step positivity threshold equals that general stability-polynomial radius.

## Verification
The companion script `verify.py` uses exact rational arithmetic. It reconstructs the pure-birth successor matrices, forms both \(R_4(x(P-I))\) and the coefficient expansion \(\sum_{j=0}^4a_jP^j\), and checks their equality at several rational values and dimensions.

It also checks exact boundary and failure witnesses:
\[
N=4,\quad x=\frac32:
\qquad
\bigl(R_4(xQ_4)\bigr)_{1,4}=-\frac9{128},
\]
and
\[
N=5,\quad x=\frac65:
\qquad
\bigl(R_4(xQ_5)\bigr)_{1,4}=-\frac{36}{625}.
\]
The infinite classification itself does not rely on finite experiments; it follows from the coefficient identities and monotonicity of the two cubic boundary polynomials.

## Relationship to prior work
Horváth develops sharp positivity-step-size theory for Runge--Kutta methods on broad classes of positive initial-value problems and, in a later section, larger invariant cones for special linear problems. That theory is deliberately worst-case over problem classes or tied to eigenvector cones; it does not state the exact all-positive-vector threshold of the fixed homogeneous pure-birth generator as a function of state count.

Classical absolute-monotonicity theory relates the stability function of a Runge--Kutta method to preservation of positivity and contractivity for linear problems. Lóczi and Ketcheson give this connection explicitly and classify their work primarily under MSC 65L06. Their framework treats the radius of absolute monotonicity of stability functions; it does not state the finite-state pure-birth thresholds above.

Bylina and Potiopa apply the standard fourth-order explicit Runge--Kutta method directly to continuous-time Markov-chain transient probability equations. Their open-access article writes the Kolmogorov system and the classical RK4 stages explicitly, but it does not give a timestep condition guaranteeing that the final update remains a probability vector.

A closely related published finding studies the same pure-birth geometry for the fourth-order \([2/2]\) Padé map. That rational method has an eight-state small-step positivity barrier and a disconnected stochasticity window. The present polynomial RK4 result is different: its positivity interval is connected, its sharp boundary depends on state count only through \(N=2,3,4,\ge5\), and dimension five already realizes the stability-polynomial absolute-monotonicity radius.

Shao, Gao, and Xue study truncated Taylor approximations for exponentials of essentially nonnegative matrices using shifting, scaling, and squaring to obtain componentwise accuracy. That construction is not the unshifted single RK4 end-step map considered here.

## Limitations
The theorem is specific to homogeneous pure-birth chains. It does not classify arbitrary Markov generators, birth--death chains, or generators with nonuniform rates.

The thresholds concern only entrywise nonnegativity of the final linear RK4 update. Classical RK4 has internal stages that need not be nonnegative under the larger small-state thresholds.

The result does not compare accuracy at the positivity boundary, recommend operating near that boundary, or claim superiority over uniformization, exponential-action methods, SSP methods, or positivity-preserving matrix-exponential algorithms.

The literature comparison found no implication-equivalent finite-state threshold table, but older Markov-chain numerics or absolute-monotonicity literature could contain the same specialization under different terminology.

## References
1. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* 53 (2005), 341–356. Available online 27 October 2004. DOI: 10.1016/j.apnum.2004.08.026.
2. B. Bylina and J. Potiopa, “Explicit Fourth-Order Runge–Kutta Method on Intel Xeon Phi Coprocessor,” *International Journal of Parallel Programming* 45 (2017), 1073–1090. Published online 29 September 2016. DOI: 10.1007/s10766-016-0458-x.
3. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” arXiv:1303.6651, first submitted 26 March 2013; later *LMS Journal of Computation and Mathematics* 17 (2014), 159–205.
4. M. Shao, W. Gao, and J. Xue, “Aggressively Truncated Taylor Series Method for Accurate Computation of Exponentials of Essentially Nonnegative Matrices,” *SIAM Journal on Matrix Analysis and Applications* 35 (2014), 317–338. DOI: 10.1137/120894294.
5. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” published finding identifier 2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
