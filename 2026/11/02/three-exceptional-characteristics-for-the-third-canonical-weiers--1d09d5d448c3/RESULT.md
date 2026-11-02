# Three exceptional characteristics for the third-canonical Weierstrass divisor of the Klein quartic

## Finding
Let \(k\) be an algebraically closed field of prime characteristic \(p\ge13\), and let \(C_p\subset\mathbb P^2_k\) be the smooth Klein quartic
\[
 F=X^3Y+Y^3Z+Z^3X=0.
\]
Write \(W_{3,p}\) for the scheme-theoretic ramification divisor of the complete linear series \(|3K_{C_p}|=|\mathcal O_{C_p}(3)|\). The tame group \(G\cong\operatorname{PSL}_2(\mathbb F_7)\) acts on \(C_p\), with three distinguished reduced orbits \(O_{24,p}\), \(O_{56,p}\), and \(O_{84,p}\), named by their cardinalities and with stabilizer orders \(7\), \(3\), and \(2\). Then
\[
 W_{3,p}=\begin{cases}
 2O_{24,p}+O_{84,p}+O_{168,p},&p\notin\{79,139,277\},\\
 2O_{24,p}+O_{84,p}+3O_{56,p},&p\in\{79,139\},\\
 2O_{24,p}+3O_{84,p},&p=277.
 \end{cases}
\]
Here \(O_{168,p}\), occurring only in the first case, is one reduced orbit with trivial stabilizer. Accordingly, the number of distinct third-canonical Weierstrass points is exactly \(276\), \(164\), or \(108\), respectively. Every displayed divisor has total degree \(300\).

## Assumptions and scope
The field is algebraically closed of characteristic \(p\ge13\). The characteristic restriction is essential to the stated proof: \(G\) is tame, the factorials through \(9!\) and the integral Wronskian normalizing scalar are invertible, and the characteristic-zero invariant-theory formulas specialize without dividing by zero. The assertion is about ramification of the *complete* \(3\)-canonical series, including its vanishing multiplicities, not about ordinary canonical flexes.

## Proof
**1. Invariants and the tame quotient.** Let \(f=F\), define
\[
 U=X^5Z+XY^5+YZ^5-5X^2Y^2Z^2,
\]
\[
 A=\frac19\det\begin{pmatrix}\operatorname{Hess}(f)&\nabla U\\(\nabla U)^T&0\end{pmatrix},\qquad
 B=\frac1{14}\det\begin{pmatrix}\nabla f\\\nabla U\\\nabla A\end{pmatrix}.
\]
Despite the displayed rational prefactors, the resulting homogeneous polynomials \(A\) and \(B\) have integer coefficients. Their degrees are \(14\) and \(21\), and direct exact polynomial division gives
\[
 B^2\equiv A^3-1728U^7\pmod{(f)}.
\]
These are Klein's classical invariants in the normalization described by Elkies. The quotient map
\[
 \pi:C_p\longrightarrow\mathbb P^1_k,\qquad \pi=A^3/U^7,
\]
has degree \(168\) for every \(p\ge13\): the Klein representation and invariant quotient spread out away from the primes dividing \(168\); the reductions of its generators remain a faithful action (the nontrivial order-seven element and simplicity of \(G\) exclude a kernel). The invariant quotient remains a \(G\)-Galois cover since \(p\nmid168\). Its three branch values are \(0,1728,\infty\), with ramification indices \(3,2,7\), respectively. The corresponding fibers are
\[
 \pi^{-1}(0)=3O_{56,p},\quad \pi^{-1}(1728)=2O_{84,p},\quad \pi^{-1}(\infty)=7O_{24,p}.
\]
In particular, \(U,A,B\) vanish simply at the appropriate reduced orbits (and there are no other branch fibers). One can alternatively use the explicit integral invariant presentation with averaging by \(|G|^{-1}\) for the base-change step. Tame Riemann–Hurwitz verifies completeness: \(56(3-1)+84(2-1)+24(7-1)=340=2(2\cdot3-2)+2\cdot168\).

**2. Integral normalization of the Wronskian.** On \(Z=1\), choose the ten cubic sections ordered
\[
 (1,x,y,x^2,xy,y^2,x^3,x^2y,xy^2,y^3).
\]
Write \(\delta=f_y\partial_x-f_x\partial_y\), and \(\Omega=\det(\delta^i s_j)_{0\le i,j\le9}\). Nawara's characteristic-zero computation gives the proportionality \(\Omega\equiv U^2B(3A^3+21962U^7)\pmod f\). The exact scalar is determined over the integers at \((x,y)=(0,0)\). In the local parameter \(t=y\), the curve equation gives \(x=-t^3+t^{10}+O(t^{17})\). The first ten section orders after elimination are \(0,1,2,3,4,5,6,7,9,10\); the leading coefficient determinant for those orders is \(-1\). Its Vandermonde factor is \(82572006251298816000000\). Since \(\delta=-\partial_t\) at the point and \(\sum_{i=0}^{9}i=45\), the leading term of \(\Omega\) is the positive Vandermonde times \(t^2\). The invariant product begins with \(3t^2\). Hence, with precisely this ordered basis,
\[
 \Omega\equiv c\,U^2B(3A^3+21962U^7)\pmod f,
 \qquad c=27524002083766272000000=2^{30}3^{14}5^6 7^3.
\]
Both sides have integer coefficients; because \(f\) is primitive, the equality modulo \(f\) over \(\mathbb Q\) descends to the integral polynomial quotient by Gauss's lemma. The scalar \(c\) is invertible for all \(p\ge13\). Thus the same factored Wronskian describes the complete \(3\)-canonical ramification divisor in every stated characteristic. Ordinary derivatives through order \(9\) are valid because their factorials are units.

**3. The exceptional fibers.** Off \(U=0\), the last factor is \(U^7(3\pi+21962)\), so its zero scheme is a complete quotient fiber at \(\pi=-21962/3\). The collision with \(\pi=0\) happens precisely when \(p\) divides \(21962=2\cdot79\cdot139\); the collision with \(\pi=1728\) precisely when \(p\) divides \(21962+3\cdot1728=27146=2\cdot7^2\cdot277\). Neither the residual factor nor the quotient map has a pole collision at \(\infty\), because its \(A^3\)-coefficient is the unit \(3\). For other primes this is a reduced, unramified quotient fiber, hence one orbit of \(168\) points. The two exceptional cases yield the stated multiplicities. The degree check \(48+84+168=300\) holds in every case and ensures no omitted ramification points.

## Verification
The standalone exact-arithmetic scripts `klein_invariants_verify.py`, `klein_leading_coefficient.py`, `klein_jet_check.py`, and `klein_modular_certificate.py` use Python 3 and SymPy. Run the first, second, and fourth with the files together in one directory. The first checks the homogeneous polynomial invariant identity over \(\mathbb Z\), the second proves the leading scalar and factors the exceptional integers, and the fourth compares finite-field Hasse jet determinants at five smooth points in each of the exceptional characteristics with the predicted invariant factor. All checks return `VERIFY_*_OK`. The infinite-characteristic conclusion follows from the integral identity, tame group quotient, and divisor argument above, not from this finite list of examples.

## Relationship to prior work
Nawara (2026) proves, over characteristic zero, the factorization of the third Veronese Wronskian of Klein's quartic up to unspecified scalar; she does not present the three exceptional positive-characteristic divisor profiles. Elkies (1998) develops the invariant polynomials, the group action, and the quotient branching; these are acknowledged inputs rather than new results. The additional argument is the exact integral normalization and the complete special-fiber classification of higher Weierstrass ramification at \(p=79,139,277\). Kamel and Elshareef (2019) give earlier third-order Weierstrass analysis for smooth quartics; their publisher abstract was inspected, but full text was not available, so priority relative to possible implicit modular formulas remains a risk. A stronger general theorem about positive-characteristic reductions could subsume this result even without naming these primes; none was identified in the inspected primary sources.

## Limitations
Only primes \(p\ge13\) are classified; the small characteristics may exhibit wild automorphisms or nonclassical Wronskians. Equality of the divisor does not determine higher-canonical gap sequences individually beyond their total weight. The proof relies on established characteristic-zero factorization and classical invariant-theory results, with the integral scalar and reduction argument supplied here. Full priority classification is not claimed, and independent mathematical review has not been performed.

## References
- E. Nawara, *Third-Order Weierstrass Points on Plane Quartics*, arXiv:2610.30992v1 (first public version, 2026-10-22), especially the Klein-quartic factorization: https://arxiv.org/abs/2610.30992 .
- N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1998), §§1–2, especially the invariant forms and orbit structure: https://library.slmath.org/books/Book35/files/elkies.pdf .
- A. Kamel and A. Elshareef, *Weierstrass points of order three on smooth quartic curves*, Journal of Algebra and Its Applications (2019), DOI: 10.1142/S0219498819500208; abstract consulted, complete text not inspected.
