# Exact full-observation reliability and optimal fragile-PMU placement on complete multipartite graphs
## Finding
Let \(G=K_{r_1,\ldots,r_k}\) be a complete multipartite graph with \(k\ge 2\), with partite sets \(A_i\) of size \(r_i\). Let \(S\subseteq V(G)\) be a set of PMU locations, put \(s_i=|S\cap A_i|\), and let \(\ell=|S|=\sum_i s_i\). Each PMU independently survives with probability \(p=1-q\), where \(0<q<1\), and write \(x=p/q\).

The probability that the surviving PMUs power-dominate the whole graph is exactly
\[
R(G,S;q)=1-q^\ell\left(1+\sum_{i=1}^k H_{r_i}(s_i;x)\right),
\qquad
H_r(s;x)=\sum_{t=1}^{\min(s,r-2)}\binom{s}{t}x^t,
\]
where the sum defining \(H_r\) is empty when \(r\le2\).

For a fixed sensor budget \(\ell\), set
\[
\Delta_r(j;x)=H_r(j;x)-H_r(j-1;x)
=\sum_{t=1}^{\min(j,r-2)}\binom{j-1}{t-1}x^t,
\qquad 1\le j\le r.
\]
For every fixed \(q\in(0,1)\), each sequence \(\Delta_r(1;x),\ldots,\Delta_r(r;x)\) is nondecreasing. Consequently, an optimal \(\ell\)-PMU placement is obtained by the following exact greedy rule: starting from no PMUs, repeatedly add the next PMU to any part whose next available value \(\Delta_{r_i}(s_i+1;x)\) is minimum. Equivalently, choose \(\ell\) marginal values of minimum total weight, respecting the prefix order within every part. This minimizes \(\sum_i H_{r_i}(s_i;x)\) and hence maximizes \(R(G,S;q)\).

There is also a closed initial regime. Define
\[
B_0=\sum_{i:r_i\le2}r_i,
\qquad
B_1=3|\{i:r_i=3\}|+|\{i:r_i\ge4\}|.
\]
Then
\[
R_{\max}(\ell;q)=1-q^\ell\quad(1\le\ell\le B_0),
\]
and
\[
R_{\max}(\ell;q)=1-q^\ell\left(1+(\ell-B_0)\frac{1-q}{q}\right)
\quad(B_0<\ell\le B_0+B_1).
\]

## Assumptions and scope
Graphs are finite, simple, and connected; thus \(k\ge2\). At most one PMU is placed at each vertex. After failures, the surviving PMUs initiate the standard power-domination process: first their closed neighborhoods are observed, then an observed vertex with exactly one unobserved neighbor forces that neighbor to become observed. Failures are independent and identically distributed with probability \(q\in(0,1)\). The optimization statement fixes both \(q\) and the number \(\ell\) of installed PMUs.

## Proof
Let \(T\subseteq S\) be the set of surviving PMUs. First characterize exactly when \(T\) power-dominates \(G\).

If \(T\) meets two distinct partite sets, every vertex lies in the closed neighborhood of \(T\): a vertex sharing a part with one survivor is adjacent to the survivor in the other part, while every other vertex is adjacent to at least one survivor. Hence the domination step already observes all of \(G\).

Now suppose \(T\ne\varnothing\) is contained in a single part \(A_i\). Immediately after the domination step, every vertex outside \(A_i\) and every vertex of \(T\) is observed; the only unobserved vertices are the \(r_i-|T|\) vertices of \(A_i\setminus T\). Every observed vertex outside \(A_i\) is adjacent to all of these unobserved vertices, and every observed vertex inside \(A_i\) is adjacent to none of them. Therefore a force is possible exactly when \(r_i-|T|=1\), while \(r_i-|T|=0\) is already complete. Thus a nonempty one-part survivor set succeeds exactly when \(|T|\ge r_i-1\).

It follows that failure occurs in pairwise disjoint cases: \(T=\varnothing\), or for exactly one index \(i\), the survivor set is a nonempty subset of the installed PMUs in \(A_i\) of size \(t\le r_i-2\). The empty-survivor event has probability \(q^\ell\). For fixed \(i\) and \(t\), the total probability of all such survivor sets is
\[
\binom{s_i}{t}p^tq^{\ell-t}=q^\ell\binom{s_i}{t}x^t.
\]
Summing the disjoint failure events yields the stated reliability formula.

For optimization, the common factor \(q^\ell\) shows that maximizing reliability is equivalent to minimizing the separable penalty \(\sum_i H_{r_i}(s_i;x)\) subject to \(0\le s_i\le r_i\) and \(\sum_i s_i=\ell\). Pascal's identity gives
\[
H_r(j;x)-H_r(j-1;x)
=\sum_{t=1}^{\min(j,r-2)}\binom{j-1}{t-1}x^t
=\Delta_r(j;x).
\]
As \(j\) increases, every coefficient already present in this sum is nondecreasing, and any newly appearing term is nonnegative; hence \(\Delta_r(j;x)\) is nondecreasing. Thus each part contributes a nondecreasing chain of marginal penalties. Selecting the smallest currently available marginal is globally optimal: if a later marginal from a chain is selected, all earlier marginals in that chain are no larger, so a minimum-weight selection can always be made prefix-closed. Summing selected marginals recovers \(\sum_i H_{r_i}(s_i;x)\), proving the greedy rule.

Finally, all \(r\) marginal values vanish for \(r\le2\), giving \(B_0\) zero-cost locations. For \(r=3\), all three marginals equal \(x\); for \(r\ge4\), only the first marginal equals \(x\), because the second is \(x+x^2>x\). Hence exactly \(B_1\) locations form the next marginal tier, and the two closed formulas follow.

## Verification
A standalone exact-rational verifier constructs each complete multipartite graph directly, simulates the power-domination process without using the structural lemma, and compares direct survivor enumeration with the closed reliability formula at \(q\in\{1/5,1/2,4/5\}\). It also checks monotonicity of every marginal chain, compares the greedy optimizer against exhaustive occupancy-vector optimization for every sensor budget, and checks the two closed initial regimes. The test covers all 58 integer-partition types of complete multipartite graphs of orders \(2\) through \(8\). The archived verification output ends with `VERIFY_OK`.

## Relationship to prior work
The fragile power-domination framework was introduced in the preprint *Power domination with random sensor failure* (first posted in 2023). Its Section 4 studies full-observation probabilities, including the power-domination-polynomial interpretation and exact star probabilities; Section 5.3 gives a complete-multipartite expected-value expression. A later preprint, *On Fragile Power Domination*, develops expected-value-polynomial comparison methods. These probability tools, the survivor-set expansion, and the elementary success criterion are not claimed as new general principles here. The retained contribution is the explicit complete-multipartite separable occupancy penalty, its nondecreasing prefix-marginal characterization of optimal fixed-budget placements for arbitrary part sizes, and the two closed initial budget tiers. The generic greedy theorem for separable discrete-convex allocation is also standard; the graph-specific penalty and its exact budget regimes, not a newly invented optimization paradigm, are what is being recorded.

## Limitations
The theorem assumes identical independent failure probabilities. Heterogeneous or correlated failures need not produce the same separable penalty or greedy optimizer. The result is specific to complete multipartite graphs and to full observation under the standard power-domination forcing rule. The originality assessment is best-of-knowledge rather than an independent literature audit, and no independent mathematical validation has yet been performed.

## References
1. Beth Bjorkman, Zachary Brennan, Mary Flagg, and Johnathan Koch, *Power domination with random sensor failure*, arXiv:2312.12259v1, first posted 2023-12-19, https://arxiv.org/html/2312.12259v1.
2. Beth Bjorkman, Sean English, Johnathan Koch, and Amanda Verga, *On Fragile Power Domination*, arXiv:2507.14620v1, first posted 2025-07-19, https://arxiv.org/html/2507.14620v1.
