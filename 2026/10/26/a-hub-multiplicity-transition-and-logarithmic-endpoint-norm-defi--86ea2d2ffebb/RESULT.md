# A hub-multiplicity transition and logarithmic endpoint-norm deficits on clique-cycle joins

## Finding

For all integers \(h\geq2\) and \(n\geq4\), form the simple, unweighted graph \(G_{h,n}=K_h\vee C_n\): a clique on \(h\) hubs joined to every vertex of a rim cycle on \(n\) vertices. Fix any edge orientation, let \(D\) be its vertex-by-edge incidence matrix, and define the canonical Euclidean-orthogonal cut and cycle projections on the **real** edge space by
\[
Q=D^{\mathsf T}(DD^{\mathsf T})^+D,\qquad P=I-Q.
\]
Set \(N=n+h\), \(\Delta=\sqrt{h(h+4)}\), \(\rho=(h+2-\Delta)/2\in(0,1)\), \(m=\lfloor n/2\rfloor\), and
\[
g_j=\frac{\rho^j+\rho^{n-j}}{\Delta(1-\rho^n)}\quad(0\leq j<n),
\qquad S=\sum_{j=0}^{n-1}\left|g_j-\frac1{hN}\right|.
\]
Define the six explicit nonnegative real numbers
\[
\begin{aligned}
q_H&=2-\frac2N,& p_H&=3-\frac6N,\\
q_R&=4(g_0-g_1)+2h(g_0-g_m),&p_R&=1+2h(g_0-g_m),\\
q_S&=1+(h-1)S+2(g_0-g_m),&p_S&=2+(h-1)S-2g_m-\frac{2(h-1)}{hN}.
\end{aligned}
\]
Then the **exact** induced endpoint norms, simultaneously for \(\ell_1(E)\) and \(\ell_\infty(E)\), are
\[
\boxed{\ \|Q\|=\max\{q_H,q_R,q_S\},\qquad
\|P\|=\max\{p_H,p_R,p_S\}.\ }
\]
Here \(H\), \(R\), and \(S\) mean respectively a hub-clique edge, a rim-cycle edge, and a hub-to-rim spoke. Every edge of a given type has exactly its displayed absolute column sum. These are finite, explicit closed expressions in the two integer parameters; they involve at most \(n\) easily evaluated terms and no optimization over matrices or unknown coefficients.

The **asymptotic hub-multiplicity transition** is sharper. Write
\[
\kappa_h=\frac{4(h-1)}{h\log(1/\rho)}>0.
\]
For each fixed integer \(h\ge2\), all sufficiently long rims have their cut-norm maximum on spoke columns, and
\[
\boxed{\ \|Q\|=3-\frac2h+\frac2\Delta
-\kappa_h\frac{\log n}{n}+O_h(n^{-1}).\ }
\]
For each fixed \(h\ge3\), all sufficiently long rims have their cycle-norm maximum on spoke columns, with
\[
\boxed{\ \|P\|=4-\frac2h-\kappa_h\frac{\log n}{n}+O_h(n^{-1}).\ }
\]
At the exceptional hub multiplicity \(h=2\), **the cycle-norm maximum instead lies on hub-clique edges for all sufficiently large \(n\)**, and its exact eventual law is
\[
\boxed{\ \|P\|=3-\frac6{n+2}.\ }
\]
Thus the approach of the cycle-projection norm to its limiting value changes from an explicit logarithmic-over-linear deficit when \(h\ge3\) to a purely reciprocal-size deficit when \(h=2\). No universal numerical threshold in \(n\) is claimed for the phrase 'sufficiently large'.

Already for \(h=3\) the maximizing edge directions separate at finite sizes: at \(n=4\), both norms are maximized on rim edges (values \(66/35\) and \(11/5\)); at \(n=5\), cut maximizers remain rim edges (\(56/29\)) while cycle maximizers are spokes (\(267/116\)); at \(n=6\), both are maximized by spokes (\(2\) and \(913/378\)). These are three explicit examples, not a claimed global finite-size classification.

## Assumptions and scope

All graphs are finite, simple, connected, and unit-conductance. Both projections are the specified canonical **orthogonal** real-linear projections, rather than minima among arbitrary nonorthogonal projections. For \(n\ge4\), the rim is the ordinary \(n\)-cycle and the clique has \(h\ge2\) vertices. All norms in this document are induced operator norms on edge-coordinate \(\ell_1\) or \(\ell_\infty\). The \(O_h\) remainder is for \(n\to\infty\) with \(h\) fixed; no uniformity in an independently growing \(h\) is asserted.

## Proof

**1. Explicit inverse on the cycle.** Let \(L_C\) be the unweighted rim-cycle Laplacian. The inverse \((hI+L_C)^{-1}\) is circulant; its first column is \((g_j)_{j=0}^{n-1}\), because \(\rho+\rho^{-1}=h+2\) and \(\Delta=\rho^{-1}-\rho\). Direct substitution into the periodic recurrence
\[
(h+2)g_j-g_{j-1}-g_{j+1}=\mathbf1_{\{j=0\}}
\]
verifies the formula, including the wraparound boundary. Summing this recurrence gives \(\sum_jg_j=1/h\). Reflection symmetry gives \(g_j=g_{n-j}>0\), and \(g_j\) decreases strictly for \(0\le j\le m\) (with the expected equality of the two antipodal representatives when \(n\) is odd). Consequently
\[
\sum_j|g_j-g_{j+1}|=2(g_0-g_m).
\]
Every subscript in this proof is understood modulo \(n\).

**2. Hub-edge column.** The graph Laplacian has the block form
\[
L=\begin{pmatrix}NI_h-J_h&-J_{h,n}\\-J_{n,h}&hI_n+L_C\end{pmatrix}.
\]
For a divergence of unit mass between two hubs, a valid potential is \((e_a-e_b)/N\) on hubs and zero on rim. Taking all oriented edge gradients yields \(q_H=2-2/N\), and the diagonal is \(2/N\). Therefore \(p_H=1+q_H-4/N=3-6/N\).

**3. Rim-edge column.** For divergence \(e_0-e_1\) between two consecutive rim vertices, a potential is zero on hubs and \(x_j=g_j-g_{j-1}\) on the rim. Monotonicity from step 1 yields
\[
\sum_j|x_j|=2(g_0-g_m),\qquad
\sum_j|x_j-x_{j+1}|=4(g_0-g_1).
\]
There are \(h\) spokes incident to each rim vertex. Their summed absolute current is therefore \(2h(g_0-g_m)\), proving \(q_R\). The diagonal of the rim-edge column is \(2(g_0-g_1)\); replacing it by \(1-2(g_0-g_1)\) gives \(p_R=1+q_R-4(g_0-g_1)=1+2h(g_0-g_m)\).

**4. Spoke column.** Fix the spoke joining hub \(a\) to rim vertex \(0\), and apply divergence \(e_a-e_0\). A valid potential is obtained by choosing constants \(c_H,c_R\) with \(c_H-c_R=1/(hn)\), setting the hub potentials to \(c_H+(\mathbf1_{\{j=a\}}-1/h)/N\), and the rim potentials to \(c_R-g_j+1/(hn)\). Substitution in the block Laplacian from step 2 gives exactly the required divergence. The absolute gradients on hub-clique edges sum to \((h-1)/N\); on spokes from hub \(a\) they sum to
\[
\sum_j\left(g_j+\frac{h-1}{hN}\right)=\frac1h+\frac{n(h-1)}{hN};
\]
on spokes from the other hubs they sum to \((h-1)S\); and on rim edges they sum to \(2(g_0-g_m)\). The three elementary non-\(S\) spoke/hub contributions sum to exactly \(1\), giving \(q_S\). The diagonal spoke entry is \(g_0+(h-1)/(hN)\), so \(p_S=1+q_S-2[g_0+(h-1)/(hN)]\), which simplifies to the stated formula.

**5. Exactly three edge orbits.** Permutations of hubs and dihedral symmetries of the rim act transitively within the three indicated edge types, and the canonical projections commute with these actions. For any matrix \(M\), its induced \(\ell_1\) norm is the maximum absolute column sum; the symmetric matrices \(Q\) and \(P\) have the same induced \(\ell_\infty\) norm. Steps 2–4 therefore determine both norms exactly. For any orthogonal projection the diagonal entries lie in \([0,1]\), so \(\|P e\|_1=1+\|Qe\|_1-2Q_{ee}\) used above is valid, including at all parameter boundaries.

**6. Logarithmic edge-current threshold.** Fix \(h\ge2\) and let \(n\to\infty\). Put \(b_n=1/[h(n+h)]\) and \(L_h=\log(1/\rho)\). On the shorter arc, the exact Green expression in step 1 implies that the last index \(r_n\) satisfying \(g_{r_n}\ge b_n\) obeys
\[
r_n=\frac{\log n}{L_h}+O_h(1).
\]
Indeed, for indices \(j=O_h(\log n)\), the reflected term \(\rho^{n-j}\) is exponentially negligible and \(g_j\) is bounded above and below by fixed positive multiples of \(\rho^j\). Outside the resulting two arcs, the total Green mass is \(O_h(\rho^{r_n})=O_h(n^{-1})\). Thus
\[
\begin{aligned}
\sum_{j=0}^{n-1}\min(g_j,b_n)
&=(2r_n+1)b_n+O_h(n^{-1})\\
&=\frac{2\log n}{hL_h n}+O_h(n^{-1}),\\
S&=\sum_j(g_j+b_n-2\min(g_j,b_n))\\
&=\frac2h-\frac{4\log n}{hL_h n}+O_h(n^{-1}).
\end{aligned}
\]
The other Green quantities obey \(g_0=1/\Delta+O_h(\rho^n)\), \(g_m=O_h(\rho^{n/2})\), and \(g_0-g_1=(1-\rho)/\Delta+O_h(\rho^{n-1})\). Substituting into the exact column formulas yields
\[
\begin{array}{lll}
q_H\to2,&q_R\to2,&q_S=3-2/h+2/\Delta-\kappa_h(\log n)/n+O_h(n^{-1}),\\
p_H=3-6/(n+h),&p_R\to1+2h/\Delta<3,&p_S=4-2/h-\kappa_h(\log n)/n+O_h(n^{-1}).
\end{array}
\]
For \(q_R\to2\), use \(2h+4(1-\rho)=2\Delta\). For \(h\ge2\), the limit of \(q_S\) is strictly greater than \(2\), so spokes eventually maximize \(Q\). For \(h\ge3\), the limit of \(p_S\) is strictly greater than \(3\), while the other two limits are at most \(3\), so spokes eventually maximize \(P\). At \(h=2\), both \(p_H\) and \(p_S\) tend to \(3\), but \(p_S=3-\kappa_2(\log n)/n+O(n^{-1})\) and \(p_H=3-6/(n+2)\); the positive logarithmic term strictly dominates every bounded reciprocal-size correction for sufficiently large \(n\), so \(p_H>p_S\) eventually. Since \(p_R\to1+2/\sqrt3<3\), hub edges then uniquely maximize the cycle norm. This proves all asymptotic claims without extrapolation from finite tests.

## Verification

The accompanying `clique_cycle_checker.py` independently constructs each full graph incidence/Laplacian matrix, inverts a grounded Laplacian over exact rational numbers, and computes **every** cut- and cycle-projection column sum; a separate inversion of the smaller rim resolvent computes the claimed rational Green entries. All six formulas agree for 31 parameter pairs (\(h\in\{2,3,4,5\}\) and \(4\le n\le10\), plus three larger configurations), totaling 1,205 exact edge columns. It also checks the Green mass identity and monotonicity on each tested cycle. The checker uses only the Python 3 standard library. These are finite corroborations; the proof above establishes all integer parameters and asymptotics.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii develop canonical and invariant projections onto graph cut/cycle spaces and compute them for Hamming cubes, tori and related graphs [1]. Their results motivate the endpoint-norm question but contain no clique-cycle join formula or hub-multiplicity asymptotic transition. Sedlák and Slavík give a general graph-join **effective-resistance** kernel and Chebyshev expressions for cycle joins [2]. Their result supplies nearby spectral information and, by polarization, enough data to recover individual transfer-current entries, but it does not evaluate the absolute **edge-column sums**, the sign threshold responsible for the logarithmic term, or which of three edge types asymptotically maximizes the complementary projection. Consequently the claimed contribution is the explicit endpoint-operator-norm calculation and its phase behavior, not the underlying join Green function. Earlier single-hub weighted-wheel and Cartesian clique-cycle projection calculations concern different graph operations; neither determines this family's multi-hub edge-column sums.

## Limitations

Only the canonical Euclidean-orthogonal cut and cycle projections on real, unweighted graphs are treated. No minimum norm among nonorthogonal projections, Banach-valued extension optimum, varying-\(h\) uniform asymptotics, or explicit universal finite threshold is claimed. The formulas are exact for every finite parameter pair; the logarithmic expansions are asymptotic, with constants depending on fixed \(h\). An independently performed mathematical audit is not available.

## References

[1] Stephen J. Dilworth, Denka Kutzarova, Mikhail I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, publicly posted 21 May 2023; sections 1.1–1.4, 2.6–2.7, https://arxiv.org/abs/2305.12582.

[2] Jan Sedlák and Antonín Slavík, *Resistance distances and Kirchhoff indices in graph joins*, *Journal of Physics A: Mathematical and Theoretical* 58 (2025), 505203, DOI:10.1088/1751-8121/ae2997, published 22 December 2025; sections 2–3, https://doi.org/10.1088/1751-8121/ae2997.
