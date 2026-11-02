# A fastest-exit positivity frontier for Crank–Nicolson on directed cycles

## Finding
Let \(n\ge3\) and \(r_0,\ldots,r_{n-1}>0\). On the one-way directed cycle with indices modulo \(n\), let the row generator \(Q\) have \(Q_{i,i+1}=r_i\), \(Q_{ii}=-r_i\), and all other entries zero. Put
\[
C(h)=(I-hQ/2)^{-1}(I+hQ/2),\qquad h\ge0.
\]
Define \(r_*=\max_i r_i\) and, for a choice of \(i_*\) with \(r_{i_*}=r_*\), define the degree-at-most-\(n-1\) polynomial
\[
F(t)=(1-tr_*)\prod_{j\ne i_*}(1+tr_j)+t^n\prod_{j=0}^{n-1}r_j.
\]
Although written with two degree-\(n\) terms, their leading coefficients cancel. There is exactly one positive root \(t_*\) of \(F\), and **the exact global end-step positivity condition** is
\[
C(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le 2t_*.
\]
Every off-diagonal entry of \(C(h)\) is positive when \(h>0\). At \(h=2t_*\), its zero diagonal entries are exactly the vertices with maximum departure rate \(r_*\). Thus the first positivity obstruction, for *all* heterogeneous positive rates, depends on which vertices have the largest departure rate; the cyclic arrangement of the remaining rates does not affect the threshold.

Moreover, for **every** vertex, the diagonal backward-Euler return probability \(\bigl[(I-tQ)^{-1}\bigr]_{ii}\) is strictly decreasing in \(t>0\), despite this generator being nonreversible for \(n\ge3\).

In the uniform-rate case \(r_i=r>0\), let \(x_n=rt_*\). Then \(x_n>1\) is the unique solution of
\[
x_n-1=\frac{x_n^n}{(1+x_n)^{n-1}},
\]
the sequence \(x_n\) decreases strictly with \(n\), and
\[
x_3=\frac{1+\sqrt5}{2},\qquad
\lim_{n\to\infty}2^{n-1}(x_n-1)=1.
\]
In particular the uniform-rate sharp timestep \(2x_n/r\) approaches \(2/r\) with an explicit exponentially small correction.

## Assumptions and scope
There are at least three vertices, every clockwise rate is strictly positive, and the generator acts on column-valued observables through \(Q\). With row-distribution convention the equivalent probability update is right multiplication by the stochastic matrix \(C(h)\); the two rational factors commute. The claim concerns positivity of the *completed* Crank–Nicolson step, not intermediate-stage positivity, positivity of a nonlinear integrator, or contractivity of arbitrary observables. Negative entries at steps beyond the threshold preclude positivity preservation for every nonnegative initial vector.

## Proof
Set \(t=h/2\), \(z_j=tr_j/(1+tr_j)\), \(y_j=1-z_j\), and \(B=\prod_jz_j\). Since the matrix \(I-tQ\) has diagonal \(1+tr_j\) and directed successor entries \(-tr_j\), a weighted geometric-series expansion over successive circuits gives the **exact diagonal resolvent**
\[
R_{ii}(t):=\bigl[(I-tQ)^{-1}\bigr]_{ii}
=\frac{y_i}{1-B}
=\frac{\prod_{j\ne i}(1+tr_j)}{\prod_j(1+tr_j)-t^n\prod_jr_j}.
\]
For \(t>0\), \(I-tQ\) is an irreducible nonsingular \(M\)-matrix, so its inverse has strictly positive entries. The Cayley identity gives \(C(2t)=2R(t)-I\), hence only the diagonal entries can violate nonnegativity.

For a fixed \(t>0\), the denominator \(1-B\) is common to all vertices, whereas \(y_i=(1+tr_i)^{-1}\) strictly decreases with \(r_i\). Therefore \(\min_i R_{ii}(t)\) is achieved exactly at the maximum-rate vertices.

The temporal monotonicity is *not* inferred from reversibility. Differentiate the preceding exact expression:
\[
t\frac{d}{dt}\log R_{ii}(t)
=-z_i+\frac{B}{1-B}\sum_j(1-z_j).
\]
Writing \(U=\prod_{j\ne i}z_j\), the right side is strictly negative exactly when
\[
U\left(1+\sum_{j\ne i}(1-z_j)\right)<1.
\]
Indeed, with \(S=\sum_{j\ne i}(1-z_j)>0\),
\[
U=\prod_{j\ne i}\bigl(1-(1-z_j)\bigr)
\le e^{-S}<\frac1{1+S}.
\]
Thus every \(R_{ii}(t)\) is strictly decreasing for \(t>0\). At zero it equals one; as \(t\to\infty\) it tends to the stationary mass
\[
\pi_i=\frac{r_i^{-1}}{\sum_jr_j^{-1}}.
\]
For a maximum-rate state, \(\pi_{i_*}\le1/n<1/2\). Its return resolvent therefore crosses \(1/2\) exactly once, at \(t_*\). The explicit diagonal formula shows that the crossing equation \(2R_{i_*i_*}(t_*)=1\) is exactly \(F(t_*)=0\). No other vertex can cross first; at equality only the maximum-rate states have zero Cayley diagonal. This proves the global criterion, the positive-root uniqueness, and the sharp boundary.

If all rates equal \(r\), write \(x=rt\) and \(q=x/(1+x)\). The diagonal resolvent is \(1/[(1+x)(1-q^n)]\). Its level-\(1/2\) equation is the displayed equation for \(x_n\). At fixed \(x>0\), this diagonal return resolvent strictly decreases as \(n\) increases, hence its unique threshold \(x_n\) strictly decreases. The equation has \(x_n>1\); for fixed \(x>1\), its left resolvent limit as \(n\to\infty\) is \(1/(1+x)<1/2\), so \(x_n\downarrow1\).

From \(1<x_n\le x_3\), the identity \(x_n-1=(1+x_n)(x_n/(1+x_n))^n\) yields an exponential bound \(x_n-1\le(1+x_3)(x_3/(1+x_3))^n\), hence \(n(x_n-1)\to0\). Finally
\[
2^{n-1}(x_n-1)=x_n^n\left(\frac2{1+x_n}\right)^{n-1}\longrightarrow1.
\]
For \(n=3\) the root equation reduces to \(x^2-x-1=0\), giving the exact golden-ratio value.

## Verification
Run \(\texttt{python3 verification.py}\) with Python 3 and no third-party packages. The checker directly inverts \(I-tQ\) using exact rational arithmetic for 6,020 instances across directed cycles with 3 through 8 vertices, checks the return-resolvent factorization, strict positivity of off-diagonals, row sums, the maximum-rate bottleneck, and the polynomial sign criterion. A 90-decimal-digit bracket computation verifies 48 uniform-rate threshold roots and their finite-size trends. Expected output starts with \(\texttt{PASS rational_cycle_step_cases 6020}\). The all-rate, all-size theorem follows from the displayed analytic proof, not from the finite checks.

For example, with three rates \((1,2,4)\), the controlling polynomial is \(1-t-10t^2\), so the exact sharp step is \(h_*=(\sqrt{41}-1)/10\). For three unit rates it is \(h_*=1+\sqrt5\).

## Relationship to prior work
Classical strong-stability-preserving work by Gottlieb, Shu, and Tadmor motivates distinguishing scalar stability from positivity of a completed numerical timestep. Higueras and Roldán study sharp Crank–Nicolson positivity thresholds for *undirected one-dimensional Dirichlet heat discretizations*, a different family.

A previously published resolvent-return theorem establishes the general Cayley identity, its diagonal-positivity test for finite Markov generators, and a single-crossing theorem under **reversibility**. Those algebraic identities are used here as prior work, not claimed as new. The present claim proves the all-rate unique crossing *without reversibility*, identifies the exact maximum-departure-rate obstruction for inhomogeneous directed cycles, gives its polynomial threshold, and determines an exponential uniform-cycle finite-size correction. The cited general reversible-chain theorem explicitly does not classify such nonreversible positivity windows.

## Limitations
No corresponding single-crossing law is asserted for arbitrary nonreversible finite-state generators, other directed graphs, or generators with reverse-direction edges. The polynomial is an exact implicit characterization; for general heterogeneous rates it need not admit a radical expression. The sharp step guarantees matrix nonnegativity in exact arithmetic, and roundoff can affect the zero entries at equality. Specialized historical literature under transport-cycle or matrix-Cayley terminology could still contain an equivalent result; independent audit has not been performed.

## References
1. S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112. DOI: 10.1137/S003614450036757X. Author full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf (first published electronically 2001-02-02).
2. I. Higueras and T. Roldán, *A New Insight on Positivity and Contractivity of the Crank–Nicolson Scheme for the Heat Equation*, arXiv:2301.01066 (2023), https://arxiv.org/pdf/2301.01066.
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
