# A binomial critical window for strong group representation in random approval elections

## Finding

Fix integers \(m>k\geq2\) and \(n\geq1\). Let each of \(n\) voters independently approve each of \(m\) candidates with probability \(p\), where \(0<p<1\). A candidate is *cohesive* when at least \(\lceil n/k\rceil\) voters approve it. Write \(R\) for the number of cohesive candidates and define

\[
q_n=\Pr\{\operatorname{Bin}(n,p)\geq\lceil n/k\rceil\},\qquad
\varepsilon_n=m\binom{m-1}{k}\bigl(1-p(1-p)^k\bigr)^n.
\]

**Theorem (finite-sample reduction and optimal-score law).** Exactly \(R\sim\operatorname{Bin}(m,q_n)\). With probability at least \(1-\min\{1,\varepsilon_n\}\), *simultaneously* for Strong Justified Representation (SJR) and Semi-Strong Justified Representation (SSJR), the optimum normalized fraction of cohesive candidates represented by a \(k\)-seat committee is

\[
f_k(R)=\begin{cases}1,&R=0,\\\min\{k,R\}/R,&R>0.\end{cases}
\]

On the same event, either axiom has a feasible committee if and only if \(R\leq k\). Any committee selecting \(\min\{k,R\}\) cohesive candidates (and, if needed, filling the remaining seats arbitrarily) is optimal for both score functions. For either axiom, the exact binomial benchmark \(B_n\) satisfies

\[
B_n:=\sum_{j=0}^{k}\binom{m}{j}q_n^j(1-q_n)^{m-j}
\;\leq\;\Pr\{\text{axiom feasible}\}\;\leq\;B_n+\varepsilon_n.
\]

For the random optimum score \(T_n\) of either axiom, \(\Pr\{T_n\neq f_k(R)\}\leq\min\{1,\varepsilon_n\}\) and \(0\leq\mathbb E[T_n]-\mathbb E[f_k(R)]\leq\min\{1,\varepsilon_n\}\). These are finite-sample results valid even if \(m,k,p\) vary with \(n\); useful approximation requires \(\varepsilon_n\) small.

**Critical window.** For fixed \(m>k\geq2\), set \(p_n=1/k+\theta/\sqrt n\) with fixed real \(\theta\), and let \(q_\theta=\Phi\bigl(\theta/\sqrt{(1/k)(1-1/k)}\bigr)\), where \(\Phi\) is the standard Gaussian distribution function. For both SJR and SSJR,

\[
\Pr\{\text{axiom feasible}\}\longrightarrow
\sum_{j=0}^k\binom{m}{j}q_\theta^j(1-q_\theta)^{m-j},
\quad
T_n\overset{d}{\longrightarrow}f_k(\operatorname{Bin}(m,q_\theta)).
\]

At the critical point \(\theta=0\), an example with \(m=8,k=3\) has limiting feasibility probability \(93/256\) and limiting expected optimal score \(55133/71680\). For fixed \(0<p<1/k\), feasibility tends to one and optimal score tends to one; for fixed \(1/k<p<1\), feasibility tends to zero and optimal score tends to \(k/m\). The fully unanimous endpoint \(p=1\) is exceptional: both axioms are feasible with score one for every \(n\).

## Assumptions and scope

The axiom names refer only to *one-cohesive* groups and the candidate-based maximization scores of Chingoma, Grossi, Lindeboom and Maly (2026), Definitions 2--8. They are **not** statements about the stronger all-\(\ell\) variants of justified representation. Each approval edge is an independent Bernoulli random variable, with the same probability across voters and candidates. Every committee has exactly \(k\) distinct candidates. The score when no candidate is cohesive is set to one by the vacuous-satisfaction convention; the published score quotient has an empty denominator in this case. Feasibility does not depend on this convention.

For each candidate \(c\), let \(N_c\) be its supporter set. The cohesive-candidate set is \(H=\{c:|N_c|\geq n/k\}\). An elected committee \(W\) represents cohesive candidate \(c\) for SJR if \(N_c\subseteq N_d\) for some \(d\in W\); it represents \(c\) for SSJR if \(N_c\subseteq\bigcup_{d\in W}N_d\). The normalized score is the fraction of cohesive candidates meeting the respective criterion.

## Proof

1. **One-cohesive reduction.** Every nonempty one-cohesive voter group is contained in \(N_c\) for some cohesive candidate \(c\). If a committee represents the entire group \(N_c\), then it also represents any subgroup of it. Conversely \(N_c\) itself is cohesive. For SJR, the required common elected approval is precisely \(N_c\subseteq N_d\) for some elected \(d\); for SSJR, individual coverage is precisely \(N_c\subseteq\bigcup_{d\in W}N_d\). These identify the source's candidate scores and are equivalent to its axioms when score one is attained.

2. **Binomial count.** For each fixed \(c\), \(|N_c|\sim\operatorname{Bin}(n,p)\). Different candidates' columns are independent, so their cohesion indicators are independent Bernoulli with parameter \(q_n\). Thus \(R\sim\operatorname{Bin}(m,q_n)\) with no asymptotic approximation.

3. **Uniform separation event.** Consider any \(c\notin W\) with \(|W|=k\). A voter approves \(c\) but approves none of \(W\) with probability \(p(1-p)^k\). Independently across voters, the chance that no such witness exists is \(\bigl(1-p(1-p)^k\bigr)^n\). There are precisely \(m\binom{m-1}{k}\) ordered pairs \((c,W)\). A union bound gives a common event \(E_n\) with \(\Pr(E_n^c)\leq\varepsilon_n\) on which **every** unselected \(c\) has \(N_c\not\subseteq\bigcup_{d\in W}N_d\). This also prohibits representation by any single elected candidate.

4. **Exact optimization on \(E_n\).** Every selected cohesive \(c\) represents itself under both axioms. The separation event ensures no unselected cohesive candidate receives credit under either axiom. Therefore every committee receives score \(|W\cap H|/R\) if \(R>0\), or one by convention if \(R=0\). Its maximum is \(f_k(R)\). Choose as many cohesive candidates as possible to attain this value; any leftover seats can be filled arbitrarily. Full satisfaction occurs exactly when \(R\leq k\). This is a statement about *every committee simultaneously*, not just one favored algorithm.

5. **Finite-sample bounds.** On any profile, \(R\leq k\) implies both axioms are satisfied by electing every cohesive candidate. On \(E_n\), the converse holds. Combining with the exact distribution of \(R\) gives \(B_n\leq\Pr\{\mathrm{feasible}\}\leq B_n+\varepsilon_n\). Likewise, \(T_n\geq f_k(R)\) deterministically, with equality on \(E_n\) and both in the unit interval. Thus their difference in expectation and their probability of inequality are at most \(\Pr(E_n^c)\).

6. **Limits.** At \(p_n=1/k+\theta/\sqrt n\), the triangular-array binomial CLT gives \(q_n\to\Phi\bigl(\theta/\sqrt{(1/k)(1-1/k)}\bigr)\), with the ceiling contributing only a vanishing lattice correction. Since \(p_n\to1/k\in(0,1)\), the positive witness probability is bounded below for large \(n\); \(\varepsilon_n\to0\) exponentially at fixed \(m,k\). The binomial polynomial and the finite-support function \(f_k\) therefore yield the displayed probability and score laws. If \(p\) is fixed strictly below/above \(1/k\), the weak law gives \(q_n\to0\)/\(1\), respectively; the same separation argument applies. At \(p=1\) all candidates have identical full supporter sets, so every committee satisfies both axioms, as stated.

## Verification

Run `python3 verify_sjr.py` from the directory containing that file. The script uses exact rational arithmetic and checks all \(2^{nm}\) approval profiles for the five parameter triples \((n,m,k)=(2,3,2),(3,3,2),(3,4,2),(4,4,2),(3,5,2)\). It recomputes cohesive counts, optimal committee scores, both axiom feasibility conditions, the universal separation event, and the finite union bounds from definitions. See `verification_output.txt` for actual output. These small exhaustive checks corroborate, but do not replace, the all-size analytic proof. As a critical-point arithmetic check, direct exact binomial summation for \((m,k)=(8,3)\) gives feasibility \(93/256\) and expected optimum \(55133/71680\).

## Relationship to prior work

Chingoma et al. (2026, arXiv:2609.29332v1) define and study the relevant one-cohesive SJR and SSJR maximization scores, establish worst-case computational limits, and report empirical feasibility and near-optimal greedy scores on real and resampled datasets; their Sections 2--4, 8.1 and supporting appendices do not supply this independent-Bernoulli finite-sample law, critical-window distribution, or optimizer equality. Here the group-representation definitions, not the scores themselves, come from that paper.

Han, Tao, Xia, Zhang and Zhou (2025, arXiv:2510.18718v1) study **average** justified representation under a Bernoulli approval model and find a two-threshold feasibility phase diagram. Their all-cohesive-level mean-utility requirement is distinct from one-cohesive SJR and SSJR unanimity/individual-coverage requirements; the AJR phase diagram therefore does not imply the present optimal-score or binomial feasibility laws. Both use the standard independent-approval benchmark. This result does not assert novelty for the binomial CLT or elementary union bound in isolation; its subject is their exact application to the two distinct group-diversity objectives and resulting optimal-score characterization.

## Limitations

The quantitative finite-sample error can exceed one and becomes informative only when the no-covering event is likely; it is not a sharp failure probability. The critical asymptotic regime holds for fixed \(m,k\); arbitrary growth requires the stated \(\varepsilon_n\to0\) control plus separate analysis of \(R\). Strongly correlated approval patterns, p near one with vanishing \(n(1-p)^k\), and the boundary \(p=1\) are not covered by the nondegenerate asymptotics. The all-\(\ell\) variants of SJR/SSJR, ordinary JR, EJR, AJR, and non-Bernoulli correlated elections are separate questions. The score convention at \(R=0\) is explicitly added. Publication priority has not been independently established, and direct equivalence in uninspected literature remains possible.

## References

1. Julian Chingoma, Davide Grossi, Feline Lindeboom and Jan Maly, *Diverse Representation in Approval-Based Committee Voting*, arXiv:2609.29332v1, initially posted 24 September 2026; https://arxiv.org/abs/2609.29332 ; Definitions 2--8, Sections 4, 8.1, Appendix B and F.
2. Qishen Han, Biaoshuai Tao, Lirong Xia, Chengkai Zhang and Houyu Zhou, *Likelihood of the Existence of Average Justified Representation*, arXiv:2510.18718v1, initially posted 21 October 2025; https://arxiv.org/abs/2510.18718 ; Section 2 (definition and threshold results).
