# A focus–double-node–node trichotomy for negative-bias reset latency

## Finding
Consider the generalized max-plus map introduced in [1,2],
\[
F_{\varepsilon,T,D}(x,y)=\bigl(y+\max(0,Tx),-\varepsilon-\max(0,Dx)\bigr).
\]
Fix \(0<D<1\), \(0<T<1+D\), a seed \((u,v)\) with \(u>0\) and \(v\ge0\), and a small **negative** input \(B=-\varepsilon\), \(\varepsilon>0\). Define the first-switching time
\[
\tau_\varepsilon=\min\{n\ge1:X_n\le0\},\quad (X_n,Y_n)=F_{\varepsilon,T,D}^{n}(u,v).
\]
The time is finite for every \(\varepsilon>0\), and the orbit reaches the absorbing fixed point \((-\varepsilon,-\varepsilon)\) for the first time at the exact time \(\tau_\varepsilon+2\).

The sharp small-bias trichotomy is
\[
\boxed{
\begin{aligned}
T^2<4D &: \quad \tau_\varepsilon=O(1),\\
T^2=4D &: \quad \tau_\varepsilon=\frac{\log(1/\varepsilon)+\log\log(1/\varepsilon)}{-\log\sqrt D}+O(1),\\
T^2>4D &: \quad \tau_\varepsilon=\frac{\log(1/\varepsilon)}{-\log\lambda_+}+O(1),
\end{aligned}}
\]
where \(\lambda_+=(T+\sqrt{T^2-4D})/2\) in the distinct-real-root case. All constants implicit in the \(O(1)\) notation may depend on the fixed parameters and seed, but **not** on \(\varepsilon\).

In the two real-root regimes there is also an exact, finite-index threshold sequence: the first contact is determined by the first index \(n\ge2\) for which \(\varepsilon\ge\varepsilon_n\), with \(\varepsilon_n=U_n/h_n\), where \(U_n,h_n\) are the explicit sequences below. The thresholds are eventually strictly decreasing; they are not asserted monotone at the first few indices.

## Assumptions and scope
The variables \((x,y)\) range over \(\mathbb R^2\), and iteration is in discrete time. The parameters satisfy \(\varepsilon>0\), \(0<D<1\), and \(0<T<1+D\). The seed \((u,v)\) is independent of \(\varepsilon\), with \(u>0\), \(v\ge0\); varying the initial condition proportionally to \(\varepsilon\) does not fall under the asserted asymptotics. The switch is defined with equality included at \(x=0\). The complex-root, repeated-root, and distinct-positive-root cases refer to the positive-branch characteristic equation \(\lambda^2-T\lambda+D=0\).

## Proof
**1. The scalar affine recurrence and exact reset.** Prior to the first \(X_n\le0\), both max operators use their positive branches, giving
\[
X_0=u,\quad X_1=Tu+v,\quad X_{n+2}=TX_{n+1}-DX_n-\varepsilon.
\]
Define \(U_0=u\), \(U_1=Tu+v\), \(U_{n+2}=TU_{n+1}-DU_n\) and \(h_0=h_1=0\), \(h_{n+2}=Th_{n+1}-Dh_n+1\). Then, **up to and including the first contact**, \(X_n=U_n-\varepsilon h_n\). At that contact, \(Y_{\tau_\varepsilon}=-\varepsilon-DX_{\tau_\varepsilon-1}<0\). Since \(X_{\tau_\varepsilon}\le0\), the next two states are \((Y_{\tau_\varepsilon},-\varepsilon)\) and \((-\varepsilon,-\varepsilon)\). The first has negative first coordinate, so the latter is the first occurrence of the fixed point.

**2. Existence of a first contact for every negative bias.** Put \(\Delta=1-T+D>0\). The affine positive-branch recurrence has equilibrium \(-\varepsilon/\Delta<0\). All the characteristic roots have modulus strictly below one: if complex their modulus is \(\sqrt D<1\); if real they are positive, have product \(D<1\), and satisfy \(\lambda_+<1\) because \(T<1+D\). Thus the indefinite positive-branch solution tends to \(-\varepsilon/\Delta\). An orbit that never switches would follow that solution forever, a contradiction. This proves finite contact without an a priori bound uniform in the bias.

**3. Oscillatory branch.** If \(T^2<4D\), set \(r=\sqrt D<1\) and \(\theta=\arccos(T/(2r))\in(0,\pi/2)\). The unforced solution \(U_n\) is a nonzero real sinusoid times \(r^n\). Some integer \(N\) has \(U_N<0\): for irrational \(\theta/(2\pi)\) use density of rotations; for rational rotation its finite orbit has zero mean and is not identically zero. The hypothetical affine solution at that fixed index is \(U_N-\varepsilon h_N\), which remains negative for all sufficiently small \(\varepsilon\). If the actual orbit has not already switched, it agrees with that hypothetical solution. Therefore \(\tau_\varepsilon\le N\) for small bias, proving \(O(1)\). The conclusion does not claim a universal bound independent of \(T,D,u,v\).

**4. Exact thresholds for positive real roots.** Suppose \(T^2\ge4D\). In the distinct-root case write \(0<\lambda_-<\lambda_+<1\) and \(d=\lambda_+-\lambda_-\). The unforced solution is
\[
U_n=\frac{(\lambda_+u+v)\lambda_+^n-(\lambda_-u+v)\lambda_-^n}{d},
\]
and define
\[
C_n=\frac{(1-\lambda_-)\lambda_+^n-(1-\lambda_+)\lambda_-^n}{d},\qquad h_n=\frac{1-C_n}{\Delta}.
\]
At the double root \(r=\sqrt D=T/2\in(0,1)\), the corresponding formulas are
\[
U_n=\bigl(u+n(u+v/r)\bigr)r^n,\quad
C_n=\bigl(1+n(1/r-1)\bigr)r^n,\quad h_n=\frac{1-C_n}{\Delta}.
\]
These identities follow either by substituting into the recurrences and their initial conditions or by taking the repeated-root limit. In both cases \(U_n>0\) for all \(n\), and \(h_n=\sum_{j=0}^{n-2}g_j>0\) for \(n\ge2\), with impulse responses \(g_j=(\lambda_+^{j+1}-\lambda_-^{j+1})/d>0\), or \(g_j=(j+1)r^j>0\) at the double root. Thus \(h_n\nearrow1/\Delta\). The actual first contact is exactly the **earliest** \(n\ge2\) satisfying
\[
\varepsilon\ge\varepsilon_n:=\frac{U_n}{h_n}=\frac{\Delta U_n}{1-C_n}.
\]
The formula uses exact equality at contact, not an asymptotic replacement.

**5. Quantitative near-border asymptotics.** With distinct roots,
\[
\varepsilon_n=\frac{\Delta(\lambda_+u+v)}{\lambda_+-\lambda_-}\,\lambda_+^n(1+o(1)).
\]
At the double root,
\[
\varepsilon_n=\Delta(u+v/r)\,n r^n(1+o(1)).
\]
The leading constants are strictly positive. Consequently \(\varepsilon_{n+1}/\varepsilon_n\to\lambda_+\) or \(r\), respectively, both strictly below one. For all sufficiently large \(n\) the thresholds decrease strictly; every finite earlier threshold is positive, so for sufficiently small \(\varepsilon\) the first crossing is controlled by this decreasing tail. Solving \(\varepsilon\asymp\lambda_+^n\) gives the overdamped estimate, whereas solving \(\varepsilon\asymp n r^n\) gives the extra \(\log\log(1/\varepsilon)\) term with coefficient \(1/(-\log r)\). The error in the integer crossing index remains bounded because neighboring thresholds have an asymptotically fixed ratio below one. This finishes all three cases.

## Verification
The companion `verify.py` is a standalone Python 3 script using `fractions.Fraction`; it needs no external packages. It checks 36 exact-rational trajectories in all three spectral regimes, reconstructs the scalar recurrence and exact reset, checks first-contact inequalities, and verifies the closed forms and eventual threshold ordering in two rational real-root examples. It reports `PASS` on success. Finite arithmetic checks are additional evidence, not a substitute for the universal arguments in the proof.

For example, with \((u,v)=(1,1)\) and \(\varepsilon=10^{-8}\), first-switch times are \(5\), \(32\), and \(80\), for \((T,D)=(9/10,3/10)\), \((1,1/4)\), and \((11/10,6/25)\), respectively.

## Relationship to prior work
Yamazaki and Ohmori [1, Eq. (11)] first proposed this two-parameter family publicly on 5 December 2023. Ohmori and Yamazaki [2, §§2–3] give its branch matrices and qualitative border-collision behavior. In particular [2, §3.2] describes finite-time reset for negative bias in the *spiral* regime and [2, §2] credits the at-most-four-step result in the special \(T=0\) model. Those reset facts are prior work and not the asserted novelty here. [2] does not give the fixed-seed, vanishing-negative-bias trichotomy across focus, repeated stable node, and distinct stable node. Its parameter rescaling of \(B\) does not determine our fixed-seed latency: under that rescaling the seed diverges.

Yamazaki and Ohmori [1] derive a logarithmic *phase-bottleneck* delay near a saddle-node of a nonzero-input oscillatory system. Its object, parameter and mechanism differ from the first passage to the inactive branch here; in particular it does not yield the repeated-root \(\log\log\) correction. Simpson [3] places the same branch matrices within the zero-determinant border-collision normal form. Its negative-parameter discussion concentrates on \(\tau_L<-1\), whereas the present subfamily has \(\tau_L=0\), and no first-switching asymptotic at fixed seeds is given. The published homogeneous-border classification [4] gives the exact \(B=0\) persistence cone and extinction times. Our \(B<0\) result is not a corollary of those formulas: points in that cone persist forever at zero input but have diverging yet finite reset times for any negative input. All comparisons are about **statements and implications**, not merely coincident maps.

## Limitations
No uniform constants in the seed or parameters are asserted. No asymptotic for seeds that themselves depend on \(\varepsilon\), for nonstable spectral parameters, or for arbitrary initial quadrants is claimed. The time is first crossing of the switching half-plane, not a mixing or phase-locking time. The literature search and direct inspections support the scoped originality judgment but cannot exclude all unindexed independent derivations. Independent validation has not been performed.

## References
1. Yoshihiro Yamazaki and Shousuke Ohmori, *Ultradiscretization in discrete limit cycles of tropically discretized and max-plus Sel'kov models*, arXiv:2312.13292v1, first public 5 December 2023, Eq. (11). https://arxiv.org/abs/2312.13292
2. Shousuke Ohmori and Yoshihiro Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230v1, first public 9 February 2024; *Journal of Mathematical Physics* 65 (2024), 082705. https://arxiv.org/abs/2402.06230
3. David J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1, first public 8 August 2024. https://arxiv.org/abs/2408.04790
4. *Sharp extinction and persistence at the homogeneous max-plus border collision*, public mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-extinction-and-persistence-at-the-homogeneous-max-plus-bor--a2b1d9a86864
