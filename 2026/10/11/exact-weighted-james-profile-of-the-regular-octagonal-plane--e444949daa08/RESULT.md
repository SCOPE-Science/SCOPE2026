# Exact weighted James profile of the regular octagonal plane

## Finding
Let \(X_8=(\mathbb R^2,N)\) be the real regular-octagonal Banach plane with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For \(0<\lambda<1\), define the weighted James constant introduced by Liu, Sarfraz and Li by
\[
J(\lambda,X_8)=\sup_{x,y\in S_{X_8}}
\min\left\{N(\lambda x+(1-\lambda)y),N(\lambda x-(1-\lambda)y)\right\}.
\]
If \(m=\min\{\lambda,1-\lambda\}\), then
\[
J(\lambda,X_8)=1-(2-\sqrt2)m.
\]
For \(0<\lambda\le 1/2\), the value is attained by
\[
x=(-(\sqrt2-1),1),\qquad y=(1,\sqrt2-1).
\]
For \(1/2\le\lambda<1\), the symmetric extremizer is obtained by interchanging the parameter weights.

## Assumptions and scope
The space is real and two-dimensional. The norm above has a Euclidean regular octagon as unit ball. The parameter satisfies \(0<\lambda<1\). The result concerns the weighted James constant \(J(\lambda,X)\) from Liu--Sarfraz--Li, not the classical James constant itself and not the distinct Euler--Lagrange or parameterized von Neumann--Jordan constants.

The classical James constant of the regular octagonal plane is
\[
J(X_8)=\sqrt2.
\]
This is a published property of the regular octagonal norm. It is also explicitly used as the defining geometric feature of the regular-octagon model in later exact-constant work.

## Proof
First note the symmetry
\[
J(\lambda,X)=J(1-\lambda,X).
\]
Indeed, interchanging \(x\) and \(y\) leaves the first norm unchanged and changes the second vector only by an overall sign. It therefore suffices to treat \(0<\lambda\le1/2\).

Liu--Sarfraz--Li prove, for every Banach space and \(0<\lambda<1\),
\[
J(\lambda,X)\le \lambda J(X)+|2\lambda-1|.
\]
Since \(J(X_8)=\sqrt2\), for \(0<\lambda\le1/2\) this gives
\[
J(\lambda,X_8)\le \lambda\sqrt2+1-2\lambda
=1-(2-\sqrt2)\lambda.
\]
Set \(r=\sqrt2-1\), and choose the unit vectors
\[
x=(-r,1),\qquad y=(1,r).
\]
Both lie on the unit sphere because
\[
N(x)=N(y)=1.
\]
Put
\[
T=1-(2-\sqrt2)\lambda,
\]
and define
\[
p=\lambda x+(1-\lambda)y,\qquad q=\lambda x-(1-\lambda)y.
\]
Direct expansion gives
\[
p=(1-\sqrt2\lambda,\;r+(2-\sqrt2)\lambda)
\]
and
\[
q=(-T,\;\sqrt2\lambda-r).
\]
For \(0\le\lambda\le1/2\), both coordinates of \(p\) are nonnegative, each is at most \(T\), and
\[
\frac{p_1+p_2}{\sqrt2}=T.
\]
Hence \(N(p)=T\).

For \(q\), the first coordinate has absolute value \(T\). It remains to check the diagonal facet. The required inequality is
\[
|\sqrt2\lambda-r|\le rT.
\]
The sign changes at \(\lambda=1-1/\sqrt2\). On the first subinterval,
\[
rT-(r-\sqrt2\lambda)=2(2-\sqrt2)\lambda\ge0,
\]
and on the second,
\[
rT-(\sqrt2\lambda-r)=2(\sqrt2-1)(1-2\lambda)\ge0.
\]
Thus
\[
\frac{T+|\sqrt2\lambda-r|}{\sqrt2}\le T,
\]
so \(N(q)=T\). Therefore the displayed unit pair yields
\[
J(\lambda,X_8)\ge T.
\]
Together with the published upper bound, this proves equality for \(0<\lambda\le1/2\), and parameter symmetry gives the formula on all of \((0,1)\).

A useful comparison follows immediately. In a Hilbert plane,
\[
J(\lambda,H)=\sqrt{\lambda^2+(1-\lambda)^2}.
\]
For \(0<\lambda<1/2\),
\[
\bigl(1-(2-\sqrt2)\lambda\bigr)^2-
\bigl(\lambda^2+(1-\lambda)^2\bigr)
=2(\sqrt2-1)\lambda(1-2\lambda)>0.
\]
Hence the full weighted profile separates the regular octagon from the Euclidean plane although both have classical James constant \(\sqrt2\).

## Verification
The upper bound is an application of Theorem 5.2 in the defining 2021 article, together with the independently published identity \(J(X_8)=\sqrt2\). The lower bound is completely explicit and uses only exact arithmetic in \(\mathbb Q(\sqrt2)\). The bundled checker replays the algebraic identities, the piecewise facet inequalities, the symmetry reduction and the Hilbert-profile comparison; the analytic proof above does not depend on numerical sampling.

## Relationship to prior work
Liu, Sarfraz and Li introduced \(J(\lambda,X)\) in 2021, proved its universal bounds, and related it to the classical James constant. Their Theorem 5.2 supplies the upper inequality used here, but their article does not give this exact regular-octagon profile.

Komuro, Saito and Tanaka's work on spaces with classical James constant \(\sqrt2\) identifies the regular octagonal norm as a canonical non-Euclidean two-dimensional example. A later Filomat paper computes exact \(L_{YJ}(\lambda,\mu,X)\) and \(L'_{YJ}(\lambda,\mu,X)\) values for the regular octagon and explicitly works in the regime \(J(X)=\sqrt2\), but those are different sum-of-squares functionals. Targeted searches for the weighted minimum functional, parameter symmetry, the exact affine formula, and regular-octagon aliases located no statement that covers the result above.

The result shows that the regular octagon saturates the source paper's \(J(X)\)-based upper estimate at every parameter after symmetry. This is stronger information than the single classical value at \(\lambda=1/2\), and it distinguishes two canonical spaces sharing the same classical James constant.

## Limitations
The theorem is restricted to the real regular octagonal plane and to the weighted James functional defined above. It does not classify all two-dimensional norms with classical James constant \(\sqrt2\), nor does it claim that equality in the general upper bound characterizes regular octagons. Bibliographic searches cannot exclude every unindexed or differently phrased source; the residual originality risk is therefore nonzero.

## References
1. Q. Liu, M. Sarfraz, Y. Li, “Some aspects of generalized Zbăganu and James constant in Banach spaces,” Demonstratio Mathematica 54 (2021), 299–310, DOI 10.1515/dema-2021-0033. Published 16 August 2021. Primary MSC 46B20.
2. N. Komuro, K.-S. Saito, R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” Mathematische Nachrichten 289 (2016), 1005–1020, DOI 10.1002/mana.201500238. First published 19 November 2015.
3. X. Yang, H. Li, C. Yang, “On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space,” Filomat 38 (2024), 1583–1593, DOI 10.2298/FIL2405583Y. Primary MSC 46B20.
