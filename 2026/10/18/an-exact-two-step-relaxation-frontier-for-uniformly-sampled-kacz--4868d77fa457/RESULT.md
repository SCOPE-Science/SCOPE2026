# An exact two-step relaxation frontier for uniformly sampled Kaczmarz

## Finding

Consider two independent linear equations in \(\mathbb R^2\) whose normalized row directions are \(u=(c,s)^{\mathsf T}\) and \(v=(1,0)^{\mathsf T}\), with \(c,s>0\) and \(c^2+s^2=1\). Give their actual rows squared norms \(1\) and \(1-\delta^2\), where \(0<\delta<1\). Select a row independently with probability \(1/2\) at each iteration. Compare ordinary Kaczmarz with relaxation \(1\) on both rows against volume-ratio relaxed uniform Kaczmarz, whose relaxation is \(1\) for row \(u\) and \(1+\delta\) for row \(v\).

For a deterministic initial error \(e\), write \(E_k^{\mathrm{uni}}(e)\) and \(E_k^{\mathrm{rel}}(e)\) for expected squared Euclidean errors after \(k\) iterations of these two methods, each started from \(e\). Their one-step difference is always nonnegative:
\[
E_1^{\mathrm{rel}}(e)-E_1^{\mathrm{uni}}(e)=\frac{\delta^2}{2}(v^{\mathsf T}e)^2.
\]

Nevertheless, there is a **sharp two-step reversal frontier**. The equation
\[
\delta_*^4+s^2\delta_*(\delta_*+2)=1
\]
has exactly one root \(\delta_*\in(0,1)\). If \(0<\delta<\delta_*\), some deterministic initial errors have \(E_2^{\mathrm{rel}}(e)<E_2^{\mathrm{uni}}(e)\), while other errors have the reverse strict inequality. If \(\delta=\delta_*\), then \(E_2^{\mathrm{rel}}(e)\ge E_2^{\mathrm{uni}}(e)\) for every \(e\), with equality on one nonzero line. If \(\delta_*<\delta<1\), the relaxed method has strictly larger expected two-step squared error for every nonzero \(e\).

In the reversal regime the best unit-norm two-step advantage equals \(-\lambda_{\min}(D_2)\), where the explicitly known symmetric matrix \(D_2\) is given in the proof. As \(\delta\downarrow0\), this maximum advantage is \(cs\delta/4+O(\delta^2)\), even though the one-step disadvantage is only of order \(\delta^2\).

## Assumptions and scope

Fix real \(c,s,\delta\) satisfying \(c>0\), \(s>0\), \(c^2+s^2=1\) and \(0<\delta<1\). Let
\[
A=\begin{pmatrix}c&s\\ \sqrt{1-\delta^2}&0\end{pmatrix},\qquad b=0.
\]
This matrix is invertible. All computations are in exact real arithmetic. Fresh row choices are independent and uniformly distributed over the two rows, with replacement. Both methods begin at the same arbitrary deterministic \(e\in\mathbb R^2\). The two-step horizon means two individual selected-row updates, not two sweeps through all rows.

The relaxation applied to an arbitrarily scaled row \(a\) is \(\omega=1+\sqrt{1-\|a\|_2^2/v_{\max}}\), with \(v_{\max}=\max_i\|a_i\|_2^2\). For these rows it is exactly \(1\) or \(1+\delta\). This is the singleton-block instance of the volume-ratio rule from Entezari, Banerjee and Kalantari, arXiv:2610.12346v1, Equation (5). The comparison always uses the same fixed matrix \(A\) in both algorithms; the ordinary method does **not** change the second row's norm.

## Proof

Let \(P_u=uu^{\mathsf T}\) and \(P_v=vv^{\mathsf T}\). The error propagator when row \(u\) is drawn is
\[
U=I-P_u=\begin{pmatrix}s^2&-cs\\-cs&c^2\end{pmatrix}.
\]
For the other row it is \(V_\delta=I-(1+\delta)P_v=\operatorname{diag}(-\delta,1)\) in the relaxed method and \(V_0=I-P_v=\operatorname{diag}(0,1)\) in the ordinary method. Both choices of row have probability \(1/2\); the sampling distribution is held fixed across the methods.

For either symmetric pair \((U,V)\), the one-step expected squared-error matrix is \((U^2+V^2)/2\). Because \(V_\delta^2-V_0^2=\delta^2P_v\), their difference is \(\delta^2P_v/2\), proving the one-step assertion.

For two independent updates with the second propagator multiplying on the left, the squared-error matrix is
\[
M_2(U,V)=\frac14\sum_{B\in\{U,V\}}\sum_{C\in\{U,V\}}(CB)^{\mathsf T}(CB).
\]
Direct multiplication, using \(c^2+s^2=1\), gives the exact two-step difference
\[
D_2:=M_2(U,V_\delta)-M_2(U,V_0)
=\frac14\begin{pmatrix}
\delta^2\bigl[s^2(1+s^2)+\delta^2\bigr]&cs\delta(1-s^2\delta)\\
cs\delta(1-s^2\delta)&c^2s^2\delta^2
\end{pmatrix}.
\]
Thus \(E_2^{\mathrm{rel}}(e)-E_2^{\mathrm{uni}}(e)=e^{\mathsf T}D_2e\). Its trace and determinant simplify to
\[
\operatorname{tr}D_2=\frac{\delta^2(2s^2+\delta^2)}4>0,
\qquad
\det D_2=-\frac{c^2s^2\delta^2}{16}\bigl[1-s^2\delta(\delta+2)-\delta^4\bigr].
\]
The scalar function \(h(t)=t^4+s^2t(t+2)\) strictly increases for positive \(t\), with \(h(0)=0\) and \(h(1)=1+3s^2>1\). Hence its unit-level set is a unique \(\delta_*\in(0,1)\). Below that root \(\det D_2<0\), so the real symmetric \(D_2\) has one negative and one positive eigenvalue. At the root its determinant is zero and its trace positive, so it is positive semidefinite with a one-dimensional kernel. Above the root its determinant and trace are both positive, so it is positive definite. Every existence, strictness, and equality statement follows by selecting the corresponding eigenvector.

The best two-step advantage for a unit vector is \(-\lambda_{\min}(D_2)\) by the Rayleigh principle. The diagonal entries of \(D_2\) are \(O(\delta^2)\), whereas the off-diagonal entry is \(cs\delta/4+O(\delta^2)\). Its smallest eigenvalue is therefore \(-cs\delta/4+O(\delta^2)\), proving the small-relaxation asymptotic.

An exact rational witness is obtained at \(c=3/5\), \(s=4/5\), \(\delta=1/4\), with rows \((3/5,4/5)\) and \((\sqrt{15}/4,0)\) and initial error \(e=(-1,1)^{\mathsf T}\). Directly averaging the two choices at one step and four ordered choices at two steps gives
\[
\begin{aligned}
E_1^{\mathrm{uni}}(e)&=37/25,& E_1^{\mathrm{rel}}(e)&=1209/800,\\
E_2^{\mathrm{uni}}(e)&=629/625,& E_2^{\mathrm{rel}}(e)&=125053/128000.
\end{aligned}
\]
The relaxed method is worse after one step, but its exact two-step advantage is \(18831/640000>0\). All fractions arise from rational projectors despite the square root in the row's unnormalized coefficient.

## Verification

Run `python3 verify.py` using Python's standard library; it needs no downloaded data or optional dependencies. The program forms all ordered two-step update products with exact rational arithmetic, checks the displayed matrix, determinant, trace and first-step identities on 1,729 rational Pythagorean-angle/relaxation instances, and verifies the exact rational witness. Its expected terminal marker begins with `VERIFY_OK exact_two_step_matrix_cases=1729`. The symbolic identities and sign argument in the proof, not finite tests, establish the universal claim.

## Relationship to prior work

Entezari, Banerjee and Kalantari (2026) introduce exactly the volume-ratio relaxation used here, derive its conditional one-step expected-error operator (Theorem 2), and compare relaxed and ordinary uniform sampling numerically (Sections 5.1–5.2). Their paper does not state this two-step Loewner-sign phase boundary or the smallest-dimension mechanism by which a one-step disadvantage becomes a two-step advantage.

Wang, Agaskar and Lu (2015) derive exact covariance-lifting formulas for standard randomized Kaczmarz, including inconsistent systems; these use the unrelaxed row projector rather than the volume-ratio relaxation. Marshall and Mickelin (2022) optimize time-indexed learning-rate bounds in a noisy setting, a different optimization criterion and sampling model. Classical results for diagonally relaxed orthogonal projections, including Censor, Elfving, Herman and Nikazad (2008), provide wider convergence frameworks; the present contribution is not a new general theory of relaxation but the explicit sharp finite-horizon frontier for the specified rule and minimal noncommuting two-row case.

## Limitations

This is a two-dimensional, two-equation, two-update exact-arithmetic classification for singleton blocks. The advantage holds only for some initial errors below the threshold; it is **not** a uniform worst-case improvement, and the result does not assert improved asymptotic convergence or wall-clock performance. The rule depends on the rows' norms, so rescaling an equation changes the relaxation even though it does not change the underlying hyperplane. The proof does not extend its threshold to larger random block systems, noisy or inconsistent equations, dependent sampling, or finite precision. Broader literature could contain an equivalent specialized formula; an independent originality audit remains outstanding.

## References

1. A. Entezari, A. Banerjee and L. Kalantari, *Volume Sampling and Spectral Equalization in Randomized Alternating Projections*, arXiv:2610.12346v1 (first public 2026-10-08), https://arxiv.org/abs/2610.12346 .
2. C. Wang, A. Agaskar and Y. M. Lu, *Randomized Kaczmarz Algorithm for Inconsistent Linear Systems: An Exact MSE Analysis*, arXiv:1502.00190v1 (2015), https://arxiv.org/abs/1502.00190 .
3. N. F. Marshall and O. Mickelin, *An Optimal Scheduled Learning Rate for a Randomized Kaczmarz Algorithm*, arXiv:2202.12224v4 (2022), https://arxiv.org/abs/2202.12224 .
4. Y. Censor, T. Elfving, G. T. Herman and T. Nikazad, *On Diagonally Relaxed Orthogonal Projection Methods*, SIAM J. Sci. Comput. 30 (2008), 473–504, https://doi.org/10.1137/050639399 .
5. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP (2014), https://doi.org/10.1109/GlobalSIP.2014.7032145 .
