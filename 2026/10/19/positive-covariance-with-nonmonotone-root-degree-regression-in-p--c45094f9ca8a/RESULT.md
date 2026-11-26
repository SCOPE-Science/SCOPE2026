# Positive covariance with nonmonotone root-degree regression in preferential attachment trees

## Finding

In the degree-proportional attachment tree seeded by the edge \(1\!-
\!2\), let \(D_n\) be the degree of vertex 1 and \(L_n\) the number of vertices of degree 1. For every \(n\ge3\), the two lowest root degrees have the same probability,
\[
 \Pr(D_n=1)=\Pr(D_n=2)=p_n=4^{-(n-2)}\binom{2n-4}{n-2},
\]
but their conditional leaf means differ:
\[
 \mathbb E[L_n\mid D_n=1]=\frac{2n}{3},\qquad
 \mathbb E[L_n\mid D_n=2]=\frac{2n}{3}-1+\frac1{2n-5}.
\]
Thus the regression drops by \(1-(2n-5)^{-1}\) between degrees 1 and 2, strictly for \(n\ge4\), even though positive root-degree/global-leaf covariance in this model is known [1]. At maximum degree \(n-1\), the tree is a star and the conditional leaf count is \(n-1\), strictly above the degree-2 mean for \(n\ge4\). The regression is therefore neither nondecreasing nor nonincreasing. At \(n=3\), both conditional means are 2.

## Assumptions and scope

At size \(n\), one new vertex attaches by one undirected edge to an existing vertex \(v\) with probability \(\deg_n(v)/[2(n-1)]\). Degrees are measured before attachment. All leaves count, including either seed vertex when its degree is one. At \(n=2\) the degree-2 conditioning event has probability zero. No full joint law or analogous assertion under other seeds or attachment kernels is claimed.

## Proof

Write \(Q=2(n-1)\) for the sum of degrees at size \(n\). If an arrival attaches to a leaf, the total number of leaves stays unchanged; otherwise it grows by one. A root of degree 1 stays there unless selected, so \(p_{n+1}=(1-1/Q)p_n\), with \(p_2=1\). The product gives the central-binomial expression. If \(r_n=\Pr(D_n=2)\), then \(r_{n+1}=(1-2/Q)r_n+p_n/Q\). Since \(r_3=p_3=1/2\), this proves equality for all \(n\ge3\).

For \(n\ge3\), set \(u_n=\mathbb E[L_n\mathbf1_{\{D_n=1\}}]\), \(v_n=\mathbb E[L_n\mathbf1_{\{D_n=2\}}]\). For a tree with root degree 1 and \(L\) leaves, the expected contribution to \(u_{n+1}\) is \((1-1/Q)L+1-L/Q\): root selection exits the degree-1 class and selects a leaf, so the extra leaf comes only from nonleaf attachment. For a tree with root degree 2 and \(L\) leaves, the expected degree-2 contribution is \((1-2/Q)L+1-(2+L)/Q\), since selecting either the root or a leaf precludes an increase in leaves within this class. A degree-1 tree contributes \(L/Q\) to the next degree-2 class via root selection. Consequently,
\[
 u_{n+1}=(1-2/Q)u_n+p_n,\qquad
 v_{n+1}=(1-3/Q)v_n+(1-2/Q)p_n+u_n/Q.
\]
Let \(x_n=u_n/p_n\) and \(y_n=v_n/p_n\). Then \(x_3=y_3=2\), and
\[
 (Q-1)x_{n+1}=(Q-2)x_n+Q,\qquad
 (Q-1)y_{n+1}=(Q-3)y_n+Q-2+x_n.
\]
The first gives \(x_n=2n/3\) by induction. For \(\delta_n=x_n-y_n\), subtraction yields
\[
 1-\delta_{n+1}=\frac{Q-3}{Q-1}(1-\delta_n)
 =\frac{2n-5}{2n-3}(1-\delta_n).
\]
The factors telescope from \(1-\delta_3=1\) to give \(1-\delta_n=1/(2n-5)\). This proves both conditional formulas. The star event has positive probability by taking every attachment at the root. On it \(L_n=n-1>2n/3\) for \(n\ge4\), completing the regression comparison.

## Verification

Run `python3 verify.py` for exact weighted enumeration of all parent-selection histories through nine vertices. The enumerator checks the degree-1 and degree-2 root probabilities and conditional leaf means directly from that joint census. It also checks the star endpoint and includes consistency tests for the earlier covariance identity [1] and asymptotic moment estimates. These finite computations do not replace the proof for all sizes.

## Relationship to prior work and limitations

Reference [1], equations (3)–(6), already gives the exact positive covariance and its square-root asymptotic for the same variables, seed, and kernel. That result is used only as context for the conditional reversal. Global degree-count moments [2] and leaf-neighbor profiles [3] address different joint statistics; neither a marginal law nor the single mixed moment in [1] specifies the conditional means at degrees 1 and 2. The inspected material did not supply the two conditional formulas. Earlier related work on leaf counts in branches of plane-oriented recursive trees [4] remains a possible source of indirect overlap; its full text was not inspected. This comparison does not certify publication priority.

## References

1. [*Oldest-hub degree has positive square-root covariance with leaf abundance*, Resultary, 2026-10-13](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-oldest-hub-degree-has-positive-square-root-covariance-with-leaf--a3885e62cb19/RESULT.md), equations (3)–(6).
2. P. L. Krapivsky and S. Redner, *Finiteness and Fluctuations in Growing Networks*, arXiv:cond-mat/0207107; J. Phys. A 35 (2002), 9517–9534.
3. H. Hartle and P. L. Krapivsky, *Leaves of Preferential Attachment Trees*, arXiv:2602.01021.
4. H. M. Mahmoud, R. T. Smythe, and J. Szymański, *On the Structure of Random Plane-Oriented Recursive Trees and Their Branches*, Random Structures & Algorithms 4 (1993), 151–176, doi:10.1002/rsa.3240040204 (abstract only).
