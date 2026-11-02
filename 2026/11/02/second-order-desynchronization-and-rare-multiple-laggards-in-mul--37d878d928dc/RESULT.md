# Second-order desynchronization and rare multiple laggards in multi-collector coupon races

## Finding

Fix an integer \(q\ge3\). There are \(q\) independent collectors, each drawing one coupon per round, with replacement, uniformly from the same set of \(d\ge2\) types. Let \(K_{d,q}\) be the number of distinct types held by every collector immediately before the **first round in which their distinct-type counts cease to be equal**. Put \(K_{d,q}=d\) if they remain synchronized through joint completion. On a genuine first unequal round, let \(J_{d,q}\in\{1,\ldots,q-1\}\) count collectors that **do not** acquire a new type in that round; put \(J_{d,q}=0\) on the exceptional complete-tie event.

For every fixed \(q\ge3\), as \(d\to\infty\),

\[
\frac{K_{d,q}}{\sqrt d}\Rightarrow X_q,\qquad
\Pr(X_q\in dx)=qxe^{-qx^2/2}\mathbf 1_{x>0}\,dx,
\]

\[
\boxed{\mathbb E K_{d,q}=\sqrt{\frac{\pi d}{2q}}-\frac1{3q}+O_q(d^{-1/2})},
\]

\[
\boxed{\Pr(J_{d,q}=2)=\frac{q-1}{2}\sqrt{\frac{\pi}{2q}}\,d^{-1/2}+O_q(d^{-1})},
\qquad
\Pr(J_{d,q}\ge3)=O_q(d^{-1}).
\]

A stronger local theorem specifies the finite-size mechanism. For \(1\le k\le R\sqrt{d\log d}\), writing \(x=k/\sqrt d\) and fixing \(R>0\),

\[
\Pr(K_{d,q}=k)=\frac{q x}{\sqrt d}e^{-qx^2/2}
\left[1+\frac1{\sqrt d}\left(\frac x2-\frac{q x^3}{6}\right)
+O_{q,R}\left(\frac{1+x^6}{d}\right)\right].
\]

The endpoint \(q=2\) has a special cancellation not present at \(q\ge3\): its exact tie-break law (already obtained in the motivating paper) admits the explicit binomial/bridge representation

\[
\Pr(K_{d,2}=k)=\frac{2k}{d}\frac{\binom{2d}{d-k}}{\binom{2d}{d}},\quad 1\le k\le d,
\]

and is the law of one plus the maximum of a simple symmetric \((2d-1)\)-step random-walk bridge ending at \(-1\). In particular,

\[
\mathbb E K_{d,2}=\frac{4^d}{2\binom{2d}{d}}=
\frac{\sqrt{\pi d}}2+\frac{\sqrt\pi}{16\sqrt d}+O(d^{-3/2}),
\qquad \mathbb E K_{d,2}^2=d.
\]

The \(q=2\) identities are auxiliary explanations of the exceptional boundary, not claims to a new two-player tie-break distribution.

## Assumptions and scope

All collectors draw independently of one another and across rounds. A coupon is new to a given collector if it has not appeared in that collector's previous draws. Simultaneous counts are compared after each complete round. The collector count \(q\) is fixed as \(d\) tends to infinity, not permitted to grow with \(d\). The variable \(K_{d,q}\) counts distinct *types* at departure, not elapsed rounds, and \(J_{d,q}\) counts the laggards on the first unequal round, not eventual losing collectors.

For \(1\le k<d\), define \(u_k=k/d\),

\[
a_{q}(u)=\frac{(1-u)^q}{1-u^q},\qquad
S_{d,q}(k)=\prod_{r=1}^{k}a_q(u_r),\quad S_{d,q}(0)=1.
\]

All-idle rounds at a tied level are erased only to compute first-exit probabilities, not to alter the underlying trial process. Erasure is justified by geometric waiting at every tied level where \(u<1\). The exact joint law is

\[
\boxed{\Pr(K_{d,q}=k,J_{d,q}=j)
=S_{d,q}(k-1)\frac{\binom qj u_k^j(1-u_k)^{q-j}}{1-u_k^q}}
\quad(1\le k<d,\ 1\le j<q).
\]

The remaining mass is \(\Pr(K_{d,q}=d,J_{d,q}=0)=S_{d,q}(d-1)\). These formulas are valid at every finite \(d\) and \(q\ge2\).

## Proof

**1. Exact renewal stage law.** At a synchronized level \(k\), each collector independently obtains a new type with probability \(1-u_k\). The probabilities of all-new and all-old updates are respectively \((1-u_k)^q\) and \(u_k^q\). The all-old update leaves every count unchanged and may be erased. Dividing the remaining transition probabilities by \(1-u_k^q\) produces the continuation factor \(a_q(u_k)\) and the joint first-exit probabilities displayed above. At \(k=0\), all collectors must advance; at \(k=d\), all have completed. The finite probabilities sum to one by telescoping the stage survival.

**2. Gaussian localization.** For fixed \(q\ge3\) and \(u\) small,

\[
\log a_q(u)=q\log(1-u)-\log(1-u^q)
=-qu-\frac q2u^2+O_q(u^3).
\]

For \(k\le d/2\), continuity and strict positivity of \(-\log a_q(u)/u\) on \([0,1/2]\) imply \(S_{d,q}(k)\le\exp(-c_q k^2/d)\). For \(k>d/2\), monotonicity of survival gives \(S_{d,q}(k)\le\exp(-c_qd)\). Consequently tails beyond \(R\sqrt{d\log d}\), even when weighted by a fixed polynomial in \(k\), are of arbitrarily small polynomial order in \(d\) by choosing \(R\) sufficiently large. Also \(S_{d,q}(d-1)=O_q(e^{-c_qd})\).

**3. Uniform local expansion.** Set \(\delta=d^{-1/2}\), \(x=k\delta\). For \(k\le R\sqrt{d\log d}\), expansion of the finite product, including the exact sums of \(r\) and \(r^2\), gives

\[
\log S_{d,q}(k-1)
=-\frac{qx^2}{2}+\delta\left(\frac{qx}{2}-\frac{qx^3}{6}\right)
+O_{q,R}\big(\delta^2(1+x^4)\big).
\]

Likewise, the conditional mixed-event hazard satisfies

\[
1-a_q(k/d)=q x\delta
\left[1-\frac{q-1}{2}x\delta+O_q(x^2\delta^2)\right].
\]

Multiplication and exponentiation prove the stated local expansion, uniformly in its window. The leading Riemann sum yields the Rayleigh law. Its first correction is nonzero for general \(q\ge3\); the exceptional \(q=2\) case has a quadratic cancellation because \(-\log(1-u^2)\) cancels the quadratic term in \(2\log(1-u)\).

**4. Mean correction.** Let \(f_q(x)=qxe^{-qx^2/2}\) and \(H_q(x)=x/2-qx^3/6\). From step 3, Gaussian localization, and a one-sided Euler--Maclaurin bound (the leading summand \(xf_q(x)\) and its first derivative vanish at zero),

\[
\mathbb E K_{d,q}
=\delta^{-1}\int_0^\infty xf_q(x)\,dx
+\int_0^\infty xf_q(x)H_q(x)\,dx+O_q(\delta).
\]

The Rayleigh moments are \(\mathbb E X_q^2=2/q\) and \(\mathbb E X_q^4=8/q^2\). Thus the constant term is

\[
\int_0^\infty xf_q(x)H_q(x)\,dx
=\frac12\frac2q-\frac q6\frac8{q^2}=-\frac1{3q}.
\]

The leading mean is \(\sqrt{\pi/(2q)}\), proving the asserted expansion. Here the Euler--Maclaurin boundary correction is zero because \(xf_q(x)=O(x^2)\); the integrable Gaussian derivatives control the remainder. In particular a finite sum does not alone justify the asymptotic result.

**5. Multiple laggards.** Exact stage probabilities from step 1 give, for \(j=2\),

\[
\Pr(K_{d,q}=k,J_{d,q}=2)
=S_{d,q}(k-1)\frac{\binom q2(k/d)^2(1-k/d)^{q-2}}{1-(k/d)^q}.
\]

Its Riemann sum, dominated by the Gaussian bound of step 2, is

\[
\Pr(J_{d,q}=2)
=\frac{\binom q2}{\sqrt d}\int_0^\infty x^2e^{-qx^2/2}\,dx+O_q(d^{-1})
=\frac{q-1}{2}\sqrt{\frac\pi{2q}}\,d^{-1/2}+O_q(d^{-1}).
\]

The local relative error is \(O_q((1+x^3)/\sqrt d)\) on the Gaussian window, which after summation contributes \(O_q(d^{-1})\). For \(j\ge3\), the same argument bounds each total by \(O_q(d^{-(j-1)/2})\), proving \(\Pr(J_{d,q}\ge3)=O_q(d^{-1})\). This includes the case \(q=3\), where three laggards cannot cause an unequal update.

**6. Exact two-collector boundary.** In the motivating two-player formula, \(a_2(k/d)=(d-k)/(d+k)\). Hence

\[
\Pr(K_{d,2}>k)
=\frac{\binom{2d-1}{d-1-k}}{\binom{2d-1}{d-1}}
\qquad(0\le k<d).
\]

The elementary reflection principle identifies this with the probability that a symmetric walk of length \(2d-1\), conditioned to end at \(-1\), reaches level \(k\). Thus the claimed bridge-maximum identity follows. Tail summation gives

\[
\mathbb E K_{d,2}=\sum_{k=0}^{d-1}\Pr(K_{d,2}>k)
=\frac{4^d}{2\binom{2d}{d}}.
\]

For the second moment use \(\mathbb E K^2=\sum_{k\ge0}(2k+1)\Pr(K>k)\) and the telescoping identity \((d+k)S_k-(d+k+1)S_{k+1}=(2k+1)S_k\), with \(S_0=1,S_d=0\). The sum is exactly \(d\). Stirling's central binomial expansion supplies the displayed mean expansion. These are elementary consequences of the two-player entrance law, explicitly distinguished from the genuinely multi-collector assertions.

## Verification

The standalone standard-library script `verify.py` checks the finite first-exit distribution exactly using rational arithmetic, sums all mixed update patterns directly, verifies two-player binomial and moment identities, and exhaustively enumerates conditioned nearest-neighbor walk bridges up to seven coupon types. It also evaluates the two \(q\ge3\) asymptotic constants at large finite \(d\) as diagnostic rather than proof. Running `python3 verify.py` returned `PASS 3278 exact finite and supplementary numerical checks`. The analytic arguments above establish the asymptotics for every fixed integer \(q\ge3\); the finite checker is not treated as an infinite certificate.

## Relationship to prior work

Long's 2026 two-player renewal--Catalan study gives the \(q=2\) first-break product and its leading Rayleigh limit. The new result is the all-fixed-\(q\ge3\) second-order first-break law and the sharp probability of multiple laggards, neither a two-player special case nor a terminal coupon-completion statistic. Myers and Wilf's earlier two-player competition analysis treats simultaneous completion and post-tie winners. Krityakierne and Aek Thanatipanonda's multi-player study analyzes fastest/slowest complete-collection times, rather than the departure level from exact count synchronization. The classical random-walk reflection principle provides the boundary case \(q=2\), not the multi-collector statement. Other unpublished or unindexed first-exit analyses may exist.

## Limitations

The result assumes equal coupon probabilities, independent parallel sampling, and fixed \(q\). Neither a joint regime \(q=q_d\to\infty\), asymmetric coupon probabilities, time-to-break distribution, nor post-break ranking/winner probabilities is established. The exact \(q=2\) distribution is credited to Long; the ancillary bridge and moment identities are not the source of the originality claim. The evidence for historical priority is a targeted but nonexhaustive literature and mathematical-record search; no independent mathematical audit has been carried out.

## References

1. Christopher D. Long, *The Ballot Event for Two-Player Coupon Collection: A Renewal--Catalan Asymptotic*, arXiv:2605.09641v1, first submitted 2026-05-10. https://arxiv.org/abs/2605.09641
2. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1, first submitted 2003-04-16. https://arxiv.org/abs/math/0304229
3. Tipaluck Krityakierne and Thotsaporn Aek Thanatipanonda, *The Slowest Coupon Collector's Problem*, arXiv:2211.04374, first submitted 2022-11-08. https://arxiv.org/abs/2211.04374
4. William Feller, *An Introduction to Probability Theory and Its Applications*, Vol. I, third edition, Wiley, 1968 (classical reflection principle and binomial estimates).
