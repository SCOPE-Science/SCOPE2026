# Minimum determining sets of Boolean annihilating-ideal graphs

## Finding

For every integer \(n\ge2\), let
\[
R_n=(\mathbb F_2)^n.
\]
The nonzero proper ideals of \(R_n\) are indexed by the nonempty proper subsets of \([n]\). Because coordinatewise multiplication is intersection of supports, the annihilating-ideal graph \(\mathbb{AG}(R_n)\) is the graph whose vertices are the nonempty proper subsets of \([n]\), with two distinct subsets adjacent exactly when they are disjoint. The same support model is the zero-divisor graph of \(R_n\).

Put
\[
k=\lceil\log_2 n\rceil.
\]
A \(k\)-vertex family
\[
D=\{S_1,\ldots,S_k\}
\]
is a minimum determining set if and only if the \(n\) coordinate-incidence words
\[
\sigma_D(i)=\bigl(\mathbf 1_{i\in S_1},\ldots,\mathbf 1_{i\in S_k}\bigr)\in\{0,1\}^k
\]
are pairwise distinct as \(i\) ranges over \([n]\).

Therefore
\[
\operatorname{Det}(\mathbb{AG}(R_n))=\lceil\log_2 n\rceil,
\]
and the exact number of minimum determining sets is
\[
\frac{(2^k)!}{(2^k-n)!\,k!}.
\]

For \(n=5\), this gives determining number \(3\) and exactly \(1120\) minimum determining sets. In particular, no two vertices can determine the Boolean graph on five coordinates.

## Assumptions and scope

The ring is the finite Boolean ring \(R_n=(\mathbb F_2)^n\) with \(n\ge2\). The annihilating-ideal graph has one vertex for each nonzero proper ideal and adjacency \(IJ=(0)\). Under the support identification, this is the disjointness graph on all nonempty proper subsets of \([n]\).

The result concerns determining sets, equivalently fixing sets. It does not assert a metric-dimension formula.

## Proof

Let \(B_n\) denote the support graph. For a vertex \(S\subset[n]\) of size \(s\), its neighbors are exactly the nonempty subsets of \([n]\setminus S\). Hence
\[
\deg(S)=2^{n-s}-1.
\]
The degree therefore determines \(|S|\). In particular, the singleton vertices are exactly the vertices of maximum degree, so every automorphism permutes the singleton layer.

Every vertex is reconstructed from that layer. Indeed,
\[
S=\{i\in[n]:\{i\}\text{ is not adjacent to }S\}.
\]
This identity also holds when \(S\) itself is a singleton because a vertex is not adjacent to itself. Thus an automorphism is completely determined by its permutation of the \(n\) singleton vertices. Conversely, every permutation of \([n]\) preserves disjointness. Therefore
\[
\operatorname{Aut}(B_n)\cong S_n.
\]

Now fix a family \(D=\{S_1,\ldots,S_t\}\) of vertices. Two coordinates \(i,j\in[n]\) have the same incidence word with respect to \(D\) exactly when every selected subset either contains both or contains neither. If their words agree, the transposition \((i\ j)\) fixes every member of \(D\) setwise, hence induces a nonidentity graph automorphism fixing \(D\) pointwise. Conversely, if all incidence words are distinct, any coordinate permutation fixing every member of \(D\) must fix each coordinate, so it is the identity. Thus \(D\) is determining exactly when its coordinate-incidence words are pairwise distinct.

With \(t\) selected subsets there are at most \(2^t\) possible incidence words, so every determining set satisfies
\[
2^t\ge n.
\]
Hence
\[
t\ge \lceil\log_2 n\rceil.
\]
For \(k=\lceil\log_2 n\rceil\), choose \(n\) distinct binary words of length \(k\) and let the \(j\)-th selected subset contain exactly the coordinates whose \(j\)-th bit is \(1\). Since
\[
n>2^{k-1},
\]
no bit position can be constant on all \(n\) chosen words, so every selected subset is nonempty and proper. This produces a determining set of size \(k\), proving the minimum formula.

For the count, order the \(k\) selected subsets temporarily. An ordered minimum determining family is exactly an injection
\[
[n]\longrightarrow\{0,1\}^k,
\]
so there are
\[
(2^k)(2^k-1)\cdots(2^k-n+1)=\frac{(2^k)!}{(2^k-n)!}
\]
ordered families. Because \(n>2^{k-1}\), two bit positions cannot agree on all chosen words; otherwise the image would lie in a \(2^{k-1}\)-point diagonal subcube. Thus the \(k\) selected subsets are distinct, and every unordered family has exactly \(k!\) orderings. Division by \(k!\) gives the stated count.

Finally, at \(n=5\), two selected subsets yield at most four distinct two-bit coordinate signatures. Two of the five coordinates must share a signature, so their transposition fixes both selected vertices. Hence no two-vertex family is determining.

## Verification

The standalone `verify.py` artifact was read from its packaged path before replay. It constructs the disjoint-support graph, checks the degree formula and graph-theoretic recovery of every subset from singleton nonadjacency, verifies that coordinate permutations preserve adjacency, and exhaustively enumerates all minimum candidate families for \(2\le n\le7\).

Exact replay output:

```text
n k minimum_set_count
2 1 2
3 2 12
4 2 12
5 3 1120
6 3 3360
7 3 6720
published_n5_two_set_obstruction 4
VERIFY_OK
```

The exhaustive counts are \(2,12,12,1120,3360,6720\) for \(n=2,3,4,5,6,7\), respectively, exactly matching the closed formula. The checker also verifies explicit optimal families for larger sample values through \(n=33\). The arbitrary-\(n\) theorem is proved combinatorially above; finite enumeration is only corroboration.

## Relationship to prior work

Behboodi and Rakeei introduced the annihilating-ideal graph and supplied the ring-theoretic object used here. Later annihilating-ideal work with primary commutative-algebra classification \(13A15\) confirms the algebraic ownership of this graph family.

Ou, Wong, Tian, and Zhou explicitly study the fixing number of the zero-divisor graph of products of copies of \(\mathbb Z_2\). Their accessible abstract states that the value is obtained, but does not advertise a classification or count of all minimum fixing sets. Full text was not accessible from the checked lawful sources, so the possibility that their proof contains a stronger unadvertised classification remains a residual literature risk.

A 2026 paper on determining number and metric dimension of semisimple zero-divisor graphs gives, in its Boolean section, the formula \(\lfloor n/2\rfloor\) and specifically asserts a two-vertex determining set for \(n=5\). The coordinate-signature lower bound above shows that this cannot hold: two selected subsets supply only four binary incidence signatures for five coordinates. The present classification both supplies the sharp obstruction and counts every minimum set.

## Limitations

The theorem is specific to the Boolean semisimple ring \((\mathbb F_2)^n\). For products of larger fields, multiple ring elements share one support and large twin classes change the determining-set problem substantially.

The originality comparison with the 2020 fixing-number paper is limited by lack of full-text access. Its abstract confirms coverage of the numerical fixing-number problem for the same graph, so the value itself is not relied upon as the sole originality contribution; the substantive claim is the complete minimum-set classification and exact enumeration, together with the explicit correction of the later Boolean-case formula.

## References

1. M. Behboodi and Z. Rakeei, “The Annihilating-Ideal Graph of Commutative Rings I,” arXiv:0808.3187, first submitted 23 August 2008; Journal of Algebra and Its Applications 10 (2011), 727–739.
2. H. Yu and T. Wu, “Commutative Rings \(R\) Whose \(C(\mathbb{AG}(R))\) Consist of Only Triangles,” Communications in Algebra 43 (2015), 1076–1097, DOI 10.1080/00927872.2013.847950.
3. S. Ou, D. Wong, F. Tian, and Q. Zhou, “Fixing number and metric dimension of a zero-divisor graph associated with a ring,” Linear and Multilinear Algebra 69 (2021), 1789–1802, DOI 10.1080/03081087.2020.1815639.
4. “On determining number and metric dimension of zero-divisor graph of semisimple rings,” Ars Combinatoria 168 (2026), 29–48, DOI 10.61091/ars168-03.
