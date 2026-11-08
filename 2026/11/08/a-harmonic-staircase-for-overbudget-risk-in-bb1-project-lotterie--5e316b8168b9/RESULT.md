# A harmonic staircase for overbudget risk in BB1 project lotteries

## Finding

Consider a participatory-budgeting lottery with \(k\ge 2\) labeled unit-cost projects, one exceptional project of cost \(c\), and budget \(B=k\). Let \(1<c<k\) and prescribe an inclusion marginal \(q\in(0,1]\) for the exceptional project and the same marginal \(p=1-cq/k\) for each unit-cost project. The expected budget expenditure is exactly \(k\).

A lottery *implements* these marginals when every project's inclusion probability equals its prescribed probability. Require every outcome in its support to be budget-balanced up to one project (BB1): an outcome below budget can reach budget by adding some omitted project, and an outcome above budget can be reduced to budget or below by removing some included project; either alternative applies to an outcome exactly at budget. Also impose a hard outcome-wise overspend cap \(\operatorname{cost}(W)\le k+\delta\), where \(\delta\ge0\). Let \(R_{k,c,q}(\delta)\) be the minimum possible probability of an outcome with cost strictly exceeding \(k\), with \(R=\mathrm{infeasible}\) when no lottery satisfies the requirements.

**Theorem.** If \(c\) is an integer, \(R_{k,c,q}(\delta)=0\) for every \(\delta\ge0\). Otherwise, write \(c=m+f\), with an integer \(1\le m<k\) and \(0<f<1\). Then the exact risk-cap frontier is

\[
R_{k,c,q}(\delta)=\begin{cases}
\mathrm{infeasible},&0\le\delta<f,\\
\dfrac{q(1-f)}{j+1},&f+j\le\delta<f+j+1,\quad j=0,\ldots,m-1,\\
\dfrac{q(1-f)}{m+1},&\delta\ge m+f.
\end{cases}
\]

Every feasible minimum is attained by an explicit lottery supported on at most \(2k+1\) labeled outcomes, all satisfying BB1. In fact, the same lower bound is valid for lotteries not required to satisfy BB1, so imposing BB1 has **zero additional overrun-risk cost** throughout this symmetric family. In particular, the risk exhibits exact downward jumps at the allowed overspend caps \(f+1,f+2,\ldots,f+m\), while no lottery at all can meet a cap smaller than \(f\).

For example, if \(k=5\), \(c=7/2\), and \(q=1/2\), each unit-cost project has marginal \(13/20\). The optimal overspending probability is \(1/4,1/8,1/12,1/16\) at caps \(\delta=1/2,3/2,5/2,7/2\), respectively.

## Assumptions and scope

The projects are indivisible and are selected at most once. The probability distribution may correlate project selections arbitrarily; independence is neither assumed nor imposed. The expensive project has cost strictly greater than one and strictly below the whole budget. Only its inclusion probability and the equal inclusion probabilities of the unit-cost projects are fixed. No voters, utility functions, or ex-post representation constraints are imposed. The result optimizes probability of a *strict* budget overrun, not expected excess cost, welfare, entropy, or the quality of a particular rounding algorithm. The cap is an outcome-wise maximum, not a bound in expectation. BB1 uses the existence-of-one-project convention of Aziz et al.; a stronger up-to-any-project requirement is not claimed.

## Proof

Let \(H\in\{0,1\}\) indicate whether the exceptional project is included. Let \(Z\in\{0,1,\ldots,k\}\) count omitted unit-cost projects. Prescribed marginals give

\[
\mathbb E H=q,\qquad \mathbb E Z=k-kp=cq,\qquad \operatorname{cost}(W)=k-Z+cH.
\]

If \(c\) is an integer, independently of whether \(H\) occurs, choose \(Z=0\) when \(H=0\), and \(Z=c\) when \(H=1\); conditionally on \(Z=c\), omit a uniformly rotated block of \(c\) unit-cost projects. All outcomes cost exactly \(k\), and all marginals are correct.

Suppose next that \(c=m+f\) is noninteger, and put \(t=\lceil c\rceil=m+1\). When \(H=1\), an outcome not exceeding budget has \(Z\ge t\). The overspend cap separately forces \(Z\ge\ell:=\max\{0,\lceil c-\delta\rceil\}\). If \(0\le\delta<f\), then \(\ell\ge t\); hence \(\mathbb E Z\ge tq>cq\), contradicting the prescribed marginals. This proves infeasibility.

For \(\delta\ge f\) we have \(0\le\ell<t\). Denote the overbudget probability by \(r=\Pr(H=1,Z<t)\). Since an outcome with \(H=0\) never exceeds budget, this is the total overbudget probability. On the events \(\{H=1,Z\ge t\}\) and \(\{H=1,Z<t\}\), the omitted count is at least \(t\) and \(\ell\), respectively. Thus

\[
cq=\mathbb E Z\ge t(q-r)+\ell r,
\qquad r\ge \frac{q(t-c)}{t-\ell}.
\]

This lower bound is attained. With probability \(1-q\), omit no unit-cost projects and omit the exceptional project. With probability \(r_*=q(t-c)/(t-\ell)\), select the exceptional project and omit exactly \(\ell\) unit-cost projects. With the remaining probability \(q-r_*\), select the exceptional project and omit exactly \(t\) unit-cost projects. Within each of the two latter types, select the omitted projects uniformly over the \(k\) cyclic shifts of a consecutive block of the specified length. Every unit-cost project is therefore omitted with probability

\[
\frac{r_*\ell+(q-r_*)t}{k}=\frac{cq}{k},
\]

so every prescribed marginal holds, and the total overbudget probability is exactly \(r_*\). The lower-cost state with \(H=1,Z=t\) is BB1 because adding an omitted unit-cost project reaches or exceeds budget, as \(t-1<c<t\). The overbudget state with \(H=1,Z=\ell\) is BB1 because deleting the exceptional project leaves at most \(k\) unit-cost projects. The state with \(H=0,Z=0\) costs exactly budget and is BB1. The cap holds because \(\ell\ge c-\delta\); every other outcome is at or below budget. There are at most \(1+2k\) support outcomes.

Finally, for \(f+j\le\delta<f+j+1\), \(0\le j<m\), the integer \(\ell\) equals \(m-j\), while for \(\delta\ge m+f\) it equals zero. Substitution into \(r_*\) yields every claimed staircase value. This proves the theorem.

## Verification

The accompanying `verification/verify_frontier.py` checks the exact rational three-type construction, the individual marginal probabilities, expected expenditure, cap, BB1 condition, and attained objective for 2,940 parameter instances with \(2\le k\le6\). When SciPy is installed, it also solves the complete probability-distribution linear program over every possible labeled outcome and independently compares the optimum or infeasibility for 420 instances with \(k\le5\). Both verification groups passed in the delivered execution. The mathematical proof, not the finite test set, covers all permitted integer \(k\), real \(c\), \(q\), and \(\delta\).

## Relationship to prior work

Aziz et al. prove that any feasible fractional participatory-budgeting outcome can be implemented by a lottery over BB1 integral outcomes (Theorem 3.2), and show that a stronger up-to-any-project rule can fail (Proposition 3.4). The theorem here addresses a distinct quantitative question: the **minimum chance of exceeding budget** subject to a specified hard overspend cap and fixed project marginals, for the natural one-expensive-project family. Their existence result is compatible with, but does not provide, the explicit staircase risk optimum. The dependent-rounding literature gives marginal-preserving constructions, not the quantified optimal risk frontier stated here. Work on optimal tail bounds for Bernoulli sums is adjacent, but results with unweighted sums and additional specified pairwise distributions have different hypotheses. The supplied claim is an exact elementary-moment-and-coupling result, not a general theorem about arbitrary project costs or fairness requirements.

## Limitations

The formula exploits both the common marginal of the unit-cost projects and the presence of only one exceptional project. For unequal small-project marginals, the simple cyclic construction may not meet the prescribed probabilities. The risk objective alone can favor rare large overruns, so practical selection requires specifying the cap as well as the risk. No assertion is made that this expression has publication priority over all unindexed, inaccessible, or differently formulated marginal-coupling results. A general-purpose coupling or rounding algorithm may solve the corresponding finite optimization implicitly, but its existence alone is not an explicit closed-form proof of this threshold classification.

## References

1. H. Aziz, X. Lu, M. Suzuki, J. Vollen, T. Walsh, *Fair Lotteries for Participatory Budgeting*, Proceedings of AAAI 38(9), 9469–9476 (publicly posted 2024-03-24), DOI: https://doi.org/10.1609/aaai.v38i9.28801 ; openly readable version: https://arxiv.org/abs/2404.05198 (first arXiv posting 2024-04-08). In particular Definition 3.1, Theorem 3.2, Proposition 3.4.
2. R. Gandhi, S. Khuller, S. Parthasarathy, A. Srinivasan, *Dependent Rounding and its Applications to Approximation Algorithms*, Journal of the ACM 53 (2006), 324–360, https://doi.org/10.1145/1147954.1147956.
3. D. Padmanabhan and K. Natarajan, *Tree Bounds for Sums of Bernoulli Random Variables: A Linear Optimization Approach*, INFORMS Journal on Optimization 3 (2021), 23–45, https://doi.org/10.1287/ijoo.2019.0038.
4. B. Wang and R. Wang, *Joint Mixability*, Mathematics of Operations Research 41 (2016), 808–826, https://doi.org/10.1287/moor.2015.0755.
