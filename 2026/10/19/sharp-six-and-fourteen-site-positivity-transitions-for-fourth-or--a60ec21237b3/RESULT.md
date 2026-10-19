# Sharp six- and fourteen-site positivity transitions for fourth-order Gauss steps on cycles

## Finding

Let \(C_n\) be the simple unweighted undirected cycle with \(n\geq3\) vertices and combinatorial Laplacian \(L_n=2I-A_n\). For every real step \(h\geq0\), form the two-stage Gauss--Legendre fourth-order end-step operator
\[
T_n(h)=\bigl(I-\tfrac h2 L_n+\tfrac{h^2}{12}L_n^2\bigr)
\bigl(I+\tfrac h2 L_n+\tfrac{h^2}{12}L_n^2\bigr)^{-1}.
\]
The following exact three-way classification holds:

1. For \(3\leq n\leq5\), \(T_n(h)\) is entrywise nonnegative for **every** \(h\geq0\), and strictly positive entrywise for \(h>0\).
2. For \(6\leq n\leq13\), \(T_n(h)\) is strictly positive entrywise for every sufficiently small positive \(h\), but has a negative entry for **every sufficiently large** \(h\).
3. For every \(n\geq14\), \(T_n(h)\) has a negative entry for **every sufficiently small** positive \(h\) and also for **every sufficiently large** \(h\).

The first small-step obstruction on a cycle therefore occurs **exactly at fourteen vertices**, in contrast with the first large-step obstruction at **six vertices**. For \(n=6\) the complete nonnegative-step set is \(0\leq h\leq h_6\), where \(h_6\approx6.368850809631016\) is the unique positive root of
\[
5h^4-12h^3-102h^2-144h-72=0.
\]

There is also a sharp spatial law for large steps. For a fixed \(n\), every off-diagonal entry at cycle distance \(d\) has expansion
\[
[T_n(h)]_{0d}=-\frac{12}{h}\left(\frac{n^2-1}{12n}-\frac{d(n-d)}{2n}\right)+O_n(h^{-2}),\qquad h\longrightarrow\infty.
\]
In the iterated limit in which \(h\to\infty\) first at each fixed \(n\), then \(n\to\infty\), the fraction of off-diagonal positions in each row that are negative converges to \(1-1/\sqrt3\). Entries where the leading coefficient vanishes affect at most four positions in a row and do not alter the limit.

## Assumptions and scope

The edges of \(C_n\) have unit conductance; no spatial rescaling or boundary condition is implicit. The matrix \(T_n(h)\) is the exact rational end-step map of the two-stage, order-four Gauss--Legendre Runge--Kutta method for \(u'=-L_n u\). All statements concern exact real arithmetic, **end-step** entrywise nonnegativity, and one time step, not positivity of internal Runge--Kutta stages or of floating-point computations. The matrix exists for every \(h\geq0\), is symmetric, and has row and column sums one. Entrywise nonnegativity is thus exactly the requirement that the end-step be a Markov transition kernel. Quantifiers in the small- and large-step claims are per fixed \(n\), not uniform in \(n\).

## Proof

**1. Spectral well-posedness and normalization.** Define
\[
r(z)=\frac{1+z/2+z^2/12}{1-z/2+z^2/12}.
\]
The graph Laplacian is positive semidefinite. For each \(x\geq0\), both \(1-x/2+x^2/12\) and \(1+x/2+x^2/12\) are strictly positive. Therefore \(r(-hL_n)\) is symmetric positive definite (as a matrix function) and its diagonal is positive. Since \(L_n\mathbf 1=0\) and \(r(0)=1\), row and column sums are one. This shows, importantly, that any failure below is purely **entrywise positivity**, not spectral stability or mass conservation.

**2. Exact small-step coefficient and graph-distance argument.** The Taylor expansion is
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{144}+0z^6-\frac{z^7}{1728}+O(z^8).
\]
If two distinct cycle vertices are at distance \(d\), then \((L_n^k)_{ij}=0\) for \(0\leq k<d\), because \(L_n=2I-A_n\). Moreover, \((-1)^d(L_n^d)_{ij}=(A_n^d)_{ij}>0\). Consequently the leading entry coefficient is positive for distances \(1\leq d\leq5\): it equals \(a_d(A_n^d)_{ij}h^d\), where \(a_1=1\), \(a_2=1/2\), \(a_3=1/6\), \(a_4=1/24\), and \(a_5=1/144\).

For distance six the sixth Taylor coefficient vanishes, so the first possible term is \(h^7(L_n^7)_{ij}/1728\). For \(C_{12}\), the antipodal entry has \((L_{12}^7)_{0,6}=28\): there are two shortest six-step walks, no seven-step walks, and the binomial coefficient of \(A_n^6\) in \((2I-A_n)^7\) equals fourteen. For \(C_{13}\), \((L_{13}^7)_{0,6}=13\), since there is one six-step walk and one seven-step walk. Both leading coefficients are positive. In all cycles with \(n\leq11\), the maximum distance is at most five. Thus every off-diagonal entry is positive at all sufficiently small positive steps on exactly the cycle sizes \(n\leq13\) relevant to this conclusion; finitely many entries let us take a common sufficiently small step neighborhood.

For every \(n\geq14\), vertices at cycle distance seven have \((L_n^7)_{0,7}=-(A_n^7)_{0,7}\), because shorter powers cannot connect them. The adjacency walk count equals two when \(n=14\) and one when \(n\geq15\). Therefore
\[
[T_n(h)]_{0,7}=-\frac{(A_n^7)_{0,7}}{1728}h^7+O_n(h^8)<0
\]
for every sufficiently small positive \(h\). This proves the sharp fourteen-vertex small-step cutoff.

**3. Exact all-step positivity through five vertices.** Circulant symmetry reduces each off-diagonal position to its cycle distance. Write \(t=h\). In \(C_3\), distance-one entries equal
\[
\frac{4t}{3t^2+6t+4}.
\]
In \(C_4\), distances one and two respectively equal
\[
\frac{3t}{4t^2+6t+3},\qquad
\frac{9t^2(t+1)}{(t^2+3t+3)(4t^2+6t+3)}.
\]
In \(C_5\), writing \(D_5(t)=25t^4+150t^3+360t^2+360t+144\), distances one and two respectively equal
\[
\frac{72t(t+2)}{D_5(t)},\qquad
\frac{12t^2(5t+6)}{D_5(t)}.
\]
Every displayed expression is strictly positive for \(t>0\). The diagonal is strictly positive by Step 1. At \(t=0\) the matrix is the identity. This completes the unconditional-positive case.

**4. Large-step obstruction and its spatial extent.** For a fixed nonzero Laplacian eigenvalue \(\lambda\), scalar expansion gives \(r(-h\lambda)=1-12/(h\lambda)+O(h^{-2})\). The constant eigenspace stays at eigenvalue one. Spectral calculus on the orthogonal complement of constants gives
\[
T_n(h)=I-\frac{12}{h}L_n^++O_n(h^{-2}),
\]
where \(L_n^+\) is the Moore--Penrose pseudoinverse. Its exact kernel is
\[
[L_n^+]_{0d}=\frac{n^2-1}{12n}-\frac{d(n-d)}{2n},
\qquad 0\leq d\leq n-1.
\]
To reconstruct this identity, set \(g_d\) equal to the right side and verify the periodic second difference \(2g_d-g_{d-1}-g_{d+1}=\mathbf1_{d=0}-1/n\) and \(\sum_d g_d=0\); these determine the pseudoinverse uniquely. In particular,
\[
[L_n^+]_{0,1}=\frac{(n-1)(n-5)}{12n}>0\quad\text{if and only if }n\geq6.
\]
Hence the nearest-neighbor entry of \(T_n(h)\) becomes negative for every sufficiently large \(h\) in every \(n\geq6\), proving the sharp six-vertex obstruction.

At a fixed \(n\), when \(d(n-d)<(n^2-1)/6\), the corresponding off-diagonal entry is eventually negative; when the inequality is reversed, it is eventually positive. At equality, the leading asymptotic term vanishes and the assertion deliberately leaves the sign unspecified. There are at most two distinct distance values satisfying equality and hence at most four affected positions per row. The strict inequality occupies asymptotically the fraction \(1-1/\sqrt3\) of the circle, proving the asserted spatial limit independently of those borderline positions.

**5. Exact positivity horizon in the first failing cycle.** For \(C_6\), let
\[
D_6(t)=(t^2+6t+12)(3t^2+6t+4)(4t^2+6t+3).
\]
All denominators are strictly positive for \(t>0\). Direct exact inversion of the degree-two Padé denominator gives entries at distances one, two, and three:
\[
\begin{aligned}
[T_6(t)]_{0,1}&=-\frac{2t(5t^4-12t^3-102t^2-144t-72)}{D_6(t)},\\
[T_6(t)]_{0,2}&=\frac{2t^2(13t^3+48t^2+72t+36)}{D_6(t)},\\
[T_6(t)]_{0,3}&=\frac{2t^3(19t^2+48t+24)}{D_6(t)}.
\end{aligned}
\]
Distance-two and distance-three entries remain positive for all \(t>0\). The distance-one numerator is governed by the quartic \(Q(t)=5t^4-12t^3-102t^2-144t-72\). Descartes' rule of signs and \(Q(0)<0\), \(Q(t)\to\infty\) prove there is exactly one positive zero, at \(t=h_6\). Therefore the entire matrix is entrywise nonnegative exactly for \(0\leq h\leq h_6\), with the only vanishing off-diagonal entries at the endpoint being the adjacent ones.

## Verification

The exact symbolic/rational replay is `python artifacts/verify_cycle_pade.py` using the dependency in `artifacts/requirements.txt`. It reconstructs all small-cycle rational entries, checks the Padé power series through order seven, independently multiplies Laplacians for each distance through seven across \(3\leq n\leq30\), and verifies the pseudoinverse's defining equations on \(3\leq n\leq39\). It also checks the six-cycle quartic root count and compares rational inverse matrices for selected steps and sizes. On the reviewed package the script completed `VERIFY_OK` with 438 exact assertions. These finite tests corroborate, but do not substitute for, the all-\(n\) proof above.

## Relationship to prior work

General positivity and absolute-monotonicity theory already explains why the fourth-order \([2/2]\) Padé map is **not** uniformly positivity-preserving over arbitrary positive systems. In particular, Lóczi and Ketcheson establish that its radius of absolute monotonicity is zero; their preprint was publicly posted on 26 March 2013 [1]. Zappavigna, Colaneri, Kirkland, and Shorten demonstrate small-step negativity on an eight-dimensional nilpotent/Metzler example, not symmetric cycle Laplacians [2]. A separate published result establishes the eight-state minimum for arbitrarily small positivity failure among general conservative finite-state Markov generators and an exact window for a directed pure-birth chain [3]. These stronger statements on **larger problem classes** do not determine the three cycle-specific size regimes, the six-cycle first loss time, or the large-step spatial sign fraction: in particular a smallest unrestricted counterexample need not be symmetric or a cycle, and no uniform method-level positivity radius supplies a cycle-by-cycle sharp cutoff. The present claim is a separate classification under unit undirected-cycle geometry, not a claim that negative Padé entries were previously unknown.

## Limitations

The result does not give the complete positivity set for \(n\geq7\); possible intermediate windows or multiple sign changes are left open. It does not cover non-unit edge rates, directed rings, higher-order Padé approximants, other boundary conditions, or internal stages. The fraction \(1-1/\sqrt3\) is an **iterated** large-step/large-size limit, not a uniform-in-size finite-step bound. A full independent audit of scientific originality remains outstanding; an equivalent unindexed cycle specialization is possible.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, first public posting 2013-03-26, later *LMS Journal of Computation and Mathematics* 17 (2014), 159–205. https://arxiv.org/abs/1303.6651
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, *Linear Algebra and its Applications* 436 (2012), 3425–3442, freely accessible author preprint. https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf
3. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, publicly available scientific result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md
