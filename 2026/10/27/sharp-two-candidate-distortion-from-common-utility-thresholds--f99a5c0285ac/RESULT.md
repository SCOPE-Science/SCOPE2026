# Sharp two-candidate distortion from common utility thresholds

## Finding

In deterministic single-winner utilitarian voting between **exactly two candidates**, common cardinal-utility thresholds induce a symmetric mesh on the one-dimensional unit-sum utility simplex. For every integer \(t\geq1\) and every choice of distinct common thresholds \(1>\tau_1>\cdots>\tau_t>0\), let
\[
0=c_0<c_1<\cdots<c_s=1
\]
be the sorted distinct elements of \(\{0,1,\tau_1,\ldots,\tau_t,1-\tau_1,\ldots,1-\tau_t\}\), and let \(w=\max_{0\leq j<s}(c_{j+1}-c_j)\). Across every positive finite electorate size, the **optimal worst-case distortion of a deterministic rule given these thresholds** is exactly
\[
\boxed{D(\boldsymbol\tau)=\frac{1+w}{1-w}.}
\]
The lower bound is already forced by **two voters**. Optimizing jointly over the \(t\) thresholds and deterministic aggregation yields the exact finite-threshold frontier
\[
\boxed{\min_{\boldsymbol\tau}D(\boldsymbol\tau)=1+\frac1t.}
\]
All optimal threshold sets are characterized: there must be exactly one threshold at each of the \(t\) reflection-pair choices \(\{j/(2t+1),1-j/(2t+1)\}\), for \(j=1,\ldots,t\). Hence there are exactly \(2^t\) optimal unordered threshold sets (equivalently, ordered decreasing vectors). For example, one threshold at \(1/3\) gives distortion \(2\); two thresholds at \(1/5,2/5\) give \(3/2\).

## Assumptions and scope

There are exactly two labeled alternatives \(A\) and \(B\) and \(n\geq1\) voters. Each voter \(i\) has nonnegative **unit-sum** utilities \(u_i(A)=x_i\in[0,1]\) and \(u_i(B)=1-x_i\). Each voter reports, for both candidates, the interval determined by the same \(t\) public thresholds which contains the candidate's utility; boundary conventions may fix a side consistently. A deterministic rule observes all such reports (and knows the thresholds and \(n\)), then returns exactly one candidate. Social welfare sums actual utilities; distortion is the supremum over all positive finite \(n\) and compatible valuation profiles of optimal welfare divided by the winner's welfare (infinite if the latter is zero and the former positive). No ordinal ranking, randomization, incentives, or additional utility query is supplied. The infimum over deterministic aggregation rules is taken with the thresholds fixed; subsequently the thresholds themselves may be designed.

## Proof

**1. The report-induced mesh.** Let \(x=u_i(A)\). Its reported bin changes exactly when \(x\) crosses some \(\tau_j\), while the reported bin of \(B\), with utility \(1-x\), changes exactly when \(x\) crosses \(1-\tau_j\). Thus the feasible values of \(x\) given both reports lie in one of the intervals between successive cuts \(c_j\), with endpoint inclusion fixed by the reporting convention. Conversely, every open such interval gives one report, and its endpoints can be approached by valuations with that report. The set of cuts is invariant under reflection \(x\mapsto1-x\), so every cell \([a,b]\) has a reflected cell \([1-b,1-a]\). All cell widths are at most \(w\); because \(t\ge1\) and the thresholds are strictly interior, \(0<w<1\).

**2. Attainable upper bound.** For the reports of voter \(i\), denote the closure of the compatible utility interval of \(A\) by \([\ell_i,h_i]\), and define the average endpoint values
\[
L=\frac1n\sum_{i=1}^n\ell_i,\qquad U=\frac1n\sum_{i=1}^n h_i.
\]
The unknown actual mean utility \(X=n^{-1}\sum_i x_i\) belongs to \([L,U]\), and \(0\leq U-L\leq w\). Select \(A\) when \(L+U\geq1\), and \(B\) otherwise. In the first case, \(2L=(L+U)-(U-L)\geq1-w\); the chosen candidate has welfare at least \(n(1-w)/2\), and its worst ratio is at most \(\max\{1,(1-L)/L\}\leq(1+w)/(1-w)\). In the second case, \(2U=(L+U)+(U-L)<1+w\); candidate \(B\) has welfare at least \(n(1-w)/2\), with worst ratio \(\max\{1,U/(1-U)\}\leq(1+w)/(1-w)\). The assertions also cover utility ties and all boundary conventions by closure.

**3. Matching two-voter lower bound.** Choose any cell \([a,b]\) of maximum width \(b-a=w\). Give the first voter a report for its interior and the second voter a report for the interior of its reflected cell \([1-b,1-a]\). These reports are fixed while the two feasible utility profiles for \(A\) approach respectively
\[
(x_1,x_2)=(a,1-b)\quad\text{and}\quad(x_1,x_2)=(b,1-a).
\]
The mean utilities for \(A\) approach \((1-w)/2\) and \((1+w)/2\), respectively; the mean for \(B\) is always one minus the mean for \(A\). A deterministic rule must make the same choice on both indistinguishable report profiles. If it chooses \(A\), the first utility profile gives limiting distortion \((1+w)/(1-w)\); if it chooses \(B\), the second gives that distortion. Approaching endpoints from within the open cells makes the argument valid without assuming a particular tie convention. This proves the exact fixed-threshold value for every \(t\) and \(n\) unrestricted.

**4. Optimizing the thresholds and classifying equality.** The \(t\) thresholds and their \(t\) reflected values create at most \(2t\) distinct interior cuts, hence at most \(2t+1\) cells. These cells partition an interval of length one, so \(w\geq1/(2t+1)\). Equality occurs only when there are precisely \(2t+1\) cells, all of equal length \(1/(2t+1)\), forcing the interior cuts to be precisely \(j/(2t+1)\) for \(j=1,\ldots,2t\). The cuts appear in \(t\) disjoint reflection pairs. Exactly one member of each pair must be a threshold, and conversely any such choice produces the required uniform mesh. Consequently there are \(2^t\) such threshold vectors. Since \(w\mapsto(1+w)/(1-w)\) is strictly increasing for \(0\leq w<1\), substitution of \(w=1/(2t+1)\) gives the claimed minimum \(1+1/t\). \(\square\)

## Verification

The accompanying standard-library-only program `verify_two_candidate_thresholds.py` performs exact-rational exhaustive checks of the pointwise minimax ratio and the proposed midpoint aggregation for all profile cells of sizes one through three under each of \(\binom9t\) tenth-grid threshold sets, for \(t=1,2,3\). It also verifies the reflected-cell two-voter witness and all \(2^t\) optimal reflection-pair selections for \(t=1,\ldots,8\). The executed program reports **639 threshold vectors and 57,568 exact-rational assertions passed**. These bounded calculations corroborate the proof but do not replace the argument valid for arbitrary real thresholds and any electorate size.

## Relationship to prior work

Latifian, Nilipour, and Voudouris (2026, arXiv:2610.13725) introduce the same shared-threshold, unit-sum, single-winner-as-a-special-case model, derive a general deterministic distortion upper bound \(2(2m)^{1/t}\), and obtain asymptotic lower bounds in the number \(m\) of candidates. Their stated theorems do not identify this exact two-candidate fixed-threshold mesh formula, its optimized finite-\(t\) value, or the complete optimal-threshold classification. The present result is limited to two alternatives and exploits the unit-sum reflection identity absent in higher dimensions.

Latifian and Voudouris (2024, arXiv:2401.09858) analyze matching under related threshold information; the feasible outcomes and unit-capacity matching constraints differ from selecting one common winner. Mandal, Procaccia, Shah, and Woodruff (2019) investigate distortion versus general communication budgets and threshold elicitation, but their inspected communication-level theorems do not give the fixed-threshold two-candidate exact value. Ebadian, Latifian, and Shah examine single-threshold approval voting with a second-stage runoff, which is an additional information and decision model. These distinctions concern statements and implications rather than title similarity. The symmetric mesh and endpoint-indistinguishability principles are elementary; the contribution is their exact sharp combination for this concrete threshold-design problem.

## Limitations

Only two candidates, deterministic winner selection, common nonadaptive thresholds, additive utilitarian welfare, and unit-sum utilities are covered. The result does not assert incentive compatibility; truthful reports are taken as input. Different results may hold with arbitrary positive scale utilities, correlated or agent-specific threshold choices, additional ranks, adaptive queries, more alternatives, or randomized aggregation. The result does not assert absolute historical priority; earlier unlocated equivalent formulations remain possible. Independent external verification has not been performed.

## References

1. M. Latifian, M. Nilipour, and A. A. Voudouris, *The Distortion of Threshold Approval Multiwinner Voting* (2026), arXiv:2610.13725, https://arxiv.org/abs/2610.13725 (first publicly posted 2026-10-09).
2. M. Latifian and A. A. Voudouris, *The Distortion of Threshold Approval Matching* (2024), arXiv:2401.09858, https://arxiv.org/abs/2401.09858.
3. D. Mandal, A. D. Procaccia, N. Shah, and D. P. Woodruff, *Efficient and Thrifty Voting by Any Means Necessary* (NeurIPS 2019), https://www.cs.toronto.edu/~nisarg/papers/thrifty.pdf.
4. S. Ebadian, M. Latifian, and N. Shah, *The Distortion of Approval Voting with Runoff*, https://www.cs.toronto.edu/~nisarg/papers/distortion-approval-runoff.pdf.
