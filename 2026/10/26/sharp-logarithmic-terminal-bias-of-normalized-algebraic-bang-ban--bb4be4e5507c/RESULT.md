# Sharp logarithmic terminal bias of normalized-algebraic bang-bang smoothing

## Finding
For a fixed smooth switching function with finitely many nondegenerate switching instants, the normalized-algebraic approximation to bang-bang control has a universal **logarithmic first-order weak bias**. In precise terms, define \(u_\delta(t)=S(t)/\sqrt{S(t)^2+\delta}\) and \(u_0(t)=\operatorname{sgn}S(t)\), and let \(t_1,\ldots,t_k\) be the interior simple zeros of \(S\). For any smooth scalar observation weight \(w\),
\[
\boxed{\int_a^b w(t)(u_\delta(t)-u_0(t))\,dt
=-\frac{\delta}{2}\log(1/\delta)\sum_{j=1}^k
\frac{w'(t_j)S'(t_j)-w(t_j)S''(t_j)}{|S'(t_j)|^3}
+O(\delta).}
\]
Meanwhile, the strong error obeys the different sharp law
\[
\boxed{\int_a^b |u_\delta(t)-u_0(t)|\,dt
=2\sqrt{\delta}\sum_{j=1}^k\frac1{|S'(t_j)|}+O(\delta\log(1/\delta)).}
\]
The logarithmic coefficient vanishes exactly when the indicated sum vanishes, in which case the weak error is \(O(\delta)\); nonvanishing makes \(\delta\log(1/\delta)\) an attained, not merely upper, order.

For the double integrator \(\dot x=v,\ \dot v=u\) on \([0,T]\), take the frozen single-switch profile \(S(t)=t-\tau\), \(0<\tau<T\), and equal initial states under smoothed and discontinuous controls. Then
\[
\boxed{x_\delta(T)-x_0(T)=\tfrac12\delta\log(1/\delta)+O(\delta),\qquad
v_\delta(T)-v_0(T)=O(\delta),}
\]
for every interior switching time. Thus the position error is asymptotically larger than any constant multiple of \(\delta\), even when the velocity error vanishes identically by symmetry.

## Assumptions and scope
Take a fixed real compact interval \([a,b]\), \(a<b\), a real \(C^3\) function \(S\), and a real \(C^2\) observation weight \(w\). Assume \(S(a)S(b)\ne0\), every zero of \(S\) lies in \((a,b)\), there are finitely many, and \(S'(t_j)\ne0\) at every zero. Set \(\operatorname{sgn}(0)=0\), which does not affect any integral. The limit is \(\delta\downarrow0\) through positive reals; implicit constants can depend on \(S,w,a,b\), never on \(\delta\). Empty zero sets are allowed: then the weak and strong differences are \(O(\delta)\). Controls are compared at the **same prescribed switching function**, not after reoptimization of costates, switching times, or boundary constraints.

For bang-bang controls of the form \(c_0+c_1\operatorname{sgn}S\), multiply every error and every leading coefficient by \(c_1\). For the Pontryagin-minimizing convention \(u= -\operatorname{sgn}S\), reverse the sign of the weak error.

## Proof
Write \(g_\delta(s)=s/\sqrt{s^2+\delta}-\operatorname{sgn}s\). This is odd; for \(s>0\),
\[
|g_\delta(s)|=1-\frac{s}{\sqrt{s^2+\delta}}
\le\min\{1,\delta/(2s^2)\}.
\]
Fix disjoint neighborhoods of the simple roots on which \(S\) is monotone; shrink each so the image contains a symmetric interval \([-r_j,r_j]\). On its inverse branch \(t_j(s)\), ordinary change of variables with positive measure gives the density
\[
\phi_j(s)=\frac{w(t_j(s))}{|S'(t_j(s))|},\qquad
\phi_j'(0)=\frac{w'(t_j)S'(t_j)-w(t_j)S''(t_j)}{|S'(t_j)|^3}.
\]
The contribution from a common symmetric subinterval in the \(s\)-coordinate is \(\int_{-r_j}^{r_j}\phi_j(s)g_\delta(s)\,ds\). The constant Taylor term vanishes by oddness. The linear term equals \(\phi_j'(0)M_\delta(r_j)\), where direct integration gives
\[
M_\delta(r)=\int_{-r}^r s g_\delta(s)\,ds
=r\sqrt{r^2+\delta}-r^2-\delta\operatorname{arsinh}(r/\sqrt\delta)
=-\tfrac\delta2\log(1/\delta)+O(\delta).
\]
Because \(\phi_j(s)=\phi_j(0)+s\phi_j'(0)+O(s^2)\), the Taylor remainder integrates to \(O(\delta)\): use \(|g_\delta(s)|\le\min\{1,\delta/(2s^2)\}\). Regions outside these neighborhoods have \(|S|\) bounded below, so their weak contribution is also \(O(\delta)\). Summation proves the weak formula, including the cancellation criterion.

For the strong difference, on each root neighborhood \(|g_\delta|\) is even. The density for the absolute-value change of variables is \(1/|S'(t_j(s))|=1/|S'(t_j)|+O(|s|)\). Its constant part contributes exactly
\[
\frac{2}{|S'(t_j)|}
\bigl(r_j+\sqrt\delta-\sqrt{r_j^2+\delta}\bigr)
=\frac{2\sqrt\delta}{|S'(t_j)|}+O(\delta).
\]
The \(O(|s|)\) density remainder contributes at most \(O(\delta\log(1/\delta))\), while the other regions contribute \(O(\delta)\). This proves the strong formula.

For the double integrator, set \(A=\tau>0\) and \(B=T-\tau>0\). Exact integration of the control difference yields
\[
\Delta v_\delta=\sqrt{B^2+\delta}-\sqrt{A^2+\delta}-(B-A),
\]
\[
\Delta x_\delta=B\Delta v_\delta-\tfrac12\Bigl[
A\sqrt{A^2+\delta}+B\sqrt{B^2+\delta}-A^2-B^2
-\delta\bigl(\operatorname{arsinh}(A/\sqrt\delta)+\operatorname{arsinh}(B/\sqrt\delta)\bigr)
\Bigr].
\]
The velocity expression is \(\tfrac\delta2(B^{-1}-A^{-1})+O(\delta^2)\), and it is identically zero when \(A=B\). Using \(\operatorname{arsinh}(c/\sqrt\delta)=\tfrac12\log(1/\delta)+\log(2c)+O(\delta)\) for fixed \(c>0\), the position expression has exactly the asserted coefficient \(1/2\). Equivalently use the weak theorem with observation weight \(w(t)=T-t\), for which the coefficient of \(\delta\log(1/\delta)\) is \(1/2\). Since it is nonzero, the order is sharp.

## Verification
The standalone `verify.py` independently quadratures the smoothed and bang-bang double-integrator terminal increments, compares them with the closed formulas, checks exact center-switch velocity cancellation, and checks the predicted weak coefficient for curved switches with both signs of switching curvature. It uses `mpmath` with 65-decimal-digit arithmetic. Run `python verify.py` after installing the dependency in `requirements.txt`; expected output is `VERIFY_OK 37`. These computations are finite consistency checks, not the proof of the infinite-parameter asymptotics, which is above.

## Relationship to prior work
Wang, Chen, Wei, Lu, and Li introduce the normalized-\(L^2\) switching approximation \(S/\sqrt{S^2+\delta}\) and compare numerical shooting performance on an oscillator and orbital-transfer model; the work supplies the smoothing method, not the displayed local-coarea weak-error coefficient, strong-error constant, or fixed-switch double-integrator terminal-error classification. Heidrich's 2021 thesis previously includes the same algebraic sigmoid (with parameter \(\epsilon=\sqrt\delta\)) among generalized optimal-control regularizations, and discusses Hamiltonian convergence; the sigmoid itself is therefore explicitly **not** claimed as new. The present statement instead quantifies the sharp small-parameter response of arbitrary smooth weighted integral observations, as well as the terminal position and velocity distinction. Silva and Trélat (2010) analyze convergence of solutions under additional auxiliary control directions rather than the frozen algebraic-sign weighted error. The mesh-refinement study of Agamawi, Hager, and Rao addresses locating discontinuities in collocation, a different approximation mechanism. Classical asymptotic integration identities underlie the proof; equivalently formulated prior asymptotic expansions remain a genuine possibility.

## Limitations
The switching profile is held fixed; the theorem does not bound errors in a newly optimized bang-bang solution, a re-solved two-point boundary-value problem, or a control with degenerate or boundary switches. The logarithmic weak coefficient may cancel for selected observations, and the resulting \(O(\delta)\) term is not generally computed here. Statements concern exact real arithmetic, independent of discretization and finite-precision effects. Published treatments under alternate variables (for example, \(\epsilon=\sqrt\delta\)) might contain an equivalent asymptotic theorem; novelty is assessed against the compared sources only, not certified exhaustively.

## References
1. K. Wang, Z. Chen, Z. Wei, F. Lu, and J. Li, *A New Smoothing Technique for Bang-Bang Optimal Control Problems*, arXiv:2309.03069 (first submitted September 6, 2023), especially Sections 3–4, https://arxiv.org/html/2309.03069v2.
2. C. R. Heidrich, *Optimal Covariance Control on Singular Manifolds with Application to Aerospace Mission Design*, PhD thesis, University of Colorado Boulder, 2021, Chapter 2 (algebraic regularization in Table 2.1), https://hanspeterschaub.info/Papers/grads/CaseyHeidrich.pdf.
3. C. Silva and E. Trélat, *Smooth Regularization of Bang-Bang Optimal Control Problems*, IEEE Trans. Automatic Control 55 (2010), 2488–2499, https://doi.org/10.1109/TAC.2010.2047742.
4. Y. M. Agamawi, W. W. Hager, and A. V. Rao, *Mesh Refinement Method for Solving Bang-Bang Optimal Control Problems Using Direct Collocation*, arXiv:1905.11895 (2019), https://arxiv.org/abs/1905.11895.
