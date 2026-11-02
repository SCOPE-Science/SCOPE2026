# Sharp positivity horizon and homogenization extremum for weighted-star Crank–Nicolson steps

## Finding
For a connected weighted star with \(m\ge2\) leaves, the Crank–Nicolson update is a nonnegative stochastic matrix **if and only if** its step size \(h\) lies in \([0,2t_*]\), where \(t_*\) is the unique positive solution of
\[
\sum_{i=1}^m\frac{t_*w_i}{1+t_*w_i}=1.
\]
The hub loses diagonal positivity first, independently of the conductance asymmetry. Under fixed total spoke conductance \(W=\sum_i w_i\), uniform weights uniquely minimize this sharp allowable step:
\[
\min_{w_i>0,\,\sum w_i=W} h_*(w)=\frac{2m}{(m-1)W},
\]
with equality precisely when \(w_1=\cdots=w_m=W/m\). The supremum of \(h_*(w)\) under this total-conductance constraint is infinite.

## Assumptions and scope
A weighted star has vertices \(0,1,\dots,m\), hub \(0\), and only edges \(\{0,i\}\) of conductance \(w_i>0\). Its symmetric Laplacian is \(L_{00}=\sum_iw_i\), \(L_{ii}=w_i\), and \(L_{0i}=L_{i0}=-w_i\). At every \(h\ge0\), set \(t=h/2\) and \(C(h)=(I+tL)^{-1}(I-tL)\). Entrywise nonnegative includes zero entries at the boundary. No claim is made for negative conductances, nonstar graphs, or other time integrators.

## Proof
Let \(R(t)=(I+tL)^{-1}\), \(x_i=tw_i/(1+tw_i)\), and \(f(t)=\sum_i x_i\). The lower-right leaf block of \(I+tL\) is diagonal with entries \(1+tw_i\); its Schur complement at the hub is \(1+f(t)\). Hence
\[
R_{00}(t)=\frac1{1+f(t)},\qquad
R_{0i}(t)=\frac{x_i}{1+f(t)},
\]
and, for \(i\ne j\) with \(i,j\ge1\),
\[
R_{ij}(t)=\frac{x_ix_j}{1+f(t)}.
\]
The diagonal leaf entries obey
\[
R_{ii}(t)=\frac1{1+tw_i}+\frac{x_i^2}{1+f(t)},\qquad
R_{ii}(t)-R_{00}(t)=\frac{\sum_{j\ne i} x_j}{(1+tw_i)(1+f(t))}>0
\]
for \(t>0\) and \(m\ge2\). The identity \(C=2R-I\) shows that all off-diagonal entries are strictly positive for \(t>0\), and every diagonal is nonnegative exactly while the hub diagonal \(2/(1+f(t))-1\) is nonnegative. Since every summand of \(f\) strictly increases from \(0\) to \(1\), the equation \(f(t_*)=1\) has one and only one positive solution. At that root the hub diagonal vanishes, all leaf diagonals are strictly positive, and all off-diagonals are positive.

For fixed \(W\) and fixed \(t>0\), the function \(s\mapsto ts/(1+ts)\) is strictly concave on \((0,\infty)\). Jensen's inequality gives
\[
f(t)\le m\frac{tW/m}{1+tW/m},
\]
with equality only for uniform conductances. The right-hand side equals \(1\) at \(t_0=m/[(m-1)W]\). Strict increase of \(f\) yields \(t_*\ge t_0\), equality if and only if the conductances are uniform. This proves the sharp fixed-budget minimization.

For unboundedness, take \(w_1=W-(m-1)\varepsilon\) and \(w_2=\cdots=w_m=\varepsilon\), where \(0<\varepsilon<W/m\). Writing \(a=w_1\) and clearing denominators in \(a t/(1+at)+(m-1)\varepsilon t/(1+\varepsilon t)=1\) gives
\[
(m-1)a\varepsilon t^2+(m-2)\varepsilon t-1=0.
\]
The unique positive root satisfies \(t_*\sim[(m-1)W\varepsilon]^{-1/2}\), proving that \(h_*=2t_*\) is unbounded as \(\varepsilon\downarrow0\). In particular, for \(m=2\), \(t_*=(w_1w_2)^{-1/2}\).

## Verification
The supplied standalone Python script verifies the exact Schur-complement identities with three rational-weight stars, and checks 525 seeded random weighted stars, totaling 3,150 complete-matrix sign and stochasticity comparisons at timesteps below, at, and above the analytically determined boundary. Finite numerical tests are corroboration only; the proof above establishes the result for all admissible real weights and all \(m\ge2\).

## Relationship to prior work
Crank and Nicolson introduced the underlying time-stepping scheme in 1947. The general connection between Markov resolvent diagonal entries and Crank–Nicolson positivity is known, including a sharp threshold statement for reversible chains, and is not claimed as new. Higueras and Roldán analyze positivity and contractivity for one-dimensional Dirichlet heat meshes (2023), not this weighted-star classification. The added structural conclusions are a single hub-controlled scalar root for arbitrary positive spoke conductances, the exact extremal weighting at fixed total conductance, and the singular blow-up law for highly imbalanced stars.

## Limitations
The theorem concerns entrywise positivity of a single Markov-chain update, not stability or global discretization error. The homogeneous minimum is strict only for fixed \(m\ge2\) and positive conductances; unbounded horizon is a supremum approached at the boundary where the star degenerates. General resolvent threshold principles can recover the initial positivity criterion; publication priority for the specialized sharp weighted-star consequences remains uncertain. No independent validation is asserted.

## References
1. J. Crank and P. Nicolson, *A practical method for numerical evaluation of solutions of partial differential equations of the heat-conduction type*, Math. Proc. Cambridge Philos. Soc. 43 (1947), 50–67, DOI 10.1017/S0305004100023197.
2. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation*, arXiv:2301.01066, posted January 3, 2023.
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, SCOPE mathematical research record (2026), identifier: 2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
