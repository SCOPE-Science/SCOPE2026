# Maximal rank-one/full numerical-index separation in an octagonal plane family
## Finding
For \(0\le \xi\le1\), let
\[
X_\xi=(\mathbb R^2,N_\xi),\qquad
N_\xi(x,y)=\max\left\{|x|,|y|,\frac{|x|+|y|}{1+\xi}\right\},
\]
and let \(n(X_\xi)\) and \(n_1(X_\xi)\) denote its numerical index and rank-one numerical index. Then the multiplicative separation
\[
R(\xi)=\frac{n_1(X_\xi)}{n(X_\xi)}
\]
has a unique global maximum at
\[
\xi=\sqrt2-1.
\]
More precisely, with
\[
a=\sqrt5-2,\qquad b=\sqrt2-1,\qquad c=\frac{\sqrt5-1}{2},
\]
one has \(R(\xi)=1\) on \([0,a]\cup[c,1]\), \(R\) is strictly increasing on \([a,b]\), and \(R\) is strictly decreasing on \([b,c]\). Hence
\[
\max_{0\le\xi\le1}R(\xi)
=
\frac{4}{3-\sqrt2+\sqrt{10\sqrt2-13}}
=
1.506878584864220\ldots.
\]
At the unique maximizer \(X_b\) is the regular octagonal plane,
\[
n(X_b)=\sqrt2-1,
\qquad
n_1(X_b)=
\frac{4(\sqrt2-1)}{3-\sqrt2+\sqrt{10\sqrt2-13}}
=
0.624169546700337\ldots.
\]
Thus, within this classical octagonal family, restricting the numerical-index infimum to rank-one operators loses the greatest multiplicative amount exactly at the regular octagon.

## Assumptions and scope
The scalar field is real. For a Banach space \(X\), the numerical index \(n(X)\) is the infimum of the numerical radii of all norm-one operators on \(X\), while \(n_1(X)\) is the same infimum restricted to norm-one rank-one operators. Consequently
\[
n(X)\le n_1(X).
\]
Only the displayed one-parameter family \(X_\xi\), \(0\le\xi\le1\), is considered.

Martín and Merí computed
\[
n(X_\xi)=
\max\left\{\xi,\frac{1-\xi}{1+\xi}\right\}.
\]
Chica and Merí computed the rank-one index. Put
\[
a=\sqrt5-2,\qquad b=\sqrt2-1,\qquad c=\frac{\sqrt5-1}{2}.
\]
Their formula is
\[
n_1(X_\xi)=
\begin{cases}
\dfrac{1-\xi}{1+\xi},&0\le\xi\le a,\\[6pt]
\dfrac{2+2\xi^2}{2+\xi-\xi^2+\sqrt{8\xi-7\xi^2+2\xi^3+\xi^4}},&a\le\xi\le b,\\[8pt]
\dfrac{2+2\xi^2}{1+3\xi+\sqrt{(1+\xi)^2+4\xi^2(1-\xi-\xi^2)}},&b\le\xi\le c,\\[8pt]
\xi,&c\le\xi\le1.
\end{cases}
\]

## Proof
Because
\[
\frac{1-\xi}{1+\xi}=\xi
\quad\Longleftrightarrow\quad
\xi=\sqrt2-1=b,
\]
the full numerical index is
\[
n(X_\xi)=
\begin{cases}
\dfrac{1-\xi}{1+\xi},&0\le\xi\le b,\\[6pt]
\xi,&b\le\xi\le1.
\end{cases}
\]
The displayed formulas immediately give \(R(\xi)=1\) on \([0,a]\cup[c,1]\). It remains to prove strict monotonicity on the two middle intervals.

For \(a\le\xi\le b\), set
\[
Q_-(\xi)=8\xi-7\xi^2+2\xi^3+\xi^4.
\]
Then
\[
R_-(\xi)=
\frac{2(1+\xi^2)(1+\xi)}
{(1-\xi)(2+\xi-\xi^2+\sqrt{Q_-(\xi)})}.
\]
Exact differentiation gives
\[
R_-'(\xi)=
\frac{2A_-(\xi)}
{\sqrt{Q_-(\xi)}(1-\xi)^2
(2+\xi-\xi^2+\sqrt{Q_-(\xi)})^2},
\]
where
\[
A_-(\xi)=P_-(\xi)
-(1+\xi)^2(3\xi^2-2\xi-3)\sqrt{Q_-(\xi)}
\]
and
\[
P_-(\xi)=
\xi^6+13\xi^5-20\xi^4+4\xi^3-\xi^2+23\xi-4.
\]
On \([a,b]\subset[0,1/2]\),
\[
P_-'(\xi)
=
6\xi^5+65\xi^4-80\xi^3+12\xi^2-2\xi+23
\ge 23-80\left(\frac12\right)^3-2\left(\frac12\right)=12.
\]
Also
\[
P_-(a)=16(263\sqrt5-588)>0,
\]
because
\[
5\cdot263^2-588^2=101>0.
\]
Thus \(P_-(\xi)>0\) on \([a,b]\). Moreover \(3\xi^2-2\xi-3<0\) there, so \(A_-(\xi)>0\). Every denominator factor is positive in the open interval, hence
\[
R_-'(\xi)>0
\qquad(a<\xi<b).
\]

For \(b\le\xi\le c\), put
\[
Q_+(\xi)=(1+\xi)^2+4\xi^2(1-\xi-\xi^2).
\]
Then
\[
R_+(\xi)=
\frac{2(1+\xi^2)}
{\xi(1+3\xi+\sqrt{Q_+(\xi)})}.
\]
Differentiation gives
\[
R_+'(\xi)=
\frac{2A_+(\xi)}
{\sqrt{Q_+(\xi)}\,\xi^2
(1+3\xi+\sqrt{Q_+(\xi)})^2},
\]
where
\[
A_+(\xi)=P_+(\xi)
+(\xi^2-6\xi-1)\sqrt{Q_+(\xi)}
\]
and
\[
P_+(\xi)=
4\xi^6+2\xi^5+12\xi^4+11\xi^3-9\xi^2-3\xi-1.
\]
Its second derivative is
\[
P_+''(\xi)
=
2(60\xi^4+20\xi^3+72\xi^2+33\xi-9).
\]
Since \(b>3/11\), this is positive throughout \([b,c]\), so \(P_+\) is convex there. Its endpoint values are
\[
P_+(b)=416-296\sqrt2<0,
\qquad
P_+(c)=32-15\sqrt5<0.
\]
The first inequality follows from
\[
2\cdot37^2-52^2=34>0,
\]
and the second from
\[
5\cdot15^2-32^2=101>0.
\]
Convexity therefore gives \(P_+(\xi)<0\) throughout the interval. Also
\[
\xi^2-6\xi-1<0
\qquad(0\le\xi\le1),
\]
so \(A_+(\xi)<0\), and hence
\[
R_+'(\xi)<0
\qquad(b<\xi<c).
\]

Thus \(R\) rises strictly from \(1\) at \(a\) to its unique maximum at \(b\), then falls strictly back to \(1\) at \(c\). Substitution of \(b=\sqrt2-1\) gives
\[
R(b)=
\frac{4}{3-\sqrt2+\sqrt{10\sqrt2-13}}.
\]
Since \(1+b=\sqrt2\),
\[
N_b(x,y)
=
\max\left\{|x|,|y|,\frac{|x|+|y|}{\sqrt2}\right\},
\]
which is the regular octagonal norm. Multiplying \(R(b)\) by \(n(X_b)=b\) gives the stated value of \(n_1(X_b)\).

## Verification
The two source formulas were checked against the primary full texts. The derivative identities were recomputed symbolically and then reduced to the displayed sign arguments, which are elementary and exact.

For the increasing branch, the only nontrivial polynomial sign is controlled by the exact endpoint value
\[
P_-(a)=16(263\sqrt5-588)>0
\]
and the uniform derivative bound \(P_-'(\xi)\ge12\).

For the decreasing branch, convexity of \(P_+\) and the two exact negative endpoint values give the polynomial sign on the whole interval. No numerical sampling is used as proof of monotonicity or uniqueness.

The decimal values are only evaluations of the proved radical expressions.

## Relationship to prior work
Martín and Merí introduced the relevant octagonal family and computed its ordinary numerical index. Chica and Merí later computed its rank-one numerical index by an explicit four-branch formula. Those two formulas show where the indices agree and where they differ, but the inspected statements do not optimize their ratio or identify a unique maximal separation point.

The ratio
\[
\frac{n_1(X)}{n(X)}
\]
is a direct measure of the multiplicative loss incurred by restricting the numerical-index infimum from all norm-one operators to rank-one operators. Optimizing it across the source family therefore compares the two invariants on exactly the common parameter space for which both are known explicitly.

The unique maximizer is not merely an algebraic breakpoint: it is the parameter \(b=\sqrt2-1\) for which the unit ball becomes a regular Euclidean octagon.

## Limitations
The result is a comparison theorem for this particular one-parameter family. It does not claim that the regular octagon maximizes \(n_1(X)/n(X)\) among all two-dimensional Banach spaces or all octagonal norms.

The originality comparison is bounded by the inspected primary sources and targeted literature-index searches. A differently phrased optimization of the same two formulas could exist outside the checked material.

## References
1. M. Martín and J. Merí, “Numerical index of some polyhedral norms on the plane,” *Linear and Multilinear Algebra* 55 (2007), 175--190, DOI 10.1080/03081080600628323; published online 2006-11-23.
2. M. Chica and J. Merí, “Rank-1 numerical index of some families of norms on the plane,” *Linear and Multilinear Algebra* 63 (2015), 1817--1828, DOI 10.1080/03081087.2014.975670; published online 2014-10-28.
