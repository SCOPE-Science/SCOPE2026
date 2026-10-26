# Rank-one Rota–Baxter loci of truncated polynomial algebras

## Finding

Let \(k\) be any field, let \(n\ge 4\), and set \(A_n=k[t]/(t^n)\). A *weight-zero Rota–Baxter operator* is a \(k\)-linear map \(P:A_n\to A_n\) satisfying
\[
P(x)P(y)=P\bigl(xP(y)+P(x)y\bigr)\qquad(x,y\in A_n).
\]
Let \(\mathcal R_n\) be the **reduced algebraic variety** of such operators with \(\operatorname{rank}_k P\le1\). Define \(m=\lceil n/2\rceil\), \(h=\lfloor n/2\rfloor\), and, for \(m\le i<n\),
\[
W_i=t^iA_n,\qquad U_i=\{\varphi\in A_n^\vee:\varphi(W_i)=0\},
\]
\[
C_i=\{P:P(x)=\varphi(x)a\text{ for some }a\in W_i,\ \varphi\in U_i\}.
\]
Then **the complete reduced rank-at-most-one locus** is
\[
\boxed{\mathcal R_n=\bigcup_{i=m}^{n-1} C_i.}
\]
The \(h\) sets \(C_i\) are precisely its irreducible components. Each is the affine cone of rank-at-most-one tensors in \(W_i\otimes_k U_i\), equivalently the cone over the Segre variety
\[
\mathbb P^{n-i-1}\times\mathbb P^{i-1},
\]
and each has dimension \(n-1\). Thus the locus is reducible for every permitted \(n\), yet is equidimensional. For \(m\le i<j<n\),
\[
\boxed{C_i\cap C_j=\{a\otimes\varphi:a\in W_j,\ \varphi\in U_i\},\qquad
\dim(C_i\cap C_j)=n-1-(j-i).}
\]
Its geometric singular locus is exactly \(\bigcup_{i=m}^{n-2}(C_i\cap C_{i+1})\), of pure dimension \(n-2\). The projectivization of \(\mathcal R_n\setminus\{0\}\) has degree \(\sum_{i=m}^{n-1}\binom{n-2}{i-1}\).

If \(k=\mathbb F_q\) for **any prime power** \(q\), the number of operators, including zero, is
\[
\boxed{\#\mathcal R_n(\mathbb F_q)=1+hq^{n-1}-\sum_{j=0}^{h-1}q^j.}
\]
More precisely, for each \(i\) with \(m\le i<n\), the number of **nonzero** such operators whose image is spanned by a vector of \(t\)-adic valuation exactly \(i\) is \(q^{n-i-1}(q^i-1)\).

## Assumptions and scope

The algebra \(A_n\) is unital, commutative, and has basis \(1,t,\ldots,t^{n-1}\). No characteristic hypothesis is imposed. Rank means rank of the underlying \(k\)-linear operator. The geometric assertions concern the **reduced** algebraic set underlying the polynomial Rota–Baxter and rank equations, rather than any possible nonreduced parameter scheme. All irreducibility and singularity assertions remain valid after extending scalars to an algebraic closure. Projectivization removes the zero map.

For a nonzero element \(a\in A_n\), its \(t\)-adic valuation \(v(a)\) is the smallest exponent of \(t\) having nonzero coefficient. A rank-one operator can be written \(P=a\otimes\varphi\), meaning \(P(x)=\varphi(x)a\), with nonzero \(a\in A_n\) and nonzero \(\varphi\in A_n^\vee\). Such a factorization is unique up to simultaneous scaling \((a,\varphi)\mapsto(ca,c^{-1}\varphi)\).

## Proof

**1. Rank-one reduction.** In any commutative associative \(k\)-algebra, write a nonzero rank-one map as \(P(x)=\varphi(x)a\). Substituting into the weight-zero Rota–Baxter identity gives
\[
\varphi(x)\varphi(y)a^2=
\bigl(\varphi(y)\varphi(xa)+\varphi(x)\varphi(ya)\bigr)a.
\tag{1}
\]
Pick \(x_0\) with \(\varphi(x_0)=1\). Putting \(x=x_0\) and \(y\in\ker\varphi\) into (1) shows \(\varphi(ya)=0\) for every \(y\in\ker\varphi\). Consequently there is \(c\in k\) such that \(\varphi(xa)=c\varphi(x)\) for every \(x\). With \(x=y=x_0\), (1) yields \(a^2=2ca\). Composing \(\varphi\) with multiplication by \(a\) twice gives \(\varphi(xa^2)=c^2\varphi(x)\); using \(a^2=2ca\) instead gives \(\varphi(xa^2)=2c^2\varphi(x)\). Thus \(c^2=2c^2\), so \(c=0\) in every characteristic. Therefore \(a^2=0\) and \(\varphi(aA_n)=0\). Conversely these two conditions make both sides of (1) vanish. Hence
\[
\boxed{P=a\otimes\varphi\text{ is weight-zero Rota–Baxter}\iff
a^2=0\text{ and }\varphi(aA_n)=0.}
\tag{2}
\]
This elementary reduction is used as a lemma; its standalone generality is not asserted to be new.

**2. Valuation classification.** Write \(a=t^iu\) with \(u\) a unit. Then \(a^2=0\) if and only if \(2i\ge n\), i.e. \(i\ge m\), and the principal ideal \(aA_n\) equals \(W_i\). By (2), every nonzero rank-one solution with \(v(a)=i\) lies in \(C_i\). Conversely every rank-one tensor in \(C_i\) satisfies (2), since \(W_i^2=0\) and \(aA_n\subseteq W_i\). The zero operator belongs to every \(C_i\), proving the union.

**3. Components and intersections.** The dimensions of \(W_i\) and \(U_i\) are \(n-i\) and \(i\). A rank-at-most-one tensor variety in the tensor product of vector spaces of dimensions \(r,s\) is the affine cone over \(\mathbb P^{r-1}\times\mathbb P^{s-1}\); this cone is irreducible of dimension \(r+s-1\), smooth at every nonzero rank-one point, and has projective degree \(\binom{r+s-2}{r-1}\). One can see irreducibility directly from the surjective polynomial parameterization \((u,v)\mapsto u\otimes v\), and smoothness off zero by using a nonzero matrix entry to solve for all other entries via the vanishing \(2\times2\) minors. Applying these facts to \(C_i\) proves its dimension and degree. Distinct \(C_i\) are not equal: their possible image subspaces decrease strictly while their allowed functionals increase strictly. Since all have the same dimension, none contains another. They therefore are exactly the irreducible components.

For \(i<j\), the common rank-at-most-one tensors have image in \(W_i\cap W_j=W_j\) and defining functional in \(U_i\cap U_j=U_i\), yielding the stated intersection cone and dimension. A nonzero point lying on precisely one component is smooth, whereas points lying on two or more components are singular in the reduced union (the local ring has at least two branches). Each individual cone is smooth away from zero; zero belongs to every component. Every nonadjacent intersection \(C_i\cap C_j\) is contained in \(C_i\cap C_{i+1}\), so the singular locus is exactly the union of adjacent intersections, each of dimension \(n-2\). Because distinct projective components meet in smaller dimension, the projective degree of the reduced union is the sum of their Segre degrees.

**4. Finite-field count.** Fix \(i\ge m\). The number of nonzero \(a\) of valuation \(i\) is \((q-1)q^{n-i-1}\). The annihilator \(U_i\) has \(q^i-1\) nonzero functionals. Each nonzero rank-one operator \(a\otimes\varphi\) is represented by exactly \(q-1\) scaled pairs. Hence the contribution is \(q^{n-i-1}(q^i-1)\). Summing over \(i=m,\ldots,n-1\) gives \(h q^{n-1}-\sum_{j=0}^{h-1}q^j\). Adding the zero operator proves the formula. The count holds for all prime powers, not only primes.

## Verification

The accompanying standalone `CHECKER.py` constructs multiplication in \(\mathbb F_q[t]/(t^n)\), enumerates **all** rank-one linear maps via normalized image generators and arbitrary nonzero functionals, and tests the original Rota–Baxter identity on every ordered pair of algebra basis vectors. The test does not use condition (2) to decide the identity; it compares that decision independently with the valuation/annihilator prediction, its rank-one fiber counts, and the closed total formula. The script includes the boundary \(n=2,3\) as additional checks outside the claimed scope, and covers \(q=2\) with \(2\le n\le7\), \(q=3\) with \(2\le n\le5\), and \(q=4\) with \(2\le n\le4\), comprising **13 parameter cases and 77,267 tested nonzero rank-one maps**. It completed with `RANK_ONE_ROTA_BAXTER_IDENTITY_OK 13 cases`. Arithmetic for \(\mathbb F_4\) uses the irreducible polynomial \(u^2+u+1\). These are finite checks, not a replacement for the unrestricted proof above.

## Relationship to prior work

Guo, Rosenkranz and Zheng (2014 preprint, later 2015 journal publication) develop Rota–Baxter operators on the **untruncated** polynomial algebra and focus on monomial and injective operators. Yu (2015 preprint) classifies monomial operators on that same untruncated algebra. Those settings and classifications do not give the present arbitrary-linear rank-one locus for \(k[t]/(t^n)\). Farooq (2026) treats the different truncation \(k[x_1,\ldots,x_r]/(x_1,\ldots,x_r)^2\), in characteristic zero; its one-variable specialization is the boundary \(n=2\), not the higher-power algebras \(n\ge3\). The elementary rank-one reduction and standard Segre facts are not claimed as novel. The specific filtration-indexed equidimensional decomposition, all intersections, singular locus and all-field finite-point formula are the proposed contribution. Search results do not establish absolute priority; an unindexed general classification might imply them.

## Limitations

This determines only the **rank-at-most-one** locus, not all higher-rank Rota–Baxter operators. The geometric variety is reduced by definition; no statement about nilpotent embedded scheme structure is made. No classification modulo algebra automorphisms is asserted. No independent mathematical audit or absolute publication-priority certification has been performed.

## References

1. L. Guo, M. Rosenkranz, S. Zheng, *Rota–Baxter operators on the polynomial algebras, integration and averaging operators*, arXiv:1407.5306v1, publicly posted 2014-07-20; Pacific Journal of Mathematics 275 (2015), 481–507. https://arxiv.org/abs/1407.5306 ; public full text: https://kar.kent.ac.uk/45956/1/GuoRosenkranzZheng.pdf
2. H. Yu, *Classification of monomial Rota–Baxter operators on k[x]*, arXiv:1503.02606v1, publicly posted 2015-03-09. https://arxiv.org/abs/1503.02606
3. A. Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1, publicly posted 2026-05-15, Section 3. https://arxiv.org/html/2605.15670v1
