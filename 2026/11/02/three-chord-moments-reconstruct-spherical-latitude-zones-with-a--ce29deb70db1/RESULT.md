# Three chord moments reconstruct spherical latitude zones, with a sharp two-moment ambiguity

## Finding
Let \(Z(a,b)=\{x\in S^2:a\le x\cdot e\le b\}\) be a proper two-boundary spherical zone on the unit sphere, where \(-1<a<b<1\) and \(e\) is an arbitrary unit axis. Choose independent surface-area-uniform \(X,Y\in Z(a,b)\), let \(\Theta=\arccos(X\cdot Y)\in[0,\pi]\) be the **ambient great-circle distance** (not a shortest path constrained to the zone), and let \(L=2\sin(\Theta/2)=\|X-Y\|_2\) be its Euclidean chord length. Then the first three even chord moments
\[
\mathbb E[L^2],\quad \mathbb E[L^4],\quad \mathbb E[L^6]
\]
uniquely determine \(Z(a,b)\) up to a rotation or reflection of the sphere. This is a sharp cutoff in the sequence of initial even chord moments: the first two can agree for noncongruent zones.

More exactly, put \(m=|a+b|/2\), \(h=(b-a)/2\), \(q=m^2+h^2/3\), and \(S=\cos\Theta=1-L^2/2\). Define \(\mu_j=\mathbb E[S^j]\). The moment identities are
\[
\begin{aligned}
\mu_1&=m^2,\\
\mu_2&=\tfrac12-q+\tfrac32q^2,\\
\mu_3&=\tfrac{m^2}{2}\left(20m^4-60m^2q+12m^2+45q^2-18q+3\right).
\end{aligned}
\]
Recover \(m=\sqrt{\mu_1}\), solve the quadratic for \(q\) subject to \(m^2<q<m^2+(1-m)^2/3\), and, if both roots are admissible, select the unique root compatible with \(\mu_3\). Finally \(h=\sqrt{3(q-m^2)}\), and the unordered latitudinal cutoffs (allowing axis reversal) are \(\{m-h,m+h\}\).

There exist two different admissible roots for the first two moments for some zones with a prescribed \(m\) **if and only if**
\[
\tfrac12<m<\tfrac1{\sqrt3}.
\]
For a particular zone, the first two moments are ambiguous precisely when \(q\ne1/3\) and both \(q\) and \(2/3-q\) lie strictly between \(m^2\) and \(m^2+(1-m)^2/3\). For example, the two zones with \(m=11/20\) and halfwidths \(h=\sqrt{17}/20\) and \(h=\sqrt{57}/20\) have equal first two even chord moments, but different sixth moments.

## Assumptions and scope
The sphere has unit radius; the sampling measure is surface area normalized by the **zone's own area**, not uniform latitude angle or uniform ambient volume. The bounds \(-1<a<b<1\) exclude one-boundary caps and degenerate circles; the result allows zones crossing the equator and zones contained in a hemisphere. The axis \(e\) and its sign are unobserved. Two such zones are congruent if and only if their parameters \(m,h\) agree. The intrinsic metric on the zone with its boundary treated as an obstacle is not considered.

## Proof
**1. Spherical area coordinates.** After rotating \(e\) to the north pole, write
\[
X=(\sqrt{1-Z^2}\cos\Phi,\sqrt{1-Z^2}\sin\Phi,Z),
\]
where \(Z\) is uniform on \([a,b]\), \(\Phi\) is uniform on \([0,2\pi)\), and they are independent. This follows directly from \(dA=d\Phi\,dZ\). Axis reversal lets us assume the interval center equals \(m\ge0\). Its halfwidth \(h\) satisfies \(0<h<1-m\). Integration gives
\[
\mathbb E Z=m,\quad \mathbb E Z^2=q=m^2+h^2/3,\quad \mathbb E Z^3=u=m^3+mh^2=m(3q-2m^2).
\]

**2. Exact pair moments.** For independent copies \(X,Y\), write \(S=X\cdot Y\). By independence, \(\mathbb ES=\|\mathbb EX\|^2=m^2\). The second-moment matrix is diagonal with entries \(((1-q)/2,(1-q)/2,q)\), so
\[
\mathbb ES^2=\tfrac12(1-q)^2+q^2=\tfrac12-q+\tfrac32q^2.
\]
For the symmetric third-moment tensor \(T_{ijk}=\mathbb E[X_iX_jX_k]\), rotational symmetry leaves only \(T_{333}=u\) and the six permutations of \(T_{113}=T_{223}=(m-u)/2\). All other components vanish. Hence
\[
\mathbb ES^3=\sum_{i,j,k=1}^3T_{ijk}^2=u^2+\tfrac32(m-u)^2.
\]
Substitution of \(u=m(3q-2m^2)\) yields the displayed polynomial for \(\mu_3\). The transformations between \((\mu_1,\mu_2,\mu_3)\) and \((\mathbb EL^2,\mathbb EL^4,\mathbb EL^6)\) are invertible triangular transformations, because \(L^2=2(1-S)\).

**3. Exact inversion and the sharp fold.** The first identity fixes \(m\). The second is invariant under \(q\mapsto q'=2/3-q\), and these are all its possible preimages. The allowed interval is
\[
I_m=\left(m^2,\ m^2+\tfrac13(1-m)^2\right).
\]
Two distinct admissible preimages require \(I_m\) to straddle \(1/3\). This occurs precisely when \(m^2<1/3\) and \(m^2+(1-m)^2/3>1/3\), equivalently \(1/2<m<1/\sqrt3\). Conversely, for every \(m\) in that open interval a small symmetric pair \(q=1/3\pm\eta\) lies in \(I_m\), proving sharpness.

Direct polynomial subtraction gives
\[
\mu_3(m,q)-\mu_3(m,2/3-q)=-4m^2(5m^2-1)(3q-1).
\]
If two distinct roots are admissible, \(m>1/2\), so \(5m^2-1>1/4\), and \(q\ne1/3\). Thus the third moment distinguishes the roots. Outside the ambiguous region \(\mu_2\) already selects the only feasible root. This proves global injectivity, including every coincident-root case.

**4. Exact nonidentifiability witness.** With \(m=11/20\), take \(h_1=\sqrt{17}/20\), \(h_2=\sqrt{57}/20\); both satisfy \(0<h_i<1-m\). Their distinct \(q\) values are \(19/60\) and \(7/20\), which sum to \(2/3\). Direct substitution gives
\[
\begin{aligned}
\mathbb E L^2&=279/200,\\
\mathbb E L^4&=583/200
\end{aligned}
\]
for both, but their sixth moments, respectively, are \(5523679/800000\) and \(5722119/800000\), differing by \(4961/20000\). Their areas \(4\pi h_i\) differ, so no spherical isometry identifies them.

## Verification
The self-contained \(check.py\) uses exact symbolic algebra to verify all moment identities, the quadratic-fold relation, the sixth-moment separation, the strict feasibility of the rational-algebraic witness, and the fold thresholds. As an independent computation it integrates the original dot product \(S=Z_1Z_2+\sqrt{1-Z_1^2}\sqrt{1-Z_2^2}\cos(\Phi_1-\Phi_2)\) by Gauss–Legendre latitude quadrature and periodic azimuth quadrature, for five geometries including both ambiguous witnesses. It also scans feasible intervals as a diagnostic; these finite tests support, but do not replace, the global algebraic proof. Execute `python check.py` with `numpy` and `sympy` installed.

## Relationship to prior work
Moseeva–Tarasov–Zaporozhets (2020) derive a spherical distance/chord-distribution relation for spherical convex bodies and the distance density of spherical caps. Proper two-boundary zones are generally not geodesically convex, and their first-three-moment inverse classification and exact two-moment ambiguity are not stated there. Mémoli–Needham (2018) give a general inverse-problem framework for metric-measure distance distributions, including manifold and graph rigidity; their stated manifold results do not reconstruct the two latitude cutoffs of spherical zones from three scalar chord moments. Balch–Peterson–Shonkwiler (2020) calculate complete distance moments for homogeneous lens spaces, which are closed quotient manifolds rather than spherical zones with boundary. Basic tensor-contraction moment identities are algebraic tools, not independently claimed discoveries. No covering claim was found in the inspected material; older equivalent formulations under stereological or spherical-moment terminology remain possible.

## Limitations
The result uses exact population moments, known unit sphere radius and surface-uniform sampling. It does not give sample-size, noise, or uniform inverse-conditioning bounds near the quadratic fold, and it does not identify arbitrary spherical regions. It concerns ambient great-circle distance/chord distance, not shortest paths constrained to a nonconvex zone. Literature priority is provisional, and an independent mathematical audit has not been performed.

## References
1. T. Moseeva, A. Tarasov, D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297, first submitted 2020-07-14, https://arxiv.org/abs/2007.07297.
2. F. Mémoli, T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, first submitted 2018-10-23, https://arxiv.org/html/1810.09646v5.
3. B. Balch, C. Peterson, C. Shonkwiler, *Distributions of Distances and Volumes of Balls in Homogeneous Lens Spaces*, arXiv:2004.13196, first submitted 2020-04-27, https://arxiv.org/html/2004.13196v1.
