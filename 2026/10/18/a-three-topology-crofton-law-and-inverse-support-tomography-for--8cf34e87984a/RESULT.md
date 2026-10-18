# A three-topology Crofton law and inverse support tomography for convex-meridian toroids

## Finding
Let \(L\subset\mathbb R^2\) be a planar convex body with nonempty interior, invariant under reflection in each coordinate axis. Write the meridian coordinates as \((x,z)\), put \(a=\max_{(x,z)\in L}|x|\), and for every \(R>a\) revolve \((R,0)+L\) about the vertical axis to obtain the solid toroid
\[
T_R(L)=\{((R+x)\cos u,(R+x)\sin u,z):(x,z)\in L,\ 0\le u<2\pi\}.
\]
Select an unoriented affine plane with motion-invariant measure (uniform normal direction, Lebesgue offset), condition on meeting \(T_R(L)\) in positive area, and classify its planar section. Almost surely the only topologies are an annulus, one closed disk, and two disjoint closed disks, each of positive probability.

Define the meridian support value \(H(\theta)=h_L(\sin\theta,\cos\theta)\) and
\[
C=\int_0^{\pi/2}H(\theta)\sin\theta\,d\theta,\quad
Z_R=C+\frac{\pi R}{4},\quad
A_R=\int_0^{\pi/2}\big(H(\theta)-R\sin\theta\big)_+\sin\theta\,d\theta.
\]
Here \(h_L(p,q)=\max_{(x,z)\in L}(px+qz)\) and \(v_+=\max(v,0)\). The full law is
\[
\Pr(\mathrm{annulus})=\frac{A_R}{Z_R},\qquad
\Pr(\mathrm{one\ disk})=\frac{2(C-A_R)}{Z_R},\qquad
\Pr(\mathrm{two\ disks})=\frac{A_R+\pi R/4-C}{Z_R}.
\]
In particular, its Euler-characteristic expectation and its universal topology difference are
\[
\mathbb E\chi=\frac{\pi R/2}{C+\pi R/4},\qquad
\Pr(\mathrm{annulus})-\Pr(\mathrm{two\ disks})=\frac{C-\pi R/4}{C+\pi R/4}.
\]
These formulas hold without strict convexity or boundary smoothness.

Moreover, if \(L\) has a \(C^2\) boundary with everywhere positive curvature, its entire shape is uniquely determined by the three section-topology probabilities as functions of \(R>a\). More explicitly, the probability difference gives \(C\). Set \(A(R)=Z_R\Pr(\mathrm{annulus})\) and \(F(\theta)=\theta/2-\sin(2\theta)/4\). For each \(R>a\) the unique angle \(\theta_R\in(0,\pi/2)\) satisfying \(H(\theta_R)=R\sin\theta_R\) obeys
\[
F(\theta_R)=-A'(R).
\]
Thus the observed profile determines the inverse graph \(R=H(\theta)/\sin\theta\), and therefore \(h_L\) in all directions and the body \(L\).

For the standard ring torus, \(L\) is a disk of radius \(r<R\). Then \(C=r\), and
\[
A_R=r-\frac r2\sqrt{1-(r/R)^2}-\frac R2\arcsin(r/R),
\]
so the three probabilities are elementary and strictly positive.

## Assumptions and scope
The solids are closed meridian-revolution toroids in \(\mathbb R^3\); \(L\) is compact, convex, two-dimensional, and symmetric under each coordinate reflection. The centerline radius \(R\) exceeds the maximal horizontal semiextent \(a\), so rotation does not meet the symmetry axis. Probabilities refer to the motion-invariant measure on unoriented affine planes, conditioned on positive-area intersection. Boundary-tangent planes, transition inclinations, and other singular sections form a measure-zero subset. The inverse assertion additionally assumes \(C^2\) positive-curvature boundary for the meridian and the full profile over every \(R>a\); no fixed-radius identifiability is claimed.

## Proof
**1. Fiber geometry.** By axial symmetry, a plane normal may be written \(n=(\sin\theta,0,\cos\theta)\), with \(0\le\theta\le\pi/2\); the plane has equation \(n\cdot p=t\). The ordinary Haar distribution of the unoriented normal has density \(\sin\theta\,d\theta\). Let \(s=\sin\theta\), \(c=\cos\theta\), and \(v=\cos u\). At a fixed azimuth \(u\), intersection with the meridian copy is the convex line segment, possibly empty, defined by
\[
(R+x)sv+zc=t,\qquad (x,z)\in L.
\]
Central symmetry of \(L\) implies that it is nonempty exactly if
\[
f_-(v)\le t\le f_+(v),\qquad
f_\pm(v)=Rsv\pm h_L(sv,c).
\]
For \(-1\le v_1<v_2\le1\), the Lipschitz bound \(|h_L(sv_2,c)-h_L(sv_1,c)|\le as(v_2-v_1)\) implies
\[
f_\pm(v_2)-f_\pm(v_1)\ge (R-a)s(v_2-v_1)>0
\]
when \(\theta>0\). Hence the feasible cosine values form one interval. Its inverse image under \(u\mapsto\cos u\) is the full circle, one arc, or two disjoint arcs. Each meridian fiber is convex and the fibers collapse only at arc endpoints, so the planar section is respectively an annulus, one disk, or two disks. The two axial reflection symmetries give the four endpoint levels
\[
f_-( -1)=-Rs-H,\quad f_+(-1)=-Rs+H,\quad
f_-(1)=Rs-H,\quad f_+(1)=Rs+H,
\]
where \(H=H(\theta)\). The full circle occurs exactly for \(|t|<H-Rs\) when \(H>Rs\); two arcs occur exactly for \(|t|<Rs-H\) when \(Rs>H\); all other nonempty generic sections consist of one disk.

**2. Invariant-plane integration.** For each fixed \(\theta\), the allowed offsets form the interval \(|t|<Rs+H\). The annulus offsets have total length \(2(H-Rs)_+\), and the two-disk offsets total length \(2(Rs-H)_+\). Integrate these lengths against \(\sin\theta\,d\theta\), and divide by \(2Z_R\). The identity
\[
\int_0^{\pi/2}(Rs-H)\sin\theta\,d\theta=\frac{\pi R}{4}-C
\]
produces the stated formulas for all three probabilities. Since \(H(0)>0\) and \(H(\pi/2)=a<R\), both the annulus and two-disk events have positive measure; the remaining one-disk event also has positive measure. Euler characteristics of annulus, disk, and two disks are \(0,1,2\), giving the expectation.

**3. Inverting the topology profile.** Let \(\Delta_R=\Pr(\mathrm{annulus})-\Pr(\mathrm{two\ disks})\). The difference identity gives
\[
C=\frac{\pi R}{4}\frac{1+\Delta_R}{1-\Delta_R}.
\]
Consequently all \(A_R\) are known. Put \(g(\theta)=H(\theta)/\sin\theta\). Since \(L\) is symmetric in both axes,
\[
g(\theta)=\max_{(x,z)\in L}\bigl(x+z\cot\theta\bigr)
\]
with the maximum achievable in the first quadrant. Positive curvature and reflection symmetry imply that, for every \(0<\theta<\pi/2\), the support point has positive \(z\) and \(g(\theta)>a\). Thus \(g\) is continuous, strictly decreasing, with \(g(0+)=+\infty\) and \(g(\pi/2)=a\). For any \(R>a\), exactly the angles \(\theta<\theta_R\) satisfy \(g(\theta)>R\). Differentiating the positive-part integral (the moving-endpoint term is zero) gives
\[
A'(R)=-\int_0^{\theta_R}\sin^2\theta\,d\theta=-F(\theta_R).
\]
As \(F\) is strictly increasing, \(\theta_R\) is determined by the data. Varying \(R\) recovers \(g\), hence \(H\). The two reflection symmetries extend these support values to all directions, and a convex body is uniquely determined by its support function.

**4. Circular meridian.** If \(H=r\), the threshold is \(\theta_R=\arcsin(r/R)\). Elementary integration yields the claimed closed form for \(A_R\).

## Verification
Run \(\texttt{python3 check_toroid.py}\) with Python 3, NumPy, and SciPy. The standalone checker independently discretizes feasible azimuth sets and counts components for meridian ellipses, rectangles, and diamonds, compares the analytical law with Haar-weighted plane sampling, and numerically recovers support directions by differentiating \(A_R\). The run recorded 797 non-transition topology comparisons, 450,000 random-plane draws across six geometries, and 15 inverse-profile tests. Its largest observed sampling discrepancy was below \(0.0021\); its largest angle-recovery error was below \(1.6\times10^{-7}\). Sampling and mesh checks are corroboration, not proofs of the infinite claims.

## Relationship to prior work
The algebraic study of sections of circular tori dates at least to Darboux. Sym (2009) reviews toric quartics and the Villarceau and spiric cases; Kim and Kim (2000) develop algorithms for special conic intersection curves. Moroni (2017) discusses generic oblique sections of circular torus surfaces. These sources concern particular intersection curves and their equations, while the present theorem gives the invariant-plane topology law for arbitrary convex symmetric meridians and a reconstruction theorem for the complete family as the revolution radius varies. Bannikova, Vakulik and Sergeev (2012) provide independently dated motivation for oval toroidal cross sections, without deriving this integral-geometric law.

## Limitations
The inverse theorem requires a continuous family of toroids with a fixed smooth positively curved meridian and varying centerline radius; a single topology distribution supplies only finitely many scalars. The forward law assumes coordinate-reflection symmetry of the meridian and does not characterize nonsymmetric toroidal shapes. The proof concerns planar-section topology, not sectional area or perimeter distributions. Numerical tests cannot rule out all implementation errors. Historical priority, especially older engineering stereology and surface-intersection literature, is not exhaustively settled. No independent mathematical audit has been conducted.

## References
1. Antoni Sym, *Darboux's greatest love*, J. Phys. A: Math. Theor. 42 (2009), 404001. DOI: 10.1088/1751-8113/42/40/404001.
2. Ku-Jin Kim and Myung-Soo Kim, *Computing All Conic Sections in Torus and Natural Quadric Intersections*, conference manuscript (2000), author-uploaded public full-text entry: https://www.researchgate.net/publication/2418506_Computing_All_Conic_Sections_in_Torus_and_Natural_Quadric_Intersections.
3. Luca Moroni, *The toric sections: a simple introduction*, arXiv:1708.00803 (2017), https://arxiv.org/abs/1708.00803; accessible full expository article at https://www.lucamoroni.it/toric-sections/.
4. E. Yu. Bannikova, V. G. Vakulik and A. V. Sergeev, *N-body simulation of a clumpy torus: application to active galactic nuclei*, arXiv:1204.6580, first posted 2012-04-30, https://arxiv.org/abs/1204.6580.
