# Primitive Frobenius line-orbit trace lattices on cubic surfaces

## Finding

Let \(S/\mathbb F_q\) be **any smooth cubic surface** over a finite field and write \(P=\operatorname{Pic}(S_{\overline{\mathbb F}_q})\). Frobenius acts on the twenty-seven geometric lines and their Picard classes through \(W(E_6)\). Define the **line-orbit trace subgroup** \(T(S)\subseteq P^F\) to be generated over the integers by the sums of line classes over each Frobenius orbit. Then \(P^F/T(S)\) is finite and

\[
P^F/T(S)\cong
\begin{cases}
\mathbb Z/3\mathbb Z,&\text{for precisely three Weyl conjugacy types},\\
0,&\text{for the other twenty-two types}.
\end{cases}
\]

The exceptional triples (Frobenius order, arithmetic Picard rank, decomposition of the twenty-seven lines) are

\[
(3,3,3^9),\qquad(6,2,3^1 6^4),\qquad(9,1,9^3).
\]

Their respective Weyl conjugacy-class sizes are \(480\), \(4320\), and \(5760\). In the order-nine case \(P^F=\mathbb ZH\) for the primitive anticanonical hyperplane class \(H\), and **each** of the three line-orbit sums equals \(3H\). Thus even an effective primitive rational divisor class need not lie in the integral span of orbit traces of the geometric lines. The theorem is a classification conditional on Frobenius conjugacy type, not a claim that every type occurs over every field.

## Assumptions and scope

A smooth cubic surface over an algebraic closure is the blow-up of six points of \(\mathbb P^2\) in general position. Choose the integral basis \(h,e_1,\ldots,e_6\) with intersection pairing \(h^2=1\), \(e_i^2=-1\), all other basis intersections zero. The canonical class is \(K=-3h+e_1+\cdots+e_6\), and \(H=-K\). The geometric exceptional-line classes are precisely

\[
\{e_i:1\le i\le6\}\ \cup\
\{h-e_i-e_j:1\le i<j\le6\}\ \cup\
\{2h-\sum_{j\ne i}e_j:1\le i\le6\}.
\]

The group \(W(E_6)\), of order \(51840\), acts faithfully on these lines. Its six chosen simple-root reflections have roots \(e_i-e_{i+1}\) for \(1\le i\le5\) and \(h-e_1-e_2-e_3\). The reflection in a root of square \(-2\) is \(v\mapsto v+(v\cdot r)r\).

Frobenius invariants are genuinely arithmetic Picard classes: the finite-field Brauer group vanishes, and the Hochschild–Serre sequence gives \(\operatorname{Pic}(S)=P^F\). The subgroup \(T(S)\) is defined using **integral line-orbit sums**, not rational span. Over \(\mathbb Q\), these traces span \(P^F\otimes\mathbb Q\), so the quotient is always finite.

## Proof

**1. Faithful finite presentation.** Associate to each simple-root reflection its permutation of the twenty-seven listed line classes. Closing under composition gives exactly \(51840\) distinct permutations. The same six generators, acting by conjugation, partition these elements into exactly \(25\) conjugacy classes. Since the resulting faithful action has the known order of \(W(E_6)\), it exhausts the Weyl group rather than a subgroup or a random sample. A conjugate Frobenius action gives an isomorphic invariant lattice and trace subgroup.

**2. Integral saturation index.** For any representative permutation \(w\), decompose its twenty-seven line indices into cycles \(O_1,\ldots,O_m\). Make the integral \(7\times m\) matrix \(A_w\) whose columns are \(t_j=\sum_{\ell\in O_j}[\ell]\), expressed in the indicated blow-up basis. Its columns span \(P^w\otimes\mathbb Q\) since the line classes generate \(P\) integrally: averaging a rational lift of an invariant divisor shows every invariant rational divisor is a rational combination of these orbit sums. Put \(r=\operatorname{rank}_{\mathbb Q}A_w\). The integral fixed module \(P^w=\ker(w-I:\mathbb Z^7\to\mathbb Z^7)\) is saturated in \(P\). Therefore its lattice index is exactly

\[
[P^w:T(S)]=\gcd\{|\det((A_w)_{I,J})|:\ |I|=|J|=r\},
\]

where the gcd ranges over all square minors of maximal rank; equivalently it is the product of the \(r\) nonzero Smith invariant factors of \(A_w\). This formulation does **not** infer integral generation from rational rank.

**3. Exhaustive conjugacy-class calculation.** Applying the preceding exact integer formula to all \(25\) classes gives the full reproducible classification below. The orbit column records `cycle length: number of cycles` (its weighted sum is always twenty-seven). The final column is \([P^w:T]\).

| Frobenius order | Weyl class size | Rank \(P^w\) | Line orbit lengths and counts | Trace index |
|---:|---:|---:|---|---:|
| 3 | 80 | 1 | 3: 9 | 1 |
| 6 | 720 | 1 | 3: 1, 6: 4 | 1 |
| 6 | 1440 | 1 | 3: 1, 6: 4 | 1 |
| 9 | 5760 | 1 | 9: 3 | 3 |
| 12 | 4320 | 1 | 3: 1, 12: 2 | 1 |
| 4 | 540 | 2 | 1: 1, 2: 3, 4: 5 | 1 |
| 6 | 1440 | 2 | 3: 5, 6: 2 | 1 |
| 6 | 4320 | 2 | 3: 1, 6: 4 | 3 |
| 8 | 6480 | 2 | 1: 1, 2: 1, 8: 3 | 1 |
| 10 | 5184 | 2 | 2: 1, 5: 3, 10: 1 | 1 |
| 12 | 4320 | 2 | 1: 1, 4: 2, 6: 1, 12: 1 | 1 |
| 2 | 45 | 3 | 1: 3, 2: 12 | 1 |
| 3 | 480 | 3 | 3: 9 | 3 |
| 4 | 540 | 3 | 1: 3, 4: 6 | 1 |
| 4 | 3240 | 3 | 1: 1, 2: 3, 4: 5 | 1 |
| 5 | 5184 | 3 | 1: 2, 5: 5 | 1 |
| 6 | 1440 | 3 | 1: 3, 2: 3, 6: 3 | 1 |
| 6 | 2160 | 3 | 1: 1, 2: 4, 3: 2, 6: 2 | 1 |
| 2 | 540 | 4 | 1: 3, 2: 12 | 1 |
| 4 | 1620 | 4 | 1: 5, 2: 1, 4: 5 | 1 |
| 6 | 1440 | 4 | 1: 3, 2: 3, 3: 4, 6: 1 | 1 |
| 2 | 270 | 5 | 1: 7, 2: 10 | 1 |
| 3 | 240 | 5 | 1: 9, 3: 6 | 1 |
| 2 | 36 | 6 | 1: 15, 2: 6 | 1 |
| 1 | 1 | 7 | 1: 27 | 1 |

The classification comprises \(22\) classes of trace index one and the three specified classes of trace index three. Their Weyl class sizes add up to \(51840\). The sum of the sizes of the three exceptional classes is \(10560\), while the other \(41280\) elements have index one. The nonzero Smith invariant factors in exceptional types are \((1,1,3)\), \((1,3)\), and \((3)\), respectively; thus each exceptional quotient is cyclic, not a rank-two elementary abelian three-group.

**4. Direct checks in the three exceptional types.** For the order-three representative permuting two triples of exceptional curves, the fixed lattice is generated by \(h\), \(e_1+e_2+e_3\), \(e_4+e_5+e_6\). Its trace subgroup is generated by the same two triple sums together with \(3h\), giving index three. For the order-six representative cyclically permuting all six exceptional curves, the fixed lattice is generated by \(h\), \(e_1+\cdots+e_6\); the trace subgroup is generated by \(3h\) and \(e_1+\cdots+e_6\). Finally, the order-nine representative has fixed Picard lattice of rank one generated by \(H=3h-e_1-\cdots-e_6\), and each of its three nine-line orbit traces is \(3H\). These explicit witnesses agree with the complete calculation and show that the nontrivial index is not a numerical artifact.

## Verification

The bundled `VERIFY_W_E6.py` reconstructs all \(51840\) distinct permutations from the six explicit root reflections and determines all \(25\) conjugacy classes by generator conjugation. For each class it calculates an integer Smith normal form of the orbit-trace matrix; separately it takes a column Hermite form and the gcd of all its maximal rank minors, giving an independent exact-integer test of the same index. It verifies the Picard rank by an explicit \(7\times7\) integral matrix, checks preservation of the intersection pairing, verifies all six generators preserve the twenty-seven lines, and confirms that the three order-nine traces are \(3H\).

Run from the directory containing `VERIFY_W_E6.py` with Python 3 and SymPy version \(1.14.0\): `python VERIFY_W_E6.py`. Successful output is `VERIFY_OK: 51840 Weyl elements; 25 conjugacy classes; index 3 for exactly orders/ranks (3,3), (6,2), (9,1); independent Hermite-minor check`.

This is an exhaustive finite computation over an explicitly proved complete finite Weyl group; it is not an inference from finite sampling of cubic surfaces. The mathematical reduction from a surface over an arbitrary finite field to its Weyl conjugacy type is furnished by the standard Picard and line theory.

## Relationship to prior work

The geometric identification of exceptional curves and the \(W(E_6)\)-action is classical. Elsenhans and Jahnel discuss the Galois action on the twenty-seven lines. Banwait, Fité and Loughran give a comprehensive table of all twenty-five finite-field Frobenius types, Picard ranks and line orbits, and study a **different** index: the largest Galois-invariant collection of pairwise skew lines. Their table does not display the index of the subgroup of the integral invariant Picard lattice generated by the **sums** over entire line orbits. Their Weyl classification is a substantial prior input, not part of the novelty claim. Swinnerton-Dyer treats the Brauer group and \(H^1(G,P)\), which is not the same functor as the current trace quotient; if \(R\) is the relation lattice in the exact sequence \(0\to R\to\mathbb Z^{27}\to P\to0\), the new quotient is the image/cokernel measured by the next connecting homomorphism, a subobject of \(H^1(G,R)\), not directly \(H^1(G,P)\).

The precise **integral orbit-trace saturation** across all conjugacy classes, including the three nontrivial quotient types and order-nine example, is the limited contribution here. It is a finite refinement obtainable in principle from classical Weyl data, and an equivalent calculation might exist under cohomological or lattice-theoretic terminology.

## Limitations

No classification of the existence of all conjugacy types over each particular \(\mathbb F_q\) is asserted. The result gives rational line-trace cone generators only incidentally and does not classify effective semigroups or rational point counts. Historical priority cannot be certified by a finite literature search; an equivalent older calculation under the name of a relation-lattice cohomology group or an integral norm map remains possible. The supplied integer computation verifies only the explicitly formulated finite Weyl claim and relies on the standard classification of cubic surfaces for its geometric interpretation.

## References

1. A.-S. Elsenhans and J. Jahnel, *The discriminant of a cubic surface*, arXiv:1006.0721 (first posted 2010-06-03), https://arxiv.org/abs/1006.0721.
2. B. Banwait, F. Fité and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300 (first posted 2016-06-01), https://arxiv.org/abs/1606.00300.
3. H. P. F. Swinnerton-Dyer, *The Brauer group of cubic surfaces*, Mathematical Proceedings of the Cambridge Philosophical Society (1993), DOI 10.1017/S0305004100076106, https://doi.org/10.1017/S0305004100076106.
4. A. Elsenhans and J. Jahnel, primary cubic-surface Galois information as in [1]; see also O. Debarre, A. Laface and X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, arXiv:1510.05803 (2015), https://arxiv.org/abs/1510.05803.
