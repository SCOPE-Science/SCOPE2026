# The sharp five-agent approximation factor of distance-proportional two-facility sampling on the line

## Finding

For exactly five agents, with arbitrary (possibly coincident) locations on the real line, the Global Pair, also called Pairwise-Distance, rule selects two distinct agent *indices* with probability proportional to the distance between their reports, and opens facilities at their reports. Relative to the **unrestricted optimal two-facility social cost**, its expected social cost satisfies
\[
\mathbb E[\operatorname{SC}]\le \frac94\operatorname{OPT}_2.
\]
The factor \(9/4\) is the exact nonattained supremum over positive-optimum profiles. For the family of five reports \((0,T,T+1,T+1,T+2)\), \(T\ge2\), the ratio is
\[
\frac{18T+22}{8T+20}\xrightarrow[T\to\infty]{}\frac94.
\]
The guarantee concerns **exactly five agents on the line**, not arbitrary metric spaces or larger electorates. In this setting, the source mechanism is known to be strategyproof in expectation on the line. The assertion here is its sharp five-agent efficiency factor, not a new incentive proof.

## Assumptions and scope

Sort the reports as \(x_1\le x_2\le x_3\le x_4\le x_5\), and put \(a=x_2-x_1\), \(b=x_3-x_2\), \(c=x_4-x_3\), \(d=x_5-x_4\), all nonnegative. For any two facility positions \(f,g\in\mathbb R\), define
\[
\operatorname{SC}(f,g)=\sum_{h=1}^{5}\min\{|x_h-f|,|x_h-g|\},\quad
\operatorname{OPT}_2=\min_{f,g\in\mathbb R}\operatorname{SC}(f,g).
\]
Set \(Z=\sum_{i<j}|x_j-x_i|=4a+6b+6c+4d\). For \(Z>0\), select pair \(\{i,j\}\) with probability \((x_j-x_i)/Z\). For \(Z=0\), every client is co-located and the social cost is zero by convention. Define the unnormalized expected-cost numerator
\[
N=\sum_{i<j}(x_j-x_i)\sum_{h=1}^{5}\min\{|x_h-x_i|,|x_h-x_j|\},\quad \mathbb E[\operatorname{SC}]=N/Z.
\]
The choice of distinct agent indices accommodates repeated reports; pairs with zero distance receive zero probability. There are no facility-opening costs.

## Proof

**Optimal social cost.** Two optimal real-line facilities induce a partition into consecutive groups, each served by its median. The four possible nontrivial cuts therefore give
\[
\operatorname{OPT}_2=\min\{T_1,T_2,T_3,T_4\},\quad
T_1=b+2c+d,\quad T_2=a+c+d,\quad
T_3=a+b+d,\quad T_4=a+2b+c.
\]
This also holds for coincident reports, since an unused center may be relocated without increasing cost.

**Two global polynomial upper envelopes.** For a sampled pair \((i,j)\), each unselected client \(h\) contributes \(\min\{p,q\}\), where \(p=|x_h-x_i|\) and \(q=|x_h-x_j|\). Replacing it by either \(p\) or \(q\) gives a valid upper bound, without any case restrictions. All terms except the ten below have a coefficientwise smaller choice. The table specifies two assignments for the ten incomparable choices; index triples are \((i,j;h)\), and each cell gives the selected **first** (\(p\)) or **second** (\(q\)) distance.

| \((i,j;h)\) | Envelope \(U_1\) | Envelope \(U_2\) |
|---|---|---|
| \((1,3;2)\) | \(q\) | \(p\) |
| \((1,4;2)\) | \(q\) | \(p\) |
| \((1,4;3)\) | \(q\) | \(q\) |
| \((1,5;2)\) | \(q\) | \(p\) |
| \((1,5;3)\) | \(q\) | \(q\) |
| \((1,5;4)\) | \(q\) | \(q\) |
| \((2,4;3)\) | \(p\) | \(q\) |
| \((2,5;3)\) | \(p\) | \(q\) |
| \((2,5;4)\) | \(p\) | \(q\) |
| \((3,5;4)\) | \(p\) | \(p\) |

Multiplying the chosen service distances by the sampled pair distances and summing yields the following polynomial **upper bounds**, valid simultaneously for all nonnegative gaps:
\[
\begin{aligned}
N\le U_1={}&9ab+12ac+9ad+6b^2+18bc+14bd+6c^2+13cd+3d^2,\\
N\le U_2={}&3a^2+9ab+12ac+9ad+12bc+12bd+5c^2+13cd+4d^2.
\end{aligned}
\]

**Two nonnegative certificates.** Direct expansion, with no division and no positivity assumptions beyond nonnegative gaps, gives
\[
\begin{aligned}
9ZT_1-4U_1={}&24ac+30b^2+90bc+34bd+84c^2+74cd+24d^2\ge0,\\
9ZT_2-4U_2={}&24a^2+18ab+42ac+36ad+6bc+6bd+34c^2+38cd+20d^2\ge0.
\end{aligned}
\]
Consequently \(4N\le9ZT_1\) and \(4N\le9ZT_2\). Reflecting all reports exchanges \((a,b,c,d)\) with \((d,c,b,a)\) but leaves \(N\) and \(Z\) unchanged, and exchanges \(T_1,T_4\) and \(T_2,T_3\). Applying the same certificates to the reflected profile yields \(4N\le9ZT_3\) and \(4N\le9ZT_4\). Taking the minimum proves
\[
4N\le9Z\operatorname{OPT}_2,
\]
for all nonnegative gaps. If \(Z=0\), both social costs are zero; if \(\operatorname{OPT}_2=0\) but \(Z>0\), the inequality forces \(N=0\). For \(\operatorname{OPT}_2>0\), the certificates (and their reflections) are strictly positive in the relevant cases, so the approximation ratio is strictly below \(9/4\) on every finite positive-optimum profile.

**Sharpness.** With gaps \((a,b,c,d)=(T,1,0,1)\), \(T\ge2\), direct enumeration of the ten weighted sampled pairs gives
\[
Z=4T+10,\quad N=18T+22,\quad \operatorname{OPT}_2=2.
\]
Thus the ratio is \((18T+22)/(8T+20)\), and the shortfall from \(9/4\) is exactly \(23/(8T+20)>0\), tending to zero. If strictly distinct reports are required, a sufficiently small positive perturbation of the repeated middle report retains ratios arbitrarily near \(9/4\) by continuity.

## Verification

The standalone standard-library Python script `verify.py` reconstructs both upper envelopes from the ten endpoint choices, multiplies symbolic coefficient vectors in integer arithmetic, checks every coefficient of the two nonnegative quadratic slack identities, and independently enumerates exact sampled-pair and optimal facility costs for all \(13^4=28{,}561\) integer gap quadruples between zero and twelve. It also checks reflected profiles, strictness when optimum is positive, and \(158\) exact rational sharpness instances. Invoke `python3 verify.py` in the same directory. The polynomial identities, not the finite tests, establish the universal continuous assertion.

## Relationship to prior work

Ma and Peng (2026) introduced Global Pair, proved its general factor-four guarantee, and its strategyproofness on Ptolemaic spaces. Chan, Lin and Wang (2026) independently analyzed the Pairwise-Distance name and general factor four. Jia (2026) studied the line-based Product-Gap extension, whose two-facility specialization is the same mechanism, with general factor four. Those universal bounds do not determine the sharp factor for five reports. Sharp bounds for populations of three and four reports do not directly determine the first five-report case, where there are four possible contiguous optimum cuts and ten genuine nearest-facility comparisons. This theorem proves the five-report line boundary \(9/4\); it does not claim the mechanism definitions or general bounds as new.

At five reports, the deterministic strategyproof lower bound \(n-2=3\) of Fotakis and Tzamos (for \(n\ge5\)) contrasts with this strategyproof randomized mechanism's sharp \(9/4\) factor. This makes the small-market constant a substantive efficiency comparison rather than an arbitrary numeric slice.

## Limitations

Only five agents, two facilities, real-line distance, utilitarian nearest-facility cost, and this particular distance-weighted sampling rule are covered. We do not prove a five-agent bound for arbitrary metric spaces, the optimal approximation among all randomized mechanisms, or any behavior for six or more agents. The factor is a supremum rather than a finite-profile maximum. Primary literature and available mathematical research records were compared, but an equivalent unindexed derivation remains possible. There has been no independent external audit of the proof or publication priority.

## References

1. M. Ma and B. Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, arXiv:2608.09061v1, first public 2026-08-10, https://arxiv.org/abs/2608.09061.
2. H. Chan, J. Lin and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484v1, first public 2026-08-23, https://arxiv.org/abs/2608.22484.
3. J. Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633v1, first public 2026-08-20, https://arxiv.org/abs/2608.19633.
4. D. Fotakis and C. Tzamos, *On the Power of Deterministic Mechanisms for Facility Location Games*, arXiv:1207.0935v1, first public 2012-07-04, https://arxiv.org/abs/1207.0935.
