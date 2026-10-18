# Boundary-twist reversal for total perfect codes of cubic ladders

## Finding
For every integer \(n\ge 3\), let \(P_n=C_n\square K_2\) be the circular ladder, and let \(M_{2n}\) be the Möbius ladder on \(2n\) vertices. A *total perfect code* is a vertex set \(D\) with \(|N(v)\cap D|=1\) for **every** vertex \(v\), including vertices of \(D\). This is also called an efficient open dominating set or a \((1,1)\)-regular set.

Write \(c_P(n)\) and \(c_M(n)\) for the numbers of distinct total perfect codes of the labeled graphs, and \(p_P(n)\) and \(p_M(n)\) for the numbers of **unordered** partitions of their entire vertex sets into three total perfect codes. Then, exactly,

\[
\begin{array}{c|cc|cc}
 n\pmod 6 & c_P(n)&c_M(n)&p_P(n)&p_M(n)\\ \hline
0&9&3&6&1\\
3&3&9&1&6\\
1,2,4,5&0&0&0&0
\end{array}
\]

Moreover, every total perfect code in either graph has exactly \(2n/3\) vertices; all such codes belong to the nine explicit six-column patterns classified below. Thus a single twist reverses both the number of codes and the number of code partitions in the two divisible-by-three residue classes. The existence criterion \(3\mid n\), unlike these exact counts and the exhaustive classification, is not claimed as new.

## Assumptions and scope
The vertices are \((i,r)\), with \(i\in\{0,\ldots,n-1\}\) and row \(r\in\{0,1\}\). Both graphs have rungs \((i,0)(i,1)\), rail edges \((i,r)(i+1,r)\) for \(0\le i<n-1\), and two closing edges. For \(P_n\), the closing edges are \((n-1,r)(0,r)\). For \(M_{2n}\), they are \((n-1,r)(0,1-r)\). These are simple cubic graphs for all stated \(n\), including the triangular prism at \(n=3\) and \(M_6\cong K_{3,3}\).

Use bit-columns \(a_i=x_i+2y_i\in\{0,1,2,3\}\), where \(x_i\) selects \((i,0)\) and \(y_i\) selects \((i,1)\). A length-six word represents its entire bi-infinite periodic sequence, not an arbitrary word labeling a graph with six columns. Rotation means cyclic shift of the six displayed entries. Swapping rows acts on column symbols by \(0\leftrightarrow0\), \(3\leftrightarrow3\), \(1\leftrightarrow2\).

## Proof
**1. Six-periodicity is forced.** Lift any proposed code across the rail seam to the bi-infinite ladder. For a prism, the lifted rows obey \((x_{i+n},y_{i+n})=(x_i,y_i)\); for a Möbius ladder they obey \((x_{i+n},y_{i+n})=(y_i,x_i)\). In either case the definition is equivalent to

\[
x_{i-1}+x_{i+1}+y_i=1,\qquad
y_{i-1}+y_{i+1}+x_i=1\quad(i\in\mathbb Z).
\]

Set \(s_i=x_i+y_i\) and \(d_i=x_i-y_i\). Adding and subtracting yields

\[
s_{i-1}+s_i+s_{i+1}=2,\qquad d_{i-1}-d_i+d_{i+1}=0.
\]

Subtract the first equation at successive indices to obtain \(s_{i+3}=s_i\). Applying the difference recurrence three times gives \(d_{i+3}=-d_i\). Therefore \(x_i=(s_i+d_i)/2\) and \(y_i=(s_i-d_i)/2\) are six-periodic and shifting three columns interchanges the two rows.

**2. Exhaustive classification on the infinite strip.** Since \(s_0+s_1+s_2=2\) and each \(s_i\in\{0,1,2\}\), its three entries are either a permutation of \((2,0,0)\) or of \((0,1,1)\). In the first case \(d_i=0\) for all \(i\), yielding exactly the three rotations of

\[
V=(0,0,3,0,0,3).
\]

In the second case choose which of the three positions contains zero. At that position \(d=0\); the difference recurrence forces the two successive nonzero \(d\)'s to be equal, with their common value \(+1\) or \(-1\). These six choices are exactly the six rotations of

\[
H=(0,1,1,0,2,2).
\]

Each displayed word satisfies both original neighborhood equations; conversely the preceding cases exhaust all binary solutions. The \(V\)-patterns have least shift-period three and are invariant under row swap. The \(H\)-patterns have least shift-period six, and row swap agrees with shifting three positions.

**3. Periodic and twisted boundary conditions.** In a prism the permitted pattern must be invariant under a shift by \(n\). Hence the three \(V\)-patterns occur exactly when \(3\mid n\), while the six \(H\)-patterns occur exactly when \(6\mid n\). In a Möbius ladder shift by \(n\) must instead equal row swap. Thus the \(V\)-patterns again occur exactly when \(3\mid n\), whereas the \(H\)-patterns occur exactly when \(n\equiv3\pmod6\). For \(n\ge3\), distinct permitted six-periodic patterns give distinct vertex subsets: a prism admitting \(H\) has at least six columns, and a Möbius ladder with \(H\) has at least three columns whose remaining three entries are determined by the twist. This proves the two code-count columns of the table.

**4. Exact numbers of three-code partitions.** Each graph is cubic. Double counting selected edges incident to vertices gives \(2n=3|D|\) for every total perfect code \(D\), so precisely three disjoint codes are needed in any partition. If just the three \(V\)-patterns are available, they partition the vertices uniquely. When all nine patterns are available, label the \(V\)-patterns as

\[
V_0=(3,0,0,3,0,0),\quad V_1=(0,3,0,0,3,0),\quad V_2=(0,0,3,0,0,3)
\]

and the \(H\)-patterns as

\[
\begin{aligned}
&H_0=(0,1,1,0,2,2),\quad H_1=(1,1,0,2,2,0),\\
&H_2=(1,0,2,2,0,1),\quad H_3=(0,2,2,0,1,1),\\
&H_4=(2,2,0,1,1,0),\quad H_5=(2,0,1,1,0,2).
\end{aligned}
\]

For three patterns to partition, the bitwise OR at each of their six columns must equal \(3\), with their pairwise bitwise AND equal to \(0\). Checking this finite list gives exactly the six unordered triples

\[
\begin{gathered}
\{V_0,V_1,V_2\},\quad\{V_0,H_0,H_3\},\quad
\{V_1,H_2,H_5\},\\
\{V_2,H_1,H_4\},\quad\{H_0,H_2,H_4\},\quad
\{H_1,H_3,H_5\}.
\end{gathered}
\]

There are no other triples, as can be checked directly from the displayed nine rows and the two bitwise criteria (or by the independent checker). For prism widths divisible by six, every six-column block repeats, so the test is equivalent to a partition of the graph. For Möbius widths congruent to three modulo six, the next three-column block is the row swap of the first, preserving disjointness and coverage; the same test applies. The two partition-count columns follow. This completes the proof.

## Verification
Run `python VERIFY.py` with Python 3.10 or newer. It constructs each graph from its edges, checks the defining condition for every labeled vertex subset for all \(3\le n\le9\) and both boundary conditions, compares the entire set of solutions with the nine-pattern classification, and independently counts all three-code partitions. It also checks the periodic formulas for \(3\le n\le150\). The deterministic expected output is in `CHECKS.txt`. These finite checks corroborate but do not replace the infinite proof.

## Relationship to prior work
Kuziak, Peterin and González Yero (2014) characterized *existence* of efficient open dominating sets in general Cartesian prisms \(G\square K_2\) (Theorem 4.3). In particular their characterization and the known perfect-code cycle criterion give prism existence for \(3\mid n\), but they do not state a count of all code sets or all partitions. Wang, Xu and Zhou (2023; arXiv first version) focus on regular subsets in Cayley graphs, chiefly \((0,k)\)-regular sets; their main classification does not enumerate the present \((1,1)\)-regular subsets. Dejter (2025–2026 preprint, Theorem 36 and Corollary 37) explicitly constructs total-perfect-code color classes for Möbius ladders of width divisible by three, establishing existence and a partition, not exhaustion or the alternating \(3/9\) and \(1/6\) multiplicities. Lekshmi and West (2020) count ordinary perfect matchings of the two graph families; this is a different invariant, since the selected vertices of a total perfect code need not cover every vertex as a matching. These foundations are credited, not claimed as new.

## Limitations
Counts distinguish labeled vertex subsets but do not count symmetry-orbit types. The theorem covers widths \(n\ge3\) only. It does not address total perfect codes of arbitrary cubic graphs, nor independence of a proof or bibliographic priority certification. It is possible that a description equivalent to these complete enumerations occurs under another coding or efficient-open-domination terminology in sources not indexed by the searches. Scientific validation beyond the stated exact proof and definition-level tests is not claimed.

## References
1. D. Kuziak, I. Peterin, I. G. Yero, *Efficient open domination in graph products*, Discrete Mathematics and Theoretical Computer Science **16** (2014), 105–120, DOI: 10.46298/dmtcs.1267, https://dmtcs.episciences.org/en/articles/1267/download .
2. X. Wang, S.-J. Xu, S. Zhou, *On regular sets in Cayley graphs*, arXiv:2310.01793v1 (3 October 2023), https://arxiv.org/abs/2310.01793 .
3. I. J. Dejter, *From semi-total to equitable total colorings, and their induced partitions into perfect and total perfect codes*, arXiv:2503.20055, Theorem 36 and Corollary 37, https://arxiv.org/html/2503.20055v6 .
4. R. S. Lekshmi, D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602, https://arxiv.org/abs/2003.09602 .
