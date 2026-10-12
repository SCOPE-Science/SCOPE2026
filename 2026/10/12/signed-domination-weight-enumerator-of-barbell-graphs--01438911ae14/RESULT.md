# Signed-domination weight enumerator of barbell graphs
## Finding
For every integer \(n\ge 2\), let \(B_n\) be the barbell graph obtained from disjoint copies \(L\cong K_n\) and \(R\cong K_n\) by adding one edge \(ab\), where \(a\in L\) and \(b\in R\). A signed dominating function is a map \(f:V(B_n)\to\{-1,1\}\) such that \(\sum_{u\in N[v]}f(u)\ge1\) for every vertex \(v\). Write
\[
L_f=\sum_{v\in L}f(v),\qquad R_f=\sum_{v\in R}f(v),\qquad \alpha=f(a),\qquad \beta=f(b).
\]
Then \(f\) is signed dominating if and only if
\[
L_f\ge1,\qquad R_f\ge1,\qquad L_f+\beta\ge1,\qquad R_f+\alpha\ge1.
\]
Let \(W_n(t)=\sum_f t^{\sum_v f(v)}\), where the sum ranges over signed dominating functions on \(B_n\).

If \(n\) is even, put
\[
P_n(t)=\sum_{k=n/2+1}^{n}\binom{n}{k}t^{2k-n}.
\]
Then
\[
W_n(t)=P_n(t)^2.
\]
In particular, the bridge changes no signed dominating function relative to the disjoint union \(2K_n\), and
\[
\gamma_s(B_n)=4,
\qquad
[t^4]W_n(t)=\binom{n}{n/2+1}^2.
\]

If \(n=2q+1\) is odd, define
\[
A_q(t)=\sum_{j=q}^{2q}\binom{2q}{j}t^{2j-2q+1},\qquad
B_q(t)=\sum_{j=q+1}^{2q}\binom{2q}{j}t^{2j-2q+1},
\]
\[
C_q(t)=\sum_{j=q+1}^{2q}\binom{2q}{j}t^{2j-2q-1},\qquad
D_q(t)=\sum_{j=q+2}^{2q}\binom{2q}{j}t^{2j-2q-1}.
\]
Then
\[
W_n(t)=A_q(t)^2+2B_q(t)C_q(t)+D_q(t)^2.
\]
Consequently,
\[
\gamma_s(B_n)=2,
\qquad
[t^2]W_n(t)=\binom{n-1}{(n-1)/2}^2.
\]
For odd \(n\), the bridge removes exactly those signed dominating functions of \(2K_n\) for which one clique has sum \(1\) while the bridge endpoint in the opposite clique has label \(-1\).

## Assumptions and scope
The graph is the symmetric one-edge barbell \(B_n\) with two cliques of the same order \(n\ge2\). The signed-domination convention uses closed neighborhoods and labels in \(\{-1,1\}\). The polynomial records total function weight, not the number of positive labels. No assertion is made here for unequal clique orders or for longer paths joining the cliques.

## Proof
Every non-bridge vertex of \(L\) has closed neighborhood exactly \(L\), while the bridge vertex \(a\) has closed neighborhood \(L\cup\{b\}\). Hence all signed-domination inequalities on the left are equivalent to \(L_f\ge1\) and \(L_f+\beta\ge1\). The right side gives \(R_f\ge1\) and \(R_f+\alpha\ge1\). This proves the four-inequality criterion.

Suppose first that \(n\) is even. Every clique sum has even parity, so \(L_f\ge1\) and \(R_f\ge1\) are equivalent to \(L_f,R_f\ge2\). Since \(\alpha,\beta\ge-1\), the bridge inequalities are then automatic. A clique with exactly \(k\) positive labels has sum \(2k-n\), so its admissible weight enumerator is \(P_n(t)\). The choices on the two cliques are independent, giving \(W_n(t)=P_n(t)^2\). The least possible clique sum is \(2\), attained by \(k=n/2+1\) positive labels, proving the minimum-weight statement and multiplicity.

Now let \(n=2q+1\). Condition on the sign of a bridge endpoint and on the number \(j\) of positive labels among the other \(2q\) vertices of that clique. With endpoint label \(+1\), the clique sum is \(2j-2q+1\); with endpoint label \(-1\), it is \(2j-2q-1\). If the opposite endpoint is \(+1\), the four-inequality criterion only requires this clique sum to be at least \(1\); if the opposite endpoint is \(-1\), it must be at least \(3\). Thus the four endpoint-sign cases contribute respectively \(A_q(t)^2\), \(B_q(t)C_q(t)\), \(C_q(t)B_q(t)\), and \(D_q(t)^2\), proving the polynomial formula.

For odd \(n\), total weight \(2\) is attained exactly when each clique has sum \(1\) and both bridge endpoints have label \(+1\). On either clique, this fixes exactly \(q\) positive labels among the remaining \(2q\) vertices, giving \(\binom{2q}{q}=\binom{n-1}{(n-1)/2}\) choices independently on each side. This proves the minimum and its multiplicity. Finally, comparing the four-inequality criterion with the condition \(L_f,R_f\ge1\) for \(2K_n\) yields the stated exact description of the functions removed by the bridge when \(n\) is odd.

## Verification
A standalone exhaustive verifier independently enumerates every labeling for \(2\le n\le8\), tests the closed-neighborhood criterion, compares every weight coefficient with the formulas above, and checks the claimed minimum layers. Its replay output is:

`VERIFY_OK n_range=2..8 labelings=87376 valid_functions=12123 coefficient_checks=31 minimum_checks=7 max_order=16`

This finite enumeration is a consistency check only; the proof above establishes the formulas for every \(n\ge2\).

## Relationship to prior work
Signed domination was introduced in 1995 by Dunbar, Hedetniemi, Henning, and Slater. Zelinka's full-text 2006 paper studies the same invariant on bipartite graphs and gives exact scalar values for complete bipartite graphs; it does not contain the barbell all-function enumerator. A 2014 paper gives general bounds for signed domination but does not imply the coefficientwise formula above.

For the same barbell graph family, Jahari and Alikhani proved that the bridge is irrelevant for the ordinary domination polynomial, so the ordinary domination polynomial equals that of \(2K_n\). The signed result above has a sharper parity phenomenon: the bridge is invisible for even clique order but not for odd clique order. This contrast is not implied by the ordinary-domination identity because signed domination imposes closed-neighborhood majority inequalities rather than set domination.

## Limitations
The result is restricted to equal-clique one-edge barbells. The literature comparison inspected a foundational bibliographic record, a full-text same-invariant complete-bipartite paper, a full-text general-bounds paper, and a full-text same-object ordinary-domination paper; an unindexed earlier family-specific signed-domination result remains a residual possibility. The exact day \(1995\text{-}04\text{-}03\) used for the foundational public-source date is the publication date recorded for the containing proceedings volume rather than a separately dated chapter release.

## References
1. J. E. Dunbar, S. T. Hedetniemi, M. A. Henning, and P. J. Slater, “Signed domination in graphs,” in *Graph Theory, Combinatorics, and Algorithms*, 1995. MR1405819; ISBN 9780471304371.
2. B. Zelinka, “Signed and minus domination in bipartite graphs,” *Czechoslovak Mathematical Journal* 56 (2006), 587–590. DML-CZ:128088.
3. S. M. Hosseini Moghaddam, A. Khodkar, and B. Samadi, “New bounds on signed domination numbers of graphs,” arXiv:1409.2755.
4. S. Jahari and S. Alikhani, “On D-equivalence classes of some graphs,” arXiv:1511.00159.
