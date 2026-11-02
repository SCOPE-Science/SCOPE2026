# The sharp dimension-two bound for finite irreducible rational matrix semigroups

## Finding

**Theorem.** Among all finite multiplicative semigroups \(S\subseteq M_2(\mathbb Q)\) having no common nonzero proper invariant rational subspace, the largest possible cardinality is exactly
\[
\boxed{\max |S|=31.}
\]
There is a semigroup attaining the maximum with one zero matrix, twelve invertible matrices, and eighteen rank-one matrices.

The bound improves, in this first nontrivial dimension, the general bound \(3^{n^2}\) proved by Kiefer--Ryzhikov and Steinberg. The exact maximum is not asserted for dimensions greater than two.

## Assumptions and scope

A multiplicative semigroup is a nonempty subset closed under ordinary matrix multiplication; it need not originally contain a zero or an identity. It is **irreducible over** \(\mathbb Q\) when its common invariant rational vector subspaces are precisely \(0\) and \(\mathbb Q^2\). Only finite semigroups are considered. The claimed maximum counts distinct rational matrices, without identifying conjugate semigroups.

For an explicit maximizing example put
\[
\begin{aligned}
U&=\left\{\binom10,\binom01,\binom11\right\},\\
V&=\left\{(1,0),(0,1),(1,-1)\right\},\\
R&=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\quad
F=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
J=-I_2,\\
H&=\langle R,F,J\rangle,\\
T&=\{\varepsilon u v:\ u\in U,\ v\in V,\ \varepsilon\in\{-1,1\}\},\\
S_*&=H\cup T\cup\{0\}.
\end{aligned}
\]
Here a column times a row is a \(2\times2\) rank-one matrix.

## Proof

### 1. Rank and maximal-subgroup preliminaries

Adjoin the zero matrix to an arbitrary \(S\); irreducibility is unchanged, and its size does not decrease. Standard finite-semigroup theory, applied to a finite irreducible rational matrix semigroup with zero, gives a unique nonzero \(0\)-minimal ideal \(I\), which is completely \(0\)-simple and has an idempotent. All nonzero matrices in \(I\) have the same rank. These facts follow, for example, from the results on the minimal ideal in Kiefer--Ryzhikov and Steinberg cited below.

Every invertible element of a finite matrix semigroup belongs to a finite subgroup \(H_S\leq\operatorname{GL}_2(\mathbb Q)\): a positive power of an invertible element is the identity, and its inverse is another positive power. A finite rational subgroup is conjugate over \(\mathbb R\) to a subgroup of \(O(2)\) by averaging a positive-definite form. Its orientation-preserving subgroup consists of rotations and is cyclic. The trace of a finite-order rational matrix is an integer: its rational trace is an algebraic integer. The possible rotational traces in \([-2,2]\) imply rotational orders in \(\{1,2,3,4,6\}\). The rotation subgroup therefore has at most six elements and the full group at most twelve:
\[
|H_S|\leq12.
\]

If the nonzero matrices in \(I\) have rank two, every nonzero matrix of \(S\) is invertible. Indeed, for an invertible \(B\in I\), a nonzero singular \(A\in S\) would give \(0\ne AB\in I\) of rank at most one. Thus in this case \(|S|\leq13\).

It remains to consider the case in which the nonzero matrices of \(I\) have rank one.

### 2. A signed rank-two incidence matrix

Choose a nonzero rank-one idempotent \(e=u_0v_0\in I\), with \(v_0u_0=1\). Since \(I\) is completely \(0\)-simple, each of its \(\mathscr R\)-classes intersects each of its \(\mathscr L\)-classes in a nonempty \(\mathscr H\)-class. Choose a representative \(a_i=u_iv_0\in I\) from the intersection of the \(i\)-th \(\mathscr R\)-class with the \(\mathscr L\)-class of \(e\), and \(b_j=u_0v_j\in I\) from the dual intersections. The indicated factorizations are possible because their row and column directions agree with those of \(e\). Write \(1\leq i\leq a\) and \(1\leq j\leq b\).

Then
\[
a_ib_j=u_iv_j\in I\setminus\{0\},\qquad
b_ja_i=(v_ju_i)e.
\]
The nonzero elements of \(eIe\) form a finite group of rational scalar multiples of \(e\). Because the only finite subgroup of \(\mathbb Q^\times\) is contained in \(\{-1,1\}\), this gives
\[
\boxed{v_ju_i\in\{-1,0,1\}\quad\text{for every }i,j.}
\]
Every \(\mathscr H\)-class contains at most two elements. Since \(I\) is an ideal and \(S\) acts irreducibly, the span of the image lines of \(I\) is all of \(\mathbb Q^2\). Dually, the span of its row lines is the entire dual plane: the annihilator of a proper nonzero right-invariant row space would be a forbidden invariant column space. Hence both families \(\{u_i\}\) and \(\{v_j\}\) span their two-dimensional spaces.

Their projective directions are pairwise distinct within each family. For example, if \(u_i=c u_k\) for different \(\mathscr R\)-classes, choose \(j\) with \(v_ju_k\ne0\). Then \(v_ju_i=c(v_ju_k)\) and both nonzero scalars belong to the group \(eIe\). Thus \(ce\in eIe\) and \(a_i=a_k(ce)\), contradicting the distinction of their \(\mathscr R\)-classes. The dual argument treats the row family.

### 3. The rank-two signed-incidence bound

**Lemma.** Let \(u_1,\ldots,u_a\) be nonproportional nonzero vectors of \(\mathbb Q^2\), and let \(v_1,\ldots,v_b\) be nonproportional nonzero covectors. Suppose each family spans its plane and every pairing \(v_ju_i\) is in \(\{-1,0,1\}\). Then
\[
\boxed{ab\leq9.}
\]

**Proof.** Choose two independent covectors, called \(v_1,v_2\). The evaluation vector \((v_1u_i,v_2u_i)\) is nonzero and lies in \(\{-1,0,1\}^2\), so its projective direction belongs to exactly four possibilities:
\[
(1,0),\quad(0,1),\quad(1,1),\quad(1,-1).
\]
Hence \(a\leq4\). Symmetrically \(b\leq4\). If \(a\leq2\), then \(ab\leq8\).

For \(a=4\), all four patterns occur. An additional covector \(w=\alpha v_1+\beta v_2\) must have \(\alpha,\beta,\alpha+\beta,\alpha-\beta\in\{-1,0,1\}\). This forces \((\alpha,\beta)\) to be one of the four signed coordinate unit vectors; no new projective covector exists. Thus \(b\leq2\).

For \(a=3\), there are only four choices of a three-element subset of those four directions. With the two coordinate directions and one diagonal direction, a covector's allowed projective directions are the two coordinate covectors and the opposite diagonal covector, at most three. With one coordinate direction and both diagonal directions, the only allowed directions are the two coordinate covectors, at most two. Exchanging coordinate axes and signs treats all four cases. Therefore \(b\leq3\) and \(ab\leq9\), as required. \(\square\)

The preceding lemma applies to the normalized families in the minimal ideal, giving \(ab\leq9\).

### 4. No other rank-one directions or scalar multiples

Let \(A\in S\) have rank one. The span of the images of \(I\) is the whole plane, so \(AI\ne\{0\}\); the row-span analogue gives \(IA\ne\{0\}\). Therefore some nonzero \(AB\in I\) has the same image direction as \(A\), and some nonzero \(CA\in I\) has the same row direction. It follows that \(A=\lambda u_iv_j\) for one of the normalized image and row pairs and some \(\lambda\in\mathbb Q^\times\).

Select \(B=\varepsilon u_kv_\ell\in I\) such that \(AB\ne0\), where \(\varepsilon\in\{-1,1\}\). Then
\[
AB=\lambda\varepsilon(v_ju_k)u_iv_\ell\in I\setminus\{0\}.
\]
Here \(v_ju_k\in\{-1,1\}\). The \(\mathscr H\)-class of \(u_iv_\ell\) contains at most its positive and negative, since it is a torsor for the local rational scalar group \(eIe\). Thus \(\lambda\in\{-1,1\}\). Every rank-one member of \(S\) is among the at most \(2ab\leq18\) signed outer products.

Every nonzero \(2\times2\) rational matrix has rank one or two. Combining the zero matrix, at most twelve invertible matrices, and at most eighteen rank-one matrices proves
\[
|S|\leq1+12+18=31.
\]

### 5. An equality example

For the sets \(U,V\) in the assumptions, their pairing matrix, with rows indexed by \(V\) and columns by \(U\), is
\[
P=\begin{pmatrix}1&0&1\\0&1&1\\1&-1&0\end{pmatrix}.
\]
All its entries belong to \(\{-1,0,1\}\). Thus products of signed outer products are again signed outer products or zero. The matrices \(R,F,J\) satisfy \(R^3=F^2=J^2=I_2\), \(FRF=R^{-1}\), and \(J\) is central and independent of \(\langle R,F\rangle\). Hence \(H\) has twelve elements. Left multiplication by \(H\) permutes the signed column vectors of \(U\), while right multiplication permutes the signed row vectors of \(V\); this is checked directly on the three stated generators. Consequently \(S_*=H\cup T\cup\{0\}\) is closed under multiplication.

All nine unsigned outer products in \(T\) are distinct, so \(T\) has eighteen elements. Rank distinguishes them from the twelve elements of \(H\), and zero is distinct from both. The matrices \(E_{11},E_{12},E_{21},E_{22}\) all lie in \(T\); therefore no rational line can be invariant under \(S_*\), since these four matrix units already span the full matrix algebra. Thus \(S_*\) is irreducible and has \(31\) elements. Equality is attained, completing the proof. \(\square\)

## Verification

The standalone `checker.py` works with exact integer matrix multiplication and exact rational arithmetic. It constructs the stated group and signed outer products, confirms the three disjoint cardinalities \(12\), \(18\), and \(1\), and checks each of the \(31^2=961\) ordered products for membership. It also independently enumerates every possible extra row direction in the signed-incidence lemma by prescribing two evaluations in \(\{-1,0,1\}\) and solving a rational \(2\times2\) linear system. Its observed maximum product of projective family sizes is \(9\).

The result of running this exact checker is in `checker_output.txt`. Its bounded finite computations do **not** replace the abstract minimal-ideal argument or the universal group bound. Both of those are proved above with standard cited structural facts.

## Relationship to prior work

Kiefer and Ryzhikov, *The asymptotic size of finite irreducible semigroups of rational matrices* (first public arXiv version January 3, 2026), prove the general upper bound \(3^{n^2}\) and construct large asymptotic examples. Their concluding section expressly identifies determining the maximum finite irreducible semigroup size in each dimension as an interesting further problem. The present theorem determines that maximum when \(n=2\), giving \(31\) rather than the general numerical bound \(81\).

Steinberg, *A short proof of a bound on the size of finite irreducible semigroups of rational matrices* (first public arXiv version January 6, 2026), establishes a shorter proof of the same general bound by using the completely \(0\)-simple minimal ideal. The proof above uses that structural framework but adds the dimension-two projective-incidence estimate and an equality construction, neither of which follows numerically from the general bound.

Bumpus and collaborators studied diameter and finiteness bounds for rational matrix semigroups. No claim of originating the classical Rees theorem or the finite planar-group bound is made here.

## Limitations

The theorem concerns finite rational \(2\times2\) matrix semigroups only. It does not classify all semigroups attaining the maximum up to conjugacy, quantify generator rank or mortality diameter, or give an exact maximum in dimension three or higher. The originality comparison covers the accessible relevant sources identified above and targeted mathematical-record searches, not every historical classification or unpublished note. Independent mathematical validation has not been performed.

## References

1. S. Kiefer and A. Ryzhikov, *The asymptotic size of finite irreducible semigroups of rational matrices*, arXiv:2601.01236v1 (public January 3, 2026); version 2, June 15, 2026. https://arxiv.org/html/2601.01236v2
2. B. Steinberg, *A short proof of a bound on the size of finite irreducible semigroups of rational matrices*, arXiv:2601.03206v1 (public January 6, 2026). https://arxiv.org/html/2601.03206v1
3. G. Bumpus, C. Haase, S. Kiefer, P.-I. Stoienescu and J. Tanner, *On the Size of Finite Rational Matrix Semigroups*, ICALP 2020. https://doi.org/10.4230/LIPIcs.ICALP.2020.115
4. Standard Rees structure theorem for finite completely \(0\)-simple semigroups; see the semigroup background and references in the two 2026 papers above.
