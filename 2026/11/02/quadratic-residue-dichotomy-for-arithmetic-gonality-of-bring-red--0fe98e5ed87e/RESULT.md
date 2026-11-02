# Quadratic-residue dichotomy for arithmetic gonality of Bring reductions

## Finding
Let \(p\ge3\) be a prime, \(p\ne5\), and let \(B_p\subset\mathbb P^4_{\mathbb F_p}\) be the projective complete intersection of the first three elementary symmetric polynomials in five homogeneous coordinates. This is the reduction of the integral elementary-symmetric canonical model of Bring's curve. Then \(B_p\) is smooth, geometrically connected, and of genus four. Its geometric gonality is three, while its arithmetic gonality is
\[
\operatorname{gon}_{\mathbb F_p}(B_p)=\begin{cases}3,&p\equiv1,4\pmod5,\\4,&p\equiv2,3\pmod5.\end{cases}
\]
In particular, its two geometric degree-three pencils are individually defined over \(\mathbb F_p\) precisely when five is a square in \(\mathbb F_p\). Otherwise they are conjugate over \(\mathbb F_{p^2}\).

## Assumptions and scope
The integer model is \(e_1=e_2=e_3=0\), where \(e_j\) is the elementary symmetric polynomial of degree \(j\) in the five homogeneous coordinates. For \(p\ge7\), it is also the reduction of the first-three-power-sums equations because the integers two and three are invertible. In characteristic three, the elementary-symmetric and literal power-sum reductions are **not** the same; the theorem is specifically about the former. Gonality over a field is the minimum degree of a nonconstant morphism to \(\mathbb P^1\) defined over that field. Geometric gonality means gonality after extension to the algebraic closure.

## Proof
**1. Smooth canonical curve.** For all \(p\ge7\), geometric smoothness and irreducibility of the same power-sum complete intersection are established in Korchmáros--Lia--Timpanella, under their hypotheses \(m=5\le p-1\). For \(p=3\), calculate on the locus \(e_1=e_2=0\): the Jacobian rows of \(e_1,e_2,e_3\), up to changing signs, are \((1)_i\), \((x_i)_i\), and \((x_i^2)_i\). If rank were below three, the five coordinates could have at most two distinct values \(a,b\), since a Vandermonde minor for any three distinct values is nonzero. If exactly \(r\) entries equal \(a\) and \(5-r\) equal \(b\), with \(1\le r\le4\), the equations \(e_1=e_2=0\) give \(r a+(5-r)b=0\) and \(r a^2+(5-r)b^2=0\). For \(r=1,4\), these equations force \(a=b=0\); for \(r=2\), they give \(a=0\), and then \(e_3=b^3\ne0\); for \(r=3\), they give \(b=0\), and then \(e_3=a^3\ne0\). A single repeated value also forces zero from \(e_1=5a=2a\). Thus there is no geometric singular point. A smooth projective complete intersection of type \((2,3)\) in \(\mathbb P^3\) is geometrically connected and has canonical sheaf \(\mathcal O(1)\), genus four and nonhyperelliptic canonical embedding.

**2. The arithmetic quadratic form.** Eliminate \(x_5=-(x_1+x_2+x_3+x_4)\) using \(e_1=0\). The unique canonical quadric is
\[
q=-\sum_{i=1}^4x_i^2-\sum_{1\le i<j\le4}x_ix_j.
\]
Its integral Hessian is the matrix with diagonal entries \(-2\) and off-diagonal entries \(-1\), of determinant \(5\). In odd characteristic the determinant square class is unchanged by multiplication of the associated matrix by \(2^{-1}\). Thus the nonsingular quadric has discriminant square class \(5\). A nonsingular quadric surface in \(\mathbb P^3_{\mathbb F_p}\) is split precisely when this class is a square. By quadratic reciprocity, \(5\) is a quadratic residue mod \(p\ne5\) precisely when \(p\equiv1,4\pmod5\).

**3. The lower bound.** Every geometric degree-three pencil on a smooth nonhyperelliptic genus-four complete intersection of a smooth quadric and a cubic is one of the two rulings of its unique canonical quadric. In the split case the rulings and their degree-three maps are individually defined over \(\mathbb F_p\). In the nonsplit case Frobenius exchanges the two rulings, so there is no \(\mathbb F_p\)-defined morphism of degree three to \(\mathbb P^1\). The canonical embedding also precludes degree-two morphisms, and the genus precludes degree one. Consequently arithmetic gonality is at least four in the nonsplit case; geometric gonality is always three.

**4. Uniform upper bound four.** In an algebraic closure choose \(i\) with \(i^2=-1\). The point
\[
P=[1:0:-1:i:-i]
\]
lies on \(B_p\): these five coordinates are roots of \(T(T^2-1)(T^2+1)=T^5-T\), whose coefficients of \(T^4,T^3,T^2\) vanish, so \(e_1=e_2=e_3=0\). If \(-1\) is a square in \(\mathbb F_p\), then \(P\) is rational. Its embedded tangent line \(L\) is defined over \(\mathbb F_p\) and meets \(B_p\) in a subscheme containing \(2P\). If \(-1\) is not a square, then \(P\) and its conjugate \(P^{(p)}\) are distinct quadratic points; their secant line \(L\) is \(\mathbb F_p\)-rational and its intersection with \(B_p\) contains the degree-two divisor \(P+P^{(p)}\). In either case, the pencil of planes through \(L\) restricts to a rational map \(B_p\dashrightarrow\mathbb P^1\) over \(\mathbb F_p\), which extends to a morphism because \(B_p\) is smooth and projective. Its degree is at most \(6-2=4\), since a hyperplane section has degree six and at least the indicated degree-two divisor is fixed. Combining with the lower bound gives arithmetic gonality four in the nonsplit case. In the split case the quadric's rational ruling gives gonality three. This proves the asserted classification.

## Verification
Run `python verify.py` to check the characteristic-three \(\mathbb F_9\)-point count, the absence of \(\mathbb F_3\)-points, a quadratic rational point, and the characteristic-three quadric discriminant. Run `python verify_witnesses.py` to verify quadratic points over characteristics three and seven by an independently coded finite-field multiplication and elementary-symmetric calculation. The proof for every prime is the symbolic determinant calculation, the published smoothness theorem for primes at least seven, the explicit characteristic-three Jacobian proof, the standard genus-four ruling theorem, and the uniform root-of-quintic point; finite enumerations are only supplementary checks.

## Relationship to prior work
Korchmáros, Lia and Timpanella study the power-sum Bring family in characteristics \(p\ge7\), giving geometric smoothness under their parameter restrictions, but do not formulate the arithmetic gonality congruence. Braden and Disney-Hogg discuss classical complex Bring geometry and a split canonical quadric after changing coordinates over a field of geometric definition; their treatment expressly excludes positive-characteristic extensions. The new point here is the quadratic-residue arithmetic descent of the two degree-three pencils for the specifically defined integral elementary-symmetric model, together with a uniform degree-four upper-bound witness. A known general correspondence between rational rulings and trigonality is used, not claimed as new. Related finite-field constructions of tetragonal genus-four curves do not fix the Bring isomorphism class or give this residue dichotomy.

## Limitations
The theorem does not address the singular special fiber at characteristic five, characteristic two, or integral models that are not arithmetically isomorphic to this coefficient-marked elementary-symmetric model. Novelty is assessed against the sources inspected and discoverable mathematical records; unpublished computations or unindexed prior arithmetic statements may remain. The proof is mathematical and reproducible but has not received an independent external audit or validation.

## References
- G. Korchmáros, S. Lia and M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886 (first public December 20, 2021), especially the smoothness theorem for \(p\ge7\). https://arxiv.org/abs/2112.10886
- H. W. Braden and L. Disney-Hogg, *Bring's curve: old and new*, arXiv:2208.13692 (first public August 29, 2022), especially the canonical model and discussion of quadric geometry. https://arxiv.org/abs/2208.13692
