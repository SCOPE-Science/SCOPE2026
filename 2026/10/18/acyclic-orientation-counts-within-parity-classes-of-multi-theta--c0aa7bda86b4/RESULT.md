# Acyclic orientation counts within parity classes of multi-theta graphs

## Finding

Let \(m\geq 3\), and let \(G\) be the simple graph formed from two distinct terminals by \(m\) internally vertex-disjoint paths of edge-lengths \(\ell_1,\ldots,\ell_m\geq 2\). An orientation \(\omega\) has **indegree-parity signature** \(\sigma(\omega)=(\deg^-_\omega(v)\bmod 2)_{v\in V(G)}\). For each feasible signature \(\sigma\), let \(a(\sigma)\) be the number of **acyclic** orientations with that signature, and put
\[
 \mathcal A_G(z)=\sum_{\sigma\text{ feasible}}z^{a(\sigma)}.
\]
This polynomial records *how many signatures admit exactly a specified number of acyclic orientations*, including those admitting none.

Write \([m]=\{1,\ldots,m\}\), \(w_i=2^{\ell_i-1}-1\), and for a proper subset \(S\subsetneq[m]\) define
\[
 B_S=2\prod_{i\notin S}w_i,\qquad
 h_m(r)=\begin{cases}2^{m-1},&r=0,1,\\2^{m-r},&2\leq r\leq m-1.\end{cases}
\]
**Theorem.** For every choice of the stated parameters,
\[
 \boxed{\mathcal A_G(z)=\sum_{S\subsetneq[m]}B_S z^{h_m(|S|)}+
 \begin{cases}2z,&m\text{ odd},\\1+z^2,&m\text{ even}.\end{cases}}
\]
Each feasible signature has exactly \(2^{m-1}\) realizing orientations. Every feasible signature has an acyclic representative if \(m\) is odd. If \(m\) is even, **exactly one feasible signature has no acyclic representative:** the all-odd indegree signature. It is the familiar no-source obstruction, not an independent new obstruction.

In the complete bipartite specialization \(G=K_{2,m}\), all \(w_i=1\), and
\[
 \mathcal A_{K_{2,m}}(z)=2\sum_{r=0}^{m-1}\binom mr z^{h_m(r)}+
 \begin{cases}2z,&m\text{ odd},\\1+z^2,&m\text{ even}.\end{cases}
\]
The total number of acyclic orientations, recovered by \(\mathcal A'_G(1)\), is
\[
 2\prod_{i=1}^m(2^{\ell_i}-1)-\prod_{i=1}^m(2^{\ell_i}-2).
\]
This last total-count identity also follows from elementary inclusion–exclusion; the main statement is the finer *signature-by-signature distribution*.

## Assumptions and scope

Graphs are finite, simple and undirected before orienting. The path interiors are pairwise disjoint and contain no additional edges. All \(m\geq3\) paths have length at least two, so the construction has no parallel edge. The two terminals are distinct. The feasible signatures are exactly those satisfying the necessary global parity equation
\[
 \sum_{v\in V(G)}\sigma(v)\equiv |E(G)|\pmod2.
\]
There are \(2^{|V(G)|-1}=2^{\sum_i\ell_i-m+1}\) such signatures. Orientations are distinguished by their directions on the **labelled** edges; no quotient by graph automorphisms is used. The polynomial includes the term \(z^0\) for signatures with no acyclic realization.

## Proof

**1. Parity fibers.** Fix a reference orientation, and encode an orientation by the edge set whose directions differ from it. Two orientations have equal indegree parity exactly when their difference has even degree at every vertex: the difference is an element of the binary cycle space. Along a path, each internal vertex has degree two, so evenness forces either both incident edges to be flipped or neither. Hence an entire path is flipped or it is not. At the terminals the number of completely flipped paths must be even. Consequently, each parity fiber consists exactly of the \(2^{m-1}\) orientations obtained by reversing an even number of the \(m\) whole paths. This also proves the global-parity feasibility claim, since there are \(2^{|E(G)|}/2^{m-1}\) fibers.

**2. Coherence is a fiber invariant.** Call a path *coherent* if every edge points from the first terminal to the second, or every edge points in the reverse direction. Full reversal of a path preserves its coherence status. Thus the subset \(S\subseteq[m]\) of coherent paths is fixed within each parity fiber. Every simple cycle in \(G\) is the union of two distinct terminal-to-terminal paths. It is directed precisely when both constituent paths are coherent and point in opposite directions. Therefore an orientation is acyclic if and only if all its coherent paths, if any, point in the same direction.

**3. Fibers with at least one incoherent path.** Fix \(S\subsetneq[m]\) with \(r=|S|\). Each coherent path has two possible directions; every path outside \(S\) has exactly \(2^{\ell_i}-2\) noncoherent orientations. There are therefore
\[
 2^r\prod_{i\notin S}(2^{\ell_i}-2)
\]
orientations with coherence set exactly \(S\). Dividing by the common fiber size \(2^{m-1}\) yields
\[
 \frac{2^r\prod_{i\notin S}(2^{\ell_i}-2)}{2^{m-1}}
 =2\prod_{i\notin S}(2^{\ell_i-1}-1)=B_S
\]
distinct parity signatures.

Because at least one path is incoherent, any prescribed reversal pattern of the \(r\) coherent paths can be completed to an even-cardinality whole-path reversal by possibly reversing one incoherent path. Thus, in any such fiber, each of the \(2^r\) coherent-direction patterns occurs exactly \(2^{m-1-r}\) times. If \(r=0\) or \(1\), all fiber orientations are acyclic, and \(a(\sigma)=2^{m-1}\). If \(2\le r<m\), exactly the two monochromatic direction patterns avoid a directed cycle, so
\[
 a(\sigma)=2\cdot2^{m-1-r}=2^{m-r}.
\]
These are the terms indexed by proper subsets \(S\).

**4. Fully coherent paths.** When all paths are coherent, the \(2^m\) orientations form two parity fibers, distinguished by the parity of the number of paths directed backward. The only acyclic orientations are the two constant-direction assignments. If \(m\) is odd, these lie in different fibers, giving one acyclic orientation in each, hence \(2z\). If \(m\) is even, they lie in the same fiber, which therefore has two acyclic realizations; the other fiber has zero, giving \(1+z^2\). In the even case every internal vertex is odd-indegree in both fully coherent fibers, and the terminal indegrees in the all-cyclic fiber are odd as well. That fiber is exactly the all-odd signature, which has no possible source.

Combining Steps 3 and 4 proves the polynomial and the feasibility statements. For \(\ell_i=2\), the graph is \(K_{2,m}\) and \(w_i=1\), yielding the binomial specialization. Finally, counting acyclic orientations directly as the union of two events — no terminal-to-terminal coherent path in the forward direction, or none in the backward direction — gives the stated global count by inclusion–exclusion.

## Verification

The standalone Python script `verify.py` independently enumerates all directed choices of every edge, obtains indegree-parity signatures from edge directions, tests acyclicity by Kahn's topological-sort algorithm, groups orientations by signature, and compares the resulting multiplicity distribution with the theorem. It checks 30 graph instances (multiple path-length patterns with three through eight paths), enumerating 159168 labelled orientations in total, and validates the number of feasible signatures. The script prints `PASS` only if every exact comparison succeeds. The general theorem does not rest on these finite checks.

## Relationship to prior work

Gravier, Petiteau and Sivignon (2026) pose acyclic orientations with prescribed indegree parity and study necessary conditions and graphs including Cartesian products of paths and cycles. Their March 2026 work supplies the motivating question, but its inspected sections and results do not provide the distribution of the number of acyclic representatives of each parity signature for multi-theta graphs.

Király and Kisfaludi-Bak (2014) give general existence equivalences for all non-full signatures via dual-critical and super-dual-critical graphs. Existence alone, including some cases of the parity-feasibility corollary here, is not claimed as the new contribution. Their structural equivalences do not give the explicit \(\mathcal A_G(z)\) multiplicity spectrum.

A related study of indegree-parity rigidity on cactus graphs concerns whether a parity fiber is wholly cyclic or wholly acyclic. Multi-theta graphs, which have overlapping cycles, are outside that graph class; the present result determines the exact mixture and its multiplicities instead. Mühlherr and Poullot (2026) directly study multipaths and introduce an acyclic polynomial, but their exponent is the number of edge directions disagreeing with a reference orientation; their parity obstruction is **edge-disagreement parity**, not the vector of vertex indegree parities. Their multipath Hamiltonicity results therefore do not determine the number of acyclic orientations inside each indegree-parity fiber. No definitive literature-priority assertion is made.

## Limitations

The statement applies only to two-terminal multi-theta graphs with internally disjoint paths, length at least two, and at least three paths. It does not characterize parity spectra of arbitrary series-parallel graphs. The computation is finite verification only; the proof above establishes all allowed parameters. The source comparison is not an exhaustive guarantee of novelty. No independent mathematical audit has been performed.

## References

- S. Gravier, M. Petiteau and I. Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475v1, first posted 10 March 2026. https://arxiv.org/abs/2603.09475
- Z. Király and S. Kisfaludi-Bak, *Notes on dual-critical graphs*, arXiv:1410.1653v1 (2014). https://arxiv.org/abs/1410.1653
- L. Mühlherr and G. Poullot, *Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*, arXiv:2609.02249v1, first posted 2 September 2026. https://arxiv.org/abs/2609.02249
- The EGRES Open problem, *Acyclic orientation with parity constraints*. https://lemon.cs.elte.hu/egres/open/Acyclic_orientation_with_parity_constraints
