# A quantitative all-ranks record-age time-change principle for lazy random walks

## Finding
For a lazy random walk obtained by inserting independent Bernoulli pauses into any active path, **all normalized ranked record ages** are close, at once, to those of the active path at the deterministic effective horizon. The comparison is pathwise and depends only on the activity clock. For \(0<q\le1\), \(h=\lfloor qn\rfloor\ge1\), and \(D_n=\max_{0\le t\le n}|\sum_{i=1}^t B_i-qt|\), its bound, when at least one activity occurs, is
\[
\|P_n-Q_h\|_\infty\le \frac{3D_n}{qn}+\frac{2(D_n+1)}h.
\]
For symmetric absolutely continuous independent active increments this yields \(P_n\Rightarrow\operatorname{PD}(1/2,0)\) coordinatewise. The coupling to the active finite-horizon law has explicit \(O_q(n^{-1/2})\) mean error. No rate to the limiting law is asserted.

## Assumptions and scope
Let \(n\) be a positive integer, and fix \(q\in(0,1]\). Independent indicators \(B_1,\ldots,B_n\) have success probability \(q\); the active path \(Y_0,Y_1,\ldots\), of arbitrary increments, is independent of the indicators. Put \(A_t=\sum_{i=1}^t B_i\) and \(X_t=Y_{A_t}\) for \(0\le t\le n\). Initial time \(0\) is a record. A later time is a *strict upper record* exactly if the value exceeds every earlier value. At horizon \(t>0\), list the lengths between successive record epochs in \([0,t]\), followed by the age of the last, right-censored record. The final length can be zero. Rank these lengths decreasingly, divide by \(t\), and pad with zeroes to obtain an element of the nonnegative unit simplex in \(\ell^\infty\). Denote this profile for the lazy path by \(P_n\) and for the active path through index \(j\ge1\) by \(Q_j\). In the probabilistic corollary \(Y_j-Y_{j-1}\) are i.i.d. with a symmetric absolutely continuous distribution. The activity indicators and the increments are independent. We exclude \(q=0\) because its deterministic effective horizon is zero.

## Proof
**Clock-to-path matching.** Let \(m=A_n\ge1\). Enumerate the active strict record indices through \(m\) as \(0=r_0<r_1<\cdots<r_s\le m\). Define the physical arrival times \(T_k=\min\{t:A_t=k\}\) for \(1\le k\le m\), with \(T_0=0\). Every strict record of the lazy path occurs precisely at a corresponding \(T_{r_j}\). Thus active consecutive gaps are \(r_j-r_{j-1}\), with final gap \(m-r_s\), while lazy gaps are \(T_{r_j}-T_{r_{j-1}}\), with final gap \(n-T_{r_s}\). Since \(|A_t-qt|\le D_n\) at all endpoints and \(A_{T_k}=k\), each paired gap obeys
\[
\left|q\,\text{physical gap}-\text{active gap}\right|\le2D_n.
\]
This also holds for the censored final pair because \(|m-qn|\le D_n\). Moreover each active gap is at most \(m\), so comparison of physical gap divided by \(n\) and active gap divided by \(m\) gives
\[
\left|\frac{\text{physical gap}}n-\frac{\text{active gap}}m\right|
\le\frac{2D_n}{qn}+\frac{|m-qn|}{qn}
\le\frac{3D_n}{qn}.
\]
A common permutation matching bounds the sup-norm distance between their decreasing rearrangements, whence \(\|P_n-Q_m\|_\infty\le3D_n/(qn)\).

**Changing the active horizon.** For arbitrary positive integer horizons \(a,b\), the two unnormalized age lists from the *same* active path can be matched, zero padding if necessary, with corresponding entries differing by at most \(d=|a-b|\). Indeed, all completed gaps before \(\min(a,b)\) are unchanged. Only its last censored gap can be extended or become the first newly completed gap, adding at most \(d\); all subsequent newly completed gaps have length at most \(d\). The decreasing-rearrangement sup-norm inequality and a normalization comparison therefore give
\[
\|Q_a-Q_b\|_\infty\le \frac{2|a-b|}{\max(a,b)}\le\frac{2|a-b|}{b}.
\]
Set \(a=m\), \(b=h=\lfloor qn\rfloor\). Since \(|m-h|\le D_n+1\), the triangle inequality gives the displayed pathwise bound.

**Concentration and expectation.** The centered activity clock is a bounded-increment martingale. The exponential supermartingale and Hoeffding's lemma imply the two-sided maximal inequality
\[
\Pr(D_n>x)\le 2\exp(-2x^2/n)\qquad(x>0).
\]
The event \(m=0\) has probability \((1-q)^n\). On its complement insert \(x=\sqrt{(n/2)\log(2/\delta)}\) in the pathwise bound, proving the high-probability assertion. Integrating the maximal bound yields \(\mathbb E D_n\le\sqrt{\pi n/2}\). On the event \(m=0\) any two ranked normalized age profiles have sup-norm distance at most one, yielding the explicit expectation bound
\[
\mathbb E\|P_n-Q_h\|_\infty\le
\left(\frac3{qn}+\frac2h\right)\sqrt{\frac{\pi n}2}+\frac2h+(1-q)^n.
\]
The law of \(Q_h\) is the no-holding walk's law at deterministic horizon \(h\). The coupling expectation bounds the corresponding \(\ell^\infty\)-cost Wasserstein distance. At fixed \(q>0\), the right side is \(O_q(n^{-1/2})\).

**Limiting ranked law.** Under i.i.d. continuous symmetric active increments, Theorem 4 of Szabó and Vető, *Ages of records in random walks*, proves \(Q_h\Rightarrow\operatorname{PD}(1/2,0)\) in the coordinatewise/vague sense for censored final ages. Since \(h\to\infty\) and the coupling discrepancy tends to zero in probability, every fixed finite vector of ranked coordinates of \(P_n\) has the same limit. This is the stated convergence and makes no claim of a convergence rate to \(\operatorname{PD}(1/2,0)\).

## Verification
The proof is deterministic through the two comparison inequalities and stochastic only for the Bernoulli-clock concentration and the cited active-walk limit. The accompanying Python script `verify_rank_ages.py` tests \(118048\) finite instances exactly with `fractions.Fraction`: all nonempty activity subsets through horizon \(9\), every subset of active record times, and activity parameters \(1/4,1/2,3/4,1\). The output is `PASS: 118048 exact rational tests over masks, record-time patterns and holding probabilities`. Such tests corroborate only the stated finite inequalities and do not establish the infinite-horizon limit.

## Relationship to prior work
Majumdar, Mounaix and Schehr (first public preprint March 25, 2021) study exactly this lazy symmetric random walk model but quantify its record **number**, variance, Fano factor and two-time record indicators; their conclusion explicitly identifies record **age** statistics under holding as an open direction. Szabó and Vető (2015 preprint; 2016 journal) already prove the non-lazy ranked-age Poisson–Dirichlet limit; this result uses that theorem and does not claim to rediscover it. Régnier, Dolgushev and Bénichou (2023) study ages for non-Markovian scale-invariant walks. Their 2023 preprint *Full Record Statistics of 1d Random Walks* (2024 journal) gives a comprehensive renewal-transform calculus for multitime record counts and times, but its inspected development does not yield the finite-sample all-ranks Bernoulli-clock coupling or this explicit rate for arbitrary continuous symmetric active jumps. General renewal and time-change principles supply background; an unindexed equivalent quantitative inequality remains possible.

## Limitations
The error estimate is an upper bound, not a sharp constant or proven optimal rate. Its \(O_q(n^{-1/2})\) constant depends on fixed positive activity probability \(q\); no uniform assertion as \(q\downarrow0\). The limiting convergence is coordinatewise/vague, not an asserted total-variation or explicit-rate theorem for Poisson–Dirichlet. The result relies on strict records and inclusion of the final *censored* interval: it does not identify the laws for other conventions for the last record age. The 2024 full-record paper has broader multitime scope but does not address the same finite coupling; future prior-art review may uncover more closely related renewal time-change bounds.

## References
1. S. N. Majumdar, P. Mounaix and G. Schehr, *Universal record statistics for random walks and Lévy flights with a nonzero staying probability*, arXiv:2103.14062v1 (2021-03-25); J. Phys. A 54 (2021), 315002. https://arxiv.org/abs/2103.14062
2. R. Szabó and B. Vető, *Ages of records in random walks*, arXiv:1510.01152v2, Theorem 4; J. Stat. Phys. 165 (2016), 1086–1101. https://arxiv.org/pdf/1510.01152
3. L. Régnier, M. Dolgushev and O. Bénichou, *Record ages of non-Markovian scale-invariant random walks*, Nature Communications 14 (2023), 6288; arXiv:2305.09642. https://arxiv.org/abs/2305.09642
4. L. Régnier, M. Dolgushev and O. Bénichou, *Full-record statistics of one-dimensional random walks*, Phys. Rev. E 109 (2024), 064101; first preprint arXiv:2312.14885 (2023-12-22). https://arxiv.org/pdf/2312.14885
