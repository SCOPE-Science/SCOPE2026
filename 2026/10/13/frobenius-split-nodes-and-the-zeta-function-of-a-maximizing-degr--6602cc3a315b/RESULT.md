# Frobenius-split nodes and the zeta function of a maximizing degree-nine free curve

## Finding
Let \(p>3\) be prime. Define the degree-six polynomial and the reduced degree-nine plane divisor
\[
 H=(x^2+y^2+z^2)^3-27x^2y^2z^2,\qquad D=V(xyzH)\subset\mathbb P^2_{\mathbb F_p}.
\]
Write \(\epsilon_p=(\frac{-3}{p})\) and \(\eta_p=(\frac{-1}{p})\) for Legendre symbols. For **every** integer \(r\ge1\),
\[
 \#D(\mathbb F_{p^r})=4p^r-2-4\epsilon_p^r-3\eta_p^r.
\]
In particular its Hasse–Weil zeta function is exactly
\[
 Z(D/\mathbb F_p,T)=\frac{(1-T)^2(1-\epsilon_pT)^4(1-\eta_pT)^3}{(1-pT)^4}.
\]
The essential geometric calculation is a normalization of the irreducible sextic \(V(H)\), defined over \(\mathbb Z[1/6]\) and yielding a normalization over every field of characteristic greater than three: the smooth conic \(Q: u^2+v^2+w^2=0\) maps birationally onto it by \([u:v:w]\mapsto[u^3:v^3:w^3]\). Four rational ordinary nodes have split branches exactly when \(\epsilon_p^r=1\). The other six sextic singularities are unibranch cusps and contribute no normalization point-count correction. The three coordinate lines meet the sextic precisely at these six cusps, defined over extensions in which \(-1\) is a square.

## Assumptions and scope
All schemes and counts use the **fixed integral equations above** and their geometric reduced support. Statements hold in every characteristic \(p>3\), over each extension \(\mathbb F_{p^r}\). A rational point of the singular curve means a closed geometric point fixed by the indicated Frobenius, not a branch on its normalization. The theorem does not claim preservation of characteristic-zero freeness under reduction, and excludes characteristics two and three. The curve was previously studied as a characteristic-zero maximizing free divisor; its known freeness, component counts and singularity labels are not new.

## Proof
**(1) The conic is the normalization.** Put \(a=u^2\), \(b=v^2\), \(c=w^2\). On \(Q\) their sum vanishes, and the identity
\[
 a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)
\]
shows \(H(u^3,v^3,w^3)=0\). The three cubics have no common zero on the smooth conic, so they define a morphism \(\nu:Q\to V(H)\). If two geometric points with nonzero coordinates have identical cubic images, after a common projective scaling their coordinates differ by elements of \(\mu_3\). Unless all three multipliers are equal, the original Fermat conic and the diagonally transformed Fermat conic are distinct conics and have only finitely many common points. Hence \(\nu\) is generically injective. Because \(\nu^*\mathcal O_{\mathbb P^2}(1)=\mathcal O_Q(3)\) has degree six, its image has degree six. The equation \(H\) also has degree six, so \(V(H)\) is the integral image and \(\nu\) is finite birational. Smoothness of \(Q\) gives normalization, over each field of characteristic \(p>3\).

**(2) Geometric singular points and branches.** Direct differentiation gives
\[
 H_x=6x(S^2-9y^2z^2),\quad H_y=6y(S^2-9x^2z^2),\quad H_z=6z(S^2-9x^2y^2),\quad S=x^2+y^2+z^2.
\]
If all coordinates are nonzero and all partials vanish, \(x^2=y^2=z^2\); this gives the four points \([1:\pm1:\pm1]\), all rational. At \([1:1:1]\), setting \(x=1\), \(y=1+U\), \(z=1+V\) gives quadratic tangent cone \(36(U^2-UV+V^2)\). Sign changes preserve the discriminant square class, which is \(-3\). Thus the four points are ordinary nodes, with two branches rational over \(\mathbb F_{p^r}\) precisely when \(\epsilon_p^r=1\), and no rational branches when \(\epsilon_p^r=-1\). This also follows directly from the two \(\mu_3\)-patterns of preimages under \(\nu\): Frobenius fixes them individually exactly when a nontrivial cube root of unity lies in the field.

On the axes, for example \(x=0\), the sextic restricts to \((y^2+z^2)^3=0\), yielding two points over the algebraic closure. Cyclically there are six distinct points. Locally the functions \(S\) and \(xyz\) are independent parameters at each such point, and \(H=S^3-27(xyz)^2\) has cusp type \(A_2\) in characteristic greater than three. Each cusp is unibranch. Its normalization preimage has the same residue field: at \(u=0\) the conic condition gives \((v/w)^2=-1\) and the image coordinate \((v/w)^3=-(v/w)\). Hence a rational cusp gives exactly one rational normalization point. The gradient equations show there are no further singularities.

**(3) Count the sextic.** Every smooth conic over a finite field has \(q+1\) rational points, where \(q=p^r\). Away from singularities normalization is an isomorphism. Each of the four rational nodes has two rational preimages in the split case and zero in the nonsplit case, whereas it contributes one rational point to the sextic. Six cusps cause no discrepancy. Consequently
\[
 \#V(H)(\mathbb F_q)=(q+1)-4\epsilon_p^r.
\]
This counts both nonsplit rational nodes (which lie on the curve but have no rational normalization preimage) and split rational nodes correctly.

**(4) Adjoin the coordinate triangle.** The union \(L=V(xyz)\) has \(3(q+1)-3=3q\) rational points, since its three pairwise coordinate intersections are distinct rational vertices. The reduced intersection \(V(H)\cap L\) consists exactly of the six cusp points, with two on each coordinate axis and disjoint from the vertices. The number rational over \(\mathbb F_q\) is \(3(1+\eta_p^r)\), as the two roots of \(t^2=-1\) exist exactly when \(\eta_p^r=1\). Inclusion-exclusion gives
\[
 \#D(\mathbb F_q)=(q+1-4\epsilon_p^r)+3q-3(1+\eta_p^r)
 =4q-2-4\epsilon_p^r-3\eta_p^r.
\]
Finally, applying the identity \(\exp(\sum_{r\ge1}\alpha^rT^r/r)=(1-\alpha T)^{-1}\) term by term proves the stated zeta function.

## Verification
Run `python3 verify.py` using only the Python standard library. The file evaluates sextic and full-divisor equations on all projective rational points over eleven prime fields, and over quadratic extensions for three small primes. It confirms the formulas separately for the sextic and for the entire divisor, including primes with both Legendre signs. The executable finite tests are consistency checks, not an induction or a replacement for the normalization and branch arguments above.

## Relationship to prior work
Dimca–Sticlaru, *Nearly free divisors and rational cuspidal curves*, Example 2.8, already described the sextic's six cusps, four nodes, rationality and a one-line union. Dimca–Ilardi–Pokora–Sticlaru, *Construction of free curves by adding lines to a given curve*, Example 6.4, explicitly studied the exact degree-nine union \(xyzH\), including its complex maximizing freeness and singularity basket. Di Gennaro–Ilardi–Miró-Roig–Schenck–Vallès, *Free curves, Eigenschemes and Pencils of curves*, Example 4.2, derived the same union from a sextic pencil and proved characteristic-zero freeness. Those known statements are not credited as new. The present claim is the **arithmetic normalization model and complete Frobenius point-count/zeta classification** of that distinguished union for every \(p>3\). The cited papers' statements about complex singularity types and free exponents do not themselves give a rational normalization over the finite fields or distinguish split from nonsplit Frobenius branches. Published-record semantic searches likewise returned no equivalent zeta theorem; this is a literature-based comparison, not proof of priority.

## Limitations
Characteristics two and three are outside scope, as are all claims concerning positive-characteristic logarithmic freeness. The arithmetic formula uses the displayed rational coordinate model and is not asserted to be invariant under arbitrary reductions of projectively equivalent models at bad primes. It determines the zeta function but does not calculate cohomology groups or construct a general theory of zeta functions for maximizing free divisors. Previously known geometric singularity counts, genus and characteristic-zero freeness are not novel claims. Independent validation has not been performed; unindexed arithmetic work on this classical sextic remains a priority risk.

## References
1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117 (first posted 2023-01-03), Example 6.4; Results in Mathematics 79 (2024), article 11, DOI:10.1007/s00025-023-02036-9.
2. R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, H. Schenck, J. Vallès, *Free curves, Eigenschemes and Pencils of curves*, arXiv:2306.09443v1 (2023-06-15), Example 4.2.
3. A. Dimca, G. Sticlaru, *Nearly free divisors and rational cuspidal curves*, arXiv:1505.00666v3 (2015), Example 2.8.
