# Sharp antithetic pairing and the \(\varphi+\sqrt{\varphi}\) stability cutoff in two-component stochastic extragradient

## Finding

Consider the real two-player bilinear saddle problem with two components \(f_1(x,y)=axy\) and \(f_2(x,y)=bxy\), where \(0<a<b\), and the average saddle operator \(F(z)=(a+b)Jz/2\), with \(z=(x,y)^\mathsf T\) and \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). Write \(F_i(z)=a_i Jz\), where \(a_1=a\), \(a_2=b\). Each iteration of paired stochastic extragradient is
\[
 w_k=z_k-\eta F_{I_k}(z_k),\qquad z_{k+1}=z_k-\eta F_{K_k}(w_k),\qquad \eta>0.
\]
Here \((I_k,K_k)\) are independent across iterations, but may be coupled *within* an iteration. Both indices have uniform marginals on \(\{1,2\}\). Every such coupling is specified by \(\theta\in[-1,1]\):
\[
 \Pr(I_k=1,K_k=1)=\Pr(I_k=2,K_k=2)=\frac{1+\theta}{4},\quad
 \Pr(I_k=1,K_k=2)=\Pr(I_k=2,K_k=1)=\frac{1-\theta}{4}.
\]
Thus \(\theta=1,0,-1\) are respectively identical-sample, independent-sample, and antithetic-sample choices. All three use exactly two component-operator evaluations per iteration. Let \(q_\theta\) be the exact mean-square multiplier, so that, for every deterministic \(z_0\),
\[
 \mathbb E\|z_k\|_2^2=q_\theta^k\|z_0\|_2^2\qquad(k=0,1,2,\ldots).
\]
Writing \(m_2=(a^2+b^2)/2\), \(m_4=(a^4+b^4)/2\), the three endpoint or midpoint multipliers are
\[
 \begin{aligned}
 q_+&=1-m_2\eta^2+m_4\eta^4,\\
 q_0&=1-ab\eta^2+m_2^2\eta^4,\\
 q_-&=1+(m_2-2ab)\eta^2+a^2b^2\eta^4,
 \end{aligned}
 \qquad q_\theta=\frac{1+\theta}{2}q_++\frac{1-\theta}{2}q_-.
\]
For unequal components the *unique* optimal coupling for any fixed step size is identical-sample when \(\eta^2<2/(a+b)^2\) and antithetic when \(\eta^2>2/(a+b)^2\), with all couplings tied at equality. Here optimal means minimizing expected squared distance after every positive number of iterations, for each nonzero deterministic starting point.

Set \(r=b/a>1\), \(\varphi=(1+\sqrt5)/2\), and \(r_\star=\varphi+\sqrt\varphi=2.890053638\ldots\). There exists an open step-size interval on which antithetic pairing is strictly mean-square contractive while *both* same-sample and independent-sample pairing are strictly mean-square expansive **if and only if** \(1<r<r_\star\). The interval is exactly
\[
 \boxed{\ \frac{4r}{(1+r^2)^2}<(a\eta)^2<\frac{4r-1-r^2}{2r^2}\ }.
\]
For example, for \((a,b,\eta)=(1,2,3/5)\),
\[
 \boxed{q_+=\frac{751}{625}>q_0=\frac{109}{100}>1>q_-=\frac{1223}{1250}}.
\]
Hence this antithetic pairing converges to the saddle in mean square geometrically while both standard choices have geometrically diverging expected squared errors. The interval and ratio cutoff are sharp within this entire two-component, uniform-marginal, fixed-equal-stepsize family.

## Assumptions and scope

The state space is \(\mathbb R^2\). The two bilinear component coefficients satisfy \(0<a<b\); the method uses the same fixed \(\eta>0\) in extrapolation and correction. Sampling pairs are iid across iterations, and each within-iteration index has probability \(1/2\) of either component. Mean-square convergence denotes \(\mathbb E\|z_k\|_2^2\to0\) for every deterministic initial state; at multiplier exactly one, nonzero initial mean-square error remains constant and is not counted as convergence. The saddle is uniquely \(z_\star=0\), because \((a+b)/2>0\).

The special constant \(r_\star\) is a *heterogeneity cutoff for this sampling comparison*, not the step-size constant of any unrelated golden-ratio algorithm.

## Proof

**1. One-step identity and moments.** Since \(J^2=-I\) and \(J^\mathsf TJ=I\), for a pair of component coefficients \(u,v\in\{a,b\}\),
\[
 z_{k+1}=\bigl((1-\eta^2uv)I-\eta vJ\bigr)z_k,
 \quad\|z_{k+1}\|_2^2=\bigl((1-\eta^2uv)^2+\eta^2v^2\bigr)\|z_k\|_2^2.
\]
The cross term vanishes because \(J\) is skew-symmetric. Averaging the four pair possibilities with the displayed coupling probabilities yields \(q_+\), \(q_-\), their convex combination \(q_\theta\), and \(q_0=(q_++q_-)/2\). Independence *between iterations* and conditional independence from the previous state imply the exact \(k\)-step identity by induction. No pathwise or almost-sure statement is inferred from it.

**2. Optimal within-iteration coupling.** Direct subtraction gives
\[
 q_+-q_-=(a-b)^2\eta^2\left(\frac{(a+b)^2\eta^2}{2}-1\right).
\]
Since \(a\ne b\), its unique positive crossing is \(\eta^2=2/(a+b)^2\). The affine dependence on \(\theta\) proves global endpoint optimality over *all* joint laws with the fixed uniform marginals. For \(k\ge1\), minimizing \(q_\theta^k\) is equivalent to minimizing \(q_\theta\) because \(q_\theta\ge0\).

**3. All three sharp mean-square step thresholds.** Define \(t=(a\eta)^2>0\). The conditions \(q_+,q_0,q_-<1\) are respectively
\[
 \begin{array}{rcl}
 0<t<t_+,&\quad&t_+=\displaystyle\frac{1+r^2}{1+r^4},\\[2mm]
 0<t<t_0,&&t_0=\displaystyle\frac{4r}{(1+r^2)^2},\\[2mm]
 0<t<t_-,&&t_-=\displaystyle\frac{4r-1-r^2}{2r^2}.
 \end{array}
\]
If \(t_-\le0\), the antithetic scheme is not mean-square contractive at any positive step. The formulas follow by dividing \(q-1\), an exact quadratic in \(t\), by positive \(t\).

**4. Sharp heterogeneity cutoff.** Put \(P(r)=r^4-2r^3-2r^2-2r+1\). Exact subtraction factors as
\[
 t_--t_0=-\frac{(r-1)^2P(r)}{2r^2(1+r^2)^2},\qquad
 t_+-t_0=\frac{(r-1)^2P(r)}{(1+r^2)^2(1+r^4)}.
\]
For \(r>1\), all denominators are positive. With \(u=r+r^{-1}>2\),
\[
 \frac{P(r)}{r^2}=u^2-2u-4
 =(u-1-\sqrt5)(u-1+\sqrt5).
\]
The second factor is positive, so \(P(r)<0\) precisely when \(u<1+\sqrt5\), equivalently \(1<r<\varphi+\sqrt\varphi\). Thus exactly in this ratio range one has \(t_- >t_0>t_+>0\). Choosing \(t\) strictly between \(t_0\) and \(t_-\) then gives \(q_-<1<q_0<q_+\). For \(r=r_\star\), the three step thresholds coincide; for \(r>r_\star\), their order is reversed (even if \(t_-\le0\)). Therefore the requested strict antithetic-only regime exists if and only if the stated condition holds.

**5. Rational witness.** At \((a,b,\eta)=(1,2,3/5)\), substitute \(m_2=5/2\), \(m_4=17/2\), \(\eta^2=9/25\) to obtain the three rational values in the finding. Also \(t_+=5/17<t_0=8/25<9/25<t_-=3/8\). All inequalities are strict.

## Verification

`CHECK.py` is a dependency-free Python 3 exact-rational replay. It verifies 1,490 arithmetic assertions for the one-step matrix update, all coupling formulas at multiple rational coefficients, step sizes and pair correlations, the factorization identities, and the rational witness. Run it with `python3 CHECK.py`. Its finite checks are supplementary; the identities and all-parameter classifications are proved above. Source dates refer to initial public appearances, not subsequent publication or revision dates.

## Relationship to prior work

Mishchenko--Kovalev--Shulgin--Richtárik--Malitsky [1] introduce same-sample stochastic extragradient as a remedy for failures of independently sampled Mirror-Prox on bilinear problems. Gorbunov--Berard--Gidel--Loizou [2] analyze same-sample and independent-sample extragradient, including arbitrary sampling *of a single reused sample or minibatch*. Li and collaborators [3] study same-sample bilinear games and iteration averaging. Yoon--Loizou [4] derive complex scalar update multipliers for the same two conventional sampling modes and distinguish almost-sure from mean-square behavior. None of the compared statements supplies the sharp **joint-law** optimizer for a within-step pair with fixed uniform marginals, the antithetic-only stable interval, or the exact heterogeneity cutoff. Chae--Yun--Kim [5] study across-iteration flip-flop shuffling and anchoring of same-sample extragradient; Luo and collaborators [6] employ antithetic *midpoint-location* randomization in a different integration method, not opposite finite-sum component indices in paired conventional extragradient. These similarities motivate scrutiny but do not themselves imply the claim. A complete publication-priority guarantee is not asserted.

## Limitations

The result is exact for two positive bilinear component coefficients, a planar skew generator, fixed equal stage steps, uniform marginal sampling, and independent iteration pairs. It does **not** establish robustness to additive noninterpolation noise, arbitrary unequal component probabilities, larger finite sums, general convex-concave games, almost-sure convergence, or adaptive step sizes. Mean-square expansion does not by itself prove almost-sure divergence. The calculation assumes exact arithmetic. Specialized equivalent results outside the inspected literature may exist.

## References

1. K. Mishchenko, D. Kovalev, E. Shulgin, P. Richtárik, Y. Malitsky, *Revisiting Stochastic Extragradient*, arXiv:1905.11373, first public 2019-05-27; AISTATS 2020.
2. E. Gorbunov, H. Berard, G. Gidel, N. Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, arXiv:2111.08611, first public 2021-11-16; AISTATS 2022.
3. C. J. Li et al., *On the Convergence of Stochastic Extragradient for Bilinear Games using Restarted Iteration Averaging*, arXiv:2107.00464, first public 2021-06-30; AISTATS 2022.
4. T. Yoon, N. Loizou, *On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities*, arXiv:2608.06182, first public 2026-08-06, especially Lemma 3.11.
5. J. Chae, C. Yun, D. Kim, *Stochastic Extragradient with Flip-Flop Shuffling & Anchoring: Provable Improvements*, arXiv:2501.00511, first public 2024-12-31; NeurIPS 2024.
6. Z. Luo et al., *RAMPAGE: RAndomized Mid-Point for debiAsed Gradient Extrapolation*, arXiv:2603.22155, first public 2026-03-23.
