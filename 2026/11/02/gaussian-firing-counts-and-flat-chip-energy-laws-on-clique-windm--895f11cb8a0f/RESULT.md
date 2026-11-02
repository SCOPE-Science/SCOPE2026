# Gaussian firing counts and flat chip-energy laws on clique windmills

## Finding
Let \(W_{n,m}=K_1\vee(nK_m)\), where \(n\ge1\) and \(m\ge2\). For ordinary synchronous degree-threshold parallel chip firing, count distinct primitive temporal two-cycle orbits of labelled chip configurations, with no quotient by graph automorphisms. Every such orbit has a unique phase in which the universal center fires. Let \(K\) count firing noncentral vertices in that phase, and let \(E\) be the conserved total number of chips.

Define the finite polynomial
\[
A_m(z)=\sum_{k=0}^{m-1}\binom{m}{k}(m-k)^k(k+1)^{m-k}z^k,
\qquad \alpha_m=A_m(1),\qquad \mu_m=\frac{A'_m(1)}{\alpha_m},
\]
with \(\nu_m=A''_m(1)/\alpha_m+\mu_m-\mu_m^2>0\). Then the exact orbit census by \(K\) is
\[
\boxed{\mathcal H_{n,m}(z)=\sum_{\mathcal O\,\text{primitive }2\text{-cycle}}z^{K(\mathcal O)}
=n A_m(z)^{n-1}\bigl(mA_m(z)-zA'_m(z)\bigr).}
\]
In particular, the unweighted orbit count is
\[
\boxed{N_{n,m}=n(m-\mu_m)\alpha_m^n,}
\]
and the average conserved energy over all such orbits is exactly
\[
\boxed{\mathbb E[E]=n\bigl(m^2+m/2\bigr)-1/2.}
\]

For each fixed \(m\ge2\), select a primitive two-cycle orbit uniformly and examine its unique center-firing phase. As \(n\to\infty\),
\[
\boxed{\left(\frac{K-n\mu_m}{\sqrt n},\frac{E}{n}\right)
\ \xrightarrow{\mathrm d}\ (Z_m,U_m),}
\]
where \(Z_m\) is centered normal with variance \(\nu_m\), \(U_m\) is uniform on the nondegenerate interval
\[
\boxed{\left[m^2+\frac{\mu_m}{2},\ m^2+m-\frac{\mu_m}{2}\right],}
\]
and \(Z_m\) and \(U_m\) are independent. Thus the firing population has Gaussian fluctuations while total chip energy has a macroscopic *uniform*, rather than Gaussian, limit.

For the friendship graphs \(W_{n,2}\), \(A_2(z)=1+4z\) and
\[
\boxed{\mathcal H_{n,2}(z)=n(2+4z)(1+4z)^{n-1},\qquad N_{n,2}=6n5^{n-1}.}
\]
Here the normalized energy converges to \(\operatorname{Uniform}[22/5,28/5]\), independently of the Gaussian firing fluctuation of variance \(4/25\).

## Assumptions and scope
The graph has one distinguished universal center and \(n\) disjoint labelled peripheral cliques each of order \(m\). The center has degree \(mn\); every peripheral vertex has degree \(m\). All chip counts are nonnegative integers. At each synchronous step, a vertex with at least its degree in chips sends one chip to every neighbor; other vertices wait. Orbits are distinguished as labelled chip configurations, not up to permutation of cliques or vertices. Only *primitive period-two orbits* are enumerated; the statement does not classify all longer-period or transient behavior. The joint limit keeps \(m\) fixed and sends \(n\) to infinity.

## Proof
**Two-cycle phase criterion.** Write \(f_v\in\{0,1\}\) for whether vertex \(v\) fires and \(q_v\) for its number of firing neighbors. A synchronous step sends \(\sigma_v\) to \(\sigma_v+q_v-d_vf_v\). On a connected graph, if the configuration returns after two steps, the total two-step firing count at each vertex must be equal: the graph Laplacian annihilates their firing-count vector, so that vector is constant. For a nonfixed two-cycle that constant is exactly one; constants zero or two force all vertices to wait or fire on both steps, giving a fixed state. Hence the firing vector is complemented on the next step, and an initial chip count is valid precisely when
\[
 d_v\le\sigma_v+q_v\le2d_v-1.
\]
For a first-step firing vertex this gives exactly \(d_v-q_v\) integer choices of \(\sigma_v\); for a waiting vertex it gives exactly \(q_v\). Conversely, these local intervals force complementary firing on the next step and exact return after two steps, so the conditions are sufficient as well as necessary. This is the elementary two-cycle criterion underlying Scully–Zhang–Jiang's general characterization [2]; it is reconstructed here for the specified graph.

**Exact labelled census.** Exactly one of the two phases has the center firing. Fix that phase. In one peripheral clique suppose exactly \(k\) of its \(m\) vertices fire. A firing peripheral vertex sees \(k\) firing neighbors (the center and \(k-1\) peers), giving \(m-k\) possible chip counts. A waiting peripheral vertex sees \(k+1\) firing neighbors, giving \(k+1\) possible chip counts. Thus its clique contributes \(a_m(k)=\binom{m}{k}(m-k)^k(k+1)^{m-k}\) labelled local configurations; \(a_m(m)=0\). If all cliques together have \(K\) firing peripheral vertices, the center has \(mn-K\) chip choices, namely the integers from \(mn\) through \(2mn-K-1\). The coefficient of \(z^K\) among all canonical phases is therefore \((mn-K)[z^K]A_m(z)^n\). Summing yields \(\mathcal H_{n,m}(z)=mn A_m(z)^n-z(A_m(z)^n)'\), the displayed polynomial. Every primitive two-cycle is counted exactly once because it has exactly one center-firing phase. Substituting \(z=1\) gives the orbit count. The terms at \(k=0\) show \(\alpha_m>0\) and \(\mu_m<m\); distinct positive terms at \(k=0,1\) give \(\nu_m>0\) for \(m\ge2\).

**Gaussian–uniform joint limit.** Let a baseline petal configuration be chosen uniformly among its \(\alpha_m\) legal local assignments, independently across cliques, before selecting a hub count. Under that product law, the number \(X_i\) of firing peripheral vertices in clique \(i\) has probabilities \(\Pr(X_i=k)=a_m(k)/\alpha_m\), mean \(\mu_m\) and variance \(\nu_m\). The uniform distribution on actual orbits is obtained by tilting this product law by \(D_n=mn-\sum_i X_i\), since there are exactly \(D_n\) permissible center-chip values. Its Radon–Nikodym derivative is \(D_n/[n(m-\mu_m)]\). The total variation distance from the baseline product law is at most
\[
\frac{\mathbb E\left|\sum_i(X_i-\mu_m)\right|}{2n(m-\mu_m)}
\le\frac{\sqrt{\nu_m}}{2(m-\mu_m)\sqrt n},
\]
so the law of large numbers and the usual iid central limit theorem apply also to uniformly sampled orbits.

Conditional on \(X_i=k\), each firing peripheral vertex has its chip count uniformly in the integer interval \([m,2m-k-1]\), and each waiting peripheral vertex in \([m-k-1,m-1]\). Their conditional *total* mean is
\[
 k\frac{3m-k-1}{2}+(m-k)\frac{2m-k-2}{2}=m(m-1)+k/2.
\]
Local chip totals are uniformly bounded for fixed \(m\), so the peripheral-chip sum divided by \(n\) converges in probability to \(m(m-1)+\mu_m/2\). Independently introduce \(V\sim\operatorname{Uniform}[0,1)\) and select the center chip count as \(mn+\lfloor V D_n\rfloor\); this is conditionally uniform over its \(D_n\) legal integer values. Since \(D_n/n\to m-\mu_m\), the normalized total energy converges to
\[
 m+\bigl(m(m-1)+\mu_m/2\bigr)+(m-\mu_m)V
 =m^2+\mu_m/2+(m-\mu_m)V.
\]
The baseline central-limit variable is independent of \(V\); the vanishing total variation tilt and Slutsky's theorem give their asserted joint independent limit.

**Exact energy mean.** On every primitive two-cycle, the chip complement \(\sigma_v\mapsto2d_v-1-\sigma_v\) is a nonnegative integer configuration, preserves the two-cycle property, and acts as an involution on orbits. Its energy is \(4|E(W_{n,m})|-|V(W_{n,m})|-E\). Since \(|E(W_{n,m})|=nm(m+1)/2\) and \(|V(W_{n,m})|=mn+1\), uniform orbit sampling has exact mean \(\bigl((2m^2+m)n-1\bigr)/2\). This is the displayed finite-size formula, without invoking the limit law.

## Verification
The standalone `verify_windmill.py` directly simulates both updates on canonical center-firing states. It exhaustively checks \(846922\) normalized labelled candidate states over the parameter pairs \((n,m)=(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,4)\), comparing their exact firing-population histograms with the coefficient formula. It additionally checks exact energy-complement symmetry and the mean identity in each case, and algebraically tests the closed orbit-count formula for \(1\le m\le9\) and multiple values of \(n\). The recorded output ends with `WINDMILL_CHIPFIRING_VERIFY_OK`. These finite checks corroborate but do not replace the proof for unbounded \(n\) and fixed \(m\).

## Relationship to prior work
Jiang [1] proves general equality of vertex firing totals over one period and discusses complete bipartite and multipartite period spectra. Scully, Zhang, and Jiang [2] give the general two-cycle condition (Section 4), which is used as a starting point here rather than claimed as new. The explicit labelled windmill orbit polynomial, its specialization \(6n5^{n-1}\), and the joint Gaussian/peripheral-firing versus uniform/energy limit do not appear in those inspected statements. Wang and Lannan [3] give a graph-universal middle chip-density interval for eventual period two, which does not enumerate primitive orbit configurations, weight their firing patterns, or determine the distribution of conserved energy under uniform orbit sampling. Levine [4] treats mode locking for complete graphs, a different graph family. The formula concerns periodically recurrent configurations, not the basins of attraction in the full unrestricted state space.

## Limitations
This is an exact specialized calculation derived from a known general two-cycle characterization, not a newly discovered general criterion for two-cycles. The result does not decide which initial nonperiodic configurations eventually enter the counted orbits, nor does it classify periods other than two. The Gaussian–uniform limit is proved only for fixed clique size \(m\) as the number of cliques grows. Literature indexing may omit historical equivalents, including equivalent formulations of chip-energy ensembles. Finite verification alone would not establish either the infinite family formula or the limit law.

## References
[1] T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first submitted 2010-03-04; https://arxiv.org/abs/1003.0943.

[2] Z. Scully, Y. Zhang, and D. Jiang, *Total Chip Numbers and Motors in the Parallel Chip-Firing Game*, 2011, Section 4; https://math.mit.edu/research/highschool/primes/materials/2011/Scully-Zhang-Jiang.pdf.

[3] D. Wang and N. Lannan, *All parallel chip-firing games with \(2|E|-|V|<|\sigma|<2|E|\) have period 2*, arXiv:2608.04153, 2026; https://arxiv.org/abs/2608.04153.

[4] L. Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number*, arXiv:0811.2800, 2008; https://arxiv.org/abs/0811.2800.
