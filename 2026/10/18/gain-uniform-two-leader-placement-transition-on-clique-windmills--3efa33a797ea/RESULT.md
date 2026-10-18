# Gain-uniform two-leader placement transition on clique windmills

## Finding

Let \(r,m\geq2\) be integers and \(\kappa>0\). On the clique windmill \(W_{r,m}=K_1\vee(rK_m)\), choose exactly two distinct vertices as equally weighted noisy leaders. The graph has a hub adjacent to all \(rm\) peripheral vertices, partitioned into \(r\) disjoint cliques of size \(m\). Its combinatorial Laplacian is \(L\). For a leader pair \(S\), minimize
\[
J(S)=\operatorname{tr}\bigl(L+\kappa\operatorname{diag}(\mathbf1_S)\bigr)^{-1}.
\]
For **two cliques** (\(r=2\)), the unique optimal orbit consists of pairs in *different peripheral cliques*, with neither leader at the hub. For **three or more cliques** (\(r\geq3\)), the unique optimal orbit consists of the hub and *any one peripheral vertex*. All these inequalities are strict for every finite \(\kappa>0\); there are no other optimal sets or gain-dependent transitions. This is a classification of the individual optimal sets up to the evident automorphisms, not merely a comparison of heuristic placements.

To state exact objective values, define \(n=rm+1\) and \(H=(m+1)^2n\). Denote the hub-plus-peripheral type by \(A\), two vertices in one peripheral clique by \(B\), and vertices in two different peripheral cliques by \(C\). Their respective traces are
\[
J_A=\frac{\kappa^2(4mr-m-3)+2\kappa m(m+1)(3r-1)+H}{2\kappa(m+1)(\kappa+m+1)},
\]
\[
J_B=\frac{\kappa^2(7mr-4m-3)+4\kappa m(m+1)(2r-1)+H}{2\kappa(m+1)(\kappa+m+1)},
\]
\[
J_C=\frac{\kappa^2(12mr-10m-10)+4\kappa m(m+1)(2r-1)+H}{2\kappa(m+1)(2\kappa+m+1)}.
\]
Consequently the exact minimum is \(J_C\) for \(r=2\), and \(J_A\) for \(r\geq3\). Under independent unit-intensity white-noise forcing the steady-state total variance is \(J/2\), which has precisely the same minimizers.

## Assumptions and scope

All graph edges have unit conductance, all vertices experience the same unit stochastic forcing, both selected leaders have an identical finite *positive* gain \(\kappa\), and exactly two distinct vertices are selected. The graph is simple and connected. \(r,m\) are arbitrary integers at least two (the case \(r=2,m=2\) is the butterfly/friendship graph with two triangles). There is no claim for unequal gains, nonuniform edge weights, more than two leaders, or the singular gain \(\kappa=0\).

## Proof

**Step 1: spectral projectors of the windmill Laplacian.** Put \(n=rm+1\), and label the hub by \(0\); the remaining vertices are divided into \(r\) blades of \(m\) vertices. The mutually orthogonal subspaces perpendicular to the constants are (i) vectors constant on each blade, zero at the hub, with blade constants summing to zero; (ii) vectors of zero sum on each blade, zero at the hub; and (iii) the one-dimensional span of \((rm,-1,\ldots,-1)\). Direct edge-by-edge application of \(L\) gives respective eigenvalues \(1,m+1,n\), with dimensions \(r-1,r(m-1),1\). Therefore, writing \(P_1,P_{m+1},P_n\) for the corresponding orthogonal projectors,
\[
G=L^+=P_1+\frac{P_{m+1}}{m+1}+\frac{P_n}{n},\qquad
G^2=P_1+\frac{P_{m+1}}{(m+1)^2}+\frac{P_n}{n^2},
\]
\[
\operatorname{tr}G=r-1+\frac{r(m-1)}{m+1}+\frac1n.
\]
For vectors \(x,y\), let \(X_i,Y_i\) be sums of their entries in blade \(i\), and let \(X=\sum_iX_i\), \(Y=\sum_iY_i\). The projector pairings, verifiable from the preceding orthogonal decomposition, are
\[
x^{\mathsf T}P_1y=\sum_i\frac{X_iY_i}{m}-\frac{XY}{rm},\qquad
x^{\mathsf T}P_{m+1}y=\sum_{v\ne0}x_vy_v-\sum_i\frac{X_iY_i}{m},
\]
\[
x^{\mathsf T}P_ny=\frac{(rm x_0-X)(rm y_0-Y)}{rmn}.
\]

**Step 2: exact two-leader inverse trace identity.** For two different vertices \(a,b\), put \(s=e_a+e_b\) and \(d=e_a-e_b\), and \(R=d^{\mathsf T}Gd>0\). Since \(\operatorname{diag}(\mathbf1_{\{a,b\}})=(ss^{\mathsf T}+dd^{\mathsf T})/2\), use the orthogonal split \(\mathbb R^n=\operatorname{span}\{\mathbf1/\sqrt n\}\oplus\mathbf1^\perp\). The scalar constant-mode block of \(L+\kappa\operatorname{diag}(\mathbf1_{\{a,b\}})\) is \(2\kappa/n\), and its Schur complement on \(\mathbf1^\perp\) is \(L|_{\mathbf1^\perp}+(\kappa/2)dd^{\mathsf T}\). Block inversion followed by the rank-one Sherman--Morrison formula (both valid since \(L\) is positive definite on \(\mathbf1^\perp\)) gives the **exact identity**
\[
\begin{split}
J(\{a,b\})={}&\frac{n}{2\kappa}+\operatorname{tr}G+\frac n4s^{\mathsf T}Gs\\
&-\frac{\kappa}{2+\kappa d^{\mathsf T}Gd}\left(d^{\mathsf T}G^2d+\frac n4(s^{\mathsf T}Gd)^2\right).
\end{split}
\]
There is no approximation, infinite-gain limit, or omitted normalization in this formula.

**Step 3: evaluate all possible orbits.** By the graph automorphism group, every unordered pair is of exactly one of the three types \(A,B,C\) stated in the finding. Substituting the projector pairings from Step 1 into the exact identity from Step 2, and simplifying rational expressions, gives the three displayed formulas \(J_A,J_B,J_C\). This computation is independently checked with exact Gaussian elimination in the accompanying program.

**Step 4: global and strict comparison.** Direct algebra yields
\[
J_B-J_A=\frac{m(r-1)(3\kappa+2m+2)}{2(m+1)(\kappa+m+1)}>0.
\]
Also,
\[
J_C-J_A=\frac{P(r,m,\kappa)}{2(m+1)(\kappa+m+1)(2\kappa+m+1)},
\]
where
\[
P(r,m,\kappa)=(r-2)m(2\kappa+m+1)^2-4\kappa^2-(m^2+8m+7)\kappa-(m+1)^2.
\]
For \(r=2\), every term in \(P\) is negative. Hence \(J_C<J_A<J_B\). For \(r\geq3\), \(P\) increases strictly with \(r\), so it suffices to examine \(r=3\), where
\[
P(3,m,\kappa)=4(m-1)\kappa^2+(m+1)(3m-7)\kappa+(m-1)(m+1)^2.
\]
For \(m\geq3\) all three coefficients are positive. For \(m=2\), the polynomial is \(4\kappa^2-3\kappa+9>0\), since its discriminant is negative. Thus \(J_A<J_C\) whenever \(r\geq3\). Together with \(J_A<J_B\), this proves the asserted strict optimal-orbit classification and covers every allowable boundary.

## Verification

Run `python3 verify.py` in the directory containing this document. The code constructs the original full Laplacian over the rational numbers, adds the exact diagonal gains, computes inverse traces by rational Gauss--Jordan elimination, compares them to the three theorem formulas, and verifies strict rankings. It tests all three orbit representatives for \(r\in\{2,3,4,5\}\), \(m\in\{2,3,4\}\), and five positive rational gains. Separately it enumerates **all** two-vertex subsets for \(r\in\{2,3\}\), \(m\in\{2,3,4\}\), and two further rational gains. The result is `VERIFY_OK: 1566 exact rational formula/order/orbit checks`.

These finite checks reproduce exact sample instances. They are **not** offered as a proof for infinitely many graph orders or all positive real gains; the spectral and polynomial arguments above supply that proof.

## Relationship to prior work

Lin--Fardad--Jovanović (arXiv:1302.0450, first posted 2013-02-03) introduced and analyzed the same finite-gain noisy leader objective and proposed general optimization algorithms, but the inspected primary paper does not give the clique-windmill two-leader classification. Fitch--Leonard (arXiv:1407.1569, 2014-07-07) developed two-leader joint-centrality formulas and gave closed leader placements for cycles and paths; the windmill transition is not stated in the inspected paper. These formulas and methods are prior art, not claimed here as original.

Sun--Li--Liu, *Noisy consensus dynamics in windmill-type graphs* (Chaos 30, 123131, 2020; DOI:10.1063/5.0020696) is a directly relevant later study whose abstract describes exact leader--follower coherence on windmills with freely assigned leaders. Full text could not be inspected. Its stated model may use perfectly anchored leaders, in contrast with the finite-gain quantity classified here; no claim about the contents of its inaccessible theorems is made. Consequently equivalent finite-gain coverage in that source remains a material residual originality risk.

## Limitations

The sharp transition concerns only the two-leader, equal-finite-gain, unit-weight setting. The same placements can or cannot persist under unequal gains, edge heterogeneity, or different leader counts; none is proved here. The finite-gain result is not presented as the first study of windmill coherence. Absence of a covering result in indexed searches does not prove absolute novelty; in particular the full Sun--Li--Liu paper and potentially unindexed results could affect originality.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450 (first posted 2013-02-03), https://arxiv.org/abs/1302.0450 .
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 2014-07-07), https://arxiv.org/abs/1407.1569 .
3. W. Sun, Y. Li, S. Liu, *Noisy consensus dynamics in windmill-type graphs*, Chaos **30** (2020), 123131, https://doi.org/10.1063/5.0020696 .
