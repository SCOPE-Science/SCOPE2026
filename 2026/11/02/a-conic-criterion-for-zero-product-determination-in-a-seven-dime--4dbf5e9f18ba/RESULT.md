# A conic criterion for zero-product determination in a seven-dimensional two-step Lie algebra

## Finding

For each field \(k\), define a Lie algebra \(L_k\) on the ordered basis
\[
e_0,e_1,e_2,e_3,z_1,z_2,z_3
\]
by declaring the \(z_i\) central and setting
\[
[e_0,e_1]=z_1,\quad [e_0,e_2]=z_2,\quad [e_0,e_3]=z_3,\quad
[e_1,e_2]=-z_3,\quad [e_1,e_3]=z_2,\quad [e_2,e_3]=-z_1.
\]
All unspecified brackets follow from bilinearity and alternation. This is an integral quaternionic-type two-step bracket; it is a Lie bracket in every characteristic, including two. Its commutator and center are both the three-space spanned by the \(z_i\).

A Lie algebra is *zero-product determined* (ZPD) when every bilinear form \(f\) which vanishes on all pairs \((x,y)\) with \([x,y]=0\) has the form \(f(x,y)=\lambda([x,y])\) for a linear functional \(\lambda\) on the derived algebra. Let \(\delta(k)\) be the dimension of the space of such bilinear forms modulo the bracket-factorizing forms.

**Theorem.** Put \(Q(a,b,c)=a^2+b^2+c^2\). Then
\[
\delta(k)=
\begin{cases}
3,&\operatorname{char}(k)\ne2\text{ and }Q\text{ is anisotropic over }k,\\
0,&\operatorname{char}(k)\ne2\text{ and }Q\text{ is isotropic over }k,\\
1,&\operatorname{char}(k)=2.
\end{cases}
\]
Consequently \(L_k\) is ZPD if and only if the characteristic is not two and the ternary form \(Q\) has a nonzero \(k\)-rational zero. In particular it is not ZPD over \(\mathbb R\) or \(\mathbb Q\), is ZPD over \(\mathbb C\) and every finite field of odd cardinality, and is not ZPD over any field of characteristic two.

The scheme of two-dimensional linear subspaces \(P\subset L_k/Z(L_k)\) satisfying \([P,P]=0\) is the plane conic
\[
\mathcal C_k:\quad a^2+b^2+c^2=0\quad\text{in }\mathbb P^2_k.
\]
For odd characteristic it is geometrically smooth; for characteristic two it is the **nonreduced double line** defined by \((a+b+c)^2=0\), with underlying reduced line \(a+b+c=0\). For every finite field \(\mathbb F_q\) the conic has exactly \(q+1\) rational points (counting rational points of the scheme, not their multiplicities).

For every finite field \(\mathbb F_q\), the exact number of ordered commuting pairs in the seven-dimensional Lie algebra is
\[
\boxed{\#\{(x,y)\in L_{\mathbb F_q}^{\,2}:[x,y]=0\}=2q^{11}+q^{10}-2q^9.}
\]
Equivalently, the commuting probability is \(2q^{-3}+q^{-4}-2q^{-5}\). The finite-field point count does not distinguish odd from even characteristic, but the ZPD defect does: it is respectively zero and one.

## Assumptions and scope

The field \(k\) is arbitrary; it need not be finite, perfect, algebraically closed or of characteristic different from two. The bracket is alternating, so in characteristic two the negatives in its structure constants coincide with positives. All zero-product statements concern **scalar-valued bilinear maps** on the specified seven-dimensional Lie algebra and their quotient by maps factoring through its derived bracket. All geometric statements refer to the explicitly defined scheme of commuting two-planes in the four-dimensional quotient \(L_k/Z(L_k)\); no assertion of reducedness of the full commuting-pair scheme is made. The arithmetic formula concerns ordered pairs of Lie-algebra elements, not subalgebras or representations.

## Proof

**1. Kernel of the bracket.** Set \(V=\langle e_0,e_1,e_2,e_3\rangle_k\) and \(W=\langle z_1,z_2,z_3\rangle_k\). Centrality gives the Jacobi identity, and direct inspection shows \(Z(L_k)=[L_k,L_k]=W\). With Plücker-coordinate order \((01,02,03,12,13,23)\), the bracket map \(b:\bigwedge^2V\to W\) is
\[
b(p_{01},p_{02},p_{03},p_{12},p_{13},p_{23})
=(p_{01}-p_{23},\ p_{02}+p_{13},\ p_{03}-p_{12}).
\]
It is surjective and its three-dimensional kernel is
\[
K=\{(a,b,c,c,-b,a):a,b,c\in k\}.
\]

**2. Commuting decomposable wedges.** Over every field, the Plücker embedding of \(\operatorname{Gr}(2,V)\) into \(\mathbb P(\bigwedge^2 V)\cong\mathbb P^5\) is cut out by the Pfaffian relation
\[
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0.
\]
(The relation remains valid in characteristic two, where the signs coincide.) Restriction to \(K\) gives precisely
\[
a^2+b^2+c^2=0.
\]
Thus the scheme of commuting two-planes is \(\mathbb P(K)\cap\operatorname{Gr}(2,V)=\mathcal C_k\), including its possibly nonreduced structure.

**3. Bilinear forms and defect.** Suppose \(f:L_k\times L_k\to k\) is bilinear and vanishes when the bracket vanishes. Every vector commutes with itself, so \(f(x,x)=0\); polarization forces \(f\) to be alternating even in characteristic two. Every central element commutes with every element, so \(f(W,L_k)=f(L_k,W)=0\). Therefore \(f\) corresponds uniquely to a linear functional on \(\bigwedge^2V\). Its vanishing on commuting pairs is equivalent to annihilating
\[
H_k=\operatorname{span}_k\{\eta\in K:\eta\text{ is a decomposable bivector}\}.
\]
Here all decomposable bivectors with zero bracket lie in \(K\), so the equivalence has no extra hypotheses. As \(b\) is surjective, the subspace of bilinear forms factoring through \(b\) is the three-dimensional annihilator of \(K\). By elementary duality,
\[
\dim\{f\text{ vanishing on commuting pairs}\}=6-\dim H_k,\qquad
\boxed{\delta(k)=3-\dim H_k.}
\]
The form \(Q\) identifies the nonzero decomposable vectors in \(K\) exactly with its nonzero isotropic vectors. This is the explicit specialization of the established general ZPD kernel-spanning criterion; the criterion itself is not claimed as new.

**4. Span of isotropic vectors.** If \(\operatorname{char}(k)\ne2\), the form \(Q\) is nondegenerate. If it is anisotropic, its only zero is the zero vector, so \(H_k=0\). Otherwise let \(e\ne0\) be isotropic. Nondegeneracy provides a second isotropic vector \(f\) with nonzero polar pairing with \(e\); scale so \(Q(se+rf)=sr\), and take a nonzero vector \(t\) perpendicular to this hyperbolic plane. Writing \(Q(t)=d\), the three vectors \(e\), \(f\), and \(e-df+t\) are isotropic and span \(K\). Hence \(H_k=K\) in the isotropic case. This proves the first two cases without assuming algebraic closure or that every element has a square root.

If \(\operatorname{char}(k)=2\), then \(Q(a,b,c)=(a+b+c)^2\). Because \(k\) is a field, its zero vectors form the two-dimensional plane \(a+b+c=0\). Therefore \(\dim H_k=2\), giving \(\delta(k)=1\). The gradient of the homogeneous quadratic \(Q\) is \((2a,2b,2c)\); hence the projective conic is smooth in odd characteristic. The displayed square shows directly why the characteristic-two scheme is a double line.

**5. Arithmetic of commuting pairs.** Over an odd finite field, the three-variable quadratic \(Q\) has a nonzero zero: for example, Chevalley–Warning implies that its number of affine zeros is divisible by the characteristic, which is impossible if only the origin vanishes. Its smooth projective conic therefore has a rational point, is isomorphic to \(\mathbb P^1\) over the field, and has exactly \(q+1\) rational points. In even characteristic its underlying line also has exactly \(q+1\) points.

Count commuting pairs in \(V^2\). Pairs of linearly dependent vectors number \(q^4+(q^4-1)q=q^5+q^4-q\): first take the first vector zero and arbitrary second vector, then take first vector nonzero and a scalar multiple as the second. Each commuting independent pair determines a unique commuting two-plane, and each such plane has \(|\mathrm{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\) ordered bases. Thus their number is
\[
(q+1)(q^2-1)(q^2-q).
\]
Adding these two disjoint contributions and simplifying yields \(2q^5+q^4-2q^3\) commuting pairs in \(V^2\). An arbitrary pair of central coordinates may be added without changing brackets, giving a multiplicative factor \(q^6\). Therefore the count in \(L_k^2\) is \(2q^{11}+q^{10}-2q^9\), as claimed.

## Verification

The supplied standard-library checker `verify.py` constructs the original six structure-constant brackets independently, verifies the three-dimensional bracket kernel and restricted Pfaffian identity, and performs exact finite-field linear algebra. It exhaustively checks all ordered pairs in the four-dimensional quotient for \(q\in\{2,3,4,5\}\), enumerates all two-planes over fields of orders \(2,3,4,5,7\), and compares the span of quadratic isotropic vectors with the predicted defect. The order-four field uses explicit irreducible-polynomial extension arithmetic, not arithmetic modulo four. Five field configurations pass and the recorded output ends with `QUATERNIONIC7_ZPD_CONIC_AND_COMMUTING_CENSUS_OK 5_FIELDS`. These finite tests only corroborate the general proof; they do not prove an arbitrary-field assertion.

## Relationship to prior work

Brešar, Guo, Liu, Lu and Zhao (2016, arXiv:1610.07178) introduced the decisive criterion that the kernel of the bracket on the exterior square must be spanned by commuting decomposable wedges (Lemma 2.3); that criterion is used, not reasserted as original. Their Proposition 5.1 establishes ZPD for **ordinary Heisenberg algebras with one-dimensional derived center**, whereas the present algebra has a three-dimensional derived center, and its ZPD behavior depends on the field.

Rostami, Parvizi and Niroomand (2018, arXiv:1805.05806) and Rai (2023, arXiv:2301.01963) treat the related cohomological Bogomolov multiplier of Lie algebras, using a **nonabelian exterior product** and commutativity-preserving central extensions. Their inspected definitions, low-dimensional classifications, and explicit generalized Heisenberg applications do not state this field-sensitive three-case defect and simultaneous commuting-pair census for the specified seven-dimensional bracket. The existence of a broader result elsewhere remains possible; neither keyword absence nor an inaccessible source would prove publication priority.

## Limitations

The result is for the displayed seven-dimensional structure constants, not for every generalized or quaternionic Heisenberg algebra and not for all forms of a given Lie algebra. The characteristic-two conclusion concerns the specialization of the displayed integral bracket, not a claim about quaternion division algebras in characteristic two. The geometric scheme refers to commuting two-planes in the four-dimensional quotient; the projective scheme is nonreduced in characteristic two. It does not classify arbitrary commuting-subalgebra schemes, their infinitesimal deformations, or conjugacy classes. The originality assessment is best-knowledge and requires independent historical review; independent mathematical audit has not occurred.

## References

1. M. Brešar, X. Guo, G. Liu, R. Lu and K. Zhao, “Zero product determined Lie algebras,” arXiv:1610.07178, first publicly posted 2016-10-23, especially Lemma 2.3 and Proposition 5.1. https://arxiv.org/abs/1610.07178
2. Z. A. Rostami, M. Parvizi and P. Niroomand, “The Bogomolov multiplier of Lie algebras,” arXiv:1805.05806, first posted 2018-05-15. https://arxiv.org/abs/1805.05806
3. P. K. Rai, “Bogomolov Multiplier of Lie algebras,” arXiv:2301.01963, first posted 2023-01-05, especially Theorems 1.5, 3.2 and Corollary 3.3. https://arxiv.org/abs/2301.01963
