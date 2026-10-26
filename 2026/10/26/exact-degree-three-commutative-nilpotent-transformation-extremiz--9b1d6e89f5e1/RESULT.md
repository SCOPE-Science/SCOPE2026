# Exact degree-three commutative nilpotent transformation extremizers through seven points

## Finding
For \(n\in\{4,5,6,7\}\), let \(M_3(n)\) be the maximum cardinality of a commutative subsemigroup \(S\) of the full transformation semigroup \(\mathcal T_n\) such that \(S^3=\{e\}\) and \(S^2\ne\{e\}\), where \(e\) is the zero of \(S\). Then
\[
(M_3(4),M_3(5),M_3(6),M_3(7))=(3,6,12,36).
\]
Every maximizing semigroup has constant zero, and **all** maximizers belong to the explicit construction below. The numbers of labeled maximizing semigroups are, respectively,
\[
24,\quad120,\quad1080,\quad2520.
\]
Up to conjugation by a permutation of the underlying points, the numbers of extremal families are \(1,1,2,1\), respectively. The two six-point types are distinguished by a subset of size \(2\) versus \(3\) in the construction. In particular, the seven-point case has precisely \(2520\) labeled maximizers and a single conjugacy type.

## Assumptions and scope
Let \(X\) be a labeled set of \(n\) points, and let the composition convention be \((f\circ g)(x)=f(g(x))\). An absorbing element \(e\) of a transformation semigroup satisfies \(ef=fe=e\) for all \(f\in S\). The condition \(S^3=\{e\}\), \(S^2\ne\{e\}\) means *nilpotency degree exactly three*; it is stronger than individual cubical nilpotence. No assumption that \(e\) is constant is made before the proof.

Here is the common construction for all extremizers. Pick a point \(0\in X\), a subset \(A\subset X\) of size \(t\ge2\) containing \(0\), and let \(B=X\setminus A\) have \(b\ge2\) points. Choose distinct \(z,y\in B\) and a point \(u\in A\setminus\{0\}\). Define \(N\) to consist of all maps that send every point of \(A\cup\{z\}\) to \(0\) and send each point of \(B\setminus\{z\}\) arbitrarily into \(A\). Define \(F\) to consist of all maps that send all points of \(A\) to \(0\), send \(z\) to \(u\), send \(y\) to \(z\), and send all points of \(B\setminus\{z,y\}\) arbitrarily into \(A\). Put \(S=N\cup F\).

For these families, \(|S|=t^{b-1}+t^{b-2}=(t+1)t^{b-2}\). In the claimed optimal cases \((n,t)=(4,2),(5,2),(6,2),(6,3),(7,3)\).

## Proof
**1. The constructed sets are semigroups of degree three.** Any two maps in \(N\) compose to the constant \(0\) map; so does any composition between \(N\) and \(F\), in either order. Every ordered product of two maps in \(F\) equals the same map \(p\), which sends \(y\) to \(u\) and all other points to \(0\). This map belongs to \(N\) and is not constant. Consequently \(S\) is commutative and closed, \(S^2\ne\{e\}\), and every threefold product equals \(e\). The cardinality formula follows from the independent free images of \(b-1\) points in \(N\) and \(b-2\) points in \(F\).

**2. Reduction to a commuting graph for constant zero.** After conjugating the constant zero point to \(0\), any element of a degree-three semigroup must satisfy \(f(0)=0\) and \(f^3(x)=0\) for every \(x\in X\). Thus it belongs to the explicitly enumerable set
\[
V_n=\{f:X\to X:f(0)=0,\ f^3(x)=0\text{ for every }x\in X\}.
\]
Form a graph on \(V_n\) in which two distinct vertices are adjacent exactly when they commute. A degree-three commutative transformation semigroup of constant zero is a clique in this graph; it is *nonnull* if some ordered product of two (possibly equal) members is nonconstant. A nonnull clique of size \(k\) can be extended to a maximal graph clique, which remains nonnull and has size at least \(k\). Closure is not assumed in this upper-bound reduction; including all commuting families only enlarges the search space.

**3. Exhaustive and reproducible graph classification.** The standalone program `verify.py` creates **every** tuple \((f(0),\ldots,f(n-1))\) with \(f(0)=0\) and checks the equality \(f^3(x)=0\) at every point. It creates each edge by comparing the full tuples of \(f\circ g\) and \(g\circ f\), then enumerates all maximal cliques with an exact, finite Bron–Kerbosch implementation provided by NetworkX. For each maximal clique of size at least the independently constructed lower bound it tests the actual products to decide whether it is nonnull. The resulting counts are:

| \(n\) | \(|V_n|\) | commuting edges | maximal graph cliques | largest nonnull clique | nonnull maximal cliques of that size |
|---:|---:|---:|---:|---:|---:|
| 4 | 16 | 33 | 12 | 3 | 6 |
| 5 | 101 | 604 | 134 | 6 | 24 |
| 6 | 756 | 13610 | 3020 | 12 | 180 |
| 7 | 6607 | 375996 | 138662 | 36 | 360 |

The code separately builds all proposed families for each row, verifies their products and their degree-three condition, and checks **equality of the entire sets of extremal cliques and constructed families**, not merely equality of their counts. Because any nonnull clique larger than the displayed bound would lie in a nonnull maximal clique of at least that size, this exhaustive check establishes the stated upper bound and exact classification. This is a finite computational proof, not a numerical sampling argument.

**4. Nonconstant zero cannot attain the bound.** An absorbing map \(e\) is idempotent. Its fibers \(e^{-1}(x)\) for \(x\in\operatorname{Im}(e)\) are invariant under every member of \(S\), with \(x\) fixed. Restriction to all fibers gives an injection of \(S\) into the product of the corresponding rooted transformation semigroups. At least one fiber must witness a nonconstant twofold product. Such a fiber has at least four points. In the present range, if \(e\) has more than one image point, the possible largest-fiber configurations are bounded above by the previous degree-three maxima, multiplied by the already known general commutative-nilpotent maxima \(\xi(k)=\max_{1\le t\le k}t^{k-t}\) on all other fibers. The resulting upper bounds for total sizes \(n=5,6,7\) are, respectively, \(3,6,12\), strictly below \(6,12,36\); no such configuration exists at \(n=4\). The fiber bounds use the established general extremal theorem of Cain–Malheiro–Paulista and the already proved smaller cases, not the current seven-point result circularly.

**5. Labeled and conjugacy classification.** Within a constructed semigroup, \(A\) is exactly the set of points sent to \(0\) by every element, \(z\) is the unique image point outside \(A\), \(y\) is the unique source mapped to \(z\) by an element, and \(u\) is the unique nonzero value assumed at \(z\). Thus the parameters are recovered from \(S\) itself. For each fixed zero point the number of constructed families of type \(t\) is
\[
\binom{n-1}{t-1}(n-t)(n-t-1)(t-1).
\]
The exact maximal-clique counts above equal the sums of these parameter counts for the listed optimal values of \(t\). Multiplication by \(n\), since the constant zero point is uniquely determined, gives the labeled totals stated above. All constructions with the same \(t\) are conjugate under the symmetric group, and different \(t\) yield different sizes of the recoverable subset \(A\). This proves the orbit counts.

## Verification
Execute `python verify.py` after installing the documented dependency in `requirements.txt`. The verifier checks every possible cube-zero transformation and every commuting edge at each specified size; it then checks all maximal cliques of relevant size and equality with the explicit constructed semigroups. Recorded output is in `verification_output.txt`. The use of a maximal-clique enumerator is sufficient because every clique extends to a maximal clique in a finite graph. The source is inspectable and uses exact integer/tuple comparisons; no random tests, heuristics, or floating-point tolerances enter the proof.

## Relationship to prior work
Cain, Malheiro and Paulista (first posted 2023) show that the largest commutative nilpotent subsemigroups of \(\mathcal T_n\), *without fixing the nilpotency degree*, are null and have order \(\xi(n)\). Their published proof also supplies the useful invariant-fiber reduction and an illustrative smaller degree-three example. Their unrestricted maxima in the four cases here are \(4,9,27,81\). These do not determine the sharp maxima under the nonnull constraint \(S^2\ne\{e\}\), nor the counts or conjugacy types of these extremizers. Distler and Mitchell (2012) count abstract nilpotent semigroup multiplication tables of degree three by the *order of the abstract semigroup*, not embeddings as commutative subsemigroups of full transformation monoids of prescribed degree \(n\). No equivalence between their enumeration and this constrained embedding-maximization is available from their theorem. The exact cutoff and complete extremizer classification above are therefore a distinct, bounded extremal statement.

## Limitations
The exhaustive upper-bound proof covers only \(4\le n\le7\). The explicit construction exists for every \(n\ge4\) and gives a general lower bound, but **no formula or classification of global optimizers for \(n\ge8\) is claimed**. The result depends on a finite, replayable computational enumeration; no short handwritten proof of the relevant maximal-clique counts is supplied. An unlocated independent enumeration or a more general extremal theorem could still cover this bounded result. Independent validation is not asserted.

## References
1. A. J. Cain, A. Malheiro and T. Paulista, *Commutative nilpotent transformation semigroups*, arXiv:2310.08481v1 (posted 2023-10-12); *Semigroup Forum* **109** (2024), 60–75. https://arxiv.org/abs/2310.08481 ; https://doi.org/10.1007/s00233-024-10444-8 .
2. A. Distler and J. D. Mitchell, *The number of nilpotent semigroups of degree 3*, arXiv:1201.3529 (2012); *Electronic Journal of Combinatorics* **19** (2012), P51. https://arxiv.org/abs/1201.3529 .
3. P. J. Cameron et al., results on largest null subsemigroups as cited in Cain–Malheiro–Paulista, Theorems 2.2–2.3; see the original reference list there.
