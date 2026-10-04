# Exact finite-hull solution of the selective AI–human testing benchmark

## Finding
For one direction \(h\in\{0,1\}\) of the information-theoretic lower bound in Ham, Zhao, Jasin, and Yang, sort the report values so that
\[
d_1\ge d_2\ge\cdots\ge d_m\ge0,
\]
write \(g_j>0\) for their probabilities, and define
\[
W_q=\sum_{j=1}^q g_j,\qquad D_q=\sum_{j=1}^q g_jd_j,
\]
with \(W_0=D_0=0\). Let \(I=I_R^{(h)}\) and \(J=J_X^{(h)}=I+D_m\). Associate to every escalation breakpoint \(q\in\{0,\ldots,m\}\) the information-cost point
\[
(K_q,C_q)=\bigl(I+D_q,\;c_{\mathrm{AI}}+c_{\mathrm H}W_q\bigr),
\]
and add the direct-human point \((J,c_{\mathrm H})\) and the idle point \((0,0)\). Let \(L_h\) be the lower convex envelope of this finite set after deleting duplicate-information points with larger cost.

Then, for every \(N>0\) and \(T\ge0\), the inner benchmark in Eq. (21) of the source paper is exactly
\[
\Gamma_h(T,N)=N L_h(T/N)
\]
when \(T\le NJ\), and is infeasible when \(T>NJ\). Therefore an optimal solution needs at most two non-idle sensing modes. In particular, the full-escalation AI-first point is \((J,c_{\mathrm{AI}}+c_{\mathrm H})\), so it is strictly dominated by direct human sensing whenever \(c_{\mathrm{AI}}>0\).

There is also an exact criterion for whether report-selective escalation can improve on merely mixing the pure AI-only and pure human-only modes. Assume \(0<I<J\) and \(0<c_{\mathrm{AI}}<c_{\mathrm H}\). A selective-escalation point lies strictly below the chord joining \((I,c_{\mathrm{AI}})\) and \((J,c_{\mathrm H})\) at some information level if and only if
\[
\frac{c_{\mathrm{AI}}}{c_{\mathrm H}}
<1-\frac{J-I}{d_1}.
\]
Thus the largest conditional follow-up information \(d_1\), not the average residual information alone, determines whether selective escalation has genuine cost-information value beyond randomized switching between the two pure sources.

Finally, if the hull segments are written \(L_h(x)=a_{h,j}x+b_{h,j}\), then on the corresponding ranges of \(N\),
\[
\Gamma_h(T_h,N)=a_{h,j}T_h+b_{h,j}N.
\]
Consequently the continuous relaxation of the paper's outer lower bound is convex and piecewise affine. Its breakpoints come only from transformed hull vertices \(N=T_h/K\) and crossings of one affine piece for \(h=0\) with one for \(h=1\). The exact integer minimum is therefore obtained by evaluating the integer neighbors of this finite candidate set together with the feasibility boundary. This replaces the paper's generic finite sequence of convex programs by finite planar hull geometry.

## Assumptions and scope
The result uses the source paper's finite report alphabet, positive report probabilities, nonnegative conditional information values, and positive query costs. It concerns the deterministic information-theoretic benchmark \(\Gamma_h\) and the derived lower bound, not the exact finite-error optimum over adaptive testing policies. The equality \(J=I+D_m\) is the source paper's chain-rule identity. The two-mode statement concerns the continuous expected-count program used in the lower bound; it does not assert that a realized sequential policy uses only two actions on every sample path.

The selective-escalation criterion additionally assumes \(0<I<J\) and \(0<c_{\mathrm{AI}}<c_{\mathrm H}\). If \(d_1=0\), then \(J=I\) and this nondegenerate criterion does not apply.

## Proof
The source paper proves that its follow-up frontier is piecewise linear. More precisely, for \(s\in[W_{q-1},W_q]\), the optimal follow-up rule fully escalates report values \(1,\ldots,q-1\), randomizes only at report \(q\), and leaves the rest un-escalated. Hence
\[
\Psi_h(s)=D_{q-1}+d_q(s-W_{q-1}).
\]
Therefore
\[
\bigl(I+\Psi_h(s),\;c_{\mathrm{AI}}+c_{\mathrm H}s\bigr)
\]
is exactly the line segment joining \((K_{q-1},C_{q-1})\) and \((K_q,C_q)\).

Now take any feasible triple \((n_{\mathrm H},n_{\mathrm{AI}},n_{\mathrm{esc}})\) with \(n_{\mathrm{AI}}>0\) and set \(s=n_{\mathrm{esc}}/n_{\mathrm{AI}}\). The preceding segment identity decomposes all AI-first mass into at most two adjacent breakpoint modes with exactly the same information and query cost. Human-first mass is already the direct-human mode. Conversely, any nonnegative mixture of breakpoint modes can be implemented by aggregating its AI-first mass; concavity of \(\Psi_h\) makes the aggregated triple at least as informative at the same cost, and adjacent mixtures give equality. Thus the source program is equivalent to the finite linear program
\[
\min_{z_a\ge0}\sum_a C_a z_a
\quad\text{subject to}\quad
\sum_a K_a z_a\ge T,
\qquad
\sum_a z_a\le N,
\]
over the finite non-idle modes above.

Because every non-idle cost is positive, an optimum for \(T>0\) can be scaled down until the information constraint is tight. Adding idle mass converts \(\sum_a z_a\le N\) into equality without changing information or cost. Dividing by \(N\) shows that the minimum cost per pool item is exactly the lower convex-envelope value at average information \(T/N\), proving \(\Gamma_h(T,N)=N L_h(T/N)\). No mode supplies more than \(J\) information per item, while direct human sensing supplies exactly \(J\), so feasibility is equivalent to \(T\le NJ\). A point on a planar polygonal lower hull lies on one edge or vertex, proving the two-mode sparsity statement. At \(q=m\), the AI-first information is \(I+D_m=J\) but its cost is \(c_{\mathrm{AI}}+c_{\mathrm H}>c_{\mathrm H}\), proving strict domination by the direct-human mode.

For the selective-escalation criterion, compare the AI escalation curve at rate \(s>0\) with the pure-source chord at the same information. The selective point is cheaper exactly when
\[
c_{\mathrm H}s
<\frac{c_{\mathrm H}-c_{\mathrm{AI}}}{J-I}\Psi_h(s).
\]
Since \(\Psi_h\) is concave with \(\Psi_h(0)=0\), the ratio \(\Psi_h(s)/s\) is nonincreasing, and its right limit at zero is \(d_1\). Therefore strict improvement exists for some \(s\) exactly when
\[
d_1>\frac{c_{\mathrm H}(J-I)}{c_{\mathrm H}-c_{\mathrm{AI}}},
\]
which is algebraically equivalent to the stated threshold.

Finally, on a hull segment \(L_h(x)=a_{h,j}x+b_{h,j}\), substitution of \(x=T_h/N\) gives \(\Gamma_h(T_h,N)=a_{h,j}T_h+b_{h,j}N\). The segment changes only when \(T_h/N\) crosses a positive hull-vertex information coordinate. The maximum of the two direction-wise piecewise-affine convex functions, plus the linear data cost, is again convex and piecewise affine. A minimum of such a function occurs at a breakpoint or on a flat interval; all breakpoints are transformed hull vertices or crossings of active affine pieces. For an integer \(N\), checking the adjacent integers to those real candidates is therefore exact.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs a three-report frontier, verifies the breakpoint interpolation formula, obtains \(\Gamma_h(21,10)=25\) independently from the hull representation and the original perspective formula, verifies that only two adjacent breakpoint modes are needed, checks strict domination of full escalation, and checks the selective-value threshold against the pure-source chord. It also builds two direction-wise hulls and confirms on a finite exact example that the finite transformed-breakpoint/crossing candidate set gives the same integer outer optimum as direct enumeration.

The computation is a finite consistency check, not the proof of the general statement; the general result follows from the exact piecewise-linear representation and elementary linear-program geometry above.

## Relationship to prior work
Ham, Zhao, Jasin, and Yang introduce the report-dependent follow-up frontier \(\Psi_h\), prove its linear-program dual representation and sorted fractional-knapsack optimizer, and define \(\Gamma_h(T,N)\) as a convex program. Their Proposition 4.10 states that the lower bound can be computed by a finite sequence of convex programs. The inspected full text does not state the finite lower-hull identity \(\Gamma_h(T,N)=N L_h(T/N)\), the resulting two-mode sparsity, the strict domination of full AI-first escalation by direct human sensing, the selective-value threshold above, or the finite transformed-breakpoint/crossing evaluation of the outer benchmark.

Angelopoulos, Eisenstein, Berant, Agarwal, and Fisch study cost-optimal allocation between weak and strong raters for unbiased mean estimation. That objective does not contain the report-dependent post-score escalation frontier or the sequential-testing lower-bound program analyzed here. Classical linear programming and fractional knapsack supply ingredients used in the proof, but they do not by themselves state the source-specific reduction or threshold.

## Limitations
This is a structural refinement of the lower-bound computation, not a new lower bound on testing error and not a proof that the source lower bound equals the exact finite-sample optimal policy cost. The outer finite-candidate statement assumes positive data cost, as in the source cost model; without a positive linear data cost an unbounded flat tail can make the set of minimizing pool sizes nonunique. Ties among \(d_j\) or collinear hull points can make the optimal two-mode representation nonunique, although the value formula remains exact. A differently indexed optimization paper could contain an equivalent polyhedral observation; targeted searches and inspection of the closest source-specific literature did not find one.

## References
1. D. W. Ham, X. Zhao, S. Jasin, and F. Yang, *Human–AI-Powered Hypothesis Testing: Cost-Aware Selective AI Scoring and Sequential Human Escalation*, arXiv:2609.28859, first submitted 2026-09-24.
2. A. N. Angelopoulos, J. Eisenstein, J. Berant, A. Agarwal, and A. Fisch, *Cost-Optimal Active AI Model Evaluation*, arXiv:2506.07949, first submitted 2025-06-09.
3. D. Bertsimas and J. N. Tsitsiklis, *Introduction to Linear Optimization*, Athena Scientific, 1997.
