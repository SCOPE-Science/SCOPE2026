# Two Crofton line-angle harmonics determine every parallelogram

## Finding
Let \(P\) be an arbitrary nondegenerate Euclidean parallelogram. Independently sample two **unoriented affine lines** from motion-invariant line measure \(d\theta\,dt\), with each line separately conditioned to intersect \(P\). Write \(\Delta\) for the difference of their unoriented line directions modulo \(\pi\), and define the two observable angular harmonics
\[
T_1=\mathbb E\cos(2\Delta),\qquad T_2=\mathbb E\cos(4\Delta).
\]
**These two real numbers determine \(P\) up to similarity (including reflection).** No individual direction labels, line offsets, chord lengths, or size measurements are required. The first harmonic alone cannot identify an arbitrary parallelogram.

More precisely, put \(A=9T_1\) and \(B=225T_2\). **The exact image of all nondegenerate parallelograms** is
\[
\boxed{0\le A<1,\qquad (2A-1)^2\le B\le1.}
\]
The upper boundary \(B=1\) consists exactly of rectangles; the lower boundary \(B=(2A-1)^2\) consists exactly of rhombi. Their intersection \((A,B)=(0,1)\) is the square. Thus the two-harmonic data both identify and characterize every feasible shape.

An explicit inverse uses
\[
q=1-A,\quad c^2=\frac{1-B}{4q},\quad
\eta=\frac{q}{1-c^2},\quad
\phi=\arccos c,\quad
\frac{a}{b}=\frac{1+\sqrt{1-\eta}}{1-\sqrt{1-\eta}}.
\]
Here \(a\ge b>0\) are the side lengths, \(\phi\in(0,\pi/2]\) is the acute angle between the *unoriented side lines*, and \(c\ge0\). The endpoint square and rectangle cases are included without limiting conventions.

In fact the entire pair-angle distribution is known by an absolutely convergent Fourier series. Writing \(p=a/(a+b)\), for \(k\ge1\),
\[
\boxed{T_k:=\mathbb E\cos(2k\Delta)=
\frac{1-4p(1-p)\sin^2(k\phi)}{(4k^2-1)^2}.}
\]
For the relative angle \(\Delta\in[0,\pi)\), its density is
\[
f_\Delta(\delta)=\frac1\pi\left(1+2\sum_{k=1}^{\infty}T_k\cos(2k\delta)\right).
\]

## Assumptions and scope
A nondegenerate parallelogram is the Minkowski sum of two nonparallel segments of lengths \(a,b>0\). Choosing signs and exchanging generators gives an acute edge-line angle \(0<\phi\le\pi/2\) and \(a\ge b\). Congruence up to a common dilation is exactly the pair of parameters \((a/b,\phi)\). The uniform invariant line measure is defined precisely by the parametrization
\[
L_{\theta,t}=\{x\in\mathbb R^2:x\cdot(-\sin\theta,\cos\theta)=t\},
\quad 0\le\theta<\pi,\quad t\in\mathbb R,
\]
with measure \(d\theta\,dt\); its total mass over lines hitting a fixed compact convex body is finite. Conditioning each line independently on intersecting the body yields a genuine probability law. **The two lines are not required to meet each other inside the body** (a different sampling experiment).

The angles are relative and unoriented: changing the representation by an integer multiple of \(\pi\), or replacing a relative angle with its supplement, leaves every displayed cosine unchanged. Side length scale, absolute position and global rotation cannot be observed.

## Proof
**1. Directional marginal under invariant line sampling.** Write the edges as \(v=(a,0)\) and \(w=b(\cos\phi,\sin\phi)\), after rigid motion. A line of direction \(\theta\) crosses the body for an interval of transverse offsets of length equal to its directional width
\[
W(\theta)=a|\sin\theta|+b|\sin(\theta-\phi)|.
\]
Because \(\int_0^\pi|\sin\theta|\,d\theta=2\), the total hitting-line measure is \(2(a+b)\). Its conditional direction density is therefore
\[
p_\Theta(\theta)=\frac{W(\theta)}{2(a+b)},\quad 0\le\theta<\pi.
\]
No assertion that hit-conditioned directions are uniform is used.

**2. Exact Fourier spectrum.** Elementary integration gives for every integer \(k\ge1\),
\[
\int_0^\pi|\sin\theta|e^{2ik\theta}\,d\theta=-\frac{2}{4k^2-1}.
\]
Thus, letting \(m_k=\mathbb E[e^{2ik\Theta}]\),
\[
m_k=-\frac{a+b e^{2ik\phi}}{(a+b)(4k^2-1)}.
\]
If \(\Theta_1,\Theta_2\) are independent copies, then
\[
\mathbb E e^{2ik(\Theta_1-\Theta_2)}=m_k\overline{m_k}=|m_k|^2.
\]
Its imaginary part is zero; expanding the squared modulus proves the stated formula for \(T_k\). Fourier inversion gives the displayed density. The Fourier series is absolutely and uniformly convergent because \(0\le T_k\le(4k^2-1)^{-2}\), so there is no hidden singular component.

**3. Two-harmonic inverse and feasible region.** Put \(p=a/(a+b)\) and \(s=\sin^2\phi\). Write \(\sigma=4p(1-p)\in(0,1]\), \(s\in(0,1]\), and \(q=\sigma s\in(0,1]\). The first two formulas simplify to
\[
A=1-q,\qquad B=1-4q(1-s).
\]
Since \(q\le s\),
\[
B-(2A-1)^2=4q(s-q)\ge0,\qquad B\le1,\qquad 0\le A<1.
\]
Conversely, take any pair in the displayed closed-parabolic strip with \(A<1\). Set \(q=1-A>0\), \(c^2=(1-B)/(4q)\), \(s=1-c^2\). The two inequalities imply \(0\le c^2<1\) and \(q\le s\). Hence \(\eta=q/s\in(0,1]\). Choose
\[
p=\frac{1+\sqrt{1-\eta}}2\in[1/2,1),
\quad \phi=\arccos\sqrt{c^2}\in(0,\pi/2].
\]
Then \(4p(1-p)=\eta\), and the formulas recover precisely the prescribed \((A,B)\). The map is injective in the normalized shape variables because these inverse expressions are unique. The equal-weight condition \(\eta=1\) holds exactly when \(a=b\), and is equivalent to the lower parabolic equality; the condition \(c^2=0\) holds exactly when edges are perpendicular, and is equivalent to the upper equality. Their intersection forces \(a=b\), \(\phi=\pi/2\).

**4. Sharp necessity of two harmonics.** Consider a rectangle with \((a,b,\phi)=(2,1,\pi/2)\), and a nonrectangular rhombus with \((a,b,\phi)=(1,1,\arcsin(2\sqrt2/3))\). For both, \(\sigma s=8/9\), hence
\[
T_1=\frac1{81}.
\]
But their second moments are respectively \(T_2=1/225\) and \(T_2=49/18225\), so they are geometrically distinct and separated by the second harmonic. This shows the first harmonic is insufficient over all parallelograms, whereas two suffice.

## Verification
The attached reproducibility script `verify.py` uses only the Python standard library. Run `python3 verify.py`. It independently approximates the complex width Fourier coefficients by midpoint quadrature (20 cases), tests exact-data inversion on 1,500 fixed-seed nondegenerate shapes, verifies the sharp one-harmonic counterexample, and compares both harmonic expectations with two independent simulation schemes: sampling width-weighted directions (three shapes, 110,000 pairs each), and rejecting isotropic lines by actual vertex-projection bounds (three shapes, 35,000 pairs each). Its success marker is `CROFTON_PAIR_ANGLE_OK`.

These finite tests support the computations but cannot replace the exact normalization, Fourier identity, algebraic inverse, and boundary proof given above. No finite-sample statistical convergence rate or noise-stability theorem is claimed.

## Relationship to prior work
Bianchi, Gardner and Kiderlen [1] develop phase retrieval and reconstruction from the **area covariogram** of a convex body. Their inverse data are translation-dependent area overlaps or Fourier magnitudes of the body indicator. Our data are just two *angular correlations of independently hitting lines*, not the area covariogram, and their uniqueness statement does not imply sufficiency of these two numbers.

Kim, Yaskin and Zvavitch [2] investigate the direction-*unlabeled distribution of projection lengths* and exhibit nonuniqueness for general bodies. That is neither the distribution of the directions of invariant lines conditioned to meet a body, nor the autocorrelation of those directions. The earlier width-based results do not supply this pair-harmonic reconstruction, its exact feasible range, or the minimality counterexample.

A related publicly available mathematical result, *Three unlabeled width statistics reconstruct a parallelogram with sharp stability* (2026), reconstructs from mean width, squared mean width and diameter. It does not use the angle between two independent hitting lines and does not identify the parabolic two-angular-moment region. A second record, *Inverse classification of projection-width distributions for tangential symmetric polygons* (2026), uses a full one-point width distribution, which is also different. A third result about fourth chord-distance moments in parallelograms uses randomly selected endpoints rather than invariant random lines. These are direct comparisons of measurement assumptions and implications, not blanket novelty claims.

Barahona Torres, Manrique-Mirón and Treviño-Aguilar [3] investigate an angular law involving endpoint-selected and horizontal chords in a disk, additionally conditioned on an intersection point lying inside that disk; that sampling convention differs from the present pair of independent invariant hitting lines. These distinctions matter even when the underlying set is a disk.

## Limitations
The inverse theorem is restricted to **nondegenerate parallelograms** and exact population angular moments under the stated motion-invariant line convention. It determines shape only up to similarity and reflection, not size or location. It does not imply recovery of arbitrary convex bodies or polygons from two harmonics. Near degenerate parallelograms, the inverse formulas become ill-conditioned, and no statistical error bound is proved. The algebraic mechanism is closely related to two-atom Fourier magnitude inversion; unindexed classical formulations may contain an equivalent result. Definitive historical priority and independent validation are not asserted.

## References
[1] G. Bianchi, R. J. Gardner and M. Kiderlen, *Phase retrieval for characteristic functions of convex bodies and reconstruction from covariograms*, arXiv:1003.4486v1, first public 2010-03-23. https://arxiv.org/abs/1003.4486

[2] J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 2015-12-22, in particular Sections 1–3 and Proposition 2. https://arxiv.org/html/1512.07289v1

[3] J. I. H. Barahona Torres, P. C. Manrique-Mirón and E. Treviño-Aguilar, *Angle distribution of two random chords in the disc: A sine law*, arXiv:1911.05576, first public 2019-11-13, Sections 1–3. https://arxiv.org/abs/1911.05576
