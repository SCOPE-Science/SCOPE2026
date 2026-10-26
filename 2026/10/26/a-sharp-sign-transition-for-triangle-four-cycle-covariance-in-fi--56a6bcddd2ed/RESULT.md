# A sharp sign transition for triangle–four-cycle covariance in fixed-edge random graphs

## Finding

Let \(G\) be uniformly chosen among simple graphs on \(n\ge4\) labeled vertices with exactly \(m\) edges, where \(0\le m\le M=\binom n2\). Count each triangle as one edge set and each unoriented 4-cycle as one edge set (there are three 4-cycles on each four-element vertex set). Write \(T\) and \(Q\) for these respective numbers, and \((m)_4=m(m-1)(m-2)(m-3)\). Then

\[
\operatorname{Cov}(T,Q)=
\frac{4(m)_4(M-m)(M-m-1)[m(n^2-2n-7)-4(n^2-n-4)]}
{(n+1)^2(n+2)(n+3)(M-5)(M-4)(M-2)^2}.
\]

The denominator is positive throughout the stated domain. Covariance vanishes when \(m\le3\) or \(m\ge M-1\). On the interior \(4\le m\le M-2\), its sign agrees with the affine expression \(L_n(m)=m(n^2-2n-7)-4(n^2-n-4)\), whose unique real zero is \(\tau_n=4(n^2-n-4)/(n^2-2n-7)\). The complete integral sign classification is:

* \(n=4\): negative only at \(m=4\), and zero otherwise.
* \(n=5\): negative at \(m=4,5,6,7\), zero at \(m=8\), and zero outside the interior.
* \(n=6\): negative for \(4\le m\le6\), positive for \(7\le m\le M-2\).
* \(n=7,8\): negative for \(m=4,5\), positive for \(6\le m\le M-2\).
* \(n\ge9\): negative at \(m=4\), positive for \(5\le m\le M-2\).

All remaining cases have zero covariance. In particular, for every \(n\ge9\), the sign reverses sharply between four and five edges.

## Assumptions and scope

The graph law is the uniform \(G(n,m)\) model, not independent-edge \(G(n,p)\). The four-cycle variable counts all subgraph occurrences, not only induced cycles, and identifies reversal/rotation of the same cycle. The covariance refers to whole-graph counts; no assertions are made about conditional associations of individual indicators, general motif pairs, or stronger negative-dependence orders. Every integer \(n\ge4\) and all allowable integers \(m\) are included.

## Proof

For any fixed set of \(j\le M\) possible edges, let \(h_j=\Pr(E\subseteq G)=(m)_j/(M)_j\), with value zero when \(j>m\). The joint probability for prescribed triangle and cycle edge sets depends only on their overlap size: if the intersection has \(s\) edges, their union has \(7-s\) edges and the joint probability is \(h_{7-s}\). The probability product is always \(h_3h_4\).

Fix an unoriented four-cycle. Of the \(\binom n3\) candidate triangles, exactly four use two of its edges: one for each omitted vertex among the four cycle vertices. Exactly \(4(n-4)\) triangles use one cycle edge: select that edge in four ways and the remaining triangle vertex outside the cycle. All other triangles use no cycle edge. The total number of unoriented four-cycles is \(3\binom n4\). Consequently the exact covariance, with no asymptotic approximation, equals

\[
3\binom n4\left\{\binom n3(h_7-h_3h_4)
+4(n-4)(h_6-h_7)+4(h_5-h_7)\right\}.
\]

For \(n=4\), the formal \(h_7\) terms cancel identically because no triangle is edge-disjoint from a four-cycle; the displayed expression is interpreted after this cancellation, avoiding a fictitious seven-edge event when \(M=6\). Inserting \(M=n(n-1)/2\) and the falling-factorial expressions, collecting over a common denominator and cancelling common factors yields exactly the rational expression stated above. This algebraic identity is checked independently and symbolically in the accompanying `verify.py`; the preceding overlap count and elementary rational simplification constitute a proof for arbitrary parameters.

The denominator is strictly positive for every \(n\ge4\), since then \(M\ge6\). For \(4\le m\le M-2\), all factors outside \(L_n(m)\) are strictly positive. Its slope is \(n^2-2n-7>0\) for \(n\ge4\), so sign classification reduces to comparing admissible integers with \(\tau_n\). Directly, \(\tau_4=32\), \(\tau_5=8\), \(\tau_6=104/17\), \(\tau_7=38/7\), and \(\tau_8=208/41\). At \(n=4\), the interior is only \(m=4\), and \(L_4(4)<0\). For \(n\ge9\), \(4<\tau_n<5\), because \(L_n(4)=-4(n+3)<0\) and \(L_n(5)=n^2-6n-19>0\) for \(n\ge9\). These comparisons establish every sign and exact zero claimed.

## Verification

Run `python verify.py` with Python 3.9+ and SymPy available. The verifier enumerates all graphs for \(n=4,5,6\) (\(33{,}856\) graphs total), constructs independent triangle and unoriented four-cycle masks, computes exact joint distributions for every \(m\), and checks the derived moments and covariance in rational arithmetic. It also simplifies the unrestricted overlap-versus-factorized identity symbolically and tests the sign law for \(4\le n\le50\). It reports 138 exact moment/identity checks, and all sign checks pass. These finite checks are supplementary; the general theorem rests on the overlap counting and symbolic rational identity.

## Relationship to prior work

Kim and Vu (2004) study triangle-count tails, rather than exact mixed triangle/cycle covariance. Drmota, Ramos and Rué (2015) analyze subgraph statistics in subcritical graph classes, not unrestricted uniform fixed-edge graphs. Stark and Wormald (2016) analyze nonexistence of a prescribed subgraph in \(G(n,m)\), while Sah and Sawhney (2020) prove individual subgraph-count local limits principally in the dense regime. None of the inspected material states the present all-parameter signed triangle/four-cycle covariance law. Elementary overlap enumeration of subgraph moments is classical, and a broader, as-yet-unidentified mixed-moment source could conceivably imply the formula; no universal novelty claim is made on the basis of searches alone.

## Limitations

No multivariate local limit or stochastic monotonicity follows from a covariance sign. Finite enumeration is not the infinite proof. The formulas count non-induced subgraphs, and the result need not carry over to \(G(n,p)\): under independently retained edges, overlapping triangle/cycle indicators have nonnegative covariance while disjoint edge sets are independent. Historical priority beyond the inspected sources remains open to further human assessment.

## References

1. J. H. Kim and V. H. Vu, “Divide and conquer martingales and the number of triangles in a random graph,” *Random Structures & Algorithms*, first published 2004-01-14, DOI: 10.1002/rsa.10113.
2. M. Drmota, L. Ramos and J. Rué, “Subgraph statistics in subcritical graph classes,” arXiv:1512.08889v1 (2015-12-30).
3. D. Stark and N. Wormald, “The probability of nonexistence of a subgraph in a moderately sparse random graph,” arXiv:1608.05193v1 (2016-08-18).
4. A. Sah and M. Sawhney, “Local limit theorems for subgraph counts,” arXiv:2006.11369v1 (2020-06-19).
