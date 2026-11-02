# Exact one-swap robustness law for three-pair stable marriage

## Finding

In a complete strict two-sided marriage market with three agents on each side, draw the six preference orders independently and uniformly, then draw one of the six agents uniformly and interchange one of that agent's two adjacent preference pairs uniformly. Let \(S\) be the number of matchings stable for the original profile and \(R\) the number stable for *both* profiles. The complete exact joint distribution is:

| \(S\) | \(R\) | Number of (profile, swap) cases |
|---:|---:|---:|
| 1 | 0 | 64,944 |
| 1 | 1 | 344,016 |
| 2 | 0 | 5,616 |
| 2 | 1 | 49,536 |
| 2 | 2 | 82,656 |
| 3 | 1 | 1,872 |
| 3 | 2 | 7,344 |
| 3 | 3 | 3,888 |

There are exactly \(6^6\cdot 6\cdot 2=559{,}872\) equiprobable cases. Thus the probability that the original and modified market have no common stable matching equals

\[
\Pr(R=0)=\frac{70{,}560}{559{,}872}=\frac{245}{1944}.
\]

If the swapped positions are the first and second, the failure count is \(49{,}248\) among \(279{,}936\) cases, giving \(19/108\); if they are the second and third, it is \(21{,}312\) cases, giving \(37/486\). Every case with three initially stable matchings retains at least one common stable matching after a single adjacent swap. For comparison, the exact failure probability with two pairs is \(1/4\) among \(64\) cases.

## Assumptions and scope

For \(n\in\{2,3\}\), let \(U=\{0,\ldots,n-1\}\) and \(V=\{0,\ldots,n-1\}\) be disjoint sets. Each member of one side strictly orders *every* member of the other. A perfect matching is a bijection \(M:U\to V\). It is stable if no nonmatched pair \((u,v)\) strictly prefers each other to its partner under \(M\). An adjacent swap exchanges two neighboring entries of exactly one agent's ranking, without altering any other preference. The sample space consists of every labeled profile, every one of the \(2n\) possible chosen agents and every one of the \(n-1\) adjacent positions, each with equal weight. Distinct choices remain distinct sample points even if the resulting modified profile coincides with a profile reached from a different original profile.

Write \(\mathcal S(P)\) for all stable perfect matchings of profile \(P\). For its one-swap modification \(P'\), set \(S=|\mathcal S(P)|\) and \(R=|\mathcal S(P)\cap\mathcal S(P')|\). The theorem concerns this *joint*, not merely marginal, statistic. It makes no claim for markets larger than three pairs or for swaps involving several agents, weak preferences or incomplete lists.

## Proof

**Local criterion.** Let \(x\succ_a y\) occupy consecutive positions in agent \(a\)'s original list, and let the modified list place \(y\succ_a x\). Fix a matching \(M\) stable before the swap. Then \(M\) is unstable afterwards exactly when both (i) the original partner of \(a\) is \(x\), and (ii) \(y\) strictly prefers \(a\) to its own partner under \(M\). Indeed, only the relative comparison of \(x,y\) made by \(a\) changes. If \(a\) is not matched to \(x\), the swap cannot create a new strict preference over its assigned partner; if \(a\) is matched to \(x\), the only newly preferred alternative is \(y\), which forms a blocking pair precisely under condition (ii). This is the adjacent-swap specialization of the shift characterization used in prior robustness work.

**Exhaustive finite argument.** List all \(n!\) possible ranking permutations on \(n\) candidates. Each profile is a \(2n\)-tuple of indices into this list; there are \((n!)^{2n}\) such tuples. For each profile enumerate every one of the \(n!\) perfect matchings. For each matching test every \(n^2\) opposite-side pair against the two strict ranking comparisons in the definition of a blocking pair. This identifies \(\mathcal S(P)\) without using heuristics or sampling. For each of the \(2n(n-1)\) adjacent swap choices, independently repeat those comparisons on each matching in \(\mathcal S(P)\) and count the survivors. The fully specified `verify_robust.py` implements precisely these nested finite loops and asserts that its direct blocking-pair test agrees for *every* case with the local criterion.

For \(n=3\), the enumerator visits all \(6^6=46{,}656\) profiles, six perfect matchings per profile, and all twelve one-swap choices per profile; its exact integer counters are the eight joint counts displayed under Finding. Their sum is \(559{,}872\). The \(R=0\) rows sum to \(64{,}944+5{,}616=70{,}560\); the adjacent-position split is \(49{,}248+21{,}312=70{,}560\). The three initially stable rows all have \(R>0\), proving the stated special guarantee. For \(n=2\), the analogous \(16\) profiles and four swaps produce \(16\) failures among \(64\). Every finite state is covered by the stated Cartesian products and every pairing by the enumerated permutations; hence these are exhaustive finite proofs, not statistical estimates.

## Verification

Run `python3 verify_robust.py` using Python's standard library. It prints the per-size totals, the joint histogram, the robust-count histogram, and the split by swap position; then it asserts all quoted numbers and prints `PASS`. Its direct blocking-pair predicate is evaluated after altering the selected ranking. An independent local condition for every candidate stable matching is asserted to give the same survival decision. All counters and fractions are exact integers/rationals, with no randomized trials, external packages, network calls or assumed files.

## Relationship to prior work

Mai and Vazirani (2018) introduced robustness against upward shifts, including adjacent swaps, and a polynomial-time optimization approach for a fixed market. Gangam, Mai, Raju and Vazirani (2026) study the structure, algorithms and lattice representation of matchings stable across preference modifications, including one adjacent promotion. Their general results establish the model and imply the local shift criterion, but the specific joint \((S,R)\) incidence, uniform one-swap failure probability, top-versus-bottom asymmetry and three-stable preservation census do not appear in the inspected material. These exact finite-population probabilities are the contribution here; the classical lattice theorems and shift characterization are not claimed as novel.

## Limitations

The result is a complete census for two or three pairs, not a closed formula for arbitrary \(n\). Its uniform probability applies to labeled impartial-culture profiles and uniformly chosen single adjacent swaps; actual matching-market preferences can be correlated, and shocks need not be uniform. Larger markets may behave differently. Any literature-priority assertion is provisional without an independent audit; in particular, other catalogues or appendices might contain an equivalent finite census.

## References

1. R. R. Gangam, T. Mai, N. Raju and V. V. Vazirani, *Robust Stable Matchings: Dealing with Changes in Preferences*, arXiv:2601.07959v1 (first public January 12, 2026), https://arxiv.org/html/2601.07959v1.
2. T. Mai and V. V. Vazirani, *Finding Stable Matchings that are Robust to Errors in the Input*, arXiv:1804.00553 (2018), https://arxiv.org/html/1804.00553v4.
3. D. Gale and L. S. Shapley, *College Admissions and the Stability of Marriage*, American Mathematical Monthly 69 (1962), 9–15.
