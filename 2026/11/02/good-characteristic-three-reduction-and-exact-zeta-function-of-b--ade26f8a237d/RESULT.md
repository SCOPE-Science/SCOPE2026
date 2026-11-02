# Good characteristic-three reduction and exact zeta function of Bring’s genus-four curve

## Finding
The elementary-symmetric integral model of Bring’s genus-four curve
\[\mathcal B:\quad e_1(X_0,\dots,X_4)=e_2(X_0,\dots,X_4)=e_3(X_0,\dots,X_4)=0\subset \mathbb P^4_{\mathbb Z_{(3)}}\]
is smooth and proper over \(\mathbb Z_{(3)}\). Its characteristic-three fiber \(B\) has no \(\mathbb F_3\)-rational points, is ordinary, and satisfies
\[Z(B/\mathbb F_3,T)=\frac{(1-T+3T^2)^4}{(1-T)(1-3T)}.\]
Equivalently, for every integer \(m\ge1\), with \(\alpha,\beta\) the roots of \(U^2-U+3\),
\[\#B(\mathbb F_{3^m})=3^m+1-4(\alpha^m+\beta^m).\]

## Assumptions and scope
All geometric smoothness statements concern the algebraic closure of \(\mathbb F_3\). The integral scheme is defined over \(\mathbb Z_{(3)}\) by the genuine elementary symmetric polynomials in five variables, not the sums of first, second and third powers. Over \(\mathbb Q\), Newton identities identify the two presentations because 2 and 3 are invertible. The equations have degrees 1, 2 and 3; the smooth special fiber is therefore a genus-four complete-intersection curve of degree six. The previously established rational isogeny \(\operatorname{Jac}(\mathcal B_{\mathbb Q})\sim_{\mathbb Q}E^4\), where \(E\) belongs to the conductor-50 elliptic isogeny class, is used as a cited input.

## Proof
**Smoothness at three.** Write \(x_0,\ldots,x_4\) for a geometric point of the special fiber. The differentials of \(e_1,e_2,e_3\), after imposing \(e_1=e_2=e_3=0\), have respective coordinate entries
\[1,\qquad -x_i,\qquad x_i^2.\]
Indeed \(\partial_i e_2=e_1-x_i\) and \(\partial_i e_3=e_2-x_i(e_1-x_i)\). The first two rows are linearly independent at every projective point satisfying \(e_1=0\): dependence would force all five coordinates equal, hence \(e_1=5x_i=2x_i=0\), so the point would be zero. If the three rows were dependent, there would be coefficients \(A,B,C\), with \(C\ne0\), such that \(A+Bx_i+Cx_i^2=0\) for all five coordinates. Therefore at most two distinct coordinate values occur.

For one value, \(e_1=0\) forces every coordinate zero. For two values, rescale and interchange the values so that their multiplicities are \(r\) and \(5-r\), with \(1\le r\le4\). When \(r=1\) or \(4\), the equation \(e_1=0\) forces the two values to be opposites (or they both vanish), and \(e_2\ne0\) for the resulting nonzero pattern. When \(r=2\) or \(3\), \(e_1=0\) forces the value with multiplicity two to vanish; then the remaining three nonzero equal entries make \(e_3\ne0\). Thus no singular geometric point exists. Since the hyperplane and quadric are also transverse, the Jacobian criterion proves smoothness of the complete intersection. A relative complete intersection with smooth geometric generic and special fibers is a smooth proper genus-four model at three.

**No rational points.** Suppose five \(\mathbb F_3\) coordinates represent a point of the curve. Since \(e_1=0\), the identity \(2e_2=e_1^2-\sum_i x_i^2\) shows that the number of nonzero coordinates is divisible by three. There must be exactly three. Their sum is zero precisely when all three nonzero entries are equal; but then \(e_3\), their product, is nonzero. Hence \(\#B(\mathbb F_3)=0\).

**Zeta function.** The rational Jacobian-isogeny statement for the usual Bring curve, established in the cited literature, gives \(\operatorname{Jac}(\mathcal B_{\mathbb Q})\sim_{\mathbb Q} E^4\), with \(E\) of conductor 50. Both sides have good reduction at three. Isogeny of their prime-to-three Tate modules therefore identifies their characteristic-three Frobenius polynomials. Write \(a\) for the elliptic Frobenius trace. The rational point count of the genus-four curve gives \(\#B(\mathbb F_3)=4-4a\). As the left side is zero, \(a=1\). The zeta numerator is consequently \((1-T+3T^2)^4\), giving the claimed formula over every extension. Since \(a\) is not divisible by 3, the elliptic curve is ordinary and so is the isogenous genus-four Jacobian.

**Hasse–Witt refinement.** In the affine coordinate hyperplane \(x_4=-x_0-x_1-x_2-x_3\), let \(Q=e_2\) and \(R=e_3\). The standard complete-intersection coefficient formula for the Hasse–Witt operator on the four canonical coordinate sections extracts from \((QR)^2\) the coefficients of monomials with exponents \((2,2,2,2)+3\mathbf e_i-\mathbf e_j\). Direct exact expansion over \(\mathbb F_3\) gives \(\delta_{ij}\), hence \(I_4\). This independently checks ordinarity; the zeta derivation does not depend on this coefficient computation.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It enumerates the five-coordinate projective points over \(\mathbb F_3\) and \(\mathbb F_9\), obtaining 0 and 30 points, respectively; it also checks the complete-intersection Hasse–Witt coefficient matrix \(I_4\). The geometric proof of smoothness is algebraic and does not rely on finite enumeration. The published rational isogeny input is a mathematical premise, not rederived by the script.

## Relationship to prior work
Braden and Northover [1] present the genus-four Bring curve and its complex period geometry. Braden and Disney-Hogg [2, Proposition 4.5] establish its \(\mathbb Q\)-Jacobian isogeny class \((50a)^4\), already implicit in earlier work. Those antecedents supply the generic curve and isogeny; the assessed addition is the explicit good model at the wild prime three, its geometric smoothness proof, and the resulting complete special-fiber arithmetic. The naive power-sum presentation does **not** specialize faithfully at three: its third equation is the cube of the first, so the elementary-symmetric integral form is essential. No uniqueness claim about all possible integral models is made.

## Limitations
The rational-isogeny theorem is imported from [2], not independently proved. The model is asserted smooth at three only; no new result is claimed about other primes or the full integral minimal regular model. The literature search and historical indexing are not exhaustive; direct earlier discussions of this special fiber may exist. The Hasse–Witt matrix depends on the stated coordinate basis; ordinarity and the zeta function are intrinsic.

## References
[1] H. W. Braden and T. P. Northover, *Bring’s Curve: its Period Matrix and the Vector of Riemann Constants*, SIGMA **8** (2012), article 065; arXiv:1206.6004 (first posted 26 June 2012). https://arxiv.org/abs/1206.6004

[2] H. W. Braden and L. Disney-Hogg, *Bring’s curve: old and new*, European Journal of Mathematics **10** (2024), article 3; first published online 18 December 2023, Proposition 4.5. https://doi.org/10.1007/s40879-023-00706-0
