# Independence polynomial and all maximal independent sets of semiprime-power annihilating-ideal graphs

## Finding

Let \(p\ne q\) be primes, \(a\ge1\), and \(G=\operatorname{AG}(\mathbb Z/(p^a q)\mathbb Z)\). With \(I(G;x)=\sum_{k\ge0}s_kx^k\) the independence polynomial, one has \[I(G;x)=(1+x)^a+(\lfloor a/2\rfloor+1)x(1+x)^{a-1}+x\sum_{t=1}^{\lceil a/2\rceil-1}(1+x)^{2t-1}.\] Moreover \(\alpha(G)=a\), there are exactly \(a+1\) maximal independent sets and exactly \(\lfloor a/2\rfloor+2\) maximum independent sets. The graph is well-covered if and only if \(a\le2\), and its independent domination number is \(1\) for \(a=1\) and \(2\) for \(a\ge2\).

The complete facet structure of the independence complex is explicit. Put
\[
A_i=(p^i)\quad(1\le i\le a),
\qquad
B_j=(p^j q)\quad(0\le j\le a-1).
\]
Besides the facet
\[
\mathcal A=\{A_1,\ldots,A_a\},
\]
there is one facet for each \(0\le m\le a-1\):
\[
\mathcal F_m
=
\{B_m\}
\cup
\{B_j:0\le j<\min(m,a-m)\}
\cup
\{A_i:1\le i\le a-m-1\}.
\]
Its size is
\[
|\mathcal F_m|
=
a-m+\min(m,a-m)
=
\begin{cases}
a,&m\le a/2,\\
2(a-m),&m>a/2.
\end{cases}
\]

## Assumptions and scope

Let
\[
R=\mathbb Z/(p^a q)\mathbb Z,
\]
where \(p\ne q\) are primes and \(a\ge1\). The annihilating-ideal graph \(\operatorname{AG}(R)\) has as vertices the nonzero annihilating ideals, with distinct ideals adjacent exactly when their product is zero.

Since \(R\) is Artinian, every nonzero proper ideal is a vertex. The nonzero proper ideals are precisely
\[
A_i=(p^i),\quad 1\le i\le a,
\qquad
B_j=(p^j q),\quad 0\le j\le a-1.
\]

## Proof

For divisor ideals in \(\mathbb Z/(p^a q)\mathbb Z\), the product is zero exactly when \(p^a q\) divides the product of the representing divisors. Hence
\[
A_iA_k\ne0,
\]
\[
A_iB_j=0
\quad\Longleftrightarrow\quad
i+j\ge a,
\]
and
\[
B_jB_k=0
\quad\Longleftrightarrow\quad
j+k\ge a.
\tag{1}
\]

Let \(X\) be an independent set. If \(X\) contains no \(B\)-vertex, then \(X\subseteq\{A_1,\ldots,A_a\}\), contributing
\[
(1+x)^a
\]
to the independence polynomial.

Now suppose \(X\) contains a \(B\)-vertex, and let \(m\) be the largest index such that \(B_m\in X\). By (1), every \(A_i\in X\) must satisfy
\[
i+m<a,
\]
so the available \(A\)-vertices are exactly
\[
A_1,\ldots,A_{a-m-1}.
\]
Likewise, an additional \(B_j\) with \(j<m\) can occur exactly when
\[
j+m<a,
\]
so the available lower-index \(B\)-vertices are exactly
\[
B_0,\ldots,B_{r-1},
\qquad
r=\min(m,a-m).
\]

These available vertices are mutually compatible. Indeed, when \(m\le a/2\), two such lower \(B\)-indices sum to at most \(2m-2<a\), and an available \(A\)-index plus a lower \(B\)-index is at most \(a-2\). When \(m>a/2\), the lower \(B\)-indices are all less than \(a-m\), so any two sum to less than \(a\), and the same bound holds for their sums with available \(A\)-indices.

Thus the independent sets whose largest \(B\)-index is \(m\) contribute
\[
x(1+x)^{a-m-1+\min(m,a-m)}.
\]
Summing over \(m\) gives
\[
I(G;x)
=
(1+x)^a
+
\sum_{m=0}^{a-1}
 x(1+x)^{a-m-1+\min(m,a-m)}.
\tag{2}
\]
For \(m\le\lfloor a/2\rfloor\), the exponent in (2) is \(a-1\). For the remaining indices, set \(t=a-m\). This yields
\[
I(G;x)
=
(1+x)^a
+
(\lfloor a/2\rfloor+1)x(1+x)^{a-1}
+
x\sum_{t=1}^{\lceil a/2\rceil-1}(1+x)^{2t-1}.
\]

For maximal independent sets, if no \(B\)-vertex occurs, maximality forces all \(A_i\), giving \(\mathcal A\). If the largest \(B\)-index is \(m\), maximality forces every compatible vertex identified above, giving exactly \(\mathcal F_m\). Hence there are exactly \(a+1\) maximal independent sets.

The facet sizes are
\[
|\mathcal A|=a,
\qquad
|\mathcal F_m|=a-m+\min(m,a-m).
\]
Therefore \(\alpha(G)=a\). Maximum size occurs for \(\mathcal A\) and for precisely the indices
\[
0\le m\le\lfloor a/2\rfloor,
\]
so the number of maximum independent sets is
\[
\lfloor a/2\rfloor+2.
\]

All facets have the same size exactly for \(a\le2\), proving the well-covered classification. Finally the smallest facet has size \(1\) when \(a=1\), while for \(a\ge2\) the facet \(\mathcal F_{a-1}=\{B_{a-1},B_0\}\) has size \(2\), and no maximal independent set has size \(1\). Thus the independent domination number is \(1\) for \(a=1\) and \(2\) thereafter.

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

For every \(1\le a\le8\), it exhaustively enumerates all \(2^{2a}\) vertex subsets, checks independence directly from the ideal-product adjacency rules, reproduces every coefficient of the claimed independence polynomial, and verifies that the complete list of maximal independent sets is exactly \(\mathcal A,\mathcal F_0,\ldots,\mathcal F_{a-1}\).

It separately confirms \(\alpha(G)=a\), the count \(\lfloor a/2\rfloor+2\) of maximum independent sets, the well-covered threshold, and the independent domination number.

As an algebra-to-graph check, it constructs the nonzero proper ideals directly from divisors and tests ideal products by divisibility for several rings, including \(\mathbb Z/12\mathbb Z\), \(\mathbb Z/80\mathbb Z\), \(\mathbb Z/1215\mathbb Z\), and \(\mathbb Z/875\mathbb Z\).

Exact replay output:

```text
a=1: polynomial=[1, 2, 0], facets=2, max_sets=2, well_covered=True, i=1
a=2: polynomial=[1, 4, 3, 0, 0], facets=3, max_sets=3, well_covered=True, i=2
a=3: polynomial=[1, 6, 8, 3, 0, 0, 0], facets=4, max_sets=3, well_covered=False, i=2
a=4: polynomial=[1, 8, 16, 13, 4, 0, 0, 0, 0], facets=5, max_sets=4, well_covered=False, i=2
a=5: polynomial=[1, 10, 26, 31, 18, 4, 0, 0, 0, 0, 0], facets=6, max_sets=4, well_covered=False, i=2
a=6: polynomial=[1, 12, 39, 63, 56, 26, 5, 0, 0, 0, 0, 0, 0], facets=7, max_sets=5, well_covered=False, i=2
a=7: polynomial=[1, 14, 54, 108, 126, 86, 32, 5, 0, 0, 0, 0, 0, 0, 0], facets=8, max_sets=5, well_covered=False, i=2
a=8: polynomial=[1, 16, 72, 174, 256, 236, 134, 43, 6, 0, 0, 0, 0, 0, 0, 0, 0], facets=9, max_sets=6, well_covered=False, i=2
Z/6Z direct ideal-product graph OK: vertices=2
Z/12Z direct ideal-product graph OK: vertices=4
Z/80Z direct ideal-product graph OK: vertices=8
Z/1215Z direct ideal-product graph OK: vertices=10
Z/875Z direct ideal-product graph OK: vertices=6
VERIFY_OK
```

The finite enumeration corroborates the symbolic classification; the arbitrary-exponent theorem is proved by the largest-\(B\)-index argument.

## Relationship to prior work

Behboodi and Rakeei introduced annihilating-ideal graphs and proved that every nonzero proper ideal of an Artinian ring is a vertex. Their original preprint lists Mathematics Subject Classification \(13A15\) first.

Nikandish, Maimani, and Izanloo study \(\operatorname{AG}(\mathbb Z_n)\) directly. Their full paper proves weak perfectness, gives exact clique numbers, and proves the graphs are class 1. The inspected full text contains no occurrence of “independence,” “well-covered,” or “polynomial.”

Visweswaran and Parejiya classify rings whose annihilating-ideal graphs have independence number at most four. That work concerns bounded independence number at the ring-classification level; it does not give the complete independence polynomial or the maximal-independent-set facets of this semiprime-power family.

The present result therefore treats the full independent-set enumerator and every maximal independent set, rather than only the extremal independence number.

## Limitations

The modulus has exactly two distinct prime divisors and one of them occurs to exponent one.

The formula depends only on the exponent \(a\); it does not recover the numerical values of \(p\) and \(q\).

The result concerns the standard annihilating-ideal graph, not element zero-divisor graphs or cozero-divisor graphs.

No claim is made here about arbitrary \(\mathbb Z_n\) with two exponents both greater than one.

## References

1. M. Behboodi and Z. Rakeei, “The Annihilating-Ideal Graph of Commutative Rings I,” arXiv:0808.3187, first submitted 23 August 2008; later *Journal of Algebra and Its Applications* 10 (2011). DOI: 10.1142/S0219498811004896.
2. R. Nikandish, H. R. Maimani, and H. Izanloo, “The annihilating-ideal graph of \(\mathbb Z_n\) is weakly perfect,” *Contributions to Discrete Mathematics* 11 (2016), 16–21. DOI: 10.55016/ojs/cdm.v11i1.62406.
3. S. Visweswaran and J. Parejiya, “Annihilating-ideal graphs with independence number at most four,” *Cogent Mathematics* 3 (2016), Article 1155858. DOI: 10.1080/23311835.2016.1155858.
