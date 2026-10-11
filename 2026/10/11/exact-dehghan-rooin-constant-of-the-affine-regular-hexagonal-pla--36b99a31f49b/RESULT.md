# Exact Dehghan–Rooin constant of the affine-regular hexagonal plane
## Finding
Let \(X_H=(\mathbb R^2,N)\) be the real affine-regular hexagonal plane
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
For nonzero vectors, let \(\alpha\) be the angular distance and \(\beta\) the skew angular distance in the sense of Fu and Li, and let \(\operatorname{DR}(X_H)\) be the supremum of \(\alpha/\beta\) over pairs for which \(\beta\ne0\). Then
\[
\operatorname{DR}(X_H)=\frac{4\sqrt6}{9}=\sqrt{\frac{32}{27}}.
\]
The supremum is attained. One maximizing choice in the equivalent unit-sphere formulation is
\[
u=(0,1),\qquad v=(1,2/3),\qquad a=\sqrt{2/3}.
\]

## Assumptions and scope
The scalar field is real and the space is exactly the two-dimensional normed space above. Fu and Li proved the equivalent formula
\[
\operatorname{DR}(X)=\sup_{x,y\in S_X,\ a>0,\ a\ne1}
\frac{\|x-y\|}{\|a x-a^{-1}y\|}.
\]
Only this invariant and this hexagonal norm are evaluated here; no formula is asserted for arbitrary hexagonal norms or higher-dimensional spaces.

A convenient representation is
\[
N(s,t)=\operatorname{rng}(0,s,t),
\]
where \(\operatorname{rng}(z_1,z_2,z_3)=\max_i z_i-\min_i z_i\). Adding a common constant to three coordinates or simultaneously permuting them does not change the range. Thus a unit vector can be represented, after a common-coordinate shift and a symmetry of the hexagon, by a triple \((0,r,1)\) with \(0\le r\le1\).

## Proof
Take unit vectors represented by triples \(U,V\) of range one. Write \(q=a^2\). The quotient in the equivalent formula becomes
\[
R(U,V,q)=\frac{\sqrt q\,\operatorname{rng}(U-V)}{\operatorname{rng}(qU-V)}.
\]
Swapping \(U\) and \(V\) replaces \(q\) by \(q^{-1}\) and leaves \(R\) unchanged. Hence it suffices to consider \(0<q\le1\).

Use simultaneous permutation symmetry to put \(U=(0,r,1)\). After shifting \(V\), it is a permutation of \((0,s,1)\). The six relative permutations reduce, under swapping and reversal, to four types.

For the identity type \(V=(0,s,1)\), put \(A=qr-s\), \(B=q-1\), and \(h=r-s\). Since
\[
h=A-rB=(1-r)A+r(A-B),
\]
we have
\[
|h|\le\max\{|A|,|A-B|\}\le\operatorname{rng}(0,A,B).
\]
Therefore \(R\le\sqrt q\le1\).

For the reversal type \(V=(1,s,0)\), the numerator range is \(2\), while the denominator range is at least the distance between \(-1\) and \(q\), namely \(1+q\). Hence
\[
R\le\frac{2\sqrt q}{1+q}\le1.
\]

For the transposition type \(V=(0,1,s)\), set \(x=1-r\), \(y=1-s\), and \(c=1-q\). Then
\[
\operatorname{rng}(U-V)=x+y
\]
and
\[
\operatorname{rng}(qU-V)=qx+\max\{c,y\}.
\]
If \(y\le c\), then for fixed \(x\) the quotient increases with \(y\), so its maximum in that region is at \(y=c\); the resulting function \((x+c)/(qx+c)\) increases with \(x\), so \(x=1\). If \(y\ge c\), then \((x+y)/(qx+y)\) increases with \(x\) and decreases with \(y\), so again \(x=1\) and \(y=c\). Thus in both regions
\[
R\le\sqrt q\,(2-q).
\]

For the cycle type \(V=(s,1,0)\), set \(x=1-r\) and \(m=\max\{s,x\}\). Then
\[
\operatorname{rng}(U-V)=1+m,
\qquad
\operatorname{rng}(qU-V)=\max\{q+s,1+qx\}.
\]
For fixed \(m\), monotonicity of the two denominator branches shows that the smallest possible denominator occurs in one of the boundary choices \((s,x)=(m,0)\) or \((0,m)\). Consequently
\[
R\le\max\left\{
\frac{\sqrt q(1+m)}{\max\{q+m,1\}},
\frac{\sqrt q(1+m)}{1+qm}
\right\}.
\]
The first expression is maximized at \(m=1-q\), giving \(\sqrt q(2-q)\). The second increases with \(m\) and is at most \(2\sqrt q/(1+q)\le1\). Therefore every relative permutation satisfies
\[
R\le\sqrt q(2-q).
\]

Finally,
\[
\left(\sqrt q(2-q)\right)^2=q(2-q)^2,
\]
and on \(0<q\le1\) this is maximized at \(q=2/3\), with value \(32/27\). Hence
\[
\operatorname{DR}(X_H)\le\sqrt{32/27}=\frac{4\sqrt6}{9}.
\]
For equality, take
\[
u=(0,1),\qquad v=(1,2/3),\qquad q=2/3,
\]
so that both vectors have norm one. With \(a=\sqrt q\),
\[
N(u-v)=\frac43,
\qquad
N(a u-a^{-1}v)=\sqrt{\frac32},
\]
and their quotient is \(4\sqrt6/9\). This proves equality.

## Verification
The companion script `verify_exact.py` checks the six relative permutations are assigned to the four symmetry types, verifies the exact maximizing identity
\[
\frac{32}{27}-q(2-q)^2=\frac{(8-3q)(3q-2)^2}{27},
\]
and verifies the rational squared quotient \(32/27\) for the displayed equality configuration. These checks support the algebraic reduction; the infinite quantifiers are discharged by the monotonicity arguments in the proof rather than by enumeration.

## Relationship to prior work
Fu and Li introduced the Dehghan–Rooin constant to quantify the gap between angular and skew angular distances, proved the unit-sphere formula used above, and established its general geometric bounds. Their paper records endpoint examples such as \(\ell_1^2\) and \(\ell_\infty^2\), where the constant equals \(2\), but the inspected text does not evaluate the affine-regular hexagonal plane. Wang, Liu, Xia and Sarfraz later introduced a broader Maligranda–Rooin family whose parameter-zero member is the Dehghan–Rooin constant; their inspected example section treats \(\ell_1\), not this hexagonal model. Searches for the invariant together with the Day–James or affine-regular hexagonal norm did not locate a statement implying the exact value above.

## Limitations
The result is confined to the stated real two-dimensional norm. It does not classify all maximizers, nor does it supply a general formula for the Dehghan–Rooin constant on arbitrary polygonal spaces. Bibliographic searches reduce but cannot eliminate the possibility of an equivalent result under different terminology or in non-indexed literature.

## References
1. Y. Fu and Y. Li, “Geometric constant for quantifying the difference between angular and skew angular distances in Banach spaces,” *Annals of Functional Analysis* 15 (2024), Article 39. DOI: 10.1007/s43034-024-00341-0.
2. Z. Wang, L. Liu, H. Xia and M. Sarfraz, “Maligranda–Rooin constant in Banach spaces,” arXiv:2504.01267.
