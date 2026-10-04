# A parity reduction of penultimate hypercube Rips complexes
## Finding
Let \(Q_n=\mathbb F_2^n\) with Hamming distance, and let \(\mathrm{VR}(Q_n;r)\) contain exactly the finite subsets of diameter at most \(r\). Let \(FQ_m\) denote the folded cube of order \(m\), namely
\[
FQ_m=\operatorname{Cay}\!\left(\mathbb F_2^{m-1},\{e_1,\ldots,e_{m-1},e_1+\cdots+e_{m-1}\}\right).
\]
For every integer \(n\ge 3\),
\[
\mathrm{VR}(Q_n;n-2)\cong
\begin{cases}
\mathrm{Ind}(FQ_{n+1}),& n\text{ even},\\
\mathrm{Ind}(K_2\square FQ_n),& n\text{ odd}.
\end{cases}
\]
Here \(\mathrm{Ind}(G)\) is the independence complex of a graph \(G\). The isomorphisms are combinatorial, not merely homotopy equivalences.

## Assumptions and scope
The scale convention is inclusive: an edge of the Rips complex joins two cube vertices exactly when their Hamming distance is at most the scale. The folded-cube convention is the one in Mančinska--Pivotto--Roberson--Royle: \(FQ_m\) has vertex group \(\mathbb F_2^{m-1}\) and the standard \(m\)-element folded generating set. The statement is structural; it does not assert a general homotopy classification of the two independence-complex families.

## Proof
Write \(j=(1,\ldots,1)\in\mathbb F_2^n\). Since a Vietoris--Rips complex is flag, a vertex set is a simplex of \(\mathrm{VR}(Q_n;n-2)\) precisely when it contains no pair at Hamming distance \(n-1\) or \(n\). Hence
\[
\mathrm{VR}(Q_n;n-2)=\mathrm{Ind}(H_n),
\]
where the forbidden-pair graph is the Cayley graph
\[
H_n=\operatorname{Cay}(\mathbb F_2^n,S_n),\qquad
S_n=\{j\}\cup\{j+e_i:1\le i\le n\}.
\]
Indeed, \(d_H(x,y)=\operatorname{wt}(x+y)\), so the nonzero differences of weights \(n-1\) and \(n\) are exactly the elements of \(S_n\).

Suppose first that \(n\) is even and put \(a_i=j+e_i\). The vectors \(a_1,\ldots,a_n\) are a basis. To see this, if \(\sum_{i\in I}a_i=0\), then for even \(|I|\) one gets \(\sum_{i\in I}e_i=0\), hence \(I=\varnothing\); for odd \(|I|\) one gets \(j=\sum_{i\in I}e_i\), which would force \(I=\{1,\ldots,n\}\), impossible because \(n\) is even. In this basis,
\[
a_i\longmapsto e_i,\qquad
j=\sum_{i=1}^n a_i\longmapsto e_1+\cdots+e_n.
\]
Thus \(H_n\cong FQ_{n+1}\).

Now suppose that \(n\) is odd. The vectors
\[
B=\{j,j+e_1,\ldots,j+e_{n-1}\}
\]
form a basis. If \(c j+\sum_{i=1}^{n-1}c_i(j+e_i)=0\), the last coordinate gives \(c+\sum_i c_i=0\), and then the first \(n-1\) coordinates force every \(c_i=0\), hence \(c=0\). In the coordinates determined by \(B\), the generator \(j\) is a new coordinate generator, the vectors \(j+e_i\) for \(i<n\) are the standard generators on the remaining coordinates, and
\[
j+e_n=\sum_{i=1}^{n-1}(j+e_i)
\]
because \(n-1\) is even. Therefore the connection set splits as one \(K_2\) generator plus the folded-cube generating set on an \((n-1)\)-dimensional subspace. Hence \(H_n\cong K_2\square FQ_n\). Taking independence complexes gives the claimed two cases.

## Verification
The proof above is symbolic and covers all \(n\ge3\). The accompanying script `verify_folded_reduction.py` independently constructs the forbidden-pair Cayley graph, computes the stated basis change over \(\mathbb F_2\), and exhaustively checks adjacency preservation for every pair of vertices for \(3\le n\le8\). Its terminal line is `VERIFY_OK`.

## Relationship to prior work
Adamaszek and Adams introduced the systematic study of these hypercube Rips complexes, identified the top scale \(n-1\) with a cross-polytope boundary, and emphasized that many larger-scale cases remain open. Later work determined much more at scale \(3\) and produced general homology lower bounds. Briggs, Feng, and Wells studied facets at arbitrary scale and described substantial remaining complexity. The present statement instead isolates the penultimate scale \(n-2\) and identifies the entire complex with an independence complex of a familiar cubelike graph family.

The folded-cube convention used here is standard and appears explicitly in Mančinska, Pivotto, Roberson, and Royle. Searches of the cited hypercube-Rips papers and targeted literature/database queries did not locate this parity-dependent identification. That negative search is not treated as a proof of global novelty; it is recorded only as the originality check performed for this result.

## Limitations
The reduction does not compute the homotopy type or integral homology of \(\mathrm{Ind}(FQ_{n+1})\) or \(\mathrm{Ind}(K_2\square FQ_n)\) in general. At \(n=5\), the scale \(n-2=3\) lies in the already-studied scale-three regime, so the value of the reduction there is a new presentation rather than a new homotopy calculation. The literature search was targeted rather than exhaustive across all graph-independence-complex literature.

## References
1. Michał Adamaszek and Henry Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, first posted 2021-03-01.
2. Henry Adams and Žiga Virk, *Lower bounds on the homology of Vietoris--Rips complexes of hypercube graphs*, arXiv:2309.06222, first posted 2023-09-12.
3. Joseph Briggs, Ziqin Feng, and Chris Wells, *Facets in the Vietoris--Rips complexes of hypercubes*, arXiv:2408.01288, first posted 2024-08-02.
4. Laura Mančinska, Irene Pivotto, David E. Roberson, and Gordon Royle, *Cores of cubelike graphs*, arXiv:1808.02051; European Journal of Combinatorics 87 (2020), 103092.
