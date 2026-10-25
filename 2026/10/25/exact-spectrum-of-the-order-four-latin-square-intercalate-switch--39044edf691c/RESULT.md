# Exact spectrum of the order-four Latin-square intercalate-switch graph

## Finding
Let \(\mathcal L_4\) be the set of all \(4\times4\) Latin squares with fixed row labels, column labels, and symbol alphabet \(\{0,1,2,3\}\). Define \(G\) to have vertex set \(\mathcal L_4\), joining two *distinct* squares when one is obtained from the other by switching a \(2\times2\) intercalate: the alternating pattern \(\left(\begin{smallmatrix}a&b\\ b&a\end{smallmatrix}\right)\) is replaced by \(\left(\begin{smallmatrix}b&a\\ a&b\end{smallmatrix}\right)\).

**Theorem.** The adjacency characteristic polynomial of this fully labeled, 576-vertex graph is
\[
\boxed{\det(xI-A_G)=x^{318}(x^2-8)^{81}(x^2-12)^8(x^2-24)^{39}(x^2-48).}
\]
The graph is connected, bipartite, and has diameter \(6\). Its degree classes have sizes \(144\) and \(432\), with respective degrees \(12\) and \(4\), and all \(1,728\) edges run between these classes. As a corollary, the lazy simple random walk \(P_{\mathrm{lazy}}=(I+D^{-1}A_G)/2\) has exact spectral gap
\[
\boxed{\gamma=\frac{1-1/\sqrt{2}}{2}.}
\]
These degrees and class sizes are context, rather than separately claimed new results; the complete adjacency spectrum and exact lazy-walk gap are the focus.

## Assumptions and scope
Every square has four rows and four columns and uses the *same* four labeled symbols, exactly once in each row and column. There is no identification under row, column, or symbol permutations. Edges are undirected and unweighted, with one edge for each unordered pair of distinct squares related by a single intercalate switch. The spectral theorem concerns the ordinary symmetric adjacency matrix, not the graph Laplacian or the \(16\)-vertex graph conventionally called a Latin-square graph. The walk is made lazy because the non-lazy walk on this bipartite graph has period two.

## Proof
**1. Finite exhaustiveness and bipartition.** Enumerate the \(24^4\) choices of four row permutations, retaining exactly those for which the four entries in each column are distinct. These are all \(576\) labeled Latin squares, each exactly once. For each square, test all \(\binom42^2=36\) choices of two rows and two columns for the alternating intercalate condition and apply the unique switch. Each output is Latin; the switch reverses itself, and distinct tested intercalates produce distinct output squares. The exhaustive exact algorithms in `verify_spectrum.py` and the independent backtracking program `verify_independent.py` confirm degrees \(12\) for \(144\) vertices and \(4\) for \(432\) vertices, with every edge crossing these two degree classes. Thus \(A_G=\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\), where \(B\) is a \(144\times432\) binary matrix having \(12\) ones per row and \(4\) per column. This entire calculation is a *finite exhaustive proof* because there are exactly \(576\) enumerated states and \(36\) candidate intercalates per state; no sampling or asymptotic inference enters.

**2. An exact \(144\)-state certificate.** Form \(Q=BB^{\mathsf T}\). The embedded algorithm checks all \(144^2\) entries and finds that each diagonal entry is \(12\) and every off-diagonal entry is either \(0\) or \(2\). Therefore
\[
Q=12I+2H
\]
for a simple, symmetric, \(18\)-regular \(144\times144\) adjacency matrix \(H\). A verifier uses only integer arithmetic to check the matrix identity
\[
H(H+6I)(H+2I)(H-6I)(H-18I)=0
\]
**on every one of the \(144\) coordinate vectors**. It independently accumulates the exact traces
\[
\bigl(\operatorname{tr}H^j\bigr)_{j=0}^{4}=(144,0,2592,10368,176256).
\]
As \(H\) is real symmetric, the matrix annihilation forces its eigenvalues into the five *distinct* possibilities \(\{-6,-2,0,6,18\}\). Solving the five trace equations \(\sum_{\lambda}m_\lambda\lambda^j=\operatorname{tr}H^j\), for \(j=0,1,2,3,4\), determines the multiplicities uniquely by the nonsingular Vandermonde matrix: they are \(15,81,8,39,1\), respectively. These values explicitly satisfy every displayed trace.

**3. Transfer to the flip graph.** The eigenvalues of \(Q=12I+2H\) are \(0\) (multiplicity \(15\)), \(8\) (multiplicity \(81\)), \(12\) (multiplicity \(8\)), \(24\) (multiplicity \(39\)), and \(48\) (multiplicity \(1\)). For a bipartite block adjacency matrix \(A_G\), every positive eigenvalue of \(BB^{\mathsf T}\) supplies the two adjacency eigenvalues \(\pm\sqrt\lambda\) with the same multiplicity; the other \(576-2(81+8+39+1)=318\) eigenvalues are zero. Multiplying the corresponding factors gives the stated polynomial. The positive eigenvalue \(\sqrt{48}\) is simple and of maximum modulus; equivalently the connectedness check in both embedded programs reaches all \(576\) vertices. The independent checker computes graph distances from *every* square and proves diameter \(6\).

**4. Exact lazy random-walk gap.** Since degrees are \(12\) and \(4\) on the two sides, the symmetrically normalized adjacency matrix \(D^{-1/2}A_GD^{-1/2}\) equals \(A_G/\sqrt{48}\) after corresponding bipartite ordering. Its eigenvalues are the displayed adjacency eigenvalues divided by \(\sqrt{48}\), and the largest eigenvalue below \(1\) is \(\sqrt{24}/\sqrt{48}=1/\sqrt2\). Laziness maps each normalized eigenvalue \(\theta\) to \((1+\theta)/2\). Consequently the second-largest lazy eigenvalue is \((1+1/\sqrt2)/2\), proving the gap. The stationary distribution of this walk is proportional to degree, not uniform across squares.

## Verification
Run the two Python 3 standard-library programs `verify_spectrum.py` and `verify_independent.py` in this package. The first generates and checks every square and intercalate switch, builds the \(144\times144\) exact intersection matrix, verifies the annihilating polynomial entrywise, and computes five exact power traces; output `verify_spectrum.log` records `EXACT_CERTIFICATE_OK`. The second enumerates squares by row-by-row backtracking, generates edges by explicit two-symbol transposition in pairs of rows, checks all \(576\) breadth-first distance searches, and reproduces the identical canonical adjacency fingerprint; `verify_independent.log` records `INDEPENDENT_GRAPH_OK`. Both methods encode each Latin square as a lexicographically ordered tuple of rows and hash the sorted lists of neighbor indices. The expected SHA-256 of the encoded adjacency lists is `07a20876e896ecc727c6a58253c4a4580fe3282b1d5262760b06bb940dbe113b`. The included scripts are complete and require no input data, unstated files, random choices, or nonstandard libraries.

## Relationship to prior work
Wanless's 2004 study of cycle switches develops intercalate switches and graphs on *isotopy or main classes* of Latin squares. In particular, its order-four switch graph has two class vertices, not the \(576\) individually labeled square vertices considered here. Its quotient result therefore does not determine the full labeled adjacency spectrum. A later, distinct analysis by Davis (2026, `spectral_branch.pdf` of the Zenodo record below) explicitly gives the \(576\)-vertex graph, its \(432{:}144\) degree partition and its Laplacian top-eigenspace characterization. Those previously recorded properties are not asserted as new here. The accessible publication description does not give the exact full adjacency characteristic polynomial or this lazy-walk spectral gap, but the attached PDF itself could not be examined and remains a material priority risk. Papers about the conventional \(16\)-vertex *Latin-square graph* concern a different object.

## Limitations
This is a complete exact finite result for order four; it does not assert formulas for general Latin-square orders or mixing times for a uniform distribution on labeled Latin squares. The displayed lazy-walk gap concerns the degree-biased stationary measure. The full text of the 2026 spectral-branch PDF was inaccessible despite inspection of its publisher-hosted record and preview; an equivalent earlier or contemporary spectrum computation hidden there or in unindexed literature cannot be excluded. No external independent scientific audit is claimed.

## References
1. I. M. Wanless, *Cycle Switches in Latin Squares*, Graphs and Combinatorics **20** (2004), 545–570. DOI: `10.1007/s00373-004-0567-7`. Author-hosted full text: `https://users.monash.edu.au/~iwanless/papers/cycleswapgr.GC.pdf`; dated author abstract: `https://users.monash.edu.au/~iwanless/abstracts/cycleswitch.html` (last modified 2004-09-08).
2. B. R. Davis, *The Field Equations of Semantic Coherence: A Geometric Theory of Meaning, Curvature, and Reasoning in Transformer Architectures*, Zenodo (2026-02-08), DOI: `10.5281/zenodo.18528388`, especially the publicly described `spectral_branch.pdf`, Section 7.5. Publisher record: `https://zenodo.org/records/18528388`. Its complete PDF was not available for inspection.
