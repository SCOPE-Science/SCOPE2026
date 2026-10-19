# Two geometrically irreducible commuting-tuple components for split octonions

## Finding

Let \(k=\mathbb F_q\) have odd cardinality \(q\), and let \(\mathbb O\) be the split eight-dimensional octonion (Cayley) algebra over \(k\). For every integer \(s\ge2\), let \(C_s\) be the affine scheme of ordered tuples \((a_1,\ldots,a_s)\in\mathbb O^s\) satisfying \(a_i a_j=a_j a_i\) for every \(i,j\). All geometric-component assertions below refer to its **reduced support**, not to a claim of scheme-theoretic reducedness.

**Theorem.** Over an algebraic closure, \((C_s)_{\mathrm{red}}\) has exactly two irreducible components. Write \(a_i=\lambda_i1+v_i\), where \(v_i\) has octonion trace zero, and let \(V\) be the seven-dimensional trace-zero subspace.

1. The first component \(X_s\) consists of tuples for which the \(7\times s\) matrix \([v_1\ \cdots\ v_s]\) has rank at most one. It has dimension \(2s+6\).
2. The second component \(Y_s\) consists of tuples whose imaginary parts lie in a common two-dimensional subspace \(P\subset V\) on which every element has zero quadratic norm and any two elements commute. It has dimension \(3s+5\).
3. The intersection \(X_s\cap Y_s\) consists exactly of tuples whose imaginary matrix has rank at most one and whose nonzero imaginary entries have zero norm. It is irreducible of dimension \(2s+5\).

Consequently the reduced commuting-tuple support is **non-equidimensional** for every \(s\ge2\). The number of rational commuting tuples is exactly
\[
|C_s(\mathbb F_q)|=[6]_q q^{3s}-q[5]_q q^{2s},\qquad [d]_q=1+q+\cdots+q^{d-1}.
\]
In particular the point count is polynomial in \(q\) for all odd prime powers and every arity. If \(r\) is the span dimension of the imaginary vectors, the exact multiplicities for \(r=0,1,2\) are
\[
q^s,\qquad q^s[7]_q(q^s-1),\qquad q^s[6]_q(q^s-1)(q^s-q),
\]
respectively; there are no larger spans.

## Assumptions and scope

The split Cayley algebra is represented by Zorn matrices \(\left(\begin{smallmatrix}a&u\\v&b\end{smallmatrix}\right)\), with \(a,b\in k\) and \(u,v\in k^3\), multiplied by
\[
(a,u,v,b)(c,x,y,d)=(ac+u\cdot y,\; ax+du-v\times y,\;cv+by+u\times x,\;bd+v\cdot x).
\]
Its identity is \((1,0,0,1)\), trace is \(a+b\), and norm is \(ab-u\cdot v\). Since \(2\) is invertible, every element splits uniquely into a scalar and a trace-zero element. For \(v=(t,u,w,-t)\in V\), the restricted norm is \(-t^2-u\cdot w\), a nondegenerate quadratic form of dimension seven and Witt index three. No characteristic-two statement is made.

The reduced scheme means the Zariski-closed set with its radical ideal. Statements about embedded components, nilpotents in the scheme structure, singularities, and smoothness are **not** asserted.

## Proof

**Centralizers.** For a nonzero trace-zero \(v\), its commutator kernel inside \(V\) has dimension one when \(N(v)\ne0\) and dimension three when \(N(v)=0\). These are directly verified in Zorn coordinates: when \(v\) is isotropic, one may take \(v=(0,e_1,0,0)\). Then
\[
K(v)=\ker([v,-]|_V)=\{(0,te_1,(0,b,c),0):t,b,c\in k\}.
\]
Every element of this three-space has norm zero. For two members with lower vectors \((0,b,c)\) and \((0,b',c')\), their commutator is proportional to \((bc'-cb')v\), which is a nonzero alternating form on \(K(v)/kv\). Hence the two-dimensional commuting subspaces of \(K(v)\) containing \(v\) correspond bijectively to the projective lines of its two-dimensional quotient: exactly \(q+1\) over \(\mathbb F_q\). The same statements hold over an algebraic closure, by the standard transitivity of split-octonion automorphisms on nonzero isotropic directions (or equivalently by a Witt-adapted Zorn basis). The nonisotropic centralizer being the line \(kv\) follows by the same coordinate calculation, or by invertibility of the pure-element square.

**Maximum span two.** In any commuting tuple, choose a nonzero imaginary vector \(v\). If \(N(v)\ne0\), all imaginary vectors belong to \(kv\). If \(N(v)=0\), the remaining vectors belong to \(K(v)\); the alternating pairing on \(K(v)/kv\) forces their images to lie on a single line, so their span has dimension at most two. Every linearly independent commuting imaginary pair thus spans an entirely norm-zero commuting plane.

**The family of commuting planes.** Let \(Q\subset\mathbb P(V)\cong\mathbb P^6\) denote the smooth projective norm-zero quadric; \(\dim Q=5\) and \(|Q(\mathbb F_q)|=(q^6-1)/(q-1)=[6]_q\). The incidence space \(I=\{([v],P):[v]\subset P,\;P\text{ a commuting norm-zero plane}\}\) is a projective-line bundle over \(Q\), since planes through \([v]\) are lines in \(K(v)/kv\). Therefore \(I\) is geometrically irreducible of dimension six. Each plane contains a projective line of null directions, so the family \(F\) of these planes is geometrically irreducible of dimension five, and double counting incidence gives \(|F(\mathbb F_q)|=[6]_q\). This is the familiar point-line incidence of the split Cayley hexagon, used here as a geometric parametrization.

**Two components.** The rank-at-most-one locus \(X_s\) is a determinantal variety in \(V^s\) times a scalar factor \(k^s\), and is irreducible of dimension \((7+s-1)+s=2s+6\). The locus \(Y_s\) is the proper image of the incidence vector bundle \(\{(P,(v_i)):P\in F,\,v_i\in P\}\to V^s\), times \(k^s\). It is closed and irreducible, and the generic rank-two tuple determines its plane uniquely, yielding dimension \(5+2s+s=3s+5\). The maximum-span result gives \(C_s=X_s\cup Y_s\) set-theoretically. For \(s\ge2\), \(X_s\) has tuples with nonisotropic rank-one direction not in \(Y_s\), while \(Y_s\) has rank-two tuples not in \(X_s\), proving these are exactly the two components. Their intersection is the null rank-at-most-one cone times \(k^s\); its nonzero part is a \(\mathbb G_m\)-quotient of the six-dimensional null cone and \(k^s\setminus\{0\}\), hence has dimension \(6+s-1+s=2s+5\) and irreducible closure.

**Rational points.** The unique rank-zero imaginary matrix contributes one; rank one contributes \([7]_q(q^s-1)\), choosing its unique projective direction; rank two contributes \([6]_q(q^s-1)(q^s-q)\), choosing its unique commuting plane and then an ordered spanning \(s\)-tuple. Scalar coordinates multiply the total by \(q^s\). Finally use \([7]_q=1+q[6]_q\) and \([6]_q=1+q[5]_q\) to obtain the displayed two-term formula. No finite census is used to conclude the infinite-field-uniform claim.

## Verification

The standalone `verify.py` reconstructs multiplication as Zorn matrices and independently computes commutator ranks by exact modular Gaussian elimination for all trace-zero elements over \(\mathbb F_3\) and \(\mathbb F_5\). It checks the three adjoint ranks and their multiplicities, the commuting-pair total, the Heisenberg centralizer pair/triple statistics, and the elementary all-arity identity. Running `python verify.py` yields `VERIFY_OK`. In particular the commuting-pair counts are \(235953\) for \(q=3\) and \(58590625\) for \(q=5\). These computations corroborate, but do not prove, the geometry over arbitrary odd finite fields.

## Relationship to prior work

Knarr and Stroppel, *Subalgebras of Octonion Algebras*, provide a general classification of subalgebras and record the two- versus four-dimensional centralizer dichotomy (Lemma 3.1), the four-dimensional nilpotent centralizer model (Example 3.2), and the commutative-subalgebra classification (Section 7). The earlier classification by Grishkov, Merlini Giuliani and Zavarnitsine counts unital subalgebras over finite fields. These powerful antecedents explain the local algebraic ingredients; the specific assertion here is the global **two-component, non-equidimensional commuting-tuple support for every arity**, together with its span-refined polynomial enumerator. The split-Cayley-hexagon point-line geometry is classical and is not claimed as new.

## Limitations

Only odd characteristic is covered; characteristic two has a different centralizer structure. The geometric claim concerns reduced support; no assertion about the scheme's defining ideal being radical is made. Classification of subalgebras in the existing literature is strong background, and an unnoticed formulation or direct implication of the global tuple-geometry theorem remains an originality risk. Independently established algebraic-geometric certification has not been performed.

## References

1. S. Giardino and H. L. Carrión, *Lie 3-algebra and super-affinization of split-octonions*, arXiv:1004.4228v1 (23 April 2010); split multiplication and structure tensors.
2. A. N. Grishkov, M. de L. Merlini Giuliani, A. V. Zavarnitsine, *Classification of subalgebras of the Cayley algebra over a finite field*, J. Algebra Appl. 9 (2010), 791–808, doi:10.1142/S0219498810004233.
3. N. Knarr and M. J. Stroppel, *Subalgebras of Octonion Algebras*, arXiv:2303.00335 (2023), especially Sections 3, 5 and 7.
4. T. C. de Mello and P. Saini, *Generalized Commutator on Octonion Algebra*, arXiv:2610.04466 (2026); abstract inspected, complete text unavailable during comparison.
