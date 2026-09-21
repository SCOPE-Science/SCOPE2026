# Sharp angular support stability for planar bodies of constant width

**Publication identity:** `7b7a6362-1f57-4e92-b665-335204af2224`  
**Record:** `SCOPE-20260921-11cc15235c14`  
**Publication date:** 2026-09-21 UTC

## Result

Let \(K\subset\mathbb R^2\) be a planar convex body of constant width \(w>0\). Let \(s(K)\) be its Steiner point and let
\[
B_S(K):=B\!\left(s(K),\frac w2\right)
\]
be the Steiner disk. Define the circle-area deficit
\[
D(K):=\frac{\pi w^2}{4}-A(K)
\]
and the canonical Hausdorff deviation
\[
\delta_S(K):=d_H\!\left(K,B_S(K)\right).
\]

Then
\[
\boxed{D(K)\ge 2\pi\,\delta_S(K)^2.}
\]

The constant \(2\pi\) is best possible over all planar constant-width bodies. Equivalently, since Barbier's theorem gives \(L(K)=\pi w\),
\[
L(K)^2-4\pi A(K)\ge 8\pi^2\,\delta_S(K)^2.
\]

This gives a canonical-center strengthening of the circular-side stability estimate in Groemer's 1988 theorem: after normalizing \(w=1\), Groemer proved that some diameter-one disk \(D\) satisfies
\[
\frac{\pi}{4}-A(K)\ge 4\,d_H(K,D)^2.
\]
Here the disk is prescribed to be the Steiner disk and the sharp coefficient is \(2\pi\).

## Proof

Translate \(K\) so that \(s(K)=0\), and write its support function as
\[
h(\theta)=\frac w2+f(\theta).
\]
The constant-width identity \(h(\theta)+h(\theta+\pi)=w\) eliminates all nonconstant even Fourier modes, while Steiner centering eliminates the first harmonics. Hence
\[
f(\theta)=\sum_{\substack{n\ge3\\ n\ {\rm odd}}}
\bigl(a_n\cos n\theta+b_n\sin n\theta\bigr).
\]
For support functions of planar convex bodies the area formula is
\[
A(K)=\frac12\int_0^{2\pi}\bigl(h^2-h'^2\bigr)\,d\theta.
\]
Consequently,
\[
D(K)=\frac{\pi}{2}
\sum_{\substack{n\ge3\\ n\ {\rm odd}}}
(n^2-1)(a_n^2+b_n^2).
\]
Set
\[
E:=\sum_{\substack{n\ge3\\ n\ {\rm odd}}}
(n^2-1)(a_n^2+b_n^2).
\]
The Hausdorff metric between convex bodies is the uniform metric on support functions, so
\[
\delta_S(K)=\|f\|_\infty.
\]
For every \(\theta\), weighted Cauchy--Schwarz gives
\[
|f(\theta)|^2
\le E
\sum_{\substack{n\ge3\\ n\ {\rm odd}}}\frac1{n^2-1}.
\]
Writing \(n=2k+1\),
\[
\sum_{k=1}^\infty\frac1{(2k+1)^2-1}
=\frac14\sum_{k=1}^\infty\left(\frac1k-\frac1{k+1}\right)
=\frac14.
\]
Thus \(\delta_S(K)^2\le E/4\). Since \(D(K)=(\pi/2)E\), the claimed inequality follows.

The formulas above hold directly for support functions in \(H^1(S^1)\), which includes planar convex bodies. Alternatively, one may convolve the support function with a circular mollifier; this preserves convexity, constant width and Steiner centering, and the result passes to the Hausdorff limit.


## Sharp angular support kernel

The scalar Hausdorff estimate is the antipodal endpoint of a stronger two-direction theorem. With the Steiner point translated to the origin, put
\[
f(\theta):=h_K(\theta)-\frac w2.
\]
For two support directions whose shorter angular separation is \(d\in[0,\pi]\),
\[
\boxed{
|f(\theta)-f(\phi)|^2
\le
\frac{2D(K)}{\pi}\,
\mathcal M(d),
}
\]
where
\[
\boxed{
\mathcal M(d)
=
\frac{1-\cos d}{2}
+
\left(\frac{\pi}{2}-d\right)\sin d.
}
\]
The coefficient \(\mathcal M(d)\) is sharp for every fixed \(d\in(0,\pi]\).

To prove this, weighted Cauchy--Schwarz gives
\[
|f(\theta)-f(\phi)|^2
\le
E
\sum_{\substack{n\ge3\\n\ {\rm odd}}}
\frac{2-2\cos(nd)}{n^2-1}.
\]
For \(0\le d\le\pi\),
\[
\sum_{\substack{n\ge3\\n\ {\rm odd}}}
\frac{\cos(nd)}{n^2-1}
=
\frac12\left(d-\frac\pi2\right)\sin d+\frac14\cos d,
\]
and the sum without the cosine is \(1/4\). Hence the last spectral sum is exactly \(\mathcal M(d)\), and \(E=2D(K)/\pi\).

For sharpness at a prescribed \(d\), truncate the odd frequencies and take
\[
a_n=c_N\frac{\cos(nd)-1}{n^2-1},
\qquad
b_n=c_N\frac{\sin(nd)}{n^2-1}.
\]
Then the quotient in the displayed angular estimate equals the corresponding finite spectral sum. Choosing \(c_N=w/(8N)\) makes
\[
\left|f_N+f_N''\right|\le 2Nc_N=\frac w4,
\]
so \(h_N+h_N''\ge w/4\) and the truncations are smooth strictly convex constant-width bodies. Their quotients converge to equality for the chosen \(d\).

At \(d=\pi\), \(\mathcal M(\pi)=1\) and \(f(\theta+\pi)=-f(\theta)\). Thus
\[
4|f(\theta)|^2\le \frac{2D(K)}{\pi},
\]
which recovers \(D(K)\ge2\pi\delta_S(K)^2\). In this sense the optimal Hausdorff coefficient is the antipodal value of the full angular stability kernel.

## Sharpness

For \(N\ge1\), let
\[
h_N(\theta)=\frac w2+c_N
\sum_{k=1}^N
\frac{\cos((2k+1)\theta)}{(2k+1)^2-1},
\qquad
c_N=\frac{w}{4N}.
\]
Then
\[
h_N+h_N''
=
\frac w2-c_N\sum_{k=1}^N\cos((2k+1)\theta)
\ge \frac w4>0,
\]
so \(h_N\) is the support function of a smooth strictly convex body. It has constant width \(w\) and Steiner point \(0\). With
\[
S_N:=\sum_{k=1}^N\frac1{(2k+1)^2-1}
=\frac{N}{4(N+1)},
\]
the maximum support deviation occurs at \(\theta=0\), giving
\[
\delta_S(K_N)=c_NS_N,
\qquad
D(K_N)=\frac{\pi}{2}c_N^2S_N.
\]
Therefore
\[
\frac{D(K_N)}{\delta_S(K_N)^2}
=
\frac{\pi}{2S_N}
=
2\pi\frac{N+1}{N}
\longrightarrow 2\pi.
\]
Hence no larger universal coefficient can replace \(2\pi\).

## Rotational-symmetry refinement

Suppose in addition that \(K\) has rotational symmetry of order \(q\ge3\).

If \(q\) is even, the half-turn belongs to the symmetry group. Constant width then forces
\[
h(\theta)=h(\theta+\pi)=w-h(\theta),
\]
so \(K\) is the disk.

If \(q\) is odd, only the frequencies
\[
n=q(2k+1),\qquad k=0,1,2,\ldots
\]
can occur after Steiner centering. The same Cauchy--Schwarz argument gives
\[
D(K)\ge C_q\,\delta_S(K)^2,
\qquad
\boxed{C_q=2q\cot\!\left(\frac{\pi}{2q}\right)}.
\]
Indeed,
\[
\sum_{k=0}^\infty
\frac1{q^2(2k+1)^2-1}
=
\frac{\pi}{4q}\tan\!\left(\frac{\pi}{2q}\right),
\]
using the standard partial-fraction expansion of the tangent function. Each \(C_q\) is sharp: truncate these admissible modes with coefficients proportional to
\[
\frac1{q^2(2k+1)^2-1}
\]
and choose the common amplitude small enough that \(h+h''>0\). The finite-mode ratios converge to \(C_q\). For example,
\[
C_3=6\sqrt3.
\]

## Closest prior work and originality boundary

The closest older source is H. Groemer, *Stability Theorems for Convex Domains of Constant Width*, Canadian Mathematical Bulletin 31 (1988), 328--337, DOI 10.4153/CMB-1988-048-3. Its Theorem 1(b) and Corollary 1 give the coefficient \(4\) for Hausdorff distance to a suitably chosen disk of the same width; they do not prescribe the Steiner center or state the sharp coefficient above.

Alvino--Ferone--Nitsch (2009) determine a sharp planar isoperimetric profile for a different Hausdorff asymmetry optimized over comparison disks. Gao (2011) develops Fourier stability estimates relative to the Steiner disk for general convex curves, and Cufí--Gallego--Reventós (2018) obtain stability bounds involving an \(L^2\) support-function distance to the Steiner disk and special improvements for constant-width bodies. These are adjacent but do not, in the inspected statements, give the sharp constant-width Hausdorff coefficient \(2\pi\).

A 2025 paper on Linderholm's problem explicitly records the same constant-width Fourier sparsity and area identity used here, but applies them to areas of circumscribed right triangles rather than Hausdorff stability. Recent general parametric isoperimetric stability work was also checked for current-status coverage.

Targeted searches for the exact inequality, equivalent support-function formulations, the angular support kernel, the coefficient \(2\pi\), and the symmetry constants \(2q\cot(\pi/(2q))\) did not locate the statements above. The originality claim is therefore **to the best of our knowledge**, not an assertion that all older convex-geometry literature has been exhausted.

One material residual risk is Deyan Zhang, *A note on the isoperimetric deficit*, J. Math. Anal. Appl. 478 (2019), 14--32, DOI 10.1016/j.jmaa.2019.04.047. Its abstract states that it gives several upper and lower deficit bounds, but the full theorem text was not inspected here; an equivalent specialized constant-width consequence there would affect priority.

## Limitations

- The result is two-dimensional and Euclidean; no higher-dimensional constant-width analogue is claimed.
- The comparison disk is specifically the Steiner disk. No optimality statement is made for other center choices beyond the displayed uniform constant.
- The coefficient \(2\pi\) is globally sharp through a smooth sequence approaching the disk; no noncircular equality case is claimed.
- The symmetry refinement concerns cyclic rotational symmetry. Reflectional symmetry alone is not classified here.
- The result quantifies the area deficit near the maximal-area disk, not stability near the Reuleaux-triangle minimum.

## Reproducibility

`artifacts/verify_constants.py` verifies the telescoping partial sums, the closed angular-kernel formula, the approach to the sharp coefficient \(2\pi\), and the closed form for the symmetry constants numerically using only the Python standard library. The analytic proof above is the certificate; the computation is only a consistency check.

## References

1. H. Groemer, *Stability Theorems for Convex Domains of Constant Width*, Canadian Mathematical Bulletin 31 (1988), 328--337. https://doi.org/10.4153/CMB-1988-048-3
2. A. Alvino, V. Ferone, C. Nitsch, *A sharp isoperimetric inequality in the plane involving Hausdorff distance*, Rend. Lincei Mat. Appl. 20 (2009), 397--412. https://doi.org/10.4171/RLM/555
3. X. Gao, *A Note On The Isoperimetric Inequality And Its Stability*, arXiv:1102.5642 (2011). https://arxiv.org/abs/1102.5642
4. J. Cufí, E. Gallego, A. Reventós, *A note on Hurwitz's inequality*, J. Math. Anal. Appl. 458 (2018), 436--451. https://doi.org/10.1016/j.jmaa.2017.09.017
5. D. Zhang, *A note on the isoperimetric deficit*, J. Math. Anal. Appl. 478 (2019), 14--32. https://doi.org/10.1016/j.jmaa.2019.04.047
6. *A note on a problem posed by Linderholm*, Journal of Geometry (2025). https://doi.org/10.1007/s00022-025-00783-4
7. H. Zhao, *A family of parametric isoperimetric-type inequalities with multiple geometric quantities*, arXiv:2605.26780 (2026). https://arxiv.org/abs/2605.26780
