# Exact enumeration of weight-one-or-two binary universal cycles

## Finding

For each integer \(k\ge 3\), let \(\mathcal L_k\) be the set of all length-\(k\) binary words with Hamming weight either \(1\) or \(2\). A universal cycle for \(\mathcal L_k\) is a cyclic binary word whose consecutive length-\(k\) circular factors are exactly the members of \(\mathcal L_k\), each appearing once. Two cycles differing by rotation are identified; reversal and complementation are not identified.

**Theorem.** The number of universal cycles for \(\mathcal L_k\) is
\[
N_k=2^{\lfloor(k-1)/2\rfloor} \qquad(k\ge3).
\]
Every such cycle has length \(k+\binom{k}{2}=k(k+1)/2\). The theorem supplies a complete parametrization via \(\lfloor(k-1)/2\rfloor\) independent binary choices in rooted directed spanning trees of the associated de Bruijn graph.

The counts for \(k=3,4,5,6,7,8,9,10\) are \(2,2,4,4,8,8,16,16\), respectively. For example, `100101000110000` is a universal cycle when \(k=5\).

## Assumptions and scope

Only ordinary binary contiguous *circular* factors are counted, including wraparound. The required factors all have the same length \(k\); they are not arbitrary superstring targets, subsequences, or a single-weight language. Universality requires every weight-one and weight-two factor exactly once and forbids other length-\(k\) windows. The unrooted equivalence relation is rotation only.

## Proof

Put \(s=k-1\). Construct the directed overlap graph \(G_k\) with one edge for each member of \(\mathcal L_k\), running from its length-\(s\) prefix to its length-\(s\) suffix. Vertices are precisely binary length-\(s\) strings with zero, one, or two ones. They all have positive indegree and outdegree. The zero vertex \(o=0^s\) has indegree and outdegree one, as does every two-one vertex. Each one-one vertex has indegree and outdegree two. In particular the graph is balanced. The sole edge leaving \(o\) is the length-\(k\) word \(0^s1\).

Let \(t_o\) denote the number of directed spanning in-arborescences rooted at \(o\) (every other vertex selects exactly one outgoing edge, and its selected directed path eventually reaches \(o\)). At two-one vertices the outgoing choice is forced: append zero, shift left, and discard the leading bit. Hence any such tree is determined solely by the outgoing choices at the \(s\) one-one vertices. Write \(e_j\), \(0\le j<s\), for the vertex having its unique one in binary position \(j\) counted *from the right*, so the update on appending a bit is \(v\mapsto (2v+b)\bmod 2^s\).

At \(e_j\), choosing the append-zero edge moves to \(e_{j+1}\) when \(j<s-1\), and to the root \(o\) when \(j=s-1\). Choosing append-one first creates a vertex of weight two unless \(j=s-1\); following its *forced* append-zero edges then reaches \(e_{s-1-j}\). Indeed the old one exits the size-\(s\) window after exactly \(s-1-j\) left shifts following its insertion, while the newly appended one has then moved into binary position \(s-1-j\). Therefore, after contracting forced weight-two paths, the index transitions are
\[
 j\longmapsto\begin{cases}
 j+1,&\text{append zero and }j<s-1,\\
 \ast,&\text{append zero and }j=s-1,\\
 s-1-j,&\text{append one},
 \end{cases}
\]
where \(\ast\) is the root. This contraction preserves the existence of directed cycles and reachability of the root.

Set \(m=\lfloor s/2\rfloor\). If append-one is selected only at indices \(j<m\), then every transition among indexed vertices strictly increases: both \(j+1>j\) and \(s-1-j>j\) for \(j<m\). Every trajectory therefore reaches \(\ast\). These choices are completely independent, giving \(2^m\) arborescences.

Conversely suppose an append-one selection is made at some index \(j\ge m\). Let \(h\) be the smallest such index and put \(r=s-1-h\), so \(r\le h\). If \(r=h\), the selection at \(h\) is a self-loop. Otherwise, every selected transition from a vertex with index \(i\in[r,h)\) strictly increases its index but stays at most \(h\): below \(m\), the jump \(s-1-i\) is at most \(s-1-r=h\); at indices at least \(m\) but below \(h\), minimality of \(h\) forces append zero. Thus the selected path starting at \(r\) reaches \(h\), whose append-one edge returns to \(r\). This creates a directed cycle and excludes a rooted in-arborescence. Consequently
\[
t_o=2^{\lfloor s/2\rfloor}=2^{\lfloor(k-1)/2\rfloor}.
\]

Since \(t_o>0\), every vertex has a directed route to \(o\). Balance then guarantees that \(G_k\) is Eulerian: each weak component is strongly connected, and all vertices lie in the one component of \(o\). (Equivalently, no proper source component can exist in a balanced finite digraph with all vertices able to reach \(o\).) By the directed BEST theorem, Euler circuits beginning with the fixed sole edge leaving \(o\) are counted by
\[
t_o\prod_{v\in V(G_k)}(d^+(v)-1)!=t_o,
\]
because every outdegree is either one or two. Each Euler circuit determines one required cyclic word and conversely. The edge \(0^s1\) appears exactly once in each circuit, so it canonically fixes rotation and there is no further division by the word length. This gives the stated formula.

## Verification

Run `python VERIFY.py` using Python 3 with no third-party dependencies. It reconstructs the whole labeled overlap graph and independently computes the in-arborescence count by an exact integer directed matrix-tree determinant for \(3\le k\le10\); a separate enumeration of outgoing-edge selectors verifies the complete high-index exclusion criterion on the same range. For \(3\le k\le8\), it additionally enumerates local Euler traversal orders without invoking BEST, reconstructs each resulting circular word, and checks that every required length-\(k\) factor appears once. This produced:

`VERIFY_OK matrix_tree_k=3..10 functional_tree_k=3..10 direct_euler_k=3..8`

These finite checks corroborate, but do not replace, the infinite argument above.

## Relationship to prior work

Ruskey, Sawada, and Williams introduced the fixed-weight **shorthand** de Bruijn-cycle construction in which words of weight \(w\) are represented by length-one-shorter factors having weight \(w-1\) or \(w\). Specializing to weight \(2\) produces *exactly* the present cycle language; their result establishes existence and constructs particular cycles but does not supply this all-order count of rotation classes. Sawada, Williams, and Wong later constructed universal cycles for general weight ranges by gluing, again addressing constructions rather than the total enumeration of all cycles. Sawada and Gabrić later gave uniform random arborescence sampling for weight-range cycles and explicitly considered the two-cycle \(k=3\) instance; this finite base case is not claimed new. They did not derive the present all-order formula. The classical BEST theorem and directed matrix-tree theorem supply general counting machinery, but the explicit binary choice classification and closed count require the special graph structure proved here.

## Limitations

This theorem does not enumerate cycles for weight ranges other than \(\{1,2\}\), nor does it count equivalence under reversal. It establishes mathematical correctness internally but has not undergone independent scientific review. Relevant literature was checked, but completeness of coverage in unindexed publications is not guaranteed.

## References

1. F. Ruskey, J. Sawada, and A. Williams, “De Bruijn Sequences for Fixed-Weight Binary Strings,” *SIAM Journal on Discrete Mathematics* 26 (2012), 605–617. DOI: 10.1137/100808782. First publicly verified online May 8, 2012.
2. J. Sawada, A. Williams, and D. Wong, “Universal Cycles for Weight-Range Binary Strings,” *Combinatorial Algorithms*, LNCS 8288 (2013), 388–401. DOI: 10.1007/978-3-642-45278-9_33.
3. J. Sawada and D. Gabrić, “Las Vegas Algorithms to Generate Universal Cycles and de Bruijn Sequences Uniformly at Random,” *RAIRO - Theoretical Informatics and Applications* 59 (2025), article 21. DOI: 10.1051/ita/2025019.
4. N. G. de Bruijn, T. van Aardenne-Ehrenfest, C. A. B. Smith, and W. T. Tutte: directed Euler-tour enumeration (BEST theorem); the classical directed matrix-tree theorem.
