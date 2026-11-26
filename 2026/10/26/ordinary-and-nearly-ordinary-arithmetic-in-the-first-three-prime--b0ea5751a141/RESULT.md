# The ordinary plane-filling octic in the Asgarli–Ghioca pencil over F₅

## Finding

For \(k\in\mathbb F_5\), let \(C_k\subset\mathbb P^2_{\mathbb F_5}\) be the member of the Asgarli–Ghioca pencil defined by
\[
F_k=x^2(x^5y-xy^5)+y^2(y^5z-yz^5)+(z^2+kx^2)(z^5x-zx^5)=0.
\]
The only geometrically smooth member is \(C_4\). Its Jacobian is ordinary: its genus and 5-rank are both \(21\), and its \(a\)-number is \(0\). The arithmetic assertion is witnessed by a Hasse–Witt determinant of \(4\) in \(\mathbb F_5\).

## Assumptions and scope

The result concerns just the indicated characteristic-five pencil, not other degree-eight curves or other fields. Smoothness is over an algebraic closure. Plane filling means containing all \(\mathbb F_5\)-rational points of the plane; this follows immediately from the pairwise expressions \(u^5v-uv^5\). The 5-rank is the \(\mathbb F_5\)-dimension of the group of geometric 5-torsion points of the Jacobian, and the \(a\)-number is the dimension of \(\operatorname{Hom}(\alpha_5,\operatorname{Jac}(C_4))\) over an algebraic closure.

## Proof and exact certificate

For \(k=0,1,2,3\), the rational projective points \((1:1:1),(4:2:1),(4:3:1),(1:4:1)\), respectively, make \(F_k\) and its partial derivatives vanish. For \(k=4\), set each coordinate in turn equal to 1, obtaining an affine polynomial \(f(u,v)\). In each chart the ideal \((f,\partial_u f,\partial_v f)\) has reduced Gröbner basis \(\{1\}\) over \(\mathbb F_5\), as computed by `verify.py`. The unit ideal remains unit after scalar extension, so the three charts certify geometric smoothness. The smooth degree-eight plane curve has genus \((8-1)(8-2)/2=21\) by adjunction.

The plane-divisor exact sequence identifies \(H^1(C_4,\mathcal O_{C_4})\) with \(H^2(\mathbb P^2,\mathcal O(-8))\). On the latter space the Čech basis consists of Laurent monomials \(x^{-u_1}y^{-u_2}z^{-u_3}\) for positive triples \(u\) of sum 8. Frobenius sends the basis monomial indexed by \(u\) to the class of \(F_4^4 x^{-5u_1}y^{-5u_2}z^{-5u_3}\): the fourth power of the defining equation converts the twisted degree \(-40\) back to degree \(-8\). With source indices on rows, the matrix entry \(H_{u,v}\) is therefore the coefficient of \(x^{5u_1-v_1}y^{5u_2-v_2}z^{5u_3-v_3}\) in \(F_4^4\), with zero for a negative exponent. The field is prime, so Frobenius is linear on its basis coefficients.

The exact calculation in `verify.py` expands \(F_4^4\) in \(\mathbb F_5[x,y,z]\), forms the \(21\) by \(21\) matrix with triples in lexicographic order, and obtains \(\det H=4\) by modular elimination. Thus Frobenius and all its powers are invertible. The stable Frobenius rank is the 5-rank, and the defect of the first rank is the \(a\)-number by duality with Cartier. Hence these invariants are \(21\) and \(0\), respectively.

## Relationship to prior work

Asgarli and Ghioca introduced the pencil. Their Theorem 1.2 supplies the rational-point smoothness criterion, and their reported computational check of Conjecture 1.5 covers geometric smoothness in this field. That classification is used here to specify the natural smooth octic of the pencil; it is not a claim of new smoothness coverage. The arithmetic calculation determines whether the Jacobian of that particular plane-filling octic is ordinary. The ordinarity result for the Tallini curves studied by Duran Cunha concerns degree \(p+2\), not this degree-\(p+3\) pencil. General Hasse–Witt formulas apply to the octic but do not supply its numerical determinant without computation. No pattern over other primes is asserted.

## Reproducibility

Run `python3 verify.py` (Python 3.10+ and SymPy). The script checks the four singular witnesses, the three chart ideals for \(C_4\), and the Hasse–Witt determinant over \(\mathbb F_5\). Its final line is `p=5 k=4 smooth genus=21 det=4 ordinary`.

## References

1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, [arXiv:2307.03072](https://arxiv.org/abs/2307.03072), equation (1), Theorem 1.2 and Conjecture 1.5.
2. G. Duran Cunha, *Curves containing all points of a finite projective Galois plane*, [arXiv:1805.07345](https://arxiv.org/abs/1805.07345), introduction.
3. A. Adolphson and S. Sperber, *A generalization of the Hasse-Witt matrix of a hypersurface*, [arXiv:1701.04509](https://arxiv.org/abs/1701.04509), classical hypersurface formula.
