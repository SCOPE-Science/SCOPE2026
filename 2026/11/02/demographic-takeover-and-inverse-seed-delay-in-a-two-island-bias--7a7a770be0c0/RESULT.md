# Demographic takeover and inverse-seed delay in a two-island biased-assimilation model

## Finding

Fix a homophily factor \(h>1\) and a positive island-size ratio \(r>0\). In the two-community, self-weight-free biased-assimilation dynamics at bias exponent \(b=1\), start the communities from complementary, strictly interior opinions \((u_0,v_0)=(x,1-x)\), where \(1/2<x<1\). The complete *demographic takeover criterion* is:

1. If \(r\ge h\), then \((u_t,v_t)\to(1,1)\) for **every** such \(x\).
2. If \(r\le h^{-1}\), then \((u_t,v_t)\to(0,0)\) for **every** such \(x\).
3. If \(h^{-1}<r<h\), then some \(\delta_*>0\) exists such that \((u_t,v_t)\to(1,0)\) whenever \(1-\delta_*<x<1\).

Thus the two demographic cutoffs include equality: even an arbitrarily strongly opposed minority ultimately adopts the larger island's initial position once its population ratio reaches the homophily ratio. These are statements about limiting deterministic opinions, not probabilities of empirical opinion changes.

There is also an exact critical waiting-time law. At \(r=h\), put \(u_0=1-\delta\), \(v_0=\delta\) and, for any fixed \(0<\eta<1\), define \(T_\eta(\delta)=\min\{t\ge0:v_t\ge\eta\}\). As \(\delta\downarrow0\),

\[
T_\eta(\delta)=\frac{1}{2\delta}+O_{h,\eta}\!\left(\log\frac1\delta\right).
\]

By exchanging the islands and complementing opinions, at \(r=h^{-1}\) the first time that \(u_t\le1-\eta\) satisfies the same asymptotic. In particular, the leading inverse-seed coefficient is universal across fixed \(h>1\) and fixed target levels \(\eta\).

## Assumptions and scope

All parameters are real and positive, with \(h>1\) and \(r>0\). The original two-island notation is \(r=n_1/n_2\), \(h=p_s/p_d\), where \(n_1,n_2>0\) are relative group masses and \(p_s>p_d>0\) are within-island and between-island mixing coefficients. Equivalently, the theorem is about the well-defined weighted two-island mean-field recurrence and does not assert that arbitrary real coefficients realize a simple unweighted regular graph.

Define \(\mathcal B(z,s)=zs/[zs+(1-z)(1-s)]\), for \(0<z<1\) and \(0<s<1\). A time step is

\[
\begin{split}
s_1&=\frac{hr\,u+v}{hr+1},& u^+&=\mathcal B(u,s_1),\\
s_2&=\frac{r\,u+h\,v}{r+h},& v^+&=\mathcal B(v,s_2).
\end{split}
\]

The two expressions follow exactly from the bias-one, zero-self-weight update using within-island total weights \(n_1p_s,n_2p_s\) and between-island total weights \(n_2p_d,n_1p_d\). All iterates of strictly interior initial data remain strictly interior at finite times. No network stochasticity, recovery or external media terms are assumed. The critical-time law holds for fixed \(h\) and \(\eta\) while \(\delta\) tends to zero, not uniformly as \(h\downarrow1\).

## Proof

**Elementary drift and monotonicity.** For \(0<z,s<1\), elementary subtraction gives

\[
\mathcal B(z,s)-z=\frac{z(1-z)(2s-1)}{zs+(1-z)(1-s)}.
\]

The map \(\mathcal B\) is strictly increasing in both \(z\) and \(s\) on the open unit square; the latter follows by differentiating the odds identity \(\mathcal B/(1-\mathcal B)=[z/(1-z)][s/(1-s)]\). Thus the sign of a community's one-step drift is exactly the sign of its neighbor mean minus \(1/2\), and an initially coordinatewise increasing (respectively, decreasing) orbit stays so under the cooperative two-island map.

For \((u_0,v_0)=(x,1-x)\), a direct calculation gives

\[
\begin{split}
s_1(0)-\frac12&=\frac{hr-1}{hr+1}\left(x-\frac12\right),\\
s_2(0)-\frac12&=\frac{r-h}{r+h}\left(x-\frac12\right).
\end{split}
\]

If \(r\ge h\), both drifts are nonnegative, the first strictly positive. The orbit is coordinatewise nondecreasing and at the next time both neighbor means are strictly greater than \(1/2\), including at \(r=h\). Hence the coordinate limits exist in \((0,1]\). An interior fixed coordinate would require its limiting neighbor mean to equal \(1/2\), contradicting these strict inequalities. Both limits must therefore equal \(1\). If \(r\le h^{-1}\), both drifts are nonpositive, the second strictly negative; from the next step both are strict, and the same fixed-coordinate argument forces both limits to zero.

**Sharpness of both cutoffs.** At the corner \((u,v)=(1,0)\), the Jacobian of the recurrence is diagonal, with eigenvalues

\[
\lambda_u=\frac{1}{hr},\qquad \lambda_v=\frac{r}{h}.
\]

For clarity, the first is the linear multiplier of \(1-u\), and the second is the multiplier of \(v\). Cross derivatives vanish at the corner because the boundary faces \(u=1\) and \(v=0\) are invariant. Both multipliers lie strictly below one exactly if \(h^{-1}<r<h\). By the standard elementary local contraction argument for a continuously differentiable map with a diagonal Jacobian strictly inside the unit disk, a full neighborhood of the corner in the closed opinion square is attracted to \((1,0)\). It contains all \((1-\delta,\delta)\) for sufficiently small positive \(\delta\). Thus neither demographic takeover criterion can be enlarged into the central ratio interval.

**Critical waiting time.** Set \(r=h\), \(u_t=1-e_t\), \(v_0=e_0=\delta\). The mixing means simplify to

\[
s_1=\frac{h^2(1-e)+v}{h^2+1},\qquad
s_2=\frac{1-e+v}{2}.
\]

For \(0<\delta<1/2\), the initial first-island drift is positive, while the initial second-island drift is zero. Cooperative monotonicity implies \(e_t\) decreases and \(v_t\) increases thereafter. Fix \(\eta\in(0,1)\). By continuity of the defect multiplier \(e^+/e\), whose boundary value at \(e=0\) is \((1-v)/(h^2+v)\le h^{-2}<1\), there exist \(q\in(h^{-2},1)\) and \(\delta_0>0\), depending on \(h,\eta\), such that until \(v_t\) first reaches \(\eta\),

\[
0<e_t\le\delta q^t,\qquad v_t\ge\delta,
\qquad \sum_{t<T_\eta}e_t/v_t\le(1-q)^{-1}.
\]

For this critical recurrence a *direct exact identity*, rather than a Taylor approximation, is

\[
\frac1{v_t}-\frac1{v_{t+1}}
=\frac{2(1-v_t)(v_t-e_t)}{v_t(1-e_t+v_t)}
=:d_t.
\]

Indeed, substitute the displayed expression for \(s_2\) into \(\mathcal B\) and cancel the common denominator. Since \(0\le e_t\le v_t<\eta\) before crossing, \(0\le d_t\le2\), and

\[
0\le2-d_t
=\frac{2(2v_t-2e_t+e_t/v_t)}{1+v_t-e_t}
\le4v_t+2e_t/v_t.
\]

Select a fixed integer \(t_0\) with \(q^{t_0}\le1/2\). For \(t_0\le t<T_\eta\), \(e_t/v_t\le1/2\) and therefore \(d_t\ge c_\eta:=(1-\eta)/(1+\eta)>0\). The identity \(v_{t+1}/v_t=(1-d_tv_t)^{-1}\) yields

\[
\log\frac{v_{t+1}}{v_t}\ge d_tv_t\ge c_\eta v_t.
\]

Summing and using \(v_{T_\eta}\le1\) and \(v_{t_0}\ge\delta\), we get \(\sum_{t<T_\eta}v_t=O_{h,\eta}(\log(1/\delta))\). In particular, the hitting time is finite (otherwise these strict reciprocal decrements would eventually make \(1/v_t\) negative). Telescoping \(d_t\) now gives

\[
2T_\eta-\left(\delta^{-1}-v_{T_\eta}^{-1}\right)
=\sum_{t<T_\eta}(2-d_t)
=O_{h,\eta}\!\left(\log\frac1\delta\right).
\]

Because \(\eta\le v_{T_\eta}<1\), its reciprocal is uniformly bounded, establishing the asserted critical-time law. The lower demographic threshold follows by exchanging islands and complementing opinions, which sends \(r\) to \(r^{-1}\) and leaves \(h\) fixed. This completes the proof.

## Verification

The standalone standard-library script `check.py` tests the exact recurrence over rational parameters, the two initial drift thresholds, the rational critical reciprocal identity, and monotonic approach of the scaled critical hitting time. It reports `VERIFY_OK assertions=1172`. The proof above establishes the statements for all admissible real parameters and all indicated initial conditions; finite checker assertions are only corroboration. Run with `python3 check.py` from the extracted package directory.

For a concrete finite-graph-compatible parameter illustration, \(p_s=3/5\), \(p_d=1/5\) and island sizes \(n_1=30,n_2=10\) give \(h=r=3\). For complementary initial data \((1-\delta,\delta)\) with \(\delta=10^{-4}\), the second island passes opinion \(1/4\) after approximately \(5007\) updates (the leading asymptotic predicts \(5000\)). These exact per-node degree numbers can be implemented by a within-group regular graph and a biregular cross-group graph; this is a model illustration, not empirical data.

## Relationship to prior work

Dandekar, Goel and Lee introduced the biased-assimilation dynamics in 2012 and studied two equal-sized homophilous islands at complementary initial opinions (arXiv:1209.5998v1, especially Section 4 and Appendix C). Their equal-size theorem places \(r=1\) strictly between the two new demographic cutoffs, and therefore neither yields the unequal-size global takeover theorem nor the critical inverse-seed delay.

Xia, Ye, Liu, Cao and Sun (arXiv:1912.01778, 2019; Automatica, 2020) derive general local stability conditions and an all-on-one-side initial-state consensus criterion. Their local theory covers the usual hyperbolic corner multiplier argument, which is *not* claimed as new here. Their all-on-one-side theorem does not apply to initially opposed communities, and their two-island local stability result assumes locally dominant within-community contact degrees; the demographic takeover regimes put one community at or beyond the corresponding cross-contact threshold. Neither inspected relevant section states the global complementary-data demographic cutoffs with equality nor the sharp algebraic waiting time.

Related demographic-peer-effect and polarization studies address different dynamics and do not supply the exact map-level statement here. Originality is stated only relative to the inspected sources, not as an independently certified priority claim.

## Limitations

The result concerns the specific discrete-time, equal-bias-exponent \(b=1\), zero-self-weight, two-homogeneous-community update. The central ratio interval is proven to contain a polarized basin, **not** to force polarization from every complementary initial state. No general classification of all basins, heterogeneous opinions within each island, stochastic meetings, or empirical population-level behavior is claimed. The logarithmic error constant is allowed to depend on fixed homophily and fixed threshold. Other unpublished or differently formulated literature may cover the finding; historical priority requires further independent scrutiny.

## References

1. P. Dandekar, A. Goel and D. Lee, *Biased Assimilation, Homophily and the Dynamics of Polarization*, arXiv:1209.5998v1 (first public 2012-09-26), https://arxiv.org/abs/1209.5998 ; later PNAS 110 (2013), 5791–5796, https://doi.org/10.1073/pnas.1217220110 .
2. W. Xia, M. Ye, J. Liu, M. Cao and X.-M. Sun, *Analysis of a Nonlinear Opinion Dynamics Model with Biased Assimilation*, arXiv:1912.01778 (first public 2019-12-04), https://arxiv.org/abs/1912.01778 ; Automatica 120 (2020), 109113, https://doi.org/10.1016/j.automatica.2020.109113 .
3. S. Bowles, G. C. Loury and R. Sethi, *Group Inequality*, Journal of the European Economic Association 12 (2014), 129–152, https://doi.org/10.1111/jeea.12037 (background on population composition and peer effects, not a matching update equation).
