# Review of the graph-diameter positivity thresholds

## Correctness — PASS
The backward-Euler extrapolation is a rational function of the positive-semidefinite weighted graph Laplacian. The binomial series gives exact coefficients, including \(a_3(r)=(r-2)/(6r)\) and \(a_4(r)=(r^2-17r-6)/(24r^2)\). The first nonzero off-diagonal term at graph distance \(d\) is \(a_d(r)W_dh^d\), where \(W_d>0\) is the sum of products of edge weights along geodesics. This proves both if-and-only-if diameter classifications. The fourth-order cancellation at \(r=2\) is treated separately by an explicit diameter-three 13-vertex witness with \((L^4)_{uv}=2\). The mathematical argument is finite-graph universal; exact arithmetic checks and representative matrices support but do not replace the proof.

## Originality — PASS with residual literature risk
Constantinescu and Sandu (2008) formulate multirate implicit Euler extrapolation and general order/stability; Mona, Lagzi and Havasi (2015) treat reaction-diffusion extrapolation numerically. The closest published mathematical record, *Richardson acceleration creates a sharp positivity barrier for backward Euler* (2026), explicitly proves a scalar sign horizon for the very same extrapolation and is not claimed as new. Its scalar decay classification does not entail entrywise signs of extrapolated weighted-graph diffusion. The current claim instead determines precise graph-diameter-dependent local nonnegativity for refinements three through eighteen, with two sharp transitions. Indexed searches did not reveal exact domination, but unindexed graph-specific positivity results remain possible.

## Value — PASS
The result answers a concrete discretization design question: whether refining implicit Euler before extrapolation removes small-timestep negative transition probabilities on finite diffusion networks. It supplies an exact, all-graph criterion and an unexpected universal microstep threshold of eighteen for diameter-four graphs, as well as a counterexample to the plausible assumption that diameter three suffices for the usual two-substep scheme. The result is local in time and does not promise nonnegativity for arbitrary timestep or arbitrary extrapolation tableau.

## Closest literature and limitations
Constantinescu--Sandu, *On Extrapolated Multirate Methods*, TR-08-12 (2008), Sections 2--3; Mona--Lagzi--Havasi, *Solving Reaction-Diffusion and Advection Problems with Richardson Extrapolation* (2015), Sections 2--4; *Richardson acceleration creates a sharp positivity barrier for backward Euler* (2026), full public RESULT.md. The conclusions apply to finite connected undirected positive-weight graphs, fixed weights and the displayed two-level endpoint formula. A further independent mathematical evaluation is outstanding.

Self-review: passed. Independent audit: not yet performed.
