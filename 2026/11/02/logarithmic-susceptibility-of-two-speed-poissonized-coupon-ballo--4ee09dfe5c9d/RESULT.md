# Logarithmic susceptibility of two-speed Poissonized coupon ballot persistence

## Finding

For each pair of integers \(m,l\geq1\), consider two independent Poissonized coupon collectors, each with \(m\) fast coupon types of Poisson arrival rate one and \(l\) slow coupon types of arrival rate \(\varepsilon>0\). Let \(B_{m,l}(\varepsilon)\) be the probability that the collector who first obtains every type has **never** had fewer distinct types than the other collector at any time. Write \(C_r=\binom{2r}{r}/(r+1)\) and \(H_q=\sum_{i=1}^{q}1/i\). Define the positive rational coefficient

\[
\kappa_m=\frac{1}{\binom{2m}{m}}\sum_{r=0}^{m-1}C_r C_{m-r}\bigl(H_{2m}-H_{2m-2r-1}\bigr).
\]

**Theorem (fixed-group first variation and large-group susceptibility).** For every fixed \(m,l\geq1\), as \(\varepsilon\downarrow0\),

\[
B_{m,l}(\varepsilon)=\frac{2}{(m+1)(l+1)}+\frac{4l}{l+1}\kappa_m\varepsilon+O_{m,l}(\varepsilon^2).
\]

Moreover \(\kappa_m>0\) for all \(m\geq1\), and

\[
\lim_{m\to\infty}\frac{m\kappa_m}{\log m}=1.
\]

Thus, at fixed positive \(l\), the **right derivative at complete speed separation** has the sharp asymptotic

\[
B'_{m,l}(0+)\sim\frac{4l}{l+1}\frac{\log m}{m},
\qquad
\frac{B'_{m,l}(0+)}{B_{m,l}(0+)}\sim2l\log m.
\]

The last two assertions concern the derivative evaluated at zero and then the limit as \(m\to\infty\); no simultaneous limit in \((m,\varepsilon)\) is claimed. An exact illustrative case is

\[
B_{1,1}(\varepsilon)=
\frac{2\varepsilon^4+11\varepsilon^3+22\varepsilon^2+11\varepsilon+2}
{2(\varepsilon+1)^2(\varepsilon+2)(2\varepsilon+1)},
\qquad B_{1,1}'(0+)=\frac12.
\]

## Assumptions and scope

For each collector and coupon label, arrivals form an independent homogeneous Poisson process. Every fast label has rate one, and every slow label rate \(\varepsilon\), identically across the two collectors. A coupon is counted at its first arrival. Each collector has the same \(d=m+l\) labels, and the two collections are independent. The comparison is in *continuous chronological time*, not in paired discrete sampling rounds. With positive rates the first completion times are almost surely distinct. At all times (including before completion), the eventual winning collector must have collected at least as many distinct types as the loser. We count only the first distinct arrival for each label; later repetitions cannot affect this event.

The expansion holds for each fixed integer pair \((m,l)\). The \(O_{m,l}(\varepsilon^2)\) constant is not asserted uniform in either group size. The endpoint \(\varepsilon=0\) is defined by the right-hand limit, not by running non-arriving labels forever. When all rates are equal, \(B_{m,l}(1)=2/(m+l+1)\), by the classical Catalan ballot law.

## Proof

**1. First arrivals and the ballot word.** Poisson thinning and independence make the first arrival of each label an independent exponential clock with its specified rate. Arrange all \(2d\) first arrivals chronologically, writing \(A\) or \(B\) for their collector. The event that \(A\) eventually wins without ever trailing is precisely the set of balanced words with all prefix heights \(\#A-\#B\geq0\). Such words are Dyck words. By exchange of collectors,

\[
B_{m,l}(\varepsilon)=2\Pr(\text{chronological arrival word is a Dyck word for collector A}).
\]

**2. Zero-rate separation and rare interleavings.** In the limit \(\varepsilon\downarrow0\), the \(2m\) fast clocks arrive before the \(2l\) slow clocks with probability tending to one. The fast-colour and slow-colour orders are independent uniformly random balanced words. The fraction of \(2h\)-letter balanced words that are Dyck words is \(C_h/\binom{2h}{h}=1/(h+1)\). Hence

\[
B_{m,l}(0+)=\frac2{(m+1)(l+1)}.
\]

For the first-order perturbation, there is with probability \(1-O_{m,l}(\varepsilon)\) no slow arrival before the last fast one, and the probability of two or more slow arrivals before the last fast one is \(O_{m,l}(\varepsilon^2)\). Let \(E_j\) denote exactly one slow arrival before all fast clocks have rung, occurring after exactly \(j\) fast arrivals, for \(0\leq j<2m\). At that point the aggregate fast rate is \(2m-j\) and the aggregate slow rate is \(2l\varepsilon\). Independence and the memoryless property give

\[
\Pr(E_j)=\frac{2l}{2m-j}\varepsilon+O_{m,l}(\varepsilon^2).
\]

The fast-colour order remains uniform, and the first slow arrival is from either collector with equal probability.

**3. Counting the admissible fast words.** If the early slow arrival belongs to \(B\), then after the last fast arrival collector \(A\) is behind and cannot satisfy the ballot event. If it belongs to \(A\), the fast-word height must be nonnegative up to position \(j\), and at least \(-1\) thereafter. Once all fast coupons are present, the remaining slow words complete a Dyck path starting from height one. Conditional on the first slow colour being \(A\), the fraction of the slow-colour orders that are admissible is \(2/(l+1)\), by the Catalan first-step count. Incorporating the \(1/2\) probability of the early \(A\) arrival yields the conditional \(A\)-ballot probability

\[
\frac{N_{m,j}}{(l+1)\binom{2m}{m}},
\]

where \(N_{m,j}\) counts balanced fast words with height at least zero through position \(j\) and at least \(-1\) afterward. Every Dyck fast word counts. For any other eligible fast word, the first visit to height \(-1\) occurs at time \(2r+1>j\), for a unique \(r\) with \(\lceil j/2\rceil\leq r\leq m-1\). There are exactly \(C_r C_{m-r}\) such words: a Dyck prefix of length \(2r\), the first downward step, followed by a reflected ballot suffix. Consequently,

\[
N_{m,j}=C_m+\sum_{r=\lceil j/2\rceil}^{m-1}C_r C_{m-r}.
\]

**4. Derivative and harmonic weights.** With no early slow arrival, \(A\)-ballot probability is \(1/((m+1)(l+1))\). Conditioning on the rare interleaving position, subtracting the baseline and multiplying by two for either winner gives

\[
B'_{m,l}(0+)=\frac{4l}{(l+1)\binom{2m}{m}}
\sum_{j=0}^{2m-1}\frac{N_{m,j}-C_m}{2m-j}.
\]

The finite sum may be interchanged. For each fixed first bad height \(-1\) at \(2r+1\), admissible positions are \(j=0,\ldots,2r\), and

\[
\sum_{j=0}^{2r}\frac1{2m-j}=H_{2m}-H_{2m-2r-1}.
\]

This proves the stated coefficient. All terms are positive, giving strict susceptibility. The finite-state exponential race has rational transition probabilities in \(\varepsilon\); once the all-fast group has finished, all remaining transition rates share and cancel a factor \(\varepsilon\). Therefore the probability extends rationally and analytically to a neighborhood of zero and the omitted terms are \(O_{m,l}(\varepsilon^2)\).

**5. Logarithmic large-group asymptotic.** Reindex the sum by \(s=m-r\) and set

\[
w_{m,s}=\frac{m C_{m-s} C_s}{\binom{2m}{m}},\qquad 1\leq s\leq m.
\]

Then \(m\kappa_m=\sum_{s=1}^m w_{m,s}(H_{2m}-H_{2s-1})\). For each fixed \(s\geq1\), central-binomial asymptotics give \(w_{m,s}\to C_s/4^s\) and \((H_{2m}-H_{2s-1})/\log m\to1\). Uniform central-binomial upper and lower bounds imply that on \(1\leq s\leq m/2\),

\[
0\leq w_{m,s}\leq K\frac{C_s}{4^s},
\qquad
0\leq \frac{H_{2m}-H_{2s-1}}{\log m}\leq K
\]

for a universal constant \(K\) and \(m\geq3\). The majorant is summable. On \(s>m/2\), let \(r=m-s\). The same central-binomial bounds give \(w_{m,m-r}\leq K C_r/4^r\), so the sum of these weights is bounded, whereas \(H_{2m}-H_{2s-1}\leq K\); this range contributes \(o(\log m)\). Dominated convergence consequently yields

\[
\lim_{m\to\infty}\frac{m\kappa_m}{\log m}
=\sum_{s=1}^{\infty}\frac{C_s}{4^s}
=\bigl(1-\sqrt{1-4(1/4)}\bigr)/(2(1/4))-1=1.
\]

Together with the first-order identity, this finishes the theorem. In particular, there is no interchange of the fixed-group \(\varepsilon\)-expansion with the large-group limit.

## Verification

The included standalone standard-library program `verify_two_speed_coupon.py` was executed from its saved package source. It passed **137 deterministic assertions**: exhaustive balanced-word enumeration for fast-group sizes up to seven; exact Catalan convolution and three small \(\kappa_m\) values; independent exact rational grouped-count and labelled-clock recursions; comparison to the closed formula for \((m,l)=(1,1)\); first-order checks at small positive rates; equal-rate Catalan identities; and numerical inspections of the log-scale coefficient. The exact check is finite. The proof above, rather than numerical extrapolation, establishes the general statements.

A reproducible command in a standard Python 3 environment is `python verify_two_speed_coupon.py`. No external packages, remote data, simulation seeds or nonlocal files are needed.

## Relationship to prior work

The original two-player coupon competition of Myers and Wilf and its asymptotic solution by Long are **simultaneous discrete-time per-round sampling models**. Their winner-never-behind comparison motivates the present question but is not equivalent to the independent continuous-time exponential-first-arrival model studied here. In particular, the new \(\varepsilon\downarrow0\) perturbation is not an asserted extension of Long's \(b_d\sim2/d\) theorem. The usual Catalan and ballot counting identities, including the equal-rate evaluation \(2/(m+l+1)\), are classical and are not claimed as new.

The present claim concerns the explicit two-speed first derivative, its strictly positive Catalan–harmonic coefficient, and its logarithmic large-fast-group susceptibility. The inspected primary papers contain no statement directly covering those conclusions. This comparison is evidence of a candidate original calculation, not a claim of exhaustive bibliographic priority.

## Limitations

Both collectors must share the same fast/slow rate profile and have independent Poisson coupon streams. The first-order error constant can depend on both group sizes. The theorem says nothing about fixed positive \(\varepsilon\) as the group sizes grow or about the simultaneous-round model. The method does not classify arbitrary vectors of coupon rates or multiple distinct slow-rate scales. Classical weighted ballot enumeration or nonidentical-exponential ordering literature may contain an unrecognized equivalent identity; independent priority verification has not been performed.

## References

1. C. D. Long, *The Ballot Event for Two-Player Coupon Collection: A Renewal–Catalan Asymptotic*, arXiv:2605.09641v1, 10 May 2026. https://arxiv.org/abs/2605.09641
2. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector’s Problem*, arXiv:math/0304229v1, 16 April 2003; *SIAM Journal on Discrete Mathematics* 17 (2003), 1–17. https://arxiv.org/abs/math/0304229
3. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. I, 3rd ed., Wiley, 1968 (classical ballot/reflection principle).
