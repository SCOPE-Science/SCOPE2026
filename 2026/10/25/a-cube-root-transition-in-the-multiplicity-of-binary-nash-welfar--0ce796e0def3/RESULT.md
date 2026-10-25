# A cube-root transition in the multiplicity of binary Nash-welfare allocations

## Finding

Consider two agents with independent binary approvals for each of \(m\) labeled indivisible goods. An approval equals one with probability \(p_m\), independently over goods and agents. Let \(K_m\) be the number of **distinct minimally complete, non-redundant maximum-Nash-welfare allocations**, *before* any deterministic tie-breaking. The Nash-welfare convention first maximizes the number of agents with positive utility and then their product; it coincides here with leximin. Goods approved by neither agent are unallocated.

Write \(a,b,c\) for the numbers of goods approved only by agent one, only by agent two, and by both, respectively, and let \(d=a-b\). Then, for every approval profile,
\[
K_m=\sum_{t=0}^{c}\binom{c}{t}\mathbf 1\{|d-c+2t|\le1\}
+\mathbf 1\{|d|>c+1\},
\qquad K_m>1\iff |d|<c.
\]
The sum is interpreted as one term at \(t=0\) when \(c=0\); the second term handles profiles whose best achievable utility difference exceeds one.

There is a sharp sparse-approval threshold. For arbitrary \(p_m\in[0,1]\),
\[
mp_m^3\to0\quad\Longrightarrow\quad\Pr(K_m>1)\to0,
\qquad
mp_m^3\to\infty\quad\Longrightarrow\quad\Pr(K_m>1)\to1.
\]
For every fixed \(\lambda>0\), in the critical window \(p_m=\lambda m^{-1/3}\),
\[
\Pr(K_m>1)\longrightarrow
2\Phi\left(\frac{\lambda^{3/2}}{\sqrt2}\right)-1
=\operatorname{erf}\left(\frac{\lambda^{3/2}}2\right).
\]
Here \(\Phi\) is the standard-normal distribution function. In particular, the limiting probability is \(\operatorname{erf}(1/2)=0.520499877813\ldots\) at \(\lambda=1\).

The transition also has a **critical multiplicity-entropy law**. Put \(h(u)=-u\log u-(1-u)\log(1-u)\) for \(0<u<1\), extended continuously by \(h(0)=h(1)=0\). If \(Z\) is standard normal, then
\[
\frac{\log K_m}{m^{1/3}}\ \xrightarrow{\ d\ }\ W_\lambda,
\qquad
W_\lambda=
\begin{cases}
\lambda^2h\!\left(\frac12-\frac{Z}{\sqrt2\lambda^{3/2}}\right),
 & |Z|<\lambda^{3/2}/\sqrt2,\\
0,& |Z|\ge\lambda^{3/2}/\sqrt2.
\end{cases}
\]
Thus the critical limiting entropy has a positive point mass at zero and a nondegenerate positive component. The theorem counts allocations of *labeled* goods, not distinct utility vectors.

## Assumptions and scope

The two agents are labeled and have equally weighted, additive, nonnegative, \(\{0,1\}\)-valued utilities. Approval indicators are iid Bernoulli with parameter \(p_m\), independent between agents and across goods. The number \(m\) tends to infinity. Minimal completeness requires every approved good to be assigned, and every completely unapproved good to remain unassigned; non-redundancy requires each allocated good to go to an agent approving it. Both conditions are essential for this count: assigning completely unapproved goods arbitrarily would create irrelevant multiplicity.

For zero utility products, the standard maximum-Nash-welfare refinement first maximizes the number of agents receiving strictly positive utility, then the product of those positive utilities. For two agents and binary additive valuations this agrees with lexicographic maximization of the sorted utility pair. **No** lexicographic priority over agents or goods is imposed to eliminate ties. The claim is only for the complete correspondence of cleaned optimal allocations, not the unique output of any preselected tie-breaking mechanism.

## Proof

**1. Exact reduction.** A minimally complete, non-redundant allocation necessarily gives the \(a\) exclusive goods to agent one and the \(b\) exclusive goods to agent two. Of the \(c\) commonly approved goods, let \(t\) go to agent one and \(c-t\) to agent two. Then its utilities are \((a+t,b+c-t)\), whose sum is \(a+b+c\), independently of \(t\). Maximizing the sorted utility vector therefore amounts to minimizing the absolute utility difference \(|a-b-c+2t|\). The minimizing values of \(t\) are either the nearest feasible integer(s) to \((c-d)/2\), or one boundary integer when that point lies outside \([0,c]\). When \(|d|\le c+1\), the minimum difference is zero or one; the allocations for each minimizing \(t\) are exactly the \(\binom{c}{t}\) subsets. When \(|d|>c+1\), the unique minimizer is an endpoint and represents one allocation. This gives the displayed finite count, including \(c=0\).

The minimizing endpoint is unique when \(|d|\ge c\). If \(|d|<c\), either an interior minimizing \(t\) exists, whose binomial coefficient exceeds one (for \(c\ge2\)), or \(c=1,d=0\), when both endpoints tie. Thus \(K_m>1\) holds exactly when \(|d|<c\).

**2. Random counts.** Let \(C_m=c\) and \(D_m=a-b\). For a single good the corresponding increments \((\Delta D,\Delta C)\) take values \((1,0),(-1,0),(0,1),(0,0)\) with probabilities \(p_m(1-p_m),p_m(1-p_m),p_m^2,(1-p_m)^2\), respectively. Independence across goods yields
\[
\mathbb E C_m=mp_m^2,\qquad
\operatorname{Var}(C_m)=mp_m^2(1-p_m^2),\qquad
\mathbb E D_m=0,\qquad
\operatorname{Var}(D_m)=2mp_m(1-p_m).
\]
The event to be studied is precisely \(\{|D_m|<C_m\}\).

**3. Subcritical and supercritical regimes.** If \(mp_m^3\to0\), then \(p_m\to0\). Along any subsequence with bounded \(mp_m\), \(\mathbb E C_m=mp_m^2\to0\), so the event probability vanishes. Along any subsequence with \(mp_m\to\infty\), the bounded-increment central limit theorem gives \(D_m/\sqrt{mp_m}\Rightarrow N(0,2)\), while Markov's inequality gives \(C_m/\sqrt{mp_m}\to0\) in probability because \(\mathbb E[C_m/\sqrt{mp_m}]=\sqrt{mp_m^3}\to0\). Hence the event probability again vanishes. This subsequence argument covers arbitrary parameter sequences.

If \(mp_m^3\to\infty\), then \(mp_m^2\to\infty\). Chebyshev's inequality yields \(C_m/(mp_m^2)\to1\) in probability. Furthermore
\[
\mathbb E\left[\left(\frac{D_m}{mp_m^2}\right)^2\right]
=\frac{2(1-p_m)}{mp_m^3}\to0.
\]
Therefore \(\Pr(|D_m|<C_m)\to1\).

**4. Critical probability.** With \(p_m=\lambda m^{-1/3}\), Chebyshev gives \(C_m/m^{1/3}\to\lambda^2\) in probability. A bounded-increment triangular-array central limit theorem, using \(\operatorname{Var}(D_m)\sim2\lambda m^{2/3}\), gives \(D_m/m^{1/3}\Rightarrow\sqrt{2\lambda}\,Z\). The boundary event \(|\sqrt{2\lambda}Z|=\lambda^2\) has probability zero, so the continuous mapping theorem proves
\[
\Pr(K_m>1)\to\Pr\left(|Z|<\frac{\lambda^{3/2}}{\sqrt2}\right),
\]
which is the claimed error-function expression.

**5. Critical entropy.** For every \(c\ge1\) and \(0\le t\le c\), the elementary method-of-types estimate
\[
\frac{e^{c h(t/c)}}{c+1}\le\binom{c}{t}\le e^{c h(t/c)}
\]
holds, including endpoints. The exact optimum has at most two adjacent maximizing choices of \(t\), so replacing \(\log K_m\) by \(c\,h(t/c)\) for either such maximizer incurs at most \(O(\log(c+1))\) error. On \(\{|D_m|<C_m\}\), any maximizing \(t\) obeys \(t/C_m=(1-D_m/C_m)/2+O(1/C_m)\). Since \(C_m/m^{1/3}\to\lambda^2>0\), the entropy bound and joint convergence from step 4 give the positive branch of \(W_\lambda\). On the complementary event \(K_m=1\), so its logarithm is zero. The entropy approaches zero continuously as \(|D_m|/C_m\to1\); Gaussian probability assigns no mass to this boundary. The extended continuous mapping theorem finishes the distributional claim.

## Verification

The standalone standard-library Python script `verify.py` independently enumerates all \(4^m\) approval profiles for each \(m=0,1,\ldots,7\), calculates the optimal leximin score by explicitly enumerating all assignments of jointly approved goods, and compares the resulting number of optimal allocations with the closed formula and exact inequality. This checks \(21{,}845\) profiles. A separate brute-force pass examines all unassigned/agent-one/agent-two choices in each of the \(341\) approval profiles with \(m\le4\), checking that clean global welfare optima agree with the reduced split model. It also verifies an independent generating-function identity for the exact mean multiplicity at \(p=1/2\). Run `python3 verify.py` in the directory containing this document. All checks pass. These finite checks exercise the counting formula; the limiting assertions follow from the proofs above, not from simulations.

## Relationship to prior work

Brandl, Suksompong, and Teh (2026, arXiv:2607.10064v1, initially posted July 11, 2026) characterize the binary-valuation Nash-welfare/leximin rule, define minimal completeness and non-redundancy, and study consistent selection among ties (especially Section 3, Theorem 3.5, and Section 4). Those results motivate counting the distinct optimal allocations *before* a tie is broken. Their characterization does not give the random Bernoulli-law event \(|D_m|<C_m\), the \(m^{-1/3}\) uniqueness/multiplicity transition, or the critical entropy distribution.

Suksompong and Teh (2022, arXiv:2204.03803v1, Sections 2 and 3) develop the weighted Nash-welfare tie-breaking rule and resource/population monotonicity. Their exact-selection and algorithmic results do not determine this random optimal-correspondence multiplicity distribution. Halpern, Procaccia, Psomas, and Shah (2020, arXiv:2007.06073) provide earlier welfare and strategyproofness foundations for binary valuations. Existing assignment-rule frequency results concern fundamentally different objects (ordinal house assignments and priority mechanisms), not arbitrary numbers of jointly approved goods under binary Nash-welfare maximization.

The exact finite count is a new observation derived directly from the simple two-agent allocation structure. The main quantitative contribution is the sharp sparse critical scale and nondegenerate limiting law, not a new definition of MNW or leximin. Searches of mathematical research records and primary literature did not establish dominating published coverage, but absence from indexed records does not prove priority.

## Limitations

The result concerns two equally weighted agents with independent homogeneous Bernoulli approvals, additive binary utilities, and cleaned allocations. It does not apply without alteration to more agents, nonuniform or correlated approvals, weighted entitlements, strict deterministic tie-breaking, or counts that include zero-valued goods assigned arbitrarily. The entropy convergence is in distribution and does not itself imply convergence of unbounded moments. A historical unpublished or unindexed equivalent result may exist. The work has not been independently audited.

## References

1. F. Brandl, W. Suksompong, and N. Teh. *Fair Division with Binary Valuations: Characterizations*. arXiv:2607.10064v1, July 11, 2026. https://arxiv.org/abs/2607.10064
2. W. Suksompong and N. Teh. *On Maximum Weighted Nash Welfare for Binary Valuations*. arXiv:2204.03803v1, April 8, 2022; Mathematical Social Sciences 2022. https://arxiv.org/abs/2204.03803
3. D. Halpern, A. D. Procaccia, A. Psomas, and N. Shah. *Fair Division with Binary Valuations: One Rule to Rule Them All*. arXiv:2007.06073, 2020. https://arxiv.org/abs/2007.06073
