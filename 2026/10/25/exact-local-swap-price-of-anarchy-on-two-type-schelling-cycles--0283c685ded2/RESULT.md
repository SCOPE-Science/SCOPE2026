# Exact local-swap price of anarchy on two-type Schelling cycles

## Finding

For any integer \(n\ge3\) and any positive integers \(a,b\) with \(a+b=n\), consider the two-type, fully occupied, nearest-neighbor local swap Schelling game on the cycle \(C_n\). Define
\[
 r_0=\min\{a,b,\lfloor n/3\rfloor\},\qquad
 \delta=\begin{cases}
 1&\text{if }n=3r_0\text{ and }\max\{a,b\}<2r_0,\\
 0&\text{otherwise},
 \end{cases}\qquad r_*=r_0-\delta.
\]
The **maximum** number of runs of either color among local swap equilibria is **exactly** \(r_*\), and their minimum social welfare is \(n-2r_*\). The exact local price of anarchy for this specified composition is therefore
\[
 \boxed{\operatorname{LPoA}(C_n;a,b)=\frac{n-2}{n-2r_*}}.
\]
For the balanced twelve-vertex instance \(a=b=6\), the maximum is \(r_*=3\), not \(\lfloor12/3\rfloor=4\): the exact ratio is \(5/3\). This establishes a sharp mod-three obstruction to attaining the elementary run bound.

## Assumptions and scope

The graph \(C_n\) has labeled vertices \(0,\ldots,n-1\), with indices read modulo \(n\). Every vertex contains exactly one agent. Exactly \(a\) agents have type \(A\) and exactly \(b\) have type \(B\). Each agent's utility is the fraction of her two neighbors with her own type; identical-type swaps change no utilities. A pair of **adjacent** agents can swap if and only if **both** agents strictly increase their own utilities. A local equilibrium is a configuration admitting no such swap. Social welfare is the sum of all agent utilities. This is **not** the globally unrestricted swap game and **not** the satisfaction-threshold model with nonstrategic swaps. Both colors occur, so the optimal welfare \(n-2\) is strictly positive.

A monochromatic run is a maximal consecutive cyclic block of vertices of one type. Every nonmonochromatic cyclic configuration has an equal number \(r\ge1\) of runs of types \(A\) and \(B\), hence \(2r\) color-changing edges.

## Proof

**1. Local improving swaps.** Suppose adjacent locations \(i,i+1\) contain unlike colors \(A,B\), and the exterior colors at \(i-1\) and \(i+2\) are \(L,R\). The first agent has no same-type neighbor at \(i+1\), and the second has none at \(i\). After they swap, each acquires exactly one possible matching exterior neighbor. The \(A\)-agent strictly gains if and only if \(R=A\) and \(L\ne A\); the \(B\)-agent strictly gains if and only if \(L=B\) and \(R\ne B\). Both strictly gain exactly when \(L=B\) and \(R=A\). Equivalently, the four cyclic positions \(i-1,i,i+1,i+2\) alternate \(B,A,B,A\). The case \(n=3\) is included: the two exterior positions then coincide, making simultaneous improvement impossible. Thus a configuration is locally stable precisely when it contains no four alternating consecutive vertices; equivalently, no two cyclically adjacent monochromatic runs are both singletons.

**2. Universal run ceiling and equality restriction.** Consider a stable configuration with \(2r\) cyclic monochromatic runs. Mark a run if it has length at least two. Since singleton runs are pairwise nonconsecutive among the \(2r\) run positions, there are at most \(r\) singleton runs; at least \(r\) runs have length at least two. Consequently \(n\ge3r\). Each color occupies at least one vertex per run, hence \(r\le\min\{a,b\}\). Therefore \(r\le r_0\).

If \(n=3r\), equality holds throughout: exactly \(r\) runs are singleton, exactly \(r\) have length two, and the singleton run positions form a maximum independent set in an even cyclic adjacency pattern of length \(2r\). Such a set alternates positions, so all singleton runs have one color and all doubleton runs the other. For \(r=1\), the same conclusion follows directly from the two runs and total length three. Thus equality \(n=3r\) requires \(\{a,b\}=\{r,2r\}\). In particular, when \(n=3r_0\) and \(\max\{a,b\}<2r_0\), the ceiling \(r=r_0\) is impossible and \(r\le r_0-1\).

**3. Constructive sufficiency.** Fix \(r\ge1\) satisfying \(r\le\min\{a,b\}\) and either \(n\ge3r+1\) or \(n=3r\) with \(\{a,b\}=\{r,2r\}\). Put \(\alpha=a-r\) and \(\beta=b-r\). Arrange \(r\) alternating runs \(A_1,B_1,\ldots,A_r,B_r\) around the cycle. If \(\alpha\ge r\), choose every \(A\)-run of length at least two and distribute the remaining \(A\)-vertices and all extra \(B\)-vertices arbitrarily; no two singleton runs touch. The symmetric construction applies if \(\beta\ge r\). This includes the permitted \(n=3r\) equality cases.

Otherwise \(\alpha<r\) and \(\beta<r\). The remaining hypothesis gives \(\alpha+\beta=n-2r\ge r+1\), so \(\alpha\ge1\), \(\beta\ge1\) and \(\beta\ge r-\alpha+1\). Give \(A_i\) length two for \(1\le i\le\alpha\), length one for \(i>\alpha\). Give \(B_i\) length two for \(\alpha\le i\le r\), length one for \(i<\alpha\); place the surplus \(\beta-(r-\alpha+1)\ge0\) vertices in the already-long run \(B_r\). The \(A\)-lengths sum to \(a\) and the \(B\)-lengths to \(b\). Every singleton \(A_i\) borders long \(B\)-runs, and every singleton \(B_i\) borders long \(A\)-runs. The configuration is therefore stable with exactly \(r\) runs of each type. Taking \(r=r_0\) when \(\delta=0\), or \(r=r_0-1\) when \(\delta=1\), constructs the claimed extremal equilibrium. The latter has \(r\ge1\), since \(n=3r_0\) and \(\delta=1\) forces \(r_0\ge2\).

**4. Welfare and ratio.** Each monochromatic edge contributes one to the sum of its endpoint utilities (one half from each endpoint), while a bichromatic edge contributes zero. A configuration with \(r\) runs per color has exactly \(2r\) bichromatic edges, hence welfare \(W=n-2r\). Every two-color configuration has at least two bichromatic edges, and grouping each color into one contiguous block attains \(W_{\mathrm{opt}}=n-2\). The maximum attainable stable run count from steps 2–3 gives the minimum equilibrium welfare \(n-2r_*\) and the stated ratio. \(\square\)

## Verification

The accompanying standalone `verify.py` directly evaluates each agent's pre- and post-swap utilities; it does not use the four-position lemma when classifying equilibria. Exhaustive enumeration checks all 131,036 nonmonochromatic binary colorings at sizes \(3\le n\le16\), grouping them into 119 fixed-composition classes and confirming the maximum run count and the lemma independently. A separate constructive sweep tests 6,215 composition instances at sizes \(3\le n\le112\), verifies stable witnesses and their run counts, and reproduces `certificate.json` exactly. These finite checks test the formula and construction; the unrestricted quantifiers are established by the preceding proof.

For explicit examples, the twelve-vertex balanced instance has welfare range from \(6\) at a worst local equilibrium to \(10\) at a social optimum; the thirteen-vertex composition \((6,7)\) permits four run pairs and a ratio of \(11/5\). Witness color words appear in `certificate.json`, using symbols `0` for type \(A\) and `1` for type \(B\).

## Relationship to prior work

Brandt, Immorlica, Kamath and Kleinberg (2012) analyzed segregation on one-dimensional graphs under a different stochastic swapping mechanism; its model does not imply an exact two-sided-profit local-equilibrium welfare classification. Bilò, Bilò, Lenzner and Molitor (MFCS 2020; expanded 2022 open-access article) defined the exact local swap game considered here. Their Theorem 13 gives a sharp local price-of-anarchy bound when the larger type has at least twice as many agents, but only an upper bound in the remaining case; the authors explicitly assert tightness only in the former regimes. The present result supplies both a matching construction where possible and the precise congruence/composition obstruction otherwise, thereby sharpening that theorem's remaining non-tight range.

No claim is made that local-swap welfare or the broad run-count ceiling \(r\le\lfloor n/3\rfloor\) is new independently. The claim is the all-composition **exact attainability criterion and sharp local price-of-anarchy classification**. Search-based novelty evidence is not a proof of uniqueness; equivalent formulations outside the inspected sources remain a bibliographic risk.

## Limitations

The result requires two nonempty types, degree-two cycle topology, complete occupation, identical fraction-of-neighbor utility, **mutual strict** payoff improvement, and swaps restricted to adjacent vertices. It does not cover paths, multiple types, nonlocal exchanges, unequal vertex weights, vacancies, alternative tolerance utilities or stochastic movement protocols. Numerical experiments alone do not establish the infinite result, and no external independent scientific audit has been performed.

## References

1. C. Brandt, N. Immorlica, G. Kamath, R. Kleinberg, *An Analysis of One-Dimensional Schelling Segregation*, arXiv:1203.6346, first publicly submitted 2012-03-28, https://arxiv.org/abs/1203.6346.
2. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Topological Influence and Locality in Swap Schelling Games*, MFCS 2020, LIPIcs 170, article 15, DOI 10.4230/LIPIcs.MFCS.2020.15, https://doi.org/10.4230/LIPIcs.MFCS.2020.15.
3. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Topological influence and locality in swap schelling games*, Autonomous Agents and Multi-Agent Systems 36, article 47 (2022), DOI 10.1007/s10458-022-09573-7, https://doi.org/10.1007/s10458-022-09573-7; Theorem 13 and its proof.
