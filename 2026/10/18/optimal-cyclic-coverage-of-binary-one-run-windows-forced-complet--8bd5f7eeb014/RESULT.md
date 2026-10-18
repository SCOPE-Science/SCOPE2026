# Optimal cyclic coverage of binary one-run windows: forced completion and exact multiplicity

## Finding
For every integer \(k\ge 2\), let \(\mathcal R_k\) be the binary length-\(k\) words in which the ones occupy at most one contiguous *linear* interval, including the all-zero word. A cyclic cover is a nonempty cyclic binary word in which every element of \(\mathcal R_k\) occurs as a length-\(k\) cyclic factor; the covering word itself is unrestricted. Let \(\mathcal C_k\) consist of binary words in which the ones occupy at most one *circular* interval, including both constant words.

**Theorem (sharp cover, forced window spectrum, and enumeration).** For every integer \(k\ge2\):

1. The shortest possible cyclic cover of \(\mathcal R_k\) has exactly \(k^2-k+2\) positions. Equivalently, its repetition overhead beyond the \(1+k(k+1)/2\) distinct required words is exactly \((k-1)(k-2)/2\).
2. Every shortest cover has precisely one occurrence of each word in \(\mathcal C_k\) and no other length-\(k\) factors. In particular, the additional factors are **forced**, being exactly the \((k-1)(k-2)/2\) words
   \[
   \mathcal X_k=\{1^a0^b1^c:a,b,c\ge1,\ a+b+c=k\}.
   \]
3. There are exactly \(2^{k-2}\) shortest cyclic covers up to rotation. Reversals are not identified. Each rotation class has one indexing that begins at its unique length-\(k\) factor \(0^k\).

The circular-interval family has exactly \(2+k(k-1)\) words: the two constant words and \(k\) rotations of \(1^j0^{k-j}\) for each \(1\le j\le k-1\). Thus the theorem gives a complete structural description, not just a shortest-cover length.

Small cases, in the order \((k,|\mathcal R_k|,\text{optimal length},\text{rotation classes})\), are \((2,4,4,1)\), \((3,7,8,2)\), \((4,11,14,4)\), \((5,16,22,8)\), \((6,22,32,16)\), and \((7,29,44,32)\).

## Assumptions and scope
The alphabet is \(\{0,1\}\); factor containment is contiguous and cyclic, so windows wrapping around the end count. A cyclic word is identified with any of its rotations when enumerating covers, but not with its reversal or bit complement. Words of length \(k\) may occur more than once in an arbitrary host; optimal hosts are proved to have no repeated length-\(k\) words. The theorem concerns all \(k\ge2\), with no fixed upper bound. The parameter \(n=k-1\) is used below; \(0^n\) and \(1^n\) denote constant length-\(n\) words. Exponents denote repetition, not arithmetic powers.

## Proof
**1. Mandatory edges and degree imbalance.** Construct the directed order-\(n\) binary de Bruijn graph: each length-\(k\) word \(w=w_1\cdots w_k\) is a directed edge from its length-\(n\) prefix to its length-\(n\) suffix. Every cyclic word of length \(L\) corresponds to a closed walk of \(L\) edges, with the length-\(k\) cyclic windows as its edge labels. Mark one occurrence of each edge in \(\mathcal R_k\) in any cover. The remaining edge occurrences form a nonnegative integer multiset whose degree imbalance cancels that of the mandatory subgraph.

For \(1\le i\le n-1\) put
\[
N_i=1^i0^{n-i},\qquad P_i=0^{n-i}1^i.
\]
In the mandatory subgraph, each \(N_i\) has indegree two and outdegree one, whereas each \(P_i\) has indegree one and outdegree two. All other active vertices are balanced. This follows by considering whether prepending or appending a zero or one preserves a single linear run of ones. Consequently, the extra edge multiset has divergence \(\deg^+_{\rm extra}-\deg^-_{\rm extra}=1\) at every \(N_i\), divergence \(-1\) at every \(P_i\), and zero elsewhere. The statements also hold for \(k=2\), where both index sets are empty.

**2. Universal lower bound, even allowing forbidden windows.** Any such integer flow decomposes into exactly \(n-1\) directed paths from the \(N_i\) to the \(P_j\), with each source and sink used once, plus directed cycles. This is the standard finite integral flow decomposition, applied after adding a super-source and super-sink. All paths use the full de Bruijn graph; hence extra edges may be arbitrary binary windows, including windows outside \(\mathcal R_k\).

A directed path of length \(\ell\) from \(N_i\) cannot reach a word beginning in zero if \(\ell<i\): at least the first of the \(i\) initial ones remains in the shifted vertex. Every \(P_j\) begins in zero; therefore a path starting at \(N_i\) has length at least \(i\). Summing over all sources gives
\[
\#\{\text{extra edges}\}\ \ge\sum_{i=1}^{n-1}i=\frac{(k-1)(k-2)}2.
\]
Since \(|\mathcal R_k|=1+k(k+1)/2\), every cover has length at least \(k^2-k+2\).

**3. Unique equality mechanism.** If equality holds, there are no extra directed cycles and the path from \(N_i\) has exactly \(i\) edges. After these shifts its terminal vertex must be \(P_j\). Its remaining suffix from the original source is \(0^{n-i}\), whereas \(P_j\) has initial zeros of length \(n-j\). Necessarily \(j\le i\). As the assignment \(i\mapsto j\) is a permutation of \(\{1,\ldots,n-1\}\), all inequalities force \(j=i\). To reach \(P_i=0^{n-i}1^i\) in exactly \(i\) shifts from \(N_i\), the appended symbols must be exactly \(1^i\). Thus each path is unique. Its \(r\)-th edge, for \(1\le r\le i\), has label
\[
1^{i-r+1}0^{n-i}1^r.
\]
As \(i\) and \(r\) vary, these labels are exactly the elements of \(\mathcal X_k\), each once: its central zero-run length determines \(i=n-b\), and its terminal one-run length determines \(r=c\). Therefore equality forces the entire extra edge multiset to be \(\mathcal X_k\); in particular every optimal cyclic host has each \(k\)-window of \(\mathcal R_k\cup\mathcal X_k=\mathcal C_k\) precisely once, with none others.

**4. Existence of equality.** The mandatory graph is strongly connected on its active vertices: from any vertex, appending zeros repeatedly reaches \(0^n\), and from \(0^n\) appending a target active vertex's symbols reaches that vertex. Every intermediate length-\(k\) edge along these paths has at most one linear run of ones. Add the \(n-1\) equality paths \(N_i\rightarrow P_i\) from Step 3. This balances every vertex and leaves a connected directed graph. Hence an Eulerian circuit exists, with exactly \(|\mathcal R_k|+|\mathcal X_k|=k^2-k+2\) edges. Read its successive appended bits to obtain the required optimal cyclic cover. This construction also works for \(k=2\), with no added paths.

**5. Exact number of optimal cycles.** By Step 3, optimal covers are precisely Eulerian circuits of the directed graph whose edges are \(\mathcal C_k\), with each edge used once. Each optimum uses \(0^k\) exactly once, so rooting the circuit at this prescribed first edge chooses exactly one representative of each rotation class. Let \(Z=0^n\) be its initial vertex and \(U=1^n\). By the directed BEST theorem, the number of circuits beginning with that specified edge equals
\[
t_Z\prod_v(\deg^+(v)-1)!,
\]
where \(t_Z\) is the number of directed in-arborescences rooted at \(Z\). Every vertex here has outdegree one or two, so the factorial product is one.

It remains to count the trees. The vertex \(U\) must select its outgoing zero edge: the alternative is a self-loop. Each vertex containing both a leading and a trailing one separated by one run of zeros has precisely one outgoing edge, which appends one, and these forced edges lead onward through the equality paths. For each \(N_i\), its two options append zero (leading to \(N_{i-1}\), interpreting \(N_0=Z\)) or append one (entering the forced path ending at \(P_i\)). For each \(P_i\), its options append zero (leading through forced zero-appending vertices to \(N_i\)) or append one (leading to \(P_{i+1}\), with \(P_{n-1}\) leading to \(U\)).

No tree can let any \(N_i\) append one. Indeed choose the largest such index \(i\); its selected path leads to \(P_i\), which either follows zero-appending edges toward some \(N_j\) with \(j\ge i\), or follows increasing \(P\)-indices to \(U\) and thence \(N_{n-1}\). Every \(N_j\) with \(j>i\) selects zero by maximality and so descends to \(N_i\). In either case the selected edges form a directed cycle, contradicting the definition of an in-arborescence. Therefore all \(N_i\) select zero. Conversely, with these selections and the forced outgoing edge at \(U\), **each** \(P_i\) may independently select zero or one: increasing along \(P\)-indices must eventually enter some \(N_j\) or \(U\), after which zero-appending \(N\)-edges reach \(Z\). All remaining forced vertices also reach \(Z\), so these choices give in-arborescences. There are \(n-1=k-2\) independent binary choices, hence \(t_Z=2^{k-2}\).

The directed BEST formula now yields exactly \(2^{k-2}\) optimal rotation classes, as claimed. \(\square\)

## Verification
Run `python3 verify.py` using only Python's standard library. The program independently constructs Eulerian cycles, verifies that every length-\(k\) cyclic window belongs to the predicted circular-interval family exactly once for \(2\le k\le18\), solves the imbalance pairing by an independent subset dynamic program for \(2\le k\le14\), directly counts rooted Euler tours for \(2\le k\le11\), and exhaustively tests all shorter cyclic hosts rooted at \(0^k\) through \(k=5\). Its expected success line is:

`VERIFY_OK construction_k=2..18 assignment_k=2..14 rooted_euler_counts_k=2..11 exhaustive_all_shorter_hosts_k=2..5`

These finite checks corroborate, but do not establish by themselves, the all-length theorem; the universal correctness and enumeration follow from the proof above.

## Relationship to prior work
The classical de Bruijn/Eulerian-circuit framework and the BEST theorem provide the machinery for exact cyclic coverage and enumeration. Moreno and Matamala study lexicographically minimal de Bruijn sequences in languages defined by forbidden substrings (arXiv:0711.1695, 2007); that work constructs exact Eulerian cycles in admissible graphs but does not supply the optimal repetition count or the forced circular completion for the present *linearly* one-run compulsory family. Leitner and Godbole's universal-cycle paper (arXiv:0808.1309, 2008) studies other restricted word families, not this compulsory one-run coverage invariant. Blanca and Godbole's work (arXiv:1008.2251, 2010) treats weight-restricted families; restricting total Hamming weight does not impose a single contiguous run, and its results do not give this theorem. Work on fixed-weight de Bruijn sequences concerns yet another coverage object: all positions of a fixed weight instead of a single circular interval. The exact forced completion and \(2^{k-2}\) rotation-class law have not been located in inspected primary results. This evidence is not a claim of exhaustive absence from all literature.

## Limitations
The theorem concerns binary words whose ones form at most one **linear** contiguous run, with a cyclic host permitting any extra windows; the stronger forced-circular-interval property is concluded only for shortest hosts. It does not classify cyclic covers for multiple runs, general regular languages, minimum *linear* superstrings, or cycles identified under reversal. The optimal result is mathematical rather than experimentally inferred, but literature indexing and inaccessible alternate formulations leave a residual originality risk. No independent scientific audit has been conducted.

## References
1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (first public preprint November 12, 2007), https://arxiv.org/abs/0711.1695.
2. M. Leitner and A. P. Godbole, *Universal Cycles of Classes of Restricted Words*, arXiv:0808.1309 (2008), https://arxiv.org/abs/0808.1309.
3. A. Blanca and A. P. Godbole, *On Universal Cycles for New Classes of Combinatorial Structures*, arXiv:1008.2251 (2010), https://arxiv.org/abs/1008.2251.
4. F. Ruskey, J. Sawada and A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, *SIAM Journal on Discrete Mathematics* **26** (2012), DOI:10.1137/100808782.
5. N. G. de Bruijn, *A Combinatorial Problem*, *Proceedings of the Section of Sciences of the Koninklijke Nederlandse Akademie van Wetenschappen* **49** (1946), 758–764.
6. T. van Aardenne-Ehrenfest and N. G. de Bruijn, *Circuits and Trees in Oriented Linear Graphs*, *Simon Stevin* **28** (1951), 203–217.
