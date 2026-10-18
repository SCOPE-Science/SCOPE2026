# Exact three-pattern bias in uniform single-cycle permutations

## Finding
Let \(n\ge4\). Select uniformly one permutation \(\pi\) of \(\{1,\ldots,n\}\) consisting of a single \(n\)-cycle. For each three-letter permutation \(\tau\), let \(N_\tau(\pi)\) be the number of indices \(1\le i\le n-2\) such that the ordered triple \((\pi(i),\pi(i+1),\pi(i+2))\) has relative order \(\tau\). Thus, for example, \(132\) means that the first entry is smallest and the second largest.

The complete conditional mean vector is
\[
\mathbb E_{\mathrm{cyc}}N_{123}=\mathbb E_{\mathrm{cyc}}N_{321}=\frac{n-2}{6},
\]
\[
\mathbb E_{\mathrm{cyc}}N_{132}=\mathbb E_{\mathrm{cyc}}N_{213}=\frac{n-2}{6}-\frac{1}{2(n-1)},
\]
\[
\mathbb E_{\mathrm{cyc}}N_{231}=\mathbb E_{\mathrm{cyc}}N_{312}=\frac{n-2}{6}+\frac{1}{2(n-1)}.
\]
In contrast, for an unrestricted uniform permutation all six expectations equal \((n-2)/6\). In particular, if \(J_n\) indicates the event that an unrestricted uniform permutation is one \(n\)-cycle, then
\[
\operatorname{Cov}(J_n,N_\tau)=\frac{\delta_\tau}{2n(n-1)},\qquad
(\delta_{123},\delta_{132},\delta_{213},\delta_{231},\delta_{312},\delta_{321})=(0,-1,-1,1,1,0).
\]
The exact cancellation for both monotone patterns and opposite biases for the four nonmonotone patterns hold for every \(n\ge4\), not only asymptotically.

## Assumptions and scope
All permutations are on labeled integers with their natural order. A single cycle refers to the group-theoretic cycle decomposition, **not** circular reading of the one-line notation. Only non-wrapping consecutive windows \(i,i+1,i+2\), \(1\le i\le n-2\), are counted. Expectations denoted \(\mathbb E_{\mathrm{cyc}}\) are uniform over the \((n-1)!\) single-cycle permutations. The result does not assert a joint distribution, independence, or a variance formula.

## Proof
**A partial-map contraction lemma.** Fix distinct sources \(a,b,c\) and an injective assignment \(f\) of their three images. Regard its three directed edges as a partial functional digraph on the \(n\) labels. An \(n\)-cycle extending \(f\) exists exactly when the partial graph has no directed cycle. If acyclic, the edges form disjoint directed paths (with unused labels as length-zero paths). Contracting the three edges gives exactly \(n-3\) path components. Every cyclic ordering of these components uniquely extends the three edges to an \(n\)-cycle. Consequently, the number of extending permutations is \((n-4)!\), independent of the particular acyclic injection. Since there are \((n-1)!\) total \(n\)-cycles, each acyclic injective image triple has conditional probability
\[
\frac{(n-4)!}{(n-1)!}=\frac{1}{(n-1)(n-2)(n-3)}.
\]
No cyclic partial injection can extend to an \(n\)-cycle because its already-closed directed cycle has size at most three, smaller than \(n\).

**Exact acyclic triple counts.** Let \(Q_\tau(i,n)\) count ordered triples of distinct output labels with relative order \(\tau\) whose directed edges from the sources \(i,i+1,i+2\) make an acyclic partial map. Write \(B=(n-1)(n-2)(n-3)\). Direct inclusion-exclusion gives the following **integer** counts (each displayed numerator is divisible by six):

| Pattern \(\tau\) | \(6Q_\tau(i,n)\) |
|---|---|
| \(123\), \(321\) | \(B\) |
| \(132\) | \(n^3-6n^2+5n+6+6i\) |
| \(213\) | \(n^3-6n^2+11n-6i\) |
| \(231\) | \(n^3-6n^2+17n-18-6i\) |
| \(312\) | \(n^3-6n^2+11n-12+6i\) |

Here is an explicit inclusion-exclusion recipe that derives the table without assuming the conclusion. Begin with \(\binom n3\) injections of each specified order type. Remove each assignment with a fixed-point loop among the three sources; add back the three pairwise intersections of fixed-point events; subtract the triple intersection. Then remove each of the three possible directed two-cycles, adding back its intersection with the fixed-point event at the remaining source; finally subtract the two possible directed three-cycles. These are all possible directed cycles in a three-edge injective map, and distinct two-cycles cannot coexist. For a fixed point at source \(s\), with its image having rank \(r\) in the prescribed triple, the single-loop contribution is exactly \(\binom{s-1}{r-1}\binom{n-s}{3-r}\). With any two image values prescribed, the remaining value has exactly the number of available labels in the required one of the three intervals separated by the prescribed values. Those observations evaluate every remaining two-edge and three-edge intersection, yielding the displayed five polynomial expressions (with the shared first and last row). This is finite inclusion-exclusion on fully specified events, not an experimental interpolation.

Summing the table over \(1\le i\le n-2\) gives
\[
\sum_iQ_{123}(i,n)=\sum_iQ_{321}(i,n)=\frac{(n-3)(n-2)^2(n-1)}6,
\]
\[
\sum_iQ_{132}(i,n)=\sum_iQ_{213}(i,n)=\frac{(n-3)(n-2)(n^2-3n-1)}6,
\]
\[
\sum_iQ_{231}(i,n)=\sum_iQ_{312}(i,n)=\frac{(n-3)(n-2)(n^2-3n+5)}6.
\]
Divide by \(B\) using the contraction lemma and simplify to obtain all six stated means. For an unrestricted uniform permutation each output triple has each relative ordering with probability \(1/6\). Finally \(\mathbb P(J_n=1)=(n-1)!/n!=1/n\), hence
\[
\operatorname{Cov}(J_n,N_\tau)=\frac1n\bigl(\mathbb E_{\mathrm{cyc}}N_\tau-\mathbb E N_\tau\bigr),
\]
which proves the covariance identity.

## Verification
The standalone `verify_cycles.py` uses standard-library integer arithmetic. It independently enumerates all \(n\)-cycles for \(4\le n\le9\) and compares each of the six exact mean identities as rational numbers (36 cases). It independently enumerates all injective triples for \(4\le n\le15\), every window and every pattern, and checks the acyclic-map polynomial table (540 cases). The script prints the case totals and raises on any mismatch. As an optional symbolic replay, `derive_table.py` uses SymPy to recompute the inclusion-exclusion polynomials and prove their identities by exact symbolic simplification in the unrestricted variables \(n\) and \(i\), not by finite interpolation. The combinatorial proof above establishes arbitrary \(n\); the finite checker is corroboration, not an infinite certificate.

## Relationship to prior work
Novelli, Reutenauer and Thibon (2009; arXiv:0911.5615) encode all consecutive \(k\)-letter patterns using generalized descent codes and study associated Hopf algebras; their inspected text does not give the single-cycle conditional six-pattern mean vector. Crane and DeSalvo (first public preprint 2015; arXiv:1509.07941) study stochastic pattern-occurrence counts and Poisson approximation under uniform and Mallows permutations, not conditioning on a single group-theoretic cycle. Elizalde and Troyka (arXiv:1710.05103, first public 2017) provide cycle-type/descent-set results and enumerate avoidance of the monotone consecutive patterns \(123\) and \(321\); those descent-set results do not determine occurrences of \(132\) and \(231\), which require the nonadjacent comparison within each triple. A separately indexed exact fixed-point/descent covariance result pertains to pairs of adjacent values rather than this six-way single-cycle triple statistic.

## Limitations
The result concerns only first moments of length-three **non-wrapping** patterns in uniformly chosen single cycles. It does not classify longer patterns or general cycle types. The two monotone components are consistent with known cycle/descent-set theory; the distinguishing contribution lies in the complete six-pattern conditioning effect, especially its nonmonotone entries. A more general older consecutive-pattern/cycle-type identity may implicitly imply the result; novelty is subject to further expert literature review.

## References
1. J.-C. Novelli, C. Reutenauer and J.-Y. Thibon, *Generalized descent patterns in permutations and associated Hopf algebras*, arXiv:0911.5615 (first submitted 2009-11-30), European J. Combin. 32 (2011), 618–627.
2. H. Crane and S. DeSalvo, *Pattern avoidance for random permutations*, arXiv:1509.07941 (first submitted 2015-09-26), DMTCS 19(2) (2018).
3. S. Elizalde and J. M. Troyka, *Exact and asymptotic enumeration of cyclic permutations according to descent set*, arXiv:1710.05103 (first submitted 2017-10-13), JCT A 165 (2019), 360–391.
4. I. M. Gessel and C. Reutenauer, *Counting permutations with given cycle structure and descent set*, JCT A 64 (1993), 189–215.
