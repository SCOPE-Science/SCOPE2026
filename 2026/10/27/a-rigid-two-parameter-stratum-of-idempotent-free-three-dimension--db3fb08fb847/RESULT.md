# A rigid two-parameter stratum of idempotent-free three-dimensional evolution algebras

## Finding

Let \(k=\mathbb C\). In the class of three-dimensional evolution algebras \(A\) for which \(A^2\) is isomorphic to the two-dimensional algebra
\[
W=ku\oplus kw,\qquad u^2=0,\quad uw=\tfrac12u,\quad w^2=u+w,
\]
consider the stratum \(\mathcal U\) admitting a natural basis whose three nonzero squares are pairwise nonproportional. Its isomorphism classes are in canonical bijection with
\[
\{(p,q)\in\mathbb C^2:-4p^3-27q^2\ne0\}.
\]
Every algebra in this stratum has zero as its only idempotent, is not solvable, and has trivial automorphism group. Thus this is a genuine two-complex-parameter family of pairwise nonisomorphic, automorphism-rigid, three-dimensional idempotent-free non-solvable evolution algebras. This classifies the stated stratum, **not** every three-dimensional idempotent-free evolution algebra.

For an unordered triple of distinct scalars \(T=\{t_1,t_2,t_3\}\), let \(s=t_1+t_2+t_3\) and \(D_i=(t_i-t_j)(t_i-t_k)\), with \(\{i,j,k\}=\{1,2,3\}\). On a basis \(e_1,e_2,e_3\) define
\[
U=e_1+e_2+e_3,\quad V=t_1e_1+t_2e_2+t_3e_3,\quad e_i e_j=0\ (i\ne j),
\]
\[
e_i^2=\frac{t_i+2-s}{2D_i}U+\frac{1}{D_i}V\quad (i=1,2,3).
\]
This algebra is denoted \(A_T\). Every member of \(\mathcal U\) is isomorphic to some \(A_T\), and
\[
A_T\cong A_{T'}\quad\Longleftrightarrow\quad T'=T+b\text{ for some }b\in\mathbb C.
\]
Writing \(r_i=t_i-s/3\), the complete invariants are \(p=\sum_{i<j}r_ir_j\) and \(q=r_1r_2r_3\); the centered triple is the root multiset of \(z^3+pz-q\).

## Assumptions and scope

An evolution algebra means a commutative, generally nonassociative \(k\)-algebra with a basis \((e_i)\) satisfying \(e_ie_j=0\) for \(i\ne j\). The square \(A^2\) is the span of all products, and the derived series is \(A^{(1)}=A\), \(A^{(m+1)}=(A^{(m)})^2\). Two nonzero square vectors are nonproportional when they span different one-dimensional subspaces. This property is stipulated for *some* natural basis; the proof shows that, on \(\mathcal U\), every natural basis differs by a permutation and nonzero individual scalings. The field is exactly \(\mathbb C\); the formulas are not asserted as a moduli classification in positive characteristic or in other strata.

## Proof

**1. The fixed square algebra.** In \(W\),
\[
(xu+yw)^2=(xy+y^2)u+y^2w.
\]
The equation \((xu+yw)^2=xu+yw\) gives \(y^2=y\). For \(y=0\), it forces \(x=0\); for \(y=1\), the remaining equation reads \(x+1=x\), impossible. Thus only zero is idempotent. Also \(W^2=W\), since \(u=2uw\) and \(w=w^2-u\). The square-zero elements are precisely \(ku\). Any automorphism must send \(u\mapsto au\) and \(w\mapsto bu+cw\) with \(ac\ne0\). Comparing images of \(uw=u/2\) gives \(c=1\); comparing \(w^2=u+w\) gives \(a=1\). Conversely all translations \(u\mapsto u,\ w\mapsto w+bu\) are automorphisms. Hence \(\operatorname{Aut}(W)\cong(\mathbb C,+)\).

**2. Explicit construction.** Set \(\iota_T(xu+yw)=xU+yV\). Distinctness of the \(t_i\) makes \(U,V\) linearly independent. The Lagrange interpolation identities
\[
\sum_i D_i^{-1}=\sum_i t_iD_i^{-1}=0,\quad \sum_i t_i^2D_i^{-1}=1,\quad\sum_i t_i^3D_i^{-1}=s
\]
imply, with \(a_i=(t_i+2-s)/(2D_i)\) and \(b_i=1/D_i\),
\[
\sum_i a_i=0,\quad 2\sum_i t_i a_i=1,\quad\sum_i t_i^2 a_i=1;
\qquad\sum_i b_i=\sum_i t_i b_i=0,\quad\sum_i t_i^2b_i=1.
\]
Therefore \(U^2=0\), \(UV=U/2\), and \(V^2=U+V\), making \(\iota_T\) an algebra isomorphism onto its image. The pairs \((a_i,b_i)\) are nonzero and pairwise nonproportional, since \(a_i/b_i=(t_i+2-s)/2\). Consequently the three squares span \(\iota_T(W)\) (indeed a pair of them already spans it), so \(A_T^2=\iota_T(W)\). Any idempotent of \(A_T\) belongs to this square and must be zero by Step 1; \((A_T^2)^2=A_T^2\ne0\), so \(A_T\) is not solvable.

**3. Monomial rigidity of natural bases.** More generally, suppose \(A\) has a natural basis with squares \(v_1,v_2,v_3\) spanning a two-dimensional subspace and no two \(v_i\) proportional. Choose linear functionals \(\alpha,\beta\) on that subspace such that \(\alpha(v_i)\ne0\) for every \(i\), and the three ratios \(\beta(v_i)/\alpha(v_i)\) are distinct. Such a choice exists over \(\mathbb C\): take \(\alpha\) off the three annihilator lines and \(\beta\) independent of \(\alpha\). The bilinear forms \(B_\alpha(x,y)=\alpha(xy)\) and \(B_\beta(x,y)=\beta(xy)\) are diagonal in the natural basis; the first is nondegenerate and the associated operator \(B_\alpha^{-1}B_\beta\) has three distinct eigenvalues. A second natural basis simultaneously diagonalizes both forms, hence consists of eigenvectors of that operator; it therefore differs from the first only by a permutation and nonzero scalings. In particular, the pairwise-nonproportional-square property is intrinsic to this stratum.

**4. Exhaustion and uniqueness.** Let \(A\in\mathcal U\), identify \(A^2\) with \(W\), and write its natural squares as \(v_i\in W\). Let \(\ell_i\in W^*\) be the coordinate restrictions of the chosen natural basis. Because \(u^2=0\),
\[
\sum_i \ell_i(u)^2v_i=0.
\]
The \(v_i\) span a plane and are pairwise nonproportional; their unique linear relation has all coefficients nonzero. Thus all \(\ell_i(u)\ne0\). Rescale each natural basis vector by \(\ell_i(u)\), so that the new restrictions are \(\ell_i(xu+yw)=x+t_i y\). The identity \(u^2=0\) becomes \(v_1+v_2+v_3=0\) for the rescaled squares. If two \(t_i\) coincide, the quadratic map \(W\to W\) becomes a scalar quadratic form times a single vector, contrary to \(W^2=W\). Hence the \(t_i\) are distinct. The three quadratics \((x+t_i y)^2\) form a basis of \(\operatorname{Sym}^2(W^*)\), by their Vandermonde determinant; decomposing the fixed map \((xu+yw)^2\) in that basis forces exactly the coefficients \(a_i,b_i\) in Step 2. This proves \(A\cong A_T\).

If \(F:A_T\to A_{T'}\) is an algebra isomorphism, Step 3 forces a monomial action on the natural bases. The restriction to the intrinsic square is an automorphism of \(W\), so Step 1 gives a translation \(w\mapsto w+bu\). Since \(U\) is the intrinsic vector \(u\), its three natural-basis coordinates are all \(1\), and preservation of \(u\) forces every monomial scaling factor to equal \(1\). Comparing the coordinates of \(w\) then yields \(T'=T-b\) as multisets. Conversely, if \(T'=T-b\), the corresponding permutation of coordinate bases carries \(U\) to \(U'\) and \(V\) to \(V'+bU'\), inducing the automorphism \(w\mapsto w+b u\) of the square and respecting the uniquely determined multiplication; hence it is an isomorphism. This proves the translation classification.

If \(F\) is an automorphism of \(A_T\), its translation parameter must stabilize the finite set \(T\). Summing the three elements of \(T+b=T\) gives \(3b=0\), hence \(b=0\), and distinctness forces its coordinate permutation to be the identity. Thus \(\operatorname{Aut}(A_T)=\{1\}\).

**5. Affine two-parameter moduli.** Every translation orbit of unordered distinct triples has a unique centered representative \(r_1+r_2+r_3=0\). The elementary symmetric functions \(p=\sum_{i<j}r_ir_j\) and \(q=r_1r_2r_3\) determine the unordered triple as the roots of \(z^3+pz-q\). The roots are distinct exactly when the discriminant \(-4p^3-27q^2\) is nonzero. Every such pair occurs over \(\mathbb C\). Consequently the classifying set is the claimed open plane, with no identifications remaining.

## Verification

A dependency-free exact-rational script `verify.py` checks the construction, rank, pairwise square-line separation, multiplication of \(U,V\), and centered moduli on several rational triples. For example, \(T=\{0,1,2\}\) gives
\[
e_1^2=-\tfrac14 e_1+\tfrac14e_2+\tfrac34e_3,\quad e_2^2=-e_2-2e_3,\quad e_3^2=\tfrac14e_1+\tfrac34e_2+\tfrac54e_3.
\]
Its moduli point is \((p,q)=(-1,0)\). These finite checks confirm sample arithmetic; the general statements follow from Steps 1–5, not from enumeration.

## Relationship to prior work

Hu and Wen (2026) construct one exceptional idempotent-free, non-solvable three-dimensional example inside a one-parameter family; their displayed exceptional natural squares include a proportional pair. Kaygorodov, Martín González and Viruel (2026), Section 2.1.8 and Question 9, report computer evidence for two essential parameters but do not claim a theorem classifying the three-dimensional idempotent-free, non-solvable locus. The present statement supplies an intrinsic complete classification and trivial automorphism groups **only for the distinct-square-line stratum**; it neither purports to recover the full idempotent-free locus nor to supersede the classical classification of all three-dimensional evolution algebras by Cabrera Casado, Siles Molina and Velasco (2017), or the later Celorrio–Velasco (2019) classification. The older global classifications may contain representatives of these algebras; a full table-to-invariant comparison is still needed to establish priority beyond this structural formulation.

## Limitations

The result covers complex algebras with square isomorphic to the specific non-evolution algebra \(W\) and pairwise nonproportional natural squares. It excludes the proportional-square-line boundary, including Hu–Wen's displayed exceptional basis. It is not a classification of all non-solvable or all idempotent-free evolution algebras. The full 2017 and 2019 classification tables were not retrievable during the bounded literature inspection; an equivalent intrinsic parametrization or rigidity assertion within them is an unresolved prior-art risk. The stated classifying set is a set of ordinary isomorphism classes, not a constructed fine moduli scheme.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, publicly posted 15 October 2026. Section 2.1.8 and Question 9. https://arxiv.org/html/2610.22248
2. X.-Y. Hu, R. Wen, *Idempotent-free non-solvable evolution algebras over* \(\mathbb C\), arXiv:2609.25023 (first arXiv version 12 August 2026); full text also at https://www.preprints.org/manuscript/202609.0078, Theorem 1, Proposition 1, and Remark 1.
3. Y. Cabrera Casado, M. Siles Molina, M. V. Velasco, *Classification of three-dimensional evolution algebras*, Linear Algebra Appl. 524 (2017), 68–108; arXiv:1701.07219; DOI:10.1016/j.laa.2017.02.015. Earlier global classification; full text not inspected here.
4. M. E. Celorrio, M. V. Velasco, *Classifying evolution algebras of dimensions two and three*, Mathematics 7 (2019), 1236; DOI:10.3390/math7121236. Earlier global classification; full text not inspected here.
