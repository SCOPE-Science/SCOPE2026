# Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs

## Finding

For every finite connected complete multipartite graph with all edges of unit conductance, the end-step positivity intervals of the degree-two, degree-three and degree-four exponential Taylor polynomials are determined exactly. The degree-two and degree-four thresholds depend **only** on the total number of vertices, while degree three depends on the existence of singleton parts and the size of the smallest nonsingleton part. In orders three and four these are respectively the stability polynomials of standard three-stage, third-order and classical four-stage, fourth-order explicit Runge–Kutta schemes on a linear autonomous system.

**Theorem.** Let \(k\ge2\), let \(n_1,\ldots,n_k\) be positive integers, and put \(N=\sum_i n_i\ge2\). Let \(L\) be the ordinary unweighted graph Laplacian of \(K_{n_1,\ldots,n_k}\). For each \(p\in\{2,3,4\}\), put
\[
T_p(h)=\sum_{j=0}^{p}\frac{(-hL)^j}{j!},\qquad h\ge0.
\]
There is a finite \(\sigma_p>0\) such that \(T_p(h)\) is entrywise nonnegative if and only if \(0\le h\le\sigma_p\). More precisely,
\[
\boxed{\sigma_2=\frac2N,\qquad\sigma_4=\frac{\rho_4}{N}},
\]
where \(\rho_4=2.78529356340528\ldots\) is the unique positive zero of
\[
 z^3-4z^2+12z-24.
\]
Let \(\eta_N>0\) be the unique root of
\[
1-\eta_N+\frac{\eta_N^2}{2}-\frac{\eta_N^3}{6}=-\frac1{N-1}.
\]
With the minimum of an empty set understood as \(+\infty\), the third-order threshold is
\[
\boxed{\sigma_3=\min\left\{\left\{\frac{\eta_N}{N}:\exists i\ (n_i=1)\right\}\cup\left\{\frac3{2N-n_i}:n_i\ge2\right\}\right\}.}
\]
At every finite positive step below the threshold all graph-edge entries are positive. At the third-order threshold, a singleton diagonal or a within-part off-diagonal reaches zero; at the second- and fourth-order thresholds every cross-part edge entry reaches zero. The matrices preserve row and column sums equal to one at all timesteps, even outside their nonnegative ranges.

**Order reversal and extremizers.** For \(N=2,3\), \(\sigma_3>\sigma_2\); for \(N=4\), \(\sigma_3=\sigma_2\) for every multipartition. For \(N\ge5\), \(\sigma_3\le\sigma_2\), with equality exactly for a balanced complete bipartite graph (necessarily even \(N\)). Thus third order usually admits a *smaller* nonnegative end-step horizon than second order, while fourth order always admits a larger one. At each \(N\ge4\), the minimum possible third-order horizon over all multipartitions is \(3/(2N-2)\), attained whenever at least one part has size two. For \(N\ge6\), the maximum is \(3/(2N-\lfloor N/2\rfloor)\), attained uniquely up to part permutation by \(K_{\lfloor N/2\rfloor,\lceil N/2\rceil}\). At \(N=5\), the maximum is instead \(\eta_5/5\), attained by the partitions \((4,1)\), \((3,1,1)\), and \((1,1,1,1,1)\). The ratio \(\sigma_4/\sigma_2=\rho_4/2\) is partition-independent.

## Assumptions and scope

All graphs are finite, simple, undirected, connected, complete multipartite, with at least two nonempty parts and a common unit edge conductance. Positivity means **entrywise nonnegativity of the final update matrix for every nonnegative initial vector**, not positivity of internal Runge–Kutta stages, nonlinear SSP guarantees, contractivity for arbitrary nonlinear operators, or unconditional stability. For uniform conductance \(c>0\), replace every displayed \(\sigma_p\) by \(\sigma_p/c\). There is no restriction that the part sizes be equal. Only the exponential Taylor stability polynomials of degrees 2, 3 and 4 are covered.

## Proof

**1. An exact spectral projector decomposition.** Partition vertex coordinates into the \(k\) classes. Write \(J\) for the \(N\times N\) all-ones matrix and \(J_i\) for the all-ones matrix on class \(i\), extended by zeros off that class. The mutually orthogonal projectors
\[
P_0=J/N,\quad P_N=\sum_i J_i/n_i-J/N,\quad
P_i=I_i-J_i/n_i
\]
resolve the identity. Their Laplacian eigenvalues are respectively \(0\), \(N\), and \(q_i=N-n_i\). Indeed class-constant vectors of total sum zero have eigenvalue \(N\), and vectors summing to zero within a class have eigenvalue \(q_i\). These subspaces exhaust the vertex space. Hence for any polynomial \(f\) with \(f(0)=1\),
\[
f(L)=P_0+f(N)P_N+\sum_i f(q_i)P_i.
\]
Write \(r_p(z)=\sum_{j=0}^p(-z)^j/j!\). For \(T_p(h)=r_p(hL)\), its entries depend on just three types. Between *different* parts,
\[
X_p(h)=\frac{1-r_p(Nh)}{N}.
\]
Between *distinct* vertices in part \(i\), writing \(a=n_i\), \(q=N-a\),
\[
Y_{p,a}(h)=\frac{a+qr_p(Nh)-Nr_p(qh)}{Na}.
\]
On the diagonal of that part, the entry is \(Y_{p,a}(h)+r_p(qh)\). When \(a=1\), there are no within-part off-diagonal entries and the diagonal simplifies to \([1+(N-1)r_p(Nh)]/N\). Every update has row and column sums one by \(L\mathbf 1=0\).

**2. Second order.** The polynomial \(r_2(z)=1-z+z^2/2\) is strictly positive for real \(z\ge0\). Direct substitution in the projector formula gives
\[
Y_{2,a}(h)=\frac{q h^2}{2}>0\qquad(a\ge2,\ h>0).
\]
All diagonal entries are positive. The only possible loss is \(X_2(h)<0\), which occurs exactly when \(Nh>2\), since \(1-r_2(z)=z(1-z/2)\). This proves \(\sigma_2=2/N\).

**3. Fourth order.** Put \(r_4(z)=1-z+z^2/2-z^3/6+z^4/24\). The identity
\[
24r_4(z)=(z^2-2z+2)^2+4((z-2)^2+1)>0
\]
holds for all real \(z\). Moreover
\[
Y_{4,a}(h)=\frac{q h^2}{24}\Big[12-4(N+q)h+(N^2+Nq+q^2)h^2\Big].
\]
The bracket is a quadratic with positive leading coefficient and discriminant
\[
16\big[(N+q)^2-3(N^2+Nq+q^2)\big]
=-16(2N^2+Nq+2q^2)<0.
\]
Thus all existing within-part off-diagonals and all diagonals remain strictly positive for every positive step. For cross-part entries,
\[
1-r_4(z)=-\frac z{24}(z^3-4z^2+12z-24).
\]
The cubic has derivative \(3z^2-8z+12>0\) everywhere and changes sign exactly once on the positive axis, at \(\rho_4\). Therefore \(X_4(h)\ge0\) precisely for \(Nh\le\rho_4\), proving both necessity and sufficiency.

**4. Third order.** We have
\[
r_3'(z)=-\tfrac12((z-1)^2+1)<0
\]
for \(z\ge0\), so \(X_3(h)>0\) for every positive step. For a class of size \(a\ge2\),
\[
Y_{3,a}(h)=\frac{q h^2}{6}\,[3-(N+q)h].
\]
This entry is nonnegative exactly when \(h\le3/(N+q)=3/(2N-a)\). Within that interval, \(qh\le3q/(N+q)<3/2\), so \(r_3(qh)>r_3(3/2)=1/16>0\). Thus its diagonal is automatically strictly positive. A singleton diagonal is \([1+(N-1)r_3(Nh)]/N\); strict decrease of \(r_3\) makes it nonnegative exactly for \(Nh\le\eta_N\). These are all entries. Since a violating entry is strictly negative immediately beyond its own cutoff and remains negative, their minimum gives exactly the claimed full positivity interval.

**5. Order comparison and part-profile extremizers.** The identity \(r_3(2)=-1/3\), together with strict decrease, gives \(\eta_N>2\) for \(N<4\), \(\eta_4=2\), and \(\eta_N<2\) for \(N>4\). If no singleton part exists, the smallest class size \(s\) satisfies \(s\le N/2\), and \(3/(2N-s)\le2/N\), with equality precisely at two equal parts. When a singleton exists and \(N\ge5\), its diagonal constraint is already strictly below \(2/N\). At \(N=2,3\) the explicit possible multipartitions show \(\sigma_3>2/N\); at \(N=4\) every possible multipartition gives equality. This proves the reversal statement.

For \(N\ge4\), every nonsingleton threshold is at least \(3/(2N-2)\). The singleton threshold obeys the same lower bound, because at \(z=3N/(2N-2)\),
\[
r_3(z)+\frac1{N-1}=\frac{N(N-4)(N+2)}{16(N-1)^3}\ge0,
\]
and \(r_3\) is strictly decreasing. A part of size two attains this bound (every integer \(N\ge4\) permits such a multipartition); conversely equality is impossible without a size-two part when \(N\ge5\). This proves the minimum classification, including its equality cases for \(N\ge5\).

For \(N\ge6\), every nonsingleton threshold is at most \(3/(2N-\lfloor N/2\rfloor)\), since the smallest nonsingleton size is at most \(\lfloor N/2\rfloor\). With singleton parts, their threshold is strictly smaller than this bound: for even \(N\) this follows from \(\eta_N<2\), and for odd \(N=2m+1\ge7\) it follows by substituting \(z=3(2m+1)/(3m+2)\) into
\[
r_3(z)+\frac1{2m}
=-\frac{(2m+1)(9m^3-9m^2-21m-8)}{2m(3m+2)^3}<0.
\]
The polynomial factor is positive for every integer \(m\ge3\). Thus exactly the balanced two-part graph attains the upper bound. For \(N=5\), a nonsingleton-only multipartition has horizon \(3/8\), while \(\eta_5/5>3/8\) by the preceding positive identity; enumerating the partitions containing singletons yields exactly the three stated maximizers. This completes the proof.

## Verification

The standalone `verify.py` (Python standard library only) independently forms exact rational graph Laplacians and evaluates their degree-two through degree-four update matrices by repeated matrix multiplication. It compares every entry with the spectral projector formulas for every multipartition of orders two through eight and three positive rational timesteps. It also tests both sides of the analytically derived sharp horizon for every multipartition through order seventeen, verifies the extremal part profiles, and independently brackets the fourth-order cubic root. Its successful replay printed `PASS exact matrix entries: 23634` and `PASS phase-transition cases: 3582`. This is supplementary finite evidence; the all-size proof rests on the displayed projector algebra, discriminant and scalar monotonicity inequalities.

## Relationship to prior work

General SSP theory characterizes method-level monotonicity guarantees relative to a forward Euler step, but those guarantees need not be sharp for a restricted fixed family of linear graph generators. Hadjimichael, Macdonald, Ketcheson and Verner (2012/2013) study SSP Runge–Kutta methods and their effective-order optimization, not exact end-step nonnegativity on complete multipartite graphs. Higueras, Ketcheson and Kocsis (first public preprint 2015) study optimized perturbations and discuss classical RK4's lack of a positive universal SSP coefficient, not the exact graph-family endpoint thresholds. Blanes, Iserles and Macnamara (2022) analyze graph-Laplacian positive ODEs and construct different positivity-preserving integrators rather than claiming these three unmodified polynomial thresholds. Horváth (1998, Sections 4–5 and Example 1) establishes general Runge–Kutta positivity radii, including the classical RK4 method’s zero universal radius of positivity. This is a bound for an entire class of positive problems and does not calculate the positive, method-specific end-step radii of complete multipartite graph generators, nor does it compare the second- and third-order graph horizons or classify optimal partitions. Closely related published analyses of implicit Padé and SDIRK positivity do not imply an identical statement about these explicit polynomial stability functions.

The new claim is the *joint, exact and all-part-profile endpoint classification*, especially third-order order reversal and global partition extremizers. It does not claim novelty for the basic RK stability polynomials, the orthogonal decomposition of complete multipartite Laplacians, or the universal SSP order barrier.

## Limitations

The conclusions apply to final update matrices for linear autonomous unit-rate complete multipartite graph diffusion. They say nothing about internal RK stage positivity, nonlinear problems, nonuniform edge rates, other graph families or orders above four. The positive stochastic endpoint matrix need not yield a good approximation at steps near the horizon; eigenmode stability and local-error considerations are distinct. The proof is mathematical but has not undergone independent audit. Publication priority remains limited by the possibility of differently worded specialist results outside the primary literature inspected; although the Horváth (1998) full text was examined, other older positivity studies and graph-specific articles have not been exhaustively checked.

## References

1. Y. Hadjimichael, C. B. Macdonald, D. I. Ketcheson and J. H. Verner, *Strong stability preserving explicit Runge–Kutta methods of maximal effective order*, arXiv:1207.2902 (first posted July 12, 2012), SIAM J. Numer. Anal. 51 (2013), 2149–2165, https://arxiv.org/abs/1207.2902, https://doi.org/10.1137/120884201.
2. I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024 (first posted May 15, 2015), J. Sci. Comput. 76 (2018), 1337–1369, https://arxiv.org/abs/1505.04024.
3. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, ESAIM Math. Model. Numer. Anal. 56 (2022), 1843–1870, https://doi.org/10.1051/m2an/2022042.
4. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Appl. Numer. Math. 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6 (full text inspected, especially Sections 4–5).
