# Normality of multi-agent someone-knows: a partition census and Poisson agent threshold

## Finding
Fix a nonempty finite set of worlds \(W\) of size \(n\) and \(r\geq 3\) epistemic agents whose accessibility relations \(E_1,\ldots,E_r\) are equivalence relations. Interpret the bundled operator \(\mathbb S\varphi:=\bigvee_{i=1}^{r}K_i\varphi\), and write \(R:=\bigcap_{i=1}^{r}E_i\). The following conditions are equivalent:

1. The normal modal distribution schema \(\mathbb S(p\to q)\to(\mathbb S p\to\mathbb S q)\) is valid under **every** valuation at **every** world.
2. At every world \(w\), some agent's information cell \(E_i[w]\) equals the distributed-knowledge cell \(R[w]\).
3. Every block of \(R\) is an entire block of at least one \(E_i\).

Under these conditions, \(\mathbb S\) agrees with the ordinary \(\mathsf{S5}\) box for \(R\), including when nested in formulas.

Let \(B_m\) be the \(m\)-th Bell number, \(\operatorname{Stir}_2(n,t)\) the Stirling number of the second kind, and let \(L_{n,r}\) count **ordered** \(r\)-tuples of equivalence relations on an \(n\)-element labelled set satisfying the equivalent conditions. For \(t\geq0\) put
\[
A_{t,j}=\sum_{k=0}^{j}(-1)^k\binom{j}{k}B_{t-k},\qquad
H_r(t)=\sum_{j=0}^{t}(-1)^j\binom tj(A_{t,j})^r.
\]
Then the exact finite census is
\[
\boxed{L_{n,r}=\sum_{t=0}^{n}\operatorname{Stir}_2(n,t)H_r(t)},\qquad
\sum_{n\geq0}L_{n,r}\frac{z^n}{n!}=
\sum_{t\geq0}H_r(t)\frac{(e^z-1)^t}{t!}.
\]
The first values at three agents, for \(n=1,\ldots,6\), are
\[
1,\quad 8,\quad 89,\quad 1449,\quad 31468,\quad 864347.
\]

There is also a sharp **growing-agent** law. For each \(n\), choose \(r_n\) independent uniformly random equivalence relations on \([n]\), let \(s_n=B_{n-1}/B_n\), and suppose
\[
r_ns_n-\log n\longrightarrow c\in\mathbb R.
\]
The number \(U_n\) of worlds that are singleton information cells for **none** of the agents converges in distribution to \(\operatorname{Poisson}(e^{-c})\). Moreover,
\[
\boxed{\Pr(\mathbb S\text{ satisfies normal distribution globally})\longrightarrow\exp(-e^{-c})}.
\]
In particular, the sharp agent-number scale is \(r_n\asymp n\log n/W(n)\), with \(W\) the positive Lambert function, because \(s_n\sim W(n)/n\). The Poisson statement and limit apply to any integer sequence \(r_n\) satisfying the displayed hypothesis.

## Assumptions and scope
All worlds are labelled, \(W\neq\varnothing\), equivalence relations are chosen independently in the random model, and each of the \(B_n\) partitions is equally likely. Every quantification over valuations ranges over arbitrary subsets of \(W\). The structural criterion holds for every integer \(r\geq1\); the new exact multi-agent census is emphasized for \(r\geq3\), while the random threshold concerns growing \(r_n\). No assertion is made about non-\(\mathsf{S5}\) epistemic accessibility or about agents sampled from a nonuniform partition law. For the formal identities at \(n=0\), use \(B_0=1\), \(L_{0,r}=1\).

## Proof
**1. Distribution is a least-cell condition.** Fix \(w\) and write \(C_i=E_i[w]\). For any subset \(P\subseteq W\), the statement \(\mathbb SP\) at \(w\) says that \(C_i\subseteq P\) for at least one \(i\). This predicate is upward closed, sends \(W\) to true, and is closed under binary intersections precisely when the finite collection \(\{C_i\}\) has a least member under inclusion. Indeed, a least member \(C_j\) gives \(\mathbb SP\iff C_j\subseteq P\). Conversely, if there is no least member, the finite family is not downward-directed: some \(C_i,C_j\) have no \(C_k\subseteq C_i\cap C_j\). Valuate \(p\) as \(C_i\) and \(q\) as \(C_j\); then \(\mathbb Sp\) and \(\mathbb Sq\) hold, but \(\mathbb S(p\land q)\) fails. Since \(\mathbb S\) is monotone and preserves truth, intersection preservation is equivalent to normal distribution: one direction uses \(\mathbb S(p\to q)\) together with \(\mathbb Sp\), the other uses the tautology \(p\to(q\to p\land q)\). Thus the local least-member criterion is equivalent to the specified schema for all valuations.

The set \(R[w]=\bigcap_iC_i\) is contained in every \(C_i\), so such a least member exists exactly when \(C_j=R[w]\) for some \(j\). Equivalence-class constancy makes this equivalent to condition 3. In that case \(\mathbb SP\iff R[w]\subseteq P\) for every \(P\), yielding the claimed equality of modal operators; induction on formulas handles nesting.

**2. Exact counting.** Partition \([n]\) first into the \(t\) blocks of \(R\), in \(\operatorname{Stir}_2(n,t)\) ways. Each \(E_i\) coarsens \(R\), so it is uniquely a partition of these \(t\) distinguishable blocks. A block of \(R\) is itself an \(E_i\)-class precisely when its corresponding quotient point is a singleton block in the \(i\)-th quotient partition. Hence the structural condition is that every quotient point be singleton in at least one of the \(r\) quotient partitions. For a specified \(j\)-point subset, inclusion-exclusion on forbidden singleton points shows that \(A_{t,j}\) is the number of partitions in which none of those \(j\) points is singleton. Independent choices of the \(r\) quotient partitions give \((A_{t,j})^r\) tuples avoiding singleton points there. A second inclusion-exclusion over uncovered quotient points gives \(H_r(t)\). This coverage property itself forces the common refinement of the quotient partitions to be discrete, so the chosen partition is indeed exactly \(R\), with no overcounting. Summing over \(t\) establishes the finite formula. The exponential generating function follows by substituting the standard Stirling transform \(\sum_{n\geq t}\operatorname{Stir}_2(n,t)z^n/n!=(e^z-1)^t/t!\).

**3. Sharp random threshold.** Fix \(k\geq1\). A uniformly random partition leaves any specified \(k\) points all **non-singleton** with probability
\[
a_{n,k}=\sum_{j=0}^{k}(-1)^j\binom kj\frac{B_{n-j}}{B_n}.
\]
Classical consecutive Bell-ratio asymptotics yield \(s_n\sim W(n)/n\) and \(B_{n-2}/B_n=O(s_n^2)\); for each fixed \(k\), terms with \(j\geq2\) in this probability therefore total \(O_k(s_n^2)\). Consequently \(a_{n,k}=1-ks_n+O_k(s_n^2)\). Independence across agents gives the exact factorial-moment identity
\[
\mathbb E[(U_n)_k]=(n)_k(a_{n,k})^{r_n}.
\]
Under the hypothesis, \(r_ns_n^2=(\log n+c+o(1))s_n\to0\), so
\[
(n)_k(a_{n,k})^{r_n}\longrightarrow e^{-kc}.
\]
These are the factorial moments of \(\operatorname{Poisson}(e^{-c})\). The factorial-moment method yields the asserted Poisson convergence and \(\Pr(U_n=0)\to\exp(-e^{-c})\).

If \(U_n=0\), every world is singleton under some relation, so the common refinement \(R_n\) is discrete and the normality criterion holds. Conversely, on the event that \(R_n\) is discrete, the criterion is exactly \(U_n=0\). For each unordered pair of distinct worlds, the probability that it lies in the same class in all \(r_n\) independently sampled partitions is \(s_n^{r_n}\). Therefore
\[
0\leq\Pr(\mathbb S\text{ is normal})-\Pr(U_n=0)
\leq\Pr(R_n\text{ is not discrete})\leq\binom n2s_n^{r_n}\longrightarrow0.
\]
The final convergence follows since \(s_n\to0\) and \(r_ns_n\sim\log n\), making \(r_n|\log s_n|\) much larger than \(\log n\). This proves the growing-agent law.

## Verification
The standalone `checker.py` enumerates partitions directly and tests the local normality condition on every ordered tuple for \((n,r)=(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(2,3),(3,3),(4,3),(5,3),(3,4)\). The observed values agree with the Stirling/inclusion-exclusion census; the largest direct test counts \(31{,}468\) qualifying triples among \(140{,}608\) tuples at \(n=5\). Separately, for \((n,r)=(2,2),(3,2),(3,3)\), it checks every valuation of two propositional letters and finds exact agreement between the normality axiom and the least-cell criterion. The asymptotic argument is analytic; these finite checks do not certify the infinite limit.

Run the embedded file using `python checker.py` with Python 3 and no third-party dependencies. The checker computes the expected census from the displayed formulas rather than from hard-coded target values.

## Relationship to prior work
Ding and Yang (2026, arXiv:2603.26268v1, §5.1) develop axiomatizations of bundled modalities, including someone-knows for a fixed finite agent group over \(\mathsf{S5}\). Ågotnes and Wáng (2021) exhibit the general failure of normal modal axioms for someone-knows. Neither inspected work gives the above complete labelled census or a growing-number-of-agents probability transition. For two agents, the criterion reduces to the inclusion-comparability of the two information cells at every world; the census specializes to \(L_{n,2}=1,4,19,111,774\) for \(n=1,2,3,4,5\), respectively. The multi-agent and growing-agent claims are not consequences of that two-agent classification: for three or more agents, cells need not be pairwise comparable, and covering by singleton quotient cells has genuinely different combinatorics.

Pittel (2000) proves that the common refinement of a fixed number of independent uniform partitions is already discrete with high probability for each fixed agent count at least three. Discreteness alone is not sufficient for normality of someone-knows: the new law asks whether every singleton in that refinement is an entire cell of at least one agent, a substantially rarer covering event whose transition needs a growing agent population. Classical Bell-number asymptotics and the factorial-moment method supply standard inputs, not independent claims of novelty. The 2023 hypergraph/weakly aggregative-modal-logic paper of Ding, Liu and Wáng analyzes representation and axiomatization of someone-knows; only its available abstract and bibliographic descriptions, not its full text, were inspected. It therefore remains a literature-priority risk.

## Limitations
The threshold requires independent **uniform** partitions, permits a growing number of agents, and gives convergence but no explicit error-rate uniform in \(c\). It does not determine the distribution of normality for other random frame ensembles. No independent audit has been performed. A previously unknown general theory of random partition coverings, or uninspected full text addressing this exact property, could imply parts of the result; no assertion of priority or uniqueness is made beyond the concrete comparisons described above.

## References
1. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268v1 (first posted 2026-03-27), especially §5.1, https://arxiv.org/abs/2603.26268.
2. T. Ågotnes and Y. Wáng, *Somebody Knows*, Proceedings of KR (2021), DOI:10.24963/kr.2021/1, https://proceedings.kr.org/2021/1/kr2021-0001-agotnes-et-al.pdf.
3. Y. Ding, J. Liu and Y. Wáng, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic*, Synthese 201 (2023), DOI:10.1007/s11229-022-04032-y (abstract and bibliographic description consulted; full text not inspected).
4. L. Moser and M. Wyman, *An Asymptotic Formula for the Bell Numbers*, Trans. Roy. Soc. Canada (1955) (consecutive Bell-ratio asymptotics).
5. B. Pittel, *Where the Typical Set Partitions Meet and Join*, Electron. J. Combin. 7 (2000), R5 (random-partition intersection background).
