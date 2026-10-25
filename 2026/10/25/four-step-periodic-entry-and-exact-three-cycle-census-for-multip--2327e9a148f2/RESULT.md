# Four-step periodic entry and exact three-cycle census for multipartite excitable dynamics

## Finding

For each integer \(r\ge3\) and every tuple of positive integers \((n_1,\ldots,n_r)\), consider the deterministic synchronous three-state Greenberg–Hastings automaton on the loopless complete multipartite graph \(K_{n_1,\ldots,n_r}\). Every configuration enters either the zero fixed state or a primitive three-cycle after **at most four updates**. Consequently, no other least periods occur. The maximum first-entry time is **three** when every part is a singleton, and **four** otherwise; both bounds are attained.

The exact periodic-state count is given by an explicit seven-support sum. For nonempty sets \(S_i\subseteq\{0,1,2\}\), put
\[
\omega_m(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}|T|^m,
\quad
\chi(S_1,\ldots,S_r)=\prod_{i=1}^{r}\prod_{c\in S_i}
\mathbf{1}\{\exists j\ne i:\ (c+1)\bmod 3\in S_j\}.
\]
Then the number of configurations lying on periodic orbits is exactly
\[
P(n_1,\ldots,n_r)=1+\sum_{\substack{\varnothing\ne S_i\subseteq\{0,1,2\}\\1\le i\le r}}
\chi(S_1,\ldots,S_r)\prod_{i=1}^{r}\omega_{n_i}(S_i).
\]
There is exactly one fixed point and \((P-1)/3\) primitive three-cycles; the Artin–Mazur zeta function is
\[
\zeta(z)=(1-z)^{-1}(1-z^3)^{-(P-1)/3}.
\]
For example, the periodic-state counts for \(K_{1,1,1}\), \(K_{2,1,1}\), \(K_{1,2,3}\), and \(K_{2,2,2}\) are respectively \(7,19,199,271\).

## Assumptions and scope

Each vertex has one of three states, resting \(0\), excited \(1\), or refractory \(2\). In one simultaneous update, \(1\mapsto2\), \(2\mapsto0\), and a resting vertex becomes excited exactly if some neighbor is excited, remaining resting otherwise. There are no loops or edges within a part, and every pair of distinct parts is joined completely. Configurations are labelled by their vertices; no quotient by graph automorphisms is taken. The first-entry time \(\tau(x)\) is the smallest nonnegative integer \(t\) for which \(F^t(x)\) belongs to a periodic orbit. Periodic-state counts include individual configurations, not merely orbits.

## Proof

**1. Exact finite reduction for the all-size transient theorem.** Record for part \(i\) only its nonempty color-support \(S_i\subseteq\{0,1,2\}\). Its updated support is determined by \(S_i\) and by whether some *other* part contains color \(1\): replace each occurrence of \(1\) by \(2\), each \(2\) by \(0\), and each \(0\) by \(1\) when an excited vertex occurs outside the part, otherwise by \(0\). Therefore parts with identical supports evolve with identical supports indefinitely, regardless of the sizes of those parts. Their multiplicity matters only as \(0\), \(1\), or **at least two**, because the excitation predicate at a part requires the existence of another part containing \(1\). Distinct support classes do not merge ambiguously: after each step one simply recounts the seven nonempty possible supports, keeping counts capped at two. This gives a genuine factor map from every multipartite system, of every size, onto a fixed finite directed transition system. We retain the original color of each individual vertex in parallel, so equal-support parts evolve identically at support level even if their within-part multiplicities differ.

There are exactly \(2158\) realizable capped-count patterns with at least three parts. Representatives use zero, one, or three copies of each of the seven supports, where three denotes an arbitrary count of at least two; for the representative, include one vertex of each present color in every part. The accompanying `verify.py` enumerates **all** patterns with three or more parts and verifies, by exact integer/Boolean operations, that the fourth and seventh images agree:
\[
F^7(x)=F^4(x),
\]
and that the fourth image is either all-zero or advances under the cyclic recoloring \(\rho(c)=(c+1)\bmod3\). It also checks directly, for every representative, that the first periodic-entry time is at most four and that the only periods are one and three. Since color-support evolution commutes with the reduction and the per-vertex update depends only on that support data, the finite exhaustive certificate applies to every original graph and every original microconfiguration. It is a complete finite proof certificate for the universal assertion, **not** sampling of graph sizes.

For completeness, the certificate groups its \(2158\) reduced patterns by (entry time, eventual least period) as
`(0,1):1; (0,3):1969; (1,1):19; (1,3):38; (2,1):21; (2,3):42; (3,1):19; (3,3):42; (4,1):3; (4,3):4`.
The executable specifies its entire enumeration and the transition rule and uses no external libraries.

**2. Sharp entry-time bounds.** When all parts are singletons, the graph is complete, and the same finite certificate restricted to supports \(\{0\},\{1\},\{2\}\) proves that every first-entry time is at most three. Placing one excited vertex and all other vertices in state zero yields first-entry time exactly three. If any part contains at least two vertices, place one vertex in state one and every other vertex in state zero. At time one the vertices outside its part are excited; at time two a different vertex inside its part is excited; at time three this second vertex is refractory while the others are resting; at time four all vertices are resting. These four distinct successive transient stages give first-entry time four.

**3. Periodic-state characterization.** The finite certificate proves that every nonzero periodic configuration belongs to a cycle of length three on which **all** vertex colors advance by one modulo three at each update. A support tuple permits this advance indefinitely exactly when for every vertex of initial color \(c\), there exists an adjacent vertex of initial color \((c+1)\bmod3\): the requirement is needed when that vertex next enters the resting phase. Equivalently, the displayed indicator \(\chi\) equals one. The certificate additionally checks this equivalence for all capped patterns, so it does not assume that a single recoloring step implies periodicity. The other periodic configuration is uniquely all-zero.

**4. Exact enumeration.** For one part of size \(m\), inclusion–exclusion gives \(\omega_m(S)\) assignments whose color support is exactly \(S\). Supports in different parts are independent; multiplying these counts and summing over tuples with \(\chi=1\) counts every nonzero periodic state exactly once. Every such state is in a primitive length-three orbit because the global recoloring changes the color at every vertex. This yields the orbit count and zeta expression.

## Verification

Run `python3 verify.py` with the standard Python library. The deterministic verifier exhausts all \(2158\) capped support patterns, verifies the time-seven/time-four identity, validates the full periodic-support criterion and counts the exact depth/period classes. It separately enumerates all \(2862\) labelled microconfigurations across eight named multipartite graphs, comparing the exact support count with direct trajectory enumeration and checking the sharp cutoff. The encoded tripartite polynomial is also cross-checked. Success prints `VERIFY_OK` and the complete finite evidence summary. The checker itself is the self-contained finite certificate underlying the general reduction; its precise domain and assumptions are stated above. Untested non-multipartite graphs and higher-state rules are not covered.

## Relationship to prior work

Durrett–Griffeath (1993) treats asymptotic patterns in excitable lattice dynamics. Gravner–Lyu–Sivakoff (2016), especially their Theorem 3, gives a general criterion for synchronization and excitation activity on arbitrary graphs. Doba (2018), especially Sections 3, 6, and 7, analyzes eventual fixed and periodic behavior and excitation rates for deterministic Greenberg–Hastings dynamics on arbitrary finite connected graphs. Those results motivate the question and give broader qualitative information; the present claim is the exact **uniform first-entry cutoff** and a complete **labelled periodic-state and orbit census** for every multipartite graph with at least three parts. Neither a general convergence theorem nor a rate criterion by itself supplies the displayed support enumerator.

## Limitations

This result does not count entire attraction basins by first-entry time, nor give an analogous result for bipartite graphs (which can have primitive four-cycles), arbitrary nonmultipartite graphs, or more than three states. Its all-size transient theorem depends on a fully specified **finite exhaustive quotient certificate**, rather than a handwritten enumeration of 2158 individual cases. Historical-priority assessment is necessarily limited by indexing and access to prior work; a specialized equivalent result in uninspected material remains possible. The result is not an independent certification.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first posted 1993-03-22), https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016), especially Section 2 and Theorem 3, https://arxiv.org/html/1610.07320v1.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, doi:10.25088/ComplexSystems.27.2.101, https://content.wolfram.com/sites/13/2018/09/27-2-1.pdf.
