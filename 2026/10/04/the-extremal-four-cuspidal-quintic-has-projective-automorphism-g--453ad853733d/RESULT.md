# The extremal four-cuspidal quintic has projective automorphism group \(C_3\)
## Finding
Over \(\mathbb C\), consider the rational four-cuspidal quintic \(\mathcal Q_4\subset\mathbb P^2\)
\[
27x^5+18x^3yz-2x^2y^3-x^2z^3+2xy^2z^2-y^4z=0.
\]
Its full projective automorphism group is
\[
\operatorname{{Aut}}_{{\mathbb P^2}}(\mathcal Q_4)=\left\langle [x:y:z]\mapsto[\omega x:\omega^2y:z]\right\rangle\cong C_3,
\]
where \(\omega^2+\omega+1=0\). On the normalization the generator fixes the distinguished cusp preimage and cyclically permutes the other three cusp preimages. It also fixes the smooth normalization point \([1:0]\).

## Assumptions and scope
Koras--Palka prove that a complex rational plane curve homeomorphic to \(\mathbb P^1\) has at most four cusps and that the four-cusp case is unique up to projective equivalence. Their representative has normalization
\[
\varphi([s:t])=[s^4t:s^2t^3-s^5:t^5+2s^3t^2].
\]
They identify one cusp, at \(\varphi([0:1])\), with local analytic type \(x^2=y^7\), and the other three with local analytic type \(x^2=y^3\). The statement here concerns only projective automorphisms of this complex plane curve; it does not classify abstract automorphisms of its singular scheme or automorphisms after resolving the curve.

## Proof
Every projective automorphism of \(\mathcal Q_4\) lifts uniquely to an automorphism of its normalization \(\mathbb P^1\). Because analytic singularity type is preserved, the unique \(A_6\) cusp must be fixed and the three \(A_2\) cusps may only be permuted.

Use \(u=s/t\) on the normalization. The four cusp preimages are \(u=0\) and \(u=-\alpha\omega^k\) for \(k=0,1,2\), where \(\alpha^3=2\). Scaling \(u\) by the nonzero constant \(-1/\alpha\) changes these four marked points to
\[
0,\quad 1,\quad \omega,\quad \omega^2.
\]
With the convention
\[
[a,b;c,d]=\frac{(a-c)(b-d)}{(a-d)(b-c)},
\]
one has
\[
[0,1;\omega,\omega^2]=-\omega.
\]
Keeping \(0\) fixed and permuting \(1,\omega,\omega^2\), the three even permutations retain the value \(-\omega\), while the three odd permutations give \(-\omega^2\). Since \(\omega\ne\omega^2\), cross-ratio invariance excludes every odd permutation. Hence the induced permutation group is contained in \(A_3\), so the projective stabilizer has order at most three. The action on the normalization is faithful: if the lift is the identity, the projective transformation fixes the nondegenerate curve pointwise and is therefore the identity.

Conversely, the order-three map \([s:t]\mapsto[\omega s:t]\) satisfies
\[
\varphi([\omega s:t])=[\omega x:\omega^2y:z]
\]
when \([x:y:z]=\varphi([s:t])\). Thus the diagonal projective transformation \([x:y:z]\mapsto[\omega x:\omega^2y:z]\) preserves \(\mathcal Q_4\) and realizes the three even permutations. The upper and lower bounds coincide, proving the claimed group. The fixed normalization points of this generator are \([0:1]\) and \([1:0]\); the first maps to the \(A_6\) cusp and the second is smooth because Koras--Palka list all singular points among the four cusp preimages.

## Verification
The accompanying exact checker uses arithmetic in \(\mathbb Q(\omega)=\mathbb Q[w]/(w^2+w+1)\). It verifies: the six monomials of the implicit quintic all acquire the same factor \(\omega^2\) under \((x,y,z)\mapsto(\omega x,\omega^2y,z)\); the three normalization coordinates acquire weights \(\omega,\omega^2,1\) under \(s\mapsto\omega s\); and the six permutations of the three equal-type cusp preimages split exactly into three cross-ratio-preserving even permutations and three cross-ratio-changing odd permutations. Running `python3 artifacts/verify_target.py` prints `VERIFY_OK`.

## Relationship to prior work
Koras--Palka supply the unique extremal four-cuspidal projective class, its explicit equation, normalization, and cusp types. Their searchable full text contains no occurrence of “automorphism”, “stabilizer”, or “symmetry”; the group computation above is not used in their classification argument. Moe's work on four-cuspidal curves on Hirzebruch surfaces treats constructions and cusp configurations rather than this projective stabilizer. Peter Field's 1924 paper on a rational plane quintic with four real cusps is a historically close source; only bibliographic metadata and references were available in the inspected interface, so it remains a residual historical-literature risk rather than evidence of coverage.

## Limitations
The originality assessment is literature-bounded rather than a proof that no older source ever recorded the same symmetry group. In particular, the body of Field's 1924 paper was not available through the inspected text interface. The result is specific to the unique four-cuspidal quintic over \(\mathbb C\); it does not assert a general automorphism theorem for rational cuspidal curves.

## References
1. M. Koras and K. Palka, “Complex planar curves homeomorphic to a line have at most four singular points,” arXiv:1905.11376; Journal de Mathématiques Pures et Appliquées 158 (2022), 144–182, DOI 10.1016/j.matpur.2021.11.003.
2. T. K. Moe, “Rational cuspidal curves with four cusps on Hirzebruch surfaces,” Le Matematiche 69 (2014).
3. P. Field, “On a Rational Plane Quintic Curve with Four Real Cusps,” American Journal of Mathematics 46 (1924), 235–240, DOI 10.2307/2370859.
