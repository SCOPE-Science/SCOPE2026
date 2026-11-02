# An exact four-residue feasibility law for realized-center delegated EF1

## Finding

Two distribution centers each have two agents, and a common set of \(m\ge1\) indivisible goods must be assigned completely to the four agents. The first three agents value each good at \(1\); the fourth, belonging to the second center, values every good at the same \(\rho\in(0,1)\). Centers evaluate their *own* bundles by their agents' realized total utility, but evaluate another center's goods by the maximal utility achievable by hypothetically reallocating those goods among their own agents (the item-based realized convention). Require EF1 between the two centers and inter-EF1 between every two individual agents.

Write \(m=4t+r\), where \(t\ge0\) is an integer and \(r\in\{0,1,2,3\}\). A simultaneous center-EF1 and individual inter-EF1 allocation **exists if and only if**

\[
\begin{array}{c|c}
r & \text{exact feasibility criterion}\\ \hline
0\text{ or }2 & t\rho\ge t-1\\
1 & t\rho\ge t-2\\
3 & (t+1)\rho\ge t-1.
\end{array}
\]

In particular, every instance in this family with at most seven goods is feasible. For \(m=8\) it is infeasible exactly when \(0<\rho<1/2\); hence eight goods are the sharp first failure *within this specified one-outlier family*. Nevertheless, nine goods are feasible for every \(0<\rho<1\). Feasibility is therefore not monotone in the number of goods: for example, at \(\rho=1/4\), eight goods are impossible, nine are possible, and ten are impossible again.

## Assumptions and scope

Let centers be \(A=\{A_1,A_2\}\) and \(B=\{B_1,B_2\}\). All goods are distinct physical objects, but identical in each individual's additive valuation:
\[
v_{A_1}(g)=v_{A_2}(g)=v_{B_1}(g)=1,\qquad v_{B_2}(g)=\rho,
\quad 0<\rho<1.
\]
A complete allocation gives counts \((a,b,c,d)\in\mathbb Z_{\ge0}^4\) with \(a+b+c+d=m\). For each ordered pair of individuals \(i,j\), inter-EF1 means that \(i\)'s own utility is at least the value of \(j\)'s bundle after removal of some good, when \(j\)'s bundle is nonempty. The condition is automatic when that bundle is empty.

For centers, realized own values are \(a+b\) for \(A\) and \(c+\rho d\) for \(B\). Under item-based evaluation of another center's goods, either center could assign each foreign good to a unit-valuing agent, obtaining the number of foreign goods. Center-EF1 applies to each directed center comparison after removal of one foreign good. No Pareto efficiency, strategic equilibrium, or EFX is imposed.

## Proof

**Step 1 (agent-level exact reduction).** Each individual's value for any single good is a strictly positive constant. Thus the inter-EF1 inequality from individual \(i\) to individual \(j\) simplifies, after division by that constant, to \(x_i\ge x_j-1\), where \(x_i\) and \(x_j\) are their bundle sizes. All ordered comparisons hold exactly when \(\max(a,b,c,d)-\min(a,b,c,d)\le1\). Consequently, there are exactly \(r\) entries equal to \(t+1\) and \(4-r\) entries equal to \(t\).

**Step 2 (center-level exact reduction).** Center \(A\)'s own value is \(a+b\), and its best item-based value for center \(B\)'s goods after deletion is \(\max(c+d-1,0)\). Center \(B\)'s realized value is \(c+\rho d\), and its best value for center \(A\)'s goods after deletion is \(\max(a+b-1,0)\). Since each own value is nonnegative, the two EF1 inequalities are equivalently
\[
a+b\ge c+d-1,\qquad c+\rho d\ge a+b-1.
\]
These equations also cover allocations with an empty center.

**Step 3 (one integer parameter).** Let \(u\) be the number of large bundles (size \(t+1\)) in center \(A\). Then its total count is \(2t+u\), while center \(B\) has \(2t+r-u\) goods. The first center inequality reads \(2u\ge r-1\). Because each center has two agents, the smallest feasible choice is \(u=0\) when \(r=0,1\), and \(u=1\) when \(r=2,3\).

**Step 4 (optimal placement within the second center).** Fix a feasible \(u\). To maximize the slack in the second inequality, place any available large bundle in the unit-valuing agent \(B_1\)'s position before placing one in \(B_2\)'s position. Reducing \(u\) when possible both decreases \(a+b-1\) by one and adds a positive amount to \(c+\rho d\), so a feasible allocation exists exactly when this smallest \(u\), best-in-center placement has nonnegative slack. The optimal count vectors, up to interchanging \(A_1,A_2\), are
\[
\begin{array}{c|c|c}
r & (a,b,c,d) & (c+\rho d)-(a+b-1)\\ \hline
0 &(t,t,t,t)&1-t(1-\rho)\\
1 &(t,t,t+1,t)&2-t(1-\rho)\\
2 &(t+1,t,t+1,t)&1-t(1-\rho)\\
3 &(t+1,t,t+1,t+1)&1-t+\rho(t+1).
\end{array}
\]
All four vectors satisfy the first center inequality, and each row's slack is nonnegative precisely under the respective criterion in the finding. This proves both necessity (every feasible vector is no better than the indicated vector) and sufficiency (the indicated vector is an allocation).

**Step 5 (sharp boundary and nonmonotonicity).** At \(m=1,\ldots,7\), the table's inequalities hold for every \(0<\rho<1\). At \(m=8\) the condition is \(2\rho\ge1\), while at \(m=9\) it is \(2\rho\ge0\). At \(m=10\), the condition returns to \(2\rho\ge1\). These exact comparisons yield all stated boundary assertions. \(\square\)

## Verification

The standalone standard-library program `verify.py` checks the theorem by direct pairwise EF1 inequalities. It enumerates every four-agent bundle-size composition for \(1\le m\le20\) and rational \(\rho=p/q\) with \(2\le q\le10\), \(1\le p<q\); for \(21\le m\le128\) it enumerates all inter-EF1-compatible bundle-size patterns and uses rational parameters with denominator at most \(16\). In total, \(13{,}860\) exact parameter cases match the formula. A separate labeled-allocation enumeration at \(\rho=1/4\) finds \(1{,}260\) feasible assignments with seven goods, none with eight goods, and \(7{,}560\) with nine goods. The nine-good count vector \((2,2,3,2)\) is directly checked as feasible.

Run `python3 verify.py` using the Python standard library. All mathematical universal quantifiers are discharged by Steps 1–5, not by the finite tests.

## Relationship to prior work

Deligkas, Fasoulakis, Ioannidis, Mancho and Markakis (2026), *Delegated Fair Division*, introduce the center valuation conventions and prove in Theorem 11 that simultaneous center-EF1 and inter-EF1 can fail in this four-agent one-exceptional-agent family using twelve goods and sufficiently small positive exceptional value. The present exact existence/nonexistence formula covers every number of goods and every \(\rho\in(0,1)\), establishes the eight-good first failure within that family, and exhibits recovery at nine goods. The earlier twelve-good negative example does not imply these cutoffs or the residue-specific sufficiency assertions.

Lucet, Benabbou, Beynier and Maudet (2025), *Multilevel Fair Allocation with Matroid-Rank Preferences*, study a different optimistic hierarchy-based fairness setting with matroid-rank leaf utilities; its EF1 guarantees do not establish the realized-versus-hypothetical center comparisons in the additive positive-outlier family here.

## Limitations

The eight-good minimality is **only within the specified homogeneous-good, one-exceptional-agent, two-center model**; it is not a lower bound for arbitrary bivalued delegated fair division. The analysis assumes strict positivity \(\rho>0\): at zero the agent-level balancing argument may fail. The result concerns exact existence of center-EF1 jointly with inter-EF1, not computational hardness, EFX, welfare efficiency, or arbitrary heterogeneous goods. Novelty comparison is limited to accessible literature and records; independent scientific validation has not been performed.

## References

1. A. Deligkas, M. Fasoulakis, S. D. Ioannidis, A. Mancho, and E. Markakis, *Delegated Fair Division*, arXiv:2607.27743v1, first public 30 July 2026. https://arxiv.org/abs/2607.27743
2. M. Lucet, N. Benabbou, A. Beynier, and N. Maudet, *Multilevel Fair Allocation*, arXiv:2512.24105, first public 30 December 2025. https://arxiv.org/abs/2512.24105
