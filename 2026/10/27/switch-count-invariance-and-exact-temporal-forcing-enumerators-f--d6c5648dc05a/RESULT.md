# Switch-count invariance and exact temporal forcing enumerators for two perfect matchings

## Finding

**Theorem (two-matching temporal forcing profile).** Let \(V\) be a finite set of positive even order, and let \(M_0,M_1\) be any two perfect matchings of \(V\), including the possibility of common edges. Take a nonempty finite word \(\omega=(\omega_1,\ldots,\omega_T)\) in \(\{0,1\}\). Snapshot \(t\) consists of the edges of \(M_{\omega_t}\). In each snapshot, all presently infected vertices simultaneously infect their unique neighbor on that matching edge; infection is permanent. Write
\[
r(\omega)=1+\sum_{t=2}^{T}{\bf1}_{\{\omega_t\ne\omega_{t-1}\}}.
\]
The two-colored multigraph \(M_0\uplus M_1\) is a disjoint union of alternating cycles with \(2m_1,\ldots,2m_h\) vertices, allowing a doubled-edge two-cycle with \(m_i=1\). Define
\[
C_{m,r}(s)=\frac{m}{s}[x^{m-s}](1+x+\cdots+x^{r-1})^s\quad(1\le s\le m),
\]
where coefficients with negative exponents are zero. Then the polynomial enumerating all initial infected subsets that infect every vertex by snapshot \(T\), by their initial cardinality, is exactly
\[
\boxed{\mathcal Z_{M_0,M_1,\omega}(z)=
\prod_{j=1}^{h}\left(\sum_{s=1}^{m_j}C_{m_j,r(\omega)}(s)(2z+z^2)^s\right).}
\]
An initial subset succeeds if and only if, on every alternating cycle, the occupied edges of the **first snapshot's matching**, viewed cyclically, are nonempty and every clockwise gap in matching-edge indices is at most \(r(\omega)\). The entire final infected set, not merely its size or success predicate, is determined by the first matching and \(r(\omega)\), independently of the durations of runs of identical snapshots.

In particular, the minimum size of a successful initial set is
\[
\boxed{\sum_{j=1}^{h}\left\lceil\frac{m_j}{r(\omega)}\right\rceil,}
\]
and the exact number of successful sets of that size is
\[
\boxed{\prod_{j=1}^{h}2^{s_j}C_{m_j,r(\omega)}(s_j),
\qquad s_j=\left\lceil\frac{m_j}{r(\omega)}\right\rceil.}
\]
When \(r(\omega)\ge\max_j m_j\), the full polynomial reduces to \(\prod_j((1+z)^{2m_j}-1)\). A schedule with no snapshots has instead the single successful initial set \(V\), contributing \(z^{|V|}\).

**Random-seed consequence.** On one alternating cycle of \(2m\) vertices, suppose vertices are independently infected initially with fixed probability \(p\in(0,1)\). Put \(q=1-(1-p)^2\), and let \(\tau_m\) be the number of alternating matching runs needed for complete infection (with \(\tau_m=0\) when all vertices are initially infected and \(\tau_m=\infty\) when none is). For every integer \(r\ge1\),
\[
\Pr(\tau_m\le r)=\sum_{s=1}^{m}C_{m,r}(s)q^s(1-q)^{m-s}.
\]
For fixed \(p\), as \(m\to\infty\),
\[
\frac{\tau_m}{\log m}\ \xrightarrow{\Pr}\ \frac{1}{-2\log(1-p)}.
\]
The stochastic statement concerns the number of **switch-separated runs**, not the number of physical snapshots when matching symbols repeat.

## Assumptions and scope

All graphs are finite and loopless. A perfect matching has no isolated vertices; a repeated color edge is treated as a two-edge alternating multigraph cycle for bookkeeping. At each snapshot only one synchronous forcing round takes place, and a newly infected vertex acts only at subsequent snapshots. Every present vertex has exactly one neighbor in its snapshot, so the ordinary temporal zero-forcing rule is precisely infection across every matching edge with at least one infected endpoint. If one forbids common matching edges, simply require \(m_j\ge2\) throughout.

An occupied matching edge means an edge of \(M_{\omega_1}\) having at least one initially infected endpoint. If the occupied matching-edge indices are \(0\le i_1<\cdots<i_s<m\), their cyclic gaps are \(i_{a+1}-i_a\) for \(a<s\) and \(m+i_1-i_s\) for the final gap. For \(s=1\), the gap is \(m\). All coefficients count labeled subsets; no quotient by rotations or graph automorphisms is taken.

## Proof

**1. Matching closure and time compression.** For a matching \(M\), define \(F_M(S)\) to be the union of the endpoints of all matching edges meeting \(S\). Then \(F_M(F_M(S))=F_M(S)\) and \(F_M(S\cup S')=F_M(S)\cup F_M(S')\). Thus every maximal consecutive run of the same matching snapshot can be replaced by one snapshot without changing the final set. The compressed schedule alternates between the two matchings, starting with \(M_{\omega_1}\), and has exactly \(r(\omega)\) snapshots. Distinct alternating-cycle components evolve independently.

**2. Single-source reachability on a component.** Index the \(2m\) vertices cyclically by \(0,1,\ldots,2m-1\), choosing labels so that the first matching consists of \(\{2i,2i+1\}\). The other matching consists of \(\{2i+1,2i+2\}\), with residues taken modulo \(2m\). A seed at either endpoint of first-matching edge \(i\) produces after one compressed snapshot the pair \(\{2i,2i+1\}\). Inductively, after \(r\) compressed snapshots its infected vertices form the cyclic interval
\[
[2i-(r-1),\,2i+r]\pmod{2m},
\]
of length \(\min(2r,2m)\); at each switch the two boundary vertices infect their outward matching neighbors, until the whole cycle is filled. Because matching closure preserves unions, the infected set from arbitrary seeds is the union of these intervals for all initially occupied first-matching edges.

**3. Exact cyclic-gap test.** The interval belonging to edge index \(i\) has \(2r\) consecutive vertices, and advancing the edge index by one translates the interval by two vertices. For \(1\le r<m\), consecutive such intervals cover every intermediate vertex exactly when the cyclic advance between occupied indices is at most \(r\). A larger gap leaves at least two vertices uncovered; if all advances are at most \(r\), the intervals meet or touch all around the cycle. For \(r\ge m\), one nonempty occupied edge covers the whole component, and the same cyclic-gap criterion holds automatically. This proves the if-and-only-if assertion, including shared-edge components \(m=1\).

**4. Count occupied edges.** Suppose exactly \(s\) among the \(m\) first-matching edges are occupied. Mark one occupied edge; there are \(m\) positions for that mark, and the clockwise inter-occupied gaps are a length-\(s\) ordered composition of \(m\) into entries between \(1\) and \(r\). The number of such gap vectors is \([x^{m-s}](1+x+\cdots+x^{r-1})^s\). Every unmarked occupied-edge subset is counted \(s\) times, giving \(C_{m,r}(s)\). On each occupied matching edge the initial infected subset has three choices: first endpoint, second endpoint, or both. Its weight is \(2z+z^2\). Unoccupied matching edges contribute weight \(1\). Multiplication across components proves the polynomial.

**5. Sharp minimum and its multiplicity.** Since \(s\) positive gaps of maximum \(r\) sum to \(m\), necessarily \(s\ge\lceil m/r\rceil\); conversely, choosing gaps of sizes at most \(r\) with this minimal \(s\) is possible, so equality is attained. Each occupied edge needs at least one seed, and at the minimum exactly one of its two endpoints is chosen. This yields the stated cardinality and count, then multiplication across components. If \(r\ge m\), every nonempty subset is successful on that component, establishing the simplified product.

**6. Random initialization.** Each first-matching edge is occupied independently with probability \(q=1-(1-p)^2\), so the cyclic-gap count weighted by \(q^s(1-q)^{m-s}\) proves the probability identity. Write \(v=1-q=(1-p)^2\). Except when no edge is occupied, the number of runs needed is the maximum cyclic gap between occupied edge indices, equivalently one plus the longest cyclic run of unoccupied matching edges; the fully infected initial state is the harmless exceptional case \(\tau_m=0\). For \(0<\varepsilon<1\), a union bound shows that the probability of a vacant run of length at least \((1+\varepsilon)\log(m)/(-\log v)\) is at most \(m v^{\lceil(1+\varepsilon)\log(m)/(-\log v)\rceil}\to0\). Conversely, partition the circle into \(\lfloor m/L\rfloor\) disjoint blocks of length \(L=\lfloor(1-\varepsilon)\log(m)/(-\log v)\rfloor\). Their complete-vacancy events are independent; their expected number diverges at least like \(m^{\varepsilon}/L\), so with probability tending to one some block is vacant. The event of no initially occupied edge has probability \(v^m\to0\). Hence \(\tau_m/\log m\to1/(-\log v)\) in probability, proving the final expression.

## Verification

The standalone standard-library program `verify.py` constructs each matching snapshot as an explicit edge list and performs synchronous infection by inspecting actual selected endpoints; it independently evaluates the polynomial and cyclic-gap conditions. Its exhaustive check covers 648 combinations of matching-cycle families and binary snapshot words and tests 257,976 initial vertex subsets. Command:

```sh
python3 verify.py
```

Expected output:

```text
VERIFY_OK schedule_graph_cases 648 initial_sets_checked 257976
```

Finite verification checks the definitions and algebra on the indicated instances; the general and asymptotic statements rely on the proof above.

## Relationship to prior work

Baste, Dreyer, Marcille, Rabie, and Toullec-Streicher (2026) define the synchronous temporal zero-forcing problem studied here and establish complexity results, including hardness on temporal stars and tractability on bounded-degree temporal trees. Their full 20-page arXiv version treats stars and trees in its main structural sections, not the all-size forcing enumerator for arbitrary pairs of perfect matchings. The independently established static zero-forcing polynomial of Boyer and collaborators motivates all-cardinality enumeration, but is defined for repeated forcing on one fixed graph and does not imply the two-snapshot-switch reduction here.

A separately indexed research archive on *Zero forcing on temporal graphs: Layer-local and footprint-constrained dynamics* mentions exact minimum forcing numbers for alternating even cycles. Its available summary does not establish whether it counts all successful initial sets; a full accessible manuscript comparison was not obtained. Accordingly, no novelty is claimed for any bare minimum-size formula already available in that work. The distinct claim is the complete all-cardinality polynomial for arbitrary two-perfect-matching schedules and component decompositions, with switch-count invariance and the random completion law. Cyclic gap compositions are classical; no novelty is claimed for their abstract counting identity.

## Limitations

The snapshot edge sets must each be one of exactly two fixed perfect matchings; for three matchings, partial matchings, or snapshots with degree exceeding one, the closure and interval proofs do not apply. This work does not solve general temporal zero forcing. The stochastic limit is for fixed \(p\in(0,1)\) on a single growing cycle, not for arbitrary correlated initial seeds or growing families of components. The results have not undergone independent mathematical verification. Historical priority remains uncertain, especially concerning enumerative versions of cyclic covering or temporal matching dynamics.

## References

1. J. Baste, S. Dreyer, C. Marcille, M. Rabie, and R. Toullec-Streicher, *Zero Forcing Sets in Temporal Graphs*, arXiv:2609.29054v1, first posted 2026-09-24, https://arxiv.org/abs/2609.29054 ; accessible complete text: https://pdfs.assets.alphaxiv.org/2609.29054v1.pdf .
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910, 2018, https://arxiv.org/abs/1801.08910 .
3. K. Harish, *Zero forcing on temporal graphs: Layer-local and footprint-constrained dynamics*, research archive description associated with https://github.com/krishnatheaverage/temporal-zero-forcing (repository full text not retrievable during this comparison); associated archive DOI stated as 10.5281/zenodo.21347118. Treat its relationship to full enumeration as an unresolved historical-priority risk.
