# Total-domination polynomial and paired minima for ideal-based graphs over chain quotients

## Finding

Let \(R\) be a finite commutative ring with identity and \(I\subsetneq R\) an ideal such that \(S=R/I\) is a finite chain ring with residue field of order \(q\) and maximal-ideal nilpotency length \(k\ge2\). Put \(s=|I|\), \(N=s(q^{k-1}-1)\), and \(m=s(q-1)\). For the simple ideal-based zero-divisor graph \(\Gamma_I(R)\), the total-domination polynomial is \[D_t(\Gamma_I(R),x)=(1+x)^N-(1+x)^{N-m}-mx.\] Equivalently, a vertex subset is total dominating exactly when it has at least two vertices and meets the \(m\)-vertex set lying above the socle layer \(\mathfrak m_S^{k-1}\setminus\{0\}\). If \(N\ge2\), then \(\gamma_t(\Gamma_I(R))=\gamma_{\mathrm{pr}(\Gamma_I(R))=2\), and the minimum total dominating sets and minimum paired dominating sets coincide: they are exactly the two-vertex subsets meeting that socle-lift set, hence their number is \[m(N-m)+\binom{m}{2}.\] If \(N=1\), the graph is one isolated vertex and neither parameter exists.

The statement classifies every total dominating set, not only the minimum size. It also identifies the algebraic locus that every total dominating set must meet and shows that the minimum paired sets are exactly the degree-two part of the same family.

## Assumptions and scope

Let \(R\) be a finite commutative ring with identity and let \(I\subsetneq R\). The ideal-based zero-divisor graph \(\Gamma_I(R)\) has as vertices the elements \(x\in R\setminus I\) for which there is \(y\in R\setminus I\) with \(xy\in I\); distinct vertices are adjacent exactly when their product lies in \(I\).

Assume that \(S=R/I\) is a finite chain ring. Write its maximal ideal as \(\mathfrak m=(\pi)\), let \(k\ge2\) be the least integer with \(\mathfrak m^k=0\), and let the residue field \(S/\mathfrak m\) have order \(q\). Put \(s=|I|\).

For a graph \(G\), write
\[
D_t(G,x)=\sum_{j\ge0} d_t(G,j)x^j,
\]
where \(d_t(G,j)\) is the number of total dominating sets of cardinality \(j\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

Every nonzero zero-divisor of \(S\) has a unique valuation \(a\in\{1,\ldots,k-1\}\), meaning that it lies in \(\mathfrak m^a\setminus\mathfrak m^{a+1}\). Multiplication by \(\pi^a\) identifies each quotient \(\mathfrak m^a/\mathfrak m^{a+1}\) with the one-dimensional residue-field layer, so
\[
|\mathfrak m^a|=q^{k-a}.
\]
In particular, the nonzero zero-divisors of \(S\) number
\[
q^{k-1}-1,
\]
and the nonzero socle layer \(\mathfrak m^{k-1}\setminus\{0\}\) has \(q-1\) elements.

Each coset of \(I\) has exactly \(s\) representatives. A vertex of \(\Gamma_I(R)\) is exactly a representative of a nonzero zero-divisor coset of \(S\). Therefore
\[
|V(\Gamma_I(R))|=N=s(q^{k-1}-1).
\tag{1}
\]
Moreover, for representatives \(x,y\in R\setminus I\),
\[
xy\in I
\iff
(x+I)(y+I)=0\text{ in }S.
\tag{2}
\]
Thus adjacency depends only on quotient valuations.

Let \(U\) be the set of all vertices whose quotient coset lies in the nonzero socle layer. By the count above,
\[
|U|=m=s(q-1).
\tag{3}
\]
Every \(u\in U\) is universal: if \(v\) is any graph vertex, its quotient valuation is at least one, so the product of its coset with the valuation-\(k-1\) coset of \(u\) is zero.

When \(k\ge3\), choose a vertex \(w\) whose quotient valuation is one. By (2), a graph vertex is adjacent to \(w\) exactly when its quotient valuation is at least \(k-1\). Hence
\[
N(w)=U.
\tag{4}
\]
For \(k=2\), every nonzero zero-divisor coset already lies in the socle layer, so \(U=V(\Gamma_I(R))\).

We now characterize total domination. If \(k\ge3\), (4) forces every total dominating set to meet \(U\). The same conclusion is automatic for \(k=2\). A total dominating set must also have at least two vertices, because a simple graph has no loops. Conversely, if \(D\subseteq V\) has \(|D|\ge2\) and contains some \(u\in U\), then \(u\) is adjacent to every other vertex, and the second selected vertex dominates \(u\). Thus \(D\) is total dominating. We have proved
\[
D\text{ is total dominating}
\iff
|D|\ge2\text{ and }D\cap U\ne\varnothing.
\tag{5}
\]

All subsets meeting \(U\) contribute
\[
(1+x)^N-(1+x)^{N-m}.
\]
The only such subsets excluded by (5) are the \(m\) singletons in \(U\). Therefore
\[
D_t(\Gamma_I(R),x)
=
(1+x)^N-(1+x)^{N-m}-mx.
\tag{6}
\]

If \(N\ge2\), the coefficient of \(x^2\) in (6) is positive, so \(\gamma_t=2\). Every two-vertex set meeting \(U\) is an edge, hence induces a perfect matching and dominates the graph. Thus it is also paired dominating. Conversely, every paired dominating set is total dominating, so no smaller paired set exists and every minimum paired set must be one of these pairs. Their number is
\[
\binom{N}{2}-\binom{N-m}{2}
=
m(N-m)+\binom{m}{2}.
\tag{7}
\]
If \(N=1\), the graph is a single isolated vertex and has neither a total nor a paired dominating set.

## Verification

The standalone `verify.py` artifact constructs actual ideal-based graphs for rings
\[
R=\mathbb Z/(p^n),
\qquad
I=(p^k),
\]
so that \(R/I\cong\mathbb Z/(p^k)\) and \(|I|=p^{n-k}\). It builds adjacency directly from the multiplication condition \(xy\in I\), identifies the universal socle lifts, exhaustively enumerates all total dominating sets, and checks every minimum paired dominating pair.

Exact replay output:

```text
p=2 n=2 k=2 vertices=1 universal=1 total_coeffs=[0, 0] paired_min_pairs=0
p=2 n=3 k=2 vertices=2 universal=2 total_coeffs=[0, 0, 1] paired_min_pairs=1
p=3 n=2 k=2 vertices=2 universal=2 total_coeffs=[0, 0, 1] paired_min_pairs=1
p=2 n=3 k=3 vertices=3 universal=1 total_coeffs=[0, 0, 2, 1] paired_min_pairs=2
p=3 n=3 k=3 vertices=8 universal=2 total_coeffs=[0, 0, 13, 36, 55, 50, 27, 8, 1] paired_min_pairs=13
p=2 n=4 k=3 vertices=6 universal=2 total_coeffs=[0, 0, 9, 16, 14, 6, 1] paired_min_pairs=9
p=2 n=5 k=4 vertices=14 universal=2 total_coeffs=[0, 0, 25, 144, 506, 1210, 2079, 2640, 2508, 1782, 935, 352, 90, 14, 1] paired_min_pairs=25
VERIFY_OK
```

The computation covers the isolated boundary, complete-graph quotients of length two, and noncomplete quotients of lengths three and four. It is corroborative only; equations (1)–(7) give the general proof.

## Relationship to prior work

Anderson and Shirinkam study the exact ideal-based graph \(\Gamma_I(R)\), including its relation to ordinary zero-divisor graphs; their article is also the archive-era algebra-primary ownership source used here.

Anderson, Ebrahimi Atani, Shajari Kohan, and Ebrahimi Sarvandi analyze \(\Gamma_I(R)\) when \(R/I\) is chained. Their full text gives the clique/independent-layer structure, diameter, and girth, but not total-domination polynomials or paired domination.

Mehdi-Nezhad and Rahimi study ordinary domination of ideal-based zero-divisor graphs. A later coupon-coloring paper proves the already-known numerical equality
\[
\gamma_t(\Gamma_I(R))=\gamma_t(\Gamma(R/I))
\]
when there are no isolated vertices. Accordingly, the numerical value \(\gamma_t=2\) in the present chain-ring setting is not treated as the novelty by itself. The contribution here is the classification of every total dominating set, the closed total-domination polynomial, and the minimum paired-set classification and count.

Alikhani and Aghaei compute total-domination polynomials for several ordinary zero-divisor graphs, including \(\Gamma(\mathbb Z/(p^\alpha))\). That gives a special ordinary-graph case when \(I=0\) and the chain ring is a prime-power residue ring. Formula (6) covers arbitrary finite chain-ring quotients and nontrivial ideal fibres; its proof also identifies exactly how the fibre size \(s\) changes the polynomial.

## Limitations

The quotient \(R/I\) must be a finite chain ring. For a general local ring, the socle can have higher residue-field dimension and valuation-one vertices need not have exactly the socle lifts as their neighborhood, so (5) can fail.

The result concerns the simple ideal-based graph on ring elements, not the annihilator-compressed graph or an ideal graph.

The numerical equality \(\gamma_t=2\) is consistent with and, in the nonisolated case, covered at the parameter level by prior total-domination work; novelty is claimed only for the full set classification, polynomial, and paired-minimum classification/count after the literature comparisons described above.

## References

1. D. F. Anderson and S. Shirinkam, “Some Remarks on the Graph \(\Gamma_I(R)\),” *Communications in Algebra* 42 (2014), 545–562. DOI: 10.1080/00927872.2012.718021.
2. D. F. Anderson, S. Ebrahimi Atani, M. Shajari Kohan, and Z. Ebrahimi Sarvandi, “The ideal-based zero-divisor graph of commutative chained rings,” *Sarajevo Journal of Mathematics* 10 (2014), 3–12. DOI: 10.5644/SJM.10.1.01.
3. E. Mehdi-Nezhad and A. M. Rahimi, “Dominating sets of the comaximal and ideal-based zero-divisor graphs of commutative rings,” *Quaestiones Mathematicae* 38 (2015), 613–629. DOI: 10.2989/16073606.2014.981713.
4. R. T. and R. Pavithra, “Coupon Coloring of Ideal-Based Zero-Divisor Graphs,” *South East Asian Journal of Mathematics and Mathematical Sciences* 21, Proceedings (2022), 183–190.
5. S. Alikhani and F. Aghaei, “Domination polynomial and total domination polynomial of zero-divisor graphs of commutative rings,” arXiv:2404.13539.
