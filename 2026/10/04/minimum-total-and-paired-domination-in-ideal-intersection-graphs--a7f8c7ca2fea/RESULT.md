# Minimum total and paired domination in ideal-intersection graphs of finite principal ideal rings

## Finding

Let \(R\cong\prod_{i=1}^{r}R_i\) be a finite commutative principal ideal ring, where each \(R_i\) is a finite chain ring with maximal-ideal nilpotency length \(\ell_i\ge1\), counting a field factor as \(\ell_i=1\). Let \(G(R)\) be the simple intersection graph on the nonzero proper ideals of \(R\). A two-vertex set \(\{I_a,I_b\}\) is total dominating if and only if, for the active supports \(\sigma(a)=\{i:a_i<\ell_i\}\) and \(\sigma(b)=\{i:b_i<\ell_i\}\), one has \(\sigma(a)\cap\sigma(b)\ne\varnothing\) and \(\sigma(a)\cup\sigma(b)=[r]\). Hence total and paired domination exist except when \(R\) is a field, a local chain ring of nilpotency length \(2\), or a product of exactly two fields; whenever they exist, \[\gamma_t(G(R))=\gamma_{\mathrm{pr}(G(R))=2.\] The minimum total dominating sets and minimum paired dominating sets coincide, and their exact number is \[\frac12\left(\prod_{i=1}^{r}\ell_i(\ell_i+2)-(2^r+1)\prod_{i=1}^{r}\ell_i-2\prod_{i=1}^{r}(\ell_i+1)+4\right).\]

The formula depends only on the nilpotency lengths of the local factors, not on their residue-field sizes. For \(R=\mathbb Z/n\mathbb Z\) with \(n=\prod_i p_i^{\ell_i}\), it therefore becomes an explicit prime-exponent formula for both strengthened domination parameters and for the number of all minimum sets.

## Assumptions and scope

Write
\[
R\cong R_1\times\cdots\times R_r,
\]
where each \(R_i\) is a finite local principal ideal ring. Let \(\mathfrak m_i\) be its maximal ideal and let \(\ell_i\ge1\) satisfy
\[
\mathfrak m_i^{\ell_i}=0,
\qquad
\mathfrak m_i^{\ell_i-1}\ne0.
\]
For a field factor, \(\mathfrak m_i=0\) and \(\ell_i=1\).

Every ideal of \(R_i\) is one of
\[
R_i=\mathfrak m_i^0,\mathfrak m_i,\ldots,\mathfrak m_i^{\ell_i}=0.
\]
Thus every ideal of \(R\) has a unique exponent vector
\[
a=(a_1,\ldots,a_r),
\qquad
0\le a_i\le\ell_i,
\]
and will be written
\[
I_a=\prod_i\mathfrak m_i^{a_i}.
\]
The graph \(G(R)\) has the nonzero proper ideals as vertices and joins distinct ideals exactly when their intersection is nonzero.

For an exponent vector define its active support by
\[
\sigma(a)=\{i:a_i<\ell_i\}.
\]
The zero ideal has empty active support, while the whole ring has full active support and is excluded from the graph.

## Proof

Because the ideals in a chain ring are linearly ordered,
\[
\mathfrak m_i^{a_i}\cap\mathfrak m_i^{b_i}
=
\mathfrak m_i^{\max(a_i,b_i)}.
\]
Therefore
\[
I_a\cap I_b\ne0
\iff
\sigma(a)\cap\sigma(b)\ne\varnothing.
\tag{1}
\]

Consider two distinct vertices \(I_a,I_b\). If \(\{I_a,I_b\}\) is total dominating, then its two vertices must be adjacent, so (1) gives
\[
\sigma(a)\cap\sigma(b)\ne\varnothing.
\tag{2}
\]
Also, for every coordinate \(k\), the ideal
\[
W_k=0\times\cdots\times0\times\mathfrak m_k^{\ell_k-1}\times0\times\cdots\times0
\]
has active support \(\{k\}\). If \(k\notin\sigma(a)\cup\sigma(b)\), then \(W_k\) intersects neither selected ideal nontrivially, contradicting total domination. Hence
\[
\sigma(a)\cup\sigma(b)=[r].
\tag{3}
\]

Conversely, suppose (2) and (3) hold. The selected vertices dominate one another by (2). Any graph vertex \(I_c\) has nonempty active support. Choose \(k\in\sigma(c)\). By (3), \(k\) belongs to \(\sigma(a)\) or \(\sigma(b)\), so (1) shows that \(I_c\) meets at least one selected ideal nontrivially. Thus the pair is total dominating. This proves the exact two-set classification.

A simple graph has no one-vertex total dominating set. Therefore, whenever a pair satisfying (2)-(3) exists,
\[
\gamma_t(G(R))=2.
\]
The same pair induces one edge, hence a perfect matching, so it is paired dominating and
\[
\gamma_{\mathrm{pr}}(G(R))=2.
\]
Conversely every two-vertex paired dominating set is total dominating, so the minimum total and paired sets coincide.

It remains to identify the existence boundary. If \(r=1\), every graph vertex has full active support and there are exactly \(\ell_1-1\) vertices. A qualifying pair exists exactly when \(\ell_1\ge3\). If \(r=2\) and \(\ell_1=\ell_2=1\), the graph consists of two disjoint singleton-support vertices, so no qualifying pair exists. If \(r=2\) and at least one length exceeds one, a full-support proper ideal exists and forms a qualifying pair with any suitable singleton-support ideal. If \(r\ge3\), supports \([r]\setminus\{1\}\) and \([r]\setminus\{2\}\) already satisfy (2)-(3). This gives exactly the three exceptional ring types stated in the finding.

For the count, put
\[
L=\prod_i\ell_i,
\qquad
B=\prod_i(\ell_i+1),
\qquad
P=\prod_i\ell_i(\ell_i+2).
\]
Among all ordered pairs of ideals, including \(0\) and \(R\), the number whose active supports have union \([r]\) is \(P\): in coordinate \(i\), every ordered exponent pair is allowed except \((\ell_i,\ell_i)\), giving \((\ell_i+1)^2-1=\ell_i(\ell_i+2)\) choices. Removing pairs involving the zero ideal and then the whole ring leaves
\[
P-2L-2B+3
\]
ordered graph-vertex pairs with full support union.

Among these, the ordered pairs with disjoint active supports are obtained by a nontrivial ordered bipartition of \([r]\). Each bipartition contributes \(L\) pairs, so their number is
\[
L(2^r-2).
\]
The only remaining diagonal ordered pairs are the \(L-1\) proper full-support ideals paired with themselves. Subtracting these and dividing by two gives
\[
\frac12\left(P-(2^r+1)L-2B+4\right),
\]
which is the stated formula.

## Verification

The accompanying `verify.py` independently builds the exponent-vector graph from the chain lengths and exhaustively checks every two-vertex set against the graph-theoretic total-domination definition. It verifies the support characterization, the existence boundary, equality with paired domination at the minimum, and the counting formula for local lengths through \(7\), all two-factor tuples with lengths through \(4\), all tested three-factor tuples, and representative four-factor tuples.

A separate layer constructs the actual ideal-intersection graph of \(\mathbb Z/n\mathbb Z\) from divisors and least common multiples for every composite \(4\le n\le120\), then checks the same formula from the prime-exponent vector.

Tail of the exact replay output:

```text
Z/108Z exponents=(2, 3) vertices=10 min_pairs=35
Z/110Z exponents=(1, 1, 1) vertices=6 min_pairs=3
Z/111Z exponents=(1, 1) vertices=2 min_pairs=0
Z/112Z exponents=(4, 1) vertices=8 min_pairs=18
Z/114Z exponents=(1, 1, 1) vertices=6 min_pairs=3
Z/115Z exponents=(1, 1) vertices=2 min_pairs=0
Z/116Z exponents=(2, 1) vertices=4 min_pairs=3
Z/117Z exponents=(2, 1) vertices=4 min_pairs=3
Z/118Z exponents=(1, 1) vertices=2 min_pairs=0
Z/119Z exponents=(1, 1) vertices=2 min_pairs=0
Z/120Z exponents=(3, 1, 1) vertices=14 min_pairs=40
VERIFY_OK
```

The computation is finite corroboration only. The arbitrary-ring result is proved by (1), the singleton-support witnesses \(W_k\), and the exact counting argument above.

## Relationship to prior work

Jafari and Jafari Rad study ordinary domination in intersection graphs of ideals and modules. Their primary subject classification is algebraic, and their ring section proves that the ordinary domination number of an intersection graph of a commutative ring is at most two; for Artinian rings it is two exactly for products of fields. Their paper does not define or treat total or paired domination.

Abu Osba, Al-Addasi, and Abughneim treat the exact finite commutative principal ideal ring family. They describe the product-of-local-rings ideal structure and prove that ordinary domination is one except for products of fields, where it is two. Their full text contains no occurrence of “total domination” or “paired.” The present theorem is not the ordinary domination formula: it classifies every minimum total and paired set, identifies the exceptional cases where strengthened domination does not exist despite ordinary domination being defined, and gives a closed count depending on all local nilpotency lengths.

Khojasteh later studies \(G(\mathbb Z_m)\) and a module-relative extension, computing ordinary domination and other invariants. The accessible abstract again concerns ordinary domination, not the strengthened parameters. This later paper is useful as a same-object comparison but is not needed for the proof.

## Limitations

The ring must be a finite commutative principal ideal ring. In a general finite commutative ring, local ideal lattices need not be chains, so adjacency is not determined solely by active-support intersection and the formula need not hold.

The result determines only the minimum total and paired sets; it does not enumerate all larger total or paired dominating sets.

The numerical formula depends on the local nilpotency lengths, so it does not distinguish principal ideal rings having the same length tuple but different residue fields.

The 2019 \(\mathbb Z_m\) paper was compared through its accessible abstract rather than a full text. That is recorded as a residual originality risk; no negative claim about uninspected material is used in the proof or acceptance argument.

## References

1. S. H. Jafari and N. Jafari Rad, “Domination in the intersection graphs of rings and modules,” *Italian Journal of Pure and Applied Mathematics* 28 (2011), 17–20.
2. E. Abu Osba, S. Al-Addasi, and O. Abughneim, “Some Properties of the Intersection Graph for Finite Commutative Principal Ideal Rings,” *International Journal of Combinatorics* 2014, Article 952371. DOI: 10.1155/2014/952371.
3. S. Khojasteh, “The intersection graph of ideals of \(\mathbb Z_m\),” *Discrete Mathematics, Algorithms and Applications* 11 (2019), 1950037. DOI: 10.1142/S179383091950037X.
