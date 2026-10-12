# Five monomial-equivalence classes of optimal \((5,3,7;1)\) Reed--Solomon sunflowers

## Finding
For each injective ordered vector \(\alpha=(\alpha_1,\ldots,\alpha_5)\in\mathbb F_7^5\), put
\[
 C_\alpha=\{(f(\alpha_1),\ldots,f(\alpha_5)): f\in\mathbb F_7[T],\ \deg f<3\}.
\]
Consider unordered families of **ten distinct** such codes satisfying
\[
 C_\alpha\cap C_\beta=\langle(1,1,1,1,1)\rangle_{\mathbb F_7}
 \quad\text{for every pair of different members.}
\]
Such families are maximum-size \((5,3,7;1)\) Reed--Solomon sunflowers. Up to ambient monomial equivalence, there are **exactly five** classes. Their numbers of distinct labeled families, and their coordinate-permutation stabilizer orders, are respectively
\[
 (6,12,30,30,60),\qquad(20,10,4,4,2).
\]
Their stabilizers are, in the same order, isomorphic to
\[
 \operatorname{AGL}(1,5),\quad D_{10},\quad C_4,\quad C_4,\quad C_2.
\]
Here \(D_{10}\) denotes the dihedral group of order ten. In particular, the two size-thirty classes are inequivalent despite having isomorphic stabilizers. The prior exact optimum of ten and the aggregate count of 138 labeled families are used as context, rather than claimed as separate new conclusions.

## Assumptions and scope
The ambient vector space is the fixed ordered coordinate space \(\mathbb F_7^5\). A monomial equivalence is a permutation of coordinates followed by nonzero coordinate scalings, applied uniformly to all subspaces in a family. No arbitrary ambient \(\operatorname{GL}(5,7)\) change of basis is allowed. All code dimensions and intersections are over \(\mathbb F_7\). The common center is the constant-vector line, and a family comprises ten **different code subspaces**, not ten evaluation vectors that might represent duplicates. The field \(\mathbb F_7\) has no nontrivial field automorphisms, so semilinear monomial equivalence agrees with monomial equivalence here.

For compactness, the string `01234` denotes the code whose normalized evaluation vector is \((0,1,2,3,4)\). The following are representatives of the five classes; each row lists its ten distinct normalized evaluation strings:

| Orbit size | Stabilizer order | Representative ten-code family |
|---:|---:|---|
| \(6\) | \(20\) | `01234,01326,01354,01425,01523,01564,01624,01635,01643,01652` |
| \(12\) | \(10\) | `01234,01253,01342,01364,01425,01456,01536,01562,01623,01645` |
| \(30\) | \(4\) | `01234,01245,01253,01326,01354,01365,01463,01564,01624,01652` |
| \(30\) | \(4\) | `01234,01246,01263,01342,01436,01465,01523,01562,01632,01653` |
| \(60\) | \(2\) | `01234,01245,01326,01354,01463,01523,01564,01624,01635,01652` |

## Proof
**Exhaustive normalization.** Every injective five-tuple has a unique affine renormalization with first two entries \(0,1\). Replacing \(\alpha\) by \(a\alpha+b\), where \(a\ne0\), preserves \(C_\alpha\), since composition with an affine polynomial preserves all polynomials of degree below three. The converse follows from the evaluation-code equality criterion of Con--Gruica--Montanucci--Zullo, Lemma 3.1: since \(5>2(3-1)\), equal code subspaces imply affine-related tuples. Therefore the 60 normalized tuples \((0,1,a,b,c)\) with distinct \(a,b,c\in\{2,3,4,5,6\}\) enumerate **all** distinct relevant codes exactly once.

**Exact compatibility test.** The code \(C_\alpha\) is the row span of the matrix with rows \((1)_i\), \((\alpha_i)_i\), and \((\alpha_i^2)_i\). Each has dimension three, and any two contain the same one-dimensional constant line. Hence
\[
 \dim(C_\alpha\cap C_\beta)=6-\operatorname{rank}\begin{pmatrix}
 (1)_i\\ (\alpha_i)_i\\ (\alpha_i^2)_i\\ (1)_i\\ (\beta_i)_i\\ (\beta_i^2)_i
 \end{pmatrix}.
\]
Deleting the repeated constant row gives the transpose of a five-by-five matrix with rows \((1,\alpha_i,\alpha_i^2,\beta_i,\beta_i^2)\). Thus the intersection has dimension one **if and only if** this latter matrix has rank five over \(\mathbb F_7\). The exact verifier computes all \(\binom{60}{2}=1770\) comparisons and obtains a 40-regular graph on 60 vertices with 1200 compatible pairs.

**All extremal families.** Sunflowers with this center correspond precisely to cliques of the compatibility graph. Complete Bron--Kerbosch enumeration of *every* maximal clique gives the cardinality histogram
\[
 \{6:30,\ 7:1920,\ 8:5070,\ 9:1800,\ 10:138\}.
\]
A separate recursion that directly lists all increasing ten-vertex cliques produces the same 138 cliques. The first enumeration proves that none has more than ten vertices. Both enumerations use exact integer arithmetic; their finite domains and recursion logic are included in `verify.py`.

**Exact equivalence relation and orbit exhaustion.** Any monomial operator carrying one such family to another must carry the intersection of all petals, namely \(\langle\mathbf1\rangle\), to itself. Applied to \(\mathbf1\), a monomial operator yields its diagonal scaling factors in permuted order. Those factors must all coincide, so the operator is a global nonzero scalar times a coordinate permutation. The common scalar acts trivially on subspaces. Therefore **the entire allowable monomial equivalence is precisely the action of \(S_5\)**, of order 120.

For each \(\sigma\in S_5\), the action on a normalized tuple \(\alpha\) is obtained by permuting the five entries to \(b_i=\alpha_{\sigma(i)}\) and renormalizing:
\[
 b_i\longmapsto (b_i-b_1)/(b_2-b_1)\quad\text{in }\mathbb F_7.
\]
The denominator never vanishes by injectivity. Applying all 120 such transformations to each ten-code family partitions the exhaustive collection of 138 families into five disjoint orbits of sizes \(6,12,30,30,60\). The stabilizer orders are \(120\) divided by these orbit sizes, and direct element-order enumeration gives the fingerprints
\[
 \{1^1,2^5,4^{10},5^4\},\quad\{1^1,2^5,5^4\},\quad
 \{1^1,2^1,4^2\},\quad\{1^1,2^1,4^2\},\quad\{1^1,2^1\}.
\]
These identify the displayed group types. The orbit-size sum is \(138\), so the five representatives account for **every** maximum family; neither a sixth class nor an unidentified optimizer can remain.

## Verification
Run `python3 verify.py` from this package, using Python 3.9 or later and only the standard library. The script regenerates all 60 distinct evaluation codes, recomputes the rank-five compatibility graph, independently enumerates maximal cliques and size-ten cliques, forms every \(S_5\) action, and checks all five orbit and stabilizer fingerprints. The expected terminal line is `VERIFY_OK`. The displayed representatives are printed by the script, and the entire proof is a finite exact enumeration rather than statistical sampling.

## Relationship to prior work
Con, Gruica, Montanucci, and Zullo (2026) introduced Reed--Solomon sunflowers, their generalized \(V\)-matrix criterion, and the general extremal problem; they provide large-family constructions and asymptotic counting bounds, not the five coordinate-equivalence classes above. Etzion and Raviv (2015) study general Grassmannian sunflowers and partial spreads, without imposing Reed--Solomon algebraic structure or classifying these optimal Reed--Solomon families. Earlier finite work at these same parameters already determines the numerical optimum and counts maximal cliques; those facts alone do **not** determine how its 138 optimizers split into equivalence classes, nor their stabilizer groups. The contribution here is exclusively the complete **symmetry classification of the optimizers**.

## Limitations
The classification is for \(q=7\), length five, dimension three, and the standard one-dimensional center, under monomial equivalence in the specified coordinate space. It makes no claim for other fields, lengths, dimensions, arbitrary ambient linear equivalence, or alternate centers. Exhaustive arithmetic supports a finite classification, not an asymptotic theorem. Independent verification outside this package has not been performed.

## References
1. R. Con, A. Gruica, M. Montanucci, and F. Zullo, *Sunflowers of Reed--Solomon Codes*, arXiv:2609.33512v1 (first public 2026-09-27), especially Lemma 3.1, Theorem 2.6, Corollary 3.3, Proposition 3.23, and Section 5.
2. T. Etzion and N. Raviv, *Equidistant Codes in the Grassmannian*, Discrete Applied Mathematics **186** (2015), 87--97; arXiv:1308.6231, especially Section 2.3 on general sunflower/partial-spread equivalence.
