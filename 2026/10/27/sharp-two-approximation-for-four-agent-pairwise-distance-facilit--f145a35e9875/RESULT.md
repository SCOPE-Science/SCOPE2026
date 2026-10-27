# Sharp two-approximation for four-agent pairwise-distance facility selection

## Finding

For exactly four agents at distinct positions \(x_1<x_2<x_3<x_4\) on the real line, consider the **Pairwise-Distance** (also called **Global Pair** or the two-facility **Product-Gap**) mechanism: select an unordered pair of distinct agents \(\{i,j\}\) with probability proportional to \(x_j-x_i\), and open one facility at each selected position. Every agent incurs distance to the closer opened facility. Among all distinct four-agent profiles, the sharp expected-social-cost approximation ratio is

\[
\boxed{\sup_{x_1<x_2<x_3<x_4}\frac{\mathbb E[C]}{\mathrm{OPT}}=2.}
\]

The inequality \(\mathbb E[C]<2\mathrm{OPT}\) is strict for every admissible finite profile; equality is approached only in a limiting sense. This is an exact four-agent refinement of the known unrestricted-population factor \(4\) guarantee for the same mechanism, not a new incentive-compatibility theorem.

## Assumptions and scope

There are precisely four equally weighted agents, one at each of four distinct real coordinates, and precisely two uncapacitated facilities may be placed anywhere on the line for the unconstrained optimum. Agents report their true coordinates. Both the mechanism and its cost function use ordinary absolute distance. Translation and positive rescaling do not change the approximation ratio. Define the positive consecutive gaps

\[
a=x_2-x_1,\qquad b=x_3-x_2,\qquad c=x_4-x_3.
\]

For \(i<j\), the sampled-pair weight is \(x_j-x_i\), with total normalization

\[
Z=\sum_{i<j}(x_j-x_i)=3a+4b+3c>0.
\]

Write \(C_{ij}=\sum_{t=1}^{4}\min\{|x_t-x_i|,|x_t-x_j|\}\) and \(N=\sum_{i<j}(x_j-x_i)C_{ij}\), so \(\mathbb E[C]=N/Z\).

## Proof

**Exact cost identity.** Directly enumerating the six unordered pairs yields, in the order \(12,13,14,23,24,34\), the sampled costs

\[
2b+c,\quad \min\{a,b\}+c,\quad
\min\{a,b+c\}+\min\{a+b,c\},\quad
a+c,\quad a+\min\{b,c\},\quad a+2b.
\]

Consequently,

\[
\begin{aligned}
N={}&a(2b+c)+(a+b)(\min\{a,b\}+c)\\
&+(a+b+c)(\min\{a,b+c\}+\min\{a+b,c\})\\
&+b(a+c)+(b+c)(a+\min\{b,c\})+c(a+2b).
\end{aligned}
\]

**Unrestricted two-facility optimum.** Assign every agent to its closest facility, choosing contiguous clusters on the line; moving each facility to a median of its assigned cluster never increases cost. The three possible positions of the intercluster cut, after the first, second, or third agent, give optimal costs \(b+c\), \(a+c\), and \(a+b\), respectively. Thus

\[
\mathrm{OPT}=\min\{a+b,a+c,b+c\}>0.
\]

**Strict upper bound.** Reflecting the line interchanges \(a\) and \(c\), so suppose \(a\le c\). Define the positive-gap certificate \(\Delta=2\mathrm{OPT}\,Z-N\). All possibilities are covered by the following elementary substitutions into the exact cost identity. Cases with equality on a boundary are consistent.

1. If \(a\le b\le c\) and \(c\ge a+b\), then \(\Delta=3a^2+6ab+6b^2\). If \(a\le b\le c\) and \(c\le a+b\), then \(\Delta=4a^2+8ab+7b^2-c^2\ge3a^2+6ab+6b^2\), using \(c^2\le(a+b)^2\).
2. If \(b\le a\le c\) and \(c\ge a+b\), then \(\Delta=4a^2+6ab+5b^2\). If \(b\le a\le c\) and \(c\le a+b\), then \(\Delta=5a^2+8ab+6b^2-c^2\ge4a^2+6ab+5b^2\).
3. If \(a\le c\le b\), then \(\Delta=4a^2+2ab+6ac+2bc+4c^2\).

In every case \(\Delta>0\) because \(a,b,c>0\). Since \(Z\mathrm{OPT}>0\), this establishes \(\mathbb E[C]/\mathrm{OPT}<2\) for every admissible profile.

**Sharpness and nonattainment.** For \(a=b=1\) and \(c=L\ge2\), direct substitution gives

\[
\frac{\mathbb E[C]}{\mathrm{OPT}}
=\frac{12L+13}{6L+14}
=2-\frac{15}{6L+14}\longrightarrow2
\qquad(L\to\infty).
\]

Every such profile has finite distinct coordinates, while strict positivity of \(\Delta\) excludes attainment. The mechanism's rare selection of a pair excluding the distant fourth agent contributes a nonvanishing amount to expected cost even as its probability tends to zero, explaining the limiting inefficiency.

## Verification

The standalone standard-library script `verify.py` computes the six weighted pair costs independently of the displayed formula, checks the unrestricted optimum by enumerating all report-pair facility placements, verifies reflection symmetry and strict two-approximation for all integer triples \(1\le a,b,c\le20\), and checks the sharpness family's closed form with exact rational arithmetic. Running `python verify.py` passed **32,015 exact-rational assertions**. The continuum theorem relies on the displayed algebraic case certificate, not on finite enumeration. There is no claim of an exhaustive computation over real profiles.

## Relationship to prior work

Ma and Peng (arXiv:2608.09061, first public 10 August 2026) introduce Global Pair and prove strategyproofness on Ptolemaic spaces, the unrestricted-population factor \(4\), and improvements from fixed mixtures. Chan, Lin, and Wang (arXiv:2608.22484, first public 23 August 2026) independently analyze the same pairwise-distance mechanism and mixtures, likewise deriving the factor \(4\) across arbitrary population sizes. Jia's Product-Gap rule (arXiv:2608.19633, first public 20 August 2026) reduces to this same rule for two facilities and gives the global factor \(4\). Those global approximation statements do not imply the sharp factor \(2\) when the electorate is held to exactly four distinct agents, and the principal inspected texts do not state that finite-electorate frontier. The classical deterministic Two-Extremes mechanism also has a factor \(2\) at four agents, but it selects different facilities and its guarantee does not imply the claimed guarantee for distance-weighted random pairs.

## Limitations

The theorem concerns exactly four equally weighted, distinct, truthful reports on the real line and the unmixed two-facility Pairwise-Distance rule. It does not claim the factor for larger populations, co-located reports with multiplicities, arbitrary metric spaces, alternative facility counts, or strategic deviations. It does not replace existing incentive proofs. An equivalent result in unindexed literature or in inaccessible portions of a relevant manuscript remains a publication-priority risk; no independent audit has been performed.

## References

- Mengfan Ma and Bo Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, arXiv:2608.09061, 10 August 2026. https://arxiv.org/abs/2608.09061
- Jianhao Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633, 20 August 2026. https://arxiv.org/abs/2608.19633
- Hau Chan, Jianan Lin, and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, 23 August 2026. https://arxiv.org/abs/2608.22484
