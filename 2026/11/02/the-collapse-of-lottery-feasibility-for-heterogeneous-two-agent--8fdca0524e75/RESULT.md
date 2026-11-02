# The collapse of lottery feasibility for heterogeneous two-agent binary chores

## Finding

**Theorem (exact best-of-both-worlds criterion).** Consider two agents with positive entitlement weights \(p\) and \(q=1-p\), where \(0<p<1\). Their additive binary chore costs comprise \(a\) labeled chores of type \((1,0)\), \(b\) of type \((0,1)\), \(c\) of type \((1,1)\), and \(d\) of type \((0,0)\), where \(a,b,c,d\) are nonnegative integers and **\(a+b\geq1\)**. The following are equivalent:

1. A lottery is weighted envy-free in expectation (ex-ante WEF), and every allocation in its support is weighted envy-free up to any chore (WEFX) and fractionally Pareto optimal (fPO).
2. There exists a single deterministic allocation that is simultaneously WEF and fPO.
3. The interval
   \[
   [\,pc-qb,\ p(c+a)\,]\cap\{0,1,\ldots,c\}
   \]
   contains an integer.

When these conditions hold, **exactly**
\[
2^d\sum_{\substack{0\leq x\leq c\\x\in\mathbb Z\\pc-qb\leq x\leq p(c+a)}}\binom{c}{x}
\]
complete allocations are WEF and fPO, treating all chores as labeled. Such an allocation itself is a valid point-mass lottery, so there is no need to randomize to attain the combined guarantee. In particular, if \(a,b\geq1\), compatibility always holds for every positive entitlement pair and every \(c,d\).

**Sharp boundary illustration.** With \(p=1/3\), \(c=1\), and \(a=b=d=0\), a single shared chore admits an ex-ante WEF lottery supported on WEFX+fPO outcomes (assign it to agent 1 with probability \(1/3\)) but has no deterministic WEF allocation. Adding just one type-\((1,0)\) chore changes the feasibility interval to \([1/3,2/3]\), leaving no admissible integer; no such lottery then exists. This illustration explains why the hypothesis \(a+b\geq1\) matters, but is not a claim that all homogeneous instances are infeasible.

## Assumptions and scope

All chores are indivisible, individually labeled, and allocated completely. For a bundle \(S\), the nonnegative cost to agent \(i\) is the sum of her individual binary item costs. An entitlement-weighted comparison from agent \(i\) to agent \(j\) divides respective bundle costs by \(w_i\) and \(w_j\). WEF requires \(c_i(A_i)/w_i\leq c_i(A_j)/w_j\). WEFX requires the same inequality **after removal of every item in the agent's own bundle**, including items having zero cost to that agent; an empty bundle vacuously passes. Ex-ante WEF applies the two WEF inequalities to expected costs of the bundles. fPO means that no **fractional** reallocation weakly decreases both agents' costs and strictly decreases at least one. All weights are strictly positive and normalized to sum to one. The theorem does not cover \(a=b=0\), other numbers of agents, other valuation domains, or weaker relaxations of WEFX.

## Proof

**1. Exact fPO characterization.** Any type-\((1,0)\) chore must go to agent 2: transferring one from agent 1 to agent 2 would strictly reduce agent 1's cost without affecting agent 2's cost. Dually, every type-\((0,1)\) chore must go to agent 1. Conversely, any allocation with these assignments has aggregate cost exactly \(c\), the universal lower bound obtained by summing the minimum possible cost of each chore. Since any fractional Pareto improvement would strictly reduce aggregate cost, every such allocation is fPO. Shared and doubly-zero chores may be split arbitrarily.

**2. One integral variable.** Let \(x\in\{0,1,\ldots,c\}\) count shared chores allocated to agent 1. Every fPO allocation then satisfies
\[
\begin{aligned}
c_1(A_1)&=x,&c_1(A_2)&=a+c-x,\\
c_2(A_2)&=c-x,&c_2(A_1)&=b+x.
\end{aligned}
\]
The agent-1 WEF inequality is \(x/p\leq(a+c-x)/q\), equivalent to \(x\leq p(c+a)\). The agent-2 inequality is \((c-x)/q\leq(b+x)/p\), equivalent to \(x\geq pc-qb\). Thus a deterministic WEF+fPO allocation exists exactly when the stated interval contains an admissible integer. WEF implies WEFX because removing any own chore cannot increase the removed bundle's nonnegative cost. It also proves the implication from deterministic feasibility to a valid point-mass lottery.

**3. Randomization gives no further feasibility when \(a+b\geq1\).** Suppose a lottery satisfies the required ex-ante and ex-post properties. Every realization is fPO, hence has the structure above with integral random variable \(X\). Ex-ante WEF implies
\[
pc-qb\leq \mathbb E[X]\leq p(c+a).
\]
If \(a>0\), agent 2 must receive at least one type-\((1,0)\) chore, having zero cost to her, in **every** realization. Apply her WEFX inequality to removal of that zero-cost chore: the removal leaves her bundle cost unchanged. Therefore each support point has \(X\geq pc-qb\). Because \(\mathbb E[X]\leq p(c+a)\), at least one supported allocation also has \(X\leq p(c+a)\). Its integral \(X\) therefore lies in the interval, and that same allocation is WEF and fPO. If \(a=0\), the assumption forces \(b>0\); agent 1 necessarily receives a zero-cost type-\((0,1)\) chore. Her WEFX inequality applied to that item forces \(X\leq p(c+a)\) at every support point, and \(\mathbb E[X]\geq pc-qb\) forces some supported allocation to have \(X\geq pc-qb\). Again an integral WEF+fPO allocation exists. These cases exhaust \(a+b\geq1\).

**4. Exact counting.** For each admissible integer \(x\), there are \(\binom{c}{x}\) ways to choose the agent-1 shared chores. The asymmetric chores are uniquely allocated under fPO, and each of the \(d\) doubly-zero chores may go to either agent. Different choices yield different labeled allocations. Multiplication and summation give the stated formula.

**5. Guaranteed feasibility with both asymmetric types.** If \(a,b\geq1\), the feasibility interval contains \([pc-q,pc+p]\), an interval of length one containing \(pc\in[0,c]\). At least one of its integer points lies in \([0,c]\): when \(pc\) is an integer choose it; otherwise choose its floor if the fractional part is at most \(q\), and its ceiling otherwise. Both choices are integral in \([0,c]\), proving existence. (For \(c=0\), choose \(x=0\).) This completes all claims.

## Verification

A standalone exact-arithmetic checker (`verify.py`) independently enumerates all \(2^m\) assignments of up to eight labeled chores, with \(a+b\geq1\), where \(m=a+b+c+d\). For every integer count tuple and every rational entitlement \(p=A/B\) with \(2\leq B\leq9\) and \(1\leq A<B\), it independently evaluates fPO by minimum aggregate cost, both actual WEFX inequalities (including zero-cost-item removal), exact deterministic WEF, and feasibility of a lottery from the convex hull of the WEFX+fPO shared-chore counts. It compares these with the closed criterion and counting expression. The exact run returned `VERIFY_OK cases=16200 allocations=2211840 wefx_supports=133848`. An independent shorter closed-form recurrence checked an additional 54,450 combinations. These finite tests corroborate rather than replace the general proof; no floating-point tolerances are used.

To reproduce, save the embedded `verify.py` in the same directory and run `python verify.py` with Python 3. The script uses only the standard library.

## Relationship to prior work

Lin, Wu and Zhou, *Revisiting EFX and fPO Allocations for Binary Chores* (arXiv:2609.13970v1, 2026), prove weighted WEFX+fPO deterministic existence for arbitrary binary chore instances (Theorem 3.5), give an identical-cost two-agent ex-ante WEF versus ex-post WEF1 impossibility (Section 4, two identical common chores), and prove a best-of-both-worlds lottery existence guarantee **for equal entitlements** (Theorem 4.8). None of those three statements determines the exact **unequal-entitlement** instance-by-instance criterion under the presence of one-sided chores, nor shows that feasible WEFX-support lotteries must contain deterministic WEF allocations here.

Lin, Liu, Tao and Zhou, *Almost Envy-Freeness for Additive Mixed Manna with Entitlements* (arXiv:2609.02724v1, 2026), provide an ex-ante WEF/ex-post WEF1T guarantee on a different, weaker ex-post fairness scale, not this strong WEFX criterion. Panchapakesan and Vaish, *Best-of-Both-Worlds Fair Division via Subsidies* (arXiv:2610.14994v1, 2026), give a general weighted two-agent characterization through **weighted envy-freeability with subsidies** at every positive rescaling (Theorem 4.3); their characterization does not identify ordinary subsidy-free WEF, the binary counting formula, or the one-sided-zero-cost collapse.

The equally valued homogeneous branch \(a=b=0\) is deliberately excluded. General heterogeneous assignment, rather than the homogeneous integer apportionment phenomenon, is essential to this statement. Searches for equivalent assertions in the above literature and published mathematical records did not identify a covering theorem, but an unindexed or unpublished equivalent remains possible.

## Limitations

The equivalence relies on **strong WEFX treating zero-cost chores as eligible for removal**, exactly as in Definition 2.4 of the motivating source; restricting removal to strictly positive-cost chores invalidates the key zero-cost argument. It relies on every realization being fPO, on two agents, binary additive costs, and at least one asymmetric chore. It gives no general result for \(n\geq3\), all-shared instances, or general costs. Numerical checking is finite and is not independent scientific certification. Publication priority has not been independently audited; the matching literature may contain an equivalent specialization.

## References

- Z. Lin, X. Wu, S. Zhou, *Revisiting EFX and fPO Allocations for Binary Chores*, arXiv:2609.13970v1, September 12, 2026, https://arxiv.org/html/2609.13970v1 (especially Definitions 2.2–2.6, Theorems 3.5 and 4.8, Section 4).
- Z. Lin, S. Liu, B. Tao, S. Zhou, *Almost Envy-Freeness for Additive Mixed Manna with Entitlements: Deterministic and Randomized Guarantees*, arXiv:2609.02724v1, September 2, 2026, https://arxiv.org/html/2609.02724v1 (especially Result 3 and Sections 1 and 5).
- S. Panchapakesan, R. Vaish, *Best-of-Both-Worlds Fair Division via Subsidies*, arXiv:2610.14994v1, October 10, 2026, https://arxiv.org/html/2610.14994v1 (especially Theorem 4.3 and Section 4.3).
