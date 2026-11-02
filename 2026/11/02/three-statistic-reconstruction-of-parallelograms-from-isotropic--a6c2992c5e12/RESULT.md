# Three-statistic reconstruction of parallelograms from isotropic random chords

## Finding

Let \(Q\) be any nondegenerate Euclidean parallelogram. Sample an unoriented affine line with the motion-invariant measure \(d\theta\,dt\), conditioned on intersecting \(Q\), and let \(L\) be the resulting chord length. Write \(S(x)=\Pr(L>x)\), and define three observables:

\[
\mu=\mathbb E L,\qquad \kappa=-S'(0+),\qquad h=\sup\{r>0:S(x)=1-\kappa x\text{ for every }0\le x\le r\}.
\]

**Three-statistic inverse and feasibility theorem.** The triple \((\mu,\kappa,h)\) determines \(Q\) up to Euclidean congruence. Exactly the positive triples satisfying

\[
\alpha:=\frac{2\mu}{\pi h}\in[1/2,1),\qquad q:=\frac{\kappa h}{1-\alpha}\in[1,\pi/2)
\]

occur. Given such a triple, the unique acute or right angle \(\delta\in(0,\pi/2]\) solves

\[
J(\delta):=(\pi/2-\delta)\cos\delta+\sin\delta=q.
\]

Writing \(s=h/((1-\alpha)\sin\delta)\), the two side lengths in decreasing order are \(a=\alpha s\) and \(b=(1-\alpha)s\). Rectangles are characterized exactly by \(q=1\), and rhombi by \(\alpha=1/2\).

The first departure from the affine small-chord survival law is a genuine square-root cusp. If \(a\ge b>0\) are the side lengths, \(h=b\sin\delta\), and \(m=1\) for \(a>b\) while \(m=2\) for \(a=b\), then

\[
(1-\kappa(h+u))-S(h+u)
\sim \frac{m(a-b\cos\delta)}{a+b}\sqrt{\frac{2u}{h}}
\quad(u\downarrow0).
\]

The inverse angle map has a sharp square-root singularity at rectangles: as \(q\downarrow1\),

\[
\frac\pi2-\delta=\sqrt{2(q-1)}+O((q-1)^{3/2}).
\]

## Assumptions and scope

All lengths are ordinary Euclidean lengths; there is no perimeter or area normalization. A parallelogram is the Minkowski sum of two nonzero segments with side lengths \(a\ge b>0\), meeting at the acute or right *edge-line* angle \(0<\delta\le\pi/2\); reversing an edge vector replaces an obtuse angle by its acute supplement without changing the congruence class. The line distribution is conditioned from the invariant measure on all unoriented affine lines, so its orientation has a **width-biased** marginal. The triple is a property of the **unlabeled** chord-length law, without recording directions of individual chords.

## Proof

Let \(C=ab\sin\delta\) be the area of \(Q\). A line parallel to \((\cos\theta,\sin\theta)\) has transverse generator widths
\[
A_\theta=a|\sin\theta|,\qquad B_\theta=b|\sin(\theta-\delta)|,
\]
so the total transverse width is \(A_\theta+B_\theta\). The distribution of the transverse coordinate of a uniform interior point is the convolution of two uniform distributions on intervals of lengths \(A_\theta\) and \(B_\theta\). Dividing the associated area-density by the chord length shows that the chord profile under uniform transverse offset consists of two linear ramps of total transverse width \(2\min(A_\theta,B_\theta)\) and a constant plateau of width \(|A_\theta-B_\theta|\); its maximum is \(C/\max(A_\theta,B_\theta)\). This elementary construction is also valid almost everywhere when either transverse generator width vanishes, by continuity.

Therefore, for every \(x\ge0\), the exact survival probability is

\[
S(x)=\frac{1}{2(a+b)}\int_0^\pi
\mathbf1_{\{x<C/\max(A_\theta,B_\theta)\}}
\left(A_\theta+B_\theta-\frac{2A_\theta B_\theta x}{C}\right)\,d\theta.
\tag{1}
\]

The total measure of intersecting lines is \(\int_0^\pi(A_\theta+B_\theta)d\theta=2(a+b)\). Moreover, for each orientation the integral of chord length over offsets is area \(C\), so

\[
\mu=\frac{\pi C}{2(a+b)}=\frac{\pi ab\sin\delta}{2(a+b)}.
\tag{2}
\]

Since \(\max(A_\theta,B_\theta)\le a\), every maximal directional chord is at least \(h_0=C/a=b\sin\delta\), with equality near the direction normal to the longer edge. For \(0\le x\le h_0\), the indicator in (1) equals one for almost all orientations. Splitting the trigonometric integral at \(\delta\) gives

\[
\int_0^\pi|\sin\theta\sin(\theta-\delta)|\,d\theta
=(\pi/2-\delta)\cos\delta+\sin\delta=J(\delta),
\]

hence

\[
S(x)=1-\frac{J(\delta)}{(a+b)\sin\delta}x\quad(0\le x\le h_0),
\qquad \kappa=\frac{J(\delta)}{(a+b)\sin\delta}.
\tag{3}
\]

To show that \(h=h_0\) is the **maximal** affine interval, examine \(\theta=\pi/2\). Because \(a>b\cos\delta\), the larger transverse width there is \(A_\theta=a\); locally the maximum chord is \(h_0/|\sin\theta|\). Once \(x=h_0+u\) with \(u>0\), formula (1) excludes a neighborhood of this orientation of half-width \(\arccos(h_0/(h_0+u))\sim\sqrt{2u/h_0}\). At its center the excluded integrand tends to \(a-b\cos\delta>0\), so the resulting deficit from the affine continuation is positive and has the stated square-root asymptotic. When \(a=b\), a second distinct global transverse-width maximum contributes equally. No other orientation can contribute at this first cutoff. Thus \(h=h_0\) and the displayed cusp formula holds, including rhombi and rectangles.

Combining (2) and (3),

\[
\frac{2\mu}{\pi h}=\frac a{a+b}=\alpha,
\qquad
\frac{\kappa h}{1-\alpha}=J(\delta)=q.
\tag{4}
\]

The derivative \(J'(\delta)=-(\pi/2-\delta)\sin\delta<0\) for \(0<\delta<\pi/2\), and \(J(\pi/2)=1\) while \(\lim_{\delta\downarrow0}J(\delta)=\pi/2\). Consequently the specified interval of \(q\) gives precisely one nondegenerate angle. The given formulas recover \(a,b\), proving injectivity. Conversely, every admissible \((\alpha,q,h)\) produces positive \(a,b\) and an angle in the required interval; substitution into (2)--(4) reproduces exactly the proposed triple. This proves necessity and sufficiency of the feasible domain.

Finally set \(\varepsilon=\pi/2-\delta\). The identity \(J(\delta)=\varepsilon\sin\varepsilon+\cos\varepsilon\) yields \(q-1=\varepsilon^2/2+O(\varepsilon^4)\), and inversion gives the asserted optimal exponent \(1/2\). An exponent larger than \(1/2\) is impossible for recovering the angle from \(q\) along this family.

## Verification

The accompanying standalone standard-library Python program `verify.py` computes the orientation integral in (1) by midpoint quadrature for seven noncongruent parameter choices, checks exact affine behavior below \(h\), positive square-root departure above \(h\) and its predicted coefficient, verifies the trigonometric integral \(J\), and reconstructs all input shapes by bisection. It also checks the rectangular endpoint and the angle-conditioning asymptotic. It returned `ALL_CHECKS_PASSED` in the recorded run. Numerical quadrature provides finite checks only; the proof above does not rely on numerical extrapolation.

## Relationship to prior work

Gasparyan and Ohanyan (2014) established explicit **forward** orientation-dependent and isotropic chord-length distribution formulas for any parallelogram, including a seven-case geometric division of chord-length ranges. This result is taken as established, not claimed anew. Martirosyan (2023) developed forward orientation-dependent chord-length formulas for arbitrary convex quadrilaterals. The present statement concerns a different inverse question: reconstructing a parallelogram from just the mean, initial density and first nonaffine threshold of its **unlabeled invariant-line** chord law, with a complete feasible signature region and an exact inverse-conditioning boundary. A published width-statistics inverse result addresses projections under uniform direction sampling, not invariant-line chords or this three-statistic map. No exhaustive priority claim is made for the inverse theorem.

## Limitations

The reconstruction is within the class of nondegenerate Euclidean parallelograms and assumes ideal exact law-level statistics. It does not claim identifiability of arbitrary quadrilaterals or convex bodies from these three numbers. Estimation of the first cutoff from finite noisy data can be difficult, especially near rectangles, and no nonasymptotic estimation guarantees are established. The sharp Hölder exponent concerns angular recovery with fixed other signature coordinates near the rectangular boundary; it is not a global bi-Hölder theorem. Specialized earlier chord-length distribution literature may contain equivalent inverse statements not found in the inspected material; independent historical priority confirmation remains open.

## References

1. A. G. Gasparyan and V. K. Ohanyan, *Covariogram of a parallelogram*, Journal of Contemporary Mathematical Analysis 49 (2014), 194--206, DOI:10.3103/S1068362314040050. Author-uploaded complete text examined, especially Sections 2--4.
2. D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, Journal of Contemporary Mathematical Analysis 58 (2023), 416--430, first online December 28, 2023, DOI:10.3103/S1068362323060055. Open full text examined, Sections 1--4.
3. W. Nagel, *Orientation-dependent chord length distributions characterize convex polygons*, Journal of Applied Probability 30 (1993), 730--736. Used only for the distinction between directed and undirected tomography.
