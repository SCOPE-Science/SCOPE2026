# A binomial staircase and a singular counting transition for fair-efficient bivalued chores

## Finding

For two agents splitting two equally abundant types of positively costly chores, the number of allocations that are simultaneously envy-free up to any owned chore (EFX) and fractionally Pareto optimal (fPO) is given by an exact binomial staircase. For each integer \(t\ge1\) and real ratio \(r>1\), put

\[
u_t(r)=\left\lfloor\frac{t}{2}-\frac{t-1}{2r}\right\rfloor.
\]

The total number of allocations of individually labeled chores meeting both criteria is

\[
N_t(r)=2\sum_{j=0}^{u_t(r)}\binom{t}{j}-1.
\]

At the coincident-cost value \(r=1\), the answer instead is

\[
N_t(1)=\binom{2t}{t}.
\]

For \(t\ge3\) the only possible jumps for \(r>1\) are at

\[
r_j=\frac{t-1}{t-2j},\qquad 1\le j\le\left\lfloor\frac{t-1}{2}\right\rfloor,
\]

where the value jumps upward by exactly \(2\binom{t}{j}\), including the threshold itself in the upper plateau. In particular, just above equality of the agents' two cost levels, exactly one allocation is EFX and fPO, whereas at equality there are \(\binom{2t}{t}\) such allocations.

For each fixed finite \(r>1\), defining \(\rho=(r-1)/(2r)\) and the binary entropy \(h_2(x)=-x\log_2 x-(1-x)\log_2(1-x)\), one also has

\[
\lim_{t\to\infty}\frac{1}{t}\log_2 N_t(r)=h_2(\rho).
\]

Thus a uniformly random labeled allocation satisfies both criteria with probability \(2^{-t(2-h_2(\rho))+o(t)}\) for fixed \(r>1\), but with probability asymptotic to \(1/\sqrt{\pi t}\) when \(r=1\).

## Assumptions and scope

There are exactly two agents and \(2t\) distinct indivisible chores, comprising \(t\) chores of type \(A\) and \(t\) of type \(B\), with integer \(t\ge1\). Each item is allocated wholly to exactly one agent. Agent 1 has additive nonnegative *disutility* equal to \(1\) per type-\(A\) chore and \(r\) per type-\(B\) chore. Agent 2 has the reversed costs, \(r\) for type \(A\) and \(1\) for type \(B\). The real parameter satisfies \(r\ge1\).

EFX means: for each agent \(i\) and every chore \(e\) owned by that agent, the cost of the agent's remaining bundle after removing \(e\) does not exceed the cost, according to that same agent, of the *other* agent's entire bundle. This condition is vacuous for an empty bundle. Fractional Pareto optimality (fPO) forbids a reallocation that divides items fractionally, weakly lowers both agents' disutilities, and strictly lowers at least one. All allocations of distinct chores are counted individually; type-level count vectors are not mistaken for labeled allocations. Efficiency here is fPO, not merely integral Pareto optimality.

## Proof

**1. Exact fPO structure for \(r>1\).** Suppose at least one type-\(A\) chore is owned by agent 2 and at least one type-\(B\) chore by agent 1. Exchange a small common fraction of these two chores. Agent 1 replaces type \(B\), cost \(r\), by type \(A\), cost \(1\), and agent 2 replaces type \(A\), cost \(r\), by type \(B\), cost \(1\). Both strictly decrease cost because \(r>1\). Hence fPO requires either all type-\(A\) chores to be allocated to agent 1, or all type-\(B\) chores to agent 2.

The condition is sufficient as well. When agent 1 receives all type-\(A\) chores, minimize the positive weighted total of costs using agent weights \((1,r)\): every type-\(A\) item has weighted cost \(1\) at agent 1 versus \(r^2\) at agent 2; every type-\(B\) item has weighted cost \(r\) at either. The given allocation is therefore a global minimum of this positive weighted sum among *all fractional allocations*. A fractional Pareto improvement would strictly reduce that sum, an impossibility. If agent 2 receives all type-\(B\) chores, the analogous certificate uses weights \((r,1)\). This establishes the if-and-only-if condition without assuming any general black-box characterization.

**2. Impose EFX.** In the first fPO family, all \(t\) chores of type \(A\) go to agent 1. Let \(j\) be the number of type-\(B\) chores also allocated to agent 1, with \(0\le j\le t\). Agent 1's total cost is \(t+rj\); their perceived cost of agent 2's bundle is \(r(t-j)\). All type-\(A\) chores in agent 1's bundle have cost \(1\), which is the smallest cost of an owned chore. Therefore the strongest EFX constraint for agent 1 is

\[
t+rj-1\le r(t-j)
\quad\Longleftrightarrow\quad
j\le\frac{t}{2}-\frac{t-1}{2r}.
\]

Agent 2, with only \(t-j\) type-\(B\) chores of unit cost, automatically satisfies EFX because, when nonempty, their post-removal cost \(t-j-1\) is no greater than their perceived other-bundle cost \(rt+j\). Hence every choice of \(j\) labeled type-\(B\) chores for agent 1 is valid precisely when \(0\le j\le u_t(r)\). There are \(\binom tj\) choices.

The second fPO family, in which all type-\(B\) chores go to agent 2, is obtained by interchanging both agents and both types. Its valid allocations have exactly \(j\) type-\(A\) chores additionally assigned to agent 2 for the same range of \(j\), again with \(\binom tj\) choices. The two families intersect in exactly one allocation: all type-\(A\) chores go to agent 1 and all type-\(B\) chores go to agent 2. Inclusion-exclusion proves the binomial sum.

**3. Coincident costs.** If \(r=1\), all chores cost \(1\) to either agent. The total disutility is constantly \(2t\), so every allocation minimizes the weighted sum with weights \((1,1)\) and is fPO. If agent 1 receives \(k\) items, EFX for each nonempty bundle forces \(k-1\le2t-k\) and \(2t-k-1\le k\). Because \(k\) is an integer, these conditions are jointly equivalent to \(k=t\), including the endpoints. The central binomial coefficient counts the ways to choose agent 1's chores.

**4. Thresholds and plateaus.** For \(r>1\), the integer bound \(u_t(r)\) increases from \(0\) to at most \(\lfloor(t-1)/2\rfloor\). Reaching the value \(j\ge1\) is equivalent to \(r\ge(t-1)/(t-2j)\); at that crossing, the two fPO families each gain exactly \(\binom tj\) new allocations, with no new intersection. This yields the stated complete list of thresholds and jump sizes. If \(t\le2\), there are no thresholds and \(N_t(r)=1\) for every \(r>1\). At large finite \(r\), the upper plateau is \(2^t-1\) for odd \(t\), or \(2^t-\binom{t}{t/2}-1\) for even \(t\).

**5. Asymptotic comparison.** Fix a finite \(r>1\). Then \(u_t(r)/t\to \rho=(r-1)/(2r)\), lying strictly between \(0\) and \(1/2\). The binomial coefficients increase throughout the summation range for large \(t\), so

\[
\binom{t}{u_t(r)}\le\sum_{j=0}^{u_t(r)}\binom tj
\le (u_t(r)+1)\binom{t}{u_t(r)}.
\]

Stirling's formula gives \(t^{-1}\log_2\binom{t}{u_t(r)}\to h_2(\rho)\). The polynomial factor in the upper bound and the multiplicative factor of two in the exact count do not change the exponential rate. The total number of labeled allocations is \(2^{2t}=4^t\). At \(r=1\), the standard central-binomial asymptotic \(\binom{2t}{t}\sim4^t/\sqrt{\pi t}\) instead applies.

## Verification

The companion standalone Python 3 file `verify_chores.py` runs entirely with the standard library and exact rational arithmetic. Its independent itemwise implementation evaluates each labeled allocation, computes EFX from each owned chore, and checks weighted-sum fPO certificates. The program independently compares the resulting count against the binomial formula, also checking every certificate against the crossed-chore obstruction. It passed 85 rational parameter instances and 356,980 labeled allocation evaluations across \(1\le t\le7\). The tested parameters include \(r=1\), \(r>1\) very close to one, and rational points on both sides of every applicable threshold. This finite replay supports but cannot establish the statements for all real parameters, all sizes, or the asymptotic limit; those follow from the algebraic proof above.

For a concrete illustrative plateau, when \(t=5\), the two thresholds are \(4/3\) and \(4\); the counts at successive \(r>1\) plateaus are \(1\), \(11\), and \(31\). The identical-cost count is separately \(252\).

## Relationship to prior work

Aziz, Lindsay, Ritossa, and Suzuki (arXiv:2211.00879, first released November 2, 2022) study two chore types and explicitly prove a general fPO structural characterization (Lemma 4.1), an EF1+fPO algorithm, and existence of EFX allocations (Theorem 5.1). The fPO sublemma used here is a special case of their known result and is **not** claimed as a new principle. Their EFX-existence theorem also covers the existence aspect of this instance. The present claim is the exact *joint* EFX-and-fPO allocation census as a function of the cost ratio, its complete rational jump structure, and the singular asymptotic random-allocation rate; the inspected 29-page arXiv version does not state these counts or rates.

Garg, Murhekar, and Qin (arXiv:2212.02440, first released December 5, 2022) analyze EFX with fPO for indivisible chores, including constructive existence on specified bivalued domains and incompatibility examples on more general domains. These prior results establish why joint fairness and efficiency is a natural quantity to analyze, but they do not imply the full allocation-counting staircase from their stated theorems.

## Limitations

The classification applies only to exactly two agents, equal counts of two chore types, symmetric cross-costs, additive strictly positive costs, and complete integral allocations. The enumerated criterion is fractional Pareto optimality, not the weaker integral criterion. The asymptotic formula assumes a fixed finite parameter \(r>1\); it does not describe double scaling with \(r\to1\) as the number of chores grows. Published priority for the precise joint count and its entropy transition has not been independently certified: equivalent unindexed results or immediate consequences recognized elsewhere may exist. Finite verification alone does not prove the infinite theorem.

## References

1. Haris Aziz, Jeremy Lindsay, Angus Ritossa, and Mashbat Suzuki, *Fair Allocation of Two Types of Chores*, arXiv:2211.00879 (first public version November 2, 2022), https://arxiv.org/abs/2211.00879 and full text https://arxiv.org/pdf/2211.00879 .
2. Jugal Garg, Aniket Murhekar, and John Qin, *New Algorithms for the Fair and Efficient Allocation of Indivisible Chores*, arXiv:2212.02440 (first public version December 5, 2022), https://arxiv.org/abs/2212.02440 and https://www.ijcai.org/proceedings/2023/0302.pdf .
