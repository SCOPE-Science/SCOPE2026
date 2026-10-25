# A sharp 21-point onset of four dependence phases for isolated vertices on a random circle

## Finding
Place \(n\ge2\) independent uniform labeled points on a unit-circumference circle. Connect two points if their shorter arc distance is at most \(r\), where \(0<r<1/4\). Write \(I_i\) for the indicator that point \(i\) is isolated, and \(C_n(r)=\operatorname{Cov}(I_1,I_2)\). Then
\[
C_n(r)=\frac{2}{n-1}(1-3r)^{n-1}+\frac{n-3}{n-1}(1-4r)^{n-1}-(1-2r)^{2n-2}.
\]
The number of zeros of \(C_n\) in \((0,1/4)\) is exactly zero for \(n=2,3\), one for every \(4\le n\le20\), and three for every \(n\ge21\). All are simple crossings. The signs across successive radius intervals are respectively positive; positive-negative; and positive-negative-positive-negative. In particular, the four-phase pattern starts sharply with \(21\) points.

At fixed \(c>0\),
\[
nC_n(c/n)\to2e^{-4c}(e^c-1-2c^2).
\]
If \(r_{1,n}<r_{2,n}<r_{3,n}\) are the three roots for \(n\ge21\), then \(nr_{1,n}\to c_1\approx0.74085043\) and \(nr_{2,n}\to c_2\approx2.84267341\), the two positive roots of \(e^c-1-2c^2\).

## Assumptions and scope
All points are independent, uniform and labeled; distance is the shorter circular arc, and hard connections use a deterministic common radius. The conclusions are **for the binomial fixed-size point model**, not a Poisson point process, and concern covariance of two specified isolation indicators, not covariance between component totals. The open interval \((0,1/4)\) avoids changes in the two-neighborhood union geometry. Endpoints are excluded. Zero multiplicities and all sign claims concern this entire open interval.

## Proof
Write \(m=n-1\). By rotation invariance, \(\mathbb EI_1=(1-2r)^m\). Given the distance \(u\in[0,1/2]\) between the first two vertices, its density is \(2\). They can both be isolated only if \(u>r\). For \(r<u<2r\) their forbidden arcs have union length \(2r+u\), and for \(u\ge2r\) that union has length \(4r\). Independence of the remaining \(n-2\) points gives
\[
\mathbb E(I_1I_2)=2\int_r^{2r}(1-2r-u)^{n-2}\,du+(1-4r)^{n-1}=
\frac2m(1-3r)^m+\frac{m-2}{m}(1-4r)^m.
\]
Subtracting \((\mathbb EI_1)^2\) proves the displayed covariance formula. For \(n=2\), \(C_2(r)=2r(1-2r)>0\). For \(n=3\), set \(X=(1-3r)/(1-2r)^2\): then \(C_3/(1-2r)^4=X^2-1>0\), since \(X-1=r(1-4r)/(1-2r)^2>0\).

For \(n\ge4\), normalize by the positive factor \((1-2r)^{2m}\) and put
\[
F(r)=\frac2m X(r)^m+\frac{m-2}{m}Y(r)^m-1,\quad
X(r)=\frac{1-3r}{(1-2r)^2},\quad Y(r)=\frac{1-4r}{(1-2r)^2}.
\]
Here \(X'=(1-6r)/(1-2r)^3\) and \(Y'=-8r/(1-2r)^3\), hence \(F'<0\) on \([1/6,1/4)\). On \((0,1/6)\), the sign of \(F'\) is the sign of
\[
H(r)-(m-2),\qquad H(r)=\frac{1-6r}{4r}\left(\frac{1-3r}{1-4r}\right)^{m-1}.
\]
The derivative of \(\log H\) has the sign of the quadratic
\[
q(r)=-1+(m+6)r-6(m+1)r^2,
\]
because its denominator \(r(1-6r)(1-3r)(1-4r)\) is positive. Thus \(H\) has at most two critical points and meets any horizontal level at most three times. Therefore \(F'\) has at most three zeros, and Rolle's theorem applied together with \(F(0)=0\) bounds the number of distinct roots in \((0,1/4)\) by three (including multiplicity, by the repeated-root version of Rolle).

For \(m\ge20\), the signs at four ordered locations are alternating. First \(C_n'(0)=2>0\). At \(r=1/n\), let \(z=4m/(m-1)^2\). Then \(X(1/n)=1+(m-3)/(m-1)^2\) and \(Y(1/n)=1-4/(m-1)^2\), so
\[
F(1/n)<\frac{2e}{m}+\left(1-\frac2m\right)\left(1-z+\frac{z^2}2\right)-1<0.
\]
Indeed, \((m-2)(z-z^2/2)\) increases for \(m\ge20\), is \(462240/130321>7/2\) at \(m=20\), and \(2(e-1)<7/2\). At \(r=1/6\), \(X=9/8\), \(Y=3/4\), and
\[
F(1/6)=\frac2m(9/8)^m+\left(1-\frac2m\right)(3/4)^m-1>0:
\]
\((2/m)(9/8)^m>1\) at \(m=20\), and this term increases with integer \(m\ge20\). Finally
\[
C_n(1/4)=\left(\frac2m-1\right)4^{-m}<0.
\]
By continuity there are at least three strict sign crossings, and the previous global root bound makes these exactly three simple zeros.

For \(4\le n\le20\), the remaining finite interval is settled without floating-point assumptions. Expand the integer polynomial
\[
P_n(r)=2(1-3r)^m+(m-2)(1-4r)^m-m(1-2r)^{2m}=mC_n(r).
\]
It is divisible by \(r\). Exact rational Sturm-sequence root counts for \(P_n(r)/r\) on \((0,1/4)\) are one for every integer \(4\le n\le20\), as independently reproducible with the complete `VERIFY.py` artifact. As \(C_n'(0)=2\) and \(C_n(1/4)<0\), the unique zero is simple and changes sign. The same exact checker tests \(n=2,3,21\) and verifies the differentiation identities.

Lastly, Taylor expansion at \(r=c/n\), uniformly for \(c\) in any compact subset of \((0,\infty)\), gives
\[
nC_n(c/n)\to2e^{-4c}(e^c-1-2c^2).
\]
The function \(e^c-1-2c^2\) has exactly two positive simple roots: its third derivative is positive, and its signs at small positive \(c\), at \(c=1\), and at \(c=4\) alternate; three positive roots would force at least four zeros counting the zero at the origin and hence a contradiction by repeated Rolle. Uniform convergence near each root, together with the global three-root bound and small-radius positivity, proves the first two rescaled-root limits.

## Verification
The standalone `VERIFY.py` uses exact symbolic algebra and Sturm sequences to determine all root counts for \(2\le n\le21\), checks the signs at the three decisive radii, and checks the derivative identities. It completed with `PASS exact finite root counts and derivative identities`. The all-\(n\) argument comes from the analytic root bound and sign witnesses, not from this finite calculation.

## Relationship to prior work
Penrose's *Random Geometric Graphs* (2003) provides broad theory for random geometric graphs, including finite-point models and component counts; its relevant chapter contents were not available for full-text comparison. Decreusefond–Ferraz (2010), read in full, derive component-count laws for a Poisson one-dimensional geometric graph and discuss the circle, not this fixed-size labeled-pair covariance phase classification. Wilsher–Dettmann–Ganesh (2020), full-text Section 4, derive mean and variance formulas for isolated nodes in a one-dimensional **Poisson soft-connection** graph using Palm measures; their general moment integration informs, but does not itself state, this fixed-\(n\) sharp 21-point root classification. Stronger historical coverage remains a possibility, especially in monograph treatments.

## Limitations
The theorem only concerns the unit circle, uniform iid locations, a hard radius and \(0<r<1/4\). It does not determine signs beyond that radius or for nonuniform sampling, higher-dimensional tori, or soft connection functions. The second-moment identity is elementary; the substantive sharp contribution is the uniform all-size sign-phase classification and its first onset. Historical originality is assessed against the material actually accessible, not certified independently.

## References
1. M. Penrose, *Random Geometric Graphs*, Oxford University Press, 2003, doi:10.1093/acprof:oso/9780198506263.001.0001.
2. L. Decreusefond and E. Ferraz, *On the One dimensional Poisson Random Geometric Graph*, arXiv:1008.5140v1, publicly posted 2010-08-30, https://arxiv.org/html/1008.5140v1.
3. M. Wilsher, C. P. Dettmann, A. Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs*, arXiv:2007.06301v1, publicly posted 2020-07-13, https://arxiv.org/html/2007.06301v2.
