# Rank spectra of algebra retractions of cubic coordinate-cross rings

## Finding
For a field \(k\) and integer \(n\ge 2\), define the finite-dimensional local, commutative unital algebra
\[
A_{n,3}(k)=k[x_1,\ldots,x_n]/(x_ix_j\ (i\ne j),\ x_1^3,\ldots,x_n^3).
\]
A *retraction* means a **unital** \(k\)-algebra endomorphism \(F:A_{n,3}\to A_{n,3}\) satisfying \(F^2=F\) under composition. The algebra has vector-space basis \(1,x_1,\ldots,x_n,x_1^2,\ldots,x_n^2\). Every retraction is characterized by two coefficient matrices \(P,Q\in M_n(k)\):
\[
F(x_i)=\sum_{j=1}^{n}P_{ji}x_j+\sum_{j=1}^{n}Q_{ji}x_j^2.
\]
The conditions are precisely: (a) each row of \(P\) contains at most one nonzero entry; (b) \(P^2=P\); and (c)
\[
Q=QP+P^{[2]}Q,\qquad P^{[2]}=(P_{ji}^2)_{j,i}.
\]
If \(r=\operatorname{rank}P\), its image is a copy of \(A_{r,3}\), taking \(A_{0,3}=k\), and \(\operatorname{rank}_kF=1+2r\). Thus there are exactly \(n+1\) possible image-isomorphism types (or algebra ranks).

For every finite field \(\mathbb F_q\), of **any characteristic**, the complete number of *labeled* retractions by \(k\)-linear rank is
\[
\boxed{\mathcal R_{n,q}(T)=\sum_{r=0}^{n}\binom nr\bigl(1+r(q-1)\bigr)^{n-r}q^{2r(n-r)}T^{1+2r}.}
\]
In particular, \(\mathcal R_{2,3}(T)=T+54T^3+T^5\) and \(\mathcal R_{3,2}(T)=T+192T^3+144T^5+T^7\). The polynomial counts maps, not their conjugacy classes or distinct image subalgebras.

## Assumptions and scope
The ground field is arbitrary for the structural theorem. Each homomorphism fixes \(k\) pointwise and sends \(1\) to \(1\); nonunital linear/algebra maps are excluded. There are no restrictions on the characteristic; no nondegeneracy or separability hypotheses enter. The finite-field enumerator requires \(q\) to be a prime power. The stated \(n\ge2\) avoids a vacuous cross-relation; the same formulas work for \(n=1\). The algebra is the cubic truncation of the union of the coordinate axes, equivalently the fiber product of \(n\) copies of \(k[t]/(t^3)\) over their common residue field.

## Proof
Write \(\mathfrak m=(x_1,\ldots,x_n)\), \(V=\mathfrak m/\mathfrak m^2\), \(W=\mathfrak m^2\). The only nonzero products between basis vectors of \(V\) are \(x_i x_i=x_i^2\), and \(\mathfrak m^3=0\). Since \(A_{n,3}\) is local with residue field \(k\), a unital \(k\)-algebra endomorphism maps every \(x_i\) into \(\mathfrak m\). Hence it has the unique displayed pair \((P,Q)\). Substituting generator images into \(x_ix_j=0\) for \(i\ne j\) gives
\[
0=F(x_i)F(x_j)=\sum_{h=1}^n P_{hi}P_{hj}x_h^2.
\]
As the squares form a basis of \(W\), this holds exactly when no row of \(P\) has nonzero entries in two distinct columns. The relations \(x_i^3=0\) are automatic because \(\mathfrak m^3=0\). Thus row sparsity is necessary and sufficient for the map to be a homomorphism.

The induced operator on \(V\) is \(P\), and the induced operator on \(W\) is \(R=P^{[2]}\): indeed, \(F(x_i^2)=\sum_jP_{ji}^2x_j^2\). In the ordered direct sum \(k\oplus V\oplus W\), the map has matrix
\[
F=\begin{pmatrix}1&0&0\\0&P&0\\0&Q&R\end{pmatrix}.
\]
Squaring proves equivalence to \(P^2=P\), \(R^2=R\), and \(Q=QP+RQ\). The middle condition follows automatically from the row sparsity and \(P^2=P\), as shown next.

A row-sparse idempotent \(P\) admits a canonical description. If its row \(j\) is nonzero, write it as \(a_j e_{s(j)}^\top\), \(a_j\ne0\). The \(j\)-th row of \(P^2=P\) then reads \(a_j\cdot(\text{row }s(j))=a_je_{s(j)}^\top\), forcing the row at the *root* \(s(j)\) to equal \(e_{s(j)}^\top\). Let \(S\) be the set of these root indices. Each \(s\in S\) has precisely the row \(e_s^\top\); each \(j\notin S\) has either a zero row or one row \(a_j e_s^\top\) for a uniquely chosen \(s\in S\), with \(a_j\in k^\times\). Conversely every matrix of this form is row-sparse and idempotent. Its rank is \(r=|S|\), since columns indexed outside \(S\) vanish and the submatrix on \(S\times S\) is the identity. Its entrywise square \(R=P^{[2]}\) has exactly the same root arrangement, with the nonzero scalar \(a_j\) replaced by \(a_j^2\); in particular \(R^2=R\) and \(\operatorname{rank}R=r\) over any field.

For a fixed \(P\), decompose the domain \(V=V_1\oplus V_0\) into image and kernel of \(P\), with dimensions \(r\) and \(n-r\). Similarly \(W=W_1\oplus W_0\) is the image-plus-kernel decomposition for the projection \(R\), of dimensions \(r\) and \(n-r\). Relative to these splittings, write \(Q\) in four blocks. The equation \(Q=QP+RQ\) forces its \(V_1\to W_1\) block to vanish (that block equals twice itself), and its \(V_0\to W_0\) block to vanish. The \(V_1\to W_0\) and \(V_0\to W_1\) blocks are unrestricted. This uses only subtraction in the additive group of \(k\), and remains valid in characteristic \(2\). Therefore the space of admissible \(Q\) is affine-linear of dimension
\[
\dim_k\{Q:Q=QP+RQ\}=r(n-r)+(n-r)r=2r(n-r).
\]
Over \(\mathbb F_q\), exactly \(q^{2r(n-r)}\) choices exist for each \(P\).

Select the root set \(S\) in \(\binom nr\) ways. Each of the other \(n-r\) rows of \(P\) has exactly \(1+r(q-1)\) choices (zero or a nonzero multiple of one of the \(r\) root rows). These choices are independent. Multiplying by the count of compatible \(Q\) gives the coefficient of \(T^{1+2r}\) in the asserted polynomial.

Finally, the images \(F(x_s)\) for \(s\in S\) have linearly independent leading classes in \(V\), their squares have linearly independent classes in \(W\), and pairwise products for distinct root indices are zero. Hence the unital subalgebra generated by them has a basis consisting of \(1\), the \(r\) image generators, and their \(r\) squares; it is isomorphic to \(A_{r,3}\). Any other generator image belongs to this subalgebra: if \(F^2=F\), the whole image is a retract, and the induced map has rank \(1+\operatorname{rank}P+\operatorname{rank}R=1+2r\) (for example, from the image/kernel block decomposition above), already equal to the dimension of this generated subalgebra. This proves the image identification and rank formula.

## Verification
Running `python3 checker.py` directly in the package directory prints `VERIFY_OK`. It independently enumerates every admissible generator-image tuple over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\) in the tested low ranks and checks multiplicativity on generating relations, composition-idempotence, and operator rank. It then compares the complete observed distribution with the formula. Exhaustive cases are \((n,q)=(1,2),(2,2),(2,3),(2,4),(3,2)\). In particular the last case has \(1,192,144,1\) retractions at ranks \(1,3,5,7\). These finite tests corroborate, but do not replace, the arbitrary-field proof. The checker uses only the Python standard library and a direct finite-field implementation for \(\mathbb F_4\).

## Relationship to prior work
Díaz, Liendo, Manzano-Flores and Regeta investigate **automorphism groups** of general finite-dimensional monomial algebras over characteristic-zero fields (arXiv:2408.02197, first publicly available 5 August 2024, primary MSC 13F55). Their invertibility requirement excludes the noninvertible retractions counted here; in particular a formula for the automorphism group does not determine the coefficients of \(\mathcal R_{n,q}\). The recent published classification *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* gives the automorphism normal form and finite-field group order for **exactly this algebra**. Its statement concerns bijective maps, whereas our claim classifies and counts all **composition-idempotent** unital endomorphisms, including augmentation and intermediate-rank maps.

Epstein and Nguyen classify graded algebra retracts of Stanley–Reisner rings, with additional results for certain monomial quotients (arXiv:1301.3967). Their structural graded description does not enumerate all nongraded retractions of the cubically truncated coordinate-cross algebra. Berkesch and collaborators (arXiv:2112.00266) study differential operators and canonical retracts of toric face rings; the setting and invariant differ from the rank distribution of nonhomogeneous endomorphisms here. All of these papers are treated as prior conceptual coverage rather than novelty-free territory.

## Limitations
This theorem counts labeled *maps* of a fixed algebra, not conjugacy classes under automorphisms, distinct retract image subalgebras, or nonunital maps. It concerns cubic branch length \(3\); a general formula for longer truncations would require additional higher-order compatibility equations. A bibliographic risk remains that the same enumerator is known under the names *fiber-product retractions* or *finite monomial-algebra endomorphism monoids*; lack of a search hit cannot certify global novelty. No independent external audit of the proof has been performed.

## References
1. R. Díaz, Á. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (v1 first posted 2024-08-05; subsequent versions inspected), https://arxiv.org/abs/2408.02197.
2. N. Epstein and H. D. Nguyen, *Algebra retracts and Stanley–Reisner rings*, arXiv:1301.3967, https://arxiv.org/abs/1301.3967.
3. C. Berkesch et al., *Differential operators, retracts, and toric face rings*, arXiv:2112.00266, https://arxiv.org/abs/2112.00266.
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb.
