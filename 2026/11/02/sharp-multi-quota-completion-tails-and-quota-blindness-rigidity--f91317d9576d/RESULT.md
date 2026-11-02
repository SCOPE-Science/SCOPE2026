# Sharp multi-quota completion tails and quota-blindness rigidity in a Pólya urn

## Finding

Let \(d\ge2\) and let \(a_1,\ldots,a_d>0\) be initial colour masses in a unit-reinforced Pólya urn. For positive integer quotas \(r_1,\ldots,r_d\), define \(\tau\) to be the first draw number at which every colour has been seen at least its quota, and let \(J\) be the colour of the unique final draw. Write
\[
 A=\sum_{i=1}^{d}a_i,\qquad R=\sum_{i=1}^{d}r_i,\qquad a_*=\min_i a_i,
\]
\[
 c_i=\frac{\Gamma(A)}{\Gamma(A-a_i)}\sum_{k=0}^{r_i-1}\frac{(a_i)_k}{k!},
 \qquad C_*=\sum_{i:a_i=a_*}c_i,
\]
where \((a)_k=a(a+1)\cdots(a+k-1)\), with \((a)_0=1\).

**Theorem (completion tail, terminal colour and exact rigidity).** For every fixed initial-mass vector and quota vector, as integer \(t\to\infty\),
\[
 \Pr(\tau>t)\sim C_*t^{-a_*},\qquad
 \Pr(\tau=t,J=i)\sim a_ic_i t^{-a_i-1}
 \quad(1\le i\le d).
\]
Consequently \(\Pr(\tau=t)\sim a_*C_*t^{-a_*-1}\), and for every real \(q>0\),
\[
 \mathbb E[\tau^q]<\infty\quad\Longleftrightarrow\quad q<a_*.
\]
Also,
\[
 \lim_{t\to\infty}\Pr(J=i\mid\tau=t)
 =\begin{cases}c_i/C_*,&a_i=a_*,\\0,&a_i>a_* .\end{cases}
\]

If instead \(a_1=\cdots=a_d=1\), then for every integer \(t\),
\[
 \Pr(\tau\le t)=
 \begin{cases}
 0,&t<R,\\
 \displaystyle\frac{\binom{t-R+d-1}{d-1}}{\binom{t+d-1}{d-1}},&t\ge R.
 \end{cases}
\]
In this case the full time law depends on the quotas **only through their sum**, and the terminal colour is independent of the completion time:
\[
 \Pr(J=i,\tau=t)=\frac{r_i}{R}\Pr(\tau=t)
 \quad(t\ge R),\qquad \Pr(J=i)=\frac{r_i}{R}.
\]
In particular, \(\Pr(\tau>t)\sim(d-1)R/t\), so every such multi-quota completion time has infinite mean.

This quota-blindness property is **rigid**: among all positive initial mass vectors with unit reinforcement and fixed \(d\ge2\), the law of \(\tau\) depends only on \(R\) for **every** positive integer quota vector if and only if \(a_1=\cdots=a_d=1\).

## Assumptions and scope

The draw at stage \(t+1\), conditional on the first \(t\) draws containing \(N_i(t)\) occurrences of colour \(i\), has probability
\[
 \Pr(X_{t+1}=i\mid N_1(t),\ldots,N_d(t))
 =\frac{a_i+N_i(t)}{A+t}.
\]
Every drawn colour receives one unit of reinforcement. All masses are fixed and strictly positive; all quotas are fixed positive integers; the number of colours \(d\ge2\) is fixed. The integer-valued completion time is
\[
 \tau=\min\{t\ge0:N_i(t)\ge r_i\ \text{for every}\ i\}.
\]
Since a single draw changes one count, exactly one colour \(J\) reaches its quota at time \(\tau\). The asymptotic statements are fixed-parameter results, not estimates uniform in growing quotas or growing numbers of colours. For arbitrary positive masses the formulas are valid as a generalized Pólya model; for integer masses they describe a literal ball urn.

## Proof

**1. Finite-time Dirichlet–multinomial law.** For every weak composition \(n_1+\cdots+n_d=t\), exchangeability of the reinforced draws gives
\[
 \Pr(N_i(t)=n_i\ \forall i)
 =\frac{t!}{(A)_t}\prod_{i=1}^{d}\frac{(a_i)_{n_i}}{n_i!}.
 \tag{1}
\]
Every colour appears infinitely often almost surely: for example the one-colour marginal calculation below gives \(\Pr(N_i(t)<r_i)\to0\), so \(\tau<\infty\) almost surely.

**2. One deficient colour.** Summing (1) over all remaining colours yields the beta–binomial marginal
\[
 \Pr(N_i(t)=k)
 =\binom tk\frac{(a_i)_k(A-a_i)_{t-k}}{(A)_t}.
 \tag{2}
\]
For each fixed nonnegative integer \(k\), elementary Gamma-ratio asymptotics give
\[
 \Pr(N_i(t)=k)
 =\frac{\Gamma(A)}{\Gamma(A-a_i)}\frac{(a_i)_k}{k!}
 t^{-a_i}\bigl(1+O(t^{-1})\bigr).
 \tag{3}
\]
Thus, for \(E_i(t)=\{N_i(t)<r_i\}\),
\[
 \Pr(E_i(t))=c_it^{-a_i}+O(t^{-a_i-1}).
 \tag{4}
\]

**3. Two simultaneously deficient colours are lower order.** For \(i\ne j\) and \(d\ge3\), the remaining initial mass \(A-a_i-a_j\) is positive. From the three-block Dirichlet–multinomial marginal, for fixed \(k,\ell\),
\[
 \Pr(N_i(t)=k,N_j(t)=\ell)
 =\frac{t!}{k!\ell!(t-k-\ell)!}
 \frac{(a_i)_k(a_j)_\ell(A-a_i-a_j)_{t-k-\ell}}{(A)_t}
 =O(t^{-a_i-a_j}).
 \tag{5}
\]
Summing over the finitely many \(k<r_i\) and \(\ell<r_j\) preserves that order. For \(d=2\), simultaneous deficiencies are impossible when \(t\ge r_i+r_j-1\). Inclusion–exclusion applied to \(\{\tau>t\}=\bigcup_i E_i(t)\) now shows that terms with minimal \(a_i\) dominate and intersections are negligible:
\[
 \Pr(\tau>t)=\sum_{i:a_i=a_*}c_it^{-a_*}+o(t^{-a_*}).
 \tag{6}
\]
The discrete tail-sum formula, or comparison of \(\sum_{t\ge1}t^{q-1}\Pr(\tau>t)\), proves the claimed necessary-and-sufficient moment threshold for every real \(q>0\).

**4. Terminal-colour local asymptotics.** The event \(\{\tau=t,J=i\}\) requires \(N_i(t-1)=r_i-1\), all other quotas attained by time \(t-1\), and draw \(i\) at time \(t\). The final-draw probability on the specified \(i\)-count event is exactly \((a_i+r_i-1)/(A+t-1)\). The error from another deficient colour is, by (5) or the two-colour impossibility, \(o(t^{-a_i-1})\) after multiplying by that final-draw probability. Hence (3) gives
\[
 \begin{aligned}
 \Pr(\tau=t,J=i)
 &\sim \frac{a_i+r_i-1}{t}
 \frac{\Gamma(A)}{\Gamma(A-a_i)}
 \frac{(a_i)_{r_i-1}}{(r_i-1)!}t^{-a_i}\\
 &=a_ic_it^{-a_i-1}.
 \end{aligned}
 \tag{7}
\]
The final equality follows from the rising-factorial identity
\[
 \sum_{k=0}^{r_i-1}\frac{(a_i)_k}{k!}
 =\frac{(a_i+1)_{r_i-1}}{(r_i-1)!}.
\]
Sum (7) over colours to obtain the local law for \(\tau\); divide by that sum to obtain the limiting conditional law of \(J\).

**5. Exact law and last-colour independence at unit masses.** If each \(a_i=1\), then the factors \((a_i)_{n_i}/n_i!\) in (1) all equal one. Thus \((N_1(t),\ldots,N_d(t))\) is uniform on the \(\binom{t+d-1}{d-1}\) weak compositions of \(t\). For \(t\ge R\), shifting each count by its quota establishes the displayed exact completion CDF.

Fix \(i\) and \(t\ge R\). Just before the last draw, the qualifying count vectors have \(N_i(t-1)=r_i-1\) and all other counts at least their quotas. There are precisely \(\binom{t-R+d-2}{d-2}\) such vectors. Each has probability \(1/\binom{t+d-2}{d-1}\) at time \(t-1\), and the next draw chooses colour \(i\) with probability \(r_i/(t+d-1)\). Therefore
\[
 \Pr(\tau=t,J=i)=
 \frac{r_i\binom{t-R+d-2}{d-2}}
 {(t+d-1)\binom{t+d-2}{d-1}}.
 \tag{8}
\]
The factor other than \(r_i\) is independent of \(i\). Summing (8) shows it equals \(\Pr(\tau=t)/R\), giving exact independence and quota-proportional terminal-colour probabilities. Expanding the completion CDF as \(t\to\infty\) gives \(\Pr(\tau>t)\sim(d-1)R/t\), consistent with (6), since \(c_i=(d-1)r_i\) when all initial masses are one.

**6. Rigidity.** Assume, conversely, that for fixed positive initial masses the entire completion-time distribution depends only on total quota \(R\) for every positive integer quota vector. At the minimal possible completion time \(t=R\), exactly the quota composition must occur, so (1) yields
\[
 \Pr(\tau=R)
 =\frac{R!}{(A)_R}\prod_{i=1}^{d}\frac{(a_i)_{r_i}}{r_i!}.
 \tag{9}
\]
Take \(R=d+1\), assigning quota \(2\) to one colour and quota \(1\) to every other colour. Comparing two choices for the colour with quota \(2\), equation (9) forces \(a_i+1=a_j+1\) for every pair \(i,j\). Thus all masses equal some \(a>0\).

Next take \(R=d+2\) and compare the quota vectors \((3,1,\ldots,1)\) and \((2,2,1,\ldots,1)\). Their probabilities in (9) have ratio
\[
 \frac{2(a+2)}{3(a+1)}.
\]
Quota-blindness requires this ratio to equal one, so \(a=1\). The forward implication was proved in step 5, completing the if-and-only-if classification. Both compared configurations exist for \(d=2\) as well.

## Verification

The independent standard-library program `verify.py` reconstructs exact finite reinforced-urn probabilities using rational rising factorials; independently propagates weighted draw paths by the urn transition law; compares completion CDFs, terminal-colour laws, and minimal-time rigidity ratios for numerous small colour counts, quotas and rational initial masses; and tests the Gamma constants numerically at increasing time scales. A full run printed `PASS 6214 exact rational comparisons and asymptotic-constant spot checks`. Rational comparisons are exact. The finite experiments validate formulas on tested instances only; the infinite statements follow from steps 1–6.

To reproduce, place `verify.py` alongside this file and run `python verify.py` with Python 3. No external packages, downloaded data or other files are required.

## Relationship to prior work

Bart Jacobs, *Urns & Tubes* (arXiv:2110.02155, publicly available October 5, 2021), formulates fully multicolour, multi-quota Pólya completion probabilities by a pointwise multivariate sum; see Definition 4, Section 7, and the conclusion. This provides the natural starting model and an exact general law. Its conclusion leaves general-tube statistical properties such as moments open. The contribution here is **not** the previously available finite-time state or negative-distribution summation formula, but the evaluated sharp multi-quota tail constants and moment boundary, limiting terminal-colour law, and the exact quota-blindness/independence phenomenon with a converse classification.

Norbert Henze and Mark P. Holmes, *Curiosities regarding waiting times in Pólya’s urn model* (arXiv:1911.01052, publicly available November 4, 2019), analyze one designated colour and show the corresponding one-target moment threshold. That result is consistent with the exponents above but does not give the multiple-colour bottleneck constants, terminal-mark law or rigidity. Classical Dirichlet–multinomial formulas yield the one- and two-colour occupancy marginals used in the proof; they are not claimed as new. Literature searches did not locate an explicit theorem containing this combined classification. Such searches cannot establish definitive historical priority, especially given the extensive classical occupancy and inverse-Pólya literature.

## Limitations

The result uses unit reinforcement, finitely many fixed colours and fixed positive integer quotas. It does not assert the same quota-blindness for unequal reinforcement strengths or changing mass/quotas, nor any uniform-in-dimension tail bounds. For non-integer initial masses, the urn interpretation is in terms of real weights rather than literal ball counts. The displayed moment boundary concerns positive raw moments, not conditional or truncated moments. Historical priority requires further specialist review; no independent mathematical audit is claimed.

## References

1. B. Jacobs, *Urns & Tubes*, arXiv:2110.02155 (initial version October 5, 2021), https://arxiv.org/abs/2110.02155 ; full text https://arxiv.org/html/2110.02155v2 .
2. N. Henze and M. P. Holmes, *Curiosities regarding waiting times in Pólya’s urn model*, arXiv:1911.01052 (initial version November 4, 2019), https://arxiv.org/abs/1911.01052 .
3. E. Anceaume, Y. Busnel, E. Schulte-Geers and B. Sericola, *Optimization results for a generalized coupon collector problem*, Journal of Applied Probability 53 (2016), 622–629, DOI: 10.1017/jpr.2016.27 (fixed, non-reinforced coupon probabilities; not a source for the reinforced-urn theorem).
