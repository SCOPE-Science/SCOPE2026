# Eight Weil-polynomial types in a diagonal genus-four family

## Finding
Let \(p\ge5\) be a prime with \(p\equiv5\pmod6\), and put \(q=p^2\). For each \(A,B\in\mathbf F_q^\times\), the curve
\[
 C_{A,B}:\quad X^3+A Y^3+B W^3=0,\qquad Z^2=YW
 \quad\subset\mathbf P^3_{\mathbf F_q}
\]
is geometrically smooth, nonhyperelliptic, and of genus four. Fix a primitive \(g\in\mathbf F_q^\times\), and define the **diagonal coefficient types** \(r\in\{0,\ldots,5\}\) and \(s\in\{0,1,2\}\) by
\[
A/B\in g^r(\mathbf F_q^\times)^6,\qquad B\in g^s(\mathbf F_q^\times)^3.
\]
These are exactly the eighteen classes under independent rescaling of the affine coordinates of the associated superelliptic model, not a claim of eighteen abstract isomorphism classes.

The zeta numerator \(L_{A,B}(T)\), defined by \(Z(C_{A,B},T)=L_{A,B}(T)/((1-T)(1-qT))\), has precisely **eight** possible factorization types. Set \(u=pT\), and for a signature \((a,b,c,d)\) write
\[
 \mathcal L_{a,b,c,d}(u)=(1+u)^a(1-u)^b(1+u+u^2)^c(1-u+u^2)^d.
\]
Then \(L_{A,B}(T)=\mathcal L_{a,b,c,d}(pT)\) according to this complete table:

| Signature \((a,b,c,d)\) | Coefficient types \((r,s)\) | \(\#C_{A,B}(\mathbf F_q)\) |
| --- | --- | --- |
| \((8,0,0,0)\) | \((0,0)\) | \(q+1+8p\) |
| \((0,0,0,4)\) | \((0,1),(0,2)\) | \(q+1-4p\) |
| \((0,2,2,1)\) | \((1,0),(1,2),(5,0),(5,1)\) | \(q+1-p\) |
| \((2,2,2,0)\) | \((1,1),(5,2)\) | \(q+1+2p\) |
| \((2,0,0,3)\) | \((2,0),(2,1),(4,0),(4,2)\) | \(q+1-p\) |
| \((4,0,0,2)\) | \((2,2),(4,1)\) | \(q+1+2p\) |
| \((2,6,0,0)\) | \((3,0)\) | \(q+1-4p\) |
| \((0,0,3,1)\) | \((3,1),(3,2)\) | \(q+1+2p\) |

In particular, the family has eight distinct \(\mathbf F_q\)-isogeny types of Jacobians, although only four rational-point totals. Exactly one diagonal coefficient type attains the Hasse--Weil upper bound \(q+1+8p\). The lower point total within this family, \(q+1-4p\), is attained in three coefficient types belonging to two *distinct* Weil-polynomial classes. The displayed polynomials determine all extension-field counts, not merely the number over \(\mathbf F_q\).

## Assumptions and scope
The prime must satisfy \(p\equiv5\pmod6\), so \(p\ne2,3\). Both coefficients must be nonzero. The scalar \(g\) is any generator of \(\mathbf F_q^\times\); changing it relabels the exponent table but not its eight polynomial types. All assertions are over \(\mathbf F_q\), not over arbitrary finite fields or for other canonical genus-four curves. The equivalence considered when defining the eighteen types is solely diagonal scaling of the affine superelliptic coordinates. Distinct Weil polynomials imply nonisogenous Jacobians over \(\mathbf F_q\), but repeated polynomials do not imply isomorphic curves.

## Proof
**(1) Geometry.** On \(W\ne0\), put \(t=Z/W\) and \(v=X/W\). The quadric forces \(Y/W=t^2\), so the affine model is
\[
 v^3+A t^6+B=0.
\]
Because \(AB\ne0\) and the characteristic is prime to six, the polynomial \(A t^6+B\) has six distinct geometric roots. The superelliptic cover of \(\mathbf P^1\) has degree three, is totally ramified at these six roots, and is unramified at infinity with three geometric points there. Riemann--Hurwitz gives \(2g-2=3(-2)+6(3-1)=6\), hence \(g=4\). The complete-intersection model lies away from the vertex of its rank-three quadric and is smooth there and at infinity, giving the canonical nonhyperelliptic model.

**(2) The untwisted curve is maximal.** Let \(C_0\) be \(v^3+t^6+1=0\). The degree-six Fermat curve \(U^6+T^6+W^6=0\) maps to its canonical model by
\[
 [U:T:W]\longmapsto[U^2:T^2:TW:W^2].
\]
Since \(6\mid(p+1)\), the degree-six Fermat curve itself is a separable quotient, over \(\mathbf F_q\), of the Hermitian curve \(U^{p+1}+T^{p+1}+W^{p+1}=0\), by raising coordinates to the power \((p+1)/6\). The Hermitian curve is maximal over \(\mathbf F_{p^2}\). Every smooth quotient of a maximal curve over \(\mathbf F_{p^2}\) is maximal (injectivity of pullback on \(H^1_{\mathrm{\acute et}}\) and purity of the scalar Frobenius). Thus \(C_0\) is maximal, and geometric Frobenius on its eight-dimensional \(\ell\)-adic \(H^1\) has all eigenvalues \(-p\).

**(3) Character decomposition.** Write \(\zeta\) for a primitive sixth root of unity. The tame automorphism group acts by \((v,t)\mapsto(\zeta^{2i}v,\zeta^j t)\), with \(i\) modulo three and \(j\) modulo six. The holomorphic differentials are
\[
 \frac{dt}{v},\qquad \frac{dt}{v^2},\qquad \frac{t\,dt}{v^2},\qquad \frac{t^2\,dt}{v^2}.
\]
Their weights under the pair of basic generators \((v\mapsto\zeta^2v,t\mapsto t)\) and \((v\mapsto v,t\mapsto\zeta t)\) are, in additive exponent notation, \((2,1),(1,1),(1,2),(1,3)\). Together with the inverse weights, the complete eight weights of \(H^1\) are
\[
 \mathcal E=\{(2,1),(1,1),(1,2),(1,3),(1,5),(2,5),(2,4),(2,3)\}.
\]
One can identify the étale character multiset by lifting the tame action and the smooth curve to characteristic zero, where it is the sum of holomorphic weights and their inverses. Equivalently, the same characters follow from the tame Lefschetz traces.

**(4) Descent from the base curve.** Choose \(\beta,\delta\) over the algebraic closure with \(\beta^3=B\), \(\delta^6=A/B\). The map \((v,t)\mapsto(v/\beta,\delta t)\) identifies \(C_{A,B}\) with \(C_0\). For \(g\) as above, take \(\zeta=g^{(q-1)/6}\) in \(\mathbf F_q\) and identify this root with the complex primitive sixth root. The descent automorphism comparing these identifications before and after \(q\)-Frobenius is
\[
 (v,t)\longmapsto (\zeta^{2s}v,\zeta^{-r}t).
\]
Indeed, \(\beta^{q-1}=B^{(q-1)/3}=\zeta^{2s}\) and \(\delta^{q-1}=(A/B)^{(q-1)/6}=\zeta^r\). Combining this automorphism with the scalar \(-p\) Frobenius on \(C_0\) gives the multiset of reciprocal zeroes of the zeta numerator:
\[
 \left\{-p\,\zeta^{2si-rj}:(i,j)\in\mathcal E\right\}.
\]
The possible convention of inverting the cocycle does not affect the multiset, since \(\mathcal E\) is closed under taking inverse weights. Hence
\[
 L_{A,B}(T)=\prod_{(i,j)\in\mathcal E}\left(1+p\,\zeta^{2si-rj}T\right).
\]

**(5) Exact finite character arithmetic.** For each of the eighteen \((r,s)\), count exponents \(0,3,\{1,5\},\{2,4\}\) in the displayed multiset. Pairing conjugates gives respectively the factors \((1+u),(1-u),(1+u+u^2),(1-u+u^2)\). Explicit enumeration of the six-by-three exponent set gives exactly the eight signatures in the table. These are distinct polynomials (their cyclotomic root multisets differ), hence eight isogeny types. From the coefficient of \(T\) in \(L_{A,B}\), the four possible rational-point totals follow.

## Verification
The independent checker in `src/verify.py` implements quadratic finite fields from polynomial arithmetic, counts cube roots of \(-A t^6-B\) for every affine \(t\), and adds the three points at infinity precisely when \(-A\) is a cube. It checks all eighteen exponent classes for \(p=5,11,17\) against the character formula. It separately constructs \(\mathbf F_{625}\) as a quadratic extension of \(\mathbf F_{25}\) and verifies the full second-extension count for all eighteen classes. The exact table is `data/expected.json`; running `python3 src/verify.py` reproduces the checks. These finite computations validate examples and both the first and second Frobenius power, but the arbitrary-prime theorem is proved by the Hermitian quotient, tame characters and descent, not by finite extrapolation.

## Relationship to prior work
Kudo and Harashita (2017) enumerate superspecial genus-four curves in small characteristic. Kudo's April 2018 preprint identifies the untwisted genus-four canonical model, proves its superspeciality for \(p\equiv2\pmod3\), and records maximality computations for finitely many primes. The 2019 journal publication states the maximality of that **single untwisted curve** uniformly; neither maximality nor superspeciality of the untwisted curve is claimed here. Li--Mantovan--Pries--Tang's 2018/2019 Newton-polygon work describes slopes in larger cyclic-cover families, a coarser invariant than the Frobenius characteristic polynomial. Standard Jacobi-sum methods count points on diagonal equations in principle and form important background. The present statement resolves, for the specified diagonal genus-four family, all eighteen coefficient types into eight complete zeta polynomials and identifies arithmetic distinctions invisible in superspeciality or in single-field point totals.

## Limitations
This theorem classifies Weil polynomials, not full \(\mathbf F_q\)-isomorphism classes, automorphism groups, polarizations, or twists outside the two-parameter diagonal model. The arithmetic character calculation does not establish that every genus-four superspecial Jacobian appears in this family. Classical general Jacobi-sum formulas could also imply a form of this table after further specialization; the exact priority of this specialization has not been independently determined. The final 2019 journal text of the most directly related paper was not inspected in full, though its full earlier preprint and later abstract were available. These are priority risks, not gaps in the displayed proof.

## References
1. M. Kudo and S. Harashita, *Enumerating superspecial curves of genus 4 over prime fields*, arXiv:1702.05313, first public February 17, 2017. https://arxiv.org/abs/1702.05313
2. M. Kudo, *On the existence of superspecial nonhyperelliptic curves of genus 4*, arXiv:1804.09063, first public April 24, 2018; subsequent journal publication in *Communications in Algebra* 47 (2019), 5020--5038, DOI 10.1080/00927872.2019.1609013. https://arxiv.org/abs/1804.09063
3. W. Li, E. Mantovan, R. Pries, Y. Tang, *Newton Polygons Arising for Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914, May 17, 2018. https://arxiv.org/abs/1805.06914
4. M. Kudo, S. Harashita, H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, *Research in Number Theory* 6 (2020), article 44. https://doi.org/10.1007/s40993-020-00217-x
