# First sign failure at an elliptic absolute-monotonicity endpoint

## Finding

Write \(\mathcal K\) for the complete elliptic integral of the first kind and define, for real \(p>0\),
\[
F_p(z)=\frac{2}{\pi}\frac{\mathcal K(\sqrt z)}{p-\frac12\operatorname{Log}(1-z)}
       =\sum_{n\ge0}a_n(p)z^n
\]
near \(z=0\), with the principal logarithm and the standard analytic branch of the elliptic integral. Put \(p_0=\log 4\). For a positive perturbation \(\delta\), define the **first sign-failure degree**
\[
N(\delta)=\min\{n\ge3:a_n(p_0+\delta)>0\},
\]
whenever this set is nonempty.

**Theorem.** For all sufficiently small \(\delta>0\), the number \(N(\delta)\) exists, and
\[
\boxed{\lim_{\delta\downarrow0}\delta N(\delta)=\frac14.}
\]
The more precise, locally uniform transition law is: for every fixed real \(L>0\),
\[
\boxed{\sup_{|\lambda|\le L}\left|\pi n^2(\log n)^2
 a_n\!\left(p_0+\frac\lambda n\right)-(4\lambda-1)\right|\longrightarrow0.}
\]
Furthermore, for every sufficiently large integer \(n\), the function \(p\mapsto a_n(p)\) is strictly increasing on the entire fixed interval \([p_0-1/10,p_0+1/10]\) and has exactly one zero \(p_n\) there. These zeros satisfy
\[
\boxed{p_n=p_0+\frac1{4n}+o(n^{-1}).}
\]
The finite-degree roots and first sign-failure index are two descriptions of the same sharp transition; no claim is made concerning all zeros of \(a_n(p)\) outside the stated fixed neighborhood.

## Assumptions and scope

The parameter is real and positive. Every \(a_n(p)\) means the coefficient of the Taylor expansion at the origin, not a boundary asymptotic or a derivative at \(z=1\). The logarithm is the principal complex logarithm on \(\Omega=\mathbb C\setminus[1,\infty)\). The asserted root uniqueness is local in \(p\), and the limits are respectively \(n\to\infty\) and \(\delta\downarrow0\).

The originating endpoint theorem of Deng, Kou and Zhong gives \(a_n(p_0)<0\) for every \(n\ge3\). Its sign statement is used only to control the fixed finite set of low indices in the first-failure argument. The singular asymptotics and parameter derivatives required below are derived independently.

## Proof

**1. Continuation and singularities.** Write
\[
C_p(z)=p-\frac12\operatorname{Log}(1-z),\qquad
K(z)=\mathcal K(\sqrt z)=\int_0^{\pi/2}(1-z\sin^2\theta)^{-1/2}\,d\theta.
\]
The integral gives an analytic continuation of \(K\) to \(\Omega\). The only zero of \(C_p\) there is the simple zero \(z_p=1-e^{2p}\). In the interval \(J=[p_0-1/10,p_0+1/10]\), the poles \(z_p\) all satisfy \(|z_p|>1\), uniformly. The quotient \(F_p\), as well as its \(p\)-derivative, is thus analytic throughout the unit disk; its exterior pole gives at most a uniformly exponentially decaying coefficient contribution times a polynomial in \(n\).

For completeness the first singular expansion of \(K\) follows directly from its differential equation
\[
z(1-z)K''+(1-2z)K'-\frac14K=0.
\]
Putting \(t=1-z\) and \(C_0(t)=p_0-\frac12\operatorname{Log}t\), its regular-singular expansion is
\[
K(z)=C_0(t)+\frac t4(C_0(t)-1)
       +O\bigl(|t|^2(1+|\operatorname{Log}t|)\bigr)
\]
uniformly in closed sectors cut along the negative \(t\)-axis. Indeed, substituting \(K=C_0+t(AC_0+B)+\cdots\) into the equation gives \(A=1/4\), \(B=-1/4\); the Frobenius series supplies the stated remainder. The leading constant \(p_0=\log4\) is fixed by the classical elliptic integral asymptotic.

**2. Boundary jumps.** For \(u>0\), on the upper bank of the cut \(z=1+u+i0\), set
\[
R_p(u)=p-\frac12\log u,\quad
C_p^+(u)=R_p(u)+\frac{\pi i}{2},\quad
D_p(u)=R_p(u)^2+\frac{\pi^2}{4}.
\]
At \(p=p_0\) the quotient expansion becomes
\[
\frac{K(z)}{C_{p_0}(z)}
 =1+\frac{1-z}{4}-\frac{1-z}{4C_{p_0}(z)}
  +O\bigl(|1-z|^2\bigr).
\]
Consequently, as \(u\downarrow0\),
\[
\operatorname{Im}F_{p_0}(1+u+i0)
 =-\frac{u}{4D_{p_0}(u)}+O(u^2).
\]
The derivative in \(p\) is \(\partial_pF_p=-(2/\pi)K/C_p^2\). With \(p\in J\), the same singular expansion yields **uniformly in \(p\)**
\[
\operatorname{Im}\partial_pF_p(1+u+i0)
 =\frac1{D_p(u)}+O\!\left((\log(1/u))^{-3}\right)
  +O\!\left(u(\log(1/u))^{-1}\right).
\]
The constants are uniform for \(p\in J\). The first displayed jump carries an additional factor \(u\), whereas the derivative jump does not.

**3. Coefficient extraction.** Deform Cauchy's coefficient contour onto the cut and around the pole \(z_p\). For \(n\ge3\), the large-circle contribution vanishes; the pole contributes \(O_J(nq^n)\) for some \(q<1\). Thus both \(a_n(p_0)\) and \(\partial_pa_n(p)\) equal, up to exponentially small terms, the cut integrals of their upper-bank imaginary parts against \((1+u)^{-n-1}du/\pi\). The coefficient sign in this formula is fixed, for instance, by the standard positive coefficients of \(\operatorname{Log}(1/(1-z))\).

For \(j=0,1\), uniformly in \(p\in J\), direct substitution \(u=v/n\) gives
\[
\int_0^\infty\frac{u^j(1+u)^{-n-1}}{D_p(u)}\,du
\sim \frac{4j!}{n^{j+1}(\log n)^2}.
\]
To justify this limit, split at \(u=n^{-1/2}\). The upper portion has exponentially small mass, while in the lower portion \(D_p(v/n)/(\log n)^2\to1/4\) for fixed \(v>0\), with a uniform integrable majorant proportional to \(v^je^{-v/2}\). Contributions from \(u\) bounded away from zero decay exponentially; hence the local jump expansions suffice.

The two boundary jumps now give
\[
\boxed{\pi n^2(\log n)^2a_n(p_0)\longrightarrow-1,}
\]
and
\[
\boxed{\sup_{p\in J}\left|\frac{\pi n(\log n)^2}{4}\,
\partial_pa_n(p)-1\right|\longrightarrow0.}
\]
These follow analytically from the original quotient; the first is a fixed-parameter comparison fact and is **not** the novelty claimed here.

**4. Uniform transition and first failure.** By the fundamental theorem of calculus, for any fixed \(L>0\) and \(|\lambda|\le L\),
\[
a_n(p_0+\lambda/n)=a_n(p_0)+\frac\lambda n
\int_0^1\partial_pa_n(p_0+t\lambda/n)\,dt.
\]
The two uniform limits in Step 3 prove the announced boundary-layer formula \(4\lambda-1\). In particular \(\partial_pa_n>0\) throughout \(J\) for all sufficiently large \(n\). Since the endpoint coefficient is negative while its increment over any fixed positive parameter shift is eventually positive, there is exactly one local root. At that root the mean-value theorem and Step 3 give \(n(p_n-p_0)\to1/4\).

Finally let \(\varepsilon\in(0,1/4)\). The uniform transition law shows that for all sufficiently large \(n\), and all small \(\delta>0\) satisfying \(n\delta\le1/4-\varepsilon\), one has \(a_n(p_0+\delta)<0\). The finitely many indices \(3\le n<n_0\) remain negative by the published endpoint sign theorem and continuity. Conversely \(n_+(\delta)=\lceil(1/4+\varepsilon)/\delta\rceil\) satisfies \(a_{n_+(\delta)}(p_0+\delta)>0\) when \(\delta\) is sufficiently small. Therefore
\[
\frac14-\varepsilon\le\delta N(\delta)
\le\frac14+\varepsilon+\delta,
\]
which proves the first-sign-failure law.

## Verification

The standalone script `verify_elliptic_transition.py` uses the exact Taylor coefficient recurrence
\[
pa_0=1,\qquad
pa_n=\left(\frac{(1/2)_n}{n!}\right)^2
      -\sum_{j=1}^n\frac{a_{n-j}}{2j}
\quad(n\ge1),
\]
together with its differentiated version, in arbitrary-precision decimal arithmetic. It checks closed-form coefficients through degree three, derivative signs, and zero locations in four finite degrees. Typical values of \(n(p_n-p_0)\) are \(0.314208\ldots\), \(0.309606\ldots\), \(0.305589\ldots\), and \(0.302033\ldots\) for degrees \(30,60,120,240\), respectively. Their slow approach is compatible with logarithmic asymptotics. These finite checks are supplementary: the uniform infinite-degree theorem is proved by the analytic cut argument, not extrapolated from the listed examples.

## Relationship to prior work

Deng, Kou and Zhong (2026, arXiv:2609.32366, Theorem 1.1 and Sections 2–3) settle the endpoint coefficient-sign conjectures at exactly \(p=\log4\), using a meromorphic-continuation and moment representation. Their published results, as materially inspected, do not state the parameter-dependent uniform derivative, local crossing degree, or first-positive-index limit proved here. Earlier work of Tian and Yang (2022, Results in Mathematics 77:109) studies necessary and sufficient parameter ranges for absolute monotonicity of derivatives of the **same quotient**. Those global conditions do not identify the first coefficient that changes sign when \(p\) crosses \(\log4\).

A fixed-parameter asymptotic of the endpoint Taylor coefficients is already available and is explicitly treated here as prior, not as an additional original finding. The present mathematical question is the **joint degree–parameter limit**, whose answer requires a uniform coefficient-derivative estimate and yields the sharp sign-loss scale.

## Limitations

The theorem is asymptotic and supplies no exact root formula at a specified finite degree. Monotonicity and root uniqueness are asserted only for sufficiently large degrees on the stated fixed parameter interval. It does not identify every sign change globally in \(p\), and the boundary-layer estimate is uniform only for bounded \(\lambda\). The underlying 2022 paper was available here only as a publisher preview; an equivalent unpublished or unindexed parameter-dependent result remains a literature risk.

## References

1. Q. Deng, Y. Kou, and F. Zhong, *Endpoint Absolute Monotonicity for the Complete Elliptic Integral of the First Kind*, arXiv:2609.32366 (first public September 26, 2026), especially Theorem 1.1 and Sections 2–3. https://arxiv.org/abs/2609.32366
2. J.-F. Tian and Z.-H. Yang, *Several Absolutely Monotonic Functions Related to the Complete Elliptic Integral of the First Kind*, Results in Mathematics **77** (2022), article 109, DOI: 10.1007/s00025-022-01641-4.
3. Z.-H. Yang and J.-F. Tian, *Absolutely Monotonic Functions Involving the Complete Elliptic Integrals of the First Kind with Applications*, Journal of Mathematical Inequalities **15** (2021), 1299–1310, DOI: 10.7153/jmi-2021-15-87 (distinct exponential family).
