# Linear subsidy separation between singleton and unrestricted binary allocations

## Finding
For each integer \(r\ge3\), consider \(2r\) agents divided into two disjoint classes \(A\) and \(B\), each of size \(r\). There are \(2r\) distinct goods. Every agent in \(A\) values only one distinguished good \(g_0\) at one; every agent in \(B\) values every other good at one and \(g_0\) at zero. All valuations are additive and binary.

Let \(S_{\mathrm{free}}(r)\) be the minimum total nonnegative monetary subsidy for an envy-free complete allocation into arbitrary bundles, and let \(S_{\mathrm{single}}(r)\) be the corresponding optimum under the requirement that each agent receives exactly one good. Money has unit marginal utility for all agents. Then
\[
S_{\mathrm{free}}(r)=r,\qquad S_{\mathrm{single}}(r)=2r-1,\qquad S_{\mathrm{single}}(r)-S_{\mathrm{free}}(r)=r-1.
\]
Consequently, the house-allocation restriction creates an unbounded additive subsidy penalty and an asymptotic multiplicative penalty of two on a simple family with two valuation types.

## Assumptions and scope
A **complete allocation** consists of pairwise disjoint bundles \(X_i\) whose union is the set of all \(2r\) goods. Empty and multiple-good bundles are allowed in the unrestricted benchmark. In the singleton benchmark, \(|X_i|=1\) for all agents \(i\). Subsidies \(p_i\) are arbitrary nonnegative real numbers, not required to be integral. An outcome is envy-free exactly when
\[
v_i(X_i)+p_i\ge v_i(X_j)+p_j\quad\text{for all ordered agent pairs }(i,j).
\]
The two types of binary values are the only valuation assumptions. The theorem asserts exact minima for all integers \(r\ge3\), not just for the enumerated test sizes.

## Proof
**An unrestricted construction of cost \(r\).** Assign the distinguished good \(g_0\) to one agent \(a_0\in A\), and no goods to the other \(r-1\) agents in \(A\). Give \(r-1\) agents in \(B\) two of the remaining goods each, and the final agent in \(B\) one remaining good. Give subsidy one to each empty agent in \(A\) and to the agent in \(B\) receiving only one valued good; give zero subsidy to every other agent. Every \(A\)-agent has perceived utility one from their own outcome and at most one from anyone else's. Every \(B\)-agent has perceived utility two from their own outcome, at most two from another \(B\)-agent, and at most one from any \(A\)-agent. This proves \(S_{\mathrm{free}}(r)\le r\).

**Unrestricted lower bound, first case.** If \(g_0\) belongs to an agent in \(B\), each of the \(r\) agents in \(A\) has no valued good and envies the recipient of \(g_0\) by at least one absent subsidies. Thus each of their subsidies is at least one, giving total subsidy at least \(r\).

**Unrestricted lower bound, second case.** Suppose instead that \(g_0\) belongs to \(a_0\in A\). Write \(t=p_{a_0}\ge0\). Because all \(A\)-agents have identical preferences, envy-freeness in both directions forces every other \(A\)-agent's subsidy to equal \(1+t\). Therefore total subsidies to \(A\) equal \(r-1+rt\). Assume for contradiction that total subsidy is strictly smaller than \(r\). Then the sum of \(rt\) and all payments to \(B\) is strictly less than one. In particular each \(B\)-agent has subsidy strictly less than one.

Let \(b_j\) be the number of non-distinguished goods in the bundle of \(B\)-agent \(j\). As all agents in \(B\) have the same preferences, bidirectional envy-freeness gives \(b_j+p_j=H\), independent of \(j\). The \(b_j\) are integers and every \(p_j\) lies in \([0,1)\), so all \(b_j\) are the same integer \(k\). Since there are only \(2r-1\) non-distinguished goods, \(k\le1\). If \(k=0\), any \(B\)-agent would envy any \(A\)-agent other than \(a_0\), whose subsidy alone is at least one; impossible. Hence \(k=1\).

The agents in \(B\) together hold exactly \(r\) non-distinguished goods, leaving \(r-1\) such goods with agents in \(A\). A non-distinguished good cannot be given to an \(A\)-agent other than \(a_0\), because each \(B\)-agent's outcome has perceived utility \(1+p_j<2\), whereas a bundle containing such a good and subsidy \(1+t\) would be worth at least two to that \(B\)-agent. Thus all \(r-1\) remaining goods are held by \(a_0\). But then \(B\)-agents value the bundle of \(a_0\) at \(r-1+t\ge2\), again exceeding their own utility \(1+p_j<2\), a contradiction. So \(S_{\mathrm{free}}(r)\ge r\). This argument allows arbitrary real subsidies.

**Singleton lower bound.** Consider any envy-free outcome with one good per agent. If a \(B\)-agent held \(g_0\), some \(A\)-agent would hold a non-distinguished good. Exchanging their goods would increase both agents' values from zero to one. Adding their two pairwise envy inequalities produces the impossible inequality \(0\ge2\). Consequently \(g_0\) belongs to some \(a_0\in A\). The other \(r-1\) agents in \(A\) each receive a non-distinguished good. As above their subsidies all equal \(1+t\), where \(t=p_{a_0}\). Each agent in \(B\) receives exactly one non-distinguished good. Comparing its own bundle with that of a subsidized \(A\)-agent holding a non-distinguished good forces each \(B\)-agent's subsidy to be at least \(1+t\). Thus the total subsidy is at least
\[
t+(r-1)(1+t)+r(1+t)=2r-1+2rt\ge2r-1.
\]

**Singleton construction.** Give \(g_0\) to \(a_0\), one non-distinguished good to each other agent, subsidy zero to \(a_0\), and subsidy one to all other agents. Every agent in \(A\) then perceives utility one for their own outcome and at most one for any other's; every agent in \(B\) perceives utility two for their own outcome and at most two for another's. Hence \(S_{\mathrm{single}}(r)\le2r-1\). The claimed equalities follow.

## Verification
The accompanying standalone `verify.py` enumerates all complete allocations up to permutations of identically valued goods. It checks the exact minimum real subsidy for each allocation using longest-path difference constraints with integer edge weights. It independently enumerates the singleton subfamily, producing:

| \(r\) | unrestricted allocation profiles | singleton profiles | unrestricted minimum | singleton minimum |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 80 | 4 | 1 | 3 |
| 3 | 1,512 | 6 | 3 | 5 |
| 4 | 27,456 | 8 | 4 | 7 |

The theorem excludes \(r=2\), for which the unrestricted minimum is one rather than two. The proof, not the finite computation, establishes the entire infinite family for \(r\ge3\). Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Wu (arXiv:2610.10272v1) establishes a high-probability coincidence between unrestricted and singleton subsidy minima in the square case under independent continuously distributed values with density assumptions. The deterministic binary family here shows why such coincidence cannot be extended indiscriminately to binary inputs: its two optima differ by \(r-1\) for every \(r\ge3\). Dai, Li, Wu, and Zhang (arXiv:2608.22216) study minimum subsidies specifically for one-house-per-agent allocations, including binary preferences and two valuation types. The present result contrasts that constrained benchmark with the unrestricted benchmark on exactly the same valuations. General envy-freeability and difference-constraint characterizations are classical; this proof does not claim them as new.

## Limitations
This is a sharp comparison for one explicit, natural two-type binary valuation family. It does not bound the largest possible gap across all binary valuation matrices, does not show a probabilistic lower bound, and does not address valuations other than the specified two classes. Existing general subsidy algorithms and house-allocation results may imply individual ingredients, while the joint exact linear separation is the claim examined here.

## References
- Zekai Wu, *Asymptotic Subsidies for Envy-Free Allocation*, arXiv:2610.10272v1, first public 2026-10-07, https://arxiv.org/abs/2610.10272.
- Sijia Dai, Minming Li, Xiaowei Wu, Yong Zhang, *The Complexity of Minimizing Subsidies in Envy-Free House Allocation*, arXiv:2608.22216, first public 2026-08-23, https://arxiv.org/abs/2608.22216.
- Siddharth Barman, Anand Krishna, Yadati Narahari, Soumyarup Sadhukhan, *Achieving Envy-Freeness with Limited Subsidies under Dichotomous Valuations*, IJCAI 2022, https://www.ijcai.org/proceedings/2022/9.
- Daniel Halpern and Nisarg Shah, *Fair Division with Subsidy*, 2019, https://www.cs.toronto.edu/~nisarg/papers/subsidy.pdf.
