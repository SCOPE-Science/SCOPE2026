# Finite-inventory minimax fairness and pairwise designs for two arriving agents

## Finding

For each integer \(m\ge2\), there are exactly two sequentially arriving agents and a known collection \(M\) of \(m\) indivisible chores. Each agent has an arbitrary binary additive cost function (each chore costs zero or one). On arrival, agent \(i\)'s entire cost function is revealed, and an allocation rule irrevocably assigns a subset of the remaining chores to that agent. The first decision cannot use the second agent's costs. All chores must eventually be allocated. The adversary fixes both cost functions before the algorithm randomizes.

The exact minimax expected ex-post maximin-share (MMS) ratio is

\[
R_m:=\inf_{\mathcal A}\sup_{c_1,c_2}\mathbb E_{\mathcal A}[\rho(X)]
=1+\frac{s-1}{2(2s-1)},\qquad s=\left\lfloor\frac m2\right\rfloor.
\]

Here \(\mu_i\) is agent \(i\)'s minimum possible maximum bundle cost in a partition into two bundles and \(\rho(X)=\max\{1,c_i(X_i)/\mu_i:i\in\{1,2\},\mu_i>0\}\). If \(\mu_i=0\), then a valid policy assigns only zero-cost chores to that agent; an allocation incurring a positive cost for such an agent has infinite ratio. In particular, \(R_2=R_3=1\), \(R_4=R_5=7/6\), and \(R_m\) increases through even inventory sizes toward \(5/4\).

More precisely, if the first agent's support of positively costly chores has known size \(t\ge2\), the exact minimax ratio restricted to that support size is

\[
R(t)=1+\frac{r(r-1)}{t(t-1)},\qquad r=\left\lfloor\frac t2\right\rfloor.
\]

For an inventory consisting entirely of the first agent's \(t\) costly chores, a randomized first-stage allocation is minimax if and only if its complement \(S\), left for the second agent, has \(|S|=r\) almost surely and

\[
\Pr(\{e,f\}\subseteq S)=\frac{r(r-1)}{t(t-1)}\quad
\text{for every two distinct chores }e,f.
\]

When \(t=2^d\ge4\), optimality can be achieved with only \(2(t-1)\) different retained sets: identify chores with \(\mathbb F_2^d\), draw a nonzero linear functional \(a\) uniformly and a bit \(b\) uniformly, and retain exactly the affine hyperplane \(\{x:a\cdot x=b\}\). Every optimal sampler on \(t\) costly chores with \(t\ge4\) has at least \(t\) distinct retained sets, so the affine construction is within a factor of two in output support and uses only logarithmically many expected unbiased random bits.

## Assumptions and scope

The inventory is labeled and known to the rule. Costs are nonnegative, additive, and in \(\{0,1\}\); no extra restriction is imposed on the supports. Decisions are irrevocable, and agent two receives all unallocated chores. Randomness belongs to the policy and is hidden from the oblivious adversary, which chooses the full input before random choices occur. No incentive-compatibility requirement is imposed. The optimization takes the supremum over all fixed binary-cost profiles and the infimum over all randomized online allocation policies, without computational restrictions. A zero-cost agent can be protected by giving it no positively costly chores.

The upper-bound policy assigns every currently zero-cost chore to the first agent, then chooses uniformly at random \(\lceil t/2\rceil\) of its \(t\) positively costly chores. Agent two receives everything left. For \(t=0\), give all chores to agent one; for \(t=1\), give its single costly chore to agent one. For \(t\ge2\), the following arguments are exact, including zero-cost second-agent cases.

## Proof

**1. A pairwise-design upper bound.** Fix first-agent positive support \(B\) of size \(t\ge2\). Suppose the first-stage rule retains a set \(S\subseteq B\) of fixed cardinality \(r=\lfloor t/2\rfloor\) and every distinct pair of \(B\) belongs to \(S\) with the same probability \(p_t=r(r-1)/(t(t-1))\). Agent one receives \(\lceil t/2\rceil\) unit-cost chores and therefore has ratio at most one. Let \(C\subseteq B\) be the second agent's positive support among the remaining candidates, and put \(k=|B_2|\), \(u=\lceil k/2\rceil\). If \(u=0\), the second agent's cost is zero. Otherwise partition the elements of \(C\) into \(u\) disjoint blocks of size at most two, possible because \(|C|\le k\le 2u\). Let \(Z_j\) be the number of retained chores in block \(j\). Using \(z^+=\max\{z,0\}\),

\[
\rho(X)=1+\frac{\bigl(\sum_{j=1}^u Z_j-u\bigr)^+}{u}
\le1+\frac1u\sum_{j=1}^u (Z_j-1)^+.
\]

A singleton block contributes zero; a two-element block contributes one exactly when both items are retained. Consequently \(\mathbb E\rho(X)\le1+p_t\). The uniform random \(r\)-subset has pair-retention probability \(p_t\), proving the achievable bound \(R(t)\le1+p_t\). This part refines the pair-block upper-bound idea in Li, Wang and Wu, Appendix B (2026).

**2. A finite, exact lower bound.** Temporarily assume all \(t\) chores have first-agent cost one, and draw the second agent's costly set \(C\) uniformly among the \(\binom t2\) unordered pairs. Freeze any random seed of the first-stage rule and suppose it assigns \(q\) chores to agent one, retaining \(t-q\) for agent two. Write \(h=\lceil t/2\rceil\), \(b_q=\max\{1,q/h\}\), and

\[
p_q=\frac{(t-q)(t-q-1)}{t(t-1)}.
\]

With probability \(p_q\), both costly chores of agent two remain; its MMS is one, so its ratio is two. Otherwise its ratio is at most one. Averaging over the uniformly random pair yields exactly

\[
\Phi_t(q)=b_q+(2-b_q)^+p_q.
\]

For \(q\le h\), this equals \(1+p_q\) and strictly decreases as \(q\) increases to \(h\) (for \(t\ge2\)). For \(q\ge h\), put \(r_q=t-q\) and \(\varepsilon=2h-t\in\{0,1\}\). An exact difference calculation gives

\[
h\bigl(\Phi_t(q+1)-\Phi_t(q)\bigr)
=1-\frac{(r_q-1)(3r_q-2+2\varepsilon)}{t(t-1)}>0,
\]

whenever \(h\le q<t\). The last strict inequality follows from \(r_q\le\lfloor t/2\rfloor\): if \(t=2s\), the subtracted numerator is at most \((s-1)(3s-2)<2s(2s-1)\); if \(t=2s+1\), it is at most \(3s(s-1)<2s(2s+1)\). Thus the unique minimizing count is \(q=h\), giving \(\min_q\Phi_t(q)=1+p_t\). The same inequality holds after averaging over any randomized policy. Averaging over the pair \(C\) then guarantees that some **fixed** second-agent support attains this expected lower bound, which is valid against an oblivious adversary. Therefore \(R(t)=1+p_t\).

**3. Characterization of all optimal randomizations.** In the all-positive first-stage subproblem, equality in the preceding bound forces \(q=h\) with probability one, because it uniquely minimizes \(\Phi_t\). Let \(S\) be the retained set of size \(r=t-h\). For each pair \(C=\{e,f\}\), the realized competitive ratio is two if both elements lie in \(S\), and one otherwise. Uniform averaging over pairs fixes the mean of \(\Pr(C\subseteq S)\) at \(p_t\); keeping the worst pair below \(p_t\) forces equality for every pair. Conversely, any fixed-size sampler with this equal-pair property satisfies Step 1. This is the stated necessary-and-sufficient pairwise-design characterization. For \(t=2,3\), the condition \(p_t=0\) is vacuous once \(|S|=1\), and deterministic optimal rules are possible.

**4. Full-inventory minimax law.** For arbitrary first support size \(t\le m\), give the zero-cost chores to agent one and use the Step 1 policy, obtaining \(\mathbb E\rho\le R(t)\). Writing \(t=2u\) or \(t=2u+1\) gives

\[
p_{2u}=\frac{u-1}{2(2u-1)},\qquad
p_{2u+1}=\frac{u-1}{2(2u+1)}.
\]

The even-index values strictly increase with \(u\ge1\), while \(p_{2u+1}\le p_{2u}\). Hence \(\max_{0\le t\le m}R(t)=R(2\lfloor m/2\rfloor)\). For the reverse inequality, set the first agent's support to exactly \(2\lfloor m/2\rfloor\) items (and at most one additional zero-cost item), and apply Step 2 to a uniformly random pair inside that support. Extra first-agent zero-cost items cannot improve the difficult pair, so the same minimax lower bound applies. This proves the formula for \(R_m\).

**5. Sparse optimal designs and support lower bound.** For \(t=2^d\), uniformly choose \(a\ne0\) and \(b\in\mathbb F_2\) and retain \(S=\{x:a\cdot x=b\}\). Each set has \(t/2\) elements. For distinct \(x,y\), exactly \(2^{d-1}-1\) nonzero functionals annihilate \(x-y\), and for each the unique matching \(b\) is chosen with probability one half. Therefore

\[
\Pr(x,y\in S)=\frac{2^{d-1}-1}{2(2^d-1)}=p_t,
\]

so Step 3 proves optimality. There are precisely \(2(t-1)\) distinct affine hyperplanes. For the support lower bound, consider any optimal sampler on even \(t\ge4\) and the indicator vector \(Y\in\{0,1\}^t\) of its retained set. Pairwise balance and the fixed sum \(\sum_iY_i=t/2\) imply \(\mathbb E Y_i=1/2\) and \(\mathbb E(Y_iY_j)=p_t\) for \(i\ne j\). Hence the moment matrix \(\mathbb E[YY^{\mathsf T}]\) has diagonal \(1/2\) and off-diagonal \(p_t\). Its eigenvalues are \(1/2-p_t>0\) (multiplicity \(t-1\)) and \(t/4>0\) (multiplicity one); its rank is \(t\). A distribution supported on \(b\) binary vectors has moment-matrix rank at most \(b\), so every optimal policy has at least \(t\) distinct retained sets. Choosing an affine hyperplane uniformly requires only \(O(\log t)\) **expected** unbiased coin flips, using rejection sampling for a nonzero \(a\) (not a bounded worst-case number of flips).

## Verification

The self-contained `checker.py` computes exact rational probabilities. It checks, for each first support size \(2\le t\le12\), every fixed first-stage count \(0\le q\le t\) against the uniform-pair lower bound and every second-agent support size \(0\le k\le t\) against the uniform-sampling upper bound. It separately enumerates all affine hyperplanes and all chore pairs for \(t\in\{2,4,8,16,32,64\}\). All 2,843 asserted identities and inequalities passed. These finite computations do not substitute for the quantifier-complete analytical argument in the Proof section. Reproduce with `python checker.py` (Python standard library only).

## Relationship to prior work

Li, Wang and Wu (arXiv:2610.15443v1, October 11, 2026), Theorem 3.1 and Appendix B, prove the optimal unrestricted-inventory two-agent competitive ratio \(5/4\) and use a uniform random half-sample with a pair-block argument. Those established facts are not claimed as new. The new statement holds inventory size fixed, determines its exact lower as well as upper bound, characterizes **all** minimax randomizations through pair probabilities, and gives an affine construction with only linearly many support sets instead of the exponentially many subsets of a fully uniform half-sample.

Li, Lin, Miao and Wu (arXiv:2609.10960v1) study the same sequential-agent timing but focus on deterministic competitive guarantees and known type classes; this does not provide a matching finite-inventory randomized minimax ratio. Zhou, Bai and Wu (arXiv:2304.13405) concern sequential **item** arrivals to already present agents; the information pattern differs. Pairwise balanced incomplete-block-design theory supplies the natural combinatorial language for the characterization, but a design's existence alone is not an online-minimax theorem.

## Limitations

The result concerns binary additive chore costs, exactly two arriving agents, expected maximum normalized MMS loss, and an oblivious adversary. It does not give the high-probability frontier, does not address heterogeneous positive costs, and does not imply a general multi-agent theorem. It is not a strategic truthfulness or Pareto-efficiency result. The affine sampler is supplied only for first-stage costly-support sizes that are powers of two; the uniform-subset policy works for every size. Publication priority, including possible unindexed equivalent refinements of the 2026 two-agent analysis, has not been independently certified.

## References

- Haolong Li, Fangxiao Wang, Xiaowei Wu, *Randomized Algorithm for MMS Allocation of Chores with Online Agent Arrivals*, arXiv:2610.15443v1, public October 11, 2026, especially Theorem 3.1 and Appendix B.
- Haolong Li, Zehan Lin, Huahua Miao, Xiaowei Wu, *MMS Allocation for Chores with Online Agent Arrivals*, arXiv:2609.10960v1, public September 10, 2026.
- Shengwei Zhou, Rufan Bai, Xiaowei Wu, *Multi-agent Online Scheduling: MMS Allocations for Indivisible Items*, arXiv:2304.13405, 2023.
