# Schäffer rigidity in the regular octagonal Banach plane
## Finding
Let \(X=(\mathbb R^2,N)\) be the real regular-octagonal Banach plane
\[
N(u,v)=\max\left\{|u|,|v|,\frac{|u|+|v|}{\sqrt2}\right\}.
\]
For the Schäffer nonsquare constant
\[
C_S(X)=\inf_{x,y\in S_X}\max\{N(x+y),N(x-y)\},
\]
one has \(C_S(X)=\sqrt2\). More strongly,
\[
\max\{N(x+y),N(x-y)\}=\sqrt2
\quad\Longleftrightarrow\quad
y=\pm Qx,
\]
where \(Q(u,v)=(-v,u)\) is Euclidean quarter-turn rotation. Hence every Schäffer-minimizing pair is automatically isosceles,
\[
N(x+y)=N(x-y)=\sqrt2,
\]
and the Schäffer minimizers coincide exactly with the James-maximizing pairs in this regular-octagonal plane.

## Assumptions and scope
The scalar field is real. The unit ball is the regular octagon
\[
B_X=\left\{(u,v): |u|\le1,\ |v|\le1,\ |u|+|v|\le\sqrt2\right\}.
\]
The theorem concerns the ordinary Schäffer nonsquare constant, not a Birkhoff-restricted variant. The scalar value \(C_S(X)=\sqrt2\) is already forced by classical nonsquare-constant identities together with the known value of the James constant; the new content here is the complete equality-pair classification.

## Proof
Put
\[
r=\sqrt2-1.
\]
The dihedral isometry group of the regular octagon lets us apply one common linear isometry to \(x\) and \(y\) so that
\[
x=(1,t),\qquad 0\le t\le r.
\]
Replacing \(y\) by \(-y\) does not change
\(\max\{N(x+y),N(x-y)\}\), so write \(y=(a,b)\in S_X\) with \(b\ge0\).

The upper half of the unit sphere consists of five boundary pieces.

On the right vertical edge, \(y=(1,b)\) with \(0\le b\le r\). Then
\[
N(x+y)=N(2,t+b)=2,
\]
because \(t+b\le2r\) and \((2+t+b)/\sqrt2\le2\). Thus no equality at \(\sqrt2\) occurs there.

On the upper-right slanted edge, \(a+b=\sqrt2\) with \(r\le a,b\le1\). Since the first coordinate of \(x+y\) is \(1+a\ge\sqrt2\), equality could only begin at \(a=r\). At that endpoint \(b=1\), but then
\[
\frac{|1+r|+|t+1|}{\sqrt2}
=
\frac{2+r+t}{\sqrt2}
>
\sqrt2.
\]
Hence throughout this slanted edge,
\[
N(x+y)>\sqrt2.
\]

On the top horizontal edge,
\[
y=(a,1),\qquad -r\le a\le r.
\]
For \(x+y=(1+a,1+t)\), both coordinates have magnitude at most \(\sqrt2\), so
\[
N(x+y)\le\sqrt2
\quad\Longleftrightarrow\quad
\frac{2+a+t}{\sqrt2}\le\sqrt2
\quad\Longleftrightarrow\quad
a+t\le0.
\]
For \(x-y=(1-a,t-1)\), again both coordinate magnitudes are at most \(\sqrt2\), so
\[
N(x-y)\le\sqrt2
\quad\Longleftrightarrow\quad
\frac{2-a-t}{\sqrt2}\le\sqrt2
\quad\Longleftrightarrow\quad
a+t\ge0.
\]
Therefore
\[
\max\{N(x+y),N(x-y)\}\le\sqrt2
\]
holds exactly when \(a=-t\). In that case
\[
y=(-t,1)=Qx
\]
and both chord norms are exactly \(\sqrt2\).

On the upper-left slanted edge, write
\[
b=\sqrt2+a,\qquad -1\le a\le-r.
\]
The first coordinate of \(x-y\) is \(1-a\ge\sqrt2\), with equality only when \(a=-r\). At that endpoint \(b=1\), and
\[
\frac{|1+r|+|t-1|}{\sqrt2}
=
\frac{2+r-t}{\sqrt2}.
\]
This exceeds \(\sqrt2\) unless \(t=r\). When \(a=-r\) and \(t=r\), the point lies on the top-edge equality branch and \(y=Qx\).

Finally, on the left vertical edge \(y=(-1,b)\),
\[
N(x-y)=N(2,t-b)=2.
\]
Thus every unit pair satisfies
\[
\max\{N(x+y),N(x-y)\}\ge\sqrt2,
\]
and equality in the reduced fundamental domain occurs exactly for \(y=Qx\). Undoing the dihedral reduction replaces \(Q\) at most by \(-Q\), so globally the equality condition is
\[
y=\pm Qx.
\]
The quarter-turn pairs therefore attain the infimum, proving \(C_S(X)=\sqrt2\) and the complete equality classification.

## Verification
The proof exhausts one dihedral fundamental half-edge for the first unit vector and all five upper-half boundary pieces for the second. No finite sample is used as proof.

The decisive top-edge calculation is the pair of opposite conditions
\[
a+t\le0,
\qquad
a+t\ge0,
\]
which forces \(a=-t\). The only potential equality point arising from the left slanted edge is its shared endpoint with the top edge and is already the quarter-turn case.

For a quarter-turn pair \(y=Qx\), the proof gives directly
\[
N(x+y)=N(x-y)=\sqrt2.
\]

## Relationship to prior work
Gao and Lau introduced the James and Schäffer nonsquare constants. Yan records the classical product identity
\[
C_J(X)C_S(X)=2
\]
and the equivalent isosceles formulations of both constants. Consequently the scalar value \(C_S(X)=\sqrt2\) follows once \(C_J(X)=\sqrt2\) is known.

Komuro, Saito, and Tanaka treat the regular octagon as a canonical non-Hilbert plane with James constant \(\sqrt2\), and their complete public article studies the associated rotation-invariant framework. A full-text search of that article found no Schäffer discussion or pair-level Schäffer equality classification.

The present result adds the equality geometry: every Schäffer minimizer is a quarter-turn pair, and there are no other minimizers. In particular, in this norm the complete Schäffer-minimizer set coincides with the complete James-maximizer set, a conclusion not implied by the scalar product identity alone.

## Limitations
The theorem is specific to the displayed real regular-octagonal norm. It does not assert that all two-dimensional norms with \(C_J=C_S=\sqrt2\) have the same equality set.

The 2003 Mitani--Saito paper on James constants of absolute norms was not available in full text through the checked route. Its accessible abstract is James-focused and does not state a Schäffer equality classification, but a differently phrased equality analysis there remains a residual bibliographic risk.

## References
1. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” *Mathematische Nachrichten* 289 (2016), 1005--1020, DOI 10.1002/mana.201500238; first published online 2015-11-19.
2. Y. Yan, “On the Nonsquare Constants of Orlicz Spaces with Orlicz Norm,” *Canadian Journal of Mathematics* 55 (2003), 204--224, DOI 10.4153/CJM-2003-009-1.
3. W. Nilsrakoo and S. Saejung, “The James constant of normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2006, Article 26265, DOI 10.1155/JIA/2006/26265; published 2006-05-04.
4. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\), III,” *Mathematical Inequalities & Applications* 20 (2017), 865--887, DOI 10.7153/mia-20-55; MSC 46B20.
