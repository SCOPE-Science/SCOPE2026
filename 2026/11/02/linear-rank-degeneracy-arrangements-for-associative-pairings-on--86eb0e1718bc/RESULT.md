# Linear rank-degeneracy arrangements for associative pairings on multi-branch Artin algebras

## Finding
Let \(k\) be any field, \(t\geq2\), and \(e_1,\ldots,e_t\geq2\) integers. Consider the finite-dimensional commutative local algebra
\[
A=k[x_1,\ldots,x_t]/(x_ix_j\ (i\ne j),\ x_i^{e_i}\ (1\le i\le t)).
\]
It is the fiber product over \(k\) of the truncated polynomial algebras \(k[x_i]/(x_i^{e_i})\). Its dimension is \(d=1+\sum_i(e_i-1)\). Every associative symmetric bilinear form on \(A\) has the unique expression \(B_f(u,v)=f(uv)\) for \(f\in A^*\).

**Rank classification.** Put \(c_0=f(1)\) and \(c_{ij}=f(x_i^j)\), for \(1\le j<e_i\). Let \(h_i=0\) if every \(c_{ij}\) is zero, and otherwise let \(h_i\) be the largest \(j\) for which \(c_{ij}\ne0\). Set \(S=\{i:h_i>0\}\). Then
\[
\operatorname{rank}B_f=\begin{cases}
0,&S=\varnothing,\ c_0=0,\\
1,&S=\varnothing,\ c_0\ne0,\\
2+\sum_{i\in S}(h_i-1),&S\ne\varnothing.
\end{cases}
\]
This formula is characteristic-independent and also gives the radical dimension \(d-\operatorname{rank}B_f\).

**Complete arithmetic distribution.** If \(k=\mathbb F_q\), write \(P_{\mathbf e,q}(z)=\sum_{f\in A^*}z^{\operatorname{rank}B_f}\). Then
\[
\boxed{P_{\mathbf e,q}(z)=1+(q-1)z+qz^2\left[\prod_{i=1}^t\left(1+(q-1)\sum_{a=0}^{e_i-2}q^az^a\right)-1\right].}
\]
In particular \(P_{\mathbf e,q}(1)=q^d\).

**Exact geometry of all degeneracy loci.** Let \(R_{\max}=2+\sum_i(e_i-2)=d-t+1\). Over any algebraically closed extension of \(k\), the reduced set of forms of rank at most \(R\) is the origin if \(R=0\), and the line \(\{f:c_{ij}=0\ \forall i,j\}\) if \(R=1\). For each \(2\le R\le R_{\max}\), its irreducible components are *exactly* the distinct linear spaces
\[
L_{\mathbf a}=\{f:c_{ij}=0\ \text{when }j>1+a_i\},\qquad
0\le a_i\le e_i-2,\quad\sum_i a_i=R-2.
\]
Every component has dimension \(t+R-1\), and the number of components is
\[
[z^{R-2}]\prod_{i=1}^t(1+z+\cdots+z^{e_i-2}).
\]
These statements concern **reduced** rank loci, not their possibly nonreduced determinantal schemes. The generic rank is \(d-t+1\), and the generic radical has dimension exactly \(t-1\).

For example, with \(\mathbf e=(2,3,3)\) and \(q=2\), the rank polynomial is \(1+z+14z^2+32z^3+16z^4\). The rank-at-most-three locus has two five-dimensional linear components in the six-dimensional parameter space. This family has no nondegenerate associative bilinear forms for \(t\geq2\), yet its entire degeneracy geometry and exact finite-field rank census are explicit.

## Assumptions and scope
The field is arbitrary for the rank and reduced-geometry assertions. The exponent tuple is any ordered finite tuple of integers \(e_i\geq2\) with \(t\geq2\). The finite-field formula applies to each prime power \(q\), without characteristic restrictions. Bilinear forms are counted as actual maps, not modulo change of basis or algebra automorphisms. By 'rank-at-most-\(R\) locus' we mean the closed reduced algebraic subset of the affine space \(A^*\) defined set-theoretically over an algebraic closure by the vanishing of minors of size \(R+1\) of the Gram matrix of \(B_f\).

## Proof
**(1) All invariant forms are multiplication pairings.** Associativity says \(B(ab,c)=B(a,bc)\). Because \(A\) has an identity, setting \(f(v)=B(1,v)\) gives \(B(a,b)=B(1,ab)=f(ab)\); conversely the displayed form is associative and symmetric. The map \(f\mapsto B_f\) is injective since \(B_f(1,v)=f(v)\).

**(2) A characteristic-free block-rank calculation.** For a fixed \(f\), the powers \(x_i^j\) with \(j>h_i\) pair to zero with every element and lie in the radical. For each active branch \(i\), the subspace \(U_i=\langle x_i,\ldots,x_i^{h_i-1}\rangle\) (empty for \(h_i=1\)) has Gram matrix \((c_{i,u+v})_{1\le u,v<h_i}\), with the convention that out-of-range coefficients vanish. Its anti-diagonal is the nonzero constant \(c_{i,h_i}\), and all entries strictly beyond that anti-diagonal vanish. Reversing the order of its columns makes it triangular with nonzero diagonal, so \(U_i\) is nondegenerate of dimension \(h_i-1\). Distinct \(U_i\) are mutually orthogonal.

Orthogonally eliminate the \(U_i\)-parts of the unit vector. The remaining nonradical block is spanned by the adjusted unit and the top powers \(x_i^{h_i}\) for \(i\in S\). The top powers are mutually orthogonal and pair with the adjusted unit by \(c_{i,h_i}\). Consequently the residual Gram matrix has the shape
\[
\begin{pmatrix}c&v^T\\v&0\end{pmatrix},\qquad v=(c_{i,h_i})_{i\in S}.
\]
It has rank two whenever \(S\ne\varnothing\), in every characteristic: take a nonzero coordinate of \(v\) to obtain a nonsingular two-by-two minor; all remaining rows are dependent on the unit row. The orthogonal nondegenerate \(U_i\) blocks supply total rank \(\sum_i(h_i-1)\). When \(S=\varnothing\), the Gram matrix only has its unit-unit entry \(c_0\). This proves the classification.

**(3) Counting over finite fields.** For a branch with \(h_i=0\), there is exactly one choice for its positive-degree coefficients. For prescribed \(h_i=j\ge1\), the top coefficient can be chosen in \(q-1\) ways and the \(j-1\) lower coefficients are free, giving \((q-1)q^{j-1}\) choices. The coefficient \(c_0\) is free in \(q\) ways unless all \(h_i\) vanish, in which case it yields one rank-zero form and \(q-1\) rank-one forms. Multiplying these independent branch weights and recording \(2+\sum(h_i-1)\) gives the boxed polynomial.

**(4) Geometry, inclusions and maximal components.** For \(R\ge2\), by the rank formula, a functional has rank at most \(R\) precisely when its vector of nonnegative 'excess heights' \(a_i=\max(0,h_i-1)\) satisfies \(\sum a_i\le R-2\). The bounds \(a_i\le e_i-2\) hold. Since \(R-2\le\sum_i(e_i-2)\), any such vector can be increased coordinatewise, without exceeding the bounds, to one with sum exactly \(R-2\). The resulting functional lies in the corresponding \(L_{\mathbf a}\), proving the indicated union. Conversely any \(f\in L_{\mathbf a}\) has rank at most \(2+\sum a_i=R\). Distinct index vectors with equal sum are incomparable coordinatewise, so their linear spaces are distinct, irreducible, and none contains another; hence they are exactly the irreducible components. Their coordinate dimensions are \(1+\sum_i(1+a_i)=t+R-1\). The coefficient extraction counts the admissible index vectors. The rank-zero and rank-one cases follow directly. Finally, the maximal-rank stratum is a nonempty Zariski-open subset of \(A^*\), with \(R_{\max}=d-t+1\), proving the generic radical claim.

## Verification
A standalone standard-library Python checker constructs the basis, product table, and Gram matrix directly from the multiplication table and uses finite-field Gaussian elimination, including a polynomial-basis implementation of \(\mathbb F_4\). It directly enumerates every functional for 18 cases over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), verifies the complete rank histogram and checks pointwise equality of each predicted rank-at-most-\(R\) union with the determinantal rank condition. The expected terminal marker is `MULTIBRANCH_ASSOCIATIVE_PAIRING_RANKS_OK 18`. Run `python verify_multibranch_forms.py` from the directory containing this file and the checker. Finite tests corroborate but are not the proof of the arbitrary-field theorem.

## Relationship to prior work
Fiber products of local rings and their homological properties are established subjects. Moore, *Cohomology over Fiber Products of Local Rings* (arXiv:0704.3631v1, 26 April 2007) computes resolutions and Ext over fiber products, not ranks of all multiplication-induced bilinear forms. Ananthnarayan, Avramov and Moore, *Connected sums of Gorenstein local rings* (arXiv:1005.1304v1, 7 May 2010), study the Gorenstein property, colength and connected sums rather than the present rank loci. Murray, *Bilinear Forms on Frobenius Algebras* (published 2005; openly available as arXiv:1401.6486), studies nondegenerate associative forms and their homotheties: by construction the present multi-branch algebras for \(t\ge2\) are not Frobenius, and their **degenerate** rank census does not follow from those theorems. A published analysis of automorphisms of the same truncated coordinate-cross algebra (equal-exponent case; 2026, Reference 4) supplies a particularly close same-object comparison but determines automorphism normal forms and group orders, not the present ranks of degenerate multiplication pairings. The canonical equivalence between linear functionals and multiplication pairings is elementary prior background; novelty is claimed only for the complete arithmetic rank formula and the linear-component description of the reduced determinantal loci in this entire multi-branch family. No claim of exhaustively certified publication priority is made.

## Limitations
The rank-stratum decomposition concerns reduced varieties; scheme-theoretic multiplicities and embedded components are not determined. The result is for fiber products of truncated one-variable polynomial algebras, not arbitrary Artinian local algebras or their deformation families. It does not classify isometry/homothety orbits of forms, and no independent mathematical audit is represented. A broader inverse-system or determinantal-arrangement theorem might imply this specialized classification in less easily retrieved literature.

## References
1. W. F. Moore, *Cohomology over Fiber Products of Local Rings*, arXiv:0704.3631v1 (2007-04-26), https://arxiv.org/abs/0704.3631.
2. H. Ananthnarayan, L. L. Avramov and W. F. Moore, *Connected sums of Gorenstein local rings*, arXiv:1005.1304v1 (2010-05-07), https://arxiv.org/abs/1005.1304.
3. W. Murray, *Bilinear Forms on Frobenius Algebras*, Journal of Algebra 293 (2005), 89–101; lawful open manuscript arXiv:1401.6486, https://arxiv.org/abs/1401.6486.
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* (2026), https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb/RESULT.md.
