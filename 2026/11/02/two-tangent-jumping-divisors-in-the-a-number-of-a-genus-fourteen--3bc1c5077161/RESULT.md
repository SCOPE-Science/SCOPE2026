# Two tangent jumping divisors in the \(a\)-number of a genus-fourteen Artin–Schreier family

## Finding
Let \(k=\overline{\mathbb F}_5\) and, for every \((a,b)\in k^2\), let \(C_{a,b}\) be the smooth projective model of the affine Artin–Schreier curve
\[
y^5-y=x^8+b x^6+a x^4.
\]
Each curve has genus \(14\), one branch point with ramification jump \(8\), and \(5\)-rank zero. Its Jacobian \(a\)-number (the dimension of the kernel of Cartier on global differentials) is **exactly**
\[
a(C_{a,b})=\begin{cases}
10,&(a,b)=(0,0),\\
9,&(a,b)\ne(0,0)\text{ and }[a=0\text{ or }2a+b^2=0],\\
8,&a\ne0\text{ and }2a+b^2\ne0.
\end{cases}
\]
Thus the \(a\)-number jumping locus in the entire marked parameter plane consists of the line \(a=0\) and the parabola \(2a+b^2=0\); these two smooth components meet **tangentially with intersection multiplicity two** at the unique \(a\)-number-ten parameter. The above classification is geometric: it holds for every parameter in \(k^2\), not merely for rational parameters of bounded extension degree.

The involution \(\iota:(x,y)\mapsto(-x,y)\) has genus-six quotient
\[
D_{a,b}:\quad y^5-y=z^4+bz^3+az^2,\qquad z=x^2.
\]
Its \(a\)-number is always \(4\). The associated eight-dimensional Prym factor has \(a\)-number respectively \(6,5,4\) on the three strata above. For \(q=5^r\), the number of **ordered, coefficient-marked** parameter pairs over \(\mathbb F_q\) with \(a\)-numbers \(10,9,8\) is respectively \(1,2(q-1),(q-1)^2\).

## Assumptions and scope
All coefficients are in characteristic \(5\). The parameter plane is the space of equations with the displayed normalized leading coefficient and absent lower odd powers; it is **not** claimed to parameterize geometric isomorphism classes injectively. Since the pole order of the right side is \(8\), prime to \(5\), every pair \((a,b)\) gives a connected, smooth projective Artin–Schreier curve. The genus formula gives \(g=(5-1)(8-1)/2=14\), while the Deuring–Shafarevich formula gives \(5\)-rank zero. The quotient under the tame involution has pole order \(4\), hence genus \(6\).

Write \(\omega_{ij}=x^iy^jdx\) and denote the Cartier operator by \(\mathcal C\), with \(\mathcal C(h^5\eta)=h\mathcal C(\eta)\). Introduce unique fifth roots \(A=a^{1/5}\) and \(B=b^{1/5}\) in the perfect field \(k\). All equalities of coefficients below are in characteristic \(5\).

## Proof
At the sole point over infinity, \(v_\infty(x)=-5\), \(v_\infty(y)=-8\), and \(v_\infty(dx)=26\). Accordingly a full \(14\)-element basis of global regular differentials is
\[
\mathcal B=\{\omega_{ij}:j\in\{0,1,2,3\},\;0\le i\le\lfloor(26-8j)/5\rfloor\}.
\]
For clarity the successive allowed \(i\)-ranges at \(j=0,1,2,3\) are \(0\ldots5\), \(0\ldots3\), \(0\ldots2\), and \(0\), respectively. One can verify the basis either from the Weierstrass semigroup at infinity or by the regularity of these differentials and the genus count.

Put \(f(x)=x^8+bx^6+ax^4\). The Artin–Schreier relation \(y^5=y+f(x)\) and \(\mathcal C(h^5\eta)=h\mathcal C(\eta)\) imply
\[
\mathcal C(x^iy^jdx)=\sum_{s=0}^j(-1)^{j-s}\binom js y^s\,\mathcal C_{\mathbb P^1}(x^if(x)^{j-s}dx),
\]
where \(\mathcal C_{\mathbb P^1}(x^Ndx)\) is zero unless \(N\equiv4\pmod5\), in which case it is \(x^{(N-4)/5}dx\); coefficients are taken to their fifth roots. Expanding only powers \(j\le3\) gives the **complete list of nonzero basis images**:
\[
\begin{aligned}
\mathcal C(\omega_{4,0})&=\omega_{0,0},&
\mathcal C(\omega_{0,1})&=-A\omega_{0,0},\\
\mathcal C(\omega_{1,1})&=-\omega_{1,0},&
\mathcal C(\omega_{3,1})&=-B\omega_{1,0},\\
\mathcal C(\omega_{0,2})&=2B\omega_{2,0}-2A\omega_{0,1},&
\mathcal C(\omega_{1,2})&=A^2\omega_{1,0}-2\omega_{1,1},\\
\mathcal C(\omega_{2,2})&=(2A+B^2)\omega_{2,0},&
\mathcal C(\omega_{0,3})&=2A^2B\omega_{2,0}-\omega_{4,0}+B\omega_{2,1}+2A\omega_{0,2}.
\end{aligned}
\]
All other basis images vanish identically. In particular, images of \(\omega_{4,0},\omega_{1,1},\omega_{1,2},\omega_{0,3}\) give four independent constant pivots, with pivot rows \(\omega_{0,0},\omega_{1,0},\omega_{1,1},\omega_{4,0}\). The only possible additional rank comes from the images of \(\omega_{0,2}\) and \(\omega_{2,2}\) on the two complementary rows \(\omega_{2,0}\) and \(\omega_{0,1}\), represented by
\[
M(A,B)=\begin{pmatrix}2B&2A+B^2\\-2A&0\end{pmatrix},
\qquad \det M=2A(2A+B^2).
\]
When \(A=B=0\), \(M=0\). At every other point of either divisor \(A=0\) or \(2A+B^2=0\), \(M\) has rank one: on the first component the right column is nonzero if \(B\ne0\); on the second with \(A\ne0\), its lower-left entry is nonzero. Outside their union its determinant is nonzero. Since the fifth-power map is an automorphism of \(k\), \(A=0\iff a=0\) and \(2A+B^2=0\iff2a+b^2=0\). Thus the three Cartier ranks are \(4,5,6\), and the three \(a\)-numbers are \(14-4=10\), \(14-5=9\), and \(14-6=8\), as claimed.

The divisors \(a=0\) and \(2a+b^2=0\) are smooth and meet only at the origin. Their local intersection length is
\[
\dim_k k[[a,b]]/(a,2a+b^2)=\dim_k k[[b]]/(b^2)=2,
\]
so the meeting is tangent, not transverse.

For the involution, \(\iota^*(x^iy^jdx)=(-1)^{i+1}x^iy^jdx\), so the \(+1\)-eigenspace has exactly six basis differentials, namely those with odd \(i\). Its Cartier images are spanned by the three columns \(\omega_{1,1},\omega_{3,1},\omega_{1,2}\), of which the first and third are independent and the middle is dependent. Its Cartier rank is constantly \(2\). These six invariant differentials are the pullbacks of differentials on \(D_{a,b}\), so \(a(D_{a,b})=6-2=4\). Since the involution has order \(2\), prime to the characteristic \(5\), its Jacobian decomposition up to an isogeny of degree prime to \(5\) respects the \(5\)-torsion group scheme, including its \(a\)-number. Hence the eight-dimensional anti-invariant Prym factor has \(a\)-number \(a(C_{a,b})-4\), as stated.

Finally, each divisor contains \(q\) rational points, and the two divisors have only the rational origin in common. Their nonorigin union has \(2q-2\) points and the complement has \(q^2-(2q-1)=(q-1)^2\) points. This proves the rational parameter census for all \(q=5^r\).

## Verification
The self-contained program `verify_symbolic.py` implements polynomial arithmetic over \(\mathbb F_5[A,B]\), reconstructs all \(14\) Cartier columns directly from \(y^5=y+f(x)\), checks their equality to the complete displayed list, and checks the residual determinant and involution eigenspace. It prints `SYMBOLIC_CARTIER_AND_PRYM_OK`.

The distinct program `verify_fields.py` works directly over \(\mathbb F_5\) and \(\mathbb F_{25}\), regenerates the Cartier columns from polynomial products and computes ranks for every marked parameter, including the quotient eigenspace. It reports `GF5_ALL_25_CARTIER_OK` and `GF25_ALL_625_CARTIER_AND_QUOTIENT_OK`. Those finite tests provide checks; **the unrestricted geometric classification follows from the symbolic matrix and its factorization, not from finite enumeration**. Run both using standard Python 3, without third-party dependencies.

## Relationship to prior work
Booher and Cais (arXiv:1807.10313; public July 26, 2018) established ramification-dependent bounds for the \(a\)-numbers of Artin–Schreier covers. Their Example 7.3 already gives a complete jumping equation for a **different genus-four, pole-order-three** two-parameter family; the general existence of such jumping phenomena is therefore not new here. Abney-McPeek and collaborators (arXiv:2003.09028; public March 19, 2020) established existence of minimum-\(a\)-number covers in characteristic five and provided explicit binomial and trinomial examples, including degree-eight minimal examples. **These prior existence and example results are not newly claimed here.** Groen (arXiv:2208.06504; public August 12, 2022) gave bounds for higher Cartier kernels. The present statement instead computes **every geometric parameter** in one natural two-dimensional deformation, identifies a tangential jumping divisor with its unique deeper point, and relates the decomposition to an invariant genus-six quotient. None of the cited results, including the full text of the characteristic-five trinomial section, supplies this exact two-parameter classification or an equivalent implication.

## Limitations
The result concerns the given normalized, coefficient-marked family and its fixed characteristic, not a complete moduli classification of all genus-fourteen Artin–Schreier covers or of Jacobians up to isomorphism. It does not determine Ekedahl–Oort types beyond the reported invariants. Published unindexed specialization calculations might overlap the result and should be checked independently. The finite-field computations are not a substitute for the general Cartier proof. There has been no independent external mathematical audit or validation.

## References
- Jeremy Booher and Bryden Cais, *a-Numbers of Curves in Artin-Schreier Covers*, arXiv:1807.10313 (first public July 26, 2018), https://arxiv.org/abs/1807.10313.
- Fiona Abney-McPeek, Hugo Berg, Jeremy Booher, et al., *Realizing Artin-Schreier Covers with Minimal a-numbers in Positive Characteristic*, arXiv:2003.09028 (first public March 19, 2020), https://arxiv.org/abs/2003.09028; specifically Sections 6–7 and the degree-eight examples.
- Steven R. Groen, *Powers of the Cartier operator on Artin-Schreier covers*, arXiv:2208.06504 (first public August 12, 2022), https://arxiv.org/abs/2208.06504.
