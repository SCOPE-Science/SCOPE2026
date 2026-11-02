# Exact horizon-wise welfare price of two-party FJR+ in temporal voting

## Finding

Fix an integer horizon \(L\ge1\). Among all complete, static, two-party approval elections with two nonempty parties, arbitrary integer electorate sizes \(n\ge2\), and one publicly selected candidate per round (repetitions allowed), the sharp utilitarian price of full justified representation plus (FJR+) is
\[
P(L)=\max_{0\le j\le\lfloor L/2\rfloor}
\frac{L(L-j)}{L^{2}-2Lj+2j^{2}}.
\]
Writing \(\alpha=1-1/\sqrt2\), it is sufficient to evaluate the integers \(\lfloor\alpha L\rfloor\) and \(\lceil\alpha L\rceil\) when they lie in the permitted index range. For \(L\ge2\), an attaining election has exactly \(L\) voters, divided into nonempty parties of sizes \(L-j\) and \(j\) for some positive maximizing index \(j\) (choose \(j=1\) when \(L=2\)); the formal index \(j=0\) has value one but does not describe a two-party split. When \(L=1\), the price is one for every two-party election. The finite-horizon sequence is not monotone:
\[
P(3)=P(4)=\frac65,\qquad P(5)=\frac{20}{17},\qquad
P(6)=\frac65,\qquad P(7)=\frac{35}{29}.
\]
Furthermore,
\[
0<\frac{1+\sqrt2}{2}-P(L)=O(L^{-2})
\quad\text{as }L\to\infty.
\]
The exact finite-population formula and a constructive optimal FJR+ outcome are given below.

## Assumptions and scope

There are \(n\ge2\) voters and precisely two parties, each with one distinct candidate. Party populations are \(a=n-b\) and \(b\), with integers \(1\le b\le\lfloor n/2\rfloor\). Every voter approves exactly its party candidate in every one of the \(L\ge1\) rounds. Each round selects one candidate, and the same candidate may be selected more than once. A voter's satisfaction is its party's total number of selected rounds; utilitarian welfare is the sum of satisfactions. Every candidate is available in every round. The price is the quotient of the unconstrained maximum welfare by the maximum welfare attainable subject to FJR+; it is not the strong price using the least-welfare FJR+ outcome.

We use the published characterization that on static party-list elections FJR+ is equivalent to *lower quota*: each party of population \(s\) receives at least \(\lfloor Ls/n\rfloor\) winning rounds (Teh, Proposition 3.4, arXiv:2609.35826). We do **not** claim this equivalence as new.

## Proof

**1. The exact finite-population welfare.** Put \(q=\lfloor Lb/n\rfloor\). The minority must win at least \(q\) rounds; the majority must win at least \(\lfloor La/n\rfloor\). Because the sum of these two lower quotas is at most \(L\), giving precisely \(q\) rounds to the minority and the remaining \(L-q\) to the majority is feasible and FJR+. Since \(a\ge b\), this allocation maximizes welfare subject to the quotas:
\[
W_{\rm FJR+}(n,b,L)=a(L-q)+bq=aL-(a-b)q.
\]
Unrestricted welfare is \(W^*=aL\). Since \(a\ge1\) and \(L\ge1\), both denominators are positive. Thus
\[
R(n,b,L)=\frac{(n-b)L}{(n-b)L-(n-2b)\lfloor Lb/n\rfloor}.
\]
This also provides an explicit optimal outcome for every admissible triple.

**2. Reduction to quota boundaries.** Normalize \(x=b/n\), so \(0<x\le1/2\), and set \(j=\lfloor Lx\rfloor\). When \(j=0\), the price is one. For \(j\ge1\),
\[
R(n,b,L)=\left(1-\frac{j}{L}\frac{1-2x}{1-x}\right)^{-1}.
\]
On the interval where \(j\) is constant, the factor \((1-2x)/(1-x)\) is strictly decreasing in \(x\), since its derivative is \(-1/(1-x)^2\). Consequently, for each nonempty quota stratum, the price is largest at the left boundary \(x=j/L\). This boundary is attainable with integers \(n=L\), \(b=j\) when \(1\le j\le\lfloor L/2\rfloor\); the \(j=0\) stratum has price one. Substitution yields the claimed finite maximum, without a limiting argument or relaxation gap.

**3. Locating the maximizing stratum.** Define
\[
f(x)=\frac{1-x}{1-2x+2x^2},\qquad 0\le x\le1/2.
\]
The stratum bound is \(f(j/L)\). Direct differentiation gives
\[
f'(x)=\frac{1-4x+2x^2}{(1-2x+2x^2)^2}.
\]
Its numerator has a unique zero on \([0,1/2]\), namely \(\alpha=1-1/\sqrt2\). Hence \(f\) increases to \(\alpha\) and decreases after it; the discrete maximum is at the floor or ceiling of \(\alpha L\), restricted to admissible indices. Evaluation at \(\alpha\) gives \(f(\alpha)=(1+\sqrt2)/2\). Because \(\alpha\) is irrational, no finite index realizes the continuous maximum. The nearest-grid distance is at most \(1/L\), and Taylor's theorem around the smooth stationary maximum, with bounded second derivative on \([0,1/2]\), gives \(0<f(\alpha)-P(L)=O(L^{-2})\). The stated values at horizons \(3\) through \(7\) follow by exact rational substitutions, proving nonmonotonicity.

## Verification

The accompanying standalone `verify.py` uses exact integer and rational arithmetic only. It compares the proposed optimum against all feasible majority/minority seat counts for every \(2\le n\le60\), \(1\le L\le50\), and \(1\le b\le\lfloor n/2\rfloor\), checks the population-specific price against the proposed horizon envelope, and checks all integer quota-boundary candidates and the nearest-grid characterization up to \(L=90\). The script also asserts the five stated finite-horizon values. It prints:

`VERIFY_OK finite_profiles=45000 feasible_seat_counts=87082 horizons=90 exact_examples=5`

This finite computation corroborates the all-parameter algebraic proof; it is not an exhaustive test of infinitely many populations or horizons. Reproduce with Python 3 using `python verify.py` from this package; no nonstandard dependencies are required.

## Relationship to prior work

Teh, *Full Justified Representation in Temporal Voting: Efficient Computation and Verification* (arXiv:2609.35826, first publicly available 2026-09-22), proves the FJR+ party-list lower-quota characterization (Proposition 3.4), but does not establish the welfare-price sequence or its extremizers. Its discussion explicitly identifies the welfare loss caused by FJR+ as a subject for further study. Teh, *The Price of Proportional Representation in Temporal Voting* (arXiv:2605.11157, 2026), studies the welfare price of JR, PJR, EJR, and EJR+, including horizon-dependent JR bounds; that is not this two-party FJR+ price. Elkind, Neoh, and Teh, *Temporal Elections: Welfare, Strategyproofness, and Proportionality* (arXiv:2408.13637, first public version 2024-08-24), establish unrestricted price bounds for the individual PROP axiom, not the exact two-party FJR+ horizon-wise characterization. The present result is a finite, exact two-party refinement with a nonmonotone horizon profile.

## Limitations

The formula concerns two parties with static, disjoint, complete approvals and one distinct candidate per party. It does not extend without further proof to three or more parties, overlapping approvals, changing ballots, cardinal utilities, or other proportionality axioms. Its asymptotic constant is a worst-case ratio, not a claim that every election incurs such a loss. No priority or independence guarantee is asserted; an equivalent observation could exist in unindexed apportionment or proportional public-decision literature. Independent scientific validation has not been performed.

## References

1. Nicholas Teh, *Full Justified Representation in Temporal Voting: Efficient Computation and Verification*, 2026, arXiv:2609.35826, https://arxiv.org/abs/2609.35826.
2. Nicholas Teh, *The Price of Proportional Representation in Temporal Voting*, 2026, arXiv:2605.11157, https://arxiv.org/abs/2605.11157.
3. Edith Elkind, Tzeh Yuan Neoh, and Nicholas Teh, *Temporal Elections: Welfare, Strategyproofness, and Proportionality*, 2024, arXiv:2408.13637, https://arxiv.org/abs/2408.13637.
