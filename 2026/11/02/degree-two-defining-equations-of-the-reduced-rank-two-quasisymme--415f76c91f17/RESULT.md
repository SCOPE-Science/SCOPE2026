# Degree-two defining equations of the reduced rank-two quasisymmetric Grassmannian

## Finding

For every integer \(n\ge4\), let \(S=\mathbb C[p_{ij}:1\le i<j\le n]\), with each Plücker variable of standard degree one, and let \(I_n\) be the homogeneous radical ideal of the reduced quasisymmetric Grassmannian \(\operatorname{QGr}(2;n)\subset\mathbb P^{\binom n2-1}\). Denote by \(P_n\) the Plücker ideal of \(\operatorname{Gr}(2;n)\).

**Theorem.** The entire degree-two ideal is the direct vector-space sum
\[
(I_n)_2=(P_n)_2\oplus
\operatorname{span}_{\mathbb C}\{p_{ab}p_{bc}:2\le a<b<c\le n\}
\oplus
\operatorname{span}_{\mathbb C}\{p_{ab}p_{cd}:2\le a<b<c<d\le n\}.
\]
Thus the Plücker quadrics, the \(\binom{n-1}{3}\) forbidden-adjacency products from the rank-two quasisymmetric Johnson graph, and precisely \(\binom{n-1}{4}\) additional disjoint-index products form a basis of all quadratic equations. Explicitly, writing \(N=\binom n2\),
\[
\dim_{\mathbb C}(I_n)_2=2\binom n4,\qquad
\dim_{\mathbb C}(S/I_n)_2=\binom{N+1}{2}-2\binom n4.
\]
For \(n=4\), there are no additional quadrics beyond the Plücker and forbidden-adjacency equations. For every \(n\ge5\), those original quadratic equations do not span the degree-two ideal of the reduced union; already at \(n=5\), the independent extra equation is \(p_{23}p_{45}=0\).

This is a degree-two statement, **not** a claim that the displayed equations generate the full homogeneous ideal or that the unsaturated projective scheme determined by the smaller set of equations is nonreduced.

## Assumptions and scope

All schemes and toric orbit closures are over \(\mathbb C\). The quasisymmetric Grassmannian is the **reduced** union of toric components constructed in Bergeron--Gagnon--Spink--Tewari (2026). For each integer \(b\) with \(1\le b\le n-2\), write \(X_b\) for the maximal component with rank-two matroid parallel classes
\[
\{1\},\quad \{2,\ldots,b+1\},\quad\{b+2,\ldots,n\}.
\]
The existence and completeness of these \(n-2\) components follow by specializing the component and moment-polytope descriptions in the cited paper. A concrete dense torus orbit is obtained by taking a \(2\times n\) matrix whose first column is \((1,0)^T\), columns \(2,\ldots,b+1\) are \((0,1)^T\), and remaining columns are \((1,1)^T\), independently scaled by nonzero scalars. The projective closure of this orbit is \(X_b\). We use the standard Plücker convention \(p_{ij}=\det(c_i,c_j)\) for \(i<j\).

## Proof

**1. Multigrading and component restrictions.** Give \(S\) the \(\mathbb Z^n\)-grading \(\deg p_{ij}=e_i+e_j\). The ideal of the reduced union equals \(I_n=\bigcap_{b=1}^{n-2}I(X_b)\), so a quadratic is in \(I_n\) precisely when its restriction to every dense component torus vanishes. On the torus of \(X_b\),
\[
p_{ij}=\epsilon_{ij}^{(b)}t_it_j,
\quad \epsilon_{ij}^{(b)}\in\{0,1,-1\},
\]
where the coefficient is zero exactly when \(i,j\) lie in the same one of the three parallel classes. Thus, inside any fixed multidegree, the rank of the degree-two restriction map is the rank of a matrix with one row for each component and one column per quadratic monomial of that multidegree. Different multidegrees cannot cancel.

**2. Repeated-index weights.** A weight involving only two different indices has the unique monomial \(p_{ij}^2\), and it is nonzero on some \(X_b\). A weight with three different indices is specified by \(a<b<c\) and a repeated index; its single monomial is a product of two Plücker variables sharing that index. If the repeated index is \(b\), the monomial \(p_{ab}p_{bc}\) vanishes on every component exactly when \(a\ge2\): the middle index cannot be separated simultaneously from its neighbors by a single cut of the ordered set \(\{2,\dots,n\}\). If \(a=1\), the first Plücker factor is always supported and a cut between \(b\) and \(c\) supports the other factor. If the repeated index is either endpoint \(a\) or \(c\), a cut between the other two indices makes both factors nonzero. Consequently the only quadratic relations in the repeated-index weight spaces are exactly \(p_{ab}p_{bc}\) for \(2\le a<b<c\le n\).

**3. Four distinct indices.** Fix \(a<b<c<d\). There are three quadratic monomials in this weight:
\[
u=p_{ab}p_{cd},\qquad v=p_{ac}p_{bd},\qquad w=p_{ad}p_{bc}.
\]
The ordinary Plücker relation \(u-v+w=0\) always holds. If \(a\ge2\), any cut among the ordered indices leaves both factors of \(u\) nonzero on no component: for a cut between \(a,b\) or between \(c,d\), one factor has both indices in the same class; for a cut between \(b,c\), **both** factors do. Therefore \(u\in I_n\). A cut between \(b,c\) supports both \(v\) and \(w\), giving a one-dimensional nonzero restriction image. Hence the kernel in this multidegree has dimension exactly two, spanned by the Plücker relation and \(u\).

If \(a=1\), choose first a component whose cut lies between \(b,c\), and next one whose cut lies between \(c,d\). On the first, \(w=0\) while \(u,v\ne0\); on the second, \(u=0\) while \(v,w\ne0\). These two restriction rows are independent. Therefore the restriction map has rank two; its sole quadratic relation is the Plücker relation. This exhausts the four-distinct-index multidegrees.

**4. Independence and dimensions.** The degree-two Plücker relations give one independent vector in each four-distinct-index weight, hence dimension \(\binom n4\). The forbidden-adjacency monomials occupy distinct repeated-index weights; there are \(\binom{n-1}{3}\). The extra disjoint-index monomials occupy the \(\binom{n-1}{4}\) four-distinct-index weights avoiding index \(1\), where they are linearly independent of the Plücker relation. No other weight admits a quadratic equation by steps 2--3. Using Pascal's identity,
\[
\binom n4+\binom{n-1}{3}+\binom{n-1}{4}=2\binom n4.
\]
Subtracting from \(\dim S_2=\binom{N+1}{2}\) proves both formulas. When \(n\ge5\), the extra monomials cannot lie in the degree-two span of the previously cited Plücker and quasisymmetric-Johnson-edge products by the same multigrading argument.

## Verification

The standalone pure-Python checker `verify_quadrics.py` constructs all quadratic monomials for \(4\le n\le10\), partitions them by torus multidegree, and computes exact rational ranks of their restrictions to all \(n-2\) component tori using the explicit \(2\times n\) column representatives. It verifies the weight-by-weight rank rules, both dimension formulas, and the additional-quadric count, reporting `VERIFY_OK`. Its tests are finite consistency checks; the proof above treats every \(n\ge4\).

## Relationship to prior work

Bergeron, Gagnon, Spink and Tewari (arXiv:2604.24903, first submitted 2026-04-27), Theorem B/5.1, supply a **set-theoretic** Plücker-product description, and Sections 5 and 9 determine the toric components. This theorem instead determines the **degree-two vector space of the homogeneous ideal of the reduced projective union**. The forbidden-adjacency products, the geometric decomposition, and the usual Plücker relations are prior results; the exact additional \(\binom{n-1}{4}\) equations and complete degree-two ideal decomposition are the contribution here. Gonzales, Le and Lowen (arXiv:2609.30257, first submitted 2026-09-24) develop the Chow theory of toric Richardson varieties, not the specific quadratic homogeneous ideal of their finite union. The general Plücker straightening framework gives only the starting rank-one four-index relation, not the extra vanishing dictated by the component union.

## Limitations

The theorem does not determine higher-degree minimal generators, a full Gröbner basis, the Hilbert series in degrees \(\ge3\), the saturation of a particular naive presentation, or infinitesimal scheme structure of that presentation. Its dimension formula is for the reduced union with the fixed projective Plücker embedding. Historical priority beyond the identified sources remains open and no independent mathematical audit has been performed.

## References

1. Nantel Bergeron, Lucas Gagnon, Hunter Spink, Vasu Tewari, *The Quasisymmetric Grassmannian* (2026), arXiv:2604.24903, https://arxiv.org/abs/2604.24903; especially Theorem B, Section 5, and Theorems 9.1/9.3.
2. Teddy Gonzales, Tuong Le, Chayim Lowen, *A quasisymmetric analog of Grassmannian Schubert varieties* (2026), arXiv:2609.30257, https://arxiv.org/abs/2609.30257; sections on toric Richardson varieties and their Chow groups.
3. Viktoriia Borovik, Takayuki Hibi, *Elimination ideals of Plücker ideals and algebras with straightening laws* (2026), arXiv:2601.06897, https://arxiv.org/abs/2601.06897; related Plücker straightening and projections, not the same reduced toric union.
