# An exact Nash-stability spectrum and reciprocity transition on signed stars

## Finding

Consider a directed signed additively separable hedonic game whose nonzero valuation graph is a star with one hub and \(n\ge1\) labeled leaves. Each leaf assigns the hub either \(+1\) or \(-1\), and the hub independently has a signed valuation in \(\{-1,+1\}\) for each leaf; all leaf-to-leaf valuations are zero. For each leaf \(i\), write \(a_i\) for its valuation of the hub and \(b_i\) for the hub's valuation of that leaf. Put
\[
U=\sum_{i:a_i=+1}b_i,\qquad R=\sum_{i:a_i=-1}b_i.
\]
**The equilibrium-existence criterion is exact:** a Nash-stable partition exists if and only if
\[
U>0\quad\text{or}\quad(U=0\text{ and }R\le0).
\]
Every Nash-stable partition has one coalition containing the hub and precisely the leaves with \(a_i=+1\). All other blocks \(B\) consist of leaves with \(a_i=-1\), and must satisfy \(\sum_{i\in B}b_i\le U\). This condition completely characterizes the set of equilibria.

Write \(p,q,r,s\) for the respective numbers of leaves with \((a_i,b_i)=(+1,+1),(+1,-1),(-1,+1),(-1,-1)\), so \(U=p-q\) and \(R=r-s\). If \(U\ge0\), the exact number of Nash-stable partitions is
\[
F_U(r,s)=r!s!\,[x^r y^s]\exp\!\left(\sum_{\substack{i,j\ge0\\i+j\ge1\\i-j\le U}}\frac{x^i y^j}{i!j!}\right).
\]
If \(U<0\), this number is zero. In particular, for \(s=0\) and \(U\ge1\), it is the restricted Bell number counting partitions of \(r\) labeled objects into blocks of size at most \(U\).

Now independently sample the leaves: \(a_i\) is an unbiased sign, and \(b_i=a_i\) with probability \(\rho\in[0,1]\), otherwise \(b_i=-a_i\). Let \(P_n(\rho)\) be the probability of a Nash-stable partition. Then
\[
\begin{aligned}
&\rho>\tfrac12:\quad P_n(\rho)\longrightarrow1,\\
&\rho<\tfrac12:\quad P_n(\rho)\longrightarrow0,
\end{aligned}
\]
with error probability bounded by \(\exp[-n(2\rho-1)^2/8]\). At the sharp window \(\rho_n=\tfrac12+c/\sqrt n\), for every fixed real \(c\),
\[
P_n(\rho_n)\longrightarrow\Phi(\sqrt2\,c),
\]
where \(\Phi\) is the standard Gaussian distribution function. At exact critical reciprocity,
\[
P_n(\tfrac12)=
\begin{cases}
\tfrac12,&n\text{ odd},\\
\tfrac12+\tfrac12\binom{n}{n/2}^{\!2}4^{-n},&n\text{ even}.
\end{cases}
\]
For even \(n\), this is \(\tfrac12+1/(\pi n)+O(n^{-2})\).

## Assumptions and scope

A coalition structure is a partition of the \(n+1\) agents into nonempty, unlabeled blocks. An agent's utility is the sum of their outgoing valuations for other agents in their own coalition; a singleton has utility zero. A unilateral Nash deviation means strictly improving utility by becoming a singleton or by joining any existing other coalition without the permission of its members. Ties are not deviations. All displayed classification and counting results hold for **every** signed instance and every integer \(n\ge1\). The probabilistic results apply only to the explicitly stated independent, identically distributed correlated-sign model, with \(\rho\) allowed to vary with \(n\) in the displayed critical window. No symmetry of valuations across a hub-leaf edge is assumed.

## Proof

**1. Mandatory hub coalition.** Any leaf whose \(a_i=+1\) must belong to the hub's coalition: otherwise joining it improves that leaf's utility from zero to one. Any leaf whose \(a_i=-1\) must not belong to it: otherwise becoming a singleton improves the leaf's utility from negative one to zero. Consequently the hub's current utility must be \(U\). It cannot profitably become a singleton exactly when \(U\ge0\), and cannot profitably move to any outsider block \(B\) exactly when \(\sum_{i\in B}b_i\le U\). Every leaf already has maximal utility among coalitions containing or excluding the hub: a positive leaf has utility one, and a negative leaf has zero. This proves necessity and sufficiency of the complete partition characterization.

**2. Existence.** If \(U\ge1\), place each outsider in its own block: its hub valuation is at most one, so all block sums are at most \(U\). If \(U=0\) and \(R\le0\), put all outsiders in one block (or use no outsider block when there are no outsiders), whose hub valuation is \(R\). If \(U<0\), the hub would leave. If \(U=0\) and \(R>0\), the sums over all outsider blocks add to \(R>0\), so some block has positive sum and the hub would join it. These cases establish the criterion.

**3. Exact counting.** For \(U\ge0\), each outsider block contains \(i\) positive and \(j\) negative hub-valued leaves, with \(i+j\ge1\) and \(i-j\le U\). The labeled-set exponential formula for unordered partitions into such blocks gives \(F_U(r,s)\). An elementary independent recurrence for \(r\ge1\) is
\[
F_U(r,s)=\sum_{i=1}^{r}\sum_{j=0}^{s}\mathbf1_{\{i-j\le U\}}\binom{r-1}{i-1}\binom{s}{j}F_U(r-i,s-j),
\]
with \(F_U(0,s)=B_s\), the unrestricted Bell number, and \(F_U(0,0)=1\). The recurrence counts the block containing one distinguished positively valued outsider. Thus the coefficient formula requires no computational approximation.

**4. Concentration and window.** In the random model, write \(U=\sum_{i=1}^{n}X_i\) with \(X_i=b_i\mathbf1_{\{a_i=+1\}}\). These variables are independent, take values in \(\{-1,0,+1\}\), and satisfy
\[
\mathbb E X_i=\rho-\tfrac12=\tfrac12(2\rho-1),\qquad
\operatorname{Var}(X_i)=\tfrac12-(\rho-\tfrac12)^2.
\]
The event \(\{U>0\}\) implies existence and the event \(\{U<0\}\) implies nonexistence; ambiguity is confined to \(U=0\). Hoeffding's inequality for the range of length two yields the claimed exponential bound on the wrong-sign event, including equality. When \(\rho_n=1/2+c/\sqrt n\), the triangular-array central limit theorem gives \(U/\sqrt n\Rightarrow N(c,1/2)\). The same convergence implies \(\Pr(U=0)\to0\), since the limiting normal law has no atom. Sandwiching the existence event between \(\{U>0\}\) and \(\{U\ge0\}\) proves the Gaussian crossover.

**5. Critical parity.** When \(\rho=1/2\), the signs \((a_i,b_i)\) are independent and uniform. Simultaneously reversing all \(b_i\) reverses both \(U\) and \(R\) while preserving their joint law. Hence
\[
\Pr(\mathrm{NS})=\Pr(U>0)+\Pr(U=0,R\le0)
=\frac12+\frac12\Pr(U=0,R=0).
\]
For odd \(n\), \(U+R=\sum b_i\) is odd, so the joint-zero event is impossible. For \(n=2m\), configurations with \(U=R=0\) have \(j\) leaves of each of the two signs in the positive-\(a\) group and \(m-j\) leaves of each sign in the negative-\(a\) group. Their count is
\[
\sum_{j=0}^{m}\frac{(2m)!}{j!^2(m-j)!^2}
=\binom{2m}{m}\sum_{j=0}^{m}\binom mj^2
=\binom{2m}{m}^2,
\]
by Vandermonde's identity. Dividing by \(4^{2m}\) yields the exact probability. Stirling's formula gives the parity correction \(1/(\pi n)+O(n^{-2})\).

## Verification

The included standard-library program `verify.py` directly constructs every coalition partition and applies the original strict unilateral Nash inequalities for every signed instance with at most five leaves. It then compares this independent test with the structural characterization, the labeled-block recurrence and the existence criterion. The run checked 1,365 signed profiles and 222,233 game-partition pairs with all assertions passing. A separate exact-rational section checks all 30 combinations of one to six leaves and five reciprocity values \(0,1/4,1/2,3/4,1\), including the exact parity formula. Reproduce with `python verify.py`. Finite checks corroborate but do not prove the universal or limiting results, which follow from the arguments above.

## Relationship to prior work

Hanaka and Lampis (2022) prove strong NP-hardness of Nash-stability existence on star interaction graphs when directed weights are unrestricted integers; that result neither implies nor excludes an exact classification for the present two-unit-weight restriction. Brandt, Bullinger and Tappe (2022) analyze single-agent stability and restricted utility alphabets on general interaction graphs, without the signed-star equilibrium spectrum shown here. Igarashi and Elkind (2016) consider a different graph-constrained coalition model requiring connected feasible coalitions; their star hardness and restricted deviations do not give the unrestricted signed-star count here. Bullinger (2022) focuses primarily on contractual and majority-consent stability variants, rather than this exact unconstrained Nash enumeration. Bullinger and Kraiczy (2024) show that Nash-stable partitions become rare in dense random hedonic games with independently sampled pairwise valuations; their complete-interaction random model is mathematically distinct from a sparse star with correlated reciprocal signs. Symmetric additive games guarantee existence as a special case, consistent with \(\rho=1\), but do not imply the general threshold, parity or counting formulas. The labeled-partition exponential formula, central limit theorem, Hoeffding inequality and Vandermonde identity are standard tools rather than claimed discoveries.

## Limitations

This theorem requires a star, zero leaf-leaf utilities, ±1 hub-leaf valuations and Nash deviations without consent. Its stochastic phase transition is not asserted for dense graphs, arbitrary weight magnitudes, unequal leaf types or other stability concepts. Exact combinatorial enumeration does not imply general complexity statements. The survey of relevant publications cannot exclude every specialist or unindexed preprint; a subsequent independent priority review remains necessary. No independent external validation is claimed.

## References

1. Tesshu Hanaka and Michael Lampis, *Hedonic Games and Treewidth Revisited*, arXiv:2202.06925, initial public version 2022-02-14, https://arxiv.org/abs/2202.06925 .
2. Felix Brandt, Martin Bullinger and Leo Tappe, *Single-Agent Dynamics in Additively Separable Hedonic Games*, AAAI 2022, https://doi.org/10.1609/aaai.v36i5.20415 .
3. Martin Bullinger and Sonja Kraiczy, *Stability in Random Hedonic Games*, arXiv:2406.01373, initial public version 2024-06-03, https://arxiv.org/abs/2406.01373 .
4. Ayumi Igarashi and Edith Elkind, *Hedonic Games with Graph-restricted Communication*, AAMAS 2016, https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p242.pdf .
5. Martin Bullinger, *Boundaries to Single-Agent Stability in Additively Separable Hedonic Games*, MFCS 2022, https://doi.org/10.4230/LIPIcs.MFCS.2022.26 .
6. Standard results used: exponential formula for labeled set partitions; Hoeffding's inequality; the triangular-array central limit theorem; Vandermonde's identity; Stirling's formula.
