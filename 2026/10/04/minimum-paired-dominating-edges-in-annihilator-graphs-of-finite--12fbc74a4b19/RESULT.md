# Minimum paired dominating edges in annihilator graphs of finite reduced rings

## Finding

Let \(R\cong\prod_{i=1}^r\mathbb F_{q_i}\) be a finite reduced commutative ring with identity that is not a field, with \(r\ge2\), and let \(AG(R)\) be Badawi’s annihilator graph. For \(x\in R\), write \(\operatorname{supp}(x)=\{i:x_i\ne0\}\). Then a two-vertex set \(\{x,y\}\) is a minimum total dominating set—and equivalently a minimum paired dominating set—of \(AG(R)\) if and only if \[\operatorname{supp}(y)=[r]\setminus\operatorname{supp}(x).\] Consequently \(\gamma_t(AG(R))=\gamma_{\mathrm{pr}}(AG(R))=2\), and the exact number of minimum total dominating sets, which is also the exact number of minimum paired dominating sets, is \[(2^{r-1}-1)\prod_{i=1}^r(q_i-1).\]

Thus the strengthened domination invariant does more than collapse to the value \(2\): every minimum witness is forced by a bipartition of the field-factor coordinates, and the number of such witnesses has a closed product formula.

## Assumptions and scope

Let
\[
R\cong\prod_{i=1}^r\mathbb F_{q_i},\qquad r\ge2,
\]
so that \(R\) is a finite reduced commutative ring that is not a field. The annihilator graph \(AG(R)\) has vertex set
\[
Z(R)^*=Z(R)\setminus\{0\},
\]
and distinct vertices \(x,y\) are adjacent when
\[
\operatorname{ann}(xy)\ne
\operatorname{ann}(x)\cup\operatorname{ann}(y).
\]

For a vertex \(x=(x_1,\ldots,x_r)\), put
\[
A_x=\operatorname{supp}(x)=\{i:x_i\ne0\}.
\]
Because \(x\) is a nonzero nonunit, \(A_x\) is a nonempty proper subset of \([r]\). For each nonempty proper \(A\subset[r]\), the support class
\[
V_A=\{x\in Z(R)^*:A_x=A\}
\]
has cardinality
\[
|V_A|=\prod_{i\in A}(q_i-1).
\]

## Proof

For \(x\in R\), multiplication is coordinatewise, so
\[
\operatorname{ann}(x)
=
\{z\in R:\operatorname{supp}(z)\subseteq [r]\setminus A_x\}.
\tag{1}
\]
Also
\[
A_{xy}=A_x\cap A_y.
\]
If \(A_x\subseteq A_y\), then \(A_{xy}=A_x\), hence
\[
\operatorname{ann}(xy)=\operatorname{ann}(x)
\supseteq \operatorname{ann}(y),
\]
so \(x\) and \(y\) are not adjacent. The same holds with \(x,y\) reversed.

Conversely, suppose \(A_x\) and \(A_y\) are incomparable. Choose
\[
i\in A_x\setminus A_y,
\qquad
j\in A_y\setminus A_x.
\]
Let \(z\) have nonzero coordinates only at \(i\) and \(j\). Then \(zxy=0\), because neither \(i\) nor \(j\) belongs to \(A_x\cap A_y\). But \(zx\ne0\) through coordinate \(i\), and \(zy\ne0\) through coordinate \(j\). Therefore
\[
z\in\operatorname{ann}(xy)
\setminus
\bigl(\operatorname{ann}(x)\cup\operatorname{ann}(y)\bigr),
\]
so \(x\) and \(y\) are adjacent. Hence
\[
x\sim y
\iff
A_x\text{ and }A_y\text{ are incomparable}.
\tag{2}
\]

Now let \(\{x,y\}\) be a total dominating set. Since each selected vertex must have a selected neighbor, \(x\sim y\); by (2), \(A_x\) and \(A_y\) are incomparable.

If
\[
A_x\cap A_y\ne\varnothing,
\]
then this intersection is a nonempty proper subset of each support. Choose a vertex \(w\) with support
\[
A_w=A_x\cap A_y.
\]
Its support is comparable with both \(A_x\) and \(A_y\), so by (2) it is adjacent to neither, contradicting domination. Thus
\[
A_x\cap A_y=\varnothing.
\tag{3}
\]

If
\[
A_x\cup A_y\ne[r],
\]
then the union is a proper nonempty subset containing both supports. A vertex \(w\) with
\[
A_w=A_x\cup A_y
\]
is again comparable with both supports and adjacent to neither, another contradiction. Therefore
\[
A_x\cup A_y=[r].
\tag{4}
\]
Equations (3) and (4) show that the supports are complementary.

Conversely, suppose
\[
A_y=[r]\setminus A_x.
\]
The two supports are nonempty and incomparable, so \(x\sim y\). Let \(w\) be any other vertex. If \(A_w\) were comparable with both \(A_x\) and \(A_y\), then one of four possibilities would hold. It cannot be contained in both disjoint nonempty supports; it cannot contain both because then it would be all of \([r]\); and either mixed containment would force one of the complementary supports into the other. Hence \(A_w\) is incomparable with at least one of \(A_x,A_y\). By (2), \(w\) is adjacent to \(x\) or \(y\). Thus \(\{x,y\}\) is total dominating.

Because the selected pair itself is an edge, the induced graph on \(\{x,y\}\) is \(K_2\), which has a perfect matching. Hence the pair is also paired dominating. No total dominating set, and no paired dominating set, can have cardinality \(1\), so
\[
\gamma_t(AG(R))=\gamma_{\mathrm{pr}}(AG(R))=2.
\]

It remains to count the minimum sets. Unordered complementary support pairs are exactly the unordered bipartitions of \([r]\) into two nonempty parts, so there are
\[
2^{r-1}-1
\]
of them. For one such pair \(\{A,A^c\}\), the number of vertex pairs with these supports is
\[
|V_A||V_{A^c}|
=
\left(\prod_{i\in A}(q_i-1)\right)
\left(\prod_{i\notin A}(q_i-1)\right)
=
\prod_{i=1}^r(q_i-1).
\]
Multiplying gives
\[
(2^{r-1}-1)\prod_{i=1}^r(q_i-1),
\]
as claimed.

## Verification

The standalone `verify.py` builds Badawi’s annihilator graph directly from the ring operations for nine products of prime fields. For each pair of vertices it computes the three annihilator sets appearing in the graph definition, tests whether the pair is an edge and a dominating set, and checks that the successful pairs are exactly those with complementary supports. It also compares the exact number of successful pairs with the closed formula.

The direct cases range through two- and three-factor products, with largest ring order \(30\). A separate support-level exhaustive check verifies the classification for every pair of nonempty proper supports for \(2\le r\le7\).

Exact output:

```text
VERIFY_OK
direct_ring_profiles=9
largest_direct_ring_order=30
support_levels_r=2..7
complementary_support_classification=passed
minimum_pair_count_formula=passed
```

The finite computations are corroborative only. The theorem for arbitrary finite field orders and arbitrary \(r\) is the support/annihilator argument above.

## Relationship to prior work

Badawi introduced the annihilator graph and proved, among other structural results, that for a reduced ring the annihilator graph agrees with the classical zero-divisor graph exactly when there are two minimal primes. That already shows that products with three or more field factors genuinely leave the classical zero-divisor-graph regime.

Dutta and Lanong later studied finite annihilator graphs. Their abstract states that the ordinary domination number always lies in \(\{1,2\}\), and their finite-ring analysis includes decomposable rings. They do not classify minimum total or paired dominating sets, nor count them in products of fields.

The present result uses the full annihilator-graph adjacency relation for arbitrary numbers of field factors. It identifies every minimum strengthened dominating pair, not merely the minimum cardinality, and the enumeration depends explicitly on all residue-field orders through
\[
\prod_i(q_i-1).
\]

Paired domination was introduced by Haynes and Slater as domination together with a perfect matching in the selected subgraph. The complementary-support characterization here supplies that matching automatically and determines all minimum paired witnesses in this algebraic graph family.

## Limitations

The exact support classification uses that every local factor is a field. It therefore applies to finite reduced commutative rings and is not asserted for rings with nilpotents.

The formula counts only minimum total and minimum paired dominating sets. It does not give the complete total-domination or paired-domination polynomial in higher cardinalities.

An ordinary domination number of \(1\) or \(2\) does not by itself imply the theorem: total domination requires adjacency inside the selected set, while the classification and count require the support-incomparability structure.

## References

1. A. Badawi, “On the Annihilator Graph of a Commutative Ring,” *Communications in Algebra* 42 (2014), 108–121. Published online 18 October 2013. DOI: 10.1080/00927872.2012.707262.
2. S. Dutta and C. Lanong, “On annihilator graph of a finite commutative ring,” *Transactions on Combinatorics* 6(1) (2017), 1–11. DOI: 10.22108/toc.2017.20360.
3. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
