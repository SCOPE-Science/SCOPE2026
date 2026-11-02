# Exact ternary four-good best-of-both-worlds lotteries for three agents

## Finding
For every complete-allocation instance with exactly three agents and four distinct indivisible goods, suppose all singleton values are integers in \(\{1,2,3\}\) and valuations are additive. There exists a lottery supported on **at most four complete deterministic allocations** such that:

1. It is **ex-ante envy-free (EF)**: for every ordered pair of agents \(i,j\), \(\mathbb E[v_i(A_i)]\ge\mathbb E[v_i(A_j)]\).
2. Every allocation in the support is **envy-free up to any good (EFX)**: for every \(i\ne j\) and each \(g\in A_j\), \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\).
3. Every allocation in the support is **Pareto optimal (PO)** among all complete deterministic allocations.

The claim is a finite-domain existence theorem with an exact reproducible certificate, **not** an assertion for arbitrary three-valued positive numbers or arbitrary numbers of goods. The proof's certificate comprises 5,053 rational lotteries covering all \(3^{12}=531{,}441\) labeled valuation profiles by relabeling agents and goods. Among the canonical profiles, 392 have all three agents genuinely using all three singleton values, so the result does not reduce to the previously solved bi-valued class.

## Assumptions and scope
Let \(N=\{0,1,2\}\), \(M=\{0,1,2,3\}\). For each agent \(i\) and good \(g\), the singleton value \(v_{ig}\) lies in \(\{1,2,3\}\), and \(v_i(S)=\sum_{g\in S}v_{ig}\). Every deterministic allocation \(A=(A_0,A_1,A_2)\) partitions \(M\), allowing empty bundles. There are \(3^4=81\) such allocations. PO means that no other such partition weakly improves every agent's *own* realized utility and strictly improves at least one. A lottery is a probability distribution on these 81 allocations.

## Proof
The proof is an exact finite certificate. Its correctness does not rely on numerical linear-programming output, heuristics, sample tests, or assuming that partial enumerations extend to infinite domains.

**Symmetry reduction.** A valuation profile is a list of four columns in \(\{1,2,3\}^3\). Permuting the four goods sorts these columns without changing existence; permuting the three agents permutes their coordinates. Enumerate all size-four multisets of the 27 possible columns and select the lexicographically least sorted representative under all six permutations of agent coordinates. This yields exactly 5,053 representatives. For each, the code independently computes the number of distinct labeled matrices in the joint orbit; summing those orbit sizes gives exactly \(531{,}441=3^{12}\), hence every labeled profile is covered exactly once.

**Allocation encoding.** Number allocations from zero to 80 by writing their four owners as a four-digit base-three vector, the leftmost digit corresponding to good zero. The file `ternary_lottery_witnesses.json` contains one entry per canonical profile, in the canonical order specified by `verify_ternary.py`. Each entry gives a list of triples `(allocation index, rational numerator, positive denominator)`.

**Exact certificate verification.** For each canonical profile, `verify_ternary.py` reconstructs all 81 allocations and reads its rational lottery. It verifies all numerators/denominators are positive, that allocation indices are unique and in range, and that weights sum exactly to one. For every positive-weight allocation and every ordered pair of distinct agents it checks EFX after deleting **each** good of the second agent. For each such allocation it compares its three-dimensional own-utility vector against those of all 81 partitions to rule out Pareto domination. Finally, for each of the six ordered agent pairs it checks the ex-ante envy-surplus inequality as an *exact rational number*. Thus each listed lottery satisfies all three conditions.

The verifier also establishes that no listed lottery has more than four support points. The support-size histogram across canonical representatives is \(1123,2091,1772,67\) for support sizes one through four, respectively. These are sizes of the supplied certificates, not claims about smallest possible support. Because every definition and certificate is invariant under simultaneous relabeling, the verified representative lotteries transport to every labeled profile.

For a concrete genuinely three-level example, values by agents in good order are \((1,2,2,3)\), \((1,2,3,3)\), \((1,2,3,3)\). Its certificate uses allocation indices \(5,7,32,61\) with respective probabilities \(1/3,1/3,1/6,1/6\); the exact checker verifies its EF, EFX and PO properties.

## Verification
With both supplied files in one directory run:

```sh
python3 verify_ternary.py ternary_lottery_witnesses.json
```

The program depends only on the Python 3 standard library, reads every certificate from the supplied JSON and reconstructs valuations and allocation utilities independently. The complete exact check returned:

```
VERIFY_OK canonical=5053 labeled=531441 all_three_level=392 any_three_level=3767 max_support=4 support_hist={1: 1123, 2: 2091, 3: 1772, 4: 67}
```

Every equality and inequality used to certify the theorem is checked with integer or rational arithmetic. No external optimization solver or cached transcript is needed to verify the theorem.

## Relationship to prior work
Aziz's August 10, 2026 preprint proves the two-agent guarantee and a **three-agent four-good counterexample** with singleton values ranging up to five; its Theorem 5 does not assert this positive theorem for the fixed alphabet \(\{1,2,3\}\). Bu, Li, Liu, Lu, and Tao establish ex-ante EF, ex-post EFX and ex-post fractional Pareto optimality for **bi-valued** additive agents. This result covers profiles in which each agent uses all three values, outside that restriction; it claims only integral PO, not fractional PO. Panchapakesan and Vaish's later subsidy-based result gives a conditional reduction from envy-freeability to best-of-both-worlds lotteries rather than an unconditional coverage of the present explicit finite domain. The finite three-valued guarantee and compact rational support are the assessed additions, not the general framework or preexisting impossibility example.

## Limitations
The conclusion is specific to three agents, four goods, and the identical positive integer alphabet \(\{1,2,3\}\) for every agent. It is **not** proved for arbitrary positive three-valued magnitudes \(\{p,q,r\}\), larger numbers of goods, fractionally PO support, truthfulness, or a general parametric characterization of solvable domains. The support bound four is constructive, not proved minimal. Exact enumeration proves the stated finite theorem but does not establish priority over unpublished or unindexed work. Independent scientific review has not been performed.

## References
- H. Aziz, *Best-of-Both-Worlds Fairness and Pareto Optimality*, arXiv:2608.08966v1, first public August 10, 2026, https://arxiv.org/pdf/2608.08966. In particular Section 6, Theorem 5 and its proof.
- X. Bu, Z. Li, S. Liu, X. Lu and B. Tao, *Best-of-Both-Worlds Fair Allocation of Indivisible and Mixed Goods*, arXiv:2410.06877v2, https://arxiv.org/html/2410.06877v2, especially Section 5.
- S. Panchapakesan and R. Vaish, *Best-of-Both-Worlds Fair Division via Subsidies*, arXiv:2610.14994v1, first public October 10, 2026, https://arxiv.org/abs/2610.14994. The full text was inaccessible at review; the abstract-level comparison is limited accordingly.
