# A sixteen-point zero-\(7\)-rank locus in a genus-ten cyclic-cover family

## Finding
Let \(k\) be an algebraically closed field of characteristic \(7\), and write \(C_u\) for the smooth projective model of
\[
 y^5=x^6+ux^3+1, \qquad u\in k,\quad u^2\ne4.
\]
Every \(C_u\) has genus \(10\). Its Jacobian has \(a\)-number \(3\) for every permitted parameter. Put
\[
 Q(U)=(3U^2-2)(U^{14}+2)-4U^8
 =3U^{16}-2U^{14}+3U^8-U^2+3\in\mathbb F_7[U].
\]
The precise \(7\)-rank dichotomy is
\[
 f_7(C_u)=\begin{cases}0,&Q(u)=0,\\4,&Q(u)\ne0.\end{cases}
\]
The exceptional polynomial has precisely sixteen distinct geometric roots, none singular for this family. Over \(\mathbb F_7\), these roots form four Frobenius orbits of lengths \(3,3,4,6\). Thus no intermediate \(7\)-rank occurs in the family, despite constant nonordinary \(a\)-number.

## Assumptions and scope
All invariants are geometric: \(f_7\) is the dimension of the \(\mathbb F_7\)-vector space of geometric \(7\)-torsion points of the Jacobian; \(a=\dim_k\ker\mathcal C\), with \(\mathcal C\) the Cartier operator on regular differentials. The claim concerns the stated one-parameter family, not all genus-ten curves or all cyclic degree-five covers. Coefficients and displayed polynomial identities are reduced modulo \(7\). The polynomial \(x^6+ux^3+1\) has a repeated root precisely when \(u^2=4\): its derivative is \(6x^5+3ux^2=3x^2(2x^3+u)\), and the common nonzero root condition is \(u^2=4\). As \(\gcd(5,6)=1\), the smooth Kummer cover has genus \((5-1)(6-1)/2=10\), one point above infinity, and a degree-five cyclic automorphism. The substitution \(x\mapsto\zeta_3x\) supplies a commuting order-three symmetry.

## Proof
**Regular differentials and the Cartier matrix.** The following ten forms form a basis of regular differentials:
\[
 \omega_{j,i}=x^i\,dx/y^j,
 \qquad 1\le j\le4,\quad0\le i<\lfloor6j/5\rfloor.
\]
For \(j=1,2,3,4\), the respective numbers of basis vectors are \(1,2,3,4\). Write \(J\in\{1,2,3,4\}\) for the unique integer satisfying \(7J\equiv j\pmod5\), and \(m=(7J-j)/5\). The \(7\)th power of the coefficient of \(\omega_{J,I}\) in \(\mathcal C(\omega_{j,i})\) equals
\[
 [x^{7(I+1)-1-i}](x^6+ux^3+1)^m.
\]
This follows directly by substituting \(y^{7J-j}=(x^6+ux^3+1)^m\), applying the standard Cartier rule \(\mathcal C(\sum_{n\ge0} b_n^7x^{7n+6}dx)=\sum_{n\ge0}b_n x^n dx\) to terms with exponents congruent to \(6\) modulo \(7\), and taking coefficient roots in the perfect field \(k\). The source-to-target character blocks cycle as \(2\to1\to3\to4\to2\).

The complete nonzero coefficient table for the entrywise seventh power of the Cartier matrix is:

| Source \((j,i)\) | Target \((J,I)\) | Entry in \(\mathbb F_7[u]\) |
|---|---|---|
| \((2,0)\) | \((1,0)\) | \(1\) |
| \((1,0)\) | \((3,0)\) | \(4-u^2\) |
| \((3,0)\) | \((4,0)\) | \(3u^2-2\) |
| \((3,0)\) | \((4,3)\) | \(-2u\) |
| \((3,1)\) | \((4,1)\) | \(-2(u^2-4)^2\) |
| \((3,2)\) | \((4,2)\) | \(-2(u^2-4)^2\) |
| \((4,0)\) | \((2,0)\) | \(u^2+2\) |
| \((4,3)\) | \((2,0)\) | \(2u\) |
| \((4,1)\) | \((2,1)\) | \(1\) |

The four character blocks have respective ranks \(1,1,3,2\) on the smooth parameter locus. Indeed, \(4-u^2\) and \(-2(u^2-4)^2\) do not vanish there; the vector \((3u^2-2,-2u)\) is never zero. Thus \(\operatorname{rank}\mathcal C=7\), so \(a(C_u)=10-7=3\) for every smooth member.

**Stable rank.** Besides the principal cycle \((2,0)\to(1,0)\to(3,0)\to\operatorname{span}\{(4,0),(4,3)\}\to(2,0)\), the only nonzero directed paths are \((3,1)\to(4,1)\to(2,1)\to0\) and \((3,2)\to(4,2)\to0\). These paths die under iteration, and the principal cycle has at most one surviving dimension in each of the four character blocks. For the principal four-step cycle, the key two-arrow contraction is
\[
 (3u^2-2)(u^2+2)^7+(-2u)(2u)^7
 =(3u^2-2)(u^{14}+2)-4u^8=Q(u).
\]
More precisely, the coefficient of \(\omega_{3,0}\) in \(\mathcal C^4(\omega_{3,0})\), raised to the \(7^4\)th power, is
\[
 (4-u^2)^{343}Q(u).
\]
This follows from Frobenius semilinearity: the two branches through \((4,0)\) and \((4,3)\) contribute the two summands above, and the arrows through \((2,0)\) and \((1,0)\) contribute the invertible factor. As \(u^2\ne4\), the stable Cartier image has dimension four exactly when \(Q(u)\ne0\), and zero when \(Q(u)=0\). Cartier stable rank equals the Jacobian \(7\)-rank, giving the dichotomy. In particular, the nine nonzero entries alone do not yield the \(7\)-rank: the semilinear iterates are essential.

**The exceptional scheme.** Exact factorization gives
\[
 Q(U)=3(U^3+U+1)(U^3+U-1)(U^4-U^2+3)
 (U^6+3U^4+2U^2+2).
\]
Each factor is irreducible over \(\mathbb F_7\), of respective degrees \(3,3,4,6\); equivalently, each passes the irreducibility tests in `verify_cartier.py`. Direct exact polynomial gcd checks give \(\gcd(Q,Q')=\gcd(Q,U^2-4)=1\). Therefore the sixteen roots are distinct, all smooth parameters, with the stated Frobenius orbit structure. This proves the claim for every parameter in \(k\), rather than just finite-field test values.

## Verification
Run `python3 verify_cartier.py` with Python 3 and SymPy, and `python3 verify_field_rank.py` using Python 3 alone. The first program reconstructs the entire ten-by-ten Cartier coefficient matrix from integer multinomial coefficients, checks all polynomial identities, rank arguments over \(\mathbb F_7\), squarefreeness, and factor degrees. The second separately constructs the matrix by polynomial multiplication and tests the stable Frobenius-twisted rank over explicit extension fields of degrees \(3,3,4,6\), on each exceptional parameter and on a shifted nonexceptional control. It also checks all smooth parameters over \(\mathbb F_7\). The observed outputs are `CARTIER_SYMBOLIC_OK` and `EXTENSION_RANK_OK`. These finite computations corroborate the algebraic proof; they are not substituted for the general parameter argument.

## Relationship to prior work
Borges and Gonçalves (2022) study the \(p\)-rank of Fermat-type curves \(y^m=x^n+1\); the parameter \(u=0\) here is such a member. Hase-Liu (2016) provides general superelliptic Hasse–Witt formulas and point-counting algorithms, including multinomial expansions, but not the displayed geometric stratification or sixteen-root exceptional polynomial. Ohashi, Kudo and Harashita (2021) investigate \(a\)-numbers in a distinct genus-three cyclic-automorphism family and provide methodological context. The new assertion is the parameter-uniform, genus-ten simultaneous \(a\)-number/\(7\)-rank classification and the exact exceptional Frobenius degrees, not the general Cartier formula or any result about the unperturbed Fermat curve alone.

## Limitations
The result is confined to characteristic seven and the displayed smooth one-parameter family. It gives no global classification of isomorphism classes of \(C_u\), no Newton polygon, Ekedahl–Oort type, or zeta functions, and does not assert that the sixteen distinct parameter values represent sixteen distinct geometric isomorphism classes. The originality comparison cannot exclude unpublished or unindexed prior calculations. The scientific review is not independent external validation.

## References
- H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987v1 (first submitted 2022-12-07), https://arxiv.org/abs/2212.03987 .
- M. Hase-Liu, *Efficient Point-Counting Algorithms for Superelliptic Curves* (2016), https://math.mit.edu/research/highschool/primes/materials/2016/Hase-Liu.pdf .
- E. Ohashi, M. Kudo and S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777, https://arxiv.org/abs/2111.09777 .
