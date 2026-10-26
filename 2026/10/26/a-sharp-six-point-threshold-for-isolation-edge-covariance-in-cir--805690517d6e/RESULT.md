# A sharp six-point threshold for isolation–edge covariance in circular geometric graphs

## Finding

Let \(n\ge2\) points be sampled independently and uniformly on a circle of circumference one, and connect two points when their circular geodesic distance is less than \(r\), with \(0<r<1/2\). Write \(I\) for the number of isolated vertices and \(E\) for the total number of edges. Define \(L=1-2r\) and
\[
\psi(r)=\begin{cases}
1-\left(1-\dfrac{r}{1-2r}\right)^2,&0<r<1/3,\\
1,&1/3\le r<1/2.
\end{cases}
\]
For every integer \(n\ge2\), the exact mixed covariance is
\[
\operatorname{Cov}(I,E)=n(n-1)L^{n-1}\left(\frac{n-2}{2}\psi(r)-nr\right).
\]
In particular, on the two radius intervals,
\[
\operatorname{Cov}(I,E)=\begin{cases}
\dfrac{n(n-1)}2 rL^{n-3}\bigl[-4+(3n+10)r-8nr^2\bigr],&0<r<1/3,\\[5pt]
\dfrac{n(n-1)}2L^{n-1}(n-2-2nr),&1/3\le r<1/2.
\end{cases}
\]

**Sharp sign classification.** For \(2\le n\le5\), this covariance is strictly negative for every \(0<r<1/2\). For every \(n\ge6\), define
\[
r_-(n)=\frac{3n+10-\sqrt{9n^2-68n+100}}{16n},\qquad
r_+(n)=\frac{n-2}{2n}.
\]
Then \(0<r_-(n)<r_+(n)<1/2\), and the covariance is negative for \(0<r<r_-(n)\), positive for \(r_-(n)<r<r_+(n)\), and negative for \(r_+(n)<r<1/2\). Its only interior zeros are these two simple roots. At the first admissible size, \(n=6\), the roots are exactly \(1/4\) and \(1/3\). Consequently six vertices are necessary and sufficient for a positive isolation–edge covariance at some radius.

## Assumptions and scope

The points are labeled and independent with uniform law on the one-dimensional torus \(\mathbb R/\mathbb Z\). The graph is the hard-cutoff geometric graph, not a soft connection graph or a fixed-edge random graph. All randomness is from vertex locations, not independently sampled edges. The strict inequality defining an edge can be replaced by a nonstrict one without affecting any probability. The theorem applies to every integer \(n\ge2\) and every real radius \(0<r<1/2\); both limiting endpoints are excluded. The covariance concerns two *different global statistics*, the isolated-vertex count and total edge count.

## Proof

For vertex \(1\), let \(A_1\) be the event that it is isolated. By rotation invariance, fix its position at zero. All other points must avoid the two-sided arc of total length \(2r\). Thus
\[
\Pr(A_1)=(1-2r)^{n-1}=L^{n-1}.
\]
Conditional on \(A_1\), the remaining \(n-1\) vertices are independent and uniform on the complementary **single interval of length** \(L\). No pair inside that interval can be connected by traversing the excluded arc around the conditioned vertex: that route has length at least \(2r>r\). Hence their graph edge condition is exactly that their ordinary distance within the interval is below \(r\).

For two independent uniform points in an interval of length \(L\), integrating the two triangular regions outside the strip of width \(r\) gives
\[
\Pr(|U-V|<r)=\begin{cases}
1-(1-r/L)^2,&r<L,\\
1,&r\ge L.
\end{cases}
\]
The change \(r=L\) occurs at \(r=1/3\), yielding \(\psi(r)\). Since no edge touching vertex \(1\) survives under \(A_1\), we have
\[
\mathbb E[E\mid A_1]=\binom{n-1}{2}\psi(r).
\]
Unconditionally the two sampled points are within circular distance \(r\) with probability \(2r\), so \(\mathbb EE=n(n-1)r\). By linearity of \(I=\sum_{j=1}^n\mathbf1_{A_j}\), exchangeability and the covariance identity,
\[
\begin{aligned}
\operatorname{Cov}(I,E)
&=n\Pr(A_1)\bigl(\mathbb E[E\mid A_1]-\mathbb EE\bigr)\\
&=n(n-1)L^{n-1}\left(\frac{n-2}{2}\psi(r)-nr\right).
\end{aligned}
\]
Substituting the two formulas for \(\psi\) gives the stated piecewise polynomials, with matching values at \(r=1/3\). Every prefactor multiplying their respective sign polynomials is strictly positive on the stated open intervals.

For \(r<1/3\), put \(Q_n(r)=-4+(3n+10)r-8nr^2\). For each such \(r\), \(Q_n(r)\) strictly increases with \(n\), because its increment is \(r(3-8r)>0\). Since \(Q_5(r)=-4+25r-40r^2<0\) for every real \(r\) (discriminant \(-15\)), all \(n\le5\) have strictly negative covariance on this interval. For \(r\ge1/3\), the sign comes from \(n-2-2nr\le(n-6)/3<0\) when \(n\le5\). Thus the claimed strict negativity holds for every \(n\le5\).

For \(n=6\), one has \(Q_6(r)=-4(1-3r)(1-4r)\), with its sole root strictly below \(1/3\) at \(r=1/4\). The upper-radius sign factor \(4-12r\) has its sole root at \(r=1/3\). Both change sign and are simple roots of the continuous covariance function.

For \(n\ge7\), \(Q_n(0)=-4\) and \(Q_n(1/3)=(n-6)/9>0\). Since \(Q_n\) is concave quadratic, it has exactly one root in \((0,1/3)\), namely its smaller quadratic root \(r_-(n)\). The other quadratic root is greater than \(1/3\) and is outside the low-radius branch. On \([1/3,1/2)\) the linear sign factor has its unique zero at \(r_+(n)=(n-2)/(2n)\), which is greater than \(1/3\). Positivity between the two roots and negativity outside follow. Each root is simple because the relevant sign factor crosses zero linearly, and all remaining factors are strictly positive. This completes the exact infinite-family classification.

## Verification

The accompanying self-contained Python 3 program `verify.py` checks the conditional-probability formula against both polynomial branches using exact fractions for \(2\le n\le50\) and 59 rational radii for every \(n\), as well as the complete sign classification away from transition points and the exact six-vertex boundary roots. It additionally simulates six representative parameter choices with a fixed pseudorandom seed, reproducing the predicted positive and negative covariances. These finite checks are corroboration; the analytic conditional-expectation and quadratic-sign proof establishes the theorem for all allowable sizes and radii.

## Relationship to prior work

Wilsher, Dettmann and Ganesh's 2022 paper studies isolated-vertex distributions and Poisson approximations for one-dimensional soft geometric graphs, with a Poisson point process rather than a fixed number of labeled points. Their 2020 paper treats connectivity, means and variances of isolated counts in the soft model. Hirsch, Moka, Taimre and Kroese study edge-count rare events in Poisson geometric graphs. Those lines of work motivate the interaction of local isolation with global graph density; the inspected treatments do not state the fixed-size hard-circle isolation–edge mixed covariance or its sharp six-point sign transition. Their stated results do not by themselves imply the complete sign theorem.

## Limitations

The proof is restricted to the one-dimensional circle, iid uniform locations, and a hard distance threshold. It does not assert a counterpart on the line segment, under inhomogeneous sampling, for soft connection functions, or in higher dimensions. The covariance magnitude can be small even when positive. Full historical priority relative to general stochastic-geometry moment formulas is not independently established. Reproducible finite computations and self-review do not constitute independent external validation.

## References

- M. Wilsher, C. Dettmann, A. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph* (first posted 2022-02-16), arXiv:2202.08044, https://arxiv.org/abs/2202.08044.
- M. Wilsher, C. Dettmann, A. Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs* (first posted 2020-07-13), arXiv:2007.06301, https://arxiv.org/abs/2007.06301.
- C. Hirsch, S. B. Moka, T. Taimre, D. P. Kroese, *Rare Events in Random Geometric Graphs*, Methodology and Computing in Applied Probability (published online 2021-05-04), https://doi.org/10.1007/s11009-021-09857-7.
