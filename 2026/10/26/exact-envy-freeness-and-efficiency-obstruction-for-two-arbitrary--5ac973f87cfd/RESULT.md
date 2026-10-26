# Exact envy-freeness and efficiency obstruction for two arbitrary Boolean valuations

## Finding

**Theorem (complete two-agent obstruction and incidence).** Let \(m\ge1\) be an integer. Partition a labeled set \(M\) of \(m\) indivisible items completely between two agents whose valuations \(v_1,v_2:2^M\to\{0,1\}\) are arbitrary set functions, without normalization, monotonicity, additivity, or disposal assumptions. There exists a complete allocation that is simultaneously envy-free (EF) and Pareto optimal (PO) **unless and only unless**

\[
v_1=v_2=v,\qquad v\not\equiv0,\qquad
v(S)v(M\setminus S)=0\quad\text{for all }S\subseteq M.
\]

Thus different Boolean valuations always admit a complete EF-and-PO allocation. Separately, *no* EF allocation exists exactly when the agents have an identical valuation satisfying \(v(S)+v(M\setminus S)=1\) for every \(S\subseteq M\).

For independent fair Boolean truth-table entries, let \(L=2^{m-1}\). Among the \(16^L\) equally likely ordered pairs of valuation tables, precisely \(3^L-1\) admit no EF-and-PO allocation, precisely \(2^L\) admit no EF allocation, and precisely \(3^L-1-2^L\) admit EF allocations but none that is PO. Hence the EF-and-PO failure probability is

\[
\frac{3^L-1}{16^L}
=\left(\frac3{16}\right)^L-\left(\frac1{16}\right)^L.
\]

All counts are exact for every \(m\ge1\); no asymptotic or genericity assumption is used in the classification.

## Assumptions and scope

An allocation is a pair \((S,T)\), with \(T=M\setminus S\). Its realized utilities are \((v_1(S),v_2(T))\). Envy-freeness is exactly the pair of inequalities
\[
v_1(S)\ge v_1(T),\qquad v_2(T)\ge v_2(S).
\]
Pareto optimality means no complete allocation has weakly larger realized utility for both agents and strictly larger utility for at least one. Equal-value bundles are permitted, and the empty bundle may have value one. Every assignment is complete; discarded goods and side payments are forbidden.

For the counting assertion, all \(2^{m+1}\) coordinates of the ordered pair of truth tables are independent fair bits. The uniform prior on complete set functions is a mathematical benchmark, not a calibrated preference-generating model. Complementation partitions the \(2^m\) subsets into \(L=2^{m-1}\) unordered pairs because \(m\ge1\).

## Proof

**1. Different valuations suffice.** If some complete allocation realizes utility vector \((1,1)\), it is automatically EF and PO: each agent has maximum possible own-bundle utility. Suppose no such allocation exists. If \(v_1\ne v_2\), there is a subset \(R\subseteq M\) on which the functions differ. If \(v_1(R)=1\) and \(v_2(R)=0\), give \(R\) to agent 1 and its complement to agent 2. Agent 1 receives utility one; agent 2 regards the other bundle as zero, so both envy inequalities hold. The realized utility is \((1,0)\), since \((1,1)\) was assumed unavailable. The only binary vector strictly Pareto dominating \((1,0)\) is \((1,1)\), hence the allocation is PO. If instead \(v_1(R)=0\) and \(v_2(R)=1\), give \(R\) to agent 2 and its complement to agent 1; by the symmetric argument this is EF and PO. This proves existence whenever \(v_1\ne v_2\).

**2. Identical valuations are the only obstruction.** Write \(v_1=v_2=v\). If \(v\equiv0\), every complete allocation is EF and PO. If some complementary pair \(S,T\) satisfies \(v(S)=v(T)=1\), allocating those bundles in either orientation gives \((1,1)\), hence EF and PO. Conversely, assume \(v\not\equiv0\) and every complementary pair has at most one value-one member. Some set \(R\) has value one. Allocating \(R\) to either agent produces a vector \((1,0)\) or \((0,1)\); it is PO because no \((1,1)\) allocation exists. Every PO vector therefore has one component one and the other zero, since \((0,0)\) is Pareto dominated. Its zero-utility agent strictly envies the winning bundle, which both agents evaluate identically. Thus no PO allocation is EF, proving both implications. For EF alone, identical valuations require \(v(S)=v(T)\) in an EF allocation; if the valuations differ, Step 1 already supplies EF. Therefore EF fails exactly for identical valuations in which each complementary pair has opposite Boolean values, equivalent to \(v(S)+v(T)=1\) everywhere.

**3. Exact enumeration.** For one unordered complementary pair \(\{S,T\}\), an identical Boolean set function takes one of four two-bit patterns: \(00,01,10,11\). The EF-and-PO obstruction in Step 2 requires all \(L\) pairs to avoid \(11\), leaving \(3^L\) patterns, except that the globally all-zero function must be removed. Since the two tables have to be identical, each such function gives exactly one ordered valuation profile. This yields \(3^L-1\). EF fails precisely when every pair takes \(01\) or \(10\), giving \(2^L\) profiles. Subtracting yields the number of profiles with EF but not EF-and-PO. Each of the two independently sampled truth tables has \(2^m=2L\) entries, hence the full sample space has size \(2^{4L}=16^L\). Division proves the displayed probability formulas.

**4. Conditioning on empty-bundle normalization.** Let \(Z=\lvert\{i:v_i(\varnothing)=0\}\rvert\). There are \(L-1\) complement pairs other than \(\{\varnothing,M\}\). The exact number of failing profiles with \(Z=0,1,2\), respectively, is
\[
3^{L-1},\quad 0,\quad 2\cdot3^{L-1}-1.
\]
For \(Z=0\), the shared value at \(\varnothing\) is one, so the shared value at \(M\) must be zero. For \(Z=2\), both shared empty values are zero, the common full-bundle value may be zero or one, and the all-zero function is excluded. Mixed empty values prohibit identical valuation tables. The respective conditioning sample-space sizes are \(4\cdot16^{L-1},8\cdot16^{L-1},4\cdot16^{L-1}\). These exact counts refine, but do not replace, earlier empty-bundle-normalization existence guarantees.

## Verification

The standalone file `check.py` directly computes, for each input pair of truth tables, all \(2^m\) complete allocations, their utility pairs, every envy inequality and Pareto dominance relation. It does **not** use the theorem to classify an allocation, so it independently tests the obstruction and the enumerated counts. Running `python3 check.py` checks every labeled Boolean-valuation profile for \(m=1,2,3\), totaling \(16+256+65536=65808\) profiles. The observed triples (no EF; no EF-and-PO; EF but no EF-and-PO) are \((2,2,0)\), \((4,8,4)\), and \((16,80,64)\); all predicted conditional normalization counts also agree. The exhaustive computation verifies the finite test domain only; Steps 1–4 supply the proof for arbitrary \(m\).

## Relationship to prior work

Shah and Verma (2026) study precisely arbitrary, possibly unnormalized Boolean set valuations. Their Lemma 3 proves EF and PO existence when exactly one agent values the empty bundle at zero, and Proposition 6 provides a counterexample to the stronger combination PO-and-EF1 for a different fixed normalization regime. The present theorem extends that **positive** result in the two-agent case from the mixed-normalization family to every pair of *distinct* truth tables, and characterizes exactly every remaining EF-and-PO obstruction, including normalized and unnormalized profiles. It does not claim Shah and Verma's known existence theorem or their EF1 impossibility construction as new.

Bérczi and coauthors (2020, later published) develop EF1 and EFX for nonmonotone, nonadditive valuations, including Boolean valuations. Their results concern envy relaxations and do not imply this exact EF-and-PO obstruction or its enumeration. The distinct 2026 results on EF1 plus PO for strictly increasing valuations use monotonicity and an inequivalent fairness criterion. No mathematically equivalent complete two-agent Boolean EF-plus-PO classification was found among the inspected sources, but a simple structural fact of this kind might have been observed elsewhere; a literature search is not a proof of global novelty.

## Limitations

The theorem concerns exactly two agents, indivisible goods, complete allocations, and binary-valued set functions. The classification need not hold for three agents, for utilities with more than two levels, or for constrained allocations. An arbitrary Boolean function may be nonmonotone; the random truth-table model is not a realistic distribution of preference rankings and should not be interpreted as an empirical market incidence. The probability conclusion follows only under the stated independent fair-entry benchmark. Independently reproduced finite checks are not an infinite proof, and publication priority remains subject to further literature discovery.

## References

1. Nisarg Shah and Paritosh Verma, *Fair Division Under Boolean Valuations: Beyond Normalization*, arXiv:2608.29497 (first posted 2026-08-30), https://arxiv.org/abs/2608.29497 . In particular, Lemma 3 and Proposition 6 in the full manuscript.
2. Kristóf Bérczi et al., *Envy-free Relaxations for Goods, Chores, and Mixed Items*, arXiv:2006.04428v1 (2020), https://arxiv.org/abs/2006.04428 .
3. Nicholas Teh, *Fair Division with Strictly Increasing Valuations: A Tight Threshold for Two-Agent EF1 and PO*, arXiv:2607.23367 (2026), https://arxiv.org/abs/2607.23367 .
