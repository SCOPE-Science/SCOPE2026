# Automorphisms of truncated coordinate-cross algebras over arbitrary fields

## Finding
Let \(k\) be any field and let \(n\ge2\). For \(d\ge2\), set
\[
A_{n,d}(k)=k[x_1,\ldots,x_n]/(x_i x_j\ (i\ne j),\ x_1^d,\ldots,x_n^d).
\]
When \(d=2\), the maximal ideal has square zero, so every invertible linear map of its cotangent space is an algebra automorphism and
\[
\operatorname{Aut}_k(A_{n,2})\cong\operatorname{GL}_n(k).
\]
For every \(d\ge3\), let \(J_d(k)=\operatorname{Aut}_k(k[t]/(t^d))\), written as truncated substitutions
\[
t\longmapsto a_1t+a_2t^2+\cdots+a_{d-1}t^{d-1},\qquad a_1\ne0.
\]
Every automorphism of \(A_{n,d}(k)\) has a unique normal form
\[
x_i\longmapsto f_i(x_{\sigma(i)})+\sum_{j\ne\sigma(i)}c_{ij}x_j^{d-1},
\]
with \(\sigma\in S_n\), \(f_i\in J_d(k)\), and \(c_{ij}\in k\). Hence
\[
\operatorname{Aut}_k(A_{n,d})\cong k^{n(n-1)}\rtimes\bigl(J_d(k)^n\rtimes S_n\bigr).
\]
The additive normal subgroup consists of the off-branch top-degree shears. If \(a_i\) denotes the linear coefficient on branch \(i\), conjugation by branch substitutions scales the shear coefficient from branch \(i\) to branch \(j\) by \(a_j^{d-1}a_i^{-1}\); permutations act by simultaneous permutation of branch indices.

Over an algebraically closed field of characteristic zero, \(\operatorname{Aut}(A_{n,2})=\operatorname{GL}_n\) is connected reductive, while for \(d\ge3\) the component group is \(S_n\), the identity component is solvable, and its reductive quotient is \((\mathbb G_m)^n\). Over a finite field \(\mathbb F_q\),
\[
|\operatorname{Aut}(A_{n,d}(\mathbb F_q))|=n!(q-1)^nq^{n(n+d-3)}\qquad(d\ge3).
\]

## Assumptions and scope
The group-theoretic normal form is proved for every field \(k\), with no restriction on characteristic. The algebraic-group statements about connected components and reductive quotients are asserted only over an algebraically closed field of characteristic zero. The finite-field formula is valid for every prime power \(q\). The family is the finite-dimensional truncation of the Stanley--Reisner ring of \(n\) isolated vertices, with each coordinate branch cut off at order \(d\).

## Proof
Let \(\mathfrak m=(x_1,\ldots,x_n)\). For \(d\ge3\), an automorphism preserves \(\mathfrak m\) and induces an invertible map \(L\) on \(V=\mathfrak m/\mathfrak m^2\). In \(\mathfrak m^2/\mathfrak m^3\), the classes of \(x_1^2,\ldots,x_n^2\) are linearly independent and the product of two distinct coordinate classes is zero. Write
\[
L(\bar x_i)=\sum_r a_{ri}\bar x_r.
\]
For \(i\ne j\), the relation \(x_ix_j=0\) gives
\[
0=L(\bar x_i)L(\bar x_j)=\sum_r a_{ri}a_{rj}\overline{x_r^2}.
\]
Thus each row of the matrix \((a_{ri})\) contains at most one nonzero entry. Since \(L\) is invertible, every row and every column contains exactly one nonzero entry. Therefore the linear part is a monomial matrix, determining a unique permutation \(\sigma\) of the branches.

Write the image of a generator as a sum of branch components,
\[
\phi(x_i)=\sum_r f_{ir}(x_r),\qquad f_{ir}(t)\in t\,k[t]/(t^d).
\]
On the principal branch \(r=\sigma(i)\), the polynomial \(f_{i,\sigma(i)}\) has valuation one and nonzero linear coefficient. For any other source \(i\ne \sigma^{-1}(r)\), the relation between \(\phi(x_i)\) and the generator whose principal branch is \(r\) yields
\[
f_{ir}(x_r)f_{\sigma^{-1}(r),r}(x_r)=0.
\]
The second factor is \(x_r\) times a unit in \(k[x_r]/(x_r^d)\), whose annihilator is exactly \(k x_r^{d-1}\). Hence every off-principal branch component is a scalar multiple of \(x_r^{d-1}\). Conversely, any map of the displayed normal form preserves all defining relations and has invertible linear part, hence is an automorphism. Uniqueness follows from the direct-sum decomposition of \(\mathfrak m\) into its coordinate branches and from uniqueness of the monomial linear part.

Let \(W\) be the subgroup of shears
\[
x_i\longmapsto x_i+\sum_{j\ne i}c_{ij}x_j^{d-1}.
\]
Because products between distinct branches vanish and \((x_j^{d-1})^2=0\), composition adds the coefficients, so \(W\cong(k,+)^{n(n-1)}\). Branchwise substitutions give \(J_d(k)^n\), permutations give \(S_n\), and the normal form gives a split exact sequence with kernel \(W\). If a branch substitution has linear coefficient \(a_i\), direct conjugation shows that \(c_{ij}\) is multiplied by \(a_j^{d-1}a_i^{-1}\). This proves the semidirect-product description.

For \(d=2\), one has \(\mathfrak m^2=0\), so multiplication imposes no restriction on the induced linear map and every element of \(\operatorname{GL}_n(k)\) extends uniquely to an automorphism fixing \(1\).

Finally, over \(\mathbb F_q\), the group \(J_d(\mathbb F_q)\) has \((q-1)q^{d-2}\) elements: the linear coefficient is nonzero and the remaining \(d-2\) coefficients are arbitrary. Multiplying the orders of \(W\), \(J_d(\mathbb F_q)^n\), and \(S_n\) gives
\[
q^{n(n-1)}\bigl((q-1)q^{d-2}\bigr)^n n!=n!(q-1)^nq^{n(n+d-3)}.
\]

## Verification
The included `verify.py` enumerates algebra endomorphisms in six small prime-field cases. It tests the defining relations directly, checks invertibility of the induced map on \(\mathfrak m/\mathfrak m^2\), verifies the normal-form restriction when \(d\ge3\), and compares the exhaustive count with the closed formula. The checked cases are \((q,n,d)=(2,2,2),(2,3,2),(2,2,3),(3,2,3),(2,2,4),(2,3,3)\). The saved output ends with `CHECK_OK`. These finite enumerations are consistency checks; the proof above establishes the result over arbitrary fields and arbitrary \(n,d\) in the stated ranges.

## Relationship to prior work
Díaz, Lucchini Arteche, and Manzano-Flores analyze automorphism groups of zero-dimensional monomial algebras over algebraically closed fields of characteristic zero and give a structural description in terms of homogeneous nilpotent derivations and root subgroups. Their paper explicitly places these groups in the setting of finite-dimensional monomial algebras and has primary MSC 13F55. The accepted claim here is not that the characteristic-zero case escapes that general theory; rather, it gives an elementary closed normal form for the truncated isolated-vertex family that remains valid over arbitrary fields, including positive characteristic, together with an exact finite-field order formula and the \(d=2\) versus \(d\ge3\) structural transition.

The earlier work of Díaz, Liendo, Manzano-Flores, and Regeta determines automorphism groups of finite-dimensional monomial algebras under a characteristic-zero hypothesis. Díaz and Lucchini Arteche likewise prove characteristic-zero reconstruction results and use the two-variable ideal \((x^3,xy,y^3)\), the case \((n,d)=(2,3)\) of the present family, as an example for derivation weights. Those results are therefore treated as strong coverage of the characteristic-zero slice, not as evidence of novelty there. The field-uniform normal form and finite-field enumeration are the additional content.

## Limitations
No claim is made that the characteristic-zero specialization is independent of the general characteristic-zero theory of monomial-algebra automorphisms. The originality claim concerns the explicit arbitrary-field normal form, its positive-characteristic validity, and the resulting finite-field order formula. Searches did not locate an older positive-characteristic treatment of this exact family, but terminology based on fiber products, truncated coordinate axes, or Artinian Stanley--Reisner algebras could conceal an equivalent statement.

## References
1. R. Díaz, G. Lucchini Arteche, G. Manzano-Flores, *The structure of automorphism groups of zero-dimensional monomial algebras*, arXiv:2609.13741v1 (2026).
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first posted 2024).
3. R. Díaz, G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first posted 2024).
