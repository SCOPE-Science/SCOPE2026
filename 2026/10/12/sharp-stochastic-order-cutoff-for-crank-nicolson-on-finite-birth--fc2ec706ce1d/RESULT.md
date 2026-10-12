# Sharp stochastic-order cutoff for Crank–Nicolson on finite birth–death chains

## Finding
Fix an integer \(n\ge2\), and let \(Q\) be the generator of an irreducible birth–death chain on the totally ordered states \(\{0,1,\ldots,n-1\}\). The birth and death rates are strictly positive whenever a neighboring edge exists:
\[
(Qf)_i=\lambda_i(f_{i+1}-f_i)+\mu_i(f_{i-1}-f_i),
\]
with \(\lambda_{n-1}=\mu_0=0\). Let the Crank–Nicolson end-step operator be
\[
T_h=(I-hQ/2)^{-1}(I+hQ/2),\qquad h\ge0.
\]
A linear operator \(T\) is said to **preserve the increasing-function cone** if every function satisfying \(f_0\le f_1\le\cdots\le f_{n-1}\) is sent to another such function. This property is separate from the requirement that \(T\) be entrywise nonnegative.

Introduce the forward difference \((Df)_i=f_{i+1}-f_i\), and the edge generator
\[
H_{ii}=-(\lambda_i+\mu_{i+1}),\quad H_{i,i+1}=\lambda_{i+1},\quad H_{i,i-1}=\mu_i
\]
for \(0\le i\le n-2\), omitting nonexistent neighbors. Let
\[
R_h=(I-hH/2)^{-1}.
\]
Every diagonal return entry \((R_h)_{ii}\) crosses \(1/2\) at a unique positive time \(h_i\). The **sharp order-preservation step limit** is
\[
\boxed{h_{\mathrm{ord}}=\min_{i=0}^{n-2} h_i,\qquad (R_{h_i})_{ii}=\frac12.}
\]
The operator \(T_h\) preserves every nondecreasing test function **if and only if**
\[
\boxed{0\le h\le h_{\mathrm{ord}}.}
\]
The result holds for all positive birth and death rates, including nonuniform and asymmetric rates. This is an exact spectral-resolvent threshold, not merely a sufficient CFL bound.

For three states, write
\[
a=\lambda_0+\mu_1,\quad d=\lambda_1+\mu_2,\quad b=\lambda_1,\quad c=\mu_1.
\]
Then
\[
\boxed{h_{\mathrm{ord}}=\frac4{|a-d|+\sqrt{(a+d)^2-4bc}}.}
\]
The appearance of the **edge-generator spectrum** rather than just the holding rates is essential.

There are explicit, contrasting three-state regimes.

For the symmetric walk
\[
Q_1=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},
\]
Crank–Nicolson is a valid nonnegative stochastic matrix through \(h=2\) but preserves increasing functions only through \(h=2/\sqrt3\). For example at \(h=3/2\),
\[
T_{3/2}=\begin{pmatrix}31/91&6/13&18/91\\6/13&1/13&6/13\\18/91&6/13&31/91\end{pmatrix}
\]
is strictly positive and stochastic; nevertheless
\[
T_{3/2}(0,1,1)^{\mathsf T}=(60,49,73)^{\mathsf T}/91
\]
is not nondecreasing.

Conversely, for
\[
Q_2=\begin{pmatrix}-1&1&0\\3&-6&3\\0&1&-1\end{pmatrix},
\]
the order cone is preserved for \(h\le2/\sqrt7\), but entrywise nonnegativity holds only for \(h\le2/5\). At \(h=1/2\),
\[
T_{1/2}=\begin{pmatrix}39/55&2/11&6/55\\6/11&-1/11&6/11\\6/55&2/11&39/55\end{pmatrix}
\]
has a negative diagonal entry despite preserving the increasing-function cone.

Thus preservation of probability and preservation of stochastic ordering are **logically different requirements** even in the smallest irreducible birth–death system where they can separate.

## Assumptions and scope
All matrices and inequalities are over the reals and in exact arithmetic. The state space is finite and linearly ordered, with strictly positive birth and death rates on existing edges. The time step is nonnegative. \(Q\) acts on column test-function values and has zero row sums.

A **valid Markov transition matrix** has nonnegative entries and every row sum equal to one. A valid transition is **stochastically monotone** precisely if it also maps increasing test functions to increasing test functions. The theorem first classifies the latter cone property without assuming nonnegative entries; only their intersection has the probabilistic meaning of stochastic monotonicity.

Crank–Nicolson has exact row-sum conservation for all \(h\ge0\), but may lose nonnegative entries and may independently lose the increasing-function property.

## Proof
Let \(D\) be the \((n-1)\times n\) matrix with row \(i\) containing \(-1\) at column \(i\) and \(1\) at column \(i+1\). Direct subtraction yields, for every \(f\),
\[
\begin{aligned}
(DQf)_i&=(Qf)_{i+1}-(Qf)_i\\
&=\mu_i(Df)_{i-1}-(\lambda_i+\mu_{i+1})(Df)_i
   +\lambda_{i+1}(Df)_{i+1},
\end{aligned}
\]
where missing terms are omitted. Hence
\[
DQ=HD.
\]
The matrix \(D\) is surjective onto \(\mathbb R^{n-1}\), and its kernel consists exactly of constants. Thus \(H\) is the operator induced by \(Q\) on the quotient by constants. Since an irreducible finite birth–death generator is reversible, its eigenvalues are real, with a simple zero and all other eigenvalues strictly negative. Therefore every eigenvalue of \(H\) is real and strictly negative.

The matrix \(H\) has strictly positive neighbor off-diagonal entries, so it is an irreducible tridiagonal Metzler matrix. It is diagonally similar to a symmetric strictly negative-definite matrix: choose a positive diagonal similarity by balancing the positive neighbor products. For \(h\ge0\), the resolvent
\[
R_h=(I-hH/2)^{-1}
\]
exists. By the Laplace integral
\[
R_h=\int_0^\infty e^{-t}e^{(ht/2)H}\,dt,
\]
all its entries are nonnegative, and when \(h>0\), every entry is strictly positive (because \(H\) is irreducible Metzler).

The diagonal similarity does not change diagonal resolvent entries. If \(S\) is the symmetric negative definite representative and \(-S\) has strictly positive eigenvalues \(\nu_j\), the symmetric spectral theorem gives for each edge \(i\)
\[
(R_h)_{ii}=\sum_{j=1}^{n-1}\frac{u_{ij}^2}{1+h\nu_j/2},\qquad \sum_j u_{ij}^2=1.
\]
Each term is continuous and strictly decreasing wherever its weight is nonzero. Thus every diagonal entry is strictly decreasing from one to zero. There is exactly one positive solution \(h_i\) to \((R_{h_i})_{ii}=1/2\).

From \(DQ=HD\), the rational-function identities follow:
\[
D(I-hQ/2)^{-1}=(I-hH/2)^{-1}D,
\]
and consequently
\[
DT_h=(2R_h-I)D.
\]
A vector \(f\) is nondecreasing exactly when \(Df\ge0\) componentwise. Because \(D\) is onto, preservation of every increasing \(f\) is equivalent to
\[
2R_h-I\ge0
\]
entrywise. All off-diagonal entries are nonnegative, so this reduces exactly to \((R_h)_{ii}\ge1/2\) for every edge. Strict diagonal decrease proves that the admissible step set is the closed interval \([0,\min_i h_i]\), and that every larger time step fails.

For three states, \(H\) has the form
\[
H=\begin{pmatrix}-a&b\\c&-d\end{pmatrix},\quad \Delta=ad-bc>0.
\]
The resolvent is
\[
R_h=\frac1{1+h(a+d)/2+h^2\Delta/4}
\begin{pmatrix}1+hd/2&hb/2\\hc/2&1+ha/2\end{pmatrix}.
\]
Its two diagonal half-crossings occur respectively at
\[
\frac{d-a+\sqrt{(a-d)^2+4\Delta}}{\Delta}
\quad\text{and}\quad
\frac{a-d+\sqrt{(a-d)^2+4\Delta}}{\Delta}.
\]
Their minimum, after rationalization, is
\[
\frac4{\sqrt{(a-d)^2+4\Delta}+|a-d|}
=\frac4{\sqrt{(a+d)^2-4bc}+|a-d|},
\]
which is the stated formula.

In the first example the edge matrix is
\[
H_1=\begin{pmatrix}-2&1\\1&-2\end{pmatrix};
\]
hence \(h_{\mathrm{ord}}=2/\sqrt3\). Direct inversion gives the transition entries
\[
T_h=\begin{pmatrix}
\frac{-h^2+4h+4}{3h^2+8h+4}&\frac{2h}{3h+2}&\frac{2h^2}{3h^2+8h+4}\\
\frac{2h}{3h+2}&\frac{2-h}{3h+2}&\frac{2h}{3h+2}\\
\frac{2h^2}{3h^2+8h+4}&\frac{2h}{3h+2}&\frac{-h^2+4h+4}{3h^2+8h+4}
\end{pmatrix}.
\]
All entries are nonnegative exactly for \(h\le2\), because the middle diagonal first becomes negative at two (the endpoint diagonals do not cross zero until \(2+2\sqrt2\)). At \(h=3/2\), the explicit rational witness above proves the order failure while probability nonnegativity still holds.

For the second example, \(H_2=\bigl(\begin{smallmatrix}-4&3\\3&-4\end{smallmatrix}\bigr)\), hence \(h_{\mathrm{ord}}=2/\sqrt7\). Direct inversion yields the middle diagonal of the full transition as \((2-5h)/(2+7h)\), while the other entries remain nonnegative through \(h=2/5\). Thus \(h_{\mathrm{pos}}=2/5\), strictly smaller than \(h_{\mathrm{ord}}\). At \(h=1/2\), the edge propagation matrix is
\[
2R_{1/2}-I=\frac1{55}\begin{pmatrix}9&24\\24&9\end{pmatrix}\ge0
\]
even though the full transition has a negative central diagonal.

## Verification
The standalone `verify.py` uses exact rational arithmetic and symbolic inversion to check \(DQ=HD\), both rational witness matrices, probability row sums, and the edge-cone intertwining in both examples. It checks the strict positive-versus-ordering separation in the first example and the opposite separation in the second. A four-state nonuniform rational-rate chain also tests the general index pattern in \(DQ=HD\).

These finite checks corroborate the algebra; the all-state theorem, diagonal resolvent monotonicity, and exact cutoff are proved analytically above.

## Relationship to prior work
The gradient intertwining of birth–death semigroups is an established concept. Chafaï and Joulin develop discrete-gradient intertwinings with Feynman–Kac semigroups and study stochastic orderings; their full paper directly motivates the edge-generator reduction. The identity \(DQ=HD\) is not claimed novel here.

Likewise, the diagonal-resolvent criterion for entrywise nonnegativity of Crank–Nicolson is a known algebraic consequence of \(T_h=2(I-hQ/2)^{-1}-I\). That **probability-positivity** fact is not the new claim. The new result is the complete sharp **stochastic-order-cone** cutoff governed by the different edge resolvent \((I-hH/2)^{-1}\), its explicit three-state rate formula, and the two exact examples proving that probability positivity and order-cone positivity need not have the same cutoff and neither implication holds unconditionally.

Dai Pra, Louis, and Minelli investigate stochastic versus realizable monotonicity for continuous-time Markov processes on finite posets. They provide the operator-order framework but do not give a Crank–Nicolson step-size classification in the inspected material. Higueras studies strong stability and monotonicity of additive Runge–Kutta methods through absolute-monotonicity regions, and Gottlieb, Grant, and Higgs examine related SSP step-size properties. Those time-discretization results do not resolve the present finite birth–death transition-versus-order-cone question.

## Limitations
The result requires nearest-neighbor finite birth–death structure. General finite Markov chains on partially ordered or unordered state spaces do not share this simple surjective adjacent-difference representation.

The sharp rate formula applies only to three states. For arbitrary size the result provides a well-posed, exactly characterized scalar root per edge, not a universal elementary closed form.

Order-cone preservation of a matrix containing negative entries has no standalone Markov-transition interpretation; such an operator is not a legitimate stochastic matrix. Actual stochastic monotonicity requires intersecting the order cutoff with the separately established entrywise-positivity cutoff.

The theorem is exact arithmetic and does not address floating-point rounding at an equality threshold. It does not assert strong stability for general nonlinear ODEs or arbitrary Runge–Kutta methods.

## References
1. I. Higueras, “Strong Stability for Additive Runge–Kutta Methods,” SIAM Journal on Numerical Analysis 44 (2006), 1735–1758, DOI 10.1137/040612968; online 2006-09-26.
2. D. Chafaï and A. Joulin, “Intertwining and commutation relations for birth–death processes,” Bernoulli 19 (2013), 1855–1879, DOI 10.3150/12-BEJ433; arXiv:1011.2331.
3. P. Dai Pra, P.-Y. Louis, and I. G. Minelli, “Realizable monotonicity for continuous-time Markov processes,” Stochastic Processes and their Applications 120 (2010), 959–982, DOI 10.1016/j.spa.2010.03.002; lawful postprint arXiv:1603.02223.
4. S. Gottlieb, Z. Grant, and D. Higgs, “Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and Optimal Nonlinear Order,” arXiv:1403.6519v1, 2014.
