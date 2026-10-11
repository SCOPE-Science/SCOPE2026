# Rigidity of James extremizers in the regular octagonal Banach plane
## Finding
Let \(X=(\mathbb R^2,N)\) be the real regular-octagonal Banach plane
\[
N(u,v)=\max\left\{|u|,|v|,\frac{|u|+|v|}{\sqrt2}\right\}.
\]
Let
\[
J(X)=\sup_{x,y\in S_X}\min\{N(x+y),N(x-y)\}.
\]
Then \(J(X)=\sqrt2\), and
\[
\min\{N(x+y),N(x-y)\}=\sqrt2
\quad\Longleftrightarrow\quad
y=\pm Qx,
\]
where \(Q(u,v)=(-v,u)\). Consequently every James-extremizing pair satisfies
\[
N(x+y)=N(x-y)=\sqrt2.
\]
Thus the complete equality set consists exactly of Euclidean quarter-turn pairs.

## Assumptions and scope
The scalar field is real. The unit ball is
\[
B_X=\left\{(u,v): |u|\le1,\ |v|\le1,\ |u|+|v|\le\sqrt2\right\}.
\]
The claim concerns the ordinary James constant.

## Proof
Put \(r=\sqrt2-1\). The dihedral symmetry group of the regular octagon lets us move any first unit vector to
\[
x=(1,t),\qquad0\le t\le r,
\]
and, after replacing \(y\) by \(-y\), assume \(y=(a,b)\in S_X\) has \(b\ge0\).

The upper half of the unit sphere consists of five pieces. On the right vertical edge \(y=(1,b)\), \(0\le b\le r\),
\[
N(x-y)=|t-b|\le r<\sqrt2.
\]
On the upper-right slanted edge \(a+b=\sqrt2\), \(r\le a,b\le1\), one has \(b\ge t\) and
\[
x-y=(1-a,t-b).
\]
Here
\[
1-a<\sqrt2,\qquad b-t\le1<\sqrt2,
\]
and
\[
(1-a)+(b-t)=1+\sqrt2-2a-t\le1+\sqrt2-2r<2,
\]
so \(N(x-y)<\sqrt2\).

On the left vertical edge \(y=(-1,b)\),
\[
N(x+y)=t+b\le2r<\sqrt2.
\]
On the upper-left slanted edge \(b=\sqrt2+a\), \(-1\le a\le-r\),
\[
x+y=(1+a,t+\sqrt2+a).
\]
The first coordinate is \(<\sqrt2\), the second is at most \(1+t\le\sqrt2\), and
\[
(1+a)+(t+\sqrt2+a)=1+t+\sqrt2+2a\le1+t+\sqrt2-2r\le2.
\]
Thus \(N(x+y)\le\sqrt2\), with equality in the required bounds only at the endpoint \(a=-r,t=r\), which is also on the top edge.

It remains to take
\[
y=(a,1),\qquad-r\le a\le r.
\]
For \(x+y=(1+a,1+t)\), both coordinates are at most \(\sqrt2\), hence
\[
N(x+y)\ge\sqrt2
\quad\Longleftrightarrow\quad
a+t\ge0.
\]
For \(x-y=(1-a,t-1)\), both coordinate magnitudes are at most \(\sqrt2\), hence
\[
N(x-y)\ge\sqrt2
\quad\Longleftrightarrow\quad
a+t\le0.
\]
Therefore both chord norms are at least \(\sqrt2\) exactly when \(a=-t\). Then
\[
y=(-t,1)=Qx
\]
and direct substitution gives
\[
N(x+y)=N(x-y)=\sqrt2.
\]

Every regular-octagon isometry conjugates \(Q\) to \(Q\) or \(-Q\), so undoing the reduction gives precisely \(y=\pm Qx\). The argument also proves \(J(X)\le\sqrt2\), while quarter-turn pairs attain \(\sqrt2\).

## Verification
The proof is an exhaustive boundary calculation, not finite sampling. After reducing the first vector to one fundamental half-edge, every upper-half boundary piece for the second vector is treated. The only surviving branch is the top edge, where the two extremality conditions reduce to
\[
a+t\ge0,\qquad a+t\le0.
\]
Thus \(a=-t\) is necessary and sufficient.

## Relationship to prior work
Komuro, Saito, and Tanaka identify the regular octagonal norm as a basic non-Hilbert two-dimensional example with James constant \(\sqrt2\), characterize the relevant rotation-invariant class, and discuss regular-octagon norm functions. The inspected full text does not classify all maximizing pairs.

Nilsrakoo and Saejung give earlier exact James-constant work for normalized norms and cite the absolute-norm literature. Their accessible full text does not state the present quarter-turn equality classification.

Targeted searches for regular-octagon James extremizers, equality pairs, quarter-turn pairs, and equivalent \(\pi/2\)-rotation formulations found no equivalent statement.

## Limitations
The theorem is specific to the displayed real regular-octagonal norm and the ordinary James constant.

The earlier 2003 Mitani--Saito paper cited for the regular-octagon calculation was not available in full text through the checked route. A differently phrased equality analysis there remains a bibliographic risk.

## References
1. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” *Mathematische Nachrichten* 289 (2016), 1005--1020, DOI 10.1002/mana.201500238; first published online 2015-11-19.
2. W. Nilsrakoo and S. Saejung, “The James constant of normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2006, Article 26265, DOI 10.1155/JIA/2006/26265; published 2006-05-04.
3. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\), III,” *Mathematical Inequalities & Applications* 20 (2017), 865--887, DOI 10.7153/mia-20-55; MSC 46B20.
