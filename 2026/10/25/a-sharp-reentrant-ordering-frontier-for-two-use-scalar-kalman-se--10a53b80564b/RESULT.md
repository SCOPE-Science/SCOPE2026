# A sharp reentrant ordering frontier for two-use scalar Kalman sensing

## Finding

Consider two scalar measurement sensors, one stronger than the other, available for **exactly one use each** over two consecutive observation times. Minimizing the *final* Kalman error variance can require the stronger sensor last for small dynamical gain, first for intermediate gain, and last again for large gain. The complete sharp classification is determined by the ratio of process noise to prior variance.

Write the prior variance as \(p>0\), the stronger and weaker information precisions as \(r>s>0\), the between-observation dynamics as \(x_1=a x_0+w\), and the independent process-noise variance as \(q>0\). Define

\[
C=1+pr,\quad D=1+ps,\quad \nu=q/p,\quad t=a^2,\quad
\nu_*=\frac{1}{(\sqrt C+\sqrt D)^2}.
\]

The final posterior variances for the stronger-first and stronger-last schedules are respectively \(P_{r,s}\) and \(P_{s,r}\). For \(0<\nu<\nu_*\), define the two positive roots

\[
t_\pm=\frac{1-\nu(C+D)\pm
\sqrt{(1-\nu(C+D))^2-4\nu^2CD}}{2}.
\]

Then, exactly:

* \(P_{r,s}<P_{s,r}\) if and only if \(t_-<t<t_+\).
* Equality holds only for \(t=t_-\) or \(t=t_+\).
* \(P_{s,r}<P_{r,s}\) for all other \(t\ge0\).

At \(\nu=\nu_*\), there is a single equality at \(t=\nu\sqrt{CD}\), with stronger-last strictly optimal elsewhere. For \(\nu>\nu_*\), stronger-last is strictly optimal for all \(t\ge0\). In all cases \(q>0\), the stronger-last schedule is strictly preferable whenever \(t\ge1\).

The width of the stronger-first window collapses at the critical noise level by the exact square-root law

\[
t_+-t_-\sim 2(CD)^{1/4}\sqrt{\nu_*-\nu}\qquad(\nu\uparrow\nu_*),
\]

while in the small-noise limit its endpoints obey

\[
t_-=\nu^2CD+O(\nu^3),\qquad
 t_+=1-\nu(C+D)+O(\nu^2).
\]

## Assumptions and scope

The scalar initial state is Gaussian with a strictly positive prior variance \(p\). Sensor observations have the form \(y=x+v\), with independent zero-mean Gaussian noises of variances \(1/r\) and \(1/s\), \(r>s>0\). There is one observation of \(x_0\) and one of \(x_1\), using both sensors exactly once and allowing only the two orders. State evolution is \(x_1=a x_0+w\), where \(a\in\mathbb R\) and \(w\) is independent Gaussian noise of variance \(q>0\). All noises and the prior are independent. The objective is the final posterior variance of \(x_1\), not the sum of intermediate variances or sensor running costs. The theorem covers all real \(a\), all positive \(p,q,s\), and all \(r>s\). In particular \(t=a^2\) may be zero. The strict positivity of \(q\) avoids singular zero-prediction cases.

## Proof

For scalar prior variance \(v>0\), a measurement with information precision \(z>0\) updates variance by

\[
\Phi_z(v)=\frac{v}{1+zv},\qquad \Phi_z(v)^{-1}=v^{-1}+z.
\]

Prediction between observations maps \(v\) to \(tv+q\). Hence, for the two possible schedules, direct recursion gives the *final information precisions*

\[
J_{r,s}=P_{r,s}^{-1}=s+\frac{1}{q+tp/(1+rp)},\qquad
J_{s,r}=P_{s,r}^{-1}=r+\frac{1}{q+tp/(1+ps)}.
\]

All denominators are strictly positive. Subtracting these two independently derived recursions and using \(C=1+pr\), \(D=1+ps\), and \(\nu=q/p\) gives the exact exchange identity

\[
\boxed{J_{r,s}-J_{s,r}
=(r-s)\left(\frac{t}{(t+\nu C)(t+\nu D)}-1\right).}
\]

Because \(r-s>0\), the stronger-first schedule has *smaller* posterior variance precisely when this expression is positive. For \(t\ge0\), that condition is equivalent to

\[
f_\nu(t):=t^2+[\nu(C+D)-1]t+\nu^2CD<0.
\]

At \(t=0\), \(f_\nu(0)=\nu^2CD>0\), giving stronger-last strictly. For \(t>0\), the inequality is equivalent to

\[
\frac{(t+\nu C)(t+\nu D)}{t}<1.
\]

The left side equals \(t+\nu(C+D)+\nu^2CD/t\), whose unique minimum over positive \(t\) occurs at \(t=\nu\sqrt{CD}\), by the arithmetic-geometric mean inequality. That minimum is

\[
\nu(C+D+2\sqrt{CD})=\nu(\sqrt C+\sqrt D)^2.
\]

It is strictly below, exactly equal to, or strictly above one according as \(\nu<\nu_*\), \(\nu=\nu_*\), or \(\nu>\nu_*\). The quadratic \(f_\nu\) opens upward. In the first regime it has the two displayed distinct positive roots and is negative precisely between them; positivity of the roots follows from the positive product \(\nu^2CD\) and positive sum \(1-\nu(C+D)>0\). At the threshold it has a repeated positive root \(\nu\sqrt{CD}\) and is never negative; above threshold it is strictly positive on all nonnegative \(t\). Inverting the strictly positive information precisions reverses their order, proving all strict/tie cases.

If \(t\ge1\), then \((t+\nu C)(t+\nu D)>t^2\ge t\), so the stronger-last schedule always strictly wins, and the entire stronger-first interval lies inside \((0,1)\).

For the endpoint asymptotics, let \(\alpha=(\sqrt C+\sqrt D)^2\) and \(\beta=(\sqrt C-\sqrt D)^2\). The discriminant factors exactly as

\[
\Delta=(1-\alpha\nu)(1-\beta\nu).
\]

Thus, because \(\nu_*=1/\alpha\) and \(\alpha-\beta=4\sqrt{CD}\),

\[
\sqrt\Delta\sim \sqrt{4\sqrt{CD}(\nu_*-\nu)}
=2(CD)^{1/4}\sqrt{\nu_*-\nu}.
\]

This is precisely \(t_+-t_-\). For \(\nu\downarrow0\), Vieta's relations \(t_-t_+=\nu^2CD\), \(t_-+t_+=1-\nu(C+D)\), and \(t_+\to1\) give the displayed small-noise expansions. This completes the proof.

## Verification

The standalone `checker.py` uses exact rational arithmetic to compute both Kalman schedules independently and compare their information-precision difference with the factored identity for 5,000 fixed-seed admissible parameter combinations. It separately checks the polynomial sign, exact rational witnesses and boundary probes. It completed 10,016 assertions. The universal assertions are established by the algebraic proof above, not by finite testing.

For a concrete three-regime witness, let \(p=1\), \(r=3\), \(s=1\), and \(q=1/100\). At \(t=0\), the two final variances are \(P_{r,s}=1/101\) and \(P_{s,r}=1/103\), so stronger-last wins. At \(t=1/4\), they are \(29/429\) and \(27/281\), so stronger-first wins. At \(t=2\), they are \(51/151\) and \(101/403\), so stronger-last wins again.

To reproduce, save the embedded `checker.py` as a file and execute `python checker.py` with a standard Python 3 interpreter; no third-party packages are required.

## Relationship to prior work

Dutta, Wilde and Smith (arXiv:2304.02692v1, 2023) formulate broad finite-horizon Kalman sensor scheduling with linear resource constraints and a mixed-integer convex quadratic optimization approach. Their formulation accommodates exactly-one-use budgets; it does not state an analytical process-noise threshold, two-order transition formula, or reentrant dynamical-gain window. Those specific closed-form structural results are the subject of this finding, not a claim to have invented sensor scheduling or the Kalman recursion.

Maity, Hartman and Baras (arXiv:2110.08924, 2021) study covariance-tracking relaxations for general sensor scheduling. Huber (IEEE TAC 2012, DOI:10.1109/TAC.2011.2175070) establishes a scalar information-dominance pruning observation when sensors may be reused across decision stages: choosing the stronger sensor at every step is then optimal. That does **not** compare the two distinct once-only schedules, where a resource constraint prevents repeated use. Pasand and Montazeri (ETRI Journal 2017, DOI:10.4218/etrij.17.0116.0566) develop a periodic sensor-access design based on convex relaxation rather than the present exact two-observation classification. No directly covering analytical frontier was identified in the investigated scientific sources; this is not a proof of publication priority.

## Limitations

Only two measurement times, one scalar state, two fixed-precision sensors used once each, and final posterior variance are covered. No claims are made for vector states, longer schedules, repeated-use settings, adaptive observation choices, correlated noises, cumulative-error objectives, finite-precision implementations, or sensor acquisition costs. The vanishing-process-noise boundary \(q=0\) is outside the theorem. The established formulas are exact algebraic statements; no independent validation or exhaustive literature priority certification is claimed.

## References

1. S. Dutta, N. Wilde, and S. L. Smith, *A Unified Approach to Optimally Solving Sensor Scheduling and Sensor Selection Problems in Kalman Filtering*, arXiv:2304.02692v1, first posted April 5, 2023. https://arxiv.org/abs/2304.02692
2. D. Maity, D. Hartman, and J. S. Baras, *Sensor Scheduling for Linear Systems: A Covariance Tracking Approach*, arXiv:2110.08924, first posted October 17, 2021. https://arxiv.org/abs/2110.08924
3. M. F. Huber, *Optimal Pruning for Multi-Step Sensor Scheduling*, IEEE Transactions on Automatic Control 57(5), 1338–1343, 2012. DOI:10.1109/TAC.2011.2175070.
4. M. M. S. Pasand and M. Montazeri, *Kalman Filtering with Optimally Scheduled Measurements in Bandwidth Limited Communication Media*, ETRI Journal 39, 13–20, 2017. DOI:10.4218/etrij.17.0116.0566.
