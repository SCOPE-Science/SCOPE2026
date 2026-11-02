# The half-budget Hare-core threshold and central-trinomial census for cyclic two-approval elections

## Finding

Consider a cyclic approval election with \(n\ge 2\) voters and \(n\) candidates, in which voter \(i\) approves exactly the adjacent candidates \(c_i,c_{i+1\bmod n}\). The utility of a candidate set is its number of approved candidates. For every committee size \(1\le k\le n\), with the strict-preference Hare core defined below, the following hold.

1. If \(2k<n\), **every** size-\(k\) committee is in the Hare core.
2. If \(n=2k\), a size-\(k\) committee is in the Hare core **exactly when its complement has no run of three cyclically consecutive candidates**.
3. At \(n=2k\), the number of labeled core committees is
   \[
   C_k=2[z^k](1+z+z^2)^k
   =2\sum_{j=0}^{\lfloor k/2\rfloor}\frac{k!}{(j!)^2(k-2j)!}.
   \]
   Among all \(\binom{2k}{k}\) committees, their exact fraction is \(C_k/\binom{2k}{k}\), with asymptotic behavior
   \[
   \frac{C_k}{\binom{2k}{k}}\sim\sqrt{3}\,(3/4)^k\qquad(k\to\infty).
   \]

The first failure **within the half-budget family** occurs at \(n=6,k=3\): selecting three cyclically consecutive candidates leaves three unselected consecutive candidates. A one-candidate alternative then blocks it.

## Assumptions and scope

The voters and candidates are each identified with \(\mathbb Z/n\mathbb Z\). Voter \(i\) approves \(A_i=\{c_i,c_{i+1}\}\) (indices cyclic), so \(u_i(X)=|A_i\cap X|\). A committee is a candidate subset \(W\) of cardinality exactly \(k\). It is blocked if there are a nonempty candidate set \(T\subseteq C\) and a voter coalition \(S\subseteq N\) with
\[
 |S|k\ge n|T|,\qquad u_i(T)>u_i(W)\quad\text{for every }i\in S.
\]
No disjointness of \(T\) from \(W\) is assumed. An arbitrary strict improvement is required for **every** blocking voter. For \(n=2\), both voters approve both candidates, and the same formula remains valid. The results make no statement about the regime \(2k>n\), alternative core notions, or arbitrary noncyclic ballots.

## Proof

**A universal incidence bound.** Each candidate is approved by exactly two voters; therefore for every candidate set \(T\),
\[
\sum_{i\in N}u_i(T)=2|T|.
\]
If voter \(i\) strictly improves from \(W\) to \(T\), integer-valued utility implies \(u_i(T)\ge u_i(W)+1\ge1\). Thus the number of strictly improving voters is at most \(2|T|\). If \(n/k>2\), every affordable nonempty deviation requires strictly more than \(2|T|\) voters. Consequently every committee lies in the core, proving the first statement.

**Exact equality at half budget.** Suppose \(n=2k\) and \(T,S\) block \(W\). Affordability gives \(|S|\ge2|T|\), whereas the incidence bound gives \(|S|\le2|T|\). Hence \(|S|=2|T|\), and equality must hold throughout
\[
2|T|=\sum_i u_i(T)\ge\sum_{i\in S}u_i(T)
\ge\sum_{i\in S}(u_i(W)+1)\ge |S|=2|T|.
\]
It follows that every voter in \(S\) approves exactly one member of \(T\) and **none** of \(W\), and no voter outside \(S\) approves a member of \(T\). Pick any \(c_j\in T\). The two voters who approve it are \(j-1\) and \(j\), and both belong to \(S\); consequently their approval pairs \(\{c_{j-1},c_j\}\) and \(\{c_j,c_{j+1}\}\) avoid \(W\). Thus the three cyclically consecutive candidates \(c_{j-1},c_j,c_{j+1}\) are absent from \(W\). This proves necessity.

Conversely, suppose such a vacant triple exists. Set \(T=\{c_j\}\) for its middle candidate, and \(S=\{j-1,j\}\). Both voters have utility zero from \(W\) and utility one from \(T\). Furthermore \(|S|k=2k=n|T|\). Hence \(S,T\) block \(W\). This proves the exact characterization. The same vacant-triple condition is also precisely a violation of ordinary justified representation (JR) at this quota: two unrepresented adjacent voters jointly approve the triple’s middle candidate. Hence JR and the Hare core coincide for this particular half-budget cyclic profile.

**Counting.** At \(n=2k\), every admissible committee has exactly \(k\) selected and \(k\) unselected candidates. Mark one of its \(k\) selected candidates as a root and traverse clockwise. The numbers \(g_1,\ldots,g_k\) of excluded candidates after successive selected candidates are in \(\{0,1,2\}\), because a run of length three is forbidden, and \(g_1+\cdots+g_k=k\). Conversely, choosing a root position (\(2k\) choices) and any such ordered gap vector constructs a unique rooted eligible committee. Each unrooted committee occurs exactly \(k\) times, giving \(C_k=(2k/k)[z^k](1+z+z^2)^k\). The displayed factorial sum follows by taking \(j\) zero-gaps, \(j\) two-gaps and \(k-2j\) one-gaps.

**Asymptotic incidence.** Let \(X_1,\ldots,X_k\) be independent uniform random variables on \(\{0,1,2\}\). They have mean \(1\), variance \(2/3\), and span one. The standard lattice local central limit theorem gives
\[
 [z^k](1+z+z^2)^k
 =3^k\Pr(X_1+\cdots+X_k=k)
 \sim \frac{3^k\sqrt3}{2\sqrt{\pi k}}.
\]
Stirling's formula gives \(\binom{2k}{k}\sim4^k/\sqrt{\pi k}\). Taking their ratio, with the counting factor two, proves \(C_k/\binom{2k}{k}\sim\sqrt3(3/4)^k\).

## Verification

Execute `python3 verify.py` using Python 3. The standalone program enumerates **all** size-\(k\) committees for half-budget cases \(k=1,\ldots,6\), **all** nonempty candidate proposals of size at most \(k\), and checks the core criterion by enumerating all strictly improving voters. It independently checks the cyclic-gap criterion and the central-trinomial count. It also tests every size-\(k\) committee with \(2k<n\le9\). The exact counts for \(k=1,2,3,4,5,6\) are \(2,6,14,38,102,282\), respectively. The file `verification_output.txt` records the observed results. Enumeration corroborates, but does not replace, the general proof and the asymptotic argument.

## Relationship to prior work

Becker, Greger, and Peters established existence of a Hare-core committee for **all** approval elections and give a polynomial-time construction. That general existence theorem does not identify **which** committees are core-stable in the present cyclic domain or count them. Pierczyński and Skowron studied core existence under restricted preference domains; the cyclic two-approval exact membership rule is different from their general existence guarantees. Berker and collaborators formulated core membership and least-core feasibility using integer programs; that generic formulation does not supply the specialized closed count. Fang studied exact margins for candidate-disjoint nested chains, rather than overlapping cyclic approval pairs. The present result supplies a sharp *all-committees versus some-committees* transition, an explicit forbidden-run characterization, and an exact central-trinomial count in one fixed domain.

## Limitations

This result concerns the strict Hare core for the precisely specified cyclic two-approval family only. It does not characterize the super-half-budget regime, arbitrary ballots, heterogeneous approval weights, Droop core, or the stronger core+ condition. The coefficient identity is standard combinatorics; novelty, if sustained, is in the stability characterization and its use to obtain the complete census, not discovery of the central-trinomial numbers. Exhaustive finite enumeration is not an infinite proof. Source inspection does not exclude a similar characterization hidden in unindexed or inaccessible prior work.

## References

- P. Becker, M. Greger, D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912v1, first posted September 10, 2026. https://arxiv.org/html/2609.11912v1
- G. Pierczyński, P. Skowron, *Core-Stable Committees under Restricted Domains*, arXiv:2108.01987, 2021. https://arxiv.org/abs/2108.01987
- R. E. Berker et al., *On the Edge of Core (Non-)Emptiness: An Automated Reasoning Approach to Approval-Based Multi-Winner Voting*, arXiv:2512.16895, 2025. https://arxiv.org/abs/2512.16895
- J. Fang, *Exact Sizewise Least Cores for Candidate-Disjoint Approval Chains*, arXiv:2610.06871, 2026. https://arxiv.org/abs/2610.06871
