# Sharp Four-Good Failure of Ex-Ante Envy-Free Optimality for Unit Bernoulli Lotteries

## Finding

For exactly two agents and at most three indivisible goods, assume each agent independently values each good at either zero or one, with the same item-dependent success probability for both agents. Every deterministic complete allocation that is envy-free in expectation maximizes, among **all deterministic allocations**, the probability that both agents are envy-free after their values realize. The bound of three is sharp within this unit-valued Bernoulli domain: a four-good profile with all success probabilities strictly between zero and one has an ex-ante envy-free allocation that is strictly suboptimal for the probability of ex-post envy-freeness.

More precisely, for three goods with Bernoulli parameters \(a,b,c\), an ex-post probability maximizer assigns an item of largest success probability to one agent and the other two to the second agent. Thus any ex-ante envy-free allocation (if one exists) is optimal. A four-good counterexample has item success probabilities
\[
(p_1,p_2,p_3,p_4)=\left(\frac7{20},\frac7{20},\frac1{20},\frac{13}{20}\right).
\]
Assigning \(\{1,2\}\) to the first agent and \(\{3,4\}\) to the second agent is ex-ante envy-free, but its ex-post envy-free probability is
\[
\frac{13144772641}{25600000000},
\]
whereas assigning \(\{1,2,3\}\) to the first agent and \(\{4\}\) to the second gives
\[
\frac{13170400347}{25600000000}.
\]
The strict improvement is \(12813853/12800000000\). In fact, the latter allocation and its agent-swapped counterpart maximize the probability among all sixteen deterministic assignments.

## Assumptions and scope

There are two labeled agents and \(m\) labeled indivisible goods, where \(0\le m\le3\) in the positive theorem and \(m=4\) in the witness. A complete allocation partitions all goods into two (possibly empty) bundles, and is selected **before** the utility realizations are observed. Utilities are additive. For each agent \(i\) and good \(j\), \(X_{ij}\) is Bernoulli with \(\Pr(X_{ij}=1)=p_j\in[0,1]\); the \(2m\) random variables are mutually independent. Thus agents have identical marginal distributions on each good but independently realized utilities; this does not mean the two agents observe the same value realization. Preferences have no transfers and ties count as envy-free.

An allocation \((A,B)\) is ex-ante envy-free if each agent's expectation for its own bundle is at least its expectation for the other's. Because expected values are equal between agents, this is equivalent to
\[
\sum_{j\in A}p_j=\sum_{j\in B}p_j.
\]
For a given realized profile, ex-post envy-freeness requires that both agents weakly prefer their own bundles to the other's. Write \(\Phi(A,B)\) for the probability of this simultaneous event. The maximum used below ranges over **all** fixed deterministic complete allocations, not just ex-ante envy-free ones.

## Proof

Let \(U\) and \(V\) be independent sums of Bernoulli random variables for the goods in bundles \(A\) and \(B\), with the respective item parameters. The first agent's realized own-versus-other comparison has probability \(\Pr(U\ge V)\); the second agent's comparison has probability \(\Pr(V\ge U)\). The agent-specific underlying draws are independent, hence
\[
\Phi(A,B)=\Pr(U\ge V)\Pr(V\ge U).
\tag{1}
\]
The formula is symmetric in the two bundles, and the random variables in its two factors represent independent agent-specific comparisons, not a shared joint comparison. An empty-versus-all allocation has probability \(\prod_j(1-p_j)\).

For one or two goods, a one-good-versus-one-good allocation (when there are two goods) has probability at least the empty-versus-all probability. Indeed, if the two Bernoulli sums have distributions \(U,V\), then \(\Pr(U\ge V)\ge\Pr(V=0)\) and \(\Pr(V\ge U)\ge\Pr(U=0)\). Their product therefore exceeds or equals \(\prod_j(1-p_j)\). The case \(m=1\) has only agent-swapped assignments, so both are optimal. For \(m=2\), every one-versus-one split has the same probability as its swap, while the only other alternatives are empty-versus-all splits. Thus every ex-ante envy-free partition is optimal: if the expected total is positive it must split one good per agent with the two item probabilities equal; if the total is zero, every partition has probability one. The zero-good case is immediate.

For \(m=3\), consider the partition isolating the good with parameter \(a\), against two goods with parameters \(b,c\). Its probability from (1) is exactly
\[
F(a;b,c)=\big((1-b)(1-c)+a(b+c-2bc)\big)
         \big(1-a(1-b)(1-c)\big).
\tag{2}
\]
Direct polynomial expansion yields the exchange identity
\[
F(a;b,c)-F(b;a,c)
=c(a-b)\big[2-c-(1-c)(a+b-2ab)\big].
\tag{3}
\]
For \(a,b,c\in[0,1]\), the factor \(a+b-2ab=a(1-b)+b(1-a)\) lies in \([0,1]\), so the bracket in (3) is at least one. Therefore if \(a\ge b\), isolating \(a\) is no worse than isolating \(b\). Repeated exchange proves that isolating any maximum-parameter good is optimal among all one-versus-two splits. The preceding bound using \(\Pr(U\ge V)\ge\Pr(V=0)\) also shows that each such split does at least as well as an empty-versus-all split. Hence a maximum-parameter isolated good globally maximizes \(\Phi\).

An ex-ante envy-free allocation with three items and nonzero total must be a one-versus-two partition; by equality of expected bundle utilities, its singleton success probability equals the sum of the other two success probabilities, and is therefore at least as large as each other parameter. It follows from the preceding optimality statement that this allocation maximizes \(\Phi\). If all parameters are zero, every allocation is ex-ante and ex-post envy-free. This proves the universal claim for at most three goods, including boundary probabilities zero and one.

For the four-good counterexample, expected values of both \(\{1,2\}\) and \(\{3,4\}\) are \(7/10\). For any bundle partition, evaluate (1) by multiplying the Bernoulli probability-generating polynomials \(\prod_{j\in A}(1-p_j+p_jz)\) and \(\prod_{j\in B}(1-p_j+p_jz)\), then summing pairwise coefficients over the two weak inequalities. Exact rational arithmetic produces the two probabilities stated in the Finding, and their difference is strictly positive. The attached checker also independently enumerates every one of the \(2^8\) agent-good realization patterns for each of the sixteen labeled allocations and confirms that the proposed alternative is a global probability maximizer. Thus the universal implication fails already at four goods, all strictly unit-valued, with item-specific success probabilities strictly inside \((0,1)\).

## Verification

Run `python3 check.py` in the directory containing this document. The Python standard-library checker recomputes the ex-post probability of all sixteen four-good partitions by two independent methods: convolution of independent Bernoulli counts and direct enumeration of the \(2^8=256\) realization patterns. It confirms both exact fractions and their difference, identifies the two global maximizers, and checks the three-good rule for all \(5^3=125\) triples on a five-point probability grid. The universal three-good proof is the symbolic identity (3) and its inequalities, **not** the finite grid check. The counterexample is proved by the exact fractions, not statistical simulation.

## Relationship to prior work

Kale, Kulkarni and Garg, *Fairly Dividing Non-identical Random Items: Just Sample or Match* (arXiv:2512.17238, first public 2025-12-19), introduce independently sampled agent utilities with item-specific distributions, but their results address asymptotic existence and algorithms that inspect realized valuations rather than fixed allocations maximizing exact ex-post envy-freeness probability. Halpern, Psomas and Zhang, *Truthful Fair Division under Stochastic Valuations* (arXiv:2602.12359, first public 2026-02-12), study strategic mechanism guarantees in stochastic valuation models, not this exact small-item probability comparison.

Igarashi and Oh, *Fair Division of Lotteries* (arXiv:2610.34906, first posted 2026-10-26), study the same fixed-before-realization objective and give positive results for common convolution-power families, together with other approximation and complexity guarantees. The heterogeneous Bernoulli distributions used here are not assumed to be powers of one common distribution; its inspected theorems and examples do not provide the three-item exchange identity or the four-unit-Bernoulli witness. Its publication is later than the source-date anchor used here, and it is recorded only as subsequent closely related literature.

An earlier exact analysis of two-agent lottery goods with differing magnitudes and common success probability \(1/2\) already demonstrates a four-good failure. That does **not** entail failure when every realized singleton utility is restricted to \(0\) or \(1\), nor prove the universal three-good optimality in this item-heterogeneous unit-Bernoulli class. Similarly, a published three-good example with deterministic valued items and a rare high-valued item lies outside this class. The present result claims only the sharp boundary within the restricted, independently sampled unit-Bernoulli family.

## Limitations

The result assumes identical per-good probability distributions between the agents, independence across all agent-good pairs, nonnegative unit Bernoulli realized values, two agents, complete deterministic pre-realization allocation and weak envy-freeness. It does not prove that ex-ante envy-freeness is generally feasible, characterize all four-good exceptions, estimate the maximal possible probability improvement, or establish conclusions for correlated realizations, asymmetric agents, more agents or arbitrary utility magnitudes. The strict four-good probability advantage is approximately \(0.00100108\) for the stated witness; its importance here is the qualitative sharp item threshold, not the magnitude of that particular advantage. Published-priority comparisons cannot exclude unindexed or inaccessible prior work. No independent scientific audit is claimed.

## References

1. A. Kale, R. Kulkarni and N. Garg. *Fairly Dividing Non-identical Random Items: Just Sample or Match*. arXiv:2512.17238 (2025-12-19), https://arxiv.org/abs/2512.17238.
2. D. Halpern, A. Psomas and S. Zhang. *Truthful Fair Division under Stochastic Valuations*. arXiv:2602.12359 (2026-02-12), https://arxiv.org/abs/2602.12359.
3. A. Igarashi and Y. Oh. *Fair Division of Lotteries*. arXiv:2610.34906 (2026-10-26), https://arxiv.org/abs/2610.34906. Subsequent comparison, not the first-source date.
4. A. Aloisio, V. Bilò, A. M. Caruso, M. Flammini and C. Vinci. *Approximately Fair Allocation of Indivisible Items with Random Valuations*. AAMAS 2024, https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p2120.pdf.
