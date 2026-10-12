# Determining sets of reduced comaximal graphs: a Boolean phase transition
## Finding

Let
\[
R=\prod_{i=1}^r\mathbb F_{q_i},\qquad r\ge2,
\]
and let \(G=CG_J(R)\). Since \(R\) is reduced and semisimple, \(J(R)=0\), so the vertices of \(G\) are precisely the nonzero nonunits of \(R\). Two distinct vertices are adjacent exactly when they generate \(R\).

For a vertex \(x\), write
\[
Z(x)=\{i:x_i=0\}.
\]
For every nonempty proper subset \(Z\subset[r]\), put
\[
C_Z=\{x:Z(x)=Z\},\qquad
m_Z=|C_Z|=\prod_{i\notin Z}(q_i-1).
\]
Also put
\[
N=|V(G)|=\prod_iq_i-\prod_i(q_i-1)-1
\]
and
\[
t=|\{i:q_i=2\}|.
\]

If at least one field factor has order larger than \(2\), then a set \(S\subseteq V(G)\) is determining if and only if
\[
|C_Z\setminus S|\le1
\]
for every nonempty proper \(Z\subset[r]\).

Consequently, if
\[
\Delta(G;x)=\sum_{S\text{ determining}}x^{|S|},
\]
then
\[
\Delta(G;x)
=
(1+x)^{2^t-1}
\prod_{\substack{\varnothing\ne Z\subsetneq[r]\\m_Z>1}}
\left(x^{m_Z}+m_Zx^{m_Z-1}\right).
\]
In particular,
\[
\operatorname{Det}(G)=N-(2^r-2),
\]
and the number of minimum determining sets is
\[
\prod_{\varnothing\ne Z\subsetneq[r]}m_Z
=
\prod_{i=1}^r(q_i-1)^{\,2^{r-1}-1}.
\]

There is a sharp Boolean boundary. If every \(q_i=2\), then \(G\) is the disjointness graph on the nonempty proper subsets of \([r]\). A family \(\mathcal F\) of its vertices is determining exactly when, for every distinct \(i,j\in[r]\), some \(A\in\mathcal F\) contains exactly one of \(i,j\). Equivalently, the \(r\) coordinate-incidence columns of \(\mathcal F\) are pairwise distinct. Hence
\[
\operatorname{Det}(G)=\lceil\log_2 r\rceil.
\]

Thus replacing even one binary factor by a larger field changes the mechanism from a logarithmic coordinate-separation problem to a forced all-but-one selection in every support fiber.

## Assumptions and scope

All rings are commutative with identity. The theorem concerns finite reduced nonfield rings written as products of finite fields. The graph is the reduced comaximal graph \(CG_J(R)\): vertices are nonunits outside \(J(R)\), and distinct vertices are adjacent when their generated ideals sum to \(R\).

The determining number is the minimum cardinality of a vertex set whose pointwise stabilizer in the graph automorphism group is trivial. The determining polynomial used here counts all determining sets by cardinality.

The theorem includes \(r=2\). The fully Boolean case is treated separately because every support fiber then has size \(1\), so the twin-class forcing mechanism disappears.

## Proof

Two vertices \(x\in C_Z\) and \(y\in C_W\) are adjacent exactly when
\[
Z\cap W=\varnothing.
\]
Indeed, coordinate \(i\) fails to be generated only when both \(x_i\) and \(y_i\) vanish. Thus each \(C_Z\) is an independent false-twin class, and the quotient on these classes is the graph \(D_r\) whose vertices are the nonempty proper subsets of \([r]\), with adjacency given by disjointness.

The quotient \(D_r\) is twin-free. For a subset \(Z\), adjacency to the singleton \(\{j\}\) records exactly whether \(j\notin Z\). Moreover
\[
\deg_{D_r}(Z)=2^{r-|Z|}-1,
\]
so an automorphism preserves \(|Z|\), in particular the singleton layer. Its permutation of singleton vertices is therefore a permutation of the coordinates, and adjacency to those singletons then determines the image of every subset. Hence
\[
\operatorname{Aut}(D_r)\cong S_r.
\]

Any graph automorphism of \(G\) preserves maximal false-twin classes and therefore induces an automorphism of \(D_r\). It also preserves their cardinalities. Since
\[
m_{[r]\setminus\{i\}}=q_i-1,
\]
the induced coordinate permutation can only permute coordinates having the same field order. Conversely such coordinate permutations preserve all fiber sizes and lift to graph automorphisms, while arbitrary permutations inside every \(C_Z\) are also automorphisms. This structural description is used only as a proof tool; the novelty claim below is the determining-set classification and enumerator.

Suppose first that some \(q_k>2\). If a determining set \(S\) omits two vertices from one class \(C_Z\), transposing those two false twins gives a nonidentity automorphism fixing \(S\) pointwise. Therefore every determining set satisfies
\[
|C_Z\setminus S|\le1.
\]

Conversely assume this inequality holds for every \(Z\). Every class with \(m_Z>1\) then contains a point of \(S\), so a pointwise stabilizer of \(S\) fixes that class setwise. For every nonbinary coordinate \(k\), the class indexed by
\[
[r]\setminus\{k\}
\]
has size \(q_k-1>1\), so the induced coordinate permutation fixes \(k\).

Now let \(j\) be a binary coordinate. If \(r=2\), the other coordinate is nonbinary and preservation of field orders already fixes \(j\). If \(r\ge3\), choose a nonbinary coordinate \(k\). The class indexed by
\[
[r]\setminus\{j,k\}
\]
has size
\[
(q_j-1)(q_k-1)=q_k-1>1.
\]
It is fixed setwise. Since \(k\) is already fixed, its complementary pair \(\{j,k\}\) being fixed setwise forces \(j\) to be fixed as well. Thus every coordinate is fixed. The induced quotient automorphism is the identity, and because all but at most one vertex in every nontrivial fiber are fixed pointwise, every remaining vertex is also fixed. Hence \(S\) is determining.

A singleton fiber occurs exactly when its nonzero support is a nonempty subset of the \(t\) binary coordinates. Because at least one coordinate is nonbinary, there are exactly
\[
2^t-1
\]
such fibers. A singleton fiber contributes \(1+x\) to the determining polynomial, while a fiber of size \(m_Z>1\) contributes
\[
x^{m_Z}+m_Zx^{m_Z-1},
\]
according as no vertex or exactly one vertex is omitted. Multiplying these independent choices proves the displayed determining polynomial.

There are \(2^r-2\) nonempty proper zero-sets. A minimum determining set omits exactly one vertex from each fiber, including the singleton fibers, so
\[
\operatorname{Det}(G)
=
\sum_Z(m_Z-1)
=
N-(2^r-2).
\]
The number of minimum sets is \(\prod_Zm_Z\). For a fixed coordinate \(i\), the factor \(q_i-1\) appears exactly when \(i\notin Z\), for
\[
2^{r-1}-1
\]
nonempty choices of \(Z\subseteq[r]\setminus\{i\}\). Hence
\[
\prod_Zm_Z
=
\prod_i(q_i-1)^{2^{r-1}-1}.
\]

Finally suppose every \(q_i=2\). Every \(C_Z\) is a singleton, so \(G=D_r\) and its automorphism group is \(S_r\) acting on coordinates. For a family \(\mathcal F\) of subsets, a coordinate permutation fixes every member of \(\mathcal F\) exactly when it permutes coordinates having identical incidence columns. Therefore the pointwise stabilizer is trivial exactly when all \(r\) incidence columns are distinct. With \(k\) selected subsets there are at most \(2^k\) possible columns, so
\[
k\ge\lceil\log_2r\rceil.
\]
Conversely, for \(k=\lceil\log_2r\rceil\), label the coordinates by \(r\) distinct binary words of length \(k\), and use the \(k\) coordinate rows as subsets. Taking the words \(0,1,\ldots,r-1\) makes every row nonempty and proper. These rows separate all coordinates, proving the upper bound.

## Verification

The standalone `verify.py` artifact uses only the Python standard library. It constructs the graph directly from the field-order tuple, exhaustively enumerates all graph automorphisms for four small cases, and then exhaustively searches all determining sets.

Its replay gives:

```text
CASE (2, 3) vertices 3 automorphisms 2 determining 1 minimum_sets 2
CASE (3, 3) vertices 4 automorphisms 8 determining 2 minimum_sets 4
CASE (2, 2, 2) vertices 6 automorphisms 6 determining 2 minimum_sets 12
CASE (2, 2, 3) vertices 9 automorphisms 16 determining 3 minimum_sets 8
FORMULA (2, 3, 3) determining 7 minimum_sets 64
FORMULA (3, 4, 5) determining 29 minimum_sets 13824
FORMULA (2, 2, 5, 3) determining 37 minimum_sets 2097152
BOOLEAN 2 determining 1
BOOLEAN 3 determining 2
BOOLEAN 4 determining 2
BOOLEAN 5 determining 3
BOOLEAN 6 determining 3
BOOLEAN 7 determining 3
BOOLEAN 8 determining 3
VERIFY_OK
```

Thus the exhaustive cases include both the Boolean boundary and mixed/nonbinary cases. The script also checks the closed minimum-size and minimum-set-count formulas on larger parameter tuples and constructs explicit Boolean separating families for \(2\le r\le8\).

These finite computations are corroborative. The arbitrary-rank result follows from the false-twin partition and the exact coordinate action proved above.

## Relationship to prior work

Moconja and Petrović gave the support-class decomposition of the reduced comaximal graph of a semilocal ring: vertices in the same maximal-ideal membership class have identical external neighborhoods, and the quotient is governed by disjointness of index sets. Their paper is the structural starting point used here.

Khashyarmanesh, Mehdi-Nezhad, and Rahimi study automorphism groups of comaximal graphs and subgraphs related to \(CG_J(R)\). Accordingly, the automorphism-group structure used in the proof is treated as prior background rather than as the new claim.

Afkhami and coauthors study determining numbers for several graph constructions, including specific blow-ups and zero-divisor graphs. Their accessible results do not give the weighted support-fiber classification, the determining polynomial above, or the Boolean phase transition for reduced comaximal graphs.

Banerjee studies metric dimension for an induced comaximal graph of \(\mathbb Z_n\). Metric dimension and determining number are distinct invariants, and that work does not imply the pointwise-stabilizer classification here.

The accepted contribution is therefore the exact if-and-only-if description of all determining sets for finite products of fields, its factorized enumerator and minimum-set count, and the separate coordinate-separation theorem at the fully Boolean boundary.

## Limitations

The theorem is restricted to finite reduced rings. Nilpotent local factors replace support fibers by finer residue or radical layers and can introduce additional twin structure.

The full text of the later automorphism-group article was not available for inspection. Its abstract confirms automorphism-group coverage but does not mention determining sets or determining polynomials. This leaves a residual literature risk for unadvertised consequences inside that paper; for this reason no novelty is claimed for the automorphism-group description itself.

No formula is claimed here for the number of minimum determining families in the fully Boolean case; only their exact separating-family characterization and minimum cardinality are asserted.

## References

1. S. Moconja and Z. Z. Petrović, “On the Structure of Comaximal Graphs of Commutative Rings with Identity,” *Bulletin of the Australian Mathematical Society* 83 (2011), 11–21. DOI: 10.1017/S0004972710001875. First published online 26 November 2010.
2. K. Khashyarmanesh, E. Mehdi-Nezhad, and A. M. Rahimi, “The Automorphism Group of the Comaximal Graph of a Commutative Ring,” *Journal of Algebra and Its Applications* 24 (2025), article 2550288. DOI: 10.1142/S0219498825502883.
3. M. Afkhami et al., “On the Determining Number of Some Graphs,” *AKCE International Journal of Graphs and Combinatorics* 21 (2024). DOI: 10.1080/09728600.2024.2365338.
4. S. Banerjee, “The Adjacency Spectrum and Metric Dimension of an Induced Subgraph of Comaximal Graph of \(\mathbb Z_n\),” *Journal of Interconnection Networks* (2022). DOI: 10.1142/S1793830922500938.
