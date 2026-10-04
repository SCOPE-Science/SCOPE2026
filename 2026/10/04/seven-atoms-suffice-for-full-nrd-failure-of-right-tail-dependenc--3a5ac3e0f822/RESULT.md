# Seven atoms suffice for full-NRD failure of right-tail dependence
## Finding
Let \(X=(X_1,X_2,X_3)\) take values in \(\{0,1\}\times\{0,1\}\times\{0,1,2\}\). Give the following cells integer masses and give every omitted cell mass zero:

| \((X_1,X_2)\) | \(X_3=0\) | \(X_3=1\) | \(X_3=2\) |
|---|---:|---:|---:|
| \((0,0)\) | 0 | 0 | 14 |
| \((0,1)\) | 18 | 3 | 0 |
| \((1,0)\) | 17 | 5 | 0 |
| \((1,1)\) | 27 | 2 | 0 |

After normalization by the total mass \(86\), this seven-atom law is fully negative regression dependent (full NRD) but is not negatively right-tail dependent (NRTD). Consequently, within the sharp minimal \(2\times2\times3\) rectangular state space identified by Su and Hu, the support-cardinality upper bound for a full-NRD/non-NRTD witness is at most \(7\), rather than the \(12\) positive atoms used by their strictly positive example. No lower bound excluding supports of size at most \(6\) is claimed.

## Assumptions and scope
For disjoint nonempty coordinate blocks \(I,J\), full NRD means that the conditional law of \(X_I\) given \(X_J=y\) is stochastically decreasing in the coordinatewise order on \(y\), whenever the compared conditioning events have positive probability. On a finite product poset it is enough to test every increasing upper set \(U\) of the output block.

The source paper states its finite criterion for strictly positive masses. The same criterion applies verbatim to nonnegative masses after omitting zero-probability conditioning values: for comparable \(y\le y'\) with positive marginal masses \(d_y,d_{y'}\), the required inequality is
\[
n_y(U)d_{y'}-n_{y'}(U)d_y\ge0,
\]
where \(n_y(U)\) is the unnormalized mass of \(X_I\in U\) jointly with \(X_J=y\). This is exactly the cross-multiplied conditional-probability comparison, and finite upper sets characterize stochastic order.

## Proof
The accompanying exact verifier enumerates every ordered choice of disjoint nonempty coordinate blocks \(I,J\), every nontrivial increasing upper set of the output block, and every pair of distinct comparable conditioning values. There are \(74\) formal upper-set comparisons. Ten involve a zero-mass conditioning value and therefore are outside the conditional definition. All \(64\) applicable comparisons have nonnegative integer cross-product slack; \(57\) are strict, \(7\) are equalities, and the smallest positive slack is \(6\). This proves full NRD without floating-point arithmetic or sampling.

NRTD fails already for the output coordinate \(X_1\) and the conditioning block \((X_2,X_3)\). Using the nested right-tail conditioning events \(\{X_3\ge1\}\) and \(\{X_2=1,X_3\ge1\}\),
\[
\Pr(X_1=1\mid X_3\ge1)=\frac724=\frac724,
\]
while
\[
\Pr(X_1=1\mid X_2=1,X_3\ge1)=\frac25=\frac25.
\]
The right-tail success probability increases under the stronger coordinatewise conditioning, because \(7/24<2/5\). The integer cross-product difference is \(7\cdot5-2\cdot24=-13\), so the violation is exact.

## Verification
Run `python3 verify_sparse_nrd.py`. The script reconstructs the seven-cell mass table from integers, generates all finite upper sets directly from the product order, checks all applicable full-NRD cross-products, and checks the displayed NRTD reversal. Its terminal assertion is `VERIFY_OK`.

The proof does not use an empirical search to infer impossibility at smaller support sizes. The verifier establishes only the displayed law and its properties.

## Relationship to prior work
Su and Hu, arXiv:2609.23313v1, prove that full NRD does not imply NRTD by a strictly positive law on a \(2\times2\times3\) rectangle and prove that no smaller rectangular state-space product can witness the implication failure. Their full-text discussion distinguishes that rectangular minimality from support sparsity and explicitly makes no assertion about the sparsest counterexample inside a \(2\times2\times3\) grid. The present law addresses that separate support-cardinality question by exhibiting a witness with only \(7\) positive cells.

This does not follow by simply deleting cells from the published strictly positive example: zeroing masses can destroy conditional stochastic-order inequalities, so full NRD must be re-established for the sparse law. The exact \(64\)-inequality verification supplies that missing step.

The earlier tournament paper of Su, Zou and Hu studies NRD, NLTD and NRTD in structured tournament models, rather than sparse generic finite-state witnesses. Dubhashi and Ranjan is foundational background for negative regression dependence, but the inspected material does not provide an implication-equivalent seven-atom construction.

## Limitations
The theorem is an upper bound on support size, not an exact sparsity classification. It does not prove that \(7\) is minimal, does not rule out a witness with at most \(6\) positive atoms, and does not alter Su and Hu's sharp result for minimal rectangular state-space cardinality. The law has zero cells, so statements in the source that assume strict positivity are not imported automatically; the proof instead uses the conditional definition only where conditioning probabilities are positive.

## References
Y. Su and T. Hu, *Full negative regression dependence: counterexamples for tail dependence and negative association*, arXiv:2609.23313v1, 2026.

Y. Su, Z. Zou and T. Hu, *Negative dependence in knockout tournaments*, Journal of Applied Probability, published online 2025, DOI: 10.1017/jpr.2025.10043.

D. Dubhashi and D. Ranjan, *Balls and bins: A study in negative dependence*, Random Structures & Algorithms 13 (1998), 99–124, DOI: 10.1002/(SICI)1098-2418(199809)13:2<99::AID-RSA1>3.0.CO;2-M.
