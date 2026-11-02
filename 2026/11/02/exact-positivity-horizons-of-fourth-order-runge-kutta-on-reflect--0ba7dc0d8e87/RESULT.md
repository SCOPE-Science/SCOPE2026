# Exact positivity horizons of fourth-order Runge–Kutta on reflecting heat paths

## Finding

For every integer \(n\ge2\), let \(Q_n\) be the symmetric generator of the unit-rate nearest-neighbor continuous-time random walk on the \(n\)-vertex path: \((Q_n)_{i,i+1}=(Q_n)_{i+1,i}=1\), \((Q_n)_{ii}=-d_i\), where \(d_1=d_n=1\) and all other degrees are \(2\), with all remaining entries zero. Define the fourth-order classical Runge–Kutta end-step matrix
\[
T_n(z)=I+zQ_n+\frac{z^2Q_n^2}{2}+\frac{z^3Q_n^3}{6}+\frac{z^4Q_n^4}{24},\qquad z\ge0.
\]
Then \(T_n(z)\) is entrywise nonnegative if and only if \(0\le z\le H_n\), where
\[
\boxed{H_n=\begin{cases}
\rho_2,&n=2,\\
\rho_3,&n=3,\\
2/3,&n=4,\\
4/7,&n=5,\\
1/2,&n\ge6.
\end{cases}}
\]
Here \(\rho_2=1.3926467817026408\ldots\) is the unique positive root of \(z^3-2z^2+3z-3=0\), and \(\rho_3=0.9284311878017605\ldots\) is the unique positive root of \(9z^3-12z^2+12z-8=0\). All endpoints are included. For \(n\ge6\), RK4 has exactly the same entrywise-positivity stepsize ceiling as forward Euler on this generator, despite its fourth-order accuracy. These statements concern the end step, not the intermediate RK stages.

## Assumptions and scope

The path has \(n\) labeled vertices, unit edge rates, reflecting endpoints (degree-one diagonal losses), and a constant autonomous generator. All computations use exact real arithmetic. A matrix is *positive preserving* when it maps every componentwise nonnegative vector to a componentwise nonnegative vector; this is equivalent to entrywise nonnegativity. Because \(Q_n\mathbf 1=0\), the RK4 end-step preserves total mass for all \(z\), even when it has negative entries. If \(Q_n\) is scaled by \(\kappa>0\), divide every stated threshold by \(\kappa\). A spatial finite-difference heat discretization with off-diagonal rate \(\kappa/\Delta x^2\) therefore uses \(z=\kappa\Delta t/\Delta x^2\).

## Proof

**1. Universal nonnegative interval.** Put \(P=I+Q_n/2\), which is a nonnegative row-stochastic matrix. With \(t=2z\), direct binomial expansion gives
\[
T_n(z)=\sum_{j=0}^{4}c_j(t)P^j,\qquad
c_j(t)=\frac{t^j}{j!}\sum_{k=0}^{4-j}\frac{(-t)^k}{k!}.
\]
For \(0\le t\le1\) each \(c_j(t)\ge0\): explicitly, \(c_4=t^4/24\), \(c_3=t^3(1-t)/6\), \(c_2=t^2(1-t+t^2/2)/2\), \(c_1=t(1-t+t^2/2-t^3/6)\), and \(c_0=1-t+t^2/2-t^3/6+t^4/24\). The alternating partial sums are nonnegative on \([0,1]\) (or use their simple derivative signs). Consequently \(T_n(z)\ge0\) entrywise whenever \(0\le z\le1/2\), for every \(n\).

**2. A distance-three degree-sum obstruction.** Consider vertices \(i,i+3\) on a path of length at least four. Exactly one three-step off-diagonal walk connects them, giving \((Q_n^3)_{i,i+3}=1\). In the fourth power, the unique length-three route acquires precisely one diagonal factor, at one of its four vertices, and no four-off-diagonal route can cover an odd displacement of three. Hence
\[
(Q_n^4)_{i,i+3}=-(d_i+d_{i+1}+d_{i+2}+d_{i+3}),
\]
and therefore
\[
(T_n(z))_{i,i+3}=\frac{z^3}{24}\left(4-z\sum_{j=i}^{i+3}d_j\right).
\]
For \(n=4\), the only four-vertex route has degree sum \(6\), forcing \(z\le2/3\). For \(n=5\), an outer four-vertex route has degree sum \(7\), forcing \(z\le4/7\). For every \(n\ge6\), there is an interior four-vertex route with degree sum \(8\), forcing \(z\le1/2\). Together with step 1 this proves the complete \(n\ge6\) classification, and the necessary bounds for \(n=4,5\). Negative entries persist at all larger \(z\), so positivity cannot reappear beyond these ceilings.

**3. No other obstruction for four or five vertices.** Since \(Q_n\) is real symmetric negative semidefinite, the polynomial \(T_n(z)\) is positive definite for all real \(z\ge0\): for any \(x\ge0\),
\[
24\left(1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24}\right)
=(x^2-2x+2)^2+4((x-2)^2+1)>0.
\]
In particular all diagonal entries are strictly positive. Entries at distance four are exactly \(z^4/24\). Entries at distance two are \(z^2q(z)\), where the only possible polynomials for \(n=4,5\) are
\[
q(z)=\frac{5z^2-5z+3}{6},\qquad
q(z)=\frac{7z^2-6z+3}{6};
\]
both are strictly positive for all real \(z\), since their quadratic discriminants are negative and leading coefficients positive. Entries at distance one are \(zq(z)\), with possible polynomials
\[
q_A(z)=\frac{6-9z+9z^2-7z^3}{6},\quad
q_B(z)=\frac{4-8z+10z^2-9z^3}{4},\quad
q_C(z)=\frac{24-48z+60z^2-55z^3}{24}.
\]
For four vertices only \(q_A,q_B\) occur; for five vertices only \(q_A,q_C\) occur. Each is strictly decreasing on \([0,\infty)\), because the derivative numerator is a negative quadratic with negative discriminant. Exact endpoint evaluations give
\[
q_A(2/3)=26/81,\quad q_B(2/3)=1/9,
\qquad q_A(4/7)=61/147,\quad q_C(4/7)=253/1029.
\]
Thus all first-neighbor entries remain positive through the asserted respective endpoints. Together with the distance-three test, all entries are nonnegative for \(0\le z\le H_4\) and \(0\le z\le H_5\), and not for any larger \(z\).

**4. Two- and three-vertex exceptions.** For \(n=2\), the unique off-diagonal entry is
\[
(T_2(z))_{1,2}=-\frac z3(z^3-2z^2+3z-3).
\]
Its cubic factor is strictly increasing on \(\mathbb R\), since \(3z^2-4z+3>0\); it changes sign exactly once on the positive axis. For \(n=3\), the nearest-neighbor entry is
\[
(T_3(z))_{1,2}=-\frac z8(9z^3-12z^2+12z-8),
\]
with strictly increasing cubic factor because \(27z^2-24z+12>0\). The only other off-diagonal type is
\[
(T_3(z))_{1,3}=\frac{z^2}{24}(13z^2-16z+12)>0\qquad(z>0),
\]
as the final quadratic has negative discriminant. Diagonal positivity follows from step 3. Both cubic roots are therefore unique sharp thresholds; beyond them an adjacent matrix entry is strictly negative. This completes all sizes.

## Verification

The standalone `verification/verify.py` uses only the Python standard library and exact rational matrix arithmetic. Running `python verification/verify.py` produced `PASS 40497 exact assertions`. It checks the small-path polynomial positivity certificates with rational Bernstein coefficients, sign-brackets both irrational roots to twelve decimal places, evaluates endpoint and beyond-endpoint matrices for every \(2\le n\le30\), and checks the degree-sum identity for every four-vertex segment through \(n=30\). The unbounded-size result comes from the proof above, not from extrapolating the finite enumeration.

## Relationship to prior work

Blanes, Iserles and Macnamara (public preprint February 16, 2021; arXiv:2102.08242, especially sections 1 and 5) give the graph-Laplacian positivity setting and use RK4 as a conventional comparator, but do not present the reflecting-path, all-size RK4 positivity classification. Gottlieb, Grant and Higgs (arXiv:1403.6519, 2014) discuss general strong-stability-preserving coefficient restrictions and convex-combination approaches; their nonlinear SSP statements do not imply the sharp matrix-specific values \(2/3\), \(4/7\), and \(1/2\). Omle, Askar and Kovács (2022) compare different explicit positivity-preserving heat solvers in the inspected full paper, but do not give the classical RK4 finite reflecting-path classification. Horváth (1998) derives universal Runge–Kutta positivity conditions and explicitly notes the classical RK4 scheme has zero universal positivity radius; Horváth (2005) studies universal thresholds and positivity for invariant sub-cones, including a Dirichlet semi-discretized heat example, rather than this sharp entrywise matrix positivity threshold for symmetric reflecting paths. A previous exact classification for directed cyclic generators already covers the two-vertex case, because the directed two-cycle generator agrees with the reflecting two-vertex path; that identical cubic root is included here only to make the path classification complete. For three or more vertices the directed cyclic generators are nonsymmetric and do not imply the reflecting-path thresholds. A 2026 general heat-scheme preprint may contain related positivity analysis but its full text was not available for decisive comparison.

## Limitations

This theorem is for unit-rate symmetric *paths with reflecting endpoints* and classical RK4 end-step nonnegativity in exact arithmetic. It does not cover intermediate-stage positivity, arbitrary weighted or directed graphs, other boundary discretizations, floating-point implementation, or accuracy and stability of long trajectories beyond one-step structure. The threshold is not an RK4 absolute-stability radius. Prior-art searches and inspected full-text literature do not establish guaranteed publication novelty, especially given inaccessible specialized heat-scheme literature.

## References

- S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models* (arXiv:2102.08242, v1, February 16, 2021), https://arxiv.org/abs/2102.08242 . The expanded work appeared as *Positivity-preserving methods for ordinary differential equations*.
- S. Gottlieb, Z. J. Grant and D. Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and optimal Nonlinear Order* (arXiv:1403.6519, March 25, 2014), https://arxiv.org/abs/1403.6519 .
- Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6 .
- Z. Horváth, *On the positivity step size threshold of Runge-Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026 .
- I. Omle, A. H. Askar and E. Kovács, *Systematic testing of explicit positivity preserving algorithms for the heat-equation*, J. Math. Comput. Sci. 12 (2022), article 162, https://doi.org/10.28919/jmcs/7407 .
- M. Coquerelle, *Comprehensive analysis of numerical schemes for the homogeneous heat equation and development of novel one-step Discrete Optimal Diffusion and Discrete Adaptive Diffusion schemes* (June 29, 2026), DOI:10.13140/RG.2.2.28643.11047. Comparison unresolved where full text is inaccessible.
