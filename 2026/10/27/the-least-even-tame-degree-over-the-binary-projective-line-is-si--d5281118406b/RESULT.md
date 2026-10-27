# The least even tame degree over the binary projective line is six, with two arithmetic orbits

## Finding
Let a rational map \(f:\mathbf P^1_{\mathbf F_2}\to\mathbf P^1_{\mathbf F_2}\) be called tame if it is finite, separable, and the ramification index at every geometric point is odd. Among such maps of **even** degree, the least possible degree is \(6\): there are no tame maps of degree \(2\) or \(4\). At degree \(6\), there are exactly \(72\) maps, counted as ordered coprime homogeneous binary form pairs modulo common scalar, and they form exactly two orbits of size \(36\) under independent changes of source and target coordinates by \(\operatorname{PGL}_2(\mathbf F_2)\). The two orbit representatives are
\[
 f_4(x)=\frac{x}{x^6+x^3+1},\qquad f_3(x)=\frac{x}{x^6+x^5+x^3+1}.
\]
Their branch-value sets contain respectively \(4\) and \(3\) geometric points, so these are distinct arithmetic and geometric configurations. The second is a degree-six tame three-point cover with rational branch values \(\{0,1,\infty\}\).

## Assumptions and scope
All polynomials and maps are defined over \(\mathbf F_2\). A degree-\(d\) map is represented uniquely by a pair of coprime binary forms of homogeneous degree \(d\), not both of smaller affine degree, after scalar normalization. Since \(\mathbf F_2^\times\) is trivial, the affine coefficient pair itself is unique. A map is everywhere tame precisely when it is separable and its local ramification indices are all prime to characteristic two. Two maps are identified for orbit purposes only when related by an automorphism of the source and an independent automorphism of the target, both defined over \(\mathbf F_2\). Thus the count \(72\) precedes quotienting by automorphisms.

## Proof
Write \(A(x),B(x)\in\mathbf F_2[x]\) with \(\gcd(A,B)=1\) and \(\max(\deg A,\deg B)=d\). Every such pair gives one degree-\(d\) map; these pairs are enumerated without omissions by iterating all \(2^{d+1}\) binary coefficient words for each of \(A,B\), imposing coprimeness and the degree condition.

For a polynomial \(P(x)\), let \(P^{[j]}\) be its \(j\)-th Hasse derivative: the coefficient of \(h^j\) in \(P(x+h)\). Define
\[
 J_j=B A^{[j]}-A B^{[j]},\qquad j=1,\ldots,d.
\]
At a finite geometric point with minimal polynomial \(q\), the local ramification index is the smallest \(j\ge1\) for which \(J_j\not\equiv0\pmod q\); the first coefficient vanishes at ramification points, so only irreducible factors of \(J_1\) need be visited. This criterion remains valid at poles because \(A\) and \(B\) are coprime, and at every point at least one of the two is a local unit. If \(J_1\equiv0\), the map is inseparable and excluded. At infinity, replace \(A,B\) by their degree-\(d\) reversed coefficient polynomials and apply the same Hasse derivative criterion at \(0\). Since \(\deg J_1\le2d-2\), enumerating all monic irreducible polynomials of degree at most \(2d-2\) suffices to determine the entire geometric ramification profile exactly; this is not a bounded extension-field sample.

The complete coefficient enumeration and irreducible-factor test in `verify_tame_bit.py` give
\[
\begin{array}{c|r|r}
 d&\text{coprime coefficient pairs}&\text{everywhere-tame maps}\\\hline
 2&24&0\\4&384&0\\6&6144&72
\end{array}.
\]
All \(72\) qualifying degree-six maps have identical ramification profile: one rational ramification point of index \(3\), one rational ramification point of index \(5\), and a degree-two closed point whose two geometric points each have index \(3\). This exhausts the Riemann–Hurwitz sum, \(2+4+2\cdot2=10=2\cdot6-2\), independently corroborating that no additional branch points are omitted.

The exact source/target group computation enumerates all six invertible \(2\times2\) binary matrices, substitutes the corresponding linear forms into each binary sextic, and independently applies all six target matrices. The orbits of coefficient pairs \((2,73)\) and \((2,105)\) (coefficient bit \(i\) representing the coefficient of \(x^i\)) each have \(36\) elements, are disjoint, and their union equals the entire \(72\)-map tame census. Each two-sided stabilizer is therefore trivial.

For both displayed representatives, the numerator of the derivative is \((x^3+1)^2=(x+1)^2(x^2+x+1)^2\). There is ramification of index \(5\) at infinity, of index \(3\) at \(1\), and of index \(3\) at the two roots of \(x^2+x+1\). For \(f_4\), their images are respectively \(0,1\), and the two conjugate roots themselves, giving four geometric branch values. For \(f_3\), their images are \(0,\infty\), and \(1\), giving three rational branch values. The geometric branch-value count is invariant under source and target automorphisms, so the two orbit representatives cannot be equivalent.

## Verification
Run `python verify_tame_bit.py` in a directory containing the code. Its exhaustive loops count \(24,384,6144\) degree-\(2,4,6\) maps and confirm \(0,0,72\) tame maps. It computes the two full 36-element orbits and writes their union as the sorted 72-row, decimal binary-coefficient certificate `tame_d6_pairs.txt`. The delivered certificate agrees byte-for-byte with the output of the final checker. Separately run `python verify_tame_sympy.py` in the same directory with SymPy installed. This independent polynomial-arithmetic implementation enumerates every degree-two and degree-four candidate and finds none tame, then verifies geometric ramification of all 72 degree-six pairs from the certificate; it does **not** independently re-enumerate the 6144 degree-six candidates. Both programs were executed from their delivered contents and returned PASS. See `VERIFICATION.md` for commands and limitations.

## Relationship to prior work
Sugiyama and Yasuda's *Belyi's theorem in characteristic two* (first arXiv version, 10 August 2017) proves a characteristic-two existence theorem; its accessible abstract gives no minimal even degree, binary coefficient census, or two-sided orbit classification. Its full text could not be inspected, so overlapping examples remain a residual priority risk. Kedlaya, Litt and Witaszek's *Tamely ramified morphisms of curves and Belyi's theorem in positive characteristic* (first arXiv version, 2 October 2020), inspected in its introductory results and its Belyi-theorem section, establishes broad tame existence and a three-branch-point construction but does not assert these exact low-degree counts. The present result is an explicit small-field arithmetic classification, not a new general existence theorem. Search of relevant mathematical records and explicit degree-six literature revealed no dominating statement; failure to locate one is not proof of absolute novelty.

## Limitations
The claim is restricted to maps defined over \(\mathbf F_2\) and to **even** degrees at the minimum. It does not claim degree six is the smallest degree of a tame map without the parity restriction, nor does it classify degree-six maps over larger fields or up to base change to an algebraic closure. All classification counts are computationally proved by short exhaustive loops; they are not inferred from random sampling. The full text of Sugiyama–Yasuda was not accessible for a decisive statement-level priority comparison, and unindexed earlier enumerations remain possible.

## References
1. Y. Sugiyama and S. Yasuda, *Belyi's theorem in characteristic two*, arXiv:1708.03036, first posted 2017-08-10, https://arxiv.org/abs/1708.03036.
2. K. Kedlaya, D. Litt, J. Witaszek, *Tamely ramified morphisms of curves and Belyi's theorem in positive characteristic*, arXiv:2010.01130, first posted 2020-10-02, https://arxiv.org/abs/2010.01130.
