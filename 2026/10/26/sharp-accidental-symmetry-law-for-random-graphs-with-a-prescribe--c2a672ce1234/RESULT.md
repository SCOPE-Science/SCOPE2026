# Sharp accidental-symmetry law for random graphs with a prescribed free involution

## Finding

Let \(f\) be a fixed-point-free involution on \(2m\) vertices, and choose \(G_m\) uniformly among undirected simple graphs for which \(f\) is an automorphism. Write \(\operatorname{Aut}(G_m,f)\) for automorphisms preserving both the graph and the named involution. The probability of any automorphism beyond the forced two-element group has the sharp asymptotic
\[
\Pr\bigl(\operatorname{Aut}(G_m,f)\ne\langle f\rangle\bigr)
= m2^{-(m-1)}(1+o(1)).
\]
There is also an exact, samplewise kernel theorem: the subgroup fixing each orbit of \(f\) setwise is \((C_2)^{c(H_m)}\), where \(H_m\) is an explicitly defined independent-edge random graph \(G(m,1/2)\). Almost all excess symmetry at the displayed exponential scale arises from one isolated vertex of \(H_m\).

## Assumptions and scope

For each integer \(m\ge2\), the domain is \(\{(i,b):1\le i\le m,\ b\in\{0,1\}\}\), with \(f(i,b)=(i,1-b)\). A graph is a symmetric, irreflexive binary relation; \(f\) is named as a unary function. The sample space consists of all graphs whose edges are preserved by \(f\), with equal probability. This is not a sample of graphs with automorphism group *exactly* \(\langle f\rangle\), nor an unconditioned Erdős–Rényi graph. The symmetry group in the claim preserves the named function; graph automorphisms not commuting with \(f\) are outside its scope.

Within the \(i\)-th orbit, one independent fair bit decides the edge \(\{(i,0),(i,1)\}\). For distinct \(i,j\), independent fair bits \(A_{ij},B_{ij}\) respectively control the two parallel edges \(\{(i,0),(j,0)\},\{(i,1),(j,1)\}\) and two crossed edges \(\{(i,0),(j,1)\},\{(i,1),(j,0)\}\). Consequently all \(m^2\) edge-orbit bits are jointly independent and unbiased. Put \(ij\in E(H_m)\) precisely when \(A_{ij}\ne B_{ij}\). The indicators are independent fair bits, hence \(H_m\) has law \(G(m,1/2)\).

## Proof

**Exact fibre kernel.** Any permutation commuting with \(f\) has a unique expression as a permutation \(\sigma\in S_m\) of its two-point orbits followed by a specified independent flip \(\varepsilon_i\in\{0,1\}\) on each orbit. For \(\sigma=\operatorname{id}\), the flip at \(i\) preserves every edge to the orbit \(j\) unless \(\varepsilon_i\ne\varepsilon_j\), in which case preservation requires \(A_{ij}=B_{ij}\). Thus \(\varepsilon_i=\varepsilon_j\) on every edge of \(H_m\), and there is no constraint on within-orbit edges. Such flips are exactly the indicator functions constant on connected components of \(H_m\), forming a group of order \(2^{c(H_m)}\). The global all-orbits flip equals \(f\), so this kernel equals \(\langle f\rangle\) if and only if \(H_m\) is connected.

**Orbit-permuting symmetries are negligible.** We bound the probability that there is an automorphism with nonidentity orbit permutation \(\sigma\). Let \(k\ge2\) be its support size and \(t=m-k\) the number of fixed orbit indices. Fix \(\sigma\) and a flip vector \(\varepsilon\). Independently across unordered pairs \(\{i,j\}\), the vector \((A_{ij},B_{ij})\) is uniform on four values. When \(\sigma\) acts on these unordered pairs, an orbit of length \(L\) forces at least \(L-1\) identifications of the four-valued vectors (allowing swaps of their coordinates), giving probability at most \(4^{-(L-1)}\).

When \(2\le k\le m/2\), for each of the \(t\) fixed indices, the \(k\) index-pairs connecting it to the moved indices form cycles of lengths at least two; they therefore impose a factor of at most \(4^{-k/2}=2^{-k}\) per fixed index. These constraints are disjoint across fixed indices. For the edges joining two fixed indices, writing \(s\) for the number of flipped fixed indices, an extra factor \(2^{-s(t-s)}\) is necessary: each edge between opposite flip statuses must satisfy equality of its independent parallel and crossed bits. Sum over the choices of flip statuses on fixed indices; for \(t\ge2\),
\[
\sum_{s=0}^{t}\binom ts2^{-s(t-s)}
\le 2+(2^t-2)2^{-(t-1)}<4.
\]
There are \(2^k\) choices of flips on moved indices and at most \(m^k\) permutations with support \(k\). Consequently this contribution is at most
\[
4\sum_{k=2}^{\lfloor m/2\rfloor}(2m)^k2^{-k(m-k)}
=o\bigl(m2^{-(m-1)}\bigr).
\]
Indeed its \(k=2\) term is \(O(m^2 2^{-2m})\), while all remaining terms decay at least exponentially faster than \(2^{-m}\) after the polynomial factors.

For \(k>m/2\), among the \(N=\binom m2\) unordered pairs at most \(\binom{m-k}{2}+k/2\) are fixed by \(\sigma\): a fixed pair consists either of two fixed indices or of one two-cycle. Therefore at least \(k(2m-k-2)/2\) pair-indices are moved, and the number \(N-\#\text{orbits}\) is at least half this number. For any fixed flip vector the probability of preserving all such four-valued bits is thus at most \(2^{-k(2m-k-2)/2}\). Uniformly for \(k>m/2\) and large \(m\), it is at most \(2^{-m(m-2)/4}\). Summing crudely over at most \(m!2^m\) permutation-and-flip pairs gives \(2^{-\Omega(m^2)}\). This proves
\[
\Pr(\exists\text{ an orbit-permuting automorphism})=o\bigl(m2^{-(m-1)}\bigr).
\]

**Connectivity asymptotics and cause.** In \(H_m\sim G(m,1/2)\), a specified isolated vertex has probability \(2^{-(m-1)}\). The union of the \(m\) possible isolated-vertex events has probability \(m2^{-(m-1)}+O(m^22^{-2m})\), by the first two Bonferroni inequalities. To be disconnected without an isolated vertex, there must be a component of size \(s\) for some \(2\le s\le m/2\). For each specified \(s\)-subset, the probability of no edges to its complement is \(2^{-s(m-s)}\); summing over all subsets yields
\[
\Pr(H_m\text{ disconnected and no isolated vertex})\le
\sum_{s=2}^{\lfloor m/2\rfloor}\binom ms2^{-s(m-s)}
=o\bigl(m2^{-(m-1)}\bigr).
\]
Thus \(\Pr(H_m\text{ disconnected})\sim m2^{-(m-1)}\). By the exact kernel theorem and the negligible orbit-permutation probability, the main asymptotic follows. More precisely the probability that the only extra symmetry is a flip of an isolated two-point orbit (in addition to \(f\)) is \(m2^{-(m-1)}(1+o(1))\); multiple isolations are of lower order.

## Verification

A standard-library checker in `check_involution_graph.py` independently enumerates every admissible labelled graph for \(m=2,3,4\), computes all permutations commuting with the fixed involution, and verifies that the fibrewise kernel size is exactly \(2^{c(H_m)}\). It also checks the occurrence of extra automorphisms and the finite isolated-fibre events. Its reproducible success line is `PAIRED_GRAPH_AUT_EXACT_OK 25190528 flip_laws 45`. Finite enumeration corroborates exact identities only; the asymptotic error bounds above are proved by the union bounds, not extrapolation.

## Relationship to prior work

The 2026 study by Xia, Zhang and Zheng proves small automorphism groups for *standard double covers of abelian Cayley graphs*, where both Cayley structure and a different edge model impose strong constraints. The present random symmetric relational model has independent parallel and crossed edge bits and arbitrary base-label permutations, so the source result does not imply its fibre-kernel identity or sharp error constant. General results on asymmetry of unconditioned dense random graphs do not transfer the sharp conditional probability. Koponen's recent paper motivates studying finite-model expansions, but its finite-model-property results do not assert this probability law. The elementary reduction to connectivity of \(G(m,1/2)\) for the exact fibre kernel is made explicit here and the orbit-permutation contribution is bounded quantitatively.

## Limitations

The group is the automorphism group of the *expanded* relational structure containing the named involution. Nothing is asserted about automorphisms of the unmarked graph that fail to commute with \(f\), or about other edge densities, several commuting symmetries, or nonuniform graph measures. The leading constant applies as the number of two-point orbits tends to infinity. Full historical priority among specialized random graph cover and permutation-group results remains an open bibliographic risk; an independent scientific audit has not been performed.

## References

1. V. Koponen, *A characterization of the finite model property for ω-categorical theories*, arXiv:2610.16163, first publicly available 2026-10-12.
2. B. Xia, Z. Zhang, and S. Zheng, *Almost all standard double covers of abelian Cayley graphs have smallest possible automorphism groups*, arXiv:2601.20214 (2026).
3. J. H. Kim, B. Sudakov, and V. Vu, *On the asymmetry of random regular graphs and random graphs*, Random Structures & Algorithms (2002), for contrasting unconditioned random-graph symmetry results.
