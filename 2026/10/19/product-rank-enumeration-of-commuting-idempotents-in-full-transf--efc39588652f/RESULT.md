# Product-rank enumeration of commuting idempotents in full transformation monoids

## Finding
Let \(X\) be a labeled set of size \(n\) and let \(\mathcal T_X\) be its full transformation monoid, with composition \((ef)(x)=e(f(x))\). Let \(c_{n,k}\) count ordered pairs \((e,f)\) satisfying \(e^2=e\), \(f^2=f\), and \(ef=fe\), classified by \(k=|\operatorname{im}(ef)|\). Set \(c_{0,0}=1\) and \(c_{n,0}=0\) for \(n>0\).

**Theorem.** The complete product-rank distribution, for all \(n\), is determined by
\[
\sum_{n\ge0}\sum_{k=0}^{n}c_{n,k}y^k\frac{z^n}{n!}=\exp(yH(z)),\qquad
H(z)=z\sum_{a,b\ge0}\frac{z^{a+b}}{a!b!}\exp\bigl(z(a+1)(b+1)\bigr).
\]
The expressions are identities in the ring of formal power series \(\mathbb Q[y][[z]]\); each coefficient involves finitely many terms. If \(h_m=m![z^m]H(z)\), then
\[
h_m=m\sum_{a+b+c=m-1}\frac{(m-1)!}{a!\,b!\,c!}\bigl((a+1)(b+1)\bigr)^c,\qquad m\ge1,
\]
and the integer recurrence is
\[
k c_{n,k}=\sum_{m=1}^{n}\binom{n}{m}h_m c_{n-m,k-1}\quad(n,k\ge1).
\]
In particular, the number \(C_n=\sum_k c_{n,k}\) of ordered commuting idempotent pairs is determined for every \(n\).

**Graph consequence.** For \(n\ge2\), the center of \(\mathcal T_X\) is the identity alone. The graph induced by noncentral idempotents within its commuting graph has
\[
\frac{C_n-3E_n+2}{2}\quad\text{edges},\qquad
E_n=\sum_{j=1}^{n}\binom{n}{j}j^{n-j}.
\]
This is the induced **idempotent** subgraph, not the full commuting graph on all noncentral transformations.

## Assumptions and scope
The result is combinatorial, valid for every finite labeled set, including the empty-set convention. It does not require a field. Transformation multiplication is ordinary composition. Both elements of each pair are idempotent, so the product is also idempotent precisely because the pair commutes. Image size and rank mean set-theoretic image cardinality. The graph is finite, undirected, simple, and has an edge between distinct commuting noncentral transformations.

## Proof
**1. Canonical product fibers.** If \(e,f\) are commuting idempotents, put \(g=ef=fe\). Then \(g^2=g\), and
\[
\operatorname{im}(g)=\operatorname{im}(e)\cap\operatorname{im}(f).
\]
Indeed, \(g(x)\) lies in both images. Conversely, if \(r\) is fixed by both idempotents, then \(g(r)=r\), hence it lies in the product image. For each \(r\in\operatorname{im}(g)\), the fiber \(F_r=g^{-1}(r)\) is preserved by both maps, since \(ge=eg=g\) and \(gf=fg=g\). Its unique common fixed point of \(e\) and \(f\) is \(r\).

**2. Exact one-fiber classification.** Fix one such fiber \(F=F_r\) of cardinal \(m\). The disjoint subsets
\[
U=\operatorname{im}(e|_F)\setminus\{r\},\quad
V=\operatorname{im}(f|_F)\setminus\{r\},\quad
W=F\setminus(\{r\}\cup U\cup V)
\]
form a partition. They are disjoint because the two restricted images intersect exactly in \(\{r\}\). Writing \(a=|U|\), \(b=|V|\), \(c=|W|\), the maps are forced on \(\{r\}\cup U\cup V\): \(r\) is fixed by both; on \(U\), \(e\) fixes every point and \(f\) sends it to \(r\); on \(V\), \(f\) fixes every point and \(e\) sends it to \(r\). For each \(w\in W\), choose independently
\[
e(w)\in U\cup\{r\},\qquad f(w)\in V\cup\{r\}.
\]
These \((a+1)(b+1)\) choices ensure both idempotence relations and \(e(f(w))=f(e(w))=r\), with product equal to the constant map onto \(r\). Conversely every commuting idempotent pair with constant product arises uniquely this way. Choosing the root, partition, and values gives exactly
\[
h_m=m\sum_{a+b+c=m-1}\frac{(m-1)!}{a!b!c!}[(a+1)(b+1)]^c.
\]
In particular \(h_1=1\), \(h_2=6\), and \(h_3=39\).

**3. Exponential composition.** Because \(g\) is an idempotent map, the fibers \(F_r\), for \(r\in\operatorname{im}(g)\), form an unordered set partition of \(X\). The pair \((e,f)\) is the disjoint union of uniquely defined structures from Step 2 on those fibers; conversely any set partition with one such structure on each block yields a commuting pair, and the number of blocks equals \(|\operatorname{im}(g)|\). The labeled SET construction yields the stated identity \(\exp(yH(z))\), including \(n=0\). Expanding the exponential shows \(c_{n,k}=\frac{n!}{k!}[z^n]H(z)^k\). Differentiating with respect to \(y\), or distinguishing one product fiber, gives the displayed integer recurrence. The alternate formula for \(H(z)\) follows by summing first over \(c\ge0\).

**4. Edges.** An idempotent on \(n\) labeled points with exactly \(j\) image points is obtained by choosing its image and then sending every other point to one of those \(j\) fixed points, giving \(E_n\). For \(n\ge2\), any central transformation commutes with every constant map, forcing every point to be fixed, so the center is precisely \(\operatorname{id}_X\). Remove the \(E_n\) diagonal ordered pairs and \(2(E_n-1)\) identity/nonidentity ordered pairs from \(C_n\), and divide by two to obtain the simple-graph edge count. This argument counts no unordered pair twice.

## Verification
The included `verify.py` computes \(h_m\) and the full distribution by exact integer arithmetic. Independently, it exhausts the idempotent transformations and tests composition and product rank for \(1\le n\le6\). Expected row distributions, ordered by rank, are:

- \(n=1\): \((1)\);
- \(n=2\): \((6,1)\);
- \(n=3\): \((39,18,1)\);
- \(n=4\): \((300,264,36,1)\);
- \(n=5\): \((2785,3840,930,60,1)\);
- \(n=6\): \((30798,58920,21780,2400,90,1)\).

The derived totals for \(n=1,\ldots,8\) are \(1,7,58,601,7616,113989,1963060,38178193\). The graph edge counts for \(n=2,\ldots,6\) are \(0,15,240,3515,55410\). The general identity is proved in the preceding steps; the finite checks are reproducibility tests, not a substitute for the proof. Run `python3 verify.py`.

## Relationship to prior work
Araújo and Konieczny [1] classify maximal commutative sets of idempotent transformations (semilattices) and give a structural commuting-idempotent lemma. Araújo, Bentz and Konieczny [2] extend extremal semilattice results to independence algebras. The distinct subject here is the **complete distribution of all commuting idempotent pairs by product rank**, including all finite sizes and the induced commuting-graph edge count. In [3] Araújo, Kinyon and Konieczny investigate commuting-graph distances, not the pair-rank enumerator. Araújo and Konieczny [4] characterize general transformation centralizers by connected digraph homomorphisms, a potentially more general structural framework; the present closed coefficient formula and rank refinement were not found in its inspected definition, theorem and application sections. The exact basic commuting condition and the formal exponential formula for labeled sets are standard tools; neither is claimed novel independently.

## Limitations
The theorem concerns **ordered pairs of idempotents**, not arbitrary commuting transformations or all higher commuting tuples. The formulas are exact but are not a closed-form asymptotic expansion. Novelty is assessed against accessible primary texts and searches, not exhaustively: Konieczny's 2002 paper on semigroups commuting with idempotents was available only through an abstract and is a material residual risk. Other older work on centralizer cardinalities could contain an equivalent enumerator. No independent mathematical audit has been performed.

## References
[1] J. Araújo and J. Konieczny, *The Largest Subsemilattices of the Semigroup of Transformations on a Finite Set*, arXiv:1007.4845v1 (first submitted 2010-07-27), https://arxiv.org/abs/1007.4845.

[2] J. Araújo, W. Bentz, and J. Konieczny, *The Largest Subsemilattices of the Endomorphism Monoid of an Independence Algebra*, arXiv:1405.7260v1 (2014), https://arxiv.org/abs/1405.7260.

[3] J. Araújo, M. Kinyon, and J. Konieczny, *Minimal Paths in the Commuting Graphs of Semigroups*, European Journal of Combinatorics 32 (2011), 178–197; author-hosted preprint: https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1006.pdf.

[4] J. Araújo and J. Konieczny, *Centralizers in the Full Transformation Semigroup*, author-hosted text, https://repositorioaberto.uab.pt/server/api/core/bitstreams/e1505ef6-df71-4791-a964-cd83058b4fc9/content.

[5] J. Konieczny, *Semigroups of transformations commuting with idempotents*, Algebra Colloquium 9 (2002), 121–134 (abstract verified; full text not obtained).

[6] I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312 (2014), https://arxiv.org/abs/1407.3312.
