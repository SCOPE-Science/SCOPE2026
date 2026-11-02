# Exact cost-induced reversal between reciprocal and cyclic restoration in three-patch recruitment

## Finding
Consider a directed three-patch recruitment network with fixed forward links and two alternative types of improved return connectivity. For every \(a,c_u,c_r,B>0\), the exact best and worst investments in linearized population growth undergo a sharp, complete reversal at
\[
B_*=\frac{a c_u^3}{c_r^2}.
\]
When \(B<B_*\), spend everything on the single shortcut that completes a three-step return cycle. When \(B>B_*\), spend everything on restoring both reverse links, thereby creating two local two-step return cycles. At \(B=B_*\), **every mixture is exactly equally effective**. All endpoints and equality cases are included. This is a spectral-growth statement, not a claim about stochastic extinction or nonlinear persistence.

## Assumptions and scope
Let \(x_t\in\mathbb R_{\ge0}^3\) contain linearized patch abundances in a discrete-time model \(x_{t+1}=M(u,v)x_t\). The nonnegative per-capita recruitment matrix is
\[
M(u,v)=\begin{pmatrix}
0&u&v\\a&0&u\\0&a&0
\end{pmatrix},\qquad a>0,\quad u,v\ge0.
\]
Rows denote destination patches and columns denote source patches. Two forward links of strength \(a\) (patch 1 to 2, patch 2 to 3) are fixed. A paired reciprocal restoration applies the same added strength \(u\) to patch 2 to 1 and patch 3 to 2. A single long-return shortcut of strength \(v\) links patch 3 to 1. These are **recruitment coefficients**, not probabilities; no column-stochastic constraint is imposed. Positive costs \(c_u,c_r\) impose the exact budget
\[
2c_u u+c_r v=B,\qquad B>0.
\]
The objective is the Perron spectral radius \(\rho(M(u,v))\), a measure of asymptotic linearized abundance growth. No additional interventions or alternative patch geometries are in the feasible set.

Define
\[
\lambda_*=\frac{a c_u}{c_r},\qquad B_*=\frac{a c_u^3}{c_r^2}.
\]
For \(B<B_*\), the **unique** maximum occurs at \((u,v)=(0,B/c_r)\) and the **unique** minimum at \((B/(2c_u),0)\). For \(B>B_*\), these unique maximum and minimum allocations exchange places. For \(B=B_*\), every feasible allocation has radius exactly \(\lambda_*\).

At all positive budgets the optimal and pessimal radii are
\[
\rho_{\max}(B)=\max\!\left\{\left(\frac{a^2B}{c_r}\right)^{1/3},\sqrt{\frac{aB}{c_u}}\right\},\quad
\rho_{\min}(B)=\min\!\left\{\left(\frac{a^2B}{c_r}\right)^{1/3},\sqrt{\frac{aB}{c_u}}\right\}.
\]
For every \(r>0\), the least budget needed to reach \(\rho\ge r\) is
\[
B_{\min}(r)=\min\!\left\{\frac{c_r r^3}{a^2},\frac{c_u r^2}{a}\right\}.
\]
The achieving allocation is all shortcut for \(0<r<\lambda_*\), all reciprocal for \(r>\lambda_*\), and all allocations on the critical budget segment when \(r=\lambda_*\). This last statement does **not** assert biological persistence at an eigenvalue exactly equal to one.

## Proof
**Characteristic polynomial.** Direct determinant expansion gives
\[
F(\lambda;u,v)=\det(\lambda I-M(u,v))
=\lambda^3-2au\lambda-a^2v.
\]
The two length-two closed walks contribute the term \(2au\lambda\), and the length-three return circuit contributes \(a^2v\). For \(u,v\ge0\), not both zero, this polynomial has exactly one positive real root: if \(v>0\) it follows from the unique coefficient-sign change, and if \(v=0\) its positive root is \(\sqrt{2au}\). The matrix is irreducible even at either endpoint (a directed three-cycle or a bidirectional three-vertex path), so this root is the Perron spectral radius. Moreover, for positive \(\lambda\), \(F(\lambda;u,v)<0\) below that root and \(F(\lambda;u,v)>0\) above it. These sign claims follow from the unique positive crossing and positive leading coefficient, including the endpoint with \(v=0\).

**Budget anchor.** Substitute \(v=(B-2c_u u)/c_r\), with \(0\le u\le B/(2c_u)\):
\[
F_B(\lambda,u)=\lambda^3-\frac{a^2B}{c_r}-2au(\lambda-\lambda_*).
\]
At the distinguished positive argument \(\lambda_*\),
\[
F_B(\lambda_*,u)=\lambda_*^3-\frac{a^2B}{c_r}
=\frac{a^2}{c_r}(B_*-B),
\]
independent of investment split. Thus every feasible Perron root lies strictly below \(\lambda_*\) if \(B<B_*\), and strictly above \(\lambda_*\) if \(B>B_*\). If \(B=B_*\), the positive root is exactly \(\lambda_*\) for every \(u\).

**Strict monotonicity.** Take \(u_2>u_1\) on the same budget segment, and write \(r_1=\rho(M(u_1,(B-2c_u u_1)/c_r))\). Then the exact identity
\[
F_B(r_1,u_2)-F_B(r_1,u_1)=-2a(u_2-u_1)(r_1-\lambda_*)
\]
has strictly positive sign when \(B<B_*\), and strictly negative sign when \(B>B_*\). By the sign of the cubic about its unique positive root, this implies \(r_2<r_1\) in the former case and \(r_2>r_1\) in the latter. All equality and uniqueness claims follow immediately. The two endpoint roots satisfy
\[
\rho(M(0,B/c_r))^3=a^2 B/c_r,\qquad
\rho(M(B/(2c_u),0))^2=aB/c_u.
\]

**Minimal threshold budget.** Since \(\rho_{\max}(B)\) is the maximum of the two strictly increasing endpoint functions, \(\rho_{\max}(B)\ge r\) is equivalent to \(B\ge c_r r^3/a^2\) **or** \(B\ge c_u r^2/a\). Their equality occurs at \(r=\lambda_*\). The above uniqueness theorem specifies the minimizing allocation, and proves the target-budget formula.

## Verification
The accompanying standard-library Python file `verify_corridor.py` computes exact \(3\times3\) determinants, checks the anchor identity with rational arithmetic, and independently bisects the positive characteristic root for sampled feasible allocations. It passed 13,440 exact determinant identities, 2,688 exact anchor identities, 384 sampled monotonicity/endpoint cases, 845 critical/target-budget checks, and exact rational examples. These are regression checks; **the proof above establishes the all-parameter statement**.

An exact example takes \(a=1,c_u=2,c_r=1\). Then \(\lambda_*=2\) and \(B_*=8\). At \(B=1/8\), all shortcut achieves radius \(1/2\), while all reciprocal achieves radius \(1/4\). At \(B=8\), every split gives radius \(2\). At \(B=32\), all reciprocal gives radius \(4\), exceeding the all-shortcut value \(\sqrt[3]{32}\).

To replay: run `python3 verify_corridor.py` from a directory containing the extracted file. Python 3.9 or newer suffices; no third-party packages are required.

## Relationship to prior work
Hanski and Ovaskainen (2000) introduced metapopulation capacity as a leading eigenvalue, motivating a spectral connectivity objective. Artzy-Randrup and Stone (2010) established the importance of feedback cycles in metapopulation persistence; their full article analyzes cycle topology and critical links, but does not specify the cost-constrained comparison between two reciprocal restorations and one closure of the longer circuit. Moon, Shuai and van den Driessche (2014) developed general weighted-walk/cycle formulas for spectral questions; these encompass tools for deriving the characteristic polynomial but do not state the present budget reversal. Nesterov and Protasov (2013) treat spectral optimization over structured matrix families; their principal product-family results use independent row/column choices, unlike the two-edge coupled investment constraint here. Bertuzzo, Rodriguez-Iturbe and Rinaldo (2015) study eigenvalue-based metapopulation capacity of evolving river networks, rather than an exact three-link investment comparison.

The exact special-case classification and the degenerate continuum of equal investment outcomes are the claims assessed here, **not** originality of Perron theory, closed-walk expansions, or ecology's use of spectral connectivity. Searches did not locate a dominating published formula, but general matrix-optimization and network-design literature may contain one; historical priority should not be construed as independently established.

## Limitations
The model is a three-patch linearized recruitment abstraction. It assumes homogeneous strengths for two reciprocal interventions, an exactly linear cost, fixed forward dispersal, no within-patch self recruitment, and no simultaneous choices beyond the two specified restoration programs. Numerical checks do not prove continuous-parameter assertions. The optimal spectral radius is not by itself a theorem about finite-population persistence, demographic stochasticity, spatially heterogeneous survival, ecological implementation costs, or effects in larger arbitrary networks.

## References
1. Hanski, I. and Ovaskainen, O. (2000), *The metapopulation capacity of a fragmented landscape*, Nature 404, 755–758, doi:10.1038/35008063, published 13 April 2000.
2. Artzy-Randrup, Y. and Stone, L. (2010), *Connectivity, Cycles, and Persistence Thresholds in Metapopulation Networks*, PLoS Computational Biology 6(8), e1000876, doi:10.1371/journal.pcbi.1000876.
3. Moon, J. W., Shuai, Z. and van den Driessche, P. (2014), *Walks and cycles on a digraph with application to population dynamics*, Linear Algebra and its Applications 451, 182–196, doi:10.1016/j.laa.2014.03.003.
4. Nesterov, Y. and Protasov, V. (2013), *Optimizing the spectral radius*, SIAM Journal on Matrix Analysis and Applications 34(3), 999–1013, doi:10.1137/110850967.
5. Bertuzzo, E., Rodriguez-Iturbe, I. and Rinaldo, A. (2015), *Metapopulation capacity of evolving fluvial landscapes*, Water Resources Research, doi:10.1002/2015WR016946.
