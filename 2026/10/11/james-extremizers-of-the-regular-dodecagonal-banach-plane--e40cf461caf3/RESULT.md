# James extremizers of the regular dodecagonal Banach plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\) have unit ball equal to the regular Euclidean dodecagon with vertices
\[
v_k=\left(\cos\frac{k\pi}{6},\sin\frac{k\pi}{6}\right),
\qquad k=0,\ldots,11.
\]
For the James constant
\[
J(X_{12})=\sup_{x,y\in S_{X_{12}}}\min\{N_{12}(x+y),N_{12}(x-y)\},
\]
one has
\[
J(X_{12})=\frac{\sqrt2}{\cos(\pi/12)}=2(\sqrt3-1).
\]
Moreover,
\[
\min\{N_{12}(x+y),N_{12}(x-y)\}=2(\sqrt3-1)
\]
holds if and only if, for some \(k\in\{0,\ldots,11\}\),
\[
x=v_k,\qquad y=\pm v_{k+3},
\]
with indices taken modulo \(12\). Thus the James extremizers are exactly the Euclidean-orthogonal vertex pairs, and every extremizer is isosceles:
\[
N_{12}(x+y)=N_{12}(x-y)=2(\sqrt3-1).
\]

## Assumptions and scope
The scalar field is real. The unit ball \(P\) is the regular dodecagon inscribed in the Euclidean unit circle, so its vertices are
\[
v_k=\left(\cos\frac{k\pi}{6},\sin\frac{k\pi}{6}\right),
\qquad k=0,\ldots,11.
\]
Its apothem is
\[
c=\cos\frac{\pi}{12}.
\]
The norm \(N_{12}\) is the Minkowski functional of \(P\). The theorem concerns the ordinary James constant and its complete equality set.

## Proof
Because \(P\) is a regular dodecagon inscribed in the Euclidean unit disk \(B_2\), and its incircle has radius \(c\),
\[
cB_2\subseteq P\subseteq B_2.
\]
Hence for every \(z\in\mathbb R^2\),
\[
\|z\|_2\le N_{12}(z)\le\frac{\|z\|_2}{c}.
\]

Take \(x,y\in S_{X_{12}}\). Since \(P\subseteq B_2\),
\[
\|x\|_2\le1,\qquad \|y\|_2\le1.
\]
Therefore
\[
\min\{N_{12}(x+y),N_{12}(x-y)\}
\le
\frac1c\min\{\|x+y\|_2,\|x-y\|_2\}.
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
and consequently
\[
J(X_{12})\le\frac{\sqrt2}{c}.
\]

For the reverse inequality, take
\[
x=v_0=(1,0),\qquad y=v_3=(0,1).
\]
The vectors \(x+y\) and \(x-y\) have Euclidean length \(\sqrt2\) and directions \(\pi/4\) and \(-\pi/4\). These are outward-normal directions of dodecagon edges, so the radial distance from the origin to \(P\) in either direction is exactly \(c\). Hence
\[
N_{12}(x+y)=N_{12}(x-y)=\frac{\sqrt2}{c}.
\]
Since
\[
\frac{\sqrt2}{\cos(\pi/12)}
=
2(\sqrt3-1),
\]
the asserted value follows.

It remains to classify equality. Suppose
\[
\min\{N_{12}(x+y),N_{12}(x-y)\}=\frac{\sqrt2}{c}.
\]
Then both \(N_{12}(x+y)\) and \(N_{12}(x-y)\) are at least \(\sqrt2/c\). The comparison inequality gives
\[
\|x+y\|_2\ge\sqrt2,\qquad
\|x-y\|_2\ge\sqrt2.
\]
Their squared sum is at most \(4\), so equality must hold everywhere:
\[
\|x+y\|_2=\|x-y\|_2=\sqrt2,
\qquad
\|x\|_2=\|y\|_2=1.
\]
The equality of the two Euclidean chord lengths gives
\[
\langle x,y\rangle=0.
\]
The only points of \(P\) lying on the Euclidean unit circle are the twelve vertices, because every open polygon edge lies strictly inside that circle. Thus \(x\) and \(y\) are vertices. Euclidean orthogonality among dodecagon vertices means precisely
\[
x=v_k,\qquad y=\pm v_{k+3}
\]
for some \(k\).

Conversely, every such orthogonal vertex pair has sum and difference in edge-normal directions, so both normed chord lengths equal \(\sqrt2/c\). This proves the complete equality classification.

## Verification
The upper bound uses only the exact inclusions
\[
cB_2\subseteq P\subseteq B_2
\]
and the Euclidean parallelogram identity. No sampling is involved.

For equality, every inequality in the comparison chain is forced to equality. This first forces both unit vectors onto the Euclidean circumcircle, hence onto vertices of \(P\), and then forces Euclidean orthogonality. The converse is checked by the exact angular relation
\[
\frac{\pi}{4}
=
\frac{\pi}{12}+\frac{\pi}{6},
\]
so the sum and difference of an orthogonal vertex pair lie on edge-normal rays.

## Relationship to prior work
Komuro, Saito, and Tanaka study two-dimensional Banach spaces with James constant \(\sqrt2\). Their 2015 paper characterizes the symmetric absolute norms at that endpoint and highlights the regular octagon as a canonical non-Euclidean example. Their later continuation states that a \(\pi/2\)-rotation-invariant plane has James constant \(\sqrt2\) exactly when it is also \(\pi/4\)-rotation invariant.

A regular dodecagonal norm has \(\pi/2\)-rotation symmetry but not \(\pi/4\)-rotation symmetry, so the cited characterization implies only the strict inequality
\[
J(X_{12})>\sqrt2.
\]
It does not give the exact value \(2(\sqrt3-1)\), nor the equality-pair classification. Targeted searches for regular-dodecagon James constants, equality cases, orthogonal vertex extremizers, and quarter-turn formulations found no statement equivalent to the theorem above.

## Limitations
The theorem is specific to the regular dodecagonal plane. It does not assert a formula for every regular polygonal norm.

The 2015 publisher page exposed the abstract, references, and first-publication date, but its full-text route was unavailable in the checked access path. The complete 2017 continuation was inspected and contains the \(\pi/2\)- versus \(\pi/4\)-rotation characterization and a detailed regular-octagon discussion, but no dodecagon occurrence. An older unindexed polygonal-norm calculation remains a residual bibliographic risk.

## References
1. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” *Mathematische Nachrichten* 289 (2016), 1005--1020, DOI 10.1002/mana.201500238; first published online 2015-11-19.
2. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\), III,” *Mathematical Inequalities & Applications* 20 (2017), 865--887, DOI 10.7153/mia-20-55; MSC 46B20.
