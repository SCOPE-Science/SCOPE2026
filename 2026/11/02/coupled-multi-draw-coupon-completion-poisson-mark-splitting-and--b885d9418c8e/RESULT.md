# Coupled multi-draw coupon completion: Poisson mark splitting and a logistic delay law

## Finding

Fix an integer \(d\ge1\). For each \(n\ge d\), independently at each discrete round sample a uniformly random \(d\)-element subset of \(\{1,\ldots,n\}\). Couple two collection policies using these identical subsets: the **all-offered** policy records every sampled type, while the **one-choice** policy selects just one sampled type, taking an as-yet-unselected type whenever one is available. The one-choice tie rule does not affect the count results. Write \(T_{\mathrm{all}}\) and \(T_{\mathrm{one}}\) for their respective complete-collection rounds.

Set
\[
C_d=\int_0^1\left(\frac{1}{1-(1-u)^d}-\frac{1}{du}\right)\,du,
\qquad c_d=e^{dC_d},
\]
with the integrand extended continuously to \(u=0\). In particular \(c_1=1\), while \(c_d>1\) for \(d\ge2\). At round \(t\), let \(A_n(t)\) count types never offered, and \(B_n(t)\) count types offered but not selected by the one-choice policy. For each fixed real \(x\), at \(t_n(x)=\lfloor n(\log n+x)/d\rfloor\),
\[
(A_n(t_n(x)),B_n(t_n(x)))\ \Longrightarrow\
\left(\operatorname{Pois}(e^{-x}),\operatorname{Pois}((c_d-1)e^{-x})\right),
\]
where the two limiting Poisson variables are **independent**. This is a joint count law, not merely two separate Poisson marginal laws.

Consequently, for the completion-time pair
\[
X_n=\frac{dT_{\mathrm{all}}}{n}-\log n,\qquad
Y_n=\frac{dT_{\mathrm{one}}}{n}-\log n,
\]
the limiting joint distribution function, for any fixed \(x,y\in\mathbb R\), is
\[
\lim_{n\to\infty}\Pr(X_n\le x,Y_n\le y)=
\begin{cases}
\exp\{-e^{-x}-(c_d-1)e^{-y}\},&x\le y,\\
\exp\{-c_de^{-y}\},&x>y.
\end{cases}
\]
For \(d\ge2\) the limiting pair can be represented as \((G_1,\max\{G_1,G_2+\log(c_d-1)\})\), where \(G_1,G_2\) are independent standard Gumbel variables. For \(d=1\) both coordinates are the same Gumbel variable.

In particular the nonnegative normalized delay \(D_n=d(T_{\mathrm{one}}-T_{\mathrm{all}})/n\) converges weakly to \(D\), with
\[
\Pr(D\le z)=\begin{cases}
0,&z<0,\\
\displaystyle\frac{1}{1+(c_d-1)e^{-z}},&z\ge0.
\end{cases}
\]
Its mass at zero is \(1/c_d\); moreover the probability of **exactly equal finite completion rounds** tends to \(\Pr(T_{\mathrm{one}}=T_{\mathrm{all}})\to1/c_d\).

## Assumptions and scope

The sample size \(d\) is a **fixed positive integer** as \(n\to\infty\). Each round's offered subset has exactly \(d\) distinct types, with different rounds independent. The one-choice policy must select an unselected offered type if any exists; its choices among already selected types after all offered types are selected are immaterial, as are ties before completion for the joint counts. For the tagged-exchangeability argument below, one can choose uniform random tie-breaking among the offered unselected types, since the three count processes and both completion times are independent of the tie-breaking rule. The limits are for fixed real arguments; no growing \(d\) or quantitative convergence rate is asserted.

## Proof

**1. Exact pure-death process and central window.** Let \(U_n(t)=A_n(t)+B_n(t)\), the number not yet selected by the one-choice policy. Whenever \(U_n(t)=u\), the probability of selecting a new type in the next round is
\[
q_{n,u}=1-\frac{\binom{n-u}{d}}{\binom nd},
\]
where the numerator is zero if \(n-u<d\). Thus \(U_n\) is a pure-death chain, starting from \(n\), with independent geometric holding times of parameters \(q_{n,u}\). Let \(m=\lfloor\sqrt n\rfloor\) and \(H_{n,m}\) be the first time it reaches \(m\). With \(g(u)=1-(1-u)^d\), fixed \(d\), the exact death parameters obey \(q_{n,u}\ge u/n\), and, after subtracting their common singular part, a Riemann-sum estimate gives
\[
\frac{\mathbb EH_{n,m}}n=
\frac1d\log\frac nm+C_d+o(1),\qquad
\frac{\operatorname{Var}H_{n,m}}{n^2}
\le\sum_{u=m+1}^n\frac1{u^2}=O(m^{-1}).
\]
For the first estimate use \(1/q_{n,u}=n/(du)+[1/g(u/n)-n/(du)]+O_d(1/u)\) uniformly away from the finitely many boundary indices; the accumulated remainder is \(o(n)\), and the bracketed term has a continuous extension at zero. The summands are independent, so standard geometric moment-generating-function bounds imply, for each fixed \(\delta>0\), that \(\Pr(|H_{n,m}-\mathbb EH_{n,m}|>\delta n)\) decays faster than any fixed inverse power of \(n\).

For \(1\le u\le m\),
\[
-\log(1-q_{n,u})=\frac{du}{n}\bigl(1+O_d(m/n)\bigr).
\]
Each remaining geometric holding time can be realized as the ceiling of an exponential holding time with that logarithmic rate. Comparison with the pure-death chain of rates \(du/n\) gives a cumulative discrepancy \(o(n)\) uniformly for the final \(m\) deaths, with errors controlled by sums of \(O(m)\) roundings and \(O_d(m/n)\) times the exponential holding times. The reference pure-death chain is exactly the number of survivors among \(m\) independent lifetimes of exponential rate \(d/n\). Because \(m e^{-(\log m+x-dC_d)}=c_de^{-x}\), the entrance-time concentration and late-time exponential coupling yield
\[
U_n(t_n(x))\Longrightarrow \operatorname{Pois}(c_de^{-x}).
\]
The geometric and exponential concentration bounds also give \(\sup_n\mathbb E[(U_n(t_n(x)))_b^2]<\infty\) for each fixed integer \(b\ge0\), hence factorial-moment convergence
\[
\mathbb E(U_n(t_n(x)))_b\longrightarrow(c_de^{-x})^b.
\]
The same limit holds if \(n\) is replaced by \(n-a\) for any fixed \(a\ge0\), while the observation time remains \(t_n(x)\). Here \((v)_b=v(v-1)\cdots(v-b+1)\).

**2. Exact tagged identity and independent Poisson splitting.** Fix disjoint labeled sets \(I,J\) of sizes \(a,b\). Using an exchangeable tie rule, condition on every round avoiding \(I\): the probability of this event is \([\binom{n-a}{d}/\binom nd]^{t}\), and conditional on it the one-choice policy acts on the other \(n-a\) types exactly as the original policy with that smaller population. The exact tagged identity is therefore
\[
\Pr(I\hbox{ all never offered},\ J\hbox{ all not selected})=
\left(\frac{\binom{n-a}{d}}{\binom nd}\right)^t
\frac{\mathbb E(U_{n-a}(t))_b}{(n-a)_b}.
\]
At \(t=t_n(x)\), multiplication by \(n^{a+b}\) makes its right-hand side tend to \(c_d^b e^{-(a+b)x}\). To require every member of \(J\) to have been offered but remain unselected, inclusion-exclusion over which members of \(J\) are still unoffered produces
\[
 n^{a+b}\Pr(I\hbox{ unseen},\ J\hbox{ seen but unselected})
 \longrightarrow e^{-(a+b)x}\sum_{j=0}^{b}(-1)^j\binom bj c_d^{b-j}
 =e^{-(a+b)x}(c_d-1)^b.
\]
Multiplying by \((n)_{a+b}\) proves, for every fixed \(a,b\ge0\),
\[
\mathbb E[(A_n(t_n(x)))_a(B_n(t_n(x)))_b]
\longrightarrow e^{-ax}\bigl((c_d-1)e^{-x}\bigr)^b.
\]
Mixed factorial moments identify the product of the two asserted Poisson distributions. This also handles \(d=1\), for which \(B_n\equiv0\).

**3. Joint completion times and exact ties.** The count pair \((A_n,B_n)\) is a finite-state Markov chain. In any time window of length \(O(n)\) around \(t_n(x)\), its counts are tight by Step 2. If \(A_n+B_n\le K\), the chance that a single offered group contains two still-unselected types is \(O_{K,d}(n^{-2})\), and each individual still-unselected type is offered with probability \(d/n\). In scaled time \(s=dt/n-\log n\), the pair therefore converges locally to two **independent linear-death processes**, each particle dying at rate one; an unoffered particle becomes selected at its first appearance, so asymptotically there is no transfer from the first to the second class. The independent Poisson initialization from Step 2 is preserved across later times by independent exponential thinning. Since completion is the first time the respective relevant counts reach zero and the marginal completion times are tight, the claimed joint completion-time distribution follows: for \(x\le y\), require \(A(x)=0\) and \(B(y)=0\); for \(x>y\), use \(T_{\mathrm{all}}\le T_{\mathrm{one}}\).

The independent death-process construction is equivalent to two independent Poisson point processes of terminal times, with intensity tails \(e^{-x}\) and \((c_d-1)e^{-x}\). Their maxima are \(G_1\) and \(G_2+\log(c_d-1)\). Since \(e^{-G_1}\) has the unit exponential law, for \(z\ge0\),
\[
\Pr(D\le z)=\mathbb E\exp[-(c_d-1)e^{-z}e^{-G_1}]
=\frac{1}{1+(c_d-1)e^{-z}}.
\]
For \(d\ge2\), the two terminal maxima are distinct almost surely. A last B-type disappearance strictly before the last A-type disappearance means both finite policies finish on the same draw for all sufficiently large \(n\), apart from events involving two rare types in one group; the opposite strict ordering means they finish on different draws. The probability of a near-tie vanishes as the window shrinks, proving \(\Pr(T_{\mathrm{one}}=T_{\mathrm{all}})\to\Pr(G_2+\log(c_d-1)<G_1)=1/c_d\). For \(d=1\) equality is exact at every \(n\).

## Verification

Run `python verify_multidraw_joint.py` with Python 3 and no third-party dependencies. The verifier checks exact rational count transitions against exhaustive labeled-mask dynamics, the exact tagged identity against independent count recursions, a finite exact tie identity for two-offer samples, and numerical finite-population joint completion probabilities against the limiting formula. The recorded package run passed 1,351 assertions. These finite calculations support the proof but do **not** establish the infinite limiting statements independently.

As illustrations, \(c_2=2\) exactly, giving limiting exact-tie probability \(1/2\); numeric quadrature gives \(c_3\approx4.289652925204\) and limiting exact-tie probability \(0.233119093185\).

## Relationship to prior work

Doumas and Spektor (2026, arXiv:2607.01463) introduce and study the two multi-draw retention rules, derive exact completion-time means, asymptotic expansions, variance rates, and the **separate** limiting Gumbel distributions. Their \(C_d\) is the same integral used above. Those individual marginal results are not claimed as new here. Xu and Tang (2011) establish related least-collected multi-draw completion expectations. The distinguishing statement here is the joint coupling under the **same offered groups**, whose two residual categories split into independent Poisson populations and whose completion lag has a nontrivial logistic law and an atom at zero. Results on group-drawn coupon occupancy that do not involve the adaptive one-choice policy do not determine this paired law.

## Limitations

All limits assume fixed \(d\). The proof does not provide uniform rates for \(d\) growing with \(n\), nor higher-order corrections to the joint distribution. The listed earlier literature was compared by mathematical statements rather than matching titles, but unindexed historical results on coupled coupon collection or general marked pure-death processes remain a possible priority risk. The research is not an independent mathematical audit.

## References

- A. V. Doumas and S. Spektor, *Two Multi--Draw Coupon Collector models with different retention rules*, arXiv:2607.01463 (first posted 2026-07-01), https://arxiv.org/abs/2607.01463.
- W. Xu and A. K. Tang, *A Generalized Coupon Collector Problem*, Journal of Applied Probability 48 (2011), 1081–1094, https://people.ece.cornell.edu/atang/pub/11/Coupon_collector.pdf.
- M. Mahmoud and R. T. Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, Advances in Applied Probability 44 (2012), 429–451, DOI 10.1239/aap/1339878719.
- P. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability (2021), https://doi.org/10.1017/jpr.2021.15.
- M. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485, https://arxiv.org/abs/2202.07485.
