# Sharp Steiner-disk Hausdorff stability for planar bodies of constant width

## Result

Let \(K\subset\mathbb R^2\) be a convex body of constant width \(w>0\), let \(s(K)\) be its Steiner point, and let
\[
B_S:=B\!\left(s(K),\frac w2\right)
\]
be its Steiner disk. Write
\[
\varepsilon(K):=\frac{\pi w^2}{4}-A(K),\qquad
\rho(K):=d_H(K,B_S).
\]
Then
\[
\boxed{\qquad
\varepsilon(K)\ge 2\pi\,\rho(K)^2,
\qquad}
\]
or equivalently
\[
\boxed{\qquad
d_H(K,B_S)\le
\frac{1}{\sqrt{2\pi}}\,
\sqrt{\frac{\pi w^2}{4}-A(K)}.
\qquad}
\]

The constant \(2\pi\) is best possible, even among \(C^\infty\), strictly convex constant-width bodies arbitrarily close to a disk. Equality holds only for the disk; the sharp constant is approached by a smooth sequence of noncircular bodies.

For width \(w=1\), Groemer's 1988 stability theorem gives the existence of a diameter-one disk \(D\) with
\[
d_H(K,D)\le \frac12\sqrt{\frac{\pi}{4}-A(K)}.
\]
The inequality above replaces the unspecified comparison disk by the canonical Steiner disk and improves the coefficient \(1/2\) to
\[
\frac1{\sqrt{2\pi}}\approx0.39894228.
\]
Sharpness here is asserted for distance to the Steiner disk; no claim is made that \(1/\sqrt{2\pi}\) is the best constant after optimizing over all translated disks.

## Proof

Translate \(K\) so that its Steiner point is the origin. Let \(h(\theta)\) be its support function. Constant width gives
\[
h(\theta)+h(\theta+\pi)=w.
\]
The zeroth Fourier coefficient is therefore \(w/2\), all positive even modes vanish, and the choice of the Steiner point as origin kills the first harmonics. Hence
\[
h(\theta)=\frac w2+q(\theta),
\]
where
\[
q(\theta)=
\sum_{\substack{n\ge3\\ n\ {\rm odd}}}
\bigl(a_n\cos n\theta+b_n\sin n\theta\bigr).
\]

For planar convex bodies the support-function area formula, equivalently its Fourier form, gives
\[
A(K)
=
\frac{\pi w^2}{4}
-\frac{\pi}{2}
\sum_{\substack{n\ge3\\n\ {\rm odd}}}
(n^2-1)(a_n^2+b_n^2).
\]
Thus
\[
\varepsilon(K)
=
\frac{\pi}{2}
\sum_{\substack{n\ge3\\n\ {\rm odd}}}
(n^2-1)(a_n^2+b_n^2).
\tag{1}
\]

Because \(B_S\) has support function \(w/2\) in these coordinates, the support-function formula for Hausdorff distance gives
\[
\rho(K)=\|q\|_\infty.
\tag{2}
\]
For every \(\theta\), weighted Cauchy--Schwarz yields
\[
\begin{aligned}
|q(\theta)|^2
&\le
\left(
\sum_{\substack{n\ge3\\n\ {\rm odd}}}
\frac{\cos^2 n\theta+\sin^2 n\theta}{n^2-1}
\right)
\left(
\sum_{\substack{n\ge3\\n\ {\rm odd}}}
(n^2-1)(a_n^2+b_n^2)
\right)\\
&=
\left(
\sum_{k=1}^{\infty}\frac1{(2k+1)^2-1}
\right)\frac{2\varepsilon(K)}{\pi}.
\end{aligned}
\]
The scalar series telescopes:
\[
\sum_{k=1}^{\infty}\frac1{(2k+1)^2-1}
=
\frac14\sum_{k=1}^{\infty}\frac1{k(k+1)}
=\frac14.
\]
Therefore
\[
|q(\theta)|^2\le \frac{\varepsilon(K)}{2\pi}
\]
for all \(\theta\). Taking the supremum and using (2) proves
\[
\varepsilon(K)\ge2\pi\rho(K)^2.
\]

The argument is valid directly at the natural \(H^1\) regularity of support functions: the weighted Fourier energy in (1) is finite, and the same Cauchy--Schwarz estimate makes the Fourier series uniformly Cauchy. Alternatively, one may first prove the statement for smooth support functions and pass to the limit by circular convolution, which preserves constant width and the Steiner center.

## Sharpness

For \(N\ge1\), put
\[
q_N(\theta)
=
\sum_{k=1}^{N}
\frac{\cos((2k+1)\theta)}{(2k+1)^2-1}
\]
and choose any \(t_N>0\) satisfying \(t_NN<w/2\). Then
\[
h_N(\theta)=\frac w2+t_Nq_N(\theta)
\]
is the support function of a \(C^\infty\), strictly convex body of constant width \(w\): indeed
\[
h_N+h_N''
=
\frac w2-t_N\sum_{k=1}^{N}\cos((2k+1)\theta)
>0.
\]
There is no first harmonic, so the origin is its Steiner point.

Set
\[
S_N:=
\sum_{k=1}^{N}\frac1{(2k+1)^2-1}
=
\frac{N}{4(N+1)}.
\]
All coefficients in \(q_N\) are positive, hence \(\|q_N\|_\infty=q_N(0)=S_N\). Consequently
\[
\rho_N=t_NS_N,
\qquad
\varepsilon_N=\frac{\pi}{2}t_N^2S_N,
\]
and therefore
\[
\frac{\varepsilon_N}{\rho_N^2}
=
\frac{\pi}{2S_N}
=
2\pi\frac{N+1}{N}
\longrightarrow 2\pi.
\]
Thus the constant \(2\pi\) cannot be increased, even locally around the disk within smooth strictly convex constant-width bodies.

## Equality

Suppose a noncircular body attained equality. Equality in the pointwise Cauchy--Schwarz step at a maximizing direction \(\theta_0\) forces, up to a nonzero scalar and rotation, the Fourier profile
\[
q(\theta)
=
c\sum_{\substack{n\ge3\\n\ {\rm odd}}}
\frac{\cos n(\theta-\theta_0)}{n^2-1}.
\]
In the sense of periodic distributions,
\[
\sum_{\substack{n\ge3\\n\ {\rm odd}}}\cos nx
=
\frac{\pi}{2}(\delta_0-\delta_\pi)-\cos x.
\]
Hence the curvature measure \(h+h''\) of the putative extremizer contains a negative Dirac mass at one of the antipodal directions (the sign depends on \(c\)). This is incompatible with convexity. Therefore the only equality case is \(q\equiv0\), i.e. the disk.

## Relation to known results

Groemer proved in 1988 that if a convex domain \(K\) has diameter one and
\[
A(K)\ge \frac{\pi}{4}-\varepsilon,
\]
then there is a disk \(D\) with
\[
d_H(K,D)\le \frac12\sqrt{\varepsilon};
\]
when \(K\) has constant width one, \(D\) may be chosen with diameter one. The present estimate is a sharper, canonical-center statement for the constant-width case.

The support-function ingredients used above are classical. In particular, for a planar convex body,
\[
A(K)=\frac12\int_0^{2\pi}(h^2-h'^2)\,d\theta,
\]
the Steiner point is exactly the first Fourier harmonic of \(h\), and constant width removes all positive even harmonics. These facts are also stated explicitly in recent Fourier-analytic work on planar constant-width bodies. Cufí, Gallego and Reventós use the Steiner disk and Fourier support functions in related \(L^2\)-type deficit inequalities, but their surfaced results concern the Hurwitz deficit and \(L^2\) distance rather than the Hausdorff estimate above.

Searches through the directly relevant stability literature, later papers citing Groemer's theorem, constant-width Fourier formulations, Steiner-disk terminology, Hausdorff/support-function formulations, and equivalent area-deficit language did not locate the sharp \(2\pi\) inequality above. The originality claim is therefore only to the best of our knowledge; an equivalent estimate could exist under a different support-function or Sobolev-embedding formulation.

## Limitations

- The theorem is two-dimensional and Euclidean.
- The comparison disk is specifically the Steiner disk. The optimal constant for the distance to the best translated disk is not determined here.
- The best constant is not attained by any noncircular convex body; it is realized only as a limit of smooth strictly convex examples.
- The originality assessment is literature-limited and is not a claim of exhaustive coverage.

## References

1. H. Groemer, *Stability Theorems for Convex Domains of Constant Width*, Canadian Mathematical Bulletin **31** (1988), 328--337. DOI: 10.4153/CMB-1988-048-3.
2. J. Cufí, E. Gallego, A. Reventós, *A note on Hurwitz's inequality*, Journal of Mathematical Analysis and Applications **458** (2018), 436--451. DOI: 10.1016/j.jmaa.2017.09.017.
3. C. Thäle, *A note on a problem posed by Linderholm*, Journal of Geometry **117** (2026), Article 1. DOI: 10.1007/s00022-025-00783-4.
4. H. Groemer, *Geometric Applications of Fourier Series and Spherical Harmonics*, Cambridge University Press, 1996.
