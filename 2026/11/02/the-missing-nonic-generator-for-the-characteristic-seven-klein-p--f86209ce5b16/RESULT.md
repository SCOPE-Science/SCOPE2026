# The missing nonic generator for the characteristic-seven Klein point configuration

## Finding
Let \(k=\mathbb F_7\), \(S=k[x,y,z]\), and let \(Z\subset\mathbb P^2(k)\) be the singular-point set of the classical characteristic-seven specialization of the Klein arrangement of 21 lines. This set consists of 49 points: 21 points lying on four arrangement lines and 28 lying on three. Equivalently,
\[
Z=\mathbb P^2(\mathbb F_7)\setminus\{[x:y:z]:x^2+y^2+z^2=0\}.
\]
Put
\[
A=x^7y-xy^7,\quad B=x^7z-xz^7,\quad C=y^7z-yz^7,
\]
and
\[
G=xyz(x^2-y^2)(y^2-z^2)(z^2-x^2).
\]
Then the *homogeneous reduced point ideal* is exactly
\[
\boxed{I(Z)=(A,B,C,G).}
\]
The first three generators have degree eight; \(G\) is an indispensable generator of degree nine. The minimal graded free resolution of this ideal is
\[
\boxed{0\longrightarrow S(-9)\oplus S(-11)\oplus S(-13)
\longrightarrow S(-8)^3\oplus S(-9)\longrightarrow I(Z)\longrightarrow0.}
\]
Thus the Hilbert numerator of \(S/I(Z)\) is \(1-3t^8+t^{11}+t^{13}\), and the Hilbert function reaches 49 at degree 11. This completes the missing-generator question explicitly noted for the characteristic-seven exception in Seceleanu's Remark 4.3 [1].

## Assumptions and scope
All polynomial and scheme assertions are over \(\mathbb F_7\). The projective point set is reduced and consists only of the 49 \(\mathbb F_7\)-rational points; no assertion concerns extension-field points of the arrangement or symbolic-power containment. The full list of the 21 specialized lines and an exact evaluator appear in `klein_bad7_verify.py`. The conic \(Q=x^2+y^2+z^2\) is nonsingular and has eight \(\mathbb F_7\)-rational points.

## Proof
**1. The arrangement and the conic complement.** Specialize the Klein line coordinates using the parameter \(a=3\) satisfying \(a^2+a+2=0\) over \(\mathbb F_7\). Exact evaluation of the 21 displayed line equations at every one of the 57 rational projective points gives the incidence distribution \(8\) on zero lines, \(28\) on three lines, and \(21\) on four lines. The eight points on zero lines are exactly the rational points of \(Q=0\). All other rational points, and no conic points, comprise \(Z\). These 57 finite evaluations are independently reproducible in the accompanying complete verifier.

**2. The separating nonic.** The three minors \(A,B,C\) vanish at every rational projective point. The polynomial \(G\) is nonzero on a rational point precisely if \(xyz\ne0\) and the three squares \(x^2,y^2,z^2\) are pairwise distinct. The nonzero squares in \(\mathbb F_7\) are \(1,2,4\), whose sum is zero. Hence nonvanishing of \(G\) implies \(Q=0\). Conversely, a nontrivial rational solution of \(Q=0\) cannot have a zero coordinate (since \(-1\) is nonsquare) or two equal squared coordinates (since \(-2\) is nonsquare); thus \(G\ne0\) at all eight conic points. Therefore \(G\) vanishes on precisely the 49 points of \(Z\).

**3. Hilbert series of the candidate ideal.** Set \(J=(A,B,C)\). The standard projective finite-field point-ideal description identifies \(J\) as the radical ideal of all 57 rational points of \(\mathbb P^2(\mathbb F_7)\). Its two explicit Frobenius syzygies have coefficient degrees one and seven. Hilbert–Burch therefore gives
\[
0\to S(-9)\oplus S(-15)\to S(-8)^3\to J\to0
\]
and Hilbert numerator \(1-3t^8+t^9+t^{15}\) for \(S/J\). Since \(J\) is radical and \(G\) is nonzero exactly on the eight conic points, \(J:G=I(Q(\mathbb F_7))\). The eight conic points form the reduced complete intersection of \(Q\) and
\[
T=(y^2-4x^2)(y^2-2x^2),
\]
a quartic: its four distinct constituent lines each meet the conic in two distinct rational points. Thus \(I(Q(\mathbb F_7))=(Q,T)\), with Hilbert numerator \((1-t^2)(1-t^4)\). The multiplication exact sequence
\[
0\to S/(J:G)(-9)\xrightarrow{\,\cdot G\,}S/J\to S/(J,G)\to0
\]
therefore gives
\[
\operatorname{Hilb}_{S/(J,G)}(t)=\frac{1-3t^8+t^{11}+t^{13}}{(1-t)^3}.
\]
Its Hilbert function is \(1,3,6,10,15,21,28,36,42,46,48,49\) in degrees zero through eleven and is 49 thereafter.

**4. Equality with the reduced ideal.** We already have \((J,G)\subseteq I(Z)\). Exact modular row reduction of the degree-\(d\) evaluation matrices on all 49 points, for every integer \(0\le d\le11\), gives ranks
\[
1,3,6,10,15,21,28,36,42,46,48,49,
\]
identical to the preceding Hilbert function. For higher degrees the rank stays 49: choose, for example, a homogeneous linear form avoiding the finite set after extending scalars to an infinite field; point evaluations then inject under multiplication by that linear form, and base-extension preserves matrix ranks. Comparing graded dimensions with the series of \(S/(J,G)\) proves \(I(Z)=(J,G)\) in every degree, without assuming that finite-degree comparisons alone imply equality.

**5. Minimal resolution.** The three independent degree-eight minors are necessary. Every element of \(J\) vanishes at all 57 rational points, whereas \(G\) does not, so \(G\) is a necessary degree-nine generator. There are no other minimal generators because these four generate \(I(Z)\). A reduced finite point ideal in \(\mathbb P^2\) is saturated of height two and perfect; Hilbert–Burch gives exactly three first syzygies. Comparing the Hilbert numerator \(1-3t^8+t^{11}+t^{13}\) with generator degrees \(8,8,8,9\) forces syzygy shifts \(9,11,13\), as asserted. This also checks the eventual degree \(49\) by differentiating the numerator twice at \(t=1\).

## Verification
Run `python3 klein_bad7_verify.py` with Python 3 and no third-party dependencies. It enumerates all 57 normalized rational points, checks 21-line incidence and the eight-point conic, verifies the nonic separator and complete-intersection equations, and performs exact \(\mathbb F_7\) Gaussian elimination of the degree-zero-through-eleven evaluation and generator matrices. Its successful terminal sentinel is `VERIFY_OK`; the printed Hilbert ranks and Betti degrees agree with the statements above. The infinite-degree conclusion follows from the exact sequence and rank stabilization proved above, not from an unbounded numerical extrapolation.

## Relationship to prior work
Seceleanu [1, Remark 4.3] gives the three specialized octics and observes explicitly that they vanish at all 57 rational points, so further minimal generators are required in characteristic seven, but does not give the extra generator or this four-generator Betti table. Szemberg and Szpond [2] describe the 21-line finite-field Klein geometry, including the 49 intersection points, in the context of symbolic power containment rather than this specific minimal free resolution. The present computation identifies the precise missing generator and resolves the associated full graded presentation. A generic theorem about the full rational-point ideal \(J\) does not determine the off-conic ideal without the separating generator and quotient comparison.

## Limitations
This is a self-contained finite-field theorem for the indicated specialized arrangement, not a classification over arbitrary characteristic-seven extensions. It does not assert new symbolic-power noncontainments. Priority remains subject to comparison with unindexed finite-geometry and commutative-algebra tables; independent scientific review has not been conducted.

## References
[1] Alexandra Seceleanu, *A homological criterion for the containment between symbolic and ordinary powers for some ideals of points in* \(\mathbb P^2\), arXiv:1410.0312, first public 2014-10-01, especially Proposition 4.2 and Remark 4.3, https://arxiv.org/abs/1410.0312.

[2] Tomasz Szemberg and Justyna Szpond, *On the containment problem*, arXiv:1601.01308, first public 2016-01-06, https://arxiv.org/html/1601.01308v1.
