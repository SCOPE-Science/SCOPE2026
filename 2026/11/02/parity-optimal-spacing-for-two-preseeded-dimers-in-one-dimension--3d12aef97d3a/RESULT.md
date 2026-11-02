# Parity-optimal spacing for two preseeded dimers in one-dimensional random sequential adsorption

## Finding

Let \(C_n\) be the cycle on \(n\ge4\) labeled vertices, with edges indexed cyclically \(0,\ldots,n-1\). In the standard random sequential dimer model, process all edges in independent continuous identically distributed random-priority order, accepting an edge if neither endpoint has previously been covered. Write \(B_n\) for the expected final number of dimers. For an integer \(2\le d\le n-2\), instead **seed** edges \(0\) and \(d\) before the other edges are processed in uniformly random order; they are disjoint and both accepted. Write \(P_{n,d}\) for the resulting expected final dimer count.

Let \(f_m\) be the expected number of dimers in the analogous process on a path of \(m\) vertices, with \(f_0=f_1=0\), and set \(\rho=(1-e^{-2})/2\). The exact finite-size laws are
\[
B_n=1+f_{n-2},\qquad P_{n,d}=2+f_{d-2}+f_{n-d-2},
\]
where the path expectation has the generating function
\[
\sum_{m\ge0}f_m z^m=\frac{z(1-e^{-2z})}{2(1-z)^2},\qquad |z|<1.
\]
In particular, for every **fixed** integer \(d\ge2\), the sequential limit
\[
I_d=\lim_{n\to\infty}(P_{n,d}-B_n)=1+f_{d-2}-d\rho
\]
exists. The complete interaction profile has the following exact positive-kernel representation. For \(k=d-2\),
\[
(-1)^d I_d=2\int_0^1 t(1-t)e^{-2(1-t)}\left[\frac{(2t)^k}{k!}+\mathbf1_{\{k\ge1\}}\frac{(2t)^{k-1}}{(k-1)!}\right]dt>0,
\]
where the second summand is defined to be absent when \(k=0\). Hence the interaction **alternates strictly in sign with separation**, and its magnitude decreases faster than any geometric rate as \(d\to\infty\).

The sharp global spacing classification is
\[
\max_{d\ge2}I_d=I_4=2e^{-2},\qquad
\min_{d\ge2}I_d=I_3=\frac{3e^{-2}-1}{2}.
\]
Both extrema are unique. Thus spacing four maximizes the excess number of accepted dimers, while spacing three minimizes it in the infinite-system limit. The adjacent-edge case \(d=1\) is not a two-seed configuration and is excluded.

## Assumptions and scope

The substrate is one cycle with homogeneous unit-rate one-attempt dimer arrivals, equivalently a uniformly random permutation of the available edges. Seeds are two **non-overlapping** fixed dimers inserted deterministically before ordinary arrivals; seed placement is a modification of the initial condition, **not** conditioning on two final occupied edges. The finite identities hold for all \(n\ge4\) and \(2\le d\le n-2\); the limit holds for fixed \(d\) as \(n\to\infty\). All expectations count initial seed dimers. No independence is assumed between the final occupancies of different sites.

The seeded experiment is equivalently the limit, for each fixed \(n\), in which the two marked edges have equal exponential attempt rates tending to infinity while other edges retain rate one. No simultaneous growing-cycle/large-rate limit is asserted.

## Proof

**1. Shielding and the exact finite-size decomposition.** The first accepted edge of a cycle, irrespective of its identity, removes its two endpoints and leaves a path of \(n-2\) uncovered vertices. Conditional on the first edge, the remaining independent continuous edge priorities induce a uniformly random order on the still-feasible edges. Thus \(B_n=1+f_{n-2}\). Two disjoint preaccepted edges at cyclic distance \(d\) partition the remaining uncovered vertices into paths of lengths \(d-2\) and \(n-d-2\), whose random-priority restrictions are independent; additivity of the expectation gives \(P_{n,d}=2+f_{d-2}+f_{n-d-2}\). These are equalities of expectations, not assertions of independent counts under the unseeded model.

**2. The path generating function.** For \(m\ge2\), the first path edge is uniform over its \(m-1\) positions. After accepting the edge between vertices \(j\) and \(j+1\), the surviving paths have \(j-1\) and \(m-j-1\) vertices. Consequently
\[
f_m=1+\frac{2}{m-1}\sum_{j=0}^{m-2}f_j.
\]
Writing \(F(z)=\sum_{m\ge0}f_m z^m\), multiplying the recurrence by \((m-1)z^{m-2}\), and summing gives
\[
\frac{zF'(z)-F(z)}{z^2}=\frac1{(1-z)^2}+\frac{2F(z)}{1-z}.
\]
The integrating factor \(e^{2z}(1-z)^2/z\), together with \(F(0)=0\), gives
\[
F(z)=\frac{z(1-e^{-2z})}{2(1-z)^2}.
\]
Its coefficient formula is, for \(m\ge1\),
\[
f_m=\frac12\left[m-\sum_{j=0}^{m-1}(m-j)\frac{(-2)^j}{j!}\right].
\]
Because the numerator is entire, its Taylor expansion at \(z=1\) yields \(f_m=\rho m-e^{-2}+o(1)\). More precisely, subtracting the two principal parts at \(z=1\) leaves an entire function, whose coefficients tend to zero. Hence \(f_{n-d-2}-f_{n-2}\to-d\rho\) for each fixed \(d\), proving the formula for \(I_d\).

**3. Strict alternating sign and factorial decay.** Set \(K(z)=\sum_{k\ge0}I_{k+2}z^k\). Substituting the path generating function and the definition of \(\rho\) gives
\[
K(z)=\frac{e^{-2}(2-z)-ze^{-2z}}{2(1-z)^2}.
\]
The apparent singularity at \(z=1\) is removable. The numerator \(N(z)=e^{-2}(2-z)-ze^{-2z}\) satisfies \(N(1)=N'(1)=0\) and \(N''(z)=4(1-z)e^{-2z}\). Taylor's integral remainder, along the line segment from \(1\) to \(z\), therefore gives the entire-function identity
\[
K(z)=2(1-z)\int_0^1t(1-t)e^{-2(1-t)}e^{-2tz}\,dt.
\]
Extracting the coefficient of \(z^k\) under this finite integral gives the positive-kernel formula in the finding. Strict positivity of its integrand for \(0<t<1\) proves \((-1)^d I_d>0\). Bounding \(t\le1\) shows, for \(k\ge1\),
\[
|I_{k+2}|\le e^{-2}\left(\frac{2^k}{k!}+\frac{2^{k-1}}{(k-1)!}\right),
\]
which proves inverse-factorial decay, and \(|I_2|=e^{-2}\).

**4. Global optimization.** Write \(A_d=|I_d|\). For \(k\ge1\), the integrand factor aside from its common positive weight is
\[
h_k(t)=\frac{(2t)^k}{k!}+\frac{(2t)^{k-1}}{(k-1)!}.
\]
For \(k\ge2\) and \(0<t\le1\),
\[
\frac{h_{k+1}(t)}{h_k(t)}=\frac{2t(k+1+2t)}{(k+1)(k+2t)}<1,
\]
because \(4t^2<k(k+1)\). Thus \(A_d\) is strictly decreasing for all \(d\ge4\). Direct evaluation from the path coefficients gives
\[
I_2=e^{-2},\quad I_3=\frac{3e^{-2}-1}{2},\quad
I_4=2e^{-2},\quad I_5=\frac{5e^{-2}-1}{2}.
\]
Since \(I_4>I_2>0\) and \(|I_3|>|I_5|\), while subsequent positive and negative magnitudes strictly decrease, the claimed global maximizer \(4\) and minimizer \(3\) are unique.

**5. Fixed-size high-rate interpretation.** For any fixed \(n\) and disjoint marked edges, assigning them equal independent rate-\(r\) exponential clocks and all other edges unit-rate clocks makes both marked edges the first two attempts with probability tending to one as \(r\to\infty\). On that event, the process is exactly the seeded process. Since the final count is bounded by \(n/2\), the expected count converges as claimed for each fixed \(n\). This argument is not uniform in \(n\); the theorem does not exchange the two limits.

## Verification

The standalone script \(`checker.py`\) independently enumerates random edge orders on small cycles, including both orders of the forced seeds, and compares exact rational expectations with the two path-decomposition formulas. It also checks generating-function coefficients and evaluates the sign-kernel integral independently by numerical quadrature. It passed 120 assertions and diagnostics. Computation verifies finite cases only; the infinite sign and optimization statements follow from the analytic proof above. Run \(`python checker.py`\) using Python 3 with no third-party dependencies.

## Relationship to prior work

Flory's classical one-dimensional dimer-jamming density \(1-e^{-2}\) and its shielding argument are not claimed as new. Krapivsky and Luck's 2022 review presents the one-dimensional dimer mapping, the density, and inverse-factorial alternating **connected correlations of final occupancies**. The present claim instead concerns an **interventional initial condition**: two fixed dimers are forced before deposition, and the sign and exact global optimizer of the resulting excess total dimer count are classified. General spatially inhomogeneous RSA methods of Percus (1993) and Šamaj–Percus (1994) are potentially broader analytic frameworks, but the particular parity-optimal two-seed comparison and its unique optimal distances were not identified in the accessible materials. Those two historical sources are an explicit priority risk because their complete texts could not be inspected here.

## Limitations

The exact classification concerns a one-dimensional cycle, unit-rate background edges, two disjoint preaccepted dimers, and a fixed separation before taking the large-cycle limit. It does not establish a finite-size universal best spacing, a theorem for arbitrary finite defect rates, multi-seed optimal placement, or a joint high-rate/large-cycle limit. The results are self-contained analytical claims with computational cross-checks, not independently certified historical priority.

## References

1. P. L. Krapivsky and J. M. Luck, *Jamming and metastability in one dimension: from the kinetically constrained Ising chain to the Riviera model*, arXiv:2211.12815v1 (first public 2022-11-23), https://arxiv.org/html/2211.12815v1 , especially §§1, 2.3 and 4.
2. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics 65 (1993), 1281–1329, https://doi.org/10.1103/RevModPhys.65.1281 .
3. J. K. Percus, *Inhomogeneous random sequential adsorption on a lattice*, Journal of Statistical Physics 71 (1993), 1201–1211; abstract/catalogue record available at https://www.researchgate.net/publication/239162113_Lattice_RSA_and_the_Gaussian-mean_spherical_strategy .
4. L. Šamaj and J. K. Percus, *Inhomogeneous random sequential adsorption with equilibrium initial conditions*, Physical Review E 49 (1994), 5149–5157, https://doi.org/10.1103/PhysRevE.49.5149 .
