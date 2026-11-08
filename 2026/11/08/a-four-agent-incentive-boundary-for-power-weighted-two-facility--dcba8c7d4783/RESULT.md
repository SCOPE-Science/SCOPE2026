# A four-agent incentive boundary for power-weighted two-facility lotteries

## Finding

Consider the power-weighted pair mechanism \(\mathsf{G}_{\alpha}\), which selects an unordered pair of reported agents \(\{i,j\}\) with probability proportional to \(|z_i-z_j|^{\alpha}\), for a fixed real exponent \(\alpha>0\), and opens two facilities at their reports. Agents incur the distance from their *true* position to the nearer facility. The familiar distance-weighted Global Pair mechanism is \(\mathsf{G}_1\).

For the four-agent profile with one strategic agent at \(0\) and three fixed agents at \((1,1,-1)\), the following hold:

1. For every real \(0<\alpha\le2\), truthful reporting is a best response to every possible real report, on this profile.
2. For every real \(\alpha\ge3\), reporting \(-1/5\) strictly improves the strategic agent's expected cost. In particular \(\mathsf{G}_{\alpha}\) is *not* strategyproof on the real line for any \(\alpha\ge3\). At \(\alpha=3\), the truthful cost is \(16/19\), the deviating cost is \(164/195\), and the exact gain is \(4/3705\).
3. For \(\alpha=3\), **all** profitable reports on this profile form precisely the open interval \((-t_+,-t_-)\), where \(t_-\approx0.1379015856\) and \(t_+\approx0.3952288519\) are the two roots in \((0,1)\) of \(-19t^3-155t^2+87t-9=0\).

The first assertion is local to the displayed profile; it makes **no** universal strategyproofness claim for \(\mathsf{G}_2\) or for exponents between \(2\) and \(3\).

## Assumptions and scope

There are four indexed agents, even when two occupy the same location. The first agent's true position is zero; the others truthfully report \(1,1,-1\). The first agent may submit any \(r\in\mathbb R\); her true position does not change with the report. A pair consists of two distinct *indices*. Coincident reports have pair weight zero but cause no ambiguity because the fixed agents at \(1\) and \(-1\) have positive separation. The mechanism's normalization is strictly positive for all reports in this setting. Randomization is over pairs; facility costs are nearest-facility absolute distances, without transfers. Statements hold for all real exponents in the specified ranges, not just integers.

## Proof

Write \(A_{\alpha}=2^{\alpha+1}\), the total pair weight among the three nonstrategic agents: the two pairs connecting \(1\) to \(-1\) have weights \(2^{\alpha}\) and the pair between the two agents at \(1\) has weight zero. A pair consisting of two fixed agents yields cost \(1\) to the strategic agent. For a report \(r\), set
\[
S_{\alpha}(r)=2|1-r|^{\alpha}+|1+r|^{\alpha}.
\]
A pair containing the strategic agent yields true cost \(\min\{|r|,1\}\). Consequently, when \(|r|\le1\), the expected cost is exactly
\[
C_{\alpha}(r)=\frac{A_{\alpha}+|r|S_{\alpha}(r)}{A_{\alpha}+S_{\alpha}(r)},
\qquad C_{\alpha}(0)=\frac{A_{\alpha}}{A_{\alpha}+3}.
\]
For \(|r|\ge1\), every selected pair has true cost \(1\), which is strictly worse than the truthful cost. For \(0<|r|<1\), cross multiplication by positive denominators shows that \(C_{\alpha}(r)<C_{\alpha}(0)\) **if and only if**
\[
S_{\alpha}(r)\left(1-|r|-\frac{3|r|}{A_{\alpha}}\right)>3. \tag{1}
\]

**No profitable deviation for \(0<\alpha\le2\).** Put \(t=|r|\), and \(\eta_{\alpha}(t)=1-t(1+3/A_{\alpha})\). Since \(A_{\alpha}\le8\), we have \(\eta_{\alpha}(t)\le\eta_2(t)=1-11t/8\). If \(\eta_{\alpha}(t)\le0\), (1) fails. Otherwise \(0<\eta_{\alpha}(t)\le\eta_2(t)\). For fixed \(-1<r<1\), \(S_{\alpha}(r)\) is a positive sum of exponentials in \(\alpha\), hence is convex; on \(0\le\alpha\le2\) it is at most \(\max\{3,S_2(r)\}\), extending to \(\alpha=0\) only as an auxiliary continuous endpoint. If \(S_2(r)\le3\), then \(S_{\alpha}(r)\eta_{\alpha}(t)<3\). If \(S_2(r)>3\), then
\[
S_{\alpha}(r)\eta_{\alpha}(t)\le S_2(r)\eta_2(t)<3,
\]
because direct expansion gives, for \(0<t<1\),
\[
\begin{aligned}
S_2(-t)\eta_2(t)-3&=-\frac{t}{8}(17-2t+33t^2)<0,\\
S_2(t)\eta_2(t)-3&=-\frac{t}{8}(49-46t+33t^2)<0.
\end{aligned}
\]
Both parentheses are strictly positive on \([0,1]\). Thus no report improves on truth for \(0<\alpha\le2\).

**All \(\alpha\ge3\) fail strategyproofness.** Take \(r=-1/5\). Then
\[
S_{\alpha}(-1/5)=2(6/5)^{\alpha}+(4/5)^{\alpha},
\quad\eta_{\alpha}(1/5)=\frac45-\frac{3}{5\cdot2^{\alpha+1}}.
\]
The second factor is positive and strictly increasing for \(\alpha\ge3\). The first is strictly increasing for \(\alpha\ge0\), since
\[
\frac{dS_{\alpha}}{d\alpha}
=2(6/5)^{\alpha}\log(6/5)+(4/5)^{\alpha}\log(4/5)
\ge2\log(6/5)-\log(5/4)>0.
\]
(The displayed lower bound holds for nonnegative \(\alpha\).) At \(\alpha=3\), their product exceeds three by \(16/625\). Equation (1) then proves improvement for every \(\alpha\ge3\). Direct exact arithmetic gives \(C_3(0)=16/19\) and \(C_3(-1/5)=164/195\).

**Complete cubic best-response interval.** For \(\alpha=3\), \(\eta_3(t)=1-19t/16\). Expanding (1), for \(r=-t\in(-1,0)\), gives
\[
S_3(-t)\eta_3(t)-3=\frac{t}{16}\bigl(-9+87t-155t^2-19t^3\bigr).
\]
The cubic \(P(t)=-9+87t-155t^2-19t^3\) is strictly concave on \([0,1]\), since \(P''(t)=-310-114t<0\), with \(P(0)=-9<0\), \(P(1)=-96<0\), and \(P(1/4)=177/64>0\). Thus it has exactly two roots inside \((0,1)\), and is positive exactly between them. For \(r=t\in(0,1)\), the corresponding difference equals
\[
\frac{t}{16}\bigl(-105+201t-187t^2+19t^3\bigr)<0,
\]
since the cubic in parentheses is at most \(-105+201t-168t^2<0\) on \([0,1]\) (the quadratic has a negative discriminant and negative leading coefficient). Reports outside \((-1,1)\) were excluded above, finishing the exact characterization.

## Verification

The accompanying `verify_power_pair.py` independently enumerates all six indexed unordered pairs using exact rational arithmetic, checks \(805\) reported-cost evaluations against the closed form, checks \(322\) rational best-response comparisons at exponents \(1,2\), verifies exact costs and the \(4/3705\) strict improvement, and checks cubic signs and \(1001\) positive-report inequalities. Run `python verify_power_pair.py` from a directory containing this document and the script. These tests are finite corroboration only. The convexity and monotonicity arguments, and exact polynomial sign analysis above, are the actual proofs for the infinite continuous ranges.

## Relationship to prior work

Ma and Peng (2026) introduce the Global Pair rule with weights proportional to distance and prove its strategyproofness on Ptolemaic spaces. Chan, Lin and Wang (2026) independently study the same linear-distance pair lottery as Pairwise-Distance and prove its strategyproofness on those spaces. Their proved results specifically use linear distance weights; they do not imply incentive compatibility for the nonlinear weights studied here. The present claim exposes the precise best-response structure at exponent three on a natural duplicated-location four-agent profile and an entire real-exponent region \(\alpha\ge3\) of incentive failure, while establishing local immunity for \(0<\alpha\le2\). Its interest lies in the failure of a tempting design modification: increasingly favoring distant report pairs is not innocuous for truthfulness.

## Limitations

The no-deviation result for exponents up to two is only for one specified profile and deviating agent. We do not determine the global strategyproofness boundary for \(2<\alpha<3\), nor claim minimality in the number of agents or locations for all exponents. No efficiency approximation bound is asserted for nonlinear mechanisms. Originality is assessed against identified accessible work and indexed searches; further equivalent literature may exist. Independent validation has not been performed.

## References

- Mengfan Ma and Bo Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, arXiv:2608.09061, first public August 10, 2026. https://arxiv.org/abs/2608.09061
- Hau Chan, Jianan Lin and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first public August 23, 2026. https://arxiv.org/abs/2608.22484
