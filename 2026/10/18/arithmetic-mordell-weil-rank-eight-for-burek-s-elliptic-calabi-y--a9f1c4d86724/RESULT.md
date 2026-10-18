# Arithmetic Mordell–Weil rank eight for Burek's elliptic Calabi–Yau threefold

## Finding

Let \(K=\mathbb Q(v,t)\) and let \(E/K\) be the elliptic curve
\[
 y^2=x^3-27\cdot481 A(v)t^4x+2916\bigl(30^4t^{10}+B(v)^4t^2\bigr)-54\cdot4879 C(v)t^6,
\]
where
\[
 A(z)=z^8+14z^4+1,\quad B(z)=z(z^4-1),\quad C(z)=z^{12}-33z^8-33z^4+1.
\]
Then
\[
 \boxed{\operatorname{rank}E(\mathbb Q(v,t))=8,\qquad
 \operatorname{rank}E(\mathbb Q(i)(v,t))=12.}
\]
More precisely, complex conjugation on the rational Mordell–Weil vector space over \(\mathbb Q(i)(v,t)\) has \(+1\)-eigenspace dimension \(8\) and \(-1\)-eigenspace dimension \(4\). In this field, the Mordell–Weil groups have no torsion (as follows from the geometric torsion-freeness established in [1]).

## Assumptions and scope

All fields have characteristic zero. The parameters \(v,t\) are algebraically independent. The elliptic curve and the twelve sections \(P_1,\ldots,P_6,P'_1,\ldots,P'_6\) are exactly the Weierstrass model (1.5) and sections (A.2)--(A.6) of [1], respectively. The coefficients of these twelve points lie in \(\mathbb Q(i)[v,t]\). The conjugation \(\sigma\) fixes \(v,t\) and sends \(i\) to \(-i\).

The rank over \(\mathbb C(v,t)\) is \(12\) by [1, Theorem 1.1 and Proposition 5.6]. This is an input, not a result reproved here. The statement concerns rational sections over the specified function fields, not the existence of a rational model for every geometric birational modification and not a classification of all section generators.

## Proof

**Step 1: produce fixed and anti-fixed sections.** For each \(j=1,\ldots,12\), let \(P_j\) denote the ordered published sections (with the primed ones relabelled \(7,\ldots,12\)). Set
\[
 Q_j=P_j+\sigma P_j,\qquad R_j=P_j-\sigma P_j.
\]
The group law has rational coefficients over \(K\). Consequently \(\sigma(Q_j)=Q_j\), so \(Q_j\in E(K)\), while \(\sigma(R_j)=-R_j\).

**Step 2: specialize at \(v=5\) and compute heights.** The specialization is an elliptic K3 surface over \(\mathbb Q(i)(t)\) with two split type-IV fibres at \(t=0\) and \(t=\infty\) and sixteen nodal fibres [1, Lemma 5.5 and Appendix A.3]. The specialization has good generic reduction at \(v=5\), so an integral relation among generic sections induces the same relation among specialized sections [1, Proposition 5.6].

For the twelve specialized points, write
\[
 H_{ij}=\langle P_i,P_j\rangle,\qquad G_{ij}=\langle P_i,\sigma P_j\rangle.
\]
Their canonical height pairing is taken on this elliptic K3 surface. The matrix \(H\) is precisely the published \(12\)-by-\(12\) matrix [1, (A.10)--(A.11)] and has determinant \(4096/9\). The new cross-pairing \(G\) is symmetric and is recorded in full as the integer matrix \(3G\) in `verification/cross_pairing.json`.

Here are the exact rules used to obtain \(G\), included to make the computational step checkable. The twelve source points and their conjugates have no intersection with the zero section. For two *distinct* such points \(S,T\), the height formula is
\[
 \langle S,T\rangle = 2-S\cdot T-\operatorname{contr}_0(S,T)-\operatorname{contr}_\infty(S,T).
\]
At \(0\) all the points and their conjugates meet the same nonidentity component and contribute \(2/3\). At infinity the unprimed points and their conjugates meet one nonidentity component, and the primed points and their conjugates meet the other; the local pairing is \(2/3\) for the same component and \(1/3\) across components. The intersection multiplicity away from \(0,\infty\) is the degree of the polynomial \(\gcd(x_S-x_T,y_S-y_T)\), after removal of its factor at \(t=0\). At \(0\) there is the additional multiplicity \(\max(0,\operatorname{ord}_0(x_S-x_T)-1)\); at infinity, after substituting \(r=1/t\) and \(x_\infty=r^4x\), the analogous expression applies if and only if the components agree. These are the local resolution and intersection rules in [1, Appendix A.3]. Exact polynomial arithmetic in \(\mathbb Q(i)[t]\) determines every entry of \(G\). The script independently recovers \(H\) *exactly* from the same rules and checks agreement with [1].

**Step 3: obtain independent fixed and anti-fixed points.** Because conjugation preserves the height pairing,
\[
 \langle Q_i,Q_j\rangle=2(H+G)_{ij},\qquad
 \langle R_i,R_j\rangle=2(H-G)_{ij}.
\]
Consider the principal matrices on the following sets of indices:
\[
 I_+=\{1,2,4,6,7,8,11,12\},\qquad I_-=\{1,4,9,10\}.
\]
Exact determinant calculation gives
\[
 \boxed{\det\bigl(2(H+G)_{I_+,I_+}\bigr)=\frac{16777216}{9}\ne0,\qquad
 \det\bigl(2(H-G)_{I_-,I_-}\bigr)=256\ne0.}
\]
Thus the eight trace sections \(Q_j\), \(j\in I_+\), are independent over \(\mathbb Q(v,t)\), and the four anti-trace sections \(R_j\), \(j\in I_-\), are independent over \(\mathbb Q(i)(v,t)\). Here independence of specialized points implies independence of the generic points: a generic integral relation would specialize to an integral relation, contradicting the nondegenerate height matrices.

**Step 4: apply the geometric upper bound.** Let \(V=E(\mathbb Q(i)(v,t))\otimes_{\mathbb Z}\mathbb Q\). By [1], \(\dim_{\mathbb Q}V\le12\). The trace sections give an eight-dimensional \(+1\)-subspace; the anti-trace sections give a four-dimensional \(-1\)-subspace. The eigenspaces intersect trivially in characteristic zero. Hence \(\dim V=12\), and these are exactly its two eigenspace dimensions. Since the fixed points of \(\sigma\) on \(E(\mathbb Q(i)(v,t))\) are precisely the points of \(E(\mathbb Q(v,t))\), its rational Mordell–Weil rank is exactly \(8\).

This proof **does not** need the twelve published points to form an integral lattice basis: they are known to be independent, and the nonzero determinants above establish independent trace and anti-trace sections directly. It also does not infer an infinite-family theorem from finite numerical point tests.

## Verification

Run `python verification/check_arithmetic_rank.py` with Python 3 and SymPy installed. The script is self-contained apart from the adjacent `verification/cross_pairing.json`, which contains the complete \(3G\) data. It performs exact Gaussian-rational arithmetic throughout and:

1. Expands and verifies all twelve original Weierstrass identities symbolically over \(\mathbb Q(i)[v,t]\).
2. Recomputes the original \(H\) and new \(G\) height matrices by polynomial greatest common divisors on the independent good K3 specializations \(v=5\) and \(v=7\).
3. Verifies the published matrix \(H\), the cross-pairing data, both exact principal determinants, and the dimensions of both height-gram images.
4. Checks the induced candidate conjugation matrix is an involution with characteristic polynomial \((\lambda-1)^8(\lambda+1)^4\), and compares its pointwise group-law action against conjugated point coordinates at three distinct exact specializations.

The additional evaluations and the \(v=7\) check corroborate the exact intersection calculation; the proof itself relies on the exact \(v=5\) height determinants and the established geometric rank bound. The execution transcript is recorded in `verification/check_output.txt`.

## Relationship to prior work

Burek [1] proves the geometric rank \(12\), constructs twelve independent points over \(\mathbb Q(i)(v,t)\), and gives their mutual height matrix. Neither Theorem 1.1 nor Proposition 5.6 nor Appendix A computes the rank over \(\mathbb Q(v,t)\) or the conjugate cross-height matrix. The new assertion identifies precisely which part of the geometric section space descends to the rational-function base field, and how much rank appears over the quadratic extension.

Kumar and Kuwata [2] develop the underlying modular quartic K3 surfaces, geometric Mordell–Weil lattices, and *fields over which all their sections can be defined* (notably Theorems 2.10--2.11 and 5.1--5.3). Such a field-of-definition statement is not the invariant rank of the present two-variable arithmetic curve. Their explicit section formulas provide background but do not supply the two fixed/anti-fixed determinants above. The specialized geometric section-counting results for the same K3 family address height distributions and pair intersections, not arithmetic descent along complex conjugation of the varying-
v family.

## Limitations

The result determines ranks of Mordell–Weil groups, not integral bases, saturation indices, canonical heights of a chosen arithmetic basis, or a Galois module structure over arbitrary number fields. Its arithmetic conclusion uses a previously established geometric rank bound. The exact Galois-eigenspace calculation is over \(\mathbb Q(i)/\mathbb Q\) with \(v,t\) fixed; it does not classify every number-field extension. Although targeted primary-source and indexed-result comparisons did not locate an equivalent computation, an unindexed or unpublished arithmetic-rank computation could exist.

## References

[1] Dominik Burek, *An elliptic Calabi–Yau threefold of Mordell–Weil rank twelve*, arXiv:2610.01276v1 (public 1 October 2026), Theorem 1.1, Proposition 5.6 and Appendix A. https://arxiv.org/abs/2610.01276

[2] Abhinav Kumar and Masato Kuwata, *Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell–Weil lattices and their fields of definition*, Nagoya Mathematical Journal 228 (2017), arXiv:1409.2931, Sections 2 and 5. https://arxiv.org/abs/1409.2931

[3] Tetsuji Shioda, *On the Mordell–Weil lattices*, Commentarii Mathematici Universitatis Sancti Pauli 39 (1990), 211–240. The height formula is used through [1, Appendix A.3].
