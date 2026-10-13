# Joint modal-saturation rank census for commuting finite equivalence relations

## Finding

For every integer \(n\geq 0\), let \(\mathcal E_n\) denote the equivalence relations on a labelled \(n\)-point set. For \(R,S\in\mathcal E_n\), let \(a\), \(b\), and \(c\) respectively be the numbers of classes of \(R\), \(S\), and their join \(R\vee S\). Write \(N_n(a,b,c)\) for the number of **ordered** pairs \((R,S)\) satisfying \(R\circ S=S\circ R\) and these three class-count conditions. In the empty case, set \(N_0(0,0,0)=1\).

The complete joint exponential generating function is

\[
\boxed{\displaystyle
\sum_{n\geq0}\frac{z^n}{n!}\sum_{a,b,c\geq0}N_n(a,b,c)u^a v^b t^c
=\exp\!\left(t\sum_{r,s\geq1}\frac{u^rv^s}{r!s!}(e^z-1)^{rs}\right).}
\]

Thus, for every \(n\geq1\), the coefficient of \(u^av^bt^c z^n/n!\) gives the exact multiplicity of two commuting finite \(\mathrm{S5}\) modalities with respectively \(a\) and \(b\) individual equivalence classes and a composite modal operator having exactly \(2^c\) distinct possible output sets.

The joint support is sharp: for positive \(a,b,c\), \(N_n(a,b,c)>0\) precisely when \(1\leq c\leq\min(a,b)\) and

\[
\boxed{\quad n\geq\begin{cases}ab,&c=1,\\a+b-c,&c\geq2.\end{cases}\quad}
\]

Consequently a single composite class imposes the product-size threshold \(ab\), whereas two or more composite classes require only the additive threshold \(a+b-c\). This difference is invisible in the known unrefined total-count sequence.

## Assumptions and scope

All underlying sets are finite and labelled, with \(n\geq0\). Relations \(R,S\) are arbitrary equivalence relations, and compositions are relational compositions. Write
\(\Diamond_R(X)=\{w:\exists x\in X,\;wRx\}\) for \(X\subseteq[n]\), and analogously for \(S\). Cardinality of the image of \(\Diamond_R\Diamond_S\) means the number of **distinct subsets** obtained as the input subset varies; it is not the cardinality of a typical subset.

Commutativity is assumed for the rank interpretation. On the empty universe the unique empty pair contributes the constant term \(1\); assertions about positive \(a,b,c\) concern \(n\geq1\). All generating-function identities are interpreted formally in \(z\); every coefficient of \(z^n\) receives contributions from finitely many indices.

## Proof

**1. The modal-composition criterion.** A relation is uniquely determined by its existential powerset operator by testing singleton input sets. Hence \(\Diamond_R\Diamond_S=\Diamond_S\Diamond_R\) if and only if \(R\circ S=S\circ R\). Moreover, \(R\circ S\) is reflexive and contains both \(R\) and \(S\). It is transitive if and only if \((R\circ S)\circ(R\circ S)=R\circ S\), the latter being equivalent to idempotence of \(\Diamond_R\Diamond_S\). When it is transitive, the fact that it contains both symmetric relations makes it symmetric: if \(xRySz\), then \(zSyRx\), and transitivity of \(R\circ S\) closes these two steps. Thus \(R\circ S\) is an equivalence relation containing \(R\cup S\); conversely it is contained in \(R\vee S\). Hence \(R\circ S=R\vee S\). Since inversion reverses composition, this holds precisely when \(R\circ S=S\circ R\).

**2. Connected rectangular decomposition.** Consider one equivalence class \(C\) of \(R\vee S\). If \(R\circ S=R\vee S\), every \(R\)-class \(U\subseteq C\) meets every \(S\)-class \(V\subseteq C\): for \(x\in U\), \(y\in V\), one has \(x(R\circ S)y\), and a mediator lies in \(U\cap V\). Conversely, if every such intersection is nonempty in each join-class, a mediator shows that \(R\circ S\) connects all pairs in each join-class; thus \(R\circ S=R\vee S\). Each join-class therefore decomposes uniquely into a complete \(r\)-by-\(s\) grid of **nonempty** intersections between its \(r\) restricted \(R\)-classes and \(s\) restricted \(S\)-classes.

**3. Exact count of one component.** On a fixed \(j\)-element labelled set, fixing positive \(r,s\), label the \(r\) rows and \(s\) columns temporarily. Assigning all \(j\) labels surjectively to the \(rs\) cells gives \((rs)!\,\left\{\begin{smallmatrix}j\\rs\end{smallmatrix}\right\}\) assignments, where the braced number is Stirling of the second kind. Forgetting the row and column labels divides by \(r!s!\); this action is free because every cell is nonempty. Therefore the count is

\[
C_j(r,s)=\frac{(rs)!}{r!s!}\left\{\begin{matrix}j\\rs\end{matrix}\right\},\qquad j\geq rs,
\]

and zero otherwise. Its exponential generating function in \(j\) is \((e^z-1)^{rs}/(r!s!)\). Each component contributes \(r\) to \(a\), \(s\) to \(b\), and \(1\) to \(c\). The unordered labelled set of components therefore has the exponential generating function displayed in the Finding.

**4. Composite image rank.** Under commutation, \(\Diamond_R\Diamond_S=\Diamond_{R\vee S}\). The image consists of exactly all unions of the \(c\) join-classes, which gives \(2^c\) possible subsets. Therefore the coefficient at \(t^c\) is the exact count for composite image cardinality \(2^c\).

**5. Sharp support.** If the \(c\) components have respectively \(r_i,s_i\geq1\) row and column classes, then \(a=\sum_i r_i\), \(b=\sum_i s_i\), and each component contains at least \(r_i s_i\) points. Thus

\[
n\geq\sum_{i=1}^{c}r_is_i=a+b-c+\sum_{i=1}^{c}(r_i-1)(s_i-1).
\]

For \(c=1\) this is \(n\geq ab\). For \(c\geq2\) it implies \(n\geq a+b-c\). These bounds are attainable: in the first case take one \(a\)-by-\(b\) grid with singleton cells; in the second take \((r_1,s_1)=(a-c+1,1)\), \((r_2,s_2)=(1,b-c+1)\), and \((r_i,s_i)=(1,1)\) for remaining components. Adding any number of extra labels to a pre-existing cell preserves all three quotient class counts. No configuration can have \(c>\min(a,b)\), since each component has at least one class of each relation. This proves necessity and sufficiency.

**6. Exact integral recurrence.** As a coefficient-extraction alternative, initialize \(N_0(0,0,0)=1\). For \(n\geq1\), distinguish one point and let its join-component have \(j\) points. Counting its other labels, its \(r,s\) grid, and the remainder yields

\[
\boxed{\displaystyle
N_n(a,b,c)=\sum_{j=1}^n\binom{n-1}{j-1}
\sum_{\substack{r,s\geq1\\rs\leq j}}
\frac{(rs)!}{r!s!}\left\{\begin{matrix}j\\rs\end{matrix}\right\}
N_{n-j}(a-r,b-s,c-1).}
\]

Out-of-range entries vanish. The recurrence is an exact finite algorithm involving nonnegative integers only.

## Verification

The standalone standard-library script `verify.py` computes the refined recurrence through \(n=9\), checks symmetry in \(a,b\), and independently enumerates all ordered partition pairs through \(n=6\) using direct binary-relation composition. The exact refined counts agree. For \(n\leq4\), it explicitly evaluates both powerset modalities on every subset, checks commutation and composite idempotence, and verifies composite image cardinality \(2^c\).

As a numerical example, for \(n=6\) the multiplicities for \(c=1,2,3,4,5,6\) are respectively \(915,3363,2550,585,45,1\). Their sum is \(7459\), agreeing with the known unrefined sequence. Other unrefined totals through \(n=9\) are \(1,1,4,19,117,864,7459,73749,818960,10078023\), beginning at \(n=0\).

These checks are finite verification only. The proof of every-\(n\) validity is the structural argument above.

## Relationship to prior work

OEIS A354458 (Critzer, first recorded May 30, 2022) **already records the unrefined number of commuting ordered pairs of finite equivalence relations**, with the relation-composition characterization and small totals. The present finding does **not** claim to discover those totals. Its distinct content is the joint three-parameter formula, its interpretation as a complete composite-modal image-rank census, and the sharp support transition at one versus multiple join-classes.

Green (2017) investigates composition and lattice join of decidable equivalence relations on a countable domain, with computability rather than labelled finite-rank enumeration as its target. Van De Putte and Klein (2022) develop pooling modalities and pointwise intersection in neighbourhood semantics; their operations, proof targets, and invariants differ from the exact commuting-equivalence census. Claesson, Dukes, and Kubitzke study partition/composition matrices, notably upper-triangular set-valued matrices with allowed empty cells and other ordering constraints; their enumerations do not provide the all-positive rectangular-grid joint rank formula here.

## Limitations

The count concerns **ordered** pairs of equivalence relations, not simultaneous conjugacy classes under relabelling, and counts image **cardinality**, not arbitrary multi-modal term clones. It does not assert uniqueness of the refined formula against every unindexed or older source: a translation of the all-positive grid decomposition or known enumerations of permuting congruences might already yield an equivalent refinement. The total-count marginal is explicitly known prior art. The remaining originality risk concerns equivalent historical multivariate enumerations.

## References

1. Geoffrey Critzer, OEIS A354458, “Number of commuting pairs of equivalence relations on [n],” 2022-05-30, https://oeis.org/A354458.
2. Edward J. Green, “Semi-decidable equivalence relations obtained by composition and lattice join of decidable equivalence relations,” arXiv:1711.03056, first submitted 2017-11-08, https://arxiv.org/abs/1711.03056.
3. Frederik Van De Putte and Dominik Klein, “Pooling Modalities and Pointwise Intersection: Semantics, Expressivity, and Dynamics,” *Journal of Philosophical Logic* 51 (2022), 485–523, published online 2022-01-07, https://doi.org/10.1007/s10992-021-09638-0.
4. Anders Claesson, Mark Dukes, and Martina Kubitzke, “Partition and Composition Matrices,” available preprint dated 2020-06-24, https://akc.is/papers/017-Partition-and-composition-matrices.pdf.
