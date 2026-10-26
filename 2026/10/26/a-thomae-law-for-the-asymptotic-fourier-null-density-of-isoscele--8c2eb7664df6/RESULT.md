# A Thomae law for the asymptotic Fourier-null density of isosceles trapezoids

## Finding

For every real parameter \(0<\alpha<1\), define the nondegenerate, area-four isosceles trapezoid
\[
T_\alpha=\{(x,y)\in\mathbb R^2:-1\le y\le1,\ |x|\le1+\alpha y\}.
\]
Use angular-frequency Fourier normalization
\[
F_\alpha(u,v)=\int_{T_\alpha}e^{-i(ux+vy)}\,dx\,dy.
\]
Let \(N_\alpha(R)\) be the **number of distinct real zeros** of \(F_\alpha\) in the closed Euclidean disk \(u^2+v^2\le R^2\). No multiplicities are assigned.

**Theorem (complete real zero set and arithmetic density).** All real zeros are isolated. They form the union of the following explicitly specified subsets, and no others:

1. The reciprocal lattice with three deleted lines,
\[
\Lambda_\alpha=\left\{\left(\frac{\pi(\ell-k)}{2\alpha},\frac{\pi(k+\ell)}2\right):k,\ell\in\mathbb Z,\ k\ell(\ell-k)\ne0\right\}.
\]
2. For every nonzero integer \(j\), the zeros on the line \(u=j\pi/2\). Set \(p_j=\alpha j\pi/2\) and \(s(z)=\sin z/z\), continuously extended by \(s(0)=1\). Their vertical coordinates \(v\) are **exactly** the real solutions of
\[
\begin{cases}
 s(v-p_j)=s(v+p_j),&j\text{ even},\\
 s(v-p_j)=-s(v+p_j),&j\text{ odd}.
\end{cases}
\]

The zero-counting limit exists and is
\[
\boxed{\lim_{R\to\infty}\frac{N_\alpha(R)}{R^2}
 =\frac2\pi\left(1+\alpha-\eta(\alpha)\right),}
\]
where \(\eta(\alpha)=0\) for irrational \(\alpha\), and \(\eta(p/q)=1/q\) for positive coprime integers \(p<q\). More sharply,
\[
N_\alpha(R)=\frac2\pi\left(1+\alpha-\eta(\alpha)\right)R^2+O_\alpha(R)
\quad(R\ge1).
\]
Thus the zero-density coefficient is continuous at every irrational \(\alpha\) and has a downward jump of precisely \(2/(\pi q)\) at each reduced rational \(p/q\) (relative to the continuous baseline). In particular, all shapes \(\alpha=1/q\), \(q\ge2\), have the same density \(2/\pi\), although their side slopes differ. The area stays equal to four throughout this family.

## Assumptions and scope

The parameter is real and strictly between zero and one. All frequencies are real and expressed in radians; switching to a Fourier convention with \(2\pi\) in the exponential rescales the density. Counts are over the closed Euclidean frequency disk and **distinct** zeros; the theorem neither counts complex zeros nor assigns analytic multiplicities. Constants in \(O_\alpha(R)\) can depend on the fixed trapezoid, and the claim is not uniform as \(\alpha\to0\) or \(\alpha\to1\). Neither the rectangular limit \(\alpha=0\) nor the triangular boundary shape \(\alpha=1\) is included.

## Proof

**Step 1: exact transform.** Integrating first in the horizontal direction gives
\[
F_\alpha(u,v)=\frac2u\int_{-1}^1e^{-ivy}\sin(u(1+\alpha y))\,dy
\qquad(u\ne0).
\]
Writing \(A=s(v-\alpha u)\) and \(B=s(v+\alpha u)\), elementary exponential integration gives the exact expression
\[
F_\alpha(u,v)=\frac2u\big[\sin u\,(A+B)-i\cos u\,(A-B)\big]. \tag{1}
\]
At \(u=0\), a separate limit or direct integration gives
\[
F_\alpha(0,v)=4\left[\frac{\sin v}{v}+i\alpha\frac{v\cos v-\sin v}{v^2}\right]
\quad(v\ne0),\qquad F_\alpha(0,0)=4.
\]
If the real part vanishes at nonzero \(v\), then \(v\) is a nonzero integer multiple of \(\pi\), and the imaginary part is nonzero. Hence there are **no zeros at \(u=0\)**.

**Step 2: exhaustive decomposition.** For \(u\ne0\), the real and imaginary parts of (1) both vanish if and only if
\[
\sin u\,(A+B)=0,\qquad \cos u\,(A-B)=0.
\]
If neither \(\sin u\) nor \(\cos u\) is zero, these imply \(A=B=0\). Because the only real zeros of \(s\) are the nonzero integer multiples of \(\pi\), there are nonzero integers \(k,\ell\) such that
\[
v-\alpha u=k\pi,\qquad v+\alpha u=\ell\pi.
\]
Solving these equations and excluding \(u=0\) yields precisely \(\Lambda_\alpha\). If \(\sin u=0\), equivalently \(u=j\pi/2\) with nonzero even \(j\), the remaining condition is \(A=B\); if \(\cos u=0\), equivalently odd \(j\), it is \(A=-B\). These are exactly the displayed vertical families. Conversely, every listed point indeed annihilates (1). This proves the full zero-set classification. For a given vertical line the defining function is analytic and not identically zero, so the zeros on that line are discrete; since the line locations and the lattice are locally finite, all real zeros are isolated.

**Step 3: uniform vertical-line census.** Write \(p=p_j\ne0\). Away from \(v=\pm p\), the two vertical equations are equivalent respectively to
\[
\frac{2[p\sin v\cos p-v\cos v\sin p]}{v^2-p^2}=0,
\quad
\frac{2[v\sin v\cos p-p\cos v\sin p]}{v^2-p^2}=0. \tag{2}
\]
Values \(v=\pm p\) in the numerators are **removable algebraic roots**, not roots of the original equations: there the original left-minus-right or left-plus-right equals \(1\mp s(2p)\), strictly nonzero because \(|s(2p)|<1\). They cost at most two points in any count.

If \(\cos p\ne0\), on each interval between consecutive positive poles of \(\tan v\), the first numerator equation becomes
\[
\frac{\tan v}{v}=\frac{\tan p}{p},
\]
while the second becomes
\[
v\tan v=p\tan p.
\]
The two left-hand functions are strictly increasing for \(v>0\) wherever finite: their respective derivatives have positive numerators proportional to \(v-\sin v\cos v\) and \(v+\sin v\cos v\). Every full positive tangent branch away from the origin therefore contains exactly one solution, independently of \(p\); the two incomplete end branches together contribute a bounded error. If \(\cos p=0\), the respective equations reduce instead to \(v\cos v=0\) and \(\cos v=0\), again one root per period, up to bounded special cases. The equations are even or odd in \(v\), as appropriate; \(v=0\) costs at most one distinct zero. Hence there is an absolute constant \(C\) such that, for every nonzero integer \(j\) and every \(V\ge0\),
\[
\left|\#\{v\in[-V,V]:F_\alpha(j\pi/2,v)=0\}-\frac{2V}{\pi}\right|\le C. \tag{3}
\]
In particular the vertical family has no continuum of zeros.

**Step 4: count each component.** The reciprocal linear lattice underlying \(\Lambda_\alpha\) has covolume \(\pi^2/(2\alpha)\). Deleting the conditions \(k=0\), \(\ell=0\), and \(k=\ell\) removes only \(O_\alpha(R)\) lattice points inside the disk. Elementary planar lattice counting therefore yields
\[
\#(\Lambda_\alpha\cap B_R)=\frac{2\alpha}{\pi}R^2+O_\alpha(R). \tag{4}
\]
For the vertical family insert \(V_j=\sqrt{R^2-(j\pi/2)^2}\) into (3) and sum over the nonzero integers with \(|j\pi/2|\le R\). The resulting semicircle Riemann sum has an \(O(R)\) error because its summand has total variation \(O(R)\). Thus
\[
\#(\text{vertical family}\cap B_R)=\frac2\pi R^2+O(R). \tag{5}
\]

**Step 5: precise overlap.** A point of \(\Lambda_\alpha\) lies on a vertical line precisely when
\[
\frac{\ell-k}{\alpha}=j\in\mathbb Z\setminus\{0\}.
\]
For irrational \(\alpha\) this is impossible. For reduced \(\alpha=p/q\) it occurs exactly on the vertical lines \(j\in q\mathbb Z\setminus\{0\}\). On such a line \(2p_j/\pi=\alpha j\) is an integer \(r\). The lattice vertical coordinates there form one translate of \(\pi\mathbb Z\), namely \(v\in\pi(\mathbb Z+r/2)\), apart from the two excluded points \(v=\pm p_j\). Substituting \(p_j=\pi r/2\) into (2) shows that the vertical equation itself reduces to \(\sin v=0\) when \(r\) is even and to \(\cos v=0\) when \(r\) is odd, with at most one additional zero at \(v=0\) and the same excluded removable points. Consequently the overlap on each such line has \(2V_j/\pi+O(1)\) points. Summing over lines spaced \(q\pi/2\) gives
\[
\#(\Lambda_\alpha\cap\text{vertical family}\cap B_R)
=\frac{2}{\pi q}R^2+O_\alpha(R). \tag{6}
\]
For irrational \(\alpha\) the overlap count is identically zero. Inclusion–exclusion using (4), (5), and (6) proves the stated density formula and its \(O_\alpha(R)\) remainder.

**Step 6: arithmetic continuity.** The continuous part of the coefficient is \(2(1+\alpha)/\pi\). If a sequence of distinct reduced rationals approaches an irrational, their denominators tend to infinity, so the correction \(2/(\pi q)\) vanishes. Near a fixed rational \(p/q\), irrational parameters approach the uncorrected baseline, giving the claimed downward jump. The values at \(\alpha=1/q\) follow immediately. Finally \(\operatorname{area}(T_\alpha)=\int_{-1}^1 2(1+\alpha y)\,dy=4\), independent of the shape parameter.

## Verification

The standalone program `checker.py` reproduces the reported finite numerical checks using `numpy` and `scipy`. It compares (1) against an independently integrated one-dimensional Fourier formula, tests exact reciprocal-lattice zeros, and enumerates distinct zeros in finite frequency disks for two rational and one irrational slope. `checker_output.txt` records its actual output. Finite numerical counts are **not** used to prove the infinitely many-line asymptotic; Steps 3–5 provide the proof.

## Relationship to prior work

The earliest directly inspected seed is Diaz–Le–Robins (arXiv:1602.08593, first submitted February 27, 2016). Its combinatorial Stokes formula evaluates Fourier transforms of general polytopes but does not enumerate real zeros or give a two-dimensional zero-density law for trapezoids. Wuttke (arXiv:1703.00255, first submitted March 1, 2017) provides form-factor formulas and treats removable singularities of polygonal transforms; it does not derive the specific irrational/rational null-density dichotomy. Kolountzakis–Spyridakis (arXiv:2404.03405, first submitted April 4, 2024) rules out whole prescribed analytic curves in complex Fourier zero sets; such non-containment results neither classify the isolated real zeros here nor provide their density. A same-object earlier formula may exist in applied diffraction literature; in particular, indexing is imperfect, and originality remains subject to independent literature evaluation. Previous mathematical findings on Fourier zeros of triangles, hexagons, and annuli concern distinct shapes and do not imply this density formula.

## Limitations

The original contribution asserted here is the exact **global real-zero decomposition and arithmetic quadratic-density law**, not the elementary polygon Fourier-integral identity itself. No assertion is made about the multiplicity or complex-frequency geometry of the zeros, zero distributions of generic nonsymmetric trapezoids, higher-dimensional frusta, or uniformity in the degenerating endpoints. The interpretation of an irrational as a continuity point is for the asymptotic coefficient, not for finite-radius counts. A highly relevant unindexed exact trapezoid zero census, if discovered, could supersede the originality claim.

## References

- R. Diaz, Q.-N. Le, and S. Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, first submitted 2016-02-27. https://arxiv.org/abs/1602.08593
- J. Wuttke, *Form factor (Fourier shape transform) of polygon and polyhedron*, arXiv:1703.00255, first submitted 2017-03-01. https://arxiv.org/abs/1703.00255
- M. N. Kolountzakis and E. Spyridakis, *Curves in the Fourier zeros of polytopal regions and the Pompeiu problem*, arXiv:2404.03405, first submitted 2024-04-04. https://arxiv.org/abs/2404.03405
