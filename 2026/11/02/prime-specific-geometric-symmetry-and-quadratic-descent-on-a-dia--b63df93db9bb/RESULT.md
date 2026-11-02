# Prime-specific geometric symmetry and quadratic descent on a diagonal degree-four del Pezzo family

## Finding
For each prime \(p\ge 7\), let \(S_p\subset\mathbb P^4_{\mathbb F_p}\) be the surface
\[
S_p:\qquad \sum_{i=0}^4 x_i^2=\sum_{i=0}^4 i x_i^2=0.
\]
This is a smooth del Pezzo surface of degree four. Its complete groups of biregular automorphisms satisfy
\[
\operatorname{Aut}_{\mathbb F_p}(S_p)\cong (C_2)^4\rtimes C_2,
\qquad\bigl|\operatorname{Aut}_{\mathbb F_p}(S_p)\bigr|=32
\]
for **every** such prime, while
\[
\bigl|\operatorname{Aut}_{\overline{\mathbb F}_p}(S_p)\bigr|=
\begin{cases}96,&p=7\text{ or }13,\\160,&p=11,\\32,&p\ge7,\ p\notin\{7,11,13\}.\end{cases}
\]
More precisely, the geometric groups are \((C_2)^4\rtimes S_3\) for \(p=7,13\), \((C_2)^4\rtimes D_5\) for \(p=11\), and \((C_2)^4\rtimes C_2\) otherwise (where \(D_5\) has order ten). Every geometric automorphism becomes defined over \(\mathbb F_{p^2}\). Thus the geometric symmetry jumps at exactly three primes, but none of those additional automorphisms descends to the corresponding prime field.

## Assumptions and scope
Here \(p\) ranges over **all primes at least seven**, and \(\operatorname{Aut}_k\) denotes biregular automorphisms defined over the indicated field, not birational selfmaps. The five pencil discriminant parameters \(0,1,2,3,4\) are distinct in the stated characteristic. All group statements concern the actual displayed diagonal equation, not arbitrary twists or all degree-four del Pezzo surfaces. The semidirect-product statement over the algebraic closure uses the standard degree-four del Pezzo automorphism theorem, whose geometric statement is also recovered here from monomial matrices.

## Proof
**Smoothness and linearity.** Let \(Q_0=\sum_i x_i^2\) and \(Q_1=\sum_i i x_i^2\). If their gradients are dependent at a projective point, for some nonzero pair \((u,v)\), every nonzero coordinate must satisfy \(u+vi=0\). Since the five indices are distinct modulo \(p\), at most one coordinate can be nonzero. Such a coordinate vector does not satisfy \(Q_0=0\), so the intersection is smooth. Adjunction gives \(-K_{S_p}=\mathcal O_{S_p}(1)\), with \((-K_{S_p})^2=4\). Every biregular automorphism therefore acts projectively on the anticanonical embedding and preserves the pencil spanned by \(Q_0,Q_1\).

**Reduction to five marked points.** The five singular members of the pencil are precisely the rank-four quadrics with vertices at the five coordinate points. Hence any projective linear automorphism of the surface is monomial, permuting these vertices and their associated pencil parameters \(T=\{0,1,2,3,4\}\). Its induced permutation \(\sigma\) must be induced by some fractional-linear transformation
\[
\phi(t)=\frac{at+b}{ct+d},\qquad ad-bc\ne0,
\]
with \(\phi(i)=\sigma(i)\) for all \(i\in T\). Conversely, over the algebraic closure, every such transformation lifts: take a monomial matrix sending coordinate \(i\) to coordinate \(\sigma(i)\) with multiplier \(r_i\) satisfying \(r_i^2=ci+d\) (up to one common nonzero scalar). Indeed, the new pair of quadratic equations becomes \((cQ_1+dQ_0,\ aQ_1+bQ_0)\). The kernel of the permutation action is the projective diagonal sign group \((C_2)^4\), order \(16\).

**Exact classification of the five-point stabilizer.** There are 120 possible permutations of \(T\). For each permutation \(\sigma\), impose the three linear equations
\[
a i+b-\sigma(i)(ci+d)=0\qquad(i=0,1,2).
\]
The signed maximal minors of their integer \(3\times4\) coefficient matrix, divided by their gcd, give a primitive integer quadruple \((a,b,c,d)\). This spans the unique rational interpolation solution. Define integer residuals
\[
R_j(\sigma)=aj+b-\sigma(j)(cj+d)\qquad(j=3,4).
\]
Exactly two permutations have both residuals zero as integers: the identity and reversal \(i\mapsto4-i\). For the other 118 permutations, the union of prime divisors of \(\gcd(R_3(\sigma),R_4(\sigma))\) is **exactly** \(\{2,3,5,7,11,13\}\). The full executable integer certificate is `verify.py`: it checks all 120 permutations and rejects singular fractional-linear matrices and poles modulo each prime. It follows, without a finite-prime cutoff assumption, that for every \(p\ge17\) the stabilizer of \(T\) has order two. Direct complete checks at the three remaining primes give orders \(6,10,6\) for \(p=7,11,13\), respectively. Reversal and respective elements of orders \(3,5,3\) generate \(S_3,D_5,S_3\). Explicit additional generators (listed as the images of \(0,1,2,3,4\)) are
\[
\begin{array}{c|c|c}
p&\sigma&(a,b,c,d)\\\hline
7&(2,1,4,3,0)&(5,-6,2,-3)\\
11&(1,3,0,4,2)&(-3,6,-5,6)\\
13&(0,2,3,1,4)&(-6,0,-1,-2).
\end{array}
\]
Multiplying stabilizer order by 16 proves all geometric group orders.

**Prime-field descent.** A stabilizer element \(\phi\) has an \(\mathbb F_p\)-rational projective lift precisely when the five nonzero numbers \(ci+d\), for \(i\in T\), have the same quadratic character. Necessity follows by dividing the squared monomial multipliers by their common scale; sufficiency follows by choosing a common scale making all five squares. Reversal has constant denominator and admits the evident coordinate-permutation lift. For the displayed extra generators, the five quadratic-character strings are, respectively,
\[
\begin{array}{c|c|c}
p&((ci+d)\bmod p)_{i=0}^4&\text{square/nonsquare pattern}\\\hline
7&(4,6,1,3,5)&(+,-,+,-,-)\\
11&(6,1,7,2,8)&(-,+,-,-,-)\\
13&(11,10,9,8,7)&(-,+,+,-,-).
\end{array}
\]
Thus these generators do not descend. Since the image of the descended automorphisms is a subgroup containing the reversal, and the full stabilizer is generated by reversal plus an element of prime order three or five, direct complete enumeration verifies that the only liftable elements are identity and reversal. (The verifier also checks the character criterion for every stabilizer element, not merely the chosen generators.) Hence the rational group is of order \(16\cdot2=32\) in all cases. The rational reversal permutes the five sign factors, so the group is \((C_2)^4\rtimes C_2\).

Finally, every element of \(\mathbb F_p^*\) is a square in \(\mathbb F_{p^2}\), because \(z^{(p^2-1)/2}=(z^{(p-1)/2})^{p+1}=1\). Thus every geometric monomial lift descends to \(\mathbb F_{p^2}\), including at the exceptional primes.

## Verification
Execute `python3 verify.py` using Python 3 and its standard library only. The script (i) enumerates all 120 permutations; (ii) constructs exact primitive interpolation matrices by integer minors; (iii) checks the zero-residual cases and the complete exceptional prime-divisor support; (iv) exhaustively finds each exceptional stabilizer and all prime-field-liftable elements; (v) checks additional prime samples; and (vi) verifies quadratic-extension square identities. The attached `verification_output.txt` is the recorded successful output, ending in `VERIFY_OK`. The all-prime assertion relies on the exact residual gcd exhaustion, not extrapolation from finite prime samples.

## Relationship to prior work
The geometric description of automorphisms of degree-four del Pezzo surfaces as \((C_2)^4\rtimes G\), with \(G\) the stabilizer of the five discriminant points, is an established theorem of Dolgachev–Duncan (2017, Section 3 and Theorem 3.1). The five-point moduli description is not claimed as new. Knecht (2013) studies finite-field degree-four del Pezzo unirationality, a different arithmetic question. Smith (2023) studies automorphism actions over fields of characteristic zero; its field restrictions do not cover the present positive-characteristic family. Kunyavskij–Skorobogatov–Tsfasman (1989) is a broad arithmetic predecessor whose complete text was not inspectable here. The specific infinitely many-primes computation, three-prime geometric jumps, unchanged prime-field group, and explicit degree-two descent are the contributions assessed here. No uniqueness or historical-priority assertion is made merely from the absence of a search hit.

## Limitations
This theorem excludes characteristics two, three and five, does not classify twists or all isomorphism classes of quartic del Pezzo surfaces, and does not describe birational automorphisms. Prior general automorphism theory already implies the geometric group **once** the five-point stabilizer is calculated; novelty is assessed for the specific arithmetic/geometric comparison and uniform exceptional-prime computation, not for that theory. Historical priority should be checked independently against older broad literature, especially the complete 1989 monograph. No independent scientific audit has been performed.

## References
1. A. Knecht, *Degree of Unirationality for Del Pezzo Surfaces over Finite Fields*, arXiv:1307.3215 (first posted July 11, 2013), https://arxiv.org/abs/1307.3215.
2. I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167 (first posted December 4, 2017), especially Section 3, https://arxiv.org/abs/1712.01167.
3. J. M. Smith, *Automorphisms of quartic del Pezzo surfaces in characteristic zero*, arXiv:2308.07904 (first posted August 15, 2023), https://arxiv.org/abs/2308.07904.
4. B. Kunyavskij, A. Skorobogatov and M. Tsfasman, *Del Pezzo surfaces of degree four*, Mémoires de la Société Mathématique de France **37** (1989), https://www.numdam.org/item/MSMF_1989_2_37__1_0/.
