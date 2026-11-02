# Rank-resolved commuting square-zero derivations of the Klein-four modular algebra

## Finding
Let \(k=\mathbb F_q\) have characteristic \(2\), and put \(A=k[x,y]/(x^2,y^2)\). For each integer \(m\ge1\), consider ordered \(m\)-tuples of associative \(k\)-derivations \(D_i\) such that \(D_i^2=0\) and \(D_iD_j=D_jD_i\) for all indices. Define the complete multivariate rank distribution
\[
\Phi_m(z_1,\ldots,z_m)=\sum_{(D_1,\ldots,D_m)}\prod_{i=1}^{m}z_i^{\operatorname{rank}_k D_i}.
\]
Set \(N=q^2+q+1\), and define
\[
\begin{aligned}
A_m&=\prod_i(1+(q^2-1)z_i),\\
F_m&=\prod_i(1+(q-1)z_i+(q^2-q)z_i^2),\\
G_m&=\prod_i(1+(q^2-1)z_i^2),\\
H_m&=\prod_i(1+(q-1)z_i),\\
K_m&=\prod_i(1+(q-1)z_i^2).
\end{aligned}
\]
Then
\[
\boxed{\begin{aligned}
\Phi_m={}&1+(q+2)(A_m-1)+(N-1)(F_m-1)+q^2(G_m-1)\\
&-(q+1)^2(H_m-1)-q^2(q+1)(K_m-1).
\end{aligned}}
\]
In particular, evaluating every variable at \(1\) gives the exact number
\[
\boxed{T_m(q)=1+(q^2+q+1)\bigl(2q^{2m}-(q+1)q^m+q-1\bigr).}
\]
For \(m\ge2\), the reduced algebraic variety of such tuples over any field of characteristic \(2\) has exactly two geometrically irreducible components, each of dimension \(2m+2\). Their reduced intersection has dimension \(m+3\).

## Assumptions and scope
All derivations are ordinary \(k\)-linear associative derivations; they need not preserve the maximal ideal. Ranks are ranks of endomorphisms of the four-dimensional \(k\)-space \(A\), not ranks of their restrictions to the maximal ideal. The characteristic is exactly \(2\), including extension fields of \(\mathbb F_2\). The geometric component assertions concern the underlying reduced variety and its reduced intersection, not a potentially nonreduced equation scheme. The pairwise commutation equations include all ordered pairs and all repetitions.

## Proof
**1. A restricted Lie-algebra identification.** A derivation is uniquely specified by arbitrary values
\[
D(x)=a+bx+cy+dxy,\qquad D(y)=e+hx+iy+jxy.
\]
Indeed the only defining relations \(x^2=y^2=0\) impose no constraints on a derivation in characteristic two. In the basis \((1,x,y,xy)\), its matrix is
\[
[D]=\begin{pmatrix}
0&a&e&0\\0&b&h&e\\0&c&i&a\\0&d&j&b+i
\end{pmatrix}.
\]
Every derivation annihilates \(1\), so the action on \(A/k1\) is well-defined and has matrix
\[
M(D)=\begin{pmatrix}b&h&e\\c&i&a\\d&j&b+i\end{pmatrix}.
\]
This establishes a linear bijection \(\operatorname{Der}_k(A)\to\mathfrak{sl}_3(k)\), since the eight entries are free and the trace is zero. The map respects commutators, because it is induced by quotienting an invariant line. In characteristic two the square of a derivation is itself a derivation, since the middle Leibniz terms cancel; the induced action of \(D^2\) is \(M(D)^2\). Injectivity therefore gives
\[
D^2=0\iff M(D)^2=0,\qquad [D,E]=0\iff[M(D),M(E)]=0.
\]
No pre-existing abstract Lie-algebra isomorphism is needed for these identities.

**2. Individual ranks.** Every nonzero \(3\times3\) square-zero matrix has rank one. Write \(M=uv^{\mathsf T}\) with nonzero column \(u\), nonzero row \(v^{\mathsf T}\), and \(v^{\mathsf T}u=0\). In the displayed four-by-four matrix the extra top row, restricted to \(A/k1\), is \((a,e,0)=(u_2v_3,u_1v_3,0)\). If \(v_3=0\) this row vanishes and \(\operatorname{rank}D=1\). If \(v_3\ne0\), the two coordinates \(u_1,u_2\) cannot both vanish (otherwise \(u\) is a multiple of the third basis vector, contradicting \(v^{\mathsf T}u=0\)). The extra row is then nonzero, with third coordinate zero, and hence is linearly independent of \(v^{\mathsf T}\), whose third coordinate is nonzero. Thus \(\operatorname{rank}D=2\). The zero matrix corresponds to the zero derivation.

Consequently, putting \(\ell\) for the third coordinate line in \(k^3\), a nonzero \(D\) has rank one exactly when \(\ell\subseteq\ker M(D)\), and has rank two otherwise.

**3. Commutation dichotomy.** If \(U\) and \(V\) are nonzero square-zero rank-one matrices with the same image line, both products \(UV\) and \(VU\) vanish. If their image lines differ and the matrices commute, the common product must be zero, as its image lies in two distinct lines. It follows that each kernel contains both image lines and, since each kernel is a plane, their kernels are equal. A third square-zero rank-one matrix commuting with both must have that same kernel. Induction shows that every commuting tuple of nonzero square-zero matrices either has one common image line or one common kernel plane. Conversely, any tuple of square-zero matrices with common image line or common kernel plane has all pairwise products zero and therefore commutes. This is an exhaustive classification of the set-theoretic locus.

**4. Two components.** For each line \(L\subset k^3\), square-zero matrices with image contained in \(L\) form \(\operatorname{Hom}(k^3/L,L)\), a vector space of dimension two. The associated incidence family for \(m\) matrices is a rank-\(2m\) vector bundle over \(\mathbb P^2\). Its image in the affine matrix-tuple space is closed (projective base), irreducible and of dimension \(2m+2\); a nonzero tuple uniquely identifies \(L\). The common-kernel counterpart is a rank-\(2m\) vector bundle over the dual projective plane of planes \(P\), with fibers \(\operatorname{Hom}(k^3/P,P)^{\oplus m}\), and has the same properties. For \(m\ge2\) neither image is contained in the other: choose two independent maps in a fixed two-dimensional fiber to obtain distinct kernels, and dually choose two with distinct image lines but the same kernel. Hence they are exactly the two geometric irreducible components. Their nonzero intersection corresponds to a unique flag \(L\subset P\subset k^3\) and an \(m\)-tuple in the one-dimensional space \(\operatorname{Hom}(k^3/P,L)\), not identically zero. The flag variety has dimension three, so the reduced intersection has dimension \(m+3\). For \(m=1\) the two families coincide, and the component statement is not asserted.

**5. Exact rank counts by inclusion-exclusion.** There are \(N=q^2+q+1\) lines and the same number of planes over \(\mathbb F_q\). For a fixed image line \(L=\ell\), all \(q^2-1\) nonzero maps have derivation rank one, giving factor \(1+(q^2-1)z_i\) per index. For each of the other \(N-1\) lines, exactly \(q-1\) nonzero maps have kernel containing \(\ell\), giving rank one, while the other \(q^2-q\) have rank two. This gives factor \(1+(q-1)z_i+(q^2-q)z_i^2\).

For a fixed common kernel plane \(P\), all its nonzero maps have derivation rank one when \(P\supset\ell\) (there are \(q+1\) such planes), and rank two otherwise (there are \(q^2\) such planes). For the intersection flags \(L\subset P\), there are \((q+1)^2\) flags with \(P\supset\ell\) and \(q^2(q+1)\) with \(P\not\supset\ell\); each flag admits \(q-1\) nonzero maps in its one-dimensional fiber, with the corresponding rank uniformly one or two.

Subtract the zero tuple from the contribution of each fixed line, plane and flag, add the zero tuple just once, and apply inclusion-exclusion for the two closed families. This produces exactly the displayed multivariate polynomial. Substituting \(z_i=1\) proves the scalar point-count formula. Every count is over actual rational lines, planes and flags, so no assumption of algebraic closedness is used for the finite-field enumeration.

## Verification
The standalone Python program `check.py` independently enumerates every eight-parameter derivation over \(\mathbb F_2\) (256 candidates) and \(\mathbb F_4\) (65,536 candidates), constructs the original four-by-four derivation matrices, and tests \(D^2=0\) and pairwise commutation by direct matrix multiplication. The four-element field uses explicit irreducible-polynomial arithmetic. It verifies the complete multivariate rank-pair histogram in both fields and, over \(\mathbb F_2\), the full rank-triple histogram. No use of the geometric classification is made in the enumeration. The resulting counts are \(22\) square-zero derivations and \(148\) commuting ordered pairs over \(\mathbb F_2\); \(316\) square-zero derivations and \(9,136\) pairs over \(\mathbb F_4\); and \(736\) commuting triples over \(\mathbb F_2\). These finite checks support but do not prove the all-fields theorem.

## Relationship to prior work
P. Levy's 2006 preprint on varieties of modules for \(\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z\) classifies geometric components of pairs of commuting square-zero matrices over an algebraic closure; specifically, its Proposition 2.3 implies the two-component, six-dimensional statement for three-by-three pairs. That special-case geometry is **prior art**, not an independent contribution here. N. V. Ngo's 2014 preprint, Theorem 3.3.3 and Proposition 3.3.4, determines the dimension of commuting restricted-nullcone tuples for general \(\mathfrak{sl}_n\) in characteristic two and supplies a maximal-dimensional component. Those dimensional conclusions are likewise prior art. The contribution assessed here is the complete all-arity **finite-field multivariate derivation-rank enumerator**, with the direct common-image/kernel and flag-incidence derivation showing its validity; the two-family geometry for arbitrary arity is recorded to make the arithmetic transparent, without claiming that the earlier component-dimension results are new. The related 2007 paper of Britnell and Wildon on commuting similarity classes concerns different matrix invariants and does not state this rank enumerator.

## Limitations
The theorem applies to \(A=k[x,y]/(x^2,y^2)\) in characteristic two, not general truncated polynomial algebras or odd characteristic. The component assertions are about reduced varieties and reduced intersections; no scheme-theoretic smoothness or radicality is asserted. The arithmetic formula counts ordered commuting tuples, not conjugacy orbits. The 2006 and 2014 literature contains significant geometric overlap, and unidentified stronger enumerations could still subsume the point-count formula; independent literature-priority verification has not occurred. The finite checks are not an infinite proof.

## References
- P. Levy, *Varieties of Modules for Z/2Z x Z/2Z*, arXiv:math/0609180, first public version September 6, 2006; Proposition 2.3 and Section 2. https://arxiv.org/abs/math/0609180
- N. V. Ngo, *On Nilpotent Commuting Varieties and Cohomology of Frobenius Kernels*, arXiv:1401.6820, first public version January 27, 2014; Theorem 3.3.3 and Proposition 3.3.4. https://arxiv.org/abs/1401.6820
- J. R. Britnell and M. Wildon, *On Types and Classes of Commuting Matrices over Finite Fields*, J. Lond. Math. Soc. 83 (2011), 470–492, doi:10.1112/jlms/jdq088 (background on other commuting invariants).
