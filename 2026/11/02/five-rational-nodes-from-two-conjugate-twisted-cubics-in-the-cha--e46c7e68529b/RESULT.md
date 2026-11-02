# Five rational nodes from two conjugate twisted cubics in the characteristic-two symmetric Bring model

## Finding

For the elementary-symmetric model \(C\subset\mathbb P^4_{\mathbb F_2}\) given by \(\sigma_1=\sigma_2=\sigma_3=0\), the geometric curve consists of two smooth rational normal cubic curves exchanged by Frobenius. Their intersection is the five-point set of permutations of \([0:1:1:1:1]\), and every intersection is transverse. The connected curve has arithmetic genus four and exactly five ordinary nodes. For all integers \(m\ge1\),
\[
\#C(\mathbb F_{2^m})=\begin{cases}5 & m\text{ odd},\\2^{m+1}-3&m\text{ even}.\end{cases}
\]
The geometric generalized Jacobian is a four-dimensional torus, and over \(\mathbb F_2\) it is \(\bigl(R^1_{\mathbb F_4/\mathbb F_2}\mathbb G_m\bigr)^4\).

## Assumptions and scope

Here \(\sigma_i\) is the elementary symmetric function of degree \(i\) in five homogeneous coordinates. The curve is considered with its reduced/projective scheme structure over \(\mathbb F_2\); the proof also shows reducedness. This is the coefficientwise reduction of the *elementary-symmetric* integral equations for Bring's canonical complete intersection. Over characteristic zero Newton identities identify it with the classical power-sum presentation, but the latter's naive reduction mod two is not equivalent: the degree-two power sum becomes the square of the first. No claim is made for that different non-flat model. All geometric statements are over an algebraic closure unless a finite field is specified.

## Proof

Eliminate the fifth coordinate by \(x_4=x_0+x_1+x_2+x_3\), writing the other coordinates \(a,b,c,d\). The quadratic equation is
\[
Q=a^2+b^2+c^2+d^2+ab+ac+ad+bc+bd+cd=0.
\]
Its alternating polar form has matrix with zero diagonal and ones off the diagonal, of determinant one in characteristic two. Hence \(Q\) is a smooth quadric surface. Directly checking the fifteen nonzero binary vectors shows \(\#Q(\mathbb F_2)=5\), so the quadric is nonsplit over \(\mathbb F_2\) and becomes a split Segre quadric over \(\mathbb F_4\).

Let \(\omega^2+\omega+1=0\), and take four isotropic vectors in coordinates \((a,b,c,d)\):
\[
p_0=(0,1,1,1),\quad p_1=(0,0,1,\omega+1),\quad p_2=(0,1,0,\omega+1),\quad p_3=(1,0,0,\omega).
\]
Their polar pairings vanish except \(B(p_0,p_3)=B(p_1,p_2)=1\). The Segre parametrization is therefore
\[
(a,b,c,d)=p_0SU+p_1SV+p_2TU+p_3TV,
\quad [S:T],[U:V]\in\mathbb P^1.
\]
A coefficientwise expansion in \(\mathbb F_4[S,T,U,V]\) gives the **exact** factorization
\[
\sigma_3=(SV^2+T(U^2+V^2))(S^2V+T^2(U+V)).
\]
The factors have bidegrees \((1,2)\) and \((2,1)\). Each is the graph of a degree-two Frobenius map between the two \(\mathbb P^1\) factors: the first has \([S:T]=[U^2+V^2:V^2]\), the second has \([U:V]=[S^2+T^2:T^2]\). Each graph is smooth, irreducible, and isomorphic to \(\mathbb P^1\); its Segre image has degree three and the four coordinate sections form a basis of the cubics on \(\mathbb P^1\), so each is a twisted cubic. Their divisor intersection number on \(\mathbb P^1\times\mathbb P^1\) is \(1\cdot1+2\cdot2=5\).

For a point on \(\sigma_1=\sigma_2=\sigma_3=0\), the three rows of the Jacobian matrix are \((1)_i,(x_i)_i,(x_i^2)_i\) in characteristic two. A three-by-three Vandermonde minor is nonzero precisely when the five coordinates take at least three distinct values. Therefore any singular geometric point has at most two coordinate values. If distinct values are \(r\) and \(s\), \(\sigma_1=0\) forces the value of odd multiplicity to vanish. The \(\sigma_2\) equation excludes two equal nonzero entries, leaving exactly four identical nonzero entries and one zero. These give five rational singular points \([0:1:1:1:1]\) and permutations; they also satisfy \(\sigma_3=0\). Since distinct smooth components meet only at singularities, the five points exhaust their intersection. The total scheme-theoretic intersection multiplicity is five, so all five points have multiplicity one, giving transverse ordinary nodes. Smoothness of the two components and their distinctness prove the complete intersection is reduced.

Frobenius interchanges the two rulings of the nonsplit quadric, hence interchanges its two constituent graphs. All intersection points are fixed by Frobenius. If \(m\) is odd, any \(\mathbb F_{2^m}\)-point must lie in both conjugate components, giving exactly five points. If \(m\) is even, both rational components contribute \(2^m+1\) points, with five common points, giving \(2^{m+1}-3\). Adjunction for a \((2,3)\) complete intersection gives \(p_a=4\), also obtained from the two genus-zero components and five nodes: \(0+0+5-2+1=4\).

For a nodal connected curve with two rational components and five nodes, the normalization sequence identifies the connected geometric Picard variety with the torus having character lattice \(H_1(\Gamma,\mathbb Z)\), where \(\Gamma\) has two vertices and five parallel edges, thus rank four. Frobenius swaps the two vertices and fixes the five edges, so its action on this cycle lattice is minus identity. This is the character action of four copies of the norm-one torus for the quadratic extension \(\mathbb F_4/\mathbb F_2\).

## Verification

The supplied standalone `verify.py` uses exact finite-field arithmetic for \(\mathbb F_4\) and symbolic expansion modulo two. It verifies smoothness and nonsplit point count of the quadric, the displayed Segre factorization, all five binary singular points, and the finite-field point counts over \(\mathbb F_2\) and \(\mathbb F_4\). The file `verification_output.txt` is the output of actually executing that script. The all-extension counts and torus statement are mathematical deductions from the two-component Frobenius descent, not finite-enumeration extrapolations.

## Relationship to prior work

Bring's symmetric canonical genus-four curve is classical. Braden–Northover (2012, arXiv:1206.6004) discuss the characteristic-zero power-sum presentation, while Braden–Disney-Hogg (2023) treat its classical automorphisms and Jacobian. Korchmáros–Lia–Timpanella (arXiv:2112.10886) study symmetric power-sum generalizations in characteristic zero and primes \(p\ge7\), explicitly excluding characteristic two. Their results do not give the elementary-symmetric special fiber considered here. No matching decomposition or Frobenius descent was identified in the examined sources or semantic comparison searches; complete historical priority is not established.

## Limitations

The algebraic object is a specific integral model; distinct models agreeing in characteristic zero can have different special fibers. No assertion is made about stable reduction of the smooth generic fiber after arbitrary base change, nor about uninspected historic accounts of special reduction. The generalized Jacobian calculation concerns the connected Picard variety of this nodal special fiber; it is not a claim about the smooth characteristic-zero Jacobian. Independent audit has not been performed.

## References

- H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, SIGMA 8 (2012), 065, arXiv:1206.6004, DOI 10.3842/SIGMA.2012.065.
- G. Korchmáros, S. Lia, M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886 (first posted 2021).
- H. W. Braden and A. Disney-Hogg, *Bring's curve: old and new*, European Journal of Mathematics (2023), DOI 10.1007/s40879-023-00706-0.
