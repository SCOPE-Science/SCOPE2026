# Quadratic onset of the Hilbert-matrix Bloch-norm interior maximizer

## Finding

For each real \(1<\alpha<2\), let \(\mathcal B^\alpha\) be the analytic \(\alpha\)-Bloch space with norm
\[
\|f\|_{\mathcal B^\alpha}=|f(0)|+\sup_{|z|<1}(1-|z|^2)^\alpha|f'(z)|,
\]
and let \(\mathcal Hf(z)=\int_0^1 f(t)/(1-tz)\,dt\) be the Hilbert-matrix operator. Define
\[
P_\alpha(t)=\int_0^t(1-s^2)^{-\alpha}\,ds,\quad
C_\alpha=\int_0^1(1-t)(1-t^2)^{-\alpha}\,dt,
\]
\[
D_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{tP_\alpha(t)}{(1-rt)^2}\,dt\quad(0\le r<1),
\qquad D_\alpha(1)=\frac{\pi}{\sin(\pi(\alpha-1))}.
\]
Write \(\alpha=3/2+\varepsilon\), where \(\varepsilon\downarrow0\). For **every** maximizing radius \(r_\alpha\in(0,1)\) of \(D_\alpha\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{1-r_\alpha}{\varepsilon^2}=\frac12.}
\]
Moreover, the positive norm excess over the boundary-expression branch has the exact quadratic law
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\|\mathcal H\|_{\mathcal B^\alpha\to\mathcal B^\alpha}-C_\alpha-\pi/\sin(\pi(\alpha-1))}{\varepsilon^2}=\pi.}
\]
At the transition itself, the previously implicit boundary deficit admits the sharp linear formula
\[
D_{3/2}(1-h)=\pi-2\pi h+o(h)\qquad(h\downarrow0).
\]
The result quantifies the emergence of the interior maximizing radius immediately above \(\alpha=3/2\). No uniqueness of the maximizing radius for a fixed \(\alpha\) away from the transition is asserted.

## Assumptions and scope

All functions are complex-analytic on the open unit disk; \(1<\alpha<2\) is real. The operator norm and variational identity \(\|\mathcal H\|=C_\alpha+\max_{0\le r\le1}D_\alpha(r)\), as well as existence of an interior maximum for \(\alpha>3/2\), are from Cui--Lin--Lu--Ye [1, Theorem 1.1]. The new assertion is the **simultaneous** parameter-boundary limit \(\alpha\downarrow3/2\), not the already published fixed-parameter \(r\uparrow1\) asymptotic. The source's earliest publicly listed version is dated 2026-08-20 UTC [1].

## Proof

We give the local calculation and its uniformity, which are the steps not supplied by a fixed-parameter expansion. Put \(h=1-r\), \(\alpha_0=3/2\), and write \(B\) for Euler's beta function. Define
\[
d_\alpha=\frac{\sqrt\pi\,\Gamma(1-\alpha)}{2\Gamma(3/2-\alpha)},\qquad
E_\alpha(t)=\int_t^1(1-s)(1-s^2)^{-\alpha}\,ds.
\]
The exact decomposition of [1, Lemma 3.3], independently checked by differentiating both sides and evaluating at \(t=0\), reads
\[
P_\alpha(t)=\frac{(1-t^2)^{1-\alpha}}{2(\alpha-1)}+d_\alpha-E_\alpha(t).
\]
Consequently (all integrals below are over \(0<t<1\)),
\[
D_\alpha(r)=\frac{M_\alpha(r)}{2(\alpha-1)}+d_\alpha J_\alpha(r)-R_\alpha(r),
\]
where \(M_\alpha=(1-r^2)^\alpha\int t(1-t^2)^{1-\alpha}(1-rt)^{-2}\,dt\), \(J_\alpha=(1-r^2)^\alpha\int t(1-rt)^{-2}\,dt\), and \(R_\alpha=(1-r^2)^\alpha\int tE_\alpha(t)(1-rt)^{-2}\,dt\). These definitions agree with [1, equations (3.15)--(3.17)].

**The regular term.** The substitution \(y=(1-t)/(1-rt)\) gives the exact representation
\[
M_\alpha(r)=\int_0^1 m_{\alpha,r}(y)\,dy,\qquad
m_{\alpha,r}(y)=(1+r)^\alpha(1-y)y^{1-\alpha}
[2-(1+r)y]^{1-\alpha}(1-ry)^{2\alpha-3}.
\]
For \(\alpha\) in a fixed small compact interval to the right of \(3/2\), the derivative with respect to \(r\) is dominated uniformly for \(r\ge1/2\) by an integrable multiple of \(y^{-3/5}(1-y)^{-1/2}\) (choose the interval small enough, for example \([3/2,8/5]\)). Differentiation and dominated convergence therefore give, uniformly in that interval,
\[
M_\alpha(1-h)=2B(2-\alpha,\alpha)-K_\alpha h+o(h),
\]
with the corresponding derivative in \(h\) equal to \(-K_\alpha+o(1)\), where direct evaluation at \(r=1\) yields
\[
K_\alpha=\alpha B(2-\alpha,\alpha)+(5-3\alpha)B(3-\alpha,\alpha-1).
\]
In particular \(K_{3/2}=\pi\).

**The remainder term.** With \(v=1-t\), set
\[
E_\alpha(1-v)=v^{2-\alpha}e_\alpha(v),\qquad
e_\alpha(v)=\int_0^1 u^{1-\alpha}(2-vu)^{-\alpha}\,du.
\]
The functions \(e_\alpha\) and their first \(v\)-derivatives are bounded continuously and uniformly for \(0\le v\le1\) and \(\alpha\) in that compact interval. In particular \(e_\alpha(0)=2^{-\alpha}/(2-\alpha)\). Rescaling \(v=hs\) in \(R_\alpha(1-h)\), and applying dominated convergence with the integrable majorants \(s^{2-\alpha}/(1+s)^2\) and \(s^{2-\alpha}/(1+s)^3\), gives **both** the function and first-derivative expansions, uniformly in \(\alpha\):
\[
R_\alpha(1-h)=L_\alpha^{(R)}h+o(h),\qquad
\frac{d}{dh}R_\alpha(1-h)=L_\alpha^{(R)}+o(1),
\]
\[
L_\alpha^{(R)}=\frac{B(3-\alpha,\alpha-1)}{2-\alpha}.
\]
For clarity, the derivative limit follows directly by differentiating \((h(2-h))^\alpha\int_0^1 (1-v)E_\alpha(1-v)/[h+(1-h)v]^2\,dv\), then rescaling. The two resulting beta integrals combine by \(B(3-\alpha,\alpha)=(\alpha-1)B(3-\alpha,\alpha-1)/2\). Thus \(L_{3/2}^{(R)}=\pi\).

**The singular term.** Exact integration yields
\[
J_\alpha(1-h)=[h(2-h)]^\alpha\frac{(1-h)/h+\log h}{(1-h)^2}.
\]
Uniformly for \(\alpha\) in the same compact interval,
\[
J_\alpha(1-h)=2^\alpha h^{\alpha-1}(1+O(h|\log h|)),
\quad \frac{d}{dh}J_\alpha(1-h)=2^\alpha(\alpha-1)h^{\alpha-2}(1+O(h|\log h|)).
\]
Combining the three terms gives the **uniform two-parameter expansion**, with its differentiated form,
\[
D_\alpha(1-h)-D_\alpha(1)=2^\alpha d_\alpha h^{\alpha-1}(1+O(h|\log h|))-c_\alpha h+o(h),
\]
\[
\frac d{dh}D_\alpha(1-h)=2^\alpha d_\alpha(\alpha-1)h^{\alpha-2}(1+O(h|\log h|))-c_\alpha+o(1),
\]
where \(c_\alpha=K_\alpha/[2(\alpha-1)]+L_\alpha^{(R)}\to2\pi\). The \(o\)-remainders are uniform as \((\alpha,h)\to(3/2,0)\) from the right. The gamma quotient and its removable zero at \(\alpha=3/2\) give \(d_{3/2+\varepsilon}=\pi\varepsilon+O(\varepsilon^2)\). Setting \(\alpha=3/2\) in the undifferentiated formula proves \(D_{3/2}(1-h)=\pi-2\pi h+o(h)\).

**Localization and maximization.** At \(\alpha=3/2\), the exact source decomposition has \(d_{3/2}=0\), \(R_{3/2}(r)>0\) for \(0\le r<1\), and \(M_{3/2}(r)\le M_{3/2}(1)\). Thus \(D_{3/2}(r)<D_{3/2}(1)=\pi\) for all \(r<1\). Joint continuity in \((\alpha,r)\) on the relevant closed compact parameter-radius rectangle implies that **every** choice of global maximizer \(r_{3/2+\varepsilon}\) converges to \(1\). The source guarantees such maximizers lie in \((0,1)\) for \(\varepsilon>0\). Their interior stationarity in \(h_\varepsilon=1-r_{3/2+\varepsilon}\) therefore gives
\[
2^\alpha d_\alpha(\alpha-1)h_\varepsilon^{\alpha-2}=c_\alpha+o(1),
\qquad\frac{h_\varepsilon^{1/2-\varepsilon}}{\varepsilon}\longrightarrow\frac1{\sqrt2}.
\]
Taking logarithms and using \(\varepsilon|\log\varepsilon|\to0\) proves \(h_\varepsilon/\varepsilon^2\to1/2\). Finally the stationary equation gives \(c_\alpha h_\varepsilon=(\alpha-1)2^\alpha d_\alpha h_\varepsilon^{\alpha-1}+o(h_\varepsilon)\). Substitution into the uniform value expansion yields
\[
D_\alpha(r_\alpha)-D_\alpha(1)=(2-\alpha)2^\alpha d_\alpha h_\varepsilon^{\alpha-1}+o(\varepsilon^2)=\pi\varepsilon^2+o(\varepsilon^2).
\]
The source's exact operator-norm representation proves the claimed norm law. This completes the proof.

## Verification

The accompanying `CHECK.py` evaluates the **original one-dimensional integral**, not a fitted asymptotic formula. It uses a hypergeometric connection formula near the singular endpoint to avoid catastrophic cancellation and computes maximizing radii for a sequence of positive parameters. Its checks independently evaluate the critical beta coefficients and verify convergence of the scaled radius and norm excess toward \(1/2\) and \(\pi\). Execute with `python3 CHECK.py` after installing the dependencies in `requirements.txt`. Numeric checks are supplementary; the proof above is analytic. See `VERIFICATION.md` for the executed test details.

## Relationship to prior work

Cui--Lin--Lu--Ye [1, Theorem 1.1] established the exact norm variational formula, the transition at \(\alpha=3/2\), and existence of an interior maximizer above it. Their Proposition 3.7 gives \(D_\alpha(1-h)=D_\alpha(1)+2^\alpha d_\alpha h^{\alpha-1}+o(h^{\alpha-1})\) **for each fixed \(\alpha>3/2\)**. The present theorem concerns the optimizer and norm defect in the coupled limit \(\alpha\downarrow3/2\), where the coefficient \(d_\alpha\) itself vanishes. That fixed-parameter statement cannot be substituted directly into the coupled limit; the regular linear deficit must be calculated uniformly. Hu--Ye [2] and Ye--Zheng [3] studied estimates for related Hilbert-operator norms but did not provide this critical optimizer scaling in the inspected material.

## Limitations

This is a local result for \(\alpha\downarrow3/2\) from above. It does not classify the number of maximizing radii at arbitrary fixed \(\alpha>3/2\), prove a global closed formula for the norm in that range, or assert independent scientific validation. The originality claim is best-knowledge relative to the inspected primary sources and database comparisons; earlier unindexed asymptotics cannot be ruled out absolutely.

## References

[1] P. Cui, Z. Lin, Y. Lu, S. Ye, *Norms of the Hilbert Matrix Operator on Some Analytic Function Spaces*, arXiv:2609.27812, earliest publicly listed version 2026-08-20, version 3 dated 2026-10-21, especially Theorem 1.1, Lemma 3.3 and Proposition 3.7. https://arxiv.org/abs/2609.27812 ; accessible full text: https://borowiecki.dev/pdf/2609.27812 .

[2] H. Hu, S. Ye, *Norm of the Hilbert matrix operator between some spaces of analytic functions*, arXiv:2410.16598; subsequently Journal of Geometric Analysis (2025). https://arxiv.org/abs/2410.16598 .

[3] S. Ye, Q. Zheng, *Norm of the Hilbert matrix operator on logarithmically weighted Bloch and Hardy spaces*, arXiv:2510.23314, 2025. https://arxiv.org/abs/2510.23314 .
