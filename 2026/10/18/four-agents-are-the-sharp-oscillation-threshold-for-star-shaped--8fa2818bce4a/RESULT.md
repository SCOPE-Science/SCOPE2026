# Four agents are the sharp oscillation threshold for star-shaped confidence sets

## Finding

Consider the homogeneous, synchronous set-based-confidence averaging model without exogenously stubborn agents. For every dimension \(d\ge 1\), every number of agents \(1\le n\le 3\), and every confidence set \(\mathcal O\subseteq\mathbb R^d\) star-shaped about \(0\), **every finite-period labeled opinion trajectory is constant**. No symmetry, boundedness, closure, or neighborhood-of-zero assumption is required of \(\mathcal O\).

This population-size restriction is sharp. A **closed star-shaped** confidence set containing the unit disk in \(\mathbb R^2\), with four ordinary (nonstubborn) agents, admits a labeled orbit of **prime period two**. Consequently four is the smallest possible number of ordinary agents for periodic motion under homogeneous star-shaped confidence, in any Euclidean opinion dimension.

## Assumptions and scope

At times \(t\in\mathbb Z_{\ge0}\), agent \(i\in\{1,\ldots,n\}\) has an opinion \(z_i(t)\in\mathbb R^d\). One common time-independent confidence set \(\mathcal O\) satisfies \(\lambda u\in\mathcal O\) for every \(u\in\mathcal O\) and \(0\le\lambda\le1\). In particular \(0\in\mathcal O\). Each agent updates simultaneously by the ordinary equal-weight rule

\[
N_i(t)=\{j:z_j(t)-z_i(t)\in\mathcal O\},\qquad
z_i(t+1)=\frac{1}{|N_i(t)|}\sum_{j\in N_i(t)}z_j(t).
\]

Self-inclusion \(i\in N_i(t)\) is automatic; agents are not externally pinned, and the state has labeled, rather than permutation-identified, periodicity. A periodic trajectory means there is a positive integer \(p\) such that \(z_i(t+p)=z_i(t)\) for every agent and all times along the trajectory. The result excludes all nonconstant such trajectories when \(n\le3\); it does **not** assert finite-time convergence, asymptotic convergence, or absence of aperiodic nonconvergent trajectories.

## Proof

**1. Constant hull on a periodic orbit.** Put \(K(t)=\operatorname{conv}\{z_1(t),\ldots,z_n(t)\}\). Each updated opinion is an average of old opinions, so \(K(t+1)\subseteq K(t)\). If the state has period \(p\), the chain \(K(t)\supseteq K(t+1)\supseteq\cdots\supseteq K(t+p)=K(t)\) forces \(K(t)=K\) independent of time.

**2. Extreme-point labels persist.** Let \(v\) be any vertex of the finite polytope \(K\), and write \(I_v(t)=\{i:z_i(t)=v\}\). If \(z_j(t+1)=v\), the average defining it is a convex combination of points in \(K\), all with strictly positive coefficients. Extremality of \(v\) implies every averaged point is \(v\), including \(z_j(t)\) because the agent trusts itself. Thus \(I_v(t+1)\subseteq I_v(t)\). The sets are periodic in time, so these inclusions must be equalities. Every label occupying any vertex therefore stays there throughout the periodic orbit.

**3. The only possible moving configuration for at most three agents.** If \(K\) is a point, every opinion is constant. If its affine dimension is at least two, it has at least three vertices; with \(n\le3\), these vertices exhaust the labels and Step 2 fixes them all. If \(K\) is a nondegenerate segment, Step 2 fixes at least one label at each endpoint. There are at most three agents, hence at most one remaining mobile label. If no such label exists the trajectory is constant. If it does, it stays strictly between the endpoints: otherwise the constant vertex-occupancy sets would contain it, and Step 2 would fix it as well.

**4. Radial star-shapedness makes the remaining scalar update order-preserving.** Write the two distinct fixed endpoint opinions as \(a\) and \(b\), put \(v=b-a\), and express the unique possible mobile opinion as \(a+s(t)v\) with \(0<s(t)<1\). Define

\[
A(s)=\boldsymbol 1_{\{-sv\in\mathcal O\}},\qquad
B(s)=\boldsymbol 1_{\{(1-s)v\in\mathcal O\}}.
\]

The mobile agent trusts the left endpoint precisely when \(A(s)=1\) and the right endpoint precisely when \(B(s)=1\). Star-shapedness about zero implies \(A(s)\) is nonincreasing and \(B(s)\) is nondecreasing in \(s\), including at any open or closed membership boundary. Since the mobile agent always averages its own opinion, its update is

\[
s(t+1)=f(s(t)),\qquad f(s)=\frac{s+B(s)}{1+A(s)+B(s)}.
\]

For fixed \(A,B\in\{0,1\}\), the function \(f_{A,B}(s)=(s+B)/(1+A+B)\) is increasing in \(s\). At fixed \(s\in[0,1]\), removing left-endpoint trust or adding right-endpoint trust cannot decrease the value, because

\[
 f_{0,B}(s)-f_{1,B}(s)=\frac{s+B}{(1+B)(2+B)}\ge0,
 \qquad f_{A,1}(s)-f_{A,0}(s)=\frac{A+1-s}{(A+1)(A+2)}\ge0.
\]

As \(s\) increases, only these two kinds of changes are possible. Thus \(f\) is nondecreasing on \((0,1)\), even when the confidence set has discontinuous radial boundaries. Any orbit of a nondecreasing one-dimensional map is either fixed or moves monotonically after its first strict displacement. A nonconstant finite cycle is impossible. This completes the proof of nonperiodicity for \(n\le3\).

**5. Sharp four-agent witness.** In \(\mathbb R^2\), let \(\overline B_1(0)\) be the closed Euclidean unit disk and set

\[
\mathcal O=\overline B_1(0)\cup
 \{(u,0):u\ge0\}\cup
 \{(u,u/5):u\le0\}\cup
 \{(u,-u/5):u\le0\}.
\]

This union is closed, star-shaped about zero, and contains a neighborhood of zero. Take the three anchor opinions \(a=(-3,1)\), \(b=(-3,-1)\), and \(c=(4,0)\), together with the fourth opinion \(x(0)=(0,0)\). Direct membership checks in \(\mathcal O\) give the respective neighbor sets

\[
\begin{array}{c|cccc}
 &x&a&b&c\\ \hline
x=(0,0)&\{x,c\}&\{a\}&\{b\}&\{c\}\\
x=(2,0)&\{x,a,b,c\}&\{a\}&\{b\}&\{c\}
\end{array}
\]

(the row entries give each agent's trusted set). Thus the anchor opinions remain unchanged, while the moving opinion follows

\[
(0,0)\ \longmapsto\ \tfrac12[(0,0)+(4,0)]=(2,0)
\ \longmapsto\ \tfrac14[(2,0)+(-3,1)+(-3,-1)+(4,0)]=(0,0).
\]

The two moving states differ, so the orbit has prime period two. This example is the four-agent construction in Zabarianska–Proskurnikov (2024), explicitly revisited here to certify sharpness of the new three-agent obstruction.

## Verification

The standalone `verify.py` uses only exact fractions. It checks all 2,925 order-comparison cases in a rational-grid test of the scalar monotonicity lemma, checks both four-agent neighborhood configurations and return updates exactly, and reproduces the source's three-agent non-star-shaped period-three example as a sharp assumption contrast. Run `python verify.py` from the directory containing the file. This finite test collection supplements the dimension-independent, all-set proof above; the test grid is not claimed to cover real-valued \(s\) or all confidence sets.

## Relationship to prior work

Zabarianska and Proskurnikov introduced the homogeneous SCOD model and provided a three-agent cycle for a confidence set **not** star-shaped at zero (their Example 2), and a four-agent cycle with star-shaped confidence (their Example 3). They did not state or prove that three agents are insufficient for periodic motion under star-shaped confidence. This result supplies precisely that missing lower bound, showing their four-agent construction is minimal. Their symmetric-confidence convergence theorem has a different hypothesis and does not cover the asymmetric star-shaped set used here. The same source cites convergence theorems for scalar interval confidence sets; those handle collinear opinion dynamics but do not, by themselves, establish why all possible three-agent periodic configurations in arbitrary dimension must reduce to a segment.

The 2022 Bernardo–Altafini–Vasca asymmetric-confidence results concern one-dimensional interval confidence; this theorem additionally uses periodic convex-hull extremality to reduce the three-agent vector-valued case to a monotone scalar map. The 2024 related discussion of heterogeneous confidence explicitly permits three-agent cycles with different agents' confidence sets; homogeneity is essential in the present statement.

## Limitations

The theorem applies to synchronous equal-weight averaging with self-confidence, a single common static confidence set, no externally stubborn agents, and finitely periodic labeled states only. It does not rule out oscillation under heterogeneous confidence, non-star-shaped sets, agents that omit themselves from averaging, other update rules, or any recurrent behavior that is not a finite cycle. The four-agent example is an existence demonstration, not a universal convergence or bifurcation classification. The result was checked against the most relevant inspected literature but independent specialist verification and comprehensive unindexed-literature coverage remain outstanding.

## References

1. I. Zabarianska and A. V. Proskurnikov, *Opinion Dynamics with Set-Based Confidence: Convergence Criteria and Periodic Solutions*, arXiv:2408.01753, first publicly posted 2024-08-03, https://arxiv.org/abs/2408.01753.
2. I. Zabarianska and A. V. Proskurnikov, *Opinion Dynamics With Set-Based Confidence: Convergence Criteria and Periodic Solutions*, IEEE Control Systems Letters **8** (2024), 2373–2378, DOI:10.1109/LCSYS.2024.3479275. Lawful author-repository copy: https://iris.polito.it/handle/11583/2993798.
3. C. Bernardo, C. Altafini, and F. Vasca, *Finite-time convergence of opinion dynamics in homogeneous asymmetric bounded confidence models*, European Journal of Control **68** (2022), 100674, DOI:10.1016/j.ejcon.2022.100674.
4. C. Bernardo, C. Altafini, A. V. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica **159** (2024), 111302, DOI:10.1016/j.automatica.2023.111302.
