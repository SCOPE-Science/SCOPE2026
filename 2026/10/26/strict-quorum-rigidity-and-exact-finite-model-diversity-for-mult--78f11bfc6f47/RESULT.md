# Strict-quorum rigidity and exact finite-model diversity for multiple successor orders

## Finding

Fix integers \(r\ge 2\), \(\lfloor r/2\rfloor<q\le r\), and \(n\ge1\). Interpret each of the \(r\) binary relations \(S_1,\ldots,S_r\) on a common \(n\)-element labelled domain as the exact successor relation of a finite linear order. Require the **quorum condition**: each directed pair belonging to at least one \(S_i\) belongs to at least \(q\) of them. For fixed \(r,q\), this is a universal sentence of two-variable first-order logic, namely

\[
\forall x\,\forall y\left(\left(\bigvee_{i=1}^r S_i(x,y)\right)\to
\bigvee_{\substack{I\subseteq\{1,\ldots,r\}\\|I|=q}}\bigwedge_{i\in I}S_i(x,y)\right).
\]

**Classification.** Every such ordered \(r\)-tuple consists either of one repeated linear order or of linear orders obtained by cutting a **single directed Hamiltonian cycle**, with no cycle arc cut by more than \(c=r-q\) of the \(r\) orders. Conversely every tuple of either form satisfies the quorum condition. In particular, every two distinct orders in a qualifying tuple differ by exactly one deleted successor arc and one inserted successor arc; equivalently their symmetric-difference size is \(2\).

**Exact census.** Let \(T_{n,r,q}\) count qualifying ordered tuples of successor relations on the labelled domain, and set \(E_c(z)=\sum_{j=0}^{c}z^j/j!\). Then, for all \(n\ge1\),

\[
T_{n,r,q}=n!+(n-1)!\,r!\,[z^r]E_c(z)^n.
\]

Exactly \(n!\) tuples have one distinct order. For \(2\le s\le\min(n,r)\), the number with exactly \(s\) distinct orders is

\[
T_{n,r,q}^{(s)}=(n-1)!\binom ns r! [z^r]\left(\sum_{j=1}^{c}\frac{z^j}{j!}\right)^s.
\]

If \(c=0\), only repeated orders occur. If \(c\ge1\), the nonzero diversity values other than \(1\) are **exactly** the integers \(s\) satisfying \(\lceil r/c\rceil\le s\le\min(n,r)\); thus no qualifying tuple has exactly two distinct orders. Nonidentical tuples exist precisely when \(n\ge\lceil r/c\rceil\). For three orders at quorum two, the closed count simplifies to

\[
T_{n,3,2}=n!\bigl(1+(n-1)(n-2)\bigr).
\]

The strict-majority hypothesis is sharp: at any lower quorum \(q\le r/2\) and with at least three worlds, qualifying tuples need not be common cuts of a cycle.

## Assumptions and scope

The domain is nonempty, finite, labelled, and of size \(n\). Each successor relation is a directed spanning path with \(n-1\) arcs, oriented from first to last in its underlying linear order. Relations are named and tuples are ordered; no quotient by vertex relabelling, relation permutations or cyclic rotation is taken. A directed Hamiltonian cycle is an oriented cycle through every vertex. When \(n=1\), the unique tuple has empty successor relations; the cyclic part of the census is zero because its coefficient vanishes. All claims count interpretations of the successor symbols alone, without additional predicates.

## Proof

**Quorum forces unique local adjacency.** Let \(U=\bigcup_i S_i\). If \(U\) had two different outgoing arcs \((a,b)\) and \((a,d)\) from one vertex, their supporter sets \(\{i:(a,b)\in S_i\}\) and \(\{i:(a,d)\in S_i\}\) would be disjoint: a successor of a linear order has at most one outgoing arc per vertex. The quorum condition gives at least \(q\) indices in each set, contradicting \(2q>r\). The same argument with incoming arcs shows that every vertex has indegree and outdegree at most one in \(U\).

**Only a path or its closure.** Select \(S_1\), which spans the domain as a directed path \(a_1\to a_2\to\cdots\to a_n\). Its internal vertices have the full allowable indegree and outdegree in \(U\). Consequently the only possible additional arc of \(U\) is \(a_n\to a_1\), so \(U\) is either exactly this path or its directed cyclic closure. In the first case, each \(S_i\) is a spanning path contained in \(U\), necessarily \(S_1\), proving that every order coincides. For \(n=1\), loops cannot be successor arcs, and the same conclusion holds.

If \(U\) is the directed cycle, every \(S_i\) is obtained by deleting exactly one cycle arc: a spanning path contained in a directed cycle must omit exactly one arc. The set of cycles is uniquely determined by \(U\). For any cycle arc \(e\), its supporter count is \(r-m_e\), where \(m_e\) is the number of component orders deleting \(e\). Thus the quorum condition is equivalent to \(m_e\le c=r-q\), proving both necessity and sufficiency. If two paths delete different arcs \(e\) and \(f\), the sets of arcs differ exactly in those two arcs, so the pairwise symmetric difference has size \(2\).

**Counting.** Repeated orders contribute exactly \(n!\). For \(n\ge2\), there are \((n-1)!\) labelled directed Hamiltonian cycles. For a fixed cycle, choosing an ordered tuple of deleted arcs means placing \(r\) labelled occurrences into its \(n\) arc-cells. With occupancy at most \(c\), the exponential formula for labelled allocations gives \(r![z^r]E_c(z)^n\). These tuples are not repeated orders (every repeated omission would have count \(r>c\)); furthermore their union recovers the parent cycle, so different parent cycles cannot lead to double counting. This proves the total census. Requiring exactly \(s\) positive cells amounts to choosing \(s\) of the \(n\) cycle arcs, then allocating between \(1\) and \(c\) omissions to each, proving the diversity formula.

Such a positive allocation exists exactly when \(s\le r\le sc\), hence \(\lceil r/c\rceil\le s\le\min(n,r)\). Because \(c<r/2\), the lower bound on \(s\) is at least three. Setting \((r,q,c)=(3,2,1)\) leaves \((n)_3\) injective choices of cut arcs and gives the displayed special case.

**Sharpness of the quorum.** For every \(r\ge2q\), take \(q\) copies of the order \((2,1,3)\) and \(r-q\) copies of \((1,2,3)\). Every arc in their union is used at least \(q\) times, yet the union has two outgoing arcs at vertices \(1\) and \(2\), so it is neither a directed path nor a directed Hamiltonian cycle. For a larger domain, append vertices \(4,5,\ldots,n\) identically to both orders. Thus the strict inequality \(2q>r\) cannot be weakened.

## Verification

The standalone `checker.py` verifies the census and exactly-distinct-order coefficients by exhaustive independent enumeration of ordered linear-order tuples for \((n,r,q)=(2,3,2),(3,3,2),(4,3,2),(5,3,2),(3,4,3),(4,4,3),(3,5,3),(4,3,3)\). The observed totals are respectively \(2,18,168,1560,6,168,186,24\). The checker also tests explicit boundary-quorum counterexamples for \(2\le r\le8\). Execute `python checker.py` using Python 3.9 or newer. The finite computations independently corroborate the formulas; the proof for all \(n,r,q\) is the structural argument above.

## Relationship to prior work

Michaliszyn and Witkowski (2026), *Two-Variable Logic with Arbitrarily Many Successor Relations*, study unrestricted satisfiability and a finite-model **disagreement budget**. Their Section 7 characterizes low-cost models by common consecutive blocks and includes an example of three cyclically permuted blocks. This supplies a relevant antecedent, but its budget condition neither imposes strict quorum on every arc nor states the complete common-cycle classification, exact labelled model counts or the diversity spectrum here. Jeż, Michaliszyn and Witkowski (2026), *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, settle the unrestricted finite satisfiability problem using local profiles and signed counting. Their counting objects are profile realizations for arbitrary input formulas, not the stated closed enumeration of strict-quorum successor tuples. The elementary path/cycle and labelled-allocation identities used in the proof are standard and are not claimed independently as innovations. The proposed contribution is their exact joint application to the strict-quorum two-variable successor constraint, especially its all-parameter diversity spectrum and sharp majority boundary.

## Limitations

No claim is made about the complexity of unrestricted two-variable satisfiability, about models with infinite orders, or about arbitrary low-quorum families. The finite enumeration is for named successor predicates on a labelled domain. The exact theorem does not imply an analogous classification for unbounded-degree binary relations. An equivalent majority-adjacency aggregation result might exist under permutation-consensus terminology; checking older specialized literature remains a priority concern. This is a mathematical proof and a finite computational cross-check, not an independently audited result.

## References

1. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1, first posted 7 October 2026. https://arxiv.org/html/2610.09758v1
2. A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943, first posted 14 October 2026. https://arxiv.org/abs/2610.19943
