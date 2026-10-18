# Two sharp finite-gain leader transitions on two-leaf pineapple graphs

## Finding
For each integer \(r\ge2\), let \(G_r\) be the unit-conductance graph formed by joining a central vertex \(H\) to every vertex of a clique \(K_r\) and to two pendant vertices \(L_1,L_2\). Equivalently, \(G_r\) is the pineapple graph consisting of \(K_{r+1}\) with two new leaves at one common clique vertex. Let \(L_r\) be its combinatorial Laplacian. For every finite gain \(\kappa>0\) and each two-element vertex set \(S\), set
\[
J_r(S;\kappa)=\operatorname{tr}\!\left[(L_r+\kappa\operatorname{diag}(\mathbf1_S))^{-1}\right].
\]
Define two strictly ordered positive thresholds
\[
\alpha_r=\frac{r+1}{r-1}\left(\sqrt{(r-1)^2+4}-2\right),\qquad
\beta_r=\frac{r^2+r+2+\sqrt{(r^2+r+2)^2+2(r-1)(r^2-1)}}{r-1}.
\]
For \(0<\kappa<\alpha_r\), exactly the pairs \(\{H,C\}\), with \(C\) a clique vertex other than \(H\), minimize \(J_r\). For \(\alpha_r<\kappa<\beta_r\), exactly the pairs \(\{L_i,C\}\) minimize it. For \(\kappa>\beta_r\), exactly the pairs \(\{H,L_i\}\) minimize it. At \(\kappa=\alpha_r\), both the first and second types, and no others, minimize it; at \(\kappa=\beta_r\), both the second and third types, and no others, minimize it. Thus there are exactly two genuine gain-dependent changes of optimal leader type for every \(r\ge2\).

## Assumptions and scope
Graphs are undirected, unweighted, finite and connected. Every vertex receives independent equal-intensity disturbance; selected vertices have an identical positive, finite anchoring gain \(\kappa\). Each two-element set is eligible, with no imposed symmetry on its choice. The objective is trace of the inverse of the positive-definite anchored Laplacian (twice the usual unit-noise steady-state total variance). The result excludes heterogeneous gains, weighted edges, and more or fewer than two leaders.

## Proof
Let \(R_{xy}\) denote effective resistance between vertices \(x,y\), \(n=r+3\), and set \(S_x=\sum_zR_{zx}\) and \(T_{xy}=\sum_z(R_{zx}-R_{zy})^2\). The following two-ground identity holds on every connected unit-conductance graph, for distinct \(x,y\):
\[
\operatorname{tr}[(L+\kappa(e_xe_x^{\mathsf T}+e_ye_y^{\mathsf T}))^{-1}]
=\frac{n}{2\kappa}+\frac{S_x+S_y}{2}-\frac{nR_{xy}}4
-\frac{\kappa T_{xy}}{4(2+\kappa R_{xy})}.\tag{1}
\]
For completeness, at a test vertex \(z\), injecting one unit of current and grounding \(x,y\) through conductances \(\kappa\) gives respective ground currents \(a,1-a\). Thomson's quadratic energy principle (or elimination of the grounded potentials) gives diagonal Green's entry as the minimum over real \(a\) of
\[
aR_{zx}+(1-a)R_{zy}-a(1-a)R_{xy}+\frac{a^2+(1-a)^2}{\kappa}.
\]
Completing the square yields
\[
\frac1{2\kappa}+\frac{R_{zx}+R_{zy}}2-\frac{R_{xy}}4
-\frac{\kappa(R_{zy}-R_{zx})^2}{4(2+\kappa R_{xy})}.
\]
Summing over \(z\) proves (1). Positive-definiteness follows from connectivity and the two positive anchoring gains.

Let \(C\) denote a core vertex other than \(H\), and \(L\) a leaf. All core-pair resistances, including \(R_{HC}\), equal \(h=2/(r+1)\); \(R_{HL}=1\), \(R_{LL'}=2\), and \(R_{LC}=1+h\), by pendant-edge series reduction and the complete-graph resistance formula. Their resistance sums are
\[
S_H=\frac{2(2r+1)}{r+1},\quad S_L=\frac{r^2+6r+3}{r+1},\quad S_C=\frac{2(2r+3)}{r+1}.
\]
There are precisely five pair orbits under graph automorphisms. For the types \(HL,HC,LL,LC,CC\), the respective resistance values \(R_{xy}\) are \(1,h,2,1+h,h\), while the respective \(T_{xy}\) values are
\[
r+3,\quad \frac{16}{(r+1)^2},\quad 8,\quad
\frac{r^3+5r^2+7r+19}{(r+1)^2},\quad \frac8{(r+1)^2}.
\]
These identities follow directly by summing separately over \(H\), the two leaves, and the \(r\) core vertices. Equation (1) therefore gives exact rational expressions for all five objective values.

Write \(J_{XY}\) for the common objective of the corresponding pair orbit. Direct substitution, with all denominators strictly positive, gives
\[
J_{LL}-J_{HL}=\frac{(r-1)\kappa^2+2(r-2)\kappa+(r-1)}{2(\kappa+1)(\kappa+2)}>0,
\]
\[
J_{CC}-J_{HC}=\frac{3\kappa+2r+2}{(r+1)(\kappa+r+1)}>0.
\]
Hence only \(HC,LC,HL\) can be optimal. Their comparison differences are
\[
J_{HL}-J_{HC}=\frac{(r-1)(r+1-\kappa)(\kappa+r+3)}{2(\kappa+2)(r+1)(\kappa+r+1)},\tag{2}
\]
\[
J_{LC}-J_{HC}=\frac{(r-1)(r+1)^2-4(r+1)\kappa-(r-1)\kappa^2}{2(\kappa+r+1)(\kappa(r+3)+2(r+1))},\tag{3}
\]
\[
J_{HL}-J_{LC}=\frac{-(r-1)\kappa^2+2(r^2+r+2)\kappa+2(r^2-1)}{(\kappa+2)(r+1)(\kappa(r+3)+2(r+1))}.\tag{4}
\]
The numerator in (3) is strictly decreasing from positive to negative and has unique positive root \(\alpha_r\). The numerator in (4) is a concave quadratic with one positive and one negative root; its positive root is \(\beta_r\). Equation (2) changes sign at \(r+1\). The root of (3) lies below \(r+1\), since its value at \(r+1\) is \(-4(r+1)^2\); the numerator in (4) at \(r+1\) is \((r+1)^2(r+3)>0\), so \(\beta_r>r+1\). Consequently \(0<\alpha_r<r+1<\beta_r\), and the three comparisons establish the asserted strict phases and the exact two boundary ties. Exhaustion of all five pair orbits proves global optimality.

## Verification
The self-contained Python program `check_pineapple.py` symbolically verifies the five difference identities and performs exact-rational full-matrix inverse-trace comparisons for every leader pair on each graph \(2\le r\le9\) at six positive gains. This is auxiliary finite verification; the preceding resistance argument and sign analysis establish the theorem for every \(r\ge2\) and real \(\kappa>0\).

## Relationship to prior work
The finite-gain anchored-Laplacian trace objective comes from Lin, Fardad and Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks* (first arXiv version 3 February 2013, arXiv:1302.0450). Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* (first arXiv version 7 July 2014, arXiv:1407.1569), provide general two-leader resistance and pseudoinverse formulations and explicit examples on cycles and paths. Their general identities are consistent with (1) but do not explicitly give the present three-phase pineapple placement classification. The present contribution is the graph-family-specific optimality and exact two thresholds, not the general noisy-leader or resistance machinery.

## Limitations
The literature comparison does not constitute a proof that no equivalent unindexed theorem exists. The exact pairwise formulas and all-order inequalities are proved only for two identical gains, two pendant leaves attached to one clique vertex, and unit edge conductances. Numerical tests alone do not certify the all-order result.

## References
1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, original public posting 2013-02-03; IEEE Trans. Automat. Control 59 (2014), 1789–1802.
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, original public posting 2014-07-07; IEEE Trans. Control Network Syst. 3 (2016), 366–378.
