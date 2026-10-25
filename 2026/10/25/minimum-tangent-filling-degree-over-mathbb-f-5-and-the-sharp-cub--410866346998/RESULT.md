# Minimum tangent-filling degree over \(\mathbb F_5\) and the sharp cubic obstruction

## Finding

In the projective plane over \(\mathbb F_5\), **no nonzero homogeneous polynomial of degree at most three has tangent lines at its smooth rational zeros covering all rational points**. The sharp maximum for the number of points covered by these tangent lines, without any irreducibility or smoothness restriction on the polynomial, is \(29\) out of \(31\) in degree three. The corresponding maxima are \(6\) in degree one and \(21\) in degree two.

On the other hand, the geometrically smooth plane quartic
\[
X^4+X^3Y+Y^3Z-Z^4=0
\]
is tangent-filling: six of its rational tangent lines form the entire pencil through \((1:1:0)\). Consequently, **the minimum degree of an irreducible tangent-filling plane curve over \(\mathbb F_5\) is exactly four**.

The cubic bound \(29\) is sharp even among smooth cubics, as witnessed by
\[
X^3+3X^2Y+2X^2Z+XZ^2+Y^3=0.
\]
Its rational tangent lines cover precisely \(29\) projective points, missing \((1:1:4)\) and \((1:4:4)\).

## Assumptions and scope

All coefficients and projective points are over \(\mathbb F_5\). At any rational zero \(P\) of a homogeneous polynomial \(H\) with nonzero gradient, its tangent is the rational line \(H_X(P)X+H_Y(P)Y+H_Z(P)Z=0\). Singular rational zeros contribute no tangent. A curve is tangent-filling if the union of these lines includes every one of the \(31\) rational points of \(\mathbb P^2(\mathbb F_5)\). The exhaustive upper bound applies even to reducible, nonreduced and singular polynomials, whereas the minimum-degree statement concerns irreducible curves.

## Proof

**Exhaustive cubic obstruction (finite, complete).** There are \(31\) normalized rational projective points, represented uniquely by \((1:y:z)\), \((0:1:z)\), and \((0:0:1)\), with \(y,z\in\mathbb F_5\). For degree \(d\), order the \(m=\binom{d+2}{2}\) monomials as \(X^aY^bZ^{d-a-b}\), decreasing first \(a\), then \(b\). Every nonzero degree-\(d\) homogeneous polynomial modulo scalar multiplication has exactly one coefficient vector whose first nonzero coordinate equals \(1\). For each possible position of that coordinate, all subsequent coordinates range independently over \(\mathbb F_5\), giving \((5^m-1)/4\) canonical coefficient vectors.

For each vector and each of the \(31\) projective points, exact modular evaluation identifies smooth rational zeros and their gradients. Each nonzero gradient determines one of the \(31\) rational projective lines. A \(31\)-bit incidence mask records the union of the corresponding six-point lines. The complete enumeration implemented in `verify.cpp` gives:

| Degree | Canonical polynomials | Maximum covered points | Tangent-filling polynomials |
|---|---:|---:|---:|
| 1 | 31 | 6 | 0 |
| 2 | 3,906 | 21 | 0 |
| 3 | 2,441,406 | 29 | 0 |

Every nonzero polynomial is represented once; all rational points, roots, gradients and tangent incidences are processed. Therefore this is a finite exhaustive proof, not a sample-based inference. It excludes tangent-filling degrees one, two and three, including all possible singular and reducible forms. In particular the maximum for cubics is \(29\). The smooth cubic displayed above realizes it.

**Quartic existence.** Set \(F=X^4+X^3Y+Y^3Z-Z^4\), with derivatives
\[
F_X=X^2(4X+3Y),\qquad F_Y=X^3+3Y^2Z,\qquad F_Z=Y^3-4Z^3.
\]
If \(X=0\) at a common zero of the derivatives, then \(Y^2Z=0\) and \(Y^3-4Z^3=0\), forcing \(Y=Z=0\), which is not a projective point. If \(X\ne0\), the first two derivatives force \(Y=2X\) and \(Z=2X\), but the third then equals \(X^3\ne0\). Thus the quartic is geometrically smooth. A smooth projective plane curve is geometrically irreducible: otherwise distinct components intersect by Bézout, forcing a singularity.

The four points \((1:0:z)\) for \(z\in\mathbb F_5^\times\), together with \((1:1:4)\) and \((0:1:0)\), are distinct smooth rational points on \(F=0\). At each, the tangent passes through \((1:1:0)\) because \(F_X+F_Y=0\) there. These six tangents are distinct: the first four have normals \((4:1:-4z^3)\), whose last entries are distinct; the fifth has normal \((2:3:0)\), and the last is \((0:0:1)\). They therefore constitute all six \(\mathbb F_5\)-lines through \((1:1:0)\), and these cover the complete rational projective plane. This proves the claimed minimum degree.

**Sharpness by a smooth cubic.** Set \(G=X^3+3X^2Y+2X^2Z+XZ^2+Y^3\). Its derivative in \(Z\) is \(2X(X+Z)\). If \(X=0\), the other two derivatives imply \(Y=Z=0\). If \(X\ne0\), then \(Z=-X\), and the derivative in \(X\) becomes \(XY\), forcing \(Y=0\); the derivative in \(Y\) is then \(3X^2\ne0\). Thus \(G\) is geometrically smooth. Independent complete evaluation at the \(31\) rational points finds ten rational points on \(G\), whose tangent lines cover precisely \(29\), missing the two specified points. The independent replay in `check_witnesses.py` records these checks.

## Verification

Two self-contained public programs reproduce the finite claims without external Python modules or algebra systems. Compile and run `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`; run `python3 check_witnesses.py`. The first lists all \(31+3906+2441406\) scalar classes of degree one through three, with degree-wise maxima \(6,21,29\), confirms no tangent-filling class, and checks the quartic's six-pencil coverage. The second independently checks the quartic and cubic witnesses, including omitted points. Both were executed successfully. The complete enumeration proves only the stated \(\mathbb F_5\) finite-degree obstruction; no claim for arbitrary finite fields is inferred from it.

## Relationship to prior work

Asgarli and Ghioca introduced tangent-filling curves and explicitly asked for the minimum possible degree over a finite field (Question 1.5 of `arXiv:2302.13420`). Their degree-\(q-1\) example requires \(q\ge11\), and the authors note that this displayed example is not tangent-filling for \(q=5\), which does not itself rule out other quartics or cubics. Their general lower bounds do not settle the \(q=5\) degree-three case. Their 2022 joint work with Yip (`arXiv:2208.13299`) concerns blocking by **curve points**, a different condition from coverage by tangent lines. Previously known \(\mathbb F_5\) smooth quartic examples establish the existence direction; the new sharp complete cubic obstruction resolves the minimum-degree question, while the displayed four-term quartic gives a particularly simple six-pencil witness.

## Limitations

The \(29\)-point bound and degree minimum are specific to \(\mathbb F_5\). They are established by a proof-producing exhaustive finite computation whose complete source and search-domain normalization are included. This does not classify curves up to projective isomorphism or compute invariants of all quartics. A historical unindexed small-field calculation could overlap with the sharp obstruction; no mathematical priority or independent validation is asserted.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, `arXiv:2302.13420`, first submitted 2023-02-26; especially Question 1.5, Theorems 1.1–1.3 and Remark 1.4. https://arxiv.org/abs/2302.13420
2. S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, `arXiv:2208.13299`, first submitted 2022-08-28. https://arxiv.org/abs/2208.13299
