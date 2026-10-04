# Forced total-domination cores in compressed zero-divisor graphs of finite principal ideal rings

## Finding

Let \(R\cong\prod_{i=1}^{r}R_i\) be a finite commutative principal ideal ring with identity, where each \(R_i\) is a finite chain ring whose maximal ideal has nilpotency length \(\ell_i\ge1\), with a field factor counted as \(\ell_i=1\). Assume that the simple annihilator-compressed zero-divisor graph \(\Gamma_E(R)\) is nonempty. If \(r\ge2\), then \(\gamma_t(\Gamma_E(R))=r\), and the unique minimum total dominating set is the set of the \(r\) valuation classes \(d_i=(\ell_1,\ldots,\ell_{i-1},\ell_i-1,\ell_{i+1},\ldots,\ell_r)\). Moreover, \(\gamma_{\mathrm{pr}}(\Gamma_E(R))=r\) for even \(r\) and \(\gamma_{\mathrm{pr}}(\Gamma_E(R))=r+1\) for odd \(r\). For even \(r\) the same core is the unique minimum paired dominating set; for odd \(r\), every minimum paired dominating set is the core plus exactly one other vertex, so their number is \(\prod_{i=1}^{r}(\ell_i+1)-2-r\). If \(r=1\), then length \(\ell_1=2\) gives one isolated compressed vertex and no total or paired dominating set, while for \(\ell_1\ge3\) both parameters equal \(2\), and the minimum sets are exactly \(\{\ell_1-1,k\}\) with \(1\le k\le\ell_1-2\).

For a nonlocal finite principal ideal ring, the strengthened domination problem therefore has a rigid algebraic core: the core consists of one class associated with each local factor. Paired domination detects only the parity of the number of factors beyond this forced core, while the number of odd-rank minimum paired sets records the total number of nontrivial valuation classes.

## Assumptions and scope

Write
\[
R\cong R_1\times\cdots\times R_r,
\]
where each \(R_i\) is a finite chain ring with maximal ideal \(\mathfrak m_i=(\pi_i)\) and
\[
\mathfrak m_i^{\ell_i}=0,
\qquad
\mathfrak m_i^{\ell_i-1}\ne0.
\]
A field factor is assigned \(\ell_i=1\). For \(x_i\in R_i\), define its valuation \(v_i(x_i)\) by
\[
v_i(x_i)=
\begin{cases}
0,&x_i\text{ is a unit},\\
a,&x_i\in\mathfrak m_i^a\setminus\mathfrak m_i^{a+1},\\
\ell_i,&x_i=0.
\end{cases}
\]
Thus a valuation vector lies in
\[
\prod_{i=1}^r\{0,1,\ldots,\ell_i\}.
\]

The graph \(\Gamma_E(R)\) is the simple graph whose vertices are annihilator-equivalence classes of nonzero zero-divisors, with distinct classes adjacent when their product is zero. We assume it is nonempty, thereby avoiding the convention-dependent empty graph attached to a field.

A total dominating set requires every vertex, including selected vertices, to have a selected neighbor. A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

In a finite chain ring,
\[
\operatorname{ann}(\pi_i^a)=\mathfrak m_i^{\ell_i-a}
\qquad
(0\le a\le\ell_i),
\]
with the endpoints interpreted as the annihilators of a unit and of zero. Distinct values of \(a\) therefore give distinct annihilators. Since annihilators in a direct product are taken coordinatewise, the annihilator class of an element of \(R\) is determined exactly by its valuation vector.

The unit class is the zero valuation vector and the zero class is \((\ell_1,\ldots,\ell_r)\). Hence the vertices of \(\Gamma_E(R)\) are precisely the remaining valuation vectors, and distinct vertices \(a=(a_i)\) and \(b=(b_i)\) are adjacent exactly when
\[
a_i+b_i\ge\ell_i
\qquad
\text{for every }i.
\tag{1}
\]

Assume first that \(r\ge2\). For each \(i\), define
\[
w_i=(0,\ldots,0,1,0,\ldots,0)
\]
and
\[
d_i=(\ell_1,\ldots,\ell_{i-1},\ell_i-1,\ell_{i+1},\ldots,\ell_r).
\]
Both are vertices. By (1), any neighbor \(b\) of \(w_i\) must satisfy
\[
b_j=\ell_j\quad(j\ne i),
\qquad
b_i\ge\ell_i-1.
\]
There are only two coordinate possibilities for \(b_i\). The choice \(b_i=\ell_i\) is the excluded zero class, so
\[
N(w_i)=\{d_i\}.
\tag{2}
\]
Thus every total dominating set must contain all of
\[
D=\{d_1,\ldots,d_r\}.
\tag{3}
\]

The vertices in \(D\) form a clique: if \(i\ne j\), then the coordinate sums of \(d_i\) and \(d_j\) meet every threshold in (1). Also, every graph vertex \(a\) has some positive coordinate \(a_i\ge1\), because the unit class was deleted. Such a vertex is adjacent to \(d_i\). Since \(r\ge2\), the clique \(D\) also internally dominates itself. Hence \(D\) is total dominating. Together with (2), this proves
\[
\gamma_t(\Gamma_E(R))=r
\]
and proves uniqueness of the minimum total dominating set.

Every paired dominating set is total dominating, because its perfect matching gives each selected vertex a selected neighbor. Consequently every paired dominating set contains \(D\). If \(r\) is even, the clique \(D\) has a perfect matching, proving
\[
\gamma_{\mathrm{pr}}(\Gamma_E(R))=r,
\]
with uniqueness.

If \(r\) is odd, a paired dominating set has even cardinality and so has size at least \(r+1\). Let \(x\notin D\) be any vertex. Choose a positive coordinate \(i\) of \(x\). Then \(x\) is adjacent to \(d_i\). Match \(x\) to \(d_i\), and pair the remaining \(r-1\) vertices of the clique \(D\) arbitrarily. Therefore every set
\[
D\cup\{x\},
\qquad
x\in V(\Gamma_E(R))\setminus D,
\]
is paired dominating, and these are all minimum paired dominating sets. Since
\[
|V(\Gamma_E(R))|
=
\prod_{i=1}^r(\ell_i+1)-2,
\]
their number is
\[
\prod_{i=1}^r(\ell_i+1)-2-r.
\]

Finally suppose \(r=1\). If \(\ell_1=2\), the only vertex has valuation \(1\), so it is isolated. If \(\ell_1\ge3\), the vertex of valuation \(1\) has the unique neighbor \(\ell_1-1\), forcing \(\ell_1-1\) into every total dominating set. Every valuation \(k\) with
\[
1\le k\le\ell_1-2
\]
is adjacent to \(\ell_1-1\), so the sets
\[
\{\ell_1-1,k\}
\]
are exactly the minimum total dominating sets. Each is an edge and therefore is also paired dominating. This gives both parameters equal to \(2\) and exactly \(\ell_1-2\) minimum sets.

## Verification

The accompanying `verify.py` constructs the valuation-vector graph directly from (1), checks the unique-neighbor witnesses in (2), and exhaustively enumerates minimum total and paired dominating sets for local lengths through \(6\), all two-factor length tuples with coordinates through \(3\), all three-factor tuples with coordinates through \(2\), and three representative four-factor tuples.

It also independently constructs several actual product rings of the form
\[
\prod_i \mathbb Z/(2^{\ell_i}),
\]
computes annihilator equivalence classes from the multiplication table, and verifies that the resulting compressed graph is exactly the valuation graph.

Exact replay output:

```text
(1,): empty graph
(2,): one isolated vertex; no total/paired domination
(3,): |V|=2 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(4,): |V|=3 gamma_t=2 min_total=2 gamma_pr=2 min_paired=2
(5,): |V|=4 gamma_t=2 min_total=3 gamma_pr=2 min_paired=3
(6,): |V|=5 gamma_t=2 min_total=4 gamma_pr=2 min_paired=4
(1, 1): |V|=2 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(1, 2): |V|=4 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(1, 3): |V|=6 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(2, 1): |V|=4 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(2, 2): |V|=7 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(2, 3): |V|=10 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(3, 1): |V|=6 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(3, 2): |V|=10 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(3, 3): |V|=14 gamma_t=2 min_total=1 gamma_pr=2 min_paired=1
(1, 1, 1): |V|=6 gamma_t=3 min_total=1 gamma_pr=4 min_paired=3
(1, 1, 2): |V|=10 gamma_t=3 min_total=1 gamma_pr=4 min_paired=7
(1, 2, 1): |V|=10 gamma_t=3 min_total=1 gamma_pr=4 min_paired=7
(1, 2, 2): |V|=16 gamma_t=3 min_total=1 gamma_pr=4 min_paired=13
(2, 1, 1): |V|=10 gamma_t=3 min_total=1 gamma_pr=4 min_paired=7
(2, 1, 2): |V|=16 gamma_t=3 min_total=1 gamma_pr=4 min_paired=13
(2, 2, 1): |V|=16 gamma_t=3 min_total=1 gamma_pr=4 min_paired=13
(2, 2, 2): |V|=25 gamma_t=3 min_total=1 gamma_pr=4 min_paired=22
(1, 1, 1, 1): |V|=14 gamma_t=4 min_total=1 gamma_pr=4 min_paired=1
(1, 1, 1, 2): |V|=22 gamma_t=4 min_total=1 gamma_pr=4 min_paired=1
(1, 1, 2, 2): |V|=34 gamma_t=4 min_total=1 gamma_pr=4 min_paired=1
direct R=product Z/(2^L), L=(3,): 2 compressed vertices OK
direct R=product Z/(2^L), L=(2, 1): 4 compressed vertices OK
direct R=product Z/(2^L), L=(2, 2): 7 compressed vertices OK
direct R=product Z/(2^L), L=(3, 1): 6 compressed vertices OK
direct R=product Z/(2^L), L=(3, 2): 10 compressed vertices OK
direct R=product Z/(2^L), L=(2, 2, 1): 16 compressed vertices OK
VERIFY_OK
```

The finite computations are corroborative only. The arbitrary-ring theorem follows from the chain-ring annihilator calculation, the unique-neighbor forcing in (2), and the explicit matching construction.

## Relationship to prior work

Spiroff and Wickham introduced the annihilator-equivalence graph \(\Gamma_E(R)\), proved basic structural facts, and related its vertices to associated primes. Their full text contains no occurrence of “domination” and does not address total or paired domination.

Kiani, Maimani, and Nikandish determine total domination for the ordinary zero-divisor graph \(\Gamma(R)\) of a Noetherian ring. Their vertex set consists of individual nonzero zero-divisors, not annihilator classes, so their associated-prime formula does not give the minimum-set rigidity or paired-domination classification above.

Hashemi, Abdi, Alhevaz, and Su study ordinary domination of \(\Gamma_E(R)\). The accessible abstract says that they obtain relations between ordinary domination of the ordinary and compressed zero-divisor graphs; it does not state a total- or paired-domination result. A later conference abstract on finite commutative rings with principal local maximal ideals states the ordinary formula that the domination number equals the number of local factors. Accordingly, ordinary domination number \(r\) is prior coverage and is not claimed here as new.

Đurić, Jevđenić, and Stopar characterize finite commutative principal ideal rings via tensor products of staircase graphs and identify the local staircase length with the maximal-ideal nilpotency index. Their full text contains no occurrence of “domination” or “paired.” The present argument uses the equivalent valuation description but adds the forced total-domination core, paired parity correction, complete minimum-set classification, and exact odd-rank count.

## Limitations

The theorem is for finite commutative principal ideal rings. For a general finite commutative ring, annihilator classes need not be indexed by one valuation coordinate per local factor, and the unique-neighbor witnesses may fail.

Ordinary domination of the same compressed graphs has prior literature and is not part of the novelty claim.

The full text of the 2020 paper on ordinary domination of compressed zero-divisor graphs was not available through the inspected lawful open routes. Its accessible abstract was checked, and the access limitation remains a residual comparison risk; it does not justify any negative claim about material beyond that abstract.

The computational replay covers finite test families only and is not an infinite proof.

## References

1. S. Spiroff and C. Wickham, “A zero divisor graph determined by equivalence classes of zero divisors,” arXiv:0801.0086; *Communications in Algebra* 39 (2011). DOI: 10.1080/00927872.2010.488675.
2. S. Kiani, H. R. Maimani, and R. Nikandish, “Some Results on the Domination Number of a Zero-divisor Graph,” *Canadian Mathematical Bulletin* 57 (2014), 573–578. DOI: 10.4153/CMB-2014-027-8.
3. E. Hashemi, M. Abdi, A. Alhevaz, and H. Su, “Domination number of graphs associated with rings,” *Journal of Algebra and Its Applications* 19 (2020), 2050009. DOI: 10.1142/S0219498820500097.
4. A. Đurić, S. Jevđenić, and N. Stopar, “Categorial properties of compressed zero-divisor graphs of finite commutative rings,” arXiv:1807.11283; *Journal of Algebra and Its Applications* 20 (2021), 2150069. DOI: 10.1142/S0219498821500699.
5. Reji T and Pavithra R, “On Compressed Zero-divisor Graphs of Finite Commutative Rings,” CALDAM 2023 Young Researchers Forum, book of abstracts.
