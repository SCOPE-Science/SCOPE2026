# A universal spectral-merger crossover for longest random chords of ellipsoids

## Finding
Let \(d\ge2\), \(m,r\ge1\), \(m+r\le d\), and \(h=d-m-r\). Let \(A>0\) and fix \(\beta_1,\ldots,\beta_h>0\). For a fixed vector \(\lambda=(\lambda_1,\ldots,\lambda_r)\in[0,\infty)^r\), consider the \(d\)-dimensional ellipsoid \(E_s\) with semiaxes \(A\) repeated \(m\) times, then \(A(1+s\lambda_j)^{-1/2}\) for \(1\le j\le r\), and then \(A(1+\beta_i)^{-1/2}\) for \(1\le i\le h\). Choose an affine line according to motion-invariant line measure conditioned on hitting \(E_s\), and let \(L_s\) be its chord length. Put \(N=m+r\), \(\nu=(2d-N-1)/2\), and
\[
M_0=\mathbb E_{U\sim\mathrm{Unif}(S^{d-1})}\sqrt{1+\sum_{i=1}^h\beta_iU_{N+i}^2},\qquad
K=\frac{\Gamma(d/2)\Gamma((d+1)/2)}{\Gamma(N/2)\Gamma(\nu+1)M_0\prod_{i=1}^h\sqrt{\beta_i}}.
\]
Then the **moving-ellipsoid longest-chord crossover** is
\[
\boxed{\Pr\{L_s>2A-As\}=K s^\nu\,[F_{m,r,\nu}(\lambda)+o(1)]}\quad(s\downarrow0),
\]
where the error is uniform when \(\lambda\) ranges over any compact subset of \([0,\infty)^r\), and the dimensionless crossover profile is
\[
\boxed{F_{m,r,\nu}(\lambda)=\mathbb E_{V\sim\mathrm{Unif}(S^{m+r-1})}
\left(1-\sum_{j=1}^r\lambda_j V_{m+j}^2\right)_+^\nu.}
\]
The function is continuous, equals \(1\) at \(\lambda=0\), and is strictly decreasing in each positive parameter. For every fixed \(\lambda_j>0\), it has the sharp **multi-axis matching limit**
\[
\boxed{F_{m,r,\nu}(t\lambda)\sim
\frac{\Gamma((m+r)/2)\Gamma(\nu+1)}{\Gamma(m/2)\Gamma(\nu+1+r/2)\prod_j\sqrt{\lambda_j}}\ t^{-r/2}}\qquad(t\to\infty).
\]
Thus a single profile interpolates between the long-chord exponent \((2d-m-r-1)/2\) at coalescence and the exponent \((2d-m-1)/2\) after all \(r\) small spectral gaps are resolved. In the intermediate regime \(\delta_j(s)\to0\) with \(s/\delta_j(s)\to0\), where the near axes are \(A(1+\delta_j(s))^{-1/2}\), the same calculation gives
\[
\Pr\{L_s>2A-As\}\sim\frac{\Gamma(d/2)\Gamma((d+1)/2)}{\Gamma(m/2)\Gamma((2d-m+1)/2)M_0\prod_i\sqrt{\beta_i}\prod_j\sqrt{\delta_j(s)}}\ s^{(2d-m-1)/2}.
\]
All products over empty sets equal one. This is a statement about a *moving family* of ellipsoids; it is not a fixed-body endpoint limit.

## Assumptions and scope
All dimensions are fixed and finite. Each \(E_s\) is centered and has precisely the displayed principal axes, with \(s>0\) tending to zero. For \(\lambda_j=0\), some near axes are exactly maximal; the displayed theorem remains valid without any generic-position assumption. An invariant affine line has uniform direction before conditioning and Lebesgue-distributed perpendicular offset. The conditioning weights directions by their projected brightness, rather than leaving their directions uniform. The profile does not depend on the absolute scale \(A\). The hard gaps \(\beta_i\) are held strictly positive; the compact-uniform statement refers only to the soft ratios \(\lambda_j\).

## Proof
Let \(p=(d-1)/2\), let \(U\) be uniform on \(S^{d-1}\), and let \(Q_s\) be the diagonal inverse-squared semiaxis matrix. Completing the square on each affine line and computing its projected offset ellipsoid yields the exact invariant-line survival identity
\[
\Pr(L_s>t)=\frac{\mathbb E[\sqrt{U^TQ_sU}\,(1-t^2U^TQ_sU/4)_+^p]}{\mathbb E\sqrt{U^TQ_sU}}.
\tag{1}
\]
Set \(t=2A-As\), \(v_s=(1-s/2)^2\), and \(H_s=1-v_s=s(1-s/4)\). For the first \(N=m+r\) coordinates put \(W=(U_1,\ldots,U_N)\) and for the last \(h\) coordinates put \(Z\). Then \(A^2 U^TQ_sU=1+s\sum_j\lambda_j W_{m+j}^2+\sum_i\beta_i Z_i^2\). The numerator of (1), after removing the common factor \(A^{-1}\), is
\[
\mathbb E\left[\sqrt{1+s\sum_j\lambda_jW_{m+j}^2+\sum_i\beta_i Z_i^2}
\left(H_s-v_s\left(s\sum_j\lambda_j W_{m+j}^2+\sum_i\beta_i Z_i^2\right)\right)_+^p\right].\tag{2}
\]
For \(h>0\), the density of \(Z\in B_h\) is
\[
\frac{\Gamma(d/2)}{\pi^{h/2}\Gamma(N/2)}(1-|Z|^2)^{N/2-1},
\]
and, conditioned on \(Z\), the direction \(W/\sqrt{1-|Z|^2}\) is uniform on \(S^{N-1}\). Replace \(Z_i=\sqrt{s}\,Y_i/\sqrt{\beta_i}\). The positive part confines \(Y\) to a bounded ball depending only on the soft parameters in a fixed compact set. Dividing (2) by \(s^{p+h/2}\) and using dominated convergence gives
\[
\frac{\Gamma(d/2)}{\pi^{h/2}\Gamma(N/2)\prod_i\sqrt{\beta_i}}
\mathbb E_{V\in S^{N-1}}\int_{\mathbb R^h}
\left(1-\sum_j\lambda_j V_{m+j}^2-|Y|^2\right)_+^p\,dY.
\tag{3}
\]
The beta-ball integral is \(\int_{\mathbb R^h}(b-|Y|^2)_+^p\,dY=\pi^{h/2}\Gamma(p+1)b_+^{p+h/2}/\Gamma(p+1+h/2)\). The denominator of (1) tends to \(M_0/A\). Since \(p+h/2=\nu\), (3) proves the boxed formula and the constant \(K\). The convergence is locally uniform in \(\lambda\), because the same compact bound dominates and the integrand is uniformly continuous in the parameters. If \(h=0\), (2) directly gives the same result without the \(Z\)-integral.

For large \(t\), let \(X=(V_{m+1},\ldots,V_{m+r})\). Its density in \(B_r\) is \(\Gamma(N/2)(1-|X|^2)^{m/2-1}/(\pi^{r/2}\Gamma(m/2))\). Substitute \(X_j=t^{-1/2}Y_j/\sqrt{\lambda_j}\) into the profile. The limiting beta-ball integral is \(\pi^{r/2}\Gamma(\nu+1)/\Gamma(\nu+1+r/2)\), yielding its exact large-parameter constant. For intermediate gaps \(\delta_j(s)\gg s\), scale *both* soft and hard sphere coordinates by \(\sqrt{s/\delta_j(s)}\) and \(\sqrt{s/\beta_i}\), respectively. The remaining sphere has dimension \(m-1\); a second application of the same beta-ball integral yields the final matching formula. In this regime all scaled coordinates vanish, and the denominator tends to \(M_0\). This establishes the theorem. \(\square\)

## Verification
The accompanying standalone numerical checker directly evaluates the exact line-survival sphere integral (1) and the limiting profile, including the nongeneric spectral-collision point. It tests the \(d=2\), \(m=r=1\), \(h=0\) case with multiple spectral gap ratios against the sharp scaling, and independently compares the large-gap profile constant with direct quadrature. Numerical convergence is supportive; proof for all dimensions and parameters is analytic.

## Relationship to prior work
The earlier exact ellipsoid line-chord survival identity and its **fixed-ellipsoid**, largest-axis-multiplicity endpoint asymptotic (finding 56f6a477-0f49-4817-ae8b-ee8ba9baa532) are explicit starting points, **not claimed as new**. Crucially, their endpoint asymptotic assumes fixed positive spectral gaps and does not allow the gap to vanish at the same rate as the chord deficit. The moving-family limit in this theorem is not obtained by substituting a vanishing gap into that fixed-body limit: those operations do not commute, and the crossover profile is nonconstant. This finding resolves the nonuniform eigenvalue-collision boundary layer and gives a matching multiaxis transition. Gečiauskas's integral-geometric chord/distance relations, Suwa's ellipsoid test-line sampling, and Kellerer's spheroid chord formulas give relevant forward geometric and stereological background. The inspected original papers do not state a general higher-dimensional, multiaxis simultaneous spectral-gap crossover. The older exact finite-threshold sphere identity mathematically permits the present asymptotic to be derived; the claimed contribution is the **evaluated singular joint limit, its locally uniform validity, and its sharp matching behavior**, not a new exact chord distribution. An equivalent uninspected historical scaling formulation remains a priority risk.

## Limitations
The theorem holds for fixed dimension and fixed hard gaps; it does not give uniform bounds as a hard gap also vanishes unless that gap is incorporated among the \(r\) soft axes. No assertion of statistical identifiability or finite-sample recovery is made, and the numerical tests are not infinite proofs. Scientific priority has not been independently audited. Publication metadata for one scanned historical reference disagree on the year; the precise public date used in the research record is that of the separately verified 1968 journal item.

## References
1. E. Gečiauskas, “The method of the integral geometry for finding the distribution functions of chord length of an oval and of distance in an oval,” *Lithuanian Mathematical Journal* 8 (1968), 237–241, DOI 10.15388/LMJ.1968.20212. The journal records publication on April 7, 1968: https://www.journals.vu.lt/LMJ/article/view/20212.
2. N. Suwa, “Estimation of the Distribution of Ellipsoids with Random Test Lines,” *Tohoku Journal of Experimental Medicine* 121 (1977), 365–370, DOI 10.1620/tjem.121.365, https://www.jstage.jst.go.jp/article/tjem1920/121/4/121_4_365/_pdf.
3. A. M. Kellerer, “Chord-Length Distributions and Related Quantities for Spheroids,” *Radiation Research* 98 (1984), 425–437, DOI 10.2307/3576477, https://epub.ub.uni-muenchen.de/8751/1/8751.pdf.
