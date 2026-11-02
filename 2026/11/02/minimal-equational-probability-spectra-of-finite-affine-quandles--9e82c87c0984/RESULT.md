# Minimal equational probability spectra of finite affine quandles

## Finding

Let \(A\) be a nonzero finite abelian group, \(T\in\operatorname{Aut}(A)\), and define the left affine quandle
\[
Q(A,T)=(A,*),\qquad x*y=(1-T)x+Ty.
\]
For an equation \(u=v\) between constant-free terms in the one binary operation \(*\), let \(\Pr_Q(u=v)\) be the proportion of all assignments of its variables in \(A\) that satisfy the equation. Let \(\operatorname{Spec}(Q)\) be the set of all these probabilities, with arbitrary finite sets of variables permitted.

**Classification theorem.** If \(|A|>1\), then
\[
\operatorname{Spec}(Q)=\{1/|A|,1\}
\]
if and only if either (a) \(T=1\), so \(x*y=y\), or (b) \(1-T\) is invertible and the finite commutative ring \(R=\mathbb Z[T]\subseteq\operatorname{End}(A)\) is a field. In case (b), uniquely up to the usual finite-field isomorphism and conjugacy data, there are a prime \(p\), a divisor \(d\) of \(m\), an integer \(s=m/d\), and \(\lambda\in\mathbb F_{p^d}\setminus\{0,1\}\) whose minimal polynomial over \(\mathbb F_p\) has degree \(d\), such that
\[
A\cong(\mathbb F_{p^d})^s,\qquad T(a)=\lambda a,\qquad |A|=p^m.
\]
This is a statement about the coefficient ring acting faithfully on the entire group, not about individual invariant factors of \(T\). In particular, \(s>1\) is allowed. Whenever the stated criterion fails, a two-variable equation already has probability strictly between \(1/|A|\) and \(1\).

**Isomorphism and enumeration theorem.** Let \(I_p(d)\) be the number of monic irreducible polynomials of degree \(d\) over \(\mathbb F_p\):
\[
I_p(d)=\frac1d\sum_{e\mid d}\mu(e)p^{d/e}.
\]
For \(n=p^m\), the number of isomorphism classes of minimal-spectrum affine quandles on \(n\) points is
\[
1+\sum_{d\mid m}\left(I_p(d)-2\mathbf1_{d=1}\right).
\]
The initial \(1\) is the projection quandle. For a fixed labeled set of \(n=p^m\) points, the number of distinct operations is
\[
1+\sum_{d\mid m}\left(I_p(d)-2\mathbf1_{d=1}\right)
\frac{n!}{n\,|\operatorname{GL}_{m/d}(\mathbb F_{p^d})|}.
\]
For non-prime-power \(n>1\), exactly one affine quandle operation has minimal spectrum: the projection operation. For every nonprojection class corresponding to \((p,d,s,\lambda)\), the automorphism group has order \(p^m|\operatorname{GL}_{s}(\mathbb F_{p^d})|\).

## Assumptions and scope

Terms have no named constants, and may use the same variable repeatedly. Equational probabilities are over **independent uniform assignments** to all variables actually appearing; adding unused variables does not change the probability. The opposite affine convention is obtained by exchanging the two arguments, so the probability statement is unaffected by consistent opposite-convention translation. An abelian group of order one has spectrum \(\{1\}\) and is excluded from the nontrivial assertion. The single binary operation is the affine quandle operation; no addition or scalar maps are admitted in the term language. The isomorphism counts are quandle-isomorphism counts, not counts of different module presentations.

## Proof

**1. Elementary witnesses.** Put \(B=1-T\). If \(T=1\), every nonempty term evaluates to its rightmost variable. Consequently each equation is either identically true or asserts equality of two independently uniform variables, of probabilities \(1\) and \(1/|A|\). These are both realized for \(|A|>1\).

Suppose \(T\ne1\) and \(B\) is noninvertible. Since \(A\) is finite, \(0\ne B\) has a kernel of cardinality strictly between \(1\) and \(|A|\): noninvertibility forces a nonzero kernel, while \(B\ne0\) excludes all of \(A\). The two-variable equation \(x*y=y\) is equivalent to \(B(x-y)=0\), and hence has probability \(|\ker B|/|A|\), strictly intermediate. Therefore minimal spectrum with \(T\ne1\) requires both \(T\) and \(B\) invertible.

**2. Every coefficient in \(\mathbb Z[T]\) is a binary term coefficient.** Now assume \(T\) and \(B\) are automorphisms. The subring \(R=\mathbb Z[T]=\mathbb Z[B]\) of the endomorphism ring is finite and commutative. Both \(T\) and \(B\) are units of \(R\): each has finite multiplicative order as an automorphism of \(A\), so its inverse is a positive integral power in \(R\).

By induction every binary term has the form \(t_f(x,y)=fx+(1-f)y\) for some \(f\in R\). Conversely, let \(F\subseteq R\) be the set of coefficients realized by binary terms. The variables \(x,y\) give \(1,0\in F\). Composition \(u*v\) transforms coefficients by
\[
(f,g)\longmapsto Bf+Tg.
\]
In particular, \(H_0(f)=Bf\) and \(H_1(f)=Bf+T\) carry \(F\) into itself. As \(B\) is invertible, each of these maps is injective on the finite set \(F\), hence permutes it. Thus \(H_1H_0^{-1}\) is translation by \(T\) on \(F\). Conjugating by \(H_0^j\) gives translation by \(B^jT\) for all \(j\ge0\). Their integer additive span is \(T\mathbb Z[B]=TR=R\), since \(T\) is a unit. Because \(0\in F\), these translations generate every element of \(R\) within \(F\). It follows that \(F=R\).

**3. The precise field obstruction.** If \(R\) is not a field, then this finite commutative ring has a nonzero nonunit \(f\). Its action on \(A\) is not invertible: if it were a bijective endomorphism, some positive power of \(f\) would act as the identity on the finite group, forcing \(f\) to be a unit already in \(R\). Faithfulness of \(R\hookrightarrow\operatorname{End}(A)\) implies \(f\ne0\) has a non-total kernel, while noninvertibility implies a nontrivial kernel. By Step 2 the coefficient \(f\) is realized by a binary term \(t_f\). The equation \(t_f(x,y)=y\) has probability \(|\ker f|/|A|\) strictly between \(1/|A|\) and \(1\). This proves necessity of the field condition.

Conversely, suppose \(R\) is a field. Every term in variables \(x_1,\ldots,x_k\) evaluates as \(\sum_i f_i x_i\) with \(f_i\in R\) and \(\sum_i f_i=1\), by induction on term construction and \(B+T=1\). For two terms, their difference is the \(R\)-linear map \((x_i)\mapsto\sum_i c_i x_i\). If all \(c_i\) vanish, the equation holds identically. Otherwise one \(c_j\ne0\) is invertible, making this map onto \(A\), with each fiber of cardinality \(|A|^{k-1}\). Hence the equation probability is \(1/|A|\). The equation \(x=y\) realizes \(1/|A|\), and \(x=x\) realizes \(1\).

**4. Structure of the field case.** If \(R\) is a field of characteristic \(p\), then \(p\) acts as zero on \(A\), so \(A\) is an elementary abelian \(p\)-group. There is an integer \(d\ge1\) with \(R\cong\mathbb F_{p^d}\), and \(A\) is a vector space over \(R\), say of dimension \(s\). As the field is generated by the operator \(T\), it corresponds to a scalar \(\lambda\) with \(\mathbb F_p[\lambda]=\mathbb F_{p^d}\), equivalently \(\lambda\) has minimal polynomial of degree \(d\). Invertibility of \(T\) and \(1-T\) is equivalent to \(\lambda\ne0,1\). Conversely, each such datum makes \(R\) a field and gives a Latin affine quandle of minimal spectrum. Its cardinality is \(p^{ds}\). For non-prime-power orders, the only remaining possibility is the projection case.

**5. Isomorphism types and labeled enumeration.** In a Latin affine quandle the left translations satisfy
\[
L_xL_z^{-1}(w)=w+B(x-z).
\]
Because \(B\) is bijective, the intrinsic group generated by these displacements is exactly the regular translation group of the additive group \(A\). Thus every isomorphism between two such quandles conjugates their regular translation groups. A bijection that normalizes their translation groups is affine with respect to an additive-group isomorphism; after translating the image of zero to zero, the isomorphism is additive. Preservation of \(*\) then says that the additive isomorphism intertwines \(T\) and the target operator. Hence the isomorphism classification is precisely conjugacy of \(T\) as an \(\mathbb F_p\)-linear automorphism, once the elementary abelian group is fixed.

For each \(d\mid m\), and every monic irreducible polynomial \(g\) of degree \(d\) except \(g=X\) and \(g=X-1\), there is exactly one resulting conjugacy class: the \(\mathbb F_p\)-linear transformation with minimal polynomial \(g\) and rational canonical module \((\mathbb F_p[X]/(g))^{m/d}\). Its centralizer in \(\operatorname{GL}_m(\mathbb F_p)\) is \(\operatorname{GL}_{m/d}(\mathbb F_{p^d})\). The displacement calculation also shows the complete quandle automorphism group consists of translations followed by these centralizing linear maps, and thus has order \(p^m|\operatorname{GL}_{m/d}(\mathbb F_{p^d})|\).

The standard irreducible-polynomial formula gives \(I_p(d)\). Excluding \(X,X-1\) removes two degree-one polynomials and no higher-degree polynomials. Summing these conjugacy types, then adding the unique projection type, proves the isomorphism formula. Finally, each isomorphism class has \(n!/|\operatorname{Aut}(Q)|\) distinct operations on a labeled \(n\)-point set by orbit–stabilizer, giving the second formula. The projection quandle has full symmetric automorphism group and contributes exactly one labeled operation. All parts of the classification follow.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently constructs the finite rings \(\mathbb F_p[B]\) in several matrix realizations, enumerates term coefficients from the binary operation rather than inserting arbitrary ring coefficients, and computes attainable equation probabilities via ranks of linear maps over the underlying prime field. A binary quadratic-irreducible example, a repeated irreducible block, a ternary scalar example, a non-Latin operator, a Latin nonsemisimple operator, a split Latin operator, and a projection example are included. It also independently checks the small-order polynomial/isomorphism enumeration. Executing `python3 verify.py` produced `VERIFY_OK`. The full general result is proved in the preceding paragraphs; these examples are not a substitute for the proof.

## Relationship to prior work

Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487v1 (public March 19, 2026), develops the minimal-equational-probability property for groupoids, proves an overall necessary classification into special families including quasigroups, and settles the associative semigroup branch. The present theorem resolves the concrete family of finite affine quandles, including the Latin/quasigroup case, by a coefficient-ring criterion and gives an exact isomorphism and labeled enumeration. No claim is made that the general minimal-spectrum definition or its preliminary groupoid reductions are new.

Jedlička, Pilitowska, Stanovský and Zamojska-Dzienio, *Subquandles of affine quandles* (arXiv:1708.02362, published 2018), gives standard affine-quandle structure and isomorphism theory, used here for context; the isomorphism argument above is also proved directly in the Latin case. The identified results concern affine-quandle isomorphisms and subquandles, rather than equational-probability spectra. Other relevant finite-module classification literature may encode the same conjugacy classes but does not by itself establish the minimal-spectrum criterion.

## Limitations

The theorem treats **finite affine quandles**, not all quasigroups, all Latin quandles, or all groupoids. The scalar-field condition is necessary only for nonprojection affine quandles; the projection exception is essential. The isomorphism enumerations count operations, not distinct choices of presentations for \((A,T)\). The conclusion is a self-review, not an independent proof audit or an assertion of absolute historical priority; an equivalent formulation in older clone-theoretic or universal-algebra literature may exist. Computations cover only small examples and prove no arbitrary-order assertion by themselves.

## References

- C. Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487v1, March 19, 2026. https://arxiv.org/abs/2603.19487
- C. Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446, April 2026. https://arxiv.org/abs/2604.08446
- P. Jedlička, A. Pilitowska, D. Stanovský and A. Zamojska-Dzienio, *Subquandles of affine quandles*, arXiv:1708.02362 (2017), *J. Algebra* **510** (2018). https://arxiv.org/abs/1708.02362
- X.-D. Hou, *Finite modules over \(\mathbb Z[t,t^{-1}]\)*, *J. Knot Theory Ramifications* **21** (2012); bibliographic background on affine-quandle modules, not a verified source for the probability theorem.
