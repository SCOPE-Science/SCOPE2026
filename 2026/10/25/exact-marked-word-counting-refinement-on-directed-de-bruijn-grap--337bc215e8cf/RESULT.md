# Exact marked-word counting refinement on directed de Bruijn graphs

## Finding

Let \(q,k\geq1\), let \(A\) be an alphabet of size \(q\), and let the directed de Bruijn graph \(D(q,k)\) have vertex set \(A^k\) and edges
\[
(a_1,\ldots,a_k)\longrightarrow(a_2,\ldots,a_k,b)\quad(b\in A).
\]
Choose any (possibly empty) subset \(M\subseteq A^k\). Give every vertex of \(M\) its own initial colour and all remaining vertices one common colour. Refine synchronously by retaining the old colour and recording **separate multisets** of incoming- and outgoing-neighbour colours; count shift loops as edges, but do not separately colour vertices according to the existence of a loop.

Let \(T\subseteq A\) be the set of letters occurring in at least one word of \(M\), let \(t=|T|\), and let \(u=q-t\). Then **two vertices have the same final refinement colour if and only if, at every word coordinate, they either contain the same letter of \(T\) or both contain a letter outside \(T\)**. This partition is reached within at most \(3k-3\) rounds, independently of \(q\) and \(|M|\).

Writing \(c=t+\mathbf 1_{\{u>0\}}\), there are exactly \(c^k\) final colours. A colour containing \(h\) unspecified-letter positions contains exactly \(u^h\) vertices (with the convention that when \(u=0\) only \(h=0\) occurs).

The automorphism group fixing each marked vertex is the full symmetric group on the \(u\) unmentioned letters, acting coordinatewise. Its orbit count is
\[
\sum_{h=0}^{k}\binom{k}{h}t^{k-h}
\sum_{b=0}^{\min(h,u)}\left\{\begin{matrix}h\\b\end{matrix}\right\},
\]
using \(0^0=1\) and the ordinary Stirling numbers of the second kind. A final colour with \(h\) unspecified positions contains exactly \(\sum_{b=0}^{\min(h,u)}\left\{\begin{smallmatrix}h\\b\end{smallmatrix}\right\}\) different stabilizer-orbits, with orbit sizes \((u)_b\) for equality patterns using \(b\) distinct unmentioned letters.

Consequently, refinement gives **exactly** the marked automorphism-orbit partition if and only if \(k=1\) or \(u\leq1\). For \(k\ge2\), this happens precisely when the marked set is a determining set (its pointwise stabilizer is trivial). For a **single named word** the first failure occurs at \(q=3,k=2\): when \(M=\{(0,0)\}\), four refinement classes contain five automorphism orbits; for example, \((1,1)\) and \((1,2)\) have the same final colour but different orbit types.

## Assumptions and scope

The graph is a **directed** unlabelled shift graph, not the underlying undirected graph and not an arc-labelled automaton. Each ordered shift pair contributes one arc; its constant-word loops are counted as ordinary neighbours. The initial colouring has precisely the chosen individually named vertices plus one colour for the rest; it has no additional atomic loop-status colour. The statement holds for all finite alphabets, all positive word lengths, and all finite marker sets including the empty set. The result concerns this specified bidirectional neighbour-counting algorithm, and does **not** purport to describe the full two-variable counting type in a language that includes the additional atomic predicate \(R(x,x)\).

## Proof

**1. An equitable upper bound.** Collapse all letters in \(A\setminus T\) into one formal symbol \(*\), keeping the \(t\) letters in \(T\) distinct. Let \(\pi(v)\) be the resulting length-\(k\) pattern. Vertices with the same pattern have outgoing neighbours with pattern-multiplicity determined by dropping their first pattern entry and appending a symbol: there is one choice for each letter of \(T\) and \(u\) choices for \(*\). The incoming pattern-multiplicities are obtained analogously by prepending. Thus the pattern partition is stable under both directed neighbour-counts. Every individually marked vertex uses only letters of \(T\), hence occupies a singleton pattern cell. This stable partition refines the prescribed initial colours. Therefore the coarsest stable refinement cannot distinguish vertices that have the same pattern.

**2. Recovering every individual named letter by local counting.** Let \(V=\mathbb R^{A^k}\). Define linear operators \(F,B:V\to V\) by
\[
(Ff)(v)=\sum_{v\to w}f(w),\qquad
(Bf)(v)=\sum_{w\to v}f(w).
\]
Let \(e_r\) denote the indicator of a named vertex \(r=(r_1,\ldots,r_k)\in M\). For every \(1\le i,j\le k\), the shift rule gives the exact identity
\[
\bigl(B^{k-j}F^{k-1}B^{i-1}e_r\bigr)(v)
 =q^{\,i-1+k-j}\,\mathbf 1_{\{v_j=r_i\}}.
\tag{1}
\]
To verify it without any appeal to computation, observe that \(B^{i-1}e_r\) is the indicator of words whose first \(k-i+1\) letters agree with the last \(k-i+1\) letters of \(r\). Summing over the \(k-1\) freely appended symbols in \(F^{k-1}\) leaves precisely the condition that the last coordinate equals \(r_i\), with \(q^{i-1}\) choices. Each of the \(k-j\) subsequent predecessor sums in \(B^{k-j}\) moves that condition one coordinate to the left and multiplies by \(q\). This proves (1), including its boundary cases \(i=1,k\) and \(j=1,k\).

Let \(\mathcal P_s\) be the colour partition after \(s\) refinement rounds and \(W_s\) the space of real functions constant on its cells. Since \(e_r\in W_0\), and \(F(W_s)\) and \(B(W_s)\) both lie in \(W_{s+1}\), identity (1) shows that every test \(\mathbf 1_{\{v_j=a\}}\) for every \(a\in T\) and every coordinate \(j\) is constant on \(\mathcal P_{3k-3}\). Vertices sharing a colour at this round must therefore have identical collapsed patterns. Combined with Step 1, their colours are *exactly* the collapsed patterns, and the partition is already stable. If \(M=\varnothing\), its single all-vertex pattern is plainly stable from round zero.

**3. Automorphisms and orbit enumeration.** The full directed de Bruijn automorphism group acts through simultaneous permutations of alphabet letters. This classical fact is also Theorem 4.12 of Boutin–Goliber–Pelto (cited below); it can be proved inductively from the line-digraph construction, where an automorphism of the length-\(k\) graph induces one on the length-\(k-1\) graph and the base length-one graph has symmetric group \(S_q\). Fixing all words in \(M\) pointwise forces every letter that occurs there to be fixed, leaving the group \(S_u\) on the remaining letters.

To enumerate its orbits, first choose the \(h\) coordinates carrying unmentioned letters, and assign to the other \(k-h\) positions arbitrary individual letters of \(T\). The residual equality pattern is a partition of the \(h\) unspecified positions into \(b\) nonempty blocks, where \(b\le u\). There are \(\left\{\begin{smallmatrix}h\\b\end{smallmatrix}\right\}\) such patterns, and each pattern has \((u)_b\) concrete alphabet assignments. Summation yields the displayed formulas. If \(k\ge2\) and \(u\ge2\), the words with the same two unspecified positions but equal, respectively unequal, unmentioned letters occupy a common refinement cell yet different automorphism orbits. Otherwise there is no such distinct equality pattern. This proves the exact criterion and the sharp pointed example.

## Verification

The accompanying three standalone Python programs use only the standard library and build the directed shift graph from its actual adjacency lists. `verify_refinement.py` tests 925 single-root configurations comprising 153,977 examined vertices, comparing the stable partition with the formula and independently enumerating restricted equality-pattern orbits. `verify_markers.py` tests 1,899 marker sets (including empty and multivertex sets), covering 143,895 examined vertices. `verify_operator.py` independently evaluates 3,423 exact vector identities across 271 configurations, including all choices of recovered letter positions and target coordinates. All completed successfully; the plain-text logs are embedded. These are finite checks, not an extrapolation to arbitrary parameters; the proof above establishes the universal claim.

## Relationship to prior work

Boutin, Goliber and Pelto (2014), *Identifying Codes on Directed De Bruijn Graphs* (arXiv:1412.5842), analyze identifying, resolving and determining sets, and prove the full automorphism group and the determining number \(\lceil(q-1)/k\rceil\). Those are used as **known background**. The new statement determines the precise *stable neighbour-counting partition for every individually marked subset*, its quantitative depth, and exactly how its classes coarsen automorphism orbits. A determining-set size theorem does not itself show that counting refinement becomes discrete for every such set, nor does it determine what counting refinement misses for non-determining sets.

Kiefer, Schweitzer and Selman (2015), *Graphs Identified by Logics with Counting* (arXiv:1503.08792), establish general relations between counting logic and equitable partitions and analyze structures identified by counting logic; they do not supply this pointed de Bruijn classification. Berkholz, Bonsma and Grohe (2016), *Tight Lower and Upper Bounds for the Complexity of Canonical Colour Refinement* (DOI 10.1007/s00224-016-9686-0), develop the general refinement framework and explicitly cover digraphs, but do not state the coordinate-pattern and Stirling-orbit formulas. The present result does not claim the cited general framework or de Bruijn automorphism theorem as new.

## Limitations

The claim applies to directed in/out neighbour-counting with the stated starting colours, not to arbitrary arc-labelled automata, undirected de Bruijn graphs, or full atomic-type refinement with an extra initial loop-status predicate. It gives the bound \(3k-3\) but does not assert optimality of the number of rounds. Finite verification covered only the listed parameter ranges. The exact literature comparison found no equivalent statement, but no literature search proves publication priority; independently reviewing additional specialized literature remains advisable. This work has not received independent mathematical audit.

## References

1. Debra Boutin, Victoria Horan Goliber, and Mikko Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, first submitted 18 December 2014; Theorems 4.12 and 4.13 and Section 4.3. https://arxiv.org/html/1412.5842v3
2. Sandra Kiefer, Pascal Schweitzer, and Erkal Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first submitted 30 March 2015; Sections 1–2 and 5. https://arxiv.org/html/1503.08792v1
3. Christoph Berkholz, Paul Bonsma, and Martin Grohe, *Tight Lower and Upper Bounds for the Complexity of Canonical Colour Refinement*, first online 27 June 2016, DOI:10.1007/s00224-016-9686-0, Sections 1–3. https://link.springer.com/article/10.1007/s00224-016-9686-0
