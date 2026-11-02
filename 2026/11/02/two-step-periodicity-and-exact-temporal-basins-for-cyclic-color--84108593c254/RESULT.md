# Two-step periodicity and exact temporal basins for cyclic color dynamics on cocktail-party graphs

## Finding

For every integer \(n\ge3\), let \(H_n\) be the graph on \(2n\) labelled vertices obtained from the complete graph by deleting a perfect matching. Consider the synchronous three-color cyclic cellular automaton \(F\): a vertex of color \(a\in\mathbb Z/3\mathbb Z\) advances to \(a+1\) if some **adjacent** vertex has color \(a+1\), and otherwise stays at \(a\). The deleted matching partner is not adjacent.

For an initial coloring, its *first-entry time* \(t\) is the smallest nonnegative integer for which its state at time \(t\) is periodic; its *eventual least period* \(p\) is the least period of that state. Let \(N_{t,p}(n)\) denote the number of **labelled initial colorings** with these attributes. The complete table is

| First entry \(t\) | Period \(p=1\) | Period \(p=3\) |
|---:|---:|---:|
| \(0\) | \(3\) | \(9^n-(6n+12)4^{n-1}+6n+3\) |
| \(1\) | \(3\cdot4^n-6n-6\) | \(6n(4^{n-1}-2n)\) |
| \(2\) | \(12n\) | \(12n(n-1)\) |

All other \(N_{t,p}(n)\) vanish. In particular, **as maps on the complete space of labelled colorings**, 
\[
F^5=F^2.
\]
The largest first-entry time is exactly two, attained for every \(n\ge3\); the only recurrent least periods are one and three. There are exactly three fixed configurations and
\[
\frac{9^n-(6n+12)4^{n-1}+6n+3}{3}
\]
distinct primitive three-cycle orbits, each orbit counted only once.

For uniformly independent initial colors, the eventual consensus probability and the immediately-periodic probability satisfy
\[
\Pr(\mathrm{consensus})=\frac{3\cdot4^n+6n-3}{9^n}
\sim3\left(\frac49\right)^n,
\qquad
\Pr(t=0)=1-O\left(n\left(\frac49\right)^n\right).
\]
Thus almost every large-system coloring is **already on** a primitive three-cycle, while the exceptional consensus basin is exponentially small. These probability assertions concern the uniform product distribution and do not assert convergence from all configurations.

## Assumptions and scope

The vertices are partitioned into \(n\) labelled unordered pairs; two vertices are nonadjacent exactly when they are partners in the same pair. Pairs and individual vertices are labelled for counting. The color set is \(\{0,1,2\}\) with cyclic successor. Time is discrete and all vertices are updated in parallel. The theorem holds for every integer \(n\ge3\) with no random-graph assumptions. The case \(n=2\), a four-cycle, is excluded and admits different recurrent periods; it is not covered by the identities above.

## Proof

**Exact pair-type reduction.** There are six unordered pair types,
\[
00,\ 11,\ 22,\ 01,\ 12,\ 02,
\]
with orientation multiplicities \(w=(1,1,1,2,2,2)\). Let \(b_j\) be the number of pairs of type \(j\), and retain its capped count \(c_j=\min(2,b_j)\). For a vertex of color \(a\), all vertices of successor color \(a+1\) are adjacent except possibly its unique matching partner. Consequently a vertex advances precisely when the successor-color population is at least two, or when it is one and the unique successor-colored vertex is not its matching partner. The three successor-population tests \(0,1,\ge2\) are determined by \(c\). The updated ordered colors of each pair, and the updated capped vector, are therefore determined by \(c\), independently of the exact multiplicities \(b_j\ge2\). Reversing the order of an original mixed pair merely reverses the corresponding updated pair, so the reduction applies to labelled orientations as well.

**Finite exact identity.** A capped vector is realized by a coloring with \(n\ge3\) if and only if it has at least one entry equal to two, or at least three entries equal to one. Exactly \(3^6-(1+6+15)=707\) vectors satisfy this. For each, use one representative pair of each type with capped value one, two representative pairs for capped value two, and pad a single capped-two type if needed to obtain at least three pairs. The exact transition rule in the previous paragraph is applied for five updates, tracking each initial pair's ordered colors. The exhaustive 707-case calculation gives \(F^5=F^2\) on each initial pair, not merely equality of aggregate color populations. It also determines the first time \(t\in\{0,1,2\}\) for which either the state at \(t\) is fixed or it returns after three steps; there are no other possibilities. The complete finite calculation, including symbolic successor-population tests, is supplied in `verification/certificate.py`. As the capped-pair rule is exact for every larger multiplicity, this finite calculation establishes the asserted dynamical identity for **all** \(n\ge3\); it is not an extrapolation from small graphs.

**Exact counting.** For an indeterminate \(z\), define
\[
h_0(u)=1,\qquad h_1(u)=u,\qquad h_2(u)=e^u-1-u.
\]
For the class \((t,p)\), let \(\mathcal C_{t,p}\) be the set of capped vectors assigned to that class by the preceding exhaustive reduction. The labelled-pair exponential generating function is
\[
P_{t,p}(z)=\sum_{c\in\mathcal C_{t,p}}
\prod_{j=1}^{6}h_{c_j}(w_jz).
\]
For every \(n\ge3\), the count is \(N_{t,p}(n)=n![z^n]P_{t,p}(z)\). This is exact because a pair of a monochromatic type has one ordered realization and a mixed pair has two, while the exponential generating function accounts for assignments of the \(n\) labelled pairs. Setting \(E=e^z\), the 707-case finite summation simplifies **exactly** to
\[
\begin{aligned}
P_{0,1}&=3(E-1-z),\\
P_{1,1}&=3(E^4-2E(1+z)-3z^2+1),\\
P_{2,1}&=12z(E-1-z),\\
P_{0,3}&=(E^3-1)(E^6+E^3-6Ez-3E+1),\\
P_{1,3}&=6z(E^4-2Ez-2E+1),\\
P_{2,3}&=12z^2(E-1).
\end{aligned}
\]
The finite sum and its exponential-polynomial simplification are checked as literal symbolic identities by the standalone certificate. Coefficient extraction for \(n\ge3\) yields the displayed six rows. These exponential polynomials are used only for the stated range; the small-degree coefficients are not asserted to describe the excluded smaller graphs.

**Consequences.** Every fixed coloring must be monochromatic: any pair of different colors contains a predecessor-successor adjacency in the connected graph, so a stationary coloring cannot use two colors. The period-three configurations initially periodic number \(N_{0,3}(n)\), hence form \(N_{0,3}(n)/3\) orbits. The two first-entry classes at time two are nonempty for \(n\ge3\), so two is sharp. Adding the three fixed-entry classes gives \(3\cdot4^n+6n-3\) consensus-basin states; all others enter a three-cycle. The asymptotics follow immediately from the explicit counts.

## Verification

The finite-state certificate `verification/certificate.py` uses exact integer symbolic transitions on all 707 possible capped-pair signatures, proves equality of full ordered pair states after two and five updates, and derives/checks the six exponential generating functions. It additionally compares the resulting counts for \(3\le n\le10\). Reproduction requires Python 3 and SymPy; run `python verification/certificate.py`.

An independently written direct vertex-by-vertex implementation is `verification/independent.cpp`; compile with `g++ -std=c++17 -O2 verification/independent.cpp -o independent` and run `./independent`. It exhaustively enumerates all \(3^{2n}\) labelled initial configurations for \(n=3,4,5,6,7\), checking the first-entry distribution and the five-versus-two-iterate identity without using the pair-type reduction. The total number of such enumerated initial configurations is \(5{,}380{,}749\). Execution outputs are embedded at `verification/certificate_output.txt` and `verification/independent_output.txt`. Neither finite raw enumeration nor external symbolic software is substituted for the exact all-size reduction explained in the proof.

## Relationship to prior work

Three-color CCA is a classical successor-activated graph automaton, investigated by Fisch, Gravner and Griffeath. Gravner, Lyu and Sivakoff (arXiv:1610.07320, first public 2016-10-24) establish an irrotationality criterion for eventual synchronization on arbitrary connected graphs and an upper bound by graph diameter for synchronization **when it occurs**. Those general facts are prior, not new. The diameter of \(H_n\) is two, so the two-step consensus-only bound is already implied by that theorem. The contribution here is the **full** periodic-entry identity for both synchronizing and oscillating trajectories, the exact six first-entry populations, and the complete primitive three-cycle census in this matching-deleted complete-graph family. General contour criteria do not furnish these numerical classes without an additional graph-specific enumeration.

Three-state Greenberg–Hastings excitation is a different rule: two colors advance unconditionally, whereas each color in CCA requires a successor neighbor. An orbit enumeration for that distinct rule, even on the same graphs, does not imply this one. Results for three-color CCA on paths, ladders and rook graphs likewise concern different adjacency relations, and do not imply these six populations.

## Limitations

The result is specific to three cyclic colors, threshold one, the complement of an exact perfect matching, and \(n\ge3\). It provides no theorem for four or more colors, for other excluded-edge patterns, or for stochastic/asynchronous updating. The novelty comparison is necessarily limited to accessible literature and records; an unindexed equivalent enumeration is possible. A separate independent mathematical audit has not been performed. The finite reduction, symbolic certificate and brute-force check are presented for reproducibility, not as an externally certified formal proof.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, initially public 1993-04-02. https://arxiv.org/abs/patt-sol/9304001
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, initially public 2016-10-24; subsequently *Annals of Applied Probability* 28 (2018), 3324–3357. https://arxiv.org/abs/1610.07320
