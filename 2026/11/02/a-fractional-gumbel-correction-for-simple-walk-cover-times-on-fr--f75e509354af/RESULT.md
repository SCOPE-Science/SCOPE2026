# The fractional correction to the discrete-step cover-time distribution on friendship graphs

## Finding

Let \(F_n\) consist of \(n\) triangles whose only common vertex is their hub \(o\). Let \(T_n\) count the steps until a discrete-time, non-lazy simple random walk, started at \(o\), has first visited all vertices. Uniformly for \(x\) in any fixed compact subset of \(\mathbb R\),
\[
\Pr\{T_n\le 4n(\log n+x)\}
=e^{-2e^{-x}}\left(1+n^{-1/3}e^{-4x/3}\right)
 + O\!\left(\frac{\log n}{\sqrt n}\right).
\]
Real thresholds are interpreted in the usual way for integer \(T_n\). The correction is positive at every fixed \(x\); it comes from triangles not entered at all. The claim concerns the distribution at the walk's actual step count, not the mean or a Poissonized walk.

## Proof

**Excursions and the Poissonized law.** At each departure from the hub the walk chooses a uniform triangle and then a uniform peripheral vertex in that triangle. Each subsequent step from a peripheral vertex returns to the hub or moves to the other peripheral vertex with equal probability. Thus a specified peripheral vertex is seen during an excursion with probability \(3/(4n)\), and the probability of entering its triangle is \(1/n\). Successive excursions are iid with respect to their full paths. Their lengths \(L_i\) have mean 3 and an exponential moment: \(\Pr(L_i=2+j)=2^{-j-1}\) for \(j\ge0\).

Let \(M_n\) count the excursions needed to see all peripheral vertices, counting the last one through its return. Independently run a rate-one Poisson process and assign excursion paths to its successive arrivals. Let \(\widetilde M_n\) be the arrival time of excursion \(M_n\). Poisson splitting over triangles and inclusion–exclusion within each triangle give the exact time law
\[
G_n(t):=\Pr\{\widetilde M_n\le t\}
=\left(1-2e^{-3t/(4n)}+e^{-t/n}\right)^n,\qquad t\ge0.
\]
At \(t=t_n(x)=(4n/3)(\log n+x)\), write \(u=e^{-x}\). The base of the power is \(1-2u/n+(u/n)^{4/3}\). Taylor expansion, uniform on compact \(x\)-sets, gives
\[
G_n(t_n(x))=e^{-2u}(1+n^{-1/3}u^{4/3})+O(n^{-2/3}).
\]
The term \((u/n)^{4/3}\) in the base is the probability that an entire triangle was not entered.

**Transfer to the discrete clocks.** For \(n\ge2\) put \(K_n=\lceil 8n\log n\rceil\). A union bound over peripheral vertices gives \(\Pr\{M_n>K_n\}\le 2n^{-5}\). Write \(S_j=\sum_{i=1}^j L_i\) and \(A_j=\sum_{i=1}^j B_i\), with \(B_i\) the independent mean-one exponential interarrival times. For either centered increment law \(X=L_i-3\) or \(X=B_i-1\) there exist constants \(b,c>0\) with \(\log\mathbb E e^{\lambda X}\le b\lambda^2\) for \(|\lambda|\le c\). The exponential Markov bound for each of the first \(K_n\) partial sums, in both directions, followed by a union bound, gives
\[
\Pr\left\{\max_{0\le j\le K_n}\left|\sum_{i=1}^j X_i\right|>a\right\}
\le 2K_n e^{-a^2/(4bK_n)},
\]
whenever \(a/(2bK_n)\le c\), by taking \(|\lambda|=a/(2bK_n)\). For \(a=A\sqrt n\log n\) and sufficiently large fixed \(A\), the bound is \(O(n^{-3})\) for both increment laws. This controls the random indices without any independence assumption between the excursion lengths and \(M_n\).

On the intersection of the three good events, \(\widetilde M_n=A_{M_n}\) differs from \(M_n\) by at most \(a\). Also \(S_{M_n-1}<T_n\le S_{M_n}\), so \(|T_n-3M_n|\le a+3\). Consequently \(|T_n-3\widetilde M_n|\le 4a+3\) except on an event of probability \(O(n^{-3})\). Sandwich the step-count distribution between the Poissonized CDFs at \(t_n(x)\pm(4a+3)/3\), up to this error. In the \(x\) variable this is a shift of size \(O(n^{-1/2}\log n)\), and the two explicit terms of the Poissonized expansion have uniformly bounded derivatives on enlarged compact sets. Inserting the expansion proves the asserted error bound and preserves the fractional coefficient. No Poisson clock is used to define the original random walk.

## Relationship to prior work

The general finite-graph inclusion–exclusion formula is due to Zlatanov and Kocarev, *Random walks on networks: Cumulative distribution of cover time*, Phys. Rev. E 80, 041102 (2009), §IV.C. The same friendship-graph Poissonized product law and the \(n^{2/3}\) correction to the expectation are also obtained in *Fractional-power cover-time improvement from pairing the leaves of a star* ([Resultary](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-fractional-power-cover-time-improvement-from-pairing-the-leaves--e2b8f714b901)); neither is claimed here as distinct. In particular a Taylor expansion of that product already yields the fractional term for the auxiliary clock. The result above controls the clock comparison at smaller order than that term, giving the distribution correction for the actual discrete stopping time. The fractional Gumbel correction in *Fractional Gumbel corrections and a logarithmic symmetry crossover* ([Resultary](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-fractional-gumbel-corrections-and-a-logarithmic-symmetry-crossov--b0e9f34d56db)) is for dimer placement on an even cycle, a different process.

## Verification and scope

The accompanying finite checker concerns the exact excursion model and the auxiliary Poissonized correction. The walk-time asymptotic, including the compact-uniform error, is proved by the two-clock bounds above rather than by numerical extrapolation. No approximation uniform over unbounded \(x\), extension to other petals, or historical priority certification is claimed.
