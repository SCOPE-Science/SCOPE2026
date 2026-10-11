# James constants and extremizers of regular \(8k+4\)-gonal Banach planes
## Finding
For every odd integer \(m\ge1\), let \(X_m=(\mathbb R^2,N_m)\) have unit ball equal to the regular Euclidean \(4m\)-gon with vertices
\[
v_j=\left(\cos\frac{j\pi}{2m},\sin\frac{j\pi}{2m}\right),
\qquad j=0,\ldots,4m-1.
\]
Then
\[
J(X_m)=\sqrt2\,\sec\frac{\pi}{4m}.
\]
Moreover,
\[
\min\{N_m(x+y),N_m(x-y)\}
=
\sqrt2\,\sec\frac{\pi}{4m}
\]
for \(x,y\in S_{X_m}\) if and only if
\[
x=v_j,\qquad y=\pm v_{j+m}
\]
for some \(j\), with indices modulo \(4m\). Hence the James extremizers are exactly the Euclidean-orthogonal vertex pairs, and every extremizer is isosceles.

## Assumptions and scope
The scalar field is real. The regular \(4m\)-gon is normalized to have Euclidean circumradius \(1\). Since \(m\) is odd, these are precisely the regular polygons whose numbers of sides are congruent to \(4\) modulo \(8\).

Write
\[
c_m=\cos\frac{\pi}{4m}
\]
for the apothem. The James constant is
\[
J(X_m)=
\sup_{x,y\in S_{X_m}}
\min\{N_m(x+y),N_m(x-y)\}.
\]

## Proof
Let \(P_m\) be the unit ball. Because \(P_m\) is a regular \(4m\)-gon with Euclidean circumradius \(1\) and apothem \(c_m\),
\[
c_m B_2\subseteq P_m\subseteq B_2.
\]
Therefore, for every \(z\in\mathbb R^2\),
\[
\|z\|_2\le N_m(z)\le \frac{\|z\|_2}{c_m}.
\]

Take \(x,y\in S_{X_m}\). Since \(P_m\subseteq B_2\),
\[
\|x\|_2\le1,\qquad \|y\|_2\le1.
\]
Hence
\[
\min\{N_m(x+y),N_m(x-y)\}
\le
\frac1{c_m}
\min\{\|x+y\|_2,\|x-y\|_2\}.
\]
The Euclidean parallelogram identity gives
\[
\|x+y\|_2^2+\|x-y\|_2^2
=
2\|x\|_2^2+2\|y\|_2^2
\le4.
\]
Thus
\[
\min\{\|x+y\|_2,\|x-y\|_2\}\le\sqrt2,
\]
so
\[
J(X_m)\le \frac{\sqrt2}{c_m}.
\]

Now take
\[
x=v_j,\qquad y=v_{j+m}.
\]
The two vertices differ in Euclidean angle by \(\pi/2\), so
\[
\|x+y\|_2=\|x-y\|_2=\sqrt2.
\]
Their sum and difference point in directions
\[
\frac{j\pi}{2m}\pm\frac{\pi}{4}.
\]
The outward normal directions to the polygon edges are
\[
\frac{(2r+1)\pi}{4m},
\qquad r\in\mathbb Z.
\]
Because \(m\) is odd,
\[
\frac{j\pi}{2m}+\frac{\pi}{4}
=
\frac{(2j+m)\pi}{4m}
\]
and \(2j+m\) is odd; the same holds for the difference direction. Hence both \(x+y\) and \(x-y\) lie on edge-normal rays. Along every such ray the boundary radius of \(P_m\) is the apothem \(c_m\). Therefore
\[
N_m(x+y)=N_m(x-y)=\frac{\sqrt2}{c_m},
\]
which proves
\[
J(X_m)=\sqrt2\,\sec\frac{\pi}{4m}.
\]

For the equality classification, suppose
\[
\min\{N_m(x+y),N_m(x-y)\}=\frac{\sqrt2}{c_m}.
\]
Then the upper comparison \(N_m(z)\le\|z\|_2/c_m\) forces
\[
\|x+y\|_2\ge\sqrt2,\qquad
\|x-y\|_2\ge\sqrt2.
\]
The parallelogram identity and \(\|x\|_2,\|y\|_2\le1\) force equality throughout:
\[
\|x+y\|_2=\|x-y\|_2=\sqrt2,
\qquad
\|x\|_2=\|y\|_2=1.
\]
The only points of a regular inscribed polygon lying on the Euclidean unit circle are its vertices, so \(x\) and \(y\) are vertices. Equality of the two Euclidean chord lengths gives
\[
\langle x,y\rangle=0.
\]
Euclidean orthogonality among the vertices is exactly
\[
x=v_j,\qquad y=\pm v_{j+m}.
\]
The converse was already verified above. This completes the proof.

## Verification
The proof uses only the exact Euclidean sandwich
\[
c_mB_2\subseteq P_m\subseteq B_2
\]
and the Euclidean parallelogram identity.

The parity condition is essential. When \(m\) is odd, a quarter-turn vertex pair has sum and difference on edge-normal rays because \(2j+m\) is odd. For even \(m\), the same directions are vertex rays instead, and the endpoint theory for \(\pi/4\)-rotation-invariant norms gives the different value \(J=\sqrt2\).

The equality proof is exhaustive: attaining the upper bound forces both unit vectors onto the Euclidean circumcircle, hence onto polygon vertices, and then forces Euclidean orthogonality.

## Relationship to prior work
Komuro, Saito, and Tanaka study two-dimensional Banach spaces with James constant \(\sqrt2\). Their 2015 paper characterizes the symmetric absolute norms at that endpoint and highlights the regular octagon as a basic non-Euclidean example. Their 2017 continuation records the rotation-invariant criterion: if a norm is \(\pi/2\)-rotation invariant, then its James constant equals \(\sqrt2\) exactly when the norm is also \(\pi/4\)-rotation invariant.

Every regular \(4m\)-gonal norm is \(\pi/2\)-rotation invariant. When \(m\) is odd it is not \(\pi/4\)-rotation invariant, so the cited criterion yields only
\[
J(X_m)>\sqrt2.
\]
It does not determine the exact value, its dependence on \(m\), or the complete maximizing-pair set. The formula above quantifies the whole \(8k+4\) residue class and identifies every extremizer.

Targeted searches for regular-polygon James constants, exact formulas, quarter-turn extremizers, and orthogonal-vertex equality sets found no statement equivalent to this family theorem.

## Limitations
The theorem covers only regular polygons with \(8k+4\) sides. It does not assert a unified formula for all regular polygons.

The strongest checked primary literature concerns the James-\(\sqrt2\) endpoint rather than exact values above the endpoint. A differently phrased historical regular-polygon calculation outside the checked sources remains a bibliographic risk.

## References
1. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” *Mathematische Nachrichten* 289 (2016), 1005--1020, DOI 10.1002/mana.201500238; first published online 2015-11-19.
2. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\), III,” *Mathematical Inequalities & Applications* 20 (2017), 865--887, DOI 10.7153/mia-20-55; primary MSC 46B20.
