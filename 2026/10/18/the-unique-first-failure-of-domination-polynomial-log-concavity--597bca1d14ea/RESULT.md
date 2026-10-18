# The unique first failure of domination-polynomial log-concavity in trivially perfect graphs

## Finding

**Theorem.** Let \(G\) range over all finite simple trivially perfect graphs, allowing disconnected graphs. If \(|V(G)|\le15\), the coefficient sequence of its ordinary domination polynomial is log-concave. At order \(16\) there is exactly one isomorphism class with non-log-concave domination polynomial:
\[
G\cong K_1\vee(K_5\sqcup K_5\sqcup K_5).
\]
For this graph, writing \(D(G;z)=\sum_{j=0}^{16}d_jz^j\),
\[
(d_0,d_1,\ldots,d_{16})=(0,1,15,230,1205,3615,7378,11080,12735,11410,8005,4368,1820,560,120,16,1).
\]
In particular \(d_2^2=225<230=d_1d_3\). Thus the least order of a trivially perfect graph with a non-log-concave ordinary domination polynomial is exactly \(16\), and the least-order example is unique up to isomorphism.

## Assumptions and scope

A set \(S\subseteq V(G)\) is *dominating* if every vertex belongs to \(S\) or has a neighbor in \(S\). The coefficient \(d_j\) counts dominating vertex subsets of cardinality \(j\). A finite sequence of nonnegative coefficients is *log-concave* if \(d_j^2\ge d_{j-1}d_{j+1}\) for every index between its endpoints. A trivially perfect graph is equivalently a graph built from singleton vertices using disjoint unions and the addition of universal vertices, or the ancestor-comparability graph of a rooted forest. Both connected and disconnected cases are included. The claim concerns log-concavity, **not** a failure of unimodality: the exhibited polynomial remains unimodal.

## Proof

**Rooted decomposition.** Associate a rooted tree \(T\) with the graph \(C(T)\) in which distinct vertices are adjacent precisely when one is an ancestor of the other. The root is universal. Removing it gives the disjoint union of \(C(T_i)\), where \(T_i\) are the root's child subtrees. Conversely every connected trivially perfect graph admits such a representation: choose any universal vertex and recurse into the connected components remaining after its removal. Every universal vertex of the same connected graph has the same closed neighborhood, and exchanging two such vertices is an automorphism. Consequently deleting any one universal vertex yields isomorphic remaining graphs, so the recursive rooted shape is unique up to permutation of isomorphic child subtrees. Thus unlabelled rooted-tree shapes index the isomorphism classes of connected trivially perfect graphs.

**Exact recurrence.** For the one-vertex rooted tree, \(D(C(T);z)=z\). For any other rooted tree \(T\) of order \(n\) with child subtrees \(T_1,\ldots,T_r\), partition dominating sets by whether they contain the root. Those containing it contribute \(z(1+z)^{n-1}\); those omitting it must dominate every child component separately, contributing the product. Since \(r\ge1\), every set counted in that product also dominates the omitted root. Hence
\[
D(C(T);z)=z(1+z)^{n-1}+\prod_{i=1}^r D(C(T_i);z).
\]
This equation and the singleton base case are exact, including every coefficient and every graph size.

**Exhaustive finite classification.** To prove the order cutoff, generate the unlabelled rooted-tree shapes of order \(n\) as all multisets of smaller rooted shapes whose total order is \(n-1\), with a new common root. Induction proves completeness: deleting the root of any rooted tree yields exactly such a multiset; sorting component types and enumerating nondecreasing index sequences counts each multiset once. The included standalone program implements precisely this recurrence using arbitrary-precision integers, computes each graph's domination polynomial by the displayed formula, and checks every log-concavity inequality. It enumerates respectively
\[
1,1,2,4,9,20,48,115,286,719,1842,4766,12486,32973,87811,235381
\]
rooted shapes at orders \(1\) through \(16\), for a total of \(376464\) connected graph classes. No coefficient failure occurs below \(16\); exactly one shape fails at order \(16\). That shape consists of one root above three chains of five vertices, giving \(K_1\vee 3K_5\). The program asserts these facts and exits unsuccessfully upon any disagreement. As a check independent of the polynomial recurrence, it also explicitly forms the ancestor-comparability edges and enumerates all vertex subsets for every shape of order at most \(7\), and all \(65536\) vertex subsets of the unique order-\(16\) witness; the coefficient vectors agree.

**Disconnected graphs.** Disjoint unions have domination polynomials equal to products of the component domination polynomials. Such polynomials have nonnegative log-concave coefficient sequences without internal zeros whenever each component does. The convolution of two nonnegative log-concave sequences without internal zeros is log-concave. One proof applies the nonnegativity of all \(2\)-by-\(2\) minors of the associated Toeplitz matrices, which is preserved under matrix multiplication, hence convolution. Since every component of a disconnected graph of order at most \(16\) has order at most \(15\), and all those connected components passed the exhaustive classification, no disconnected graph of order at most \(16\) can fail. Uniqueness follows.

**Independent witness calculation and extension.** More generally, for the windmill \(W_{3,m}=K_1\vee3K_m\), the same dominating-set split gives
\[
D(W_{3,m};z)=z(1+z)^{3m}+((1+z)^m-1)^3.
\]
For integers \(m\ge1\), its first positive coefficients obey \(d_1=1\), \(d_2=3m\), and \(d_3=\binom{3m}{2}+m^3\). Therefore
\[
d_1d_3-d_2^2=\frac{m(2m^2-9m-3)}2>0\quad\text{for all integers }m\ge5.
\]
This verifies the claimed order-\(16\) witness analytically and supplies an infinite family of further failures. It does not replace the finite exhaustive argument needed for least order and uniqueness.

## Verification

Run `python3 verify_trivially_perfect.py` in the directory containing the supplied program. The program uses only the Python standard library. It verifies the rooted-tree class counts, every polynomial and local log-concavity inequality for all \(376464\) connected classes of order at most \(16\), and direct vertex-subset domination counts for the specified independent tests. `verification_output.txt` is the recorded successful output. The exact coefficient vector above agrees with brute-force enumeration. All integer comparisons are exact; no numerical tolerances or sampled graph instances are used in the full rooted-tree census.

## Relationship to prior work

The June 24, 2025 article *On domination polynomials of some graphs* (DOI below), Section 2, Theorem 2.16, gives a general formula for domination polynomials of graphs formed by joining a clique to a disjoint union of cliques; this formula covers the **polynomial identity** for the exhibited windmill. Its discussion following Theorem 2.16 explicitly leaves log-concavity questions for the heterogeneous generalization open. The theorem here does **not** claim that known polynomial identity as novel; its assertion is the first-order and unique-isomorphism cutoff across **all** trivially perfect graphs, established by a separate exhaustive classification.

Omar's January 2026 preprint, especially Section 5 and Theorem 19, studies the domination-polynomial coefficient behavior of threshold graphs. Threshold graphs are a proper subclass of trivially perfect graphs; the present windmill is outside that subclass. Beaton and Schoonhoven's November 2024 work exhibits different non-log-concave domination polynomials in ordinary trees, a different graph class and construction. Comparisons with accessible mathematical-record summaries for generalized windmills concern other invariants (general-position, dissociation, and discounted hitting domination), rather than the ordinary domination-polynomial minimality assertion. These comparisons do not establish absolute bibliographic priority.

## Limitations

The least-order assertion is a finite computer-assisted proof, not an analytic inequality for every trivially perfect graph of arbitrary size. Completeness rests on the explicit multiset enumeration algorithm, its inductive justification, the exact recurrence, and the supplied executable checks; the console output alone is not a proof. The theorem does not resolve unimodality of general domination polynomials, and does not assert any independent audit or external certification. Bibliographic searches cannot rule out all inaccessible or unindexed prior sources; priority remains provisional.

## References

1. *On domination polynomials of some graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **126** (2025), 279–289; published online 2025-06-24, DOI: `10.61091/jcmcc126-19`, https://combinatorialpress.com/jcmcc-articles/volume-126/on-domination-polynomials-of-some-graphs/ . See Theorem 2.16 and the following open question.
2. Mohamed Omar, *New Perspectives On The Unimodality Of Domination Polynomials*, arXiv:`2601.14494`, first submitted 2026-01-20, https://arxiv.org/html/2601.14494v1 . See Section 5, Theorem 19.
3. Iain Beaton and Sam Schoonhoven, *On the unimodality of nearly well-dominated trees*, arXiv:`2411.02288`, first submitted 2024-11-04, https://arxiv.org/abs/2411.02288 . See Section 2.
4. OEIS A000081, *Number of unlabeled rooted trees with n nodes*, https://oeis.org/A000081 . Class counts provide an additional cross-check of the enumerator.
