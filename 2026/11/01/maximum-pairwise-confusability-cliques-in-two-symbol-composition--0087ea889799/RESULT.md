# Maximum pairwise-confusability cliques in two-symbol composition reads

## Finding
Fix integers \(q\ge2\) and \(n\ge1\), and a labeled alphabet \(\Sigma\) of size \(q\). For every word \(w=w_1\cdots w_n\), let its **two-symbol composition read** \(R(w)\) consist of the \(n+1\) unordered pairs
\[
R(w)_i=\{w_{i-1},w_i\}_{\mathrm{multi}}\quad(1\le i\le n+1),
\]
with \(w_0=w_{n+1}=\bot\) a fixed boundary marker not in \(\Sigma\). Define the simple graph \(G_{q,n}\) on \(\Sigma^n\) by joining distinct \(u,v\) exactly when the Hamming distance between \(R(u)\) and \(R(v)\) is two. Replacing \(\bot\) by any fixed alphabet symbol leaves this distance, hence the graph, unchanged.

**Theorem.** The clique number is
\[
\omega(G_{q,n})=\max\{q,n+1\}.
\]
For \(n\ge2\), all cliques of maximum size are exactly those among these two constructions whose cardinality equals \(\max\{q,n+1\}\):

1. A **coordinate star** \(S(i,v)=\{v_1\cdots v_{i-1}av_i\cdots v_{n-1}:a\in\Sigma\}\), where \(1\le i\le n\) and \(v\in\Sigma^{n-1}\), of size \(q\).
2. An **alternating deletion clique** \(D(a,b)\), comprising all \(n+1\) distinct one-position deletions of the length-\(n+1\) alternating word \(abab\cdots\), for ordered distinct symbols \(a,b\in\Sigma\).

The number of maximum cliques, for \(n\ge2\), therefore equals
\[
M_q(n)=\begin{cases}
q(q-1),&n+1>q,\\
nq^{n-1}+q(q-1),&n+1=q,\\
nq^{n-1},&n+1<q.
\end{cases}
\]
For \(n=1\), \(G_{q,1}\) is complete and \(M_q(1)=1\). These are **maximum** cliques, not a claimed classification of every inclusion-maximal smaller clique.

## Assumptions and scope
The alphabet is finite and labeled. The read map records unordered multisets, not ordered adjacent pairs, and compares its \(n+1\) read entries by ordinary Hamming distance. The terminal boundary convention makes the mapping injective but imposes no physical boundary-symbol requirement: the model with zero padding used in the guiding literature has the same pairwise distances. The graph records pairwise ambiguity at read distance two; it is not the graph obtained from a single-deletion ball, nor does a clique necessarily consist of reads compatible with one common corrupted output.

## Proof
### 1. Two-place read differences and their word support
If distinct words \(u,v\) differ first at source position \(i\) and last at \(j\), their read entries necessarily differ at \(i\) and \(j+1\). If their read distance is exactly two, the internal read multisets agree. From \(\{u_r,u_{r+1}\}=\{v_r,v_{r+1}\}\) and \(u_r\ne v_r\), induction forces \(u_i\cdots u_j\) to alternate between two distinct letters and \(v_i\cdots v_j\) to take the opposite phase (the length-one case permits any replacement). Conversely, this interval phase exchange changes precisely the read entries \(i\) and \(j+1\). Consequently a specified two-coordinate read-difference support \(\{i,j+1\}\) identifies **at most one** neighbor if \(j>i\). If \(j=i\), its neighbors are precisely the \(q-1\) possible substitutions at source coordinate \(i\).

### 2. Read-support stars and exclusion of a triangle
Fix a clique \(C\) and base word \(x\in C\). For each \(y\in C\setminus\{x\}\), let \(E_y\subseteq\{1,\ldots,n+1\}\) be the two-element set of read coordinates where \(R(y)\) differs from \(R(x)\). Two such sets must intersect, because disjoint supports would make the corresponding read vectors differ at four coordinates. When \(E_y\ne E_z\), the read entries of \(y,z\) at their single shared coordinate must **agree**, or else their read distance would be three.

A basic support fact is that a pairwise-intersecting collection of distinct two-element subsets either has a common point or is exactly the three sides of a triangle. The latter cannot occur here. Identify each multiset of letters with its integer incidence vector in the free abelian group on \(\Sigma\cup\{\bot\}\). For every pair of source words \(x,y\), the difference of read incidence vectors obeys the alternating-sum identity
\[
\sum_{t=1}^{n+1}(-1)^t\bigl(R(y)_t-R(x)_t\bigr)=0,
\]
because each interior source letter occurs once with each sign; the boundary-marker contribution cancels in the difference. If supports \(\{a,b\},\{a,c\},\{b,c\}\) occurred for three neighbors of \(x\), agreement of the read entries at shared coordinates would give nonzero vectors \(A,B,C\) at coordinates \(a,b,c\) such that
\[
(-1)^a A+(-1)^b B=0,\quad
(-1)^a A+(-1)^c C=0,\quad
(-1)^b B+(-1)^c C=0.
\]
These equations imply \(2A=0\), impossible over the torsion-free integer incidence group. Hence **distinct supports form a star**.

If a support repeats, Step 1 shows it must be \(\{i,i+1\}\), and the corresponding neighbors are distinct source substitutions at position \(i\). Their read entries differ at **both** support coordinates. No neighbor with any other support can be adjacent to both, because at the one shared read coordinate it would need to equal two distinct multisets. Thus the entire clique lies in the coordinate star at position \(i\), and has size at most \(q\). If no support repeats, the supports form a star in the \(n+1\) read coordinates, giving at most \(n\) other vertices and hence \(|C|\le n+1\). This proves the upper bound.

### 3. Constructions attain the bound
A coordinate star changes only one source letter; each pair of its distinct members differs at exactly its two incident read coordinates, so has \(q\) vertices. For a word \(z\) alternating between distinct \(a,b\) and of length \(n+1\), deleting at each of its \(n+1\) positions gives distinct words. Two such descendants, deleted at positions \(s<t\), agree outside their source interval \([s,t-1]\) and exhibit opposite alternating phases within that interval. Step 1 makes them adjacent. Thus \(D(a,b)\) has \(n+1\) vertices.

### 4. Equality and completeness of classification
Assume \(n\ge2\), that a clique has \(n+1\) members and no repeated read supports. Relative to a base word \(x\), all \(n\) other read supports must be \(\{c,j\}\), one for every \(j\ne c\). At read coordinate \(c\), all these neighbors have one common read entry distinct from that of \(x\), since pairwise differences have to occupy only their two nonshared coordinates.

If \(c=1\), the support \(\{1,2\}\) changes source letter \(x_1=a\) to some \(b\ne a\). The support \(\{1,3\}\) must exchange the phases of the two-letter prefix, so \(x_2=b\); the remaining supports \(\{1,j\}\) force the entire source word to alternate \(a,b\). The clique is precisely the deletion clique of the length-\(n+1\) alternating word beginning with \(b\) and followed by \(x\). The case \(c=n+1\) follows by reversal.

For \(2\le c\le n\), supports \(\{c-1,c\}\) and \(\{c,c+1\}\) change source letters \(x_{c-1}=p\) to \(p'\ne p\) and \(x_c=s\) to \(s'\ne s\). Equality of the modified read multisets at \(c\) gives \(\{p',s\}=\{p,s'\}\), hence necessarily \(p=s=a\) and \(p'=s'=b\ne a\). Every other support ending or starting at \(c\) then requires alternation on its corresponding left or right segment, with the same two letters \(a,b\). Consequently \(x\) is obtained by deleting the middle \(b\) between consecutive copies of \(a\) from a fully alternating length-\(n+1\) word \(z\). Step 1 determines each other clique member uniquely, so the clique equals \(D(a,b)\) for the ordered initial letters of \(z\).

Finally, a clique attaining \(q\) when \(q>n+1\) must have a repeated read support, hence be a coordinate star. When \(q=n+1\), equality can arise from either family; both have size \(q\) and no others exist. For \(n\ge2\), different stars are distinct, different ordered alternating words have distinct deletion-descendant sets (the two-letter alphabet and first letter are recoverable from the set, using the descendant beginning with a repeated first letter), and no deletion clique is a coordinate star because its members vary in multiple source positions. Counting the \(nq^{n-1}\) coordinate stars and \(q(q-1)\) deletion cliques proves \(M_q(n)\). For \(n=1\) all letters form one clique.

## Verification
The included Python 3 program `verify_read_cliques.py` builds all words and their read vectors directly, constructs exact read-distance-two edges, and exhaustively enumerates **all** inclusion-maximal cliques without relying on the classification. It compares the full set of maximum cliques with the proposed coordinate-star/deletion families, not just their sizes. It passed for \(q=2\), \(1\le n\le8\); \(q=3\), \(1\le n\le5\); \(q=4\), \(1\le n\le4\); and \(q=5\), \(1\le n\le3\). These are finite consistency checks; the preceding argument proves the theorem for every \(q,n\).

Reproduction: from a directory containing the standalone script run `python3 verify_read_cliques.py`; only Python's standard library is required.

## Relationship to prior work
Sun and Ge (2024), arXiv:2403.11754, §III Theorem 1 characterize read-vector pairs of Hamming distance two by opposite alternating intervals. Their §IV-B Lemma 11 gives explicit local cliques of size \(2t+1\) for a covering argument; it does not state an upper bound, the complete extremal classification, or a count of all maximum cliques across arbitrary alphabet sizes and lengths. Cai, Kiah, Nguyen and Yaakobi (2020), arXiv:2001.01376, analyze single-edit reconstruction-ball overlaps and redundancy, but do not establish this read-vector clique extremum. Banerjee, Yehezkeally, Wachter-Zeh and Yaakobi (2023), arXiv:2305.10214, develop the composition-read channel and graph-theoretic code bounds, with primary emphasis on binary reads and larger read windows. The present structural step is the signed incidence conservation law excluding triangular read-difference supports, which upgrades alternating-clique examples to an exhaustive classification.

## Limitations
The theorem concerns the simple distance-exactly-two read graph only, not cliques for other read lengths or read distances, not clique-cover numbers or code independence numbers, and not actual common-output list sizes under a single noisy read. A clique's pairwise one-substitution confusability need not imply a jointly common corrupted read. Originality remains subject to discovery of an unindexed equivalent in the broader insertion reconstruction or equidistant-code literature; the cited characterization of every edge is prior work.

## References
1. Y. Sun and G. Ge, *Bounds and Constructions of \(\ell\)-Read Codes under the Hamming Metric*, arXiv:2403.11754v1 (first public March 18, 2024), particularly §§II–IV, Theorems 1–3 and Lemma 11. https://arxiv.org/abs/2403.11754
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (first public January 6, 2020). https://arxiv.org/abs/2001.01376
3. A. Banerjee, Y. Yehezkeally, A. Wachter-Zeh and E. Yaakobi, *Error-Correcting Codes for Nanopore Sequencing*, arXiv:2305.10214 (first public May 17, 2023). https://arxiv.org/abs/2305.10214
