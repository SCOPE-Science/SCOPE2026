# Exact RK4 positivity horizons on networks of maximum degree two

## Finding

Let \(G\) be any finite simple undirected **unweighted** graph with maximum degree at most two, let \(L_G\) be its combinatorial Laplacian, and define the completed classical four-stage, fourth-order Runge--Kutta heat step
\[
K_G(h)=I-hL_G+\frac{h^2L_G^2}{2}-\frac{h^3L_G^3}{6}+\frac{h^4L_G^4}{24},\qquad h\geq0.
\]
For each connected component \(H\), define its exact positivity horizon \(\rho(H)\) by the following complete table. Here \(P_n\) is the path on \(n\) vertices and \(C_n\) is the cycle on \(n\geq3\) vertices.

| Component | Exact positivity horizon |
| --- | --- |
| \(P_1\) | \(+\infty\) |
| \(P_2\) | the unique positive root of \(h^3-2h^2+3h-3=0\) |
| \(P_3\) | the unique positive root of \(9h^3-12h^2+12h-8=0\) |
| \(P_4\) | \(2/3\) |
| \(P_5\) | \(4/7\) |
| \(P_n\), \(n\geq6\) | \(1/2\) |
| \(C_3\) | the same root as \(P_3\) |
| \(C_4\) | the unique positive root of \(8h^3-8h^2+6h-3=0\) |
| \(C_5\) | the unique positive root of \(55h^3-60h^2+48h-24=0\) |
| \(C_6\) | \(1/2\) |
| \(C_7\) | \(4/7\) |
| \(C_n\), \(n\geq8\) | \(1/2\) |

Set \(\rho(G)=\min_H\rho(H)\), with \(+\infty\) for an edgeless graph. Then
\[
\boxed{K_G(h)\text{ is entrywise nonnegative}\ \Longleftrightarrow\ 0\leq h\leq\rho(G).}
\]
If \(\rho(G)<+\infty\), then for **every** \(h>\rho(G)\) some matrix entry is strictly negative. The map has unit row sums for all \(h\), so the stated range is precisely its stochasticity range. At the endpoint the entries causing the first loss are: nearest-neighbor entries for \(P_2,P_3,C_3,C_4,C_5\); distance-three entries for all other nontrivial components. In particular, the classical fourth-order method improves on the forward-Euler positivity limit for short chains and for cycles of orders \(3,4,5,7\), but not for any path of order at least six or any cycle of order six or at least eight.

The four nonrational horizons are approximately \(1.392646781703\) for \(P_2\), \(0.928431187802\) for \(P_3,C_3\), \(0.696323390851\) for \(C_4\), and \(0.720325733183\) for \(C_5\).

## Assumptions and scope

All edges have unit conductance; the Laplacian has diagonal vertex degrees and \(-1\) on adjacent off-diagonal positions. Vertex labels do not matter. The statement concerns the completed **linear autonomous** fourth-order RK4 step, not positivity at its internal stages, nonlinear equations, arbitrary weights, or graphs with degree above two. Nonnegative means all entries \(\geq0\), including structural zeros between components and pairs farther than four steps apart. An isolated vertex contributes the identity block and imposes no upper bound. This is a numerical-method classification (primary MSC2020 65L06).

## Proof

**(1) Locality and diagonal positivity.** Put \(Q=-L_G\) and \(R_4(z)=\sum_{k=0}^4z^k/k!\). The entry \([R_4(hQ)]_{uv}\) uses only walks of length at most four from \(u\) to \(v\), with stationary diagonal steps weighted by the negative vertex degree. Hence it vanishes for graph distance greater than four. Every diagonal entry is strictly positive for all \(h\geq0\): by the spectral theorem it is a convex sum of \(R_4(-h\lambda)\), and
\[
24R_4(-x)=(x^2-2x+2)^2+4((x-2)^2+1)>0
\]
for every real \(x\geq0\). Also \(Q\mathbf 1=0\), hence \(K_G(h)\mathbf 1=\mathbf 1\).

**(2) Distance-three obstruction.** On a path \(u_0,u_1,u_2,u_3\) that is the unique length-three walk connecting its endpoints and has no alternative length-four route, the unique length-three contribution is \(h^3/6\). Every possible length-four walk is obtained by inserting exactly one diagonal stay along that route, giving
\[
[K_G(h)]_{u_0u_3}=\frac{h^3}{24}\left(4-h\sum_{j=0}^3\deg(u_j)\right).
\]
For \(P_4\), the degree sum is six; for \(P_5\), the largest degree sum among the length-three subpaths is seven; and for every \(P_n\) with \(n\geq6\), an all-interior length-three subpath has degree sum eight. These yield upper bounds \(2/3,4/7,1/2\), respectively, with permanent negativity beyond the bound in the displayed entry.

For \(C_6\), each antipodal pair has **two** three-edge geodesics, yielding \(h^3(4-8h)/12\); for \(C_7\), the other direction around the ring is an extra four-edge walk, yielding \(h^3(4-7h)/24\); and for every \(C_n\) with \(n\geq8\), a distance-three pair has \(h^3(4-8h)/24\). Thus the cycle thresholds for orders six, seven, and at least eight cannot exceed \(1/2,4/7,1/2\), respectively. The exceptional seven-cycle is explained by the positive four-walk around its other side.

**(3) All remaining off-diagonal entries.** The following exhaustive normalized formulas follow by multiplying \(Q,Q^2,Q^3,Q^4\), or equivalently counting walks with diagonal stays. Each distance-one entry is \(h\) times one of the listed cubics:
\[
\begin{aligned}
g_{2}(h)&=1-h+\tfrac23h^2-\tfrac13h^3 &&(P_2),\\
g_{3}(h)&=1-\tfrac32h+\tfrac32h^2-\tfrac98h^3 &&(P_3,C_3),\\
g_{e}(h)&=1-\tfrac32h+\tfrac32h^2-\tfrac76h^3 &&(\text{path end}),\\
g_{4}(h)&=1-2h+\tfrac52h^2-\tfrac94h^3 &&(\text{middle edge of }P_4),\\
g_{n}(h)&=1-2h+\tfrac52h^2-\tfrac{55}{24}h^3 &&(\text{next-to-end path, }C_5),\\
g_{i}(h)&=1-2h+\tfrac52h^2-\tfrac73h^3 &&(\text{interior path, }C_n:n\ge6),\\
g_{c4}(h)&=1-2h+\tfrac83h^2-\tfrac83h^3 &&(C_4).
\end{aligned}
\]
The path edge classes are exactly \(g_2\) for \(P_2\), \(g_3\) for \(P_3\), \(g_e,g_4\) for \(P_4\), \(g_e,g_n\) for \(P_5\), and \(g_e,g_n,g_i\) for all larger paths. Cycle edges have the sole factor \(g_3,g_{c4},g_n,g_i\) for orders \(3,4,5,\ge6\), respectively. Every listed cubic has value one at zero and a strictly negative derivative on the entire real line: its derivative is a quadratic with negative leading coefficient and negative discriminant. Hence each has exactly one positive zero and is nonnegative precisely up to it.

For the cases in which a distance-three entry is critical, **all** edge factors are strictly positive at the proposed threshold. Explicit values are
\[
\begin{array}{c|c|c}
\text{case}&h&\text{remaining edge factors at }h\\\hline
P_4&2/3&g_e=26/81,\;g_4=1/9\\
P_5&4/7&g_e=61/147,\;g_n=253/1029\\
P_n\ (n\ge6)&1/2&g_e=23/48,\;g_n=65/192,\;g_i=1/3\\
C_6,C_n\ (n\ge8)&1/2&g_i=1/3\\
C_7&4/7&g_i=5/21.
\end{array}
\]
In the five cases with no distance-three obstruction before the edge threshold (\(P_2,P_3,C_3,C_4,C_5\)), the unique positive root of the stated edge cubic is therefore the exact endpoint.

Every distance-two entry is \(h^2\) times one of
\[
\frac{13h^2-16h+12}{24},\quad
\frac{5h^2-5h+3}{6},\quad
\frac{7h^2-6h+3}{6},\quad
\frac{7h^2-6h+3}{3},\quad
\frac{29h^2-24h+12}{24}.
\]
These quadratics have positive leading coefficients and strictly negative discriminants, hence are positive for every real \(h\). Every distance-four entry is a positive multiple of \(h^4\) (\(1/24\) for paths and ordinary cycles; \(1/12\) for antipodal pairs in \(C_8\)). Thus no entry type omitted from the table can force an earlier failure.

**(4) Exhaustiveness for unbounded graph order.** A connected graph of maximum degree two is precisely \(P_n\) or \(C_n\). A four-step walk in a path only depends on whether the local window meets an endpoint: the three eventual edge types, two distance-two types, three distance-three degree sums, and single distance-four type listed above exhaust all path orders \(n\ge6\). In a cycle of order \(n\ge9\), any four-step walk remains in the same nonwrapping local stencil; the cycle-specific wraps are exactly those shown for orders at most eight. Hence no unenumerated type arises at larger order. Block-diagonal decomposition takes the minimum of component horizons and completes the proof. In particular, the conclusion is not inferred from a finite matrix sample.

## Verification

The self-contained `verify.py` script uses SymPy rational polynomial arithmetic. It rederives the entry formulas directly from exact path and cycle Laplacians, checks all distinct normalized entry types over boundary-complete sample orders, verifies the strictly negative derivative discriminants and strictly negative distance-two discriminants, checks the endpoint rational inequalities, proves the diagonal sum-of-squares identity algebraically, and gives rational isolation intervals for each of the four nonrational roots. It also checks the general path distance-three degree-sum identity symbolically across every eligible subpath of several sizes. Run `python verify.py` after installing `sympy` (see `requirements.txt`). The infinite-size claim is justified by the preceding walk-locality proof; finite program tests are not represented as an infinite proof.

The four positive roots are isolated, respectively, in \((1.392646,1.392647)\), \((0.928431,0.928432)\), \((0.696323,0.696324)\), and \((0.720325,0.720326)\). These are exact rational intervals, not floating-point uniqueness arguments.

## Relationship to prior work

Gottlieb, Shu and Tadmor [1], especially their Section 3 and equation (3.5), give the exact convex-Euler decomposition
\[
R_4(z)=\frac38+\frac13(1+z)+\frac14(1+z)^2+\frac1{24}(1+z)^4.
\]
Thus for **any** Markov generator, not merely paths and cycles, forward-Euler nonnegativity at \(h\) guarantees completed RK4 nonnegativity at the same \(h\). In particular, the baseline \(h\leq1/2\) for paths with interior vertices and all cycles is *already implied by prior work* and is not asserted as new. What is established here beyond that bound is its **sharpness** for the infinite families, the exact larger horizons on all small exceptional paths and cycles, and the isolated seven-cycle exception with its walk-level explanation.

Ketcheson, Gottlieb and Macdonald [2] investigate SSP two-step methods and discuss the general RK SSP setting; their relevant inspected statements concern stability coefficients and method classes, not the exact graph-specific upper limits here. Hundsdorfer and collaborators [3] examine positivity of finite-difference **advection** schemes with flux limiting and Runge--Kutta time stepping, a distinct spatial operator; only its available abstract was read, so potential broader coverage in its full text is not excluded. The novelty comparison is thus specific to these exact graph-indexed horizons, not to the known positivity mechanism below the Euler limit.

## Limitations

The theorem gives **entrywise nonnegativity of one completed update** only. A fourth-order Runge--Kutta step may be linearly stable for timesteps outside this positivity set; stability is not the same as a stochastic transition matrix. No statement is made about intermediate Runge--Kutta stages, graph conductance heterogeneity, spatial operators with different boundary treatment, graph maximum degree greater than two, or nonlinear dynamics. Root uniqueness rests on exact derivative signs; rounded decimals are illustrative. Mathematical originality is assessed against available sources and is not a claim of exhaustive literature coverage. Independent external verification has not been performed.

## References

[1] S. Gottlieb, C.-W. Shu, E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89--112, DOI: 10.1137/S003614450036757X; lawful full text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download (original PDF states electronically published 2 February 2001).

[2] D. I. Ketcheson, S. Gottlieb, C. B. Macdonald, *Strong Stability Preserving Two-Step Runge--Kutta Methods*, arXiv:1106.3626, v1 made public 18 June 2011; https://arxiv.org/pdf/1106.3626; journal DOI: 10.1137/10080960X.

[3] W. Hundsdorfer, B. Koren, M. van Loon, J. G. Verwer, *A Positive Finite-Difference Advection Scheme*, Journal of Computational Physics 117 (1995), 35--46, DOI: 10.1006/jcph.1995.1042; publisher-indexed abstract: https://research.tue.nl/en/publications/a-positive-finite-difference-advection-scheme/.
