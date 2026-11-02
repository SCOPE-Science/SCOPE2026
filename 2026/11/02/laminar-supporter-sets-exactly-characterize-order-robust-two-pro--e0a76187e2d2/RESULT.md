# Laminar supporter sets exactly characterize order-robust two-project MES-Style preallocation

## Finding

For two **preselected** projects charged sequentially by the MES-Style preallocation of Baychkov, Brill and Utke, universal invariance of the final voter budgets under swapping project order has an exact set-theoretic characterization. Write \(S,T\ne\varnothing\) for the projects' supporter sets. For every pair of positive project costs under which the projects are **both fully paid for under both possible orders**, the final budgets agree if and only if

\[
S\subseteq T\quad\text{or}\quad T\subseteq S\quad\text{or}\quad S\cap T=\varnothing.
\]

If the sets cross, one can choose strictly positive costs that are fully funded in both orders, but generate different final budgets. This is not merely numerical order sensitivity: an additional available project approved by just one voter can be MES-affordable after one order and unaffordable after the other. Three voters and three projects (two preselected, one remaining) suffice and are minimal for such an effect.

## Assumptions and scope

There are \(n\ge1\) voters, an MES rule budget \(B>0\), and two distinct preselected projects \(p,q\) with nonempty supporter sets \(S,T\subseteq [n]\) and positive costs \(u,v\). Initially, each voter has balance \(h=B/n\). To charge an amount \(c\) to a project supported by \(U\), find a level \(\lambda\ge0\) such that \(\sum_{i\in U}\min\{b_i,\lambda\}=c\) and subtract \(\min\{b_i,\lambda\}\) from every supporter; this operation is permitted here only if the supporters can meet the full cost. There are no other mandatory projects. Both orders \(p,q\) and \(q,p\) are required to finance **both** projects completely. A pair of supporter sets is *laminar* when one includes the other or they are disjoint; otherwise it is *crossing*. The final budget vector means the vector after the authors' maximum-minimum-endowment rebalancing, not only the intermediate vector after direct charges.

For the downstream selection assertion, append a single available project \(r\) and run ordinary approval-based MES on the resulting voter balances. A project is affordable to MES exactly if its supporters' residual balances sum to at least its cost. The claim concerns possible outcomes of this precisely specified algorithm, not every mixed voting rule or arbitrary preselected project families.

## Proof

**Rebalancing does nothing when the two mandatory projects are fully financed.** Every voter began with \(h\) and contributes the amount consumed from that initial budget. If the residual after charging is \(b_i\), the charge \(\pi_i\) therefore obeys \(\pi_i+b_i=h\). Since full financing gives \(\sum_i\pi_i=u+v\), the vector \(b\) sums to \(B-u-v\), the rebalancing budget. Under the rebalancing objective \(\max \min_i(\pi_i+\widetilde b_i)\), no feasible vector can have minimum total endowment above \(h\), because the total of all endowments is \(B=nh\). The original residual vector attains \(h\) for every voter, and is the **unique** maximizing budget vector: all \(n\) terms must equal \(h\). Therefore the comparison may be made using the direct residual balances.

**Laminar sufficiency.** Disjoint supporter sets affect independent coordinates, hence the charges commute. Suppose next that \(S\subseteq T\), and write \(s=|S|\), \(t=|T|\). In order \(q,p\), the first project charges \(v/t\) uniformly to every voter in \(T\), leaving all voters in \(S\) with \(h-v/t\). The second project is fully financed by assumption, so \(u/s\le h-v/t\). In order \(p,q\), the first project charges \(u/s\) to all members of \(S\). The same inequality implies every member of \(T\) can subsequently contribute \(v/t\); thus project \(q\) is uniformly financed in this order too. Each voter has the same total payment under the two orders. The proof for \(T\subseteq S\) is symmetric, and equality of sets is included.

**Crossing necessity and downstream effect.** Suppose \(a=|S\setminus T|\ge1\), \(b=|T\setminus S|\ge1\), and \(k=|S\cap T|\ge1\). Write \(s=a+k\), \(t=b+k\) and normalize \(h=1\), so \(B=n\). All three strict inequalities \(s/(s+k)>1/2\), \(t/(t+k)>1/2\), and \(n/(s+t)>1/2\) hold: the last follows from \(s+t=a+b+2k<2n\). Choose

\[
\frac12<\theta<\min\left\{\frac{s}{s+k},\frac{t}{t+k},\frac{n}{s+t}\right\},\qquad u=s\theta,\quad v=t\theta.
\]

In order \(p,q\), everyone in \(S\) initially pays \(\theta\). The \(k\) common supporters then each exhaust their remaining \(1-\theta\) on \(q\), while the \(b\) exclusive supporters of \(T\) each pay

\[
\lambda=\theta+\frac{k}{b}(2\theta-1)<1.
\]

The equality \(k(1-\theta)+b\lambda=t\theta=v\) proves full finance of \(q\). The strict bound on \(\lambda\) follows from \(\theta<t/(t+k)\); in particular, members of \(S\setminus T\) retain \(1-\theta\). Conversely, in order \(q,p\), the \(a\) exclusive supporters of \(S\) each pay \(\mu=\theta+(k/a)(2\theta-1)<1\) on \(p\) and retain \(1-\mu\). Both projects are fully financed, and the total \((s+t)\theta<n=B\) makes the mandatory set feasible. Since \(\theta>1/2\), \(\mu>\theta\); thus for any \(z\in S\setminus T\) the residual is strictly greater in the \(p,q\) order than in the \(q,p\) order.

Choose a third, nonpreselected project supported **only by \(z\)**, with cost \(w\) strictly between \(1-\mu\) and \(1-\theta\). It is affordable under the first order but not under the second. Because it is the only remaining project, ordinary MES must buy it in the first order and cannot buy it in the second. The strict inequalities avoid ties. Multiplying all budgets and costs by an arbitrary positive \(h\) removes the normalization.

**Smallest domain.** Crossing sets require a voter in each of the three nonempty regions \(S\setminus T\), \(S\cap T\), and \(T\setminus S\), hence at least three voters. With one mandatory project there is no ordering. With only the two mandatory projects and full finance in both orders, the selected project set cannot depend on order; a third project is therefore necessary for differing selected project sets.

For concreteness, with \(n=B=3\), \(S=\{1,2\}\), \(T=\{2,3\}\), and \(u=v=6/5\), the residual vectors are, respectively, \((2/5,0,1/5)\) and \((1/5,0,2/5)\). A third project supported solely by voter \(1\), costing \(3/10\), is purchased only in the first case.

## Verification

Execute `python3 verification/check.py` from the extracted package root. The exact-rational program checks all unordered pairs of distinct nonempty supporter sets on up to six voters, compares both orders across a thirteen-by-thirteen rational cost grid whenever both projects are fully funded, and constructs a full-funding witness for each crossing pair. It separately checks the explicit three-voter witness. The program printed:

```
VERIFY_OK support_pairs= 2547 fully_funded_cost_profiles= 383958 laminar_pairs= 1269 crossing_pairs= 1278 crossing_constructed_witnesses= 1278
WITNESS_OK (Fraction(2, 5), Fraction(0, 1), Fraction(1, 5)) (Fraction(1, 5), Fraction(0, 1), Fraction(2, 5)) third_project_cost=3/10
```

The finite checks are corroboration, not the universal proof; universality follows from the algebraic inequalities above.

## Relationship to prior work

Baychkov, Brill and Utke define MES-Style preallocation in §4.2 of *Mixed Voting Rules for Participatory Budgeting*. Their Example 2 explicitly demonstrates that choosing different orders for two preselected projects can change subsequent voter balances, using a four-voter example. Thus, **order dependence itself is already prior work**. The distinct claim proved here is a necessary-and-sufficient characterization of **all** two-project support structures that universally avoid dependence under the stated full-funding condition, together with a three-voter downstream-selection witness for every crossing structure. Their proportionality guarantees and impossibility constructions in §5 and Appendices A–B do not state this classification. The ordinary MES funding rule predates this work and is not claimed as a new mechanism.

## Limitations

The iff classification is restricted to exactly two preselected projects, equal initial budgets, and cost pairs that achieve full financing in **both** orders. It does not classify cases where the authors' procedure discards a funding shortfall, more than two preselected projects, or unequal endowments. The theorem proves existence of order-sensitive costs for crossing sets, **not** that every possible cost pair is order sensitive. Nor does it prove a difference in all possible downstream completion schemes. Although direct literature and research-record comparisons found no matching result, differently formulated earlier commutativity theorems for water-filling operators remain a publication-priority risk.

## References

1. A. Baychkov, M. Brill and M. Utke, *Mixed Voting Rules for Participatory Budgeting*, full author-hosted manuscript, §4.2 (MES-Style and Example 2), §5, Appendices A–B, https://markus-utke.github.io/files/mixed_PB.pdf ; arXiv:2606.23320, first arXiv submission 22 June 2026, https://arxiv.org/abs/2606.23320 . The work was publicly presented under this title at the 10 July 2025 EC workshop, https://ec25.comsocseminar.org/ .
2. D. Peters, G. Pierczyński and P. Skowron, foundational analysis of the Method of Equal Shares, https://arxiv.org/abs/2008.13276 .
