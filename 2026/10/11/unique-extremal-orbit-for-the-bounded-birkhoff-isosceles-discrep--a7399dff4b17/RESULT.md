# Unique extremal orbit for the bounded Birkhoff--isosceles discrepancy of the Day--James hexagon
## Finding
Let \(X=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Define
\[
IB'(X)=\inf\left\{\inf_{\lambda\in\mathbb R}N(x+\lambda y):x\in S_X,\ 0<N(y)\le1,\ N(x+y)=N(x-y)\right\}.
\]
Then
\[
IB'(X)=D(X)=\frac89,
\]
where \(D(X)\) is the same infimum with \(x,y\in S_X\). Every pair attaining \(IB'(X)\) has \(N(y)=1\), and, up to a linear isometry of \(X\) and replacement of \(y\) by \(-y\), the unique extremal pair is
\[
x=\left(1,\frac23\right),\qquad y=\left(\frac13,-\frac23\right).
\]

## Assumptions and scope
The scalar field is real. The norm is the affine-regular hexagonal realization of the Day--James endpoint \(\ell_\infty-\ell_1\). The claim concerns only \(IB'(X)\) and \(D(X)\).

## Proof
The unit ball has vertices
\[
(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1),
\]
and the dual norm is
\[
N^*(a,b)=\max\{|a|,|b|,|a+b|\}.
\]
For \(y\ne0\), the functional \(z\mapsto\det(z,y)\) has dual norm \(N(y)\). Hence
\[
\inf_{\lambda\in\mathbb R}N(x+\lambda y)=\frac{|\det(x,y)|}{N(y)}.
\]
Write \(y=ru\), with \(0<r\le1\) and \(u\in S_X\). The quantity to minimize is then \(|\det(x,u)|\).

Dihedral symmetry lets us take
\[
x=(1,t),\qquad0\le t\le1.
\]
After allowing \(u\mapsto-u\), the normalized direction \(u\) lies on one of three relative edges:
\[
E_0:\ u=(1,s),\quad
E_1:\ u=(1-s,-s),\quad
E_2:\ u=(-s,-1),
\qquad0\le s\le1.
\]

For \(E_0\), no nonzero isosceles solution exists because \(N(x+ru)\ge1+r\) while \(N(x-ru)\le1\).

For \(E_1\),
\[
N(x+ru)=1+r-\min\{rs,t\},\qquad
N(x-ru)=rs+\max\{1-r,t\}.
\]
The isosceles equation either gives \(|\det(x,u)|=s+t-st=1\), or implies
\[
s+t\le3st.
\]
Set \(a=1-s\), \(b=1-t\), \(q=\sqrt{ab}\). Then
\[
0\le1-2a-2b+3ab\le1-4q+3q^2=(1-q)(1-3q).
\]
In a nontrivial case \(q<1\), so \(q\le1/3\), and
\[
|\det(x,u)|=1-ab\ge\frac89.
\]
Equality forces \(s=t=2/3\), and the isosceles equation forces \(r=1\).

For \(E_2\),
\[
N(x+ru)=
\begin{cases}
1-rs,&t\ge r,\\
1-t+r(1-s),&r>t,
\end{cases}
\qquad
N(x-ru)=\max\{1+rs,t+r\}.
\]
If \(t\ge r\), isosceles equality forces \(s=0\), giving determinant ratio \(1\). Every other nontrivial isosceles case implies
\[
1-2s-2t+3st\ge0.
\]
With \(q=\sqrt{st}\),
\[
0\le1-2s-2t+3st\le(1-q)(1-3q),
\]
so \(q\le1/3\), and
\[
|\det(x,u)|=1-st\ge\frac89.
\]
Equality forces \(s=t=1/3\) and \(r=1\).

The pair
\[
x=\left(1,\frac23\right),\qquad
y=\left(\frac13,-\frac23\right)
\]
has \(N(x)=N(y)=1\), \(N(x+y)=N(x-y)=4/3\), and line distance \(8/9\). The map
\[
T(s,t)=(s,s-t)
\]
is an isometry and carries this equality chamber to the second one after \(y\mapsto-y\). Thus there is one equality orbit. Since the extremizer has \(N(y)=1\), the same value is attained in \(D(X)\).

## Verification
The edge reduction is exhaustive. The line-distance identity follows exactly from the dual norm. The two lower bounds use only active-branch identities and \(a+b\ge2\sqrt{ab}\). Equality in that inequality forces the displayed parameters. No numerical search is used as proof.

## Relationship to prior work
Yang and Wang studied the same Day--James endpoint for a different von Neumann--Jordan-type invariant.

Mizuguchi introduced \(IB\) and \(IB'\). For the Day--James family, the inspected paper gives the parameter \(2/3\) witness and the one-sided bound \(IB'\le8/9\), but it does not prove the matching bounded-domain lower bound or classify equality pairs.

Later Dunkl--Williams theory gives strong indirect scalar coverage for the related unbounded constant \(IB\). Such scalar information does not imply that every bounded \(IB'\)-minimizer has unit second vector or belongs to one dihedral orbit.

## Limitations
The theorem is specific to the affine-regular hexagonal endpoint. The scalar value \(8/9\) is not presented as the sole novelty; the new content is the bounded-domain lower bound and complete equality classification. A differently worded prior classification remains a bibliographic risk.

## References
1. Y. Yang and F. Wang, “On a new geometric constant related to the von Neumann--Jordan constant,” *Journal of Mathematical Analysis and Applications* 324 (2006), 555--563, DOI 10.1016/j.jmaa.2005.12.009; available online 2006-01-18.
2. H. Mizuguchi, “The Constants to Measure the Differences Between Birkhoff and Isosceles Orthogonalities,” *Filomat* 30 (2016), 2761--2770, DOI 10.2298/FIL1610761M.
3. Y. Fu, H. Xie, and Y. Li, “The Dunkl-Williams constant related to the Singer orthogonality and red isosceles orthogonality in Banach spaces,” *Filomat* 37 (2023), 5601--5622, DOI 10.2298/FIL2317601F.
