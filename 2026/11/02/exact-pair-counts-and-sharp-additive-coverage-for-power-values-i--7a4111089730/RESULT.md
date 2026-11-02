# Exact pair counts and sharp additive coverage for power values in Galois rings

## Finding
Let \(R=\operatorname{GR}(p^m,p^{mf})\), \(q=p^f\), and \(P=\{x^d:x\in R\}\setminus\{0\}\). In the index-one case \(\gcd(d,q-1)=1\), the number \(N_2(b)\) of unordered two-element subsets of *distinct* members of \(P\) with sum \(b\) depends only on \(v_p(b)\). The formula below evaluates this number explicitly for every target, every characteristic and every ring length. It implies a sharp criterion for \(P+P\) to cover \(R\) with distinct summands:
\[
(\forall b\in R,\ N_2(b)>0)\iff
\begin{cases}
(q,m)\ne(3,1),&p\text{ odd},\\
m\ge2\text{ and }(q\ge4\text{ or }m>d),&p=2.
\end{cases}
\]
The binary residue-field case \(q=2\) exhibits a genuine length threshold: coverage is absent when \(m\le d\), but present for every \(m>d\).

## Assumptions and scope
Assume \(p\) is prime, \(m,f\ge1\), \(d\ge2\), \(p\nmid d\) and \(\gcd(d,q-1)=1\), with \(q=p^f\). Set \(S=\{jd: j\ge0,\ jd<m\}\) and \(L_s=(q-1)q^{m-s-1}\) for \(s\in S\). The valuation \(v_p(x)\) is the largest \(t<m\) for which \(x\in p^tR\) if \(x\ne0\), and \(v_p(0)=m\). Put \(t=v_p(b)\). Define
\[
A_t=\sum_{s\in S:s<t}L_s+\mathbf1_{\{t<m,t\in S\}}\Bigl((q-2)q^{m-t-1}+2\sum_{u\in S:u>t}L_u\Bigr).
\]
Define the diagonal term \(D_t\) as follows. If \(p\) is odd, \(D_t=1\) exactly when \(t<m\) and \(t\in S\); otherwise it is zero. If \(p=2,m=1\), \(D_t=q-1\) exactly when \(t=m\), otherwise zero. If \(p=2,m\ge2\), \(D_t=q\) exactly when \(1\le t<m\) and \(t-1\in S\); \(D_m=q-1\) exactly when \(m-1\in S\); otherwise it is zero. These cases do not overlap. Then, for **every** \(b\in R\),
\[\boxed{N_2(b)=\frac{A_t-D_t}{2}.}\]

## Proof
**1. Power-value valuation shells.** Every nonzero \(x\in R\) has form \(p^k u\) with a unit \(u\). Since \(p\nmid d\), raising to the \(d\)-th power is an automorphism on the finite principal-unit group, while the index-one condition makes it bijective on \(\mathbb F_q^\times\). Consequently every unit of \(R/p^rR\) is a \(d\)-th power for every \(r\le m\). It follows that \(P\) is the disjoint union of the **entire** nonzero valuation shells \(V_s=\{x\in R:v_p(x)=s\}\) over \(s\in S\); \(|V_s|=L_s\). This is the power-value decomposition in Gu, Proposition 1; only index one is used here.

**2. Ordered pair count.** Fix \(b\in R\) with \(v_p(b)=t\). If \(x,y\in P\) have distinct valuations, then \(v_p(x+y)=\min(v_p(x),v_p(y))\); hence such a pair can sum to \(b\) only when its minimum valuation is \(t\in S\), \(t<m\). For every \(u\in S\) with \(u>t\), choosing \(y\in V_u\) freely forces \(x=b-y\in V_t\). This accounts for \(2\sum_{u>t}L_u\) **ordered** pairs. If \(v_p(x)=v_p(y)=s\), then for \(s>t\) there are none; for \(s<t\), every \(x\in V_s\) has \(b-x\in V_s\), yielding \(L_s\) pairs; and for \(s=t<m\), the residues of \(x/p^t\) and \((b-x)/p^t\) must both be nonzero. There are \(q-2\) permissible nonzero residues, each lifting \(q^{m-t-1}\) times. Summing these mutually exclusive cases gives \(A_t\).

**3. Remove repeated summands.** A pair of distinct summands is counted twice in \(A_t\), whereas a diagonal pair corresponds to \(2x=b\) with \(x\in P\). If \(p\) is odd, multiplication by two is a unit automorphism, yielding one diagonal exactly when \(b\in P\). If \(p=2,m=1\), two annihilates the whole ring, giving \(|P|=q-1\) diagonal pairs for \(b=0\). If \(p=2,m\ge2\), multiplication by two carries every shell \(V_s\), \(s<m-1\), onto \(V_{s+1}\) with exactly \(q\) preimages per element; it sends \(V_{m-1}\) to zero, giving \(q-1\) nonzero preimages. This proves the given \(D_t\) and \(N_2(b)=(A_t-D_t)/2\). Both sides are nonnegative integers by this counting argument.

**4. Positivity, odd characteristic.** When \(q\ge5\), if \(t=0\) then the equal-unit-shell contribution after removing the possible diagonal is at least \(((q-2)q^{m-1}-1)/2\ge1\). For all \(t>0\) the whole unit shell contributes \(L_0=(q-1)q^{m-1}\) ordered pairs and there is no odd-characteristic diagonal, so positivity follows. The only remaining odd \(q\) is \(q=3\). At \(m=1\), the only two distinct units sum to zero, so nonzero targets have count zero. At \(m\ge2\), for unit targets \(((q-2)q^{m-1}-1)/2\ge1\), and all nonunit targets again have the \(L_0\) contribution.

**5. Positivity, characteristic two.** At \(m=1\), every \(x+x=0\), so a *distinct* two-element subset cannot sum to zero. For \(m\ge2,q\ge4\), unit targets have at least \((q-2)q^{m-1}/2>0\) representations. For nonunit targets the unit shell supplies \(L_0\) ordered pairs; at most \(q\) of these are diagonal, leaving at least \(((q-1)q^{m-1}-q)/2>0\). Finally take \(q=2\), so \(d\) is odd and \(d\ge3\). If \(m\le d\), then \(P\) is precisely the unit shell; the sum of two units cannot be a unit. If \(m>d\), the new shell \(V_d\) exists: every unit target is the sum of one unit and one value from \(V_d\). Every nonunit target receives \(L_0=2^{m-1}\) ordered equal-unit-shell pairs, with at most two diagonal pairs; as \(m>d\ge3\), \((2^{m-1}-2)/2>0\). Thus all targets, including zero, are covered. This proves the sharp criterion.

## Verification
Run `python3 verify_pair_counts.py` from this package. It constructs finite rings directly using integer coefficient arithmetic modulo \(p^m\), enumerates distinct power values and unordered pairs, and independently compares each target's exact count to the displayed formula. It checks both ordinary residue rings and unramified quadratic extensions in both odd and binary characteristics. The executed check passed **234 target equalities across 12 ring instances**. These finite tests do not establish the universal theorem; the proof above does.

## Relationship to prior work
Zijie Gu, *Subset sums of power values over Galois rings*, arXiv:2610.28837v1 (first public 2026-10-20), defines the identical set \(P\) and same distinct-element subset count. Proposition 1 supplies the complete valuation-shell decomposition for index one; equation (17) is an **exact character-inversion formula for all subset sizes and all targets**, therefore already determines each specific value of \(N_2(b)\) formally. Appendix B explicitly evaluates the index-one *field* case. The present result does not claim novelty for those general identities or field evaluations: it evaluates the length-unrestricted index-one pair counts as simple valuation polynomials and establishes the complete, sharp finite-ring **coverage equivalence**, including the binary threshold at \(m=d+1\), which is not among the source's stated results. Unlike the generic character identity, no character enumeration is required. The earlier finite-ring distinct-coordinate sieve of Li and Wan is also broader as an algorithmic identity, and does not itself state the resulting valuation-stratified threshold.

## Limitations
The hypotheses \(p\nmid d\) and \(\gcd(d,q-1)=1\) are essential to the full-shell simplification; no classification is claimed when the nonzero residue-field powers form a proper subgroup. The finding provides no general formula for subset sizes exceeding two and no new asymptotic beyond Gu's published results. The broad existing exact character-inversion formula is a material originality risk; the distinct contribution asserted here is its explicit evaluation and sharp global finite-parameter positivity classification. No independent mathematical audit has been performed.

## References
1. Zijie Gu, *Subset sums of power values over Galois rings*, arXiv:2610.28837v1, publicly submitted 2026-10-20. https://arxiv.org/html/2610.28837v1
2. Li and Wan, general finite-ring distinct-coordinate sieve, Lemma 3.1, as cited and formulated in Gu, Sections 1 and 5.
3. Ding and Zhou, odd-characteristic length-two power-value counting formulas, as cited and compared in Gu, Appendix A.
