# Monitoring edge-geodetic sets of cycles: exact enumeration and a parity split among irredundant sets

## Finding

For every simple cycle \(C_n\) on \(n\ge3\) labeled vertices, put \(h=\lfloor(n-1)/2\rfloor\). A vertex set \(S\) is a monitoring edge-geodetic set (MEG-set) if and only if its successive clockwise gaps \(g_1,\ldots,g_m\) all satisfy \(1\le g_i\le h\), where \(m=|S|\), the gaps are positive, and \(\sum_i g_i=n\).

The cardinality enumerator of **all** MEG-sets is
\[
\mathcal E_n(z)=\sum_{m=3}^{n}\frac{n}{m}[u^n]\left(\sum_{j=1}^{h}u^j\right)^m z^m.
\]
Equivalently, its coefficient at \(z^m\) is
\[
\frac{n}{m}\sum_{j=0}^{m}(-1)^j\binom mj\binom{n-jh-1}{m-1},
\]
where a binomial coefficient is zero if its upper index is below its lower index or negative.

An MEG-set is inclusion-minimal if and only if its gap sequence also satisfies \(g_{i-1}+g_i\ge h+1\) at every cyclic index. Its inclusion-minimal-set enumerator is therefore
\[
\mathcal M_n(z)=\begin{cases}
z^3,&n=3,\\
z^4,&n=4,\\
\dfrac{n(n^2-1)}{24}z^3,&n\ge5\text{ odd},\\
\dfrac{n(n-2)(n-4)}{24}z^3+\dfrac{n(n-2)}8z^4,&n\ge6\text{ even}.
\end{cases}
\]
For every odd \(n\ge5\), all inclusion-minimal MEG-sets are triples. For every even \(n\ge6\), there are exactly \(\binom{n/2}{2}\) inclusion-minimal four-vertex MEG-sets, each consisting of two distinct antipodal vertex pairs, in addition to the inclusion-minimal triples. Thus inclusion-minimal monitoring configurations exhibit a sharp parity distinction invisible to the scalar minimum MEG number.

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. \(C_n\) has vertex set \(\mathbb Z/n\mathbb Z\), with edges joining consecutive residues. For an edge \(e\), the pair of probes \(x,y\in S\) monitors \(e\) exactly if removing \(e\) strictly increases their graph distance, equivalently if every shortest \(x\)-\(y\) path contains \(e\). An MEG-set monitors every edge. An inclusion-minimal MEG-set is one for which deleting any single selected vertex destroys monitoring; upward closure of monitoring makes that condition equivalent to inclusion-minimality. All coefficients count **labeled subsets**, not rotational equivalence classes.

For a nonempty selected subset \(S=\{v_1,\ldots,v_m\}\), vertices are indexed in cyclic order and \(g_i\) is the number of clockwise edges from \(v_i\) to \(v_{i+1}\), with \(v_{m+1}=v_1\). The cyclic gap sequence is positive and sums to \(n\). The parameter \(h=\lfloor(n-1)/2\rfloor\) is the greatest integer strictly less than half the cycle length.

## Proof

**Lemma 1 (exact gap criterion).** Suppose some selected-vertex gap has length \(g\ge n/2\). Any path between selected vertices that uses an edge strictly inside that gap must traverse the entire gap, because no selected vertex lies in its interior and a simple cycle path can enter or exit the gap only through its two end vertices. Such a path has length at least \(g\ge n/2\). The complementary path between the same two selected endpoints has length at most \(n-g\le n/2\) (more generally, every arc containing the entire gap has length at least half the cycle). Hence a path through the gap is never a **unique** shortest path, so its edges cannot be monitored. This rules out MEG-sets with any gap \(g\ge n/2\).

Conversely, suppose every gap satisfies \(g_i<n/2\). For each consecutive selected pair \(v_i,v_{i+1}\), its gap arc has strictly fewer than \(n/2\) edges and is therefore the **unique** shortest path between these vertices. Every edge of that arc is monitored by this pair. These arcs partition the edge set of the cycle, so every edge is monitored. Since gaps are integers, the stated condition is exactly \(g_i\le h\).

**Lemma 2 (all-set enumerator).** The gap criterion implies that no MEG-set has fewer than three selected vertices: at most two gaps, each of length at most \(h<n/2\), cannot sum to \(n\). For each \(m\ge3\), the number of ordered gap sequences is \([u^n](u+\cdots+u^h)^m\). Choosing the first selected vertex gives \(n\) choices, while each labeled selected set is represented exactly \(m\) times (once per possible selected starting vertex). Multiplying by \(n/m\) proves \(\mathcal E_n(z)\). Inclusion-exclusion on gaps exceeding \(h\) gives the displayed binomial sum.

**Lemma 3 (irredundance).** Removing selected vertex \(v_i\) merges the two adjacent gaps \(g_{i-1},g_i\) into a single gap of length \(g_{i-1}+g_i\); all other gaps remain unchanged. By Lemma 1, the reduced set is an MEG-set precisely when \(g_{i-1}+g_i\le h\). As monitoring is monotone under adding selected vertices, the original set is inclusion-minimal exactly when \(g_{i-1}+g_i\ge h+1\) for all \(i\).

**Lemma 4 (possible cardinalities of inclusion-minimal sets).** Summing the inequalities from Lemma 3 gives \(2n=\sum_i(g_{i-1}+g_i)\ge m(h+1)\). When \(n=2k+1\) is odd, \(h=k\), so \(m(k+1)\le4k+2\), forcing \(m\le3\); together with Lemma 2, \(m=3\). When \(n=2k\) is even, \(h=k-1\), so \(mk\le4k\) and \(m\le4\). Any MEG triple is automatically inclusion-minimal, since no two-vertex subset is monitoring. If \(m=4\), equality holds throughout the sum, so every adjacent pair of gaps sums to \(k\). In particular the gaps alternate as \(a,k-a,a,k-a\) for some integer \(1\le a\le k-1\), and the four selected vertices are precisely two antipodal pairs. Conversely, any two distinct antipodal pairs have this gap sequence, so they are inclusion-minimal. There are \(k\) antipodal vertex pairs; choosing two gives \(\binom{k}{2}\) distinct four-sets. This includes the unique \(C_4\) MEG-set when \(k=2\).

**Lemma 5 (number of triples).** Every MEG triple is inclusion-minimal. The number of ordered positive triples summing to \(n\) with each entry at most \(h\) is \(\binom{n-1}{2}-3\binom{n-h-1}{2}\) (there cannot be two oversize gaps because \(2(h+1)>n\)). Thus the triple count is \(n/3\) times this number. If \(n=2k+1\), substitution of \(h=k\) simplifies it to \(n(n^2-1)/24\); if \(n=2k\), substitution of \(h=k-1\) simplifies it to \(n(n-2)(n-4)/24\). At \(n=3\), the formula yields the single triple; at \(n=4\), it yields zero triples. Lemmas 4 and 5 prove the claimed inclusion-minimal polynomial in every case. \(\square\)

## Verification

The standalone `verify.py` enumerates every vertex subset for all \(3\le n\le16\). For each deleted cycle edge and each selected vertex pair, it computes the shortest-path distance before and after deletion directly by breadth-first search, builds the monitoring predicate from the original definition, and checks the all-set gap characterization and the closed inclusion-minimal polynomial. All fourteen exhaustive sizes pass and the program prints `VERIFY_OK`. The tests are finite consistency checks; the all-orders conclusions are proved by Lemmas 1--5.

Reproduce with `python3 verify.py` using only the Python standard library. At \(n=16\), the verifier finds \(112\) inclusion-minimal triples and \(28\) inclusion-minimal four-sets, matching both formulas.

## Relationship to prior work

Dev, Dey, Foucaud, Krishna, and Ramasubramony Sulochana (arXiv:2210.03774, first posted 2022-10-07, Section 3.2, Theorem 3.4) introduced MEG-sets and proved \(\operatorname{meg}(C_n)=3\) for \(n=3\) or \(n\ge5\), and \(\operatorname{meg}(C_4)=4\). Their theorem supplies the scalar minimum and an example of a size-three MEG-set, **not** the all-subset polynomial or inclusion-minimal parity census here. The present counts refine, rather than reprove as new, that minimum.

Haslegrave (arXiv:2210.08955, Section 2) develops MEG-set inequalities for Cartesian and strong graph products and discusses cycles as factors; its graph-product bounds do not enumerate all MEG-subsets or irredundant sets of a single cycle. Foucaud et al. (arXiv:2403.09122) address mandatory vertices, extremal classes, bounds and graph operations; their structural results do not supply the cycle-set census. Foucaud et al. (arXiv:2409.19067) address algorithmic complexity and interval/chordal graph classes. The exact cyclic-gap criterion and both enumerators are the contributions assessed here.

## Limitations

The result concerns simple, unweighted, undirected cycles only. It does not assert corresponding formulas for weighted cycles, graphs with chords, Cartesian tori, or arbitrary unicyclic networks. No independent mathematical audit has been performed. Exhaustive verification through sixteen vertices corroborates but does not replace the symbolic proof. Novelty is assessed against the cited inspected primary literature and indexed records; undiscovered, unindexed or differently phrased results remain a priority risk.

## References

1. S. R. Dev, S. Dey, F. Foucaud, N. Krishna, L. R. Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, first posted 2022-10-07. https://arxiv.org/abs/2210.03774
2. J. Haslegrave, *Monitoring edge-geodetic sets: Hardness and graph products*, arXiv:2210.08955, first posted 2022-10-17; *Discrete Applied Mathematics* 340 (2023), 79--84. https://arxiv.org/abs/2210.08955
3. F. Foucaud, C. Marcille, Z. M. Myint, R. B. Sandeep, S. Sen, S. Taruni, *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122, first posted 2024-03-14. https://arxiv.org/abs/2403.09122
4. F. Foucaud, C. Marcille, R. B. Sandeep, S. Sen, S. Taruni, *Algorithms and complexity for monitoring edge-geodetic sets in graphs*, arXiv:2409.19067, first posted 2024-09-27. https://arxiv.org/abs/2409.19067
