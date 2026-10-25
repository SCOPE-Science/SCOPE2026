# Sharp Nash-welfare loss under proposer-optimal stable marriage

## Finding
For every balanced stable-marriage market with \(n\ge2\) men and \(n\) women and strict complete preference orders, let \(M\) denote the men-proposing deferred-acceptance outcome. If \(T\) is any other stable matching that changes exactly \(k\) men's partners, then
\[
 \frac{P(T)}{P(M)}\le (n-1)^k,
 \qquad P(X)=\prod_{a\in\mathcal A}u_a(X(a)),
\]
where \(\mathcal A\) consists of all \(2n\) agents, and \(u_a\) is rank-induced utility. For each integer \(2\le k\le n\), there is a profile and a stable matching attaining equality with exactly \(k\) changed partners. Since \(k\le n\), the ratio of Nash social welfare at an optimal stable matching to that at \(M\) is at most
\[
 \boxed{\sqrt{n-1}},
\]
and this bound is sharp for every \(n\ge2\) (with value \(1\) when \(n=2\)).

For \(n\ge3\), equality in the global bound holds **exactly** for the following preference profiles: there exist two disjoint perfect matchings \(M,T\) such that each man ranks his \(M\)-partner first and his \(T\)-partner second, while every woman ranks her \(T\)-partner first and her \(M\)-partner last. All other preference positions can be assigned arbitrarily and independently. On these profiles, \(M\) is the men-optimal matching, \(T\) is the unique Nash-welfare-maximizing stable matching, and exactly
\[
 \boxed{n!D_n\big((n-2)!\big)^{2n}}
\]
labeled profiles attain the extreme, where \(D_n\) is the number of derangements of \(n\) elements. At \(n=3\), this count is \(12\) out of \(46656\) preference profiles. When \(n=2\), all stable matchings have identical Nash social welfare.

## Assumptions and scope
There are \(n\) men and \(n\) women. Every agent strictly ranks every member of the opposite side, preferring any partner to remaining unmatched. Positions are indexed \(r=0,\ldots,n-1\), and utility for rank \(r\) is \(u=n-r\). Thus all utilities are in \(\{1,\ldots,n\}\). A matching is a bijection and is stable when no unmatched man--woman pair prefers one another to their designated partners. Men-proposing deferred acceptance returns the unique *men-optimal stable matching* \(M\), meaning every man weakly prefers his partner at \(M\) to his partner at any stable matching. The Nash product is \(P(X)=\prod_{a\in\mathcal A}u_a(X(a))\), and Nash social welfare is \(N(X)=P(X)^{1/(2n)}\).

The count concerns **labeled** agents and all complete strict preference lists; the number of profiles is \(\big(n!\big)^{2n}\). No randomness is assumed. If \(T\) differs from \(M\) on exactly \(k\) men, then it differs on exactly \(k\) women, by bijectivity. The possible values of \(k\) are \(0\) and \(2,\ldots,n\): a bijection cannot change exactly one partner.

## Proof
**Pairwise loss bound.** Fix an arbitrary stable matching \(T\). On every changed man's edge, men-optimality and strictness yield \(u_i(T)<u_i(M)\). Since the utilities are positive integers, with \(u_i(M)\le n\),
\[
\frac{u_i(T)}{u_i(M)}\le\frac{u_i(M)-1}{u_i(M)}\le\frac{n-1}{n}.
\]
For each changed woman \(j\), \(u_j(T)/u_j(M)\le n/1=n\). Unchanged agents contribute a unit factor. Precisely \(k\) men and \(k\) women change, so multiplying these \(2k\) inequalities gives
\[
\frac{P(T)}{P(M)}\le\left(\frac{n-1}{n}\right)^k n^k=(n-1)^k.
\]
When \(k=0\), the product ratio is exactly \(1\). Maximizing over stable \(T\), then taking the \(2n\)-th root, proves the claimed Nash-welfare bound. At \(n=2\), either \(T=M\), or both pairs change. In the latter case both men prefer their \(M\)-partners to their \(T\)-partners, hence each man changes utility from \(2\) to \(1\). Every woman must prefer her \(T\)-partner to her \(M\)-partner: otherwise the woman and the man she was paired with in \(M\) would block \(T\), since this man strictly prefers \(M\). Thus each woman changes from utility \(1\) to \(2\). The two male factors \(1/2\) and the two female factors \(2\) multiply to \(1\), giving \(P(T)=P(M)\) for every stable \(T\).

**Sharpness for any changed-set size.** Fix \(2\le k\le n\), and label partners by indices \(0,\ldots,n-1\). Let \(M\) pair \(m_i\) with \(w_i\) for all indices. Let \(T\) pair \(m_i\) with \(w_{i+1\bmod k}\) for \(0\le i<k\), leaving the other pairs unchanged. Each of the first \(k\) men ranks his \(M\)-partner first and his \(T\)-partner second. Each of the first \(k\) women ranks her \(T\)-partner first and her \(M\)-partner last. Every unmoved man and woman ranks the common \(M\)- and \(T\)-partner first. Complete the lists with the remaining opposite-side agents in arbitrary order. Thus \(M\) is stable (all men obtain first choice), while \(T\) is stable (every moved woman and each unmoved man obtains first choice). Men-proposing deferred acceptance returns \(M\) because every man ranks its assignment first. Every changed man contributes ratio \((n-1)/n\) and every changed woman ratio \(n\), whence \(P(T)/P(M)=(n-1)^k\). With \(k=n\), this is the global upper bound.

**Rigidity and count.** Assume \(n\ge3\). Because \(n-1>1\), equality in \(P(T)/P(M)\le(n-1)^k\le(n-1)^n\) requires \(k=n\). Each contributing man must realize equality in both elementary inequalities, forcing \(u_i(M)=n\) and \(u_i(T)=n-1\): his two partners are ranked first and second. Each contributing woman must have \(u_j(M)=1\) and \(u_j(T)=n\): her \(M\)-partner is last and her \(T\)-partner is first. Necessity follows. These same conditions suffice for stability of both matchings (all men rank \(M\) first; all women rank \(T\) first), as well as the Nash ratio. They uniquely determine \(M\) from men's first choices and \(T\) from women's first choices; hence \(T\) is the unique optimal stable matching in an extreme profile. For each of \(n!\) choices of \(M\), a disjoint \(T\) is a derangement relative to \(M\), giving \(D_n\) choices. Each man's first and second choices are fixed, and each woman's first and last choices are fixed; each of the \(2n\) agents has \((n-2)!\) remaining strict orders. No profile is counted twice because both matchings are uniquely recoverable. This proves the exact count.

## Verification
A standalone standard-library Python checker, `verify.py`, reconstructs the definitions rather than using precomputed tables. It independently implements men-proposing deferred acceptance, brute-force stability tests over all perfect matchings, and exact integer Nash products. Exhausting all \(16\) strict labeled profiles for \(n=2\) and all \(46656\) for \(n=3\), it verifies the bound for every stable alternative, the strict-loss count \(5424\) at \(n=3\), the maximum product ratio \(8\), and exactly \(12\) maximizing profiles. It checks explicit sharp constructions for all \(2\le n\le14\) and each \(2\le k\le n\). This finite execution corroborates, rather than replaces, the proof for arbitrary \(n\).

## Relationship to prior work
Gale and Shapley's classical theorem that deferred acceptance is proposer-optimal supplies the comparison premise. Desai, Rasheed, Ghalme, and Gujar (2026) formulate Nash social welfare for rank-induced stable marriage and give a polynomial-time algorithm to maximize it; their main theorems prove algorithmic correctness and running time. The present statement instead determines the exact *worst-case quantitative loss* of men-proposing deferred acceptance relative to their optimal stable objective, and completely classifies its equality cases. Jain and Vaish (2023/2024) investigate Nash-welfare maximization in more general two-sided cardinal-valuation matching, without the same stable-marriage constraint; those results do not provide this stable proposer-optimal comparison. General comparisons between egalitarian, sex-equal, rank-maximal, or regret-optimal stable matchings do not imply this exact multiplicative Nash-product bound.

## Limitations
This statement relies on **unit-spaced positive rank-induced utilities**. It does not assert a bound for arbitrary cardinal utilities, incomplete lists, ties, quotas, one-sided assignment, randomized procedures, or weighted agents. The exhaustive computations cover only small finite markets, and they are not used as the infinite proof. Relevant searched literature did not reveal a statement of the sharp ratio and equality classification, but historical priority is not guaranteed: an unindexed equivalent or an implicit corollary of older known inequalities remains possible. All scientific checking here is non-independent.

## References
1. D. Gale and L. S. Shapley. *College Admissions and the Stability of Marriage*. American Mathematical Monthly 69 (1962), 9–15.
2. P. Desai, Rasheed M, G. Ghalme, and S. Gujar. *Fair Stable Matching: A Nash Social Welfare Approach*. arXiv:2609.02354v1 (first posted 2026-09-02). https://arxiv.org/html/2609.02354v1
3. P. Jain and N. Vaish. *Maximizing Nash Social Welfare under Two-Sided Preferences*. arXiv:2312.09167v1 (2023). https://arxiv.org/html/2312.09167v1
