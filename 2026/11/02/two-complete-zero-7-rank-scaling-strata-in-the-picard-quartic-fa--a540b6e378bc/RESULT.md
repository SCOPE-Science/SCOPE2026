# Two complete zero-\(7\)-rank scaling strata in the Picard quartic family

## Finding

Let \(k\) be an algebraically closed field of characteristic \(7\). Among all smooth Picard curves in the centered monic three-parameter family
\[
C_{a,b,c}:\quad y^3=x^4+a x^2+b x+c,
\]
the Jacobian has \(7\)-rank zero **if and only if**
\[
a=0,\qquad c(c^3-2b^4)=0,\qquad b\ne0.
\]
The corresponding smooth parameter locus has exactly two connected irreducible components \(a=c=0,b\ne0\) and \(a=0,c^3=2b^4,b\ne0\) (the second is irreducible over \(k\)); each is one orbit under the natural weighted coordinate scalings. In the first orbit one can take \((a,b,c)=(0,1,0)\); in the second, \((0,1,\rho)\) for any \(\rho\in k\) satisfying \(\rho^3=2\). Both have Jacobian \(a\)-number \(2\), and neither is superspecial.

In fact, the entire smooth family has only two possible Cartier ranks: \(1\) on \(a=0\), with \(a\)-number \(2\), and \(3\) on \(a\ne0\), with \(a\)-number \(0\). Thus every smooth member with \(a\ne0\) is ordinary, and no smooth member has \(a\)-number \(1\) or \(7\)-rank \(2\).

## Assumptions and scope

All coefficients are in \(k\), and the right-hand quartic is squarefree. This is equivalent to the discriminant condition
\[
\Delta=2a^4c+3a^3b^2-2a^2c^2-3ab^2c+b^4-3c^3\ne0,
\]
with coefficients read in characteristic \(7\). The smooth projective curve is genus \(3\) since it is a cyclic degree-three cover of \(\mathbb P^1\) branched at four finite roots and infinity. The claimed orbit classification concerns **marked weighted-scaling classes** of normalized equations, not an asserted complete classification under all possible unmarked geometric isomorphisms.

## Proof

A basis of regular differentials is
\[
\omega_0=dx/y,\qquad \omega_1=dx/y^2,\qquad \omega_2=x\,dx/y^2.
\]
For \(p=7\), the identity \(y^{-j}=f(x)^{2j} y^{-7j}\), where \(f(x)=x^4+ax^2+bx+c\), gives the coefficient-form Cartier matrix, obtained by raising the actual Cartier entries to the seventh power:
\[
H=\begin{pmatrix}2a&0&0\\0&B_{11}&B_{12}\\0&B_{21}&B_{22}\end{pmatrix},\quad
B=\begin{pmatrix}
-3a^3c-a^2b^2-2ac^2-2b^2c&-2a^2bc-3ab^3-2bc^2\\
-3b&-a^2-3c
\end{pmatrix}.
\]
Indeed the scalar is the coefficient of \(x^6\) in \(f^2\); the displayed \(2\)-by-\(2\) block consists of coefficients of \(x^6,x^5,x^{13},x^{12}\) in \(f^4\), respectively. Direct polynomial multiplication gives \(\det B=aR\), where \(R=3a^4c+a^3b^2-3a^2c^2-ab^2c-2b^4-c^3\), and, crucially, \(\Delta=3R\) in characteristic seven.

For a smooth parameter triple, \(B\) never has rank zero. If \(B=0\), its bottom left entry forces \(b=0\), and its bottom right entry forces \(c=2a^2\). Substituting into \(\Delta\) gives \(0\). Since \(\Delta=3R\), smoothness forces \(R\ne0\). Hence \(a\ne0\) gives invertible Cartier matrix and an ordinary Jacobian of \(7\)-rank \(3\). On \(a=0\), Cartier has rank \(1\). As the \(a\)-number equals three minus Cartier rank, the only smooth \(a\)-numbers are \(0\) and \(2\); in particular rank two is excluded entirely.

The direct summand acted upon by the Cartier coefficient \(2a\) contributes a nonzero stable Frobenius direction whenever \(a\ne0\). Hence \(7\)-rank zero forces \(a=0\). On \(a=0\), the remaining matrix factors as
\[
B=uv,\qquad u=\begin{pmatrix}-2bc\\-3\end{pmatrix},\quad v=\begin{pmatrix}b&c\end{pmatrix}.
\]
For the semilinear Cartier operator, composition twice has vanishing coefficient matrix if and only if \(B^{(7)}B=0\), where \(B^{(7)}\) denotes entrywise seventh powers. Since \(B^{(7)}B=u^{(7)}(v^{(7)}u)v\), its scalar factor is
\[
v^{(7)}u=-2b^8c-3c^7=-3c(c^3-2b^4)(c^3+2b^4).
\]
On \(a=0\), the discriminant simplifies to
\[
\Delta=-3(c^3+2b^4),
\]
so the last factor is nonzero by smoothness. Thus Cartier is eventually zero exactly when \(c(c^3-2b^4)=0\). If this scalar is nonzero, every further twisted composition is nonzero on the one-dimensional stable image; the \(7\)-rank is then \(1\). If zero, Cartier squared is zero on the two-dimensional block and the one-dimensional block vanishes, yielding \(7\)-rank \(0\).

Smoothness in either zero-rank branch forces \(b\ne0\). On the branch \(c^3=2b^4\), the discriminant is \(2b^4\ne0\). The coordinate change \(x\mapsto tx\), together with the compatible rescaling of \(y\), changes the coefficients to \((a/t^2,b/t^3,c/t^4)\); over algebraically closed \(k\), this is an isomorphism for each \(t\ne0\). Choosing \(t^3=b\) normalizes \(b\) to \(1\); the remaining cube-root-of-unity freedom acts transitively on the three solutions \(c^3=2\). The two cases \(c=0\) and \(c\ne0\) are distinct under these scalings. Both lie in the rank-one Cartier divisor, so their \(a\)-numbers are \(2\), not \(3\).

## Verification

Run `python verify_picard7.py` with Python \(3\) and `sympy==1.14.0`. The script independently multiplies the defining polynomial using symbolic powers and a sparse combinatorial convolution, compares all entries of the Cartier matrix, checks \(\Delta=3R\), \(\det B=aR\), the rank-one factorization and the twisted-composition scalar, then exhausts all \(343\) rational coefficient triples over \(\mathbb F_7\). This final finite enumeration tests only examples; the polynomial identities and the rank-one semilinear argument prove the statements over the entire algebraic closure.

## Relationship to prior work

The classical Picard quartic \(y^3=x^4-x\) belongs to the first zero-rank branch; it was explicitly studied by Lario and Somoza. Kazemifard and Tafazolian determined Newton polygons for such highly symmetric Picard curves, including \(y^3=x^4-x\). Sutherland's general superelliptic Cartier coefficient formula applies to the entire ambient family; it supplies the method for computing entries, but does not state the explicit two-component rank-zero classification or the full coefficientwise ordinary/nonordinary partition derived above. Bouw, Koutsianas, Sijsling and Wewers study Picard normal forms and arithmetic conductor questions rather than this characteristic-seven stable-rank locus. These distinctions are between the actual mathematical conclusions, not titles. Published priority for the exact result is not independently established.

## Limitations

This result is a classification in a specified centered monic coefficient space and under its natural weighted scalings; it does not classify all abstract genus-three curves, their complete Newton polygons or Ekedahl–Oort types, nor claim that the two orbits remain distinct under every unmarked isomorphism. The relevant Picard literature is extensive; an unnoticed equivalent arithmetic-locus classification remains possible. The mathematical calculations are reproducible, but no independent audit has taken place.

## References

- J.-C. Lario and A. Somoza, *The Sato-Tate conjecture for a Picard curve with complex multiplication*, arXiv:1409.6020, submitted September 21, 2014. https://arxiv.org/abs/1409.6020
- A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields Appl. 34 (2015), 107–122. https://doi.org/10.1016/j.ffa.2014.12.002
- A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, arXiv:2004.10189, especially §2 and formula (8). https://arxiv.org/abs/2004.10189
- I. I. Bouw, A. Koutsianas, J. Sijsling and S. Wewers, *Conductor and discriminant of Picard curves*, J. Lond. Math. Soc. 102 (2020), 368–404. https://doi.org/10.1112/jlms.12323
- S. Asif, F. Fité and D. Pentland, *Computing L-polynomials of Picard curves from Cartier–Manin matrices*, arXiv:2010.07247. https://arxiv.org/abs/2010.07247
