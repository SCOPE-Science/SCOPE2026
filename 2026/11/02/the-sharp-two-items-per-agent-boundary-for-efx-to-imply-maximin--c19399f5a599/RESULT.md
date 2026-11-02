# The sharp two-items-per-agent boundary for EFX to imply maximin shares under positive bivalued valuations

## Finding

For any integer \(n\ge2\), consider \(m\) indivisible goods and strictly positive personalized bivalued additive utilities. An allocation is *complete* when each good belongs to exactly one agent. Then:

**Sparse-supply theorem.** Every complete EFX allocation is exact maximin-share (MMS) fair whenever \(m<2n\). Equivalently, EFX can fail to imply MMS in this valuation domain only with at least two goods per agent on average. The threshold is sharp for every \(n\ge2\).

**High-tier barrier.** Without any restriction on \(m\), for every agent \(i\) in every complete EFX allocation, if the agent's own value \(s_i\) is below the high tier \(h_i\), then \(s_i\ge\operatorname{MMS}_i\). Thus an MMS violation necessitates both \(s_i\ge h_i\) and \(m\ge2n\).

## Assumptions and scope

Fix \(n\ge2\), a finite good set \(G\) of size \(m\ge0\), and agents \(i=1,\ldots,n\). Utilities are additive: \(v_i(S)=\sum_{g\in S}v_i(g)\). For each agent choose real \(0<\ell_i<h_i\) and require \(v_i(g)\in\{\ell_i,h_i\}\) for every \(g\in G\); agents may use different tiers and classify a good differently. A tier need not actually occur in the instance.

For a complete partition \(X=(X_1,\ldots,X_n)\), EFX means that for every \(i\ne j\) and every \(g\in X_j\), \(v_i(X_i)\ge v_i(X_j\setminus\{g\})\). Strict positivity makes the positive-good and all-good deletion conventions coincide. The maximin share is

\[
\operatorname{MMS}_i=\max_{(P_1,\ldots,P_n)\text{ partition of }G}\ \min_{1\le j\le n}v_i(P_j),
\]

where empty parts are permitted. An exact MMS allocation satisfies \(v_i(X_i)\ge\operatorname{MMS}_i\) for every \(i\). The finding concerns a property of every EFX allocation, not whether EFX allocations exist.

## Proof

Fix an arbitrary focal agent \(i\) and abbreviate \(s=v_i(X_i)\), \(L=\ell_i\), \(H=h_i\). A contradiction to MMS-fairness is exactly a partition of \(G\) into \(n\) parts, all of value strictly greater than \(s\).

**Case 1: \(s\ge H\).** Each good is worth at most \(H\le s\). If \(m<2n\), every partition into \(n\) parts has at least one part containing at most one good (otherwise it would contain at least \(2n\) goods). That part is worth at most \(s\). Thus \(\operatorname{MMS}_i\le s\). No bivalued assumption is needed in this case beyond the single-good bound.

**Case 2: \(s<H\).** Every good in \(X_i\) has value \(L\). Set \(t=|X_i|\), so \(s=tL\). Let \(p\) and \(q\) denote the total numbers of goods worth \(H\) and \(L\), respectively, to agent \(i\). A high-valued good must occupy a foreign singleton bundle: if it shared a foreign bundle with any second good, EFX after deleting that second positive-valued good would require \(s\ge H\), contradiction. Consequently these \(p\) goods occupy distinct foreign singleton bundles and \(p\le n-1\).

The remaining \(n-p\) bundles (including \(X_i\)) contain only low goods. For each foreign low-only bundle of size \(u\), EFX after deleting a low good implies \((u-1)L\le tL\), and therefore \(u\le t+1\); this also holds for an empty bundle. The focal bundle contains exactly \(t\) low goods. Hence

\[
q\le t+(n-p-1)(t+1)=(n-p)(t+1)-1.
\]

Now consider any hypothetical partition into \(n\) parts all valued strictly above \(s=tL\). Since there are only \(p\) high goods, at least \(n-p\) of its parts must be high-free. Each such part would need at least \(t+1\) low goods. It would follow that \(q\ge(n-p)(t+1)\), contradicting the previous bound. Thus \(\operatorname{MMS}_i\le s\), regardless of \(m\).

These two cases prove the theorem for all agents. In particular, for \(m<2n\), Case 1 applies when \(s\ge H\) and Case 2 applies otherwise, so every agent meets their MMS.

**Sharpness at \(m=2n\).** Take identical additive valuations for all agents, with two goods worth \(2\) each and \(2n-2\) goods worth \(3\) each. Give the two 2-valued goods to agent 1 and give two 3-valued goods to each other agent. Agent 1 gets value \(4\) and values any other bundle after removing either good at \(3\). Every other agent gets \(6\), and values the remainder of any foreign bundle after any deletion at at most \(3\) (or \(2\) for agent 1's bundle). Thus this allocation is EFX.

A different partition pairs each 2-valued good with a 3-valued good, and pairs the remaining 3-valued goods among themselves. It has two parts of value \(5\) and \(n-2\) parts of value \(6\), so \(\operatorname{MMS}_1\ge5>4\). The case \(n=2\) is included (there are no additional value-6 parts). This proves the cardinality threshold cannot be improved.

## Verification

The accompanying dependency-free Python program `verify.py` independently enumerates every focal-agent high/low count distribution across \(n\) bundles for \(n=2,3,4,5\) and \(m<2n\), and for integer \(L\in\{1,2,3\}\) and \(H\in\{L+1,L+2,L+3\}\). For each distribution satisfying the focal EFX inequalities, it uses a separate exact integer dynamic program to test whether an \(n\)-partition can make every part worth more than the own bundle. All \(305{,}148\) focal EFX instances among \(893{,}790\) tested count configurations passed. The program additionally checks global EFX and the explicit MMS-defeating partition in the sharpness examples for \(n=2,3,4,5\).

Reproduce with `python3 verify.py`; no external packages, random sampling, floating-point comparisons, or external datasets are required. Exhaustion is over the stated finite test grid only. The proof above, not the finite computation, establishes the theorem for arbitrarily many agents, any integer good count, and all positive real tier values.

## Relationship to prior work

Zhang (arXiv:2608.15822, first public August 16, 2026) proves existence and computability of *some* exact MMS allocation under personalized bivalued valuations, for both goods and chores. This does not logically entail that *every* EFX allocation meets MMS in a sparse-supply goods instance. Qin (arXiv:2608.30267, first public August 31, 2026) proves a sharp general-domain EFX-to-MMS approximation factor of \(10/17\), which does not itself establish an exact factor of \(1\) in the restricted two-tier domain below the cardinality threshold.

Amanatidis, Birmpas and Markakis (arXiv:1806.03114, 2018) already exhibit EFX allocations failing MMS, including a two-goods-per-agent-type obstruction. The counterexample direction is therefore *not* claimed to be new; the finding concerns the matching universal lower-cardinality implication and high-tier barrier. Chen, Wong and Zhang (arXiv:2610.19099) study a different restriction of two item *types*, rather than agent-specific possible values. The inspected literature contains no stated domination of the new universal implication. The complete Zhang manuscript was not accessible for full-text comparison, so additional uninspected overlap remains a priority risk.

## Limitations

The proof needs each agent's values to lie in **two strictly positive personal tiers**; it does not extend to arbitrary additive valuations or to chores. EFX is assumed and complete; no EFX existence or construction algorithm is asserted. The high-tier lemma holds independently of the good count, but the global MMS conclusion needs \(m<2n\); the displayed two-tier construction violates it at \(m=2n\). The finite verifier does not independently establish the infinite theorem. No independent scientific audit has been performed. The 2018 obstruction is prior art, not a newly discovered example.

## References

1. Yuhao Zhang, *Exact MMS Allocations under Personalized Bivalued Valuations: Goods and Chores*, arXiv:2608.15822 (first posted 2026-08-16), https://arxiv.org/abs/2608.15822.
2. Qinghua Qin, *The Exact MMS Guarantees of EFX and PMMS*, arXiv:2608.30267 (first posted 2026-08-31), https://arxiv.org/abs/2608.30267.
3. Georgios Amanatidis, Georgios Birmpas and Evangelos Markakis, *Comparing Approximate Relaxations of Envy-Freeness*, arXiv:1806.03114 (first posted 2018-06-08), https://arxiv.org/abs/1806.03114.
4. Yu Chen, Kai Jie Wong and Xiaorui Zhang, *Maximin share allocations for two types of items*, arXiv:2610.19099 (first posted 2026-10-13), https://arxiv.org/abs/2610.19099.
