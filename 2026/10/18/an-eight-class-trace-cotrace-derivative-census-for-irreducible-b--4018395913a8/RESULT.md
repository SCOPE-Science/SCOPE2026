# An eight-class trace–cotrace–derivative census for irreducible binary polynomials
## Finding
For every integer \(n\ge2\), write a monic irreducible polynomial over \(\mathbb F_2\) as
\[
f(X)=X^n+\sum_{j=1}^{n-1}f_jX^j+1.
\]
Let \(I_n(a,b,c)\) count such polynomials with the three specified bits
\[
(f_{n-1},f_1,f'(1))=(a,b,c)\in\mathbb F_2^3.
\]
The third bit is the parity of the coefficients of the odd powers of \(X\), including the leading term if \(n\) is odd. The first two bits are the trace and reciprocal trace of a root; the third is a genuinely additional coefficient constraint.

Here is an exact all-degree formula. Define two integer sequences by
\[
K_0=-2,\quad K_1=1,\qquad K_n=-K_{n-1}-2K_{n-2}\quad(n\ge2),
\]
\[
H_1=H_3=0,\quad H_2=-2,\quad H_4=14,\qquad
H_n=H_{n-2}-4H_{n-4}\quad(n\ge5).
\]
For \(u,v,w\in\{0,1\}\), put
\[
J_n(u,v,w)=
\begin{cases}
2^n-2,&u+v+w=0,\\
-1-(-1)^n,&u+v+w=1,\\
(-1)^n(K_n-1),&(u,v,w)=(1,0,1),\\
K_n-1,&u+v+w=2,\ (u,v,w)\ne(1,0,1),\\
H_n,&(u,v,w)=(1,1,1).
\end{cases}
\]
Define
\[
U_d(a,b,c)=\frac18\sum_{u,v,w\in\{0,1\}}
(-1)^{au+bv+cw}J_d(u,v,w).
\]
Then, for every \(n\ge2\),
\[
\boxed{I_n(a,b,c)=\frac1n\sum_{d\mid n}\mu(n/d)
\begin{cases}
U_d(a,b,c),&n/d\ \text{odd},\\
(2^d-2)\,\mathbf1_{(a,b,c)=(0,0,0)},&n/d\ \text{even}.
\end{cases}}
\]
The expression is an integer, and its eight values sum to the usual number of monic irreducible degree-\(n\) polynomials.

Moreover, the sharp simultaneous-attainability threshold is
\[
\boxed{I_n(a,b,c)>0\text{ for all }(a,b,c)\in\mathbb F_2^3
\quad\Longleftrightarrow\quad n\ge7.}
\]
For \(n=2,3,4,5,6\), the eight count vectors, in lexicographic bit order, are respectively
\[
(0,0,0,0,0,0,0,1),\ (0,0,1,0,0,1,0,0),\
(0,0,0,1,0,1,1,0),\ (1,1,0,1,1,0,1,1),\
(0,1,1,2,1,2,2,0).
\]
For \(n=7,8,9\), they are
\[
(2,2,3,2,2,3,2,2),\ (3,4,4,3,4,3,3,6),\ (7,7,7,7,7,7,7,7).
\]

## Assumptions and scope
All fields are finite extensions of \(\mathbb F_2\). Traces are absolute traces to \(\mathbb F_2\); \(f'(X)\) is the formal derivative. The theorem is for every integer degree \(n\ge2\), every one of the eight triples, and all monic irreducibles of that degree. The two recurrence formulas are integral and determine counts without enumerating polynomials of degree \(n\). The proof does not address higher-order jets or arbitrary collections of coefficient constraints.

## Proof
**1. Three root traces.** If \(f\) is irreducible of degree \(n\ge2\) and \(\alpha\in\mathbb F_{2^n}\) is one of its roots, its conjugates are \(\alpha^{2^j}\), and \(\alpha\ne0,1\). Expanding coefficients and the logarithmic derivative gives
\[
f_{n-1}=\operatorname{Tr}(\alpha),\quad
f_1=\operatorname{Tr}(\alpha^{-1}),\quad
f'(1)=\operatorname{Tr}((\alpha+1)^{-1}).
\]
The last equality uses \(f(1)=1\), since a degree-at-least-two irreducible cannot vanish at \(1\).

**2. Walsh sums on the punctured line.** On \(\mathbb F_{2^d}\setminus\{0,1\}\), let \(\chi(z)=(-1)^{\operatorname{Tr}(z)}\) and
\[
J_d(u,v,w)=\sum_{z\ne0,1}\chi\bigl(uz+v/z+w/(z+1)\bigr).
\]
Fourier inversion on \(\mathbb F_2^3\) makes \(U_d(a,b,c)\) the number of elements in the punctured line having the indicated three traces. With one nonzero parameter, the full-field character sum is zero and the two removed values contribute \(1+(-1)^d\), giving \(-1-(-1)^d\). In the three two-parameter cases, substitutions \(z\mapsto z^{-1}\), \(z\mapsto z+1\), and \(z\mapsto1+z^{-1}\), together with the excluded-point correction, reduce the sum to \(K_d-1\). The \((u,w)=(1,1)\) case gains the character factor \((-1)^d\).

**3. The elliptic two-trace sum.** Define
\[
K_d=\sum_{z\in\mathbb F_{2^d}^{\times}}\chi(z+z^{-1}).
\]
By counting points of the nonsingular elliptic curve \(y^2+xy=x^3+x\), one gets \(\#E(\mathbb F_{2^d})=2^d+1+K_d\). Direct counting over \(\mathbb F_2\) gives four points. Its Frobenius characteristic polynomial is therefore \(T^2+T+2\), and the Weil trace formula gives \(K_0=-2\), \(K_1=1\), and \(K_d=-K_{d-1}-2K_{d-2}\). In particular \(|K_d|\le2\cdot2^{d/2}\).

**4. The three-trace genus-two sum.** The triple character is
\[
H_d=\sum_{z\ne0,1}\chi\bigl(z+z^{-1}+(z+1)^{-1}\bigr).
\]
Consider the smooth projective Artin–Schreier curve
\[
C:\quad y^2+y=x+x^{-1}+(x+1)^{-1}.
\]
Its three simple poles are at \(0,1,\infty\). The Artin–Schreier ramification genus formula gives genus \(2\), and there is one rational place above each pole. Consequently \(\#C(\mathbb F_{2^d})=2^d+1+H_d\). Direct evaluation gives \(H_1=0\) and \(H_2=-2\); specifically, over \(\mathbb F_4\) the two nonzero nonunit elements both contribute \(-1\). Thus the curve has \(3\) points over \(\mathbb F_2\) and \(7\) over \(\mathbb F_4\). The reciprocal-root symmetries of a genus-two curve over \(\mathbb F_2\) make its zeta numerator
\[
P_C(T)=1-T^2+4T^4.
\]
The Newton identities give \(H_3=0\), \(H_4=14\) and \(H_d=H_{d-2}-4H_{d-4}\) for \(d\ge5\). Weil bounds give \(|H_d|\le4\cdot2^{d/2}\). This completes all eight cases of \(J_d\).

**5. Primitive-degree extraction.** Every element of \(\mathbb F_{2^n}\setminus\{0,1\}\) has a unique minimal subfield \(\mathbb F_{2^d}\) with \(d\mid n\). Write \(h=n/d\). Restricting any absolute trace from \(\mathbb F_{2^n}\) to \(\mathbb F_{2^d}\) multiplies it by \(h\) modulo \(2\). When \(h\) is odd, the triple is preserved; when \(h\) is even, all three traces are zero. Möbius inversion on the subfield lattice therefore isolates the elements of exact degree \(n\) with specified traces as the displayed divisor sum. Every irreducible polynomial corresponds to exactly \(n\) such conjugate roots, proving the formula for \(I_n\).

**6. Sharp positivity.** The explicit recurrence formula, or the standalone exact checker, gives the finite count vectors through degree \(9\). For degree \(n\ge10\), the Walsh formula and the above Weil bounds give uniformly in \((a,b,c)\):
\[
U_n(a,b,c)\ge\frac{2^n-11-10\cdot2^{n/2}}8.
\]
The union of proper subfields of \(\mathbb F_{2^n}\) has at most \(\sum_{j=1}^{\lfloor n/2\rfloor}2^j<2^{n/2+1}\) elements. Hence the exact-degree-\(n\) count is at least
\[
\frac{2^n-11-26\cdot2^{n/2}}8>0\qquad(n\ge10).
\]
The inequality holds at \(n=10\) and remains true thereafter because its positive quadratic term grows faster than the linear root term. All eight triples occur in degrees \(7,8,9\); at least one is missing in each degree \(2\le n\le6\). The threshold is sharp.

## Verification
The included self-contained `checker.py` uses exact integer polynomial arithmetic and standard binary irreducibility testing to enumerate irreducibles independently for degrees \(2\) through \(15\), and checks every one of the eight closed-form counts. It separately enumerates the two character sums over explicitly represented finite fields for degrees \(2\) through \(10\). It reports `VERIFY_OK` on passing all assertions. These finite checks support, but do not replace, the proof for all degrees.

## Relationship to prior work
Moisio (2007) connects Kloosterman sums, elliptic curves and prescribed coefficients, furnishing classical background for the two-trace character-sum ingredient. Tuxanidy and Wang (2016) study occurrence of a single prescribed subset-coefficient sum rather than the joint distribution of three traces. Granger (2023) studies trace–cotrace counts and uses an interior-coefficient parity **signature** in bijective proofs; that signature is closely related to \(f'(1)\). However its stated enumerations are of the two-variable trace–cotrace margins, not the full eight joint \((f_{n-1},f_1,f'(1))\) counts, and do not state the genus-two recurrence or the sharp threshold at \(7\). Gao, Kuttner and Wang (2021) enumerate prescribed finite leading and trailing coefficient blocks; arbitrary middle odd-position parity is not fixed by a bounded block at either end. These results are consistent with, but do not directly state or imply, the present full joint census.

## Limitations
The results give the exact joint census for this particular three-trace choice over the binary field, not for larger fields or arbitrary trace sets. The proof uses standard Artin–Schreier ramification and Weil zeta theorems. Available comparison material does not rule out an equivalent census under a different formulation; especially, the earlier trace–cotrace signature bijections leave a residual priority risk. No external independent review has been completed.

## References
- M. Moisio, “Kloosterman sums, elliptic curves, and irreducible polynomials with prescribed trace and norm,” 2007, arXiv:0706.2112.
- A. Tuxanidy and Q. Wang, “Irreducible polynomials with prescribed sums of coefficients,” 2016, arXiv:1605.00351.
- R. Granger, “Three Proofs of an Observation on Irreducible Polynomials over GF(2),” 2023, arXiv:2302.11932.
- Z. Gao, B. Kuttner and Q. Wang, “Counting irreducible polynomials with prescribed coefficients over a finite field,” 2021, arXiv:2109.02000.
