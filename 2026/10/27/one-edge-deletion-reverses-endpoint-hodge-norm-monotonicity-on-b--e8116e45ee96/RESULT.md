# One-edge deletion reverses endpoint Hodge-norm monotonicity on balanced tripartite graphs

## Finding

Let \(m\ge2\) be an integer. Begin with the simple, unweighted, complete tripartite graph \(H_m=K_{m,m,m}\), whose vertex parts are \(A,B,C\), and delete one edge \(e_0=uv\) with \(u\in A\), \(v\in B\). Write \(G_m=H_m-e_0\). On real edge-coordinate spaces, let \(Q\) be the canonical Euclidean-orthogonal projector onto the cut space and \(P=I-Q\) the orthogonal projector onto the cycle space. Norms below are induced by either edge \(\ell_1\) or edge \(\ell_\infty\); the two norms agree because both projectors are symmetric matrices.

Put \(S_m=3m^2-3m+1\). For \(m=2\),
\[
\|Q_{G_m}\|=\frac{13}{7},\qquad \|P_{G_m}\|=2.
\]
For every \(m\ge3\),
\[
\boxed{\|Q_{G_m}\|=\frac{16m^4-26m^3+16m^2-5m+1}{2m^2S_m}.}
\]
The cycle-projection norm has a sharp second transition:
\[
\boxed{
\|P_{G_m}\|=\begin{cases}
\dfrac{142}{57},&m=3,\\[3pt]
\dfrac{(m-1)(22m^3-22m^2+9m-2)}{2m^2S_m},&m\ge4.
\end{cases}}
\]

The maximizing edges are **exactly** as follows: at \(m=2\), both norms are maximized on the single edge joining the non-deleted vertices of \(A\) and \(B\); at \(m=3\), the cut norm is maximized on the \(2m\) edges joining \(u\) or \(v\) to \(C\), while the cycle norm is maximized on the \((m-1)^2\) edges joining \(A\setminus\{u\}\) to \(B\setminus\{v\}\); for every \(m\ge4\), both norms are maximized exactly on the \(2m\) edges joining \(u\) or \(v\) to \(C\). All comparisons are strict between the maximizing orbit and the other edge orbits.

For the intact graph,
\[
\|Q_{H_m}\|=\frac{2(4m^2-3m+1)}{3m^2},\qquad
\|P_{H_m}\|=\frac{11m^2-12m+4}{3m^2}.
\]
Thus deleting an edge **strictly increases** the canonical cut-projection norm for every \(m\ge2\) and **strictly increases** the canonical cycle-projection norm for every \(m\ge3\), while leaving the latter unchanged for \(m=2\). The two strict increases share the asymptotic law
\[
\|Q_{G_m}\|-\|Q_{H_m}\|=\frac{1}{3m}+O(m^{-2}),\qquad
\|P_{G_m}\|-\|P_{H_m}\|=\frac{1}{3m}+O(m^{-2}).
\]
This gives an infinite family of explicit edge-addition reversals for endpoint cycle-projection norms, including precise maximizing-edge phase transitions.

## Assumptions and scope

All vertices and edges are distinct; all present edges have unit conductance, and the graph is connected for every \(m\ge2\). Choose an arbitrary orientation of the edge set and let \(D\) be its vertex-edge incidence matrix. The cut projection is \(Q=D^{\mathsf T}(DD^{\mathsf T})^+D\), where \((\cdot)^+\) is the Moore--Penrose inverse; the cycle projection is \(P=I-Q\). Reversing orientations conjugates either matrix by a diagonal sign matrix and does not change its induced endpoint norm. Both projectors are real and symmetric. No minimization over **arbitrary** (nonorthogonal) projections is asserted.

For an edge \(f\), write \(q_f=\sum_e|Q_{ef}|\) and \(p_f=\sum_e|P_{ef}|\). Symmetry of the matrices makes the maximum absolute column sum equal to both induced endpoint operator norms.

## Proof

**Unpunctured Green kernel.** Put \(N=3m\). In \(H_m\), the Laplacian acts by the scalar \(2m\) on each part's zero-sum subspace and by \(3m\) on the subspace of part-constant vectors with total sum zero. For a unit current along an edge \(f=st\) from a vertex \(s\) in one part to a vertex \(t\) in a different part, an allowed potential with mean zero is
\[
\phi_f(x)=\frac{1}{6m^2}
\begin{cases}
3m-1,&x=s,\\
-1,&x\ne s\text{ in the part of }s,\\
-(3m-1),&x=t,\\
1,&x\ne t\text{ in the part of }t,\\
0,&x\text{ in the remaining part}.
\end{cases}
\]
The Laplacian eigen-decomposition above verifies \(L_{H_m}\phi_f=\mathbf e_s-\mathbf e_t\). In particular the resistance of the edge \(e_0\) is \(r_0=(3m-1)/(3m^2)<1\).

**Deleting the edge.** Since \(L_{G_m}=L_{H_m}-b_0b_0^{\mathsf T}\), where \(b_0=\mathbf e_u-\mathbf e_v\), applying the Sherman--Morrison identity on the zero-sum vertex space gives, for each surviving oriented edge \(f=st\),
\[
\phi'_f=\phi_f+\frac{\phi_{e_0}(s)-\phi_{e_0}(t)}{1-r_0}\phi_{e_0},
\qquad 1-r_0=\frac{S_m}{3m^2}>0.
\]
The signed transfer-current entry in row \(e=xy\), column \(f\) is \(Q_{ef}=\phi'_f(x)-\phi'_f(y)\).

**All edge orbits and exact column sums.** The surviving edges split into four disjoint orbits under permutations fixing the deleted endpoints and swapping the first two vertex parts:

- \(X\): edges from \(u\) to \(B\setminus\{v\}\), or from \(A\setminus\{u\}\) to \(v\), of cardinality \(2(m-1)\).
- \(Y\): edges joining \(A\setminus\{u\}\) to \(B\setminus\{v\}\), of cardinality \((m-1)^2\).
- \(Z\): edges joining \(u\) or \(v\) to \(C\), of cardinality \(2m\).
- \(W\): edges joining \((A\cup B)\setminus\{u,v\}\) to \(C\), of cardinality \(2m(m-1)\).

For any column in a specified orbit, direct substitution of the displayed potential into its edge differences, followed by summing absolute values, gives the following **four exact pairs**; denominators are positive for \(m\ge2\):

| Orbit | \(q_f\) | \(p_f\) |
|:---:|:---|:---|
| \(X\) | \(\dfrac{(2m-1)(4m^2-5m+2)}{mS_m}\) | \(\dfrac{22m^3-46m^2+33m-8}{2mS_m}\) |
| \(Y\) | \(\dfrac{8m^3-14m^2+11m-4}{mS_m}\) | \(\dfrac{(m-1)(11m^2-12m+8)}{mS_m}\) |
| \(Z\) | \(\dfrac{16m^4-26m^3+16m^2-5m+1}{2m^2S_m}\) | \(\dfrac{(m-1)(22m^3-22m^2+9m-2)}{2m^2S_m}\) |
| \(W\) | \(\dfrac{16m^4-28m^3+21m^2-8m+1}{2m^2S_m}\) | \(\dfrac{(2m^2-2m+1)(11m^2-12m+2)}{2m^2S_m}\) |

The cycle-column identity is \(p_f=1+q_f-2Q_{ff}\); here \(0\le Q_{ff}\le1\) since \(Q\) is an orthogonal projection. The absolute-value signs in the table are **not** inferred numerically: a complete symbolic certificate in `verify_symbolic.py` derives the scaled potentials from the rank-one formula and proves each of the 80 relevant signed edge-type differences has a definite sign for every integer \(m\ge2\), by expressing its numerator in \(t=m-2\) with coefficients all nonnegative or all nonpositive. The script also checks the exact table identities through integer-polynomial cross multiplication. This sign certificate is an explicit finite algebraic verification of an all-parameter identity, not finite sampling.

**Maximizing-orbit transitions.** Subtracting the exact formulas gives
\[
q_Y-q_X=\frac{2(m-1)}{mS_m}>0,\quad
q_Y-q_W=\frac{(m-1)(m+1)}{2m^2S_m}>0,\quad
q_Z-q_W=\frac{(m-1)(2m-3)}{2mS_m}>0.
\]
Consequently only \(Y\) and \(Z\) can maximize the cut norm. Their difference is
\[
q_Y-q_Z=-\frac{(m-1)(2m^2-4m-1)}{2m^2S_m},
\]
which is positive at \(m=2\) and negative at every integer \(m\ge3\).

Similarly,
\[
p_Y-p_X=\frac{7m-8}{2mS_m}>0,\qquad
p_Y-p_W=\frac{m^2-2}{2m^2S_m}>0.
\]
Therefore only \(Y\) and \(Z\) can maximize the cycle norm. Their difference is
\[
p_Y-p_Z=-\frac{(m-1)(2m^2-7m-2)}{2m^2S_m},
\]
positive at integer \(m=2,3\) and negative for all \(m\ge4\). These inequalities prove the stated maximizing edge classes and norm formulas with no omitted parameter values.

**Sign of the deletion response.** The intact formulas follow by directly summing the unpunctured Green kernel over the three edge classes. For \(m=2\), subtraction gives \(\|Q_{G_m}\|-\|Q_{H_m}\|=1/42\) and \(\|P_{G_m}\|-\|P_{H_m}\|=0\). For every \(m\ge3\),
\[
\|Q_{G_m}\|-\|Q_{H_m}\|=
\frac{6m^3-16m^2+9m-1}{6m^2S_m}>0.
\]
The numerator becomes \(6t^3+38t^2+75t+44\) on setting \(m=t+3\). At \(m=3\), the cycle-norm increase equals \(5/513\). For every \(m\ge4\),
\[
\|P_{G_m}\|-\|P_{H_m}\|=
\frac{(2m-1)(3m^2-11m+2)}{6m^2S_m}>0,
\]
since \(3m^2-11m+2=3t^2+13t+6\) with \(m=t+4\). The stated asymptotics follow by taking the leading terms in the two rational expressions.

## Verification

Execute `python verify_symbolic.py` for the all-parameter integer-polynomial sign, rank-one potential, orbit maximization, and deletion-comparison certificates. Execute `python check_projection.py` for an independent exact-rational reconstruction of grounded graph Laplacians and all surviving projector columns for \(m=2,3,4,5,6\), comparing both norms with the formulas. This second calculation checks 535 complete projector columns across intact and punctured graphs; it is finite corroboration and not an infinite proof. Both scripts are self-contained and use only the Python standard library.

## Relationship to prior work

The cycle-space and transportation-cost framework is developed in Dilworth, Kutzarova and Ostrovskii's 2018 and 2023 papers. The 2023 paper's central exact families are discrete tori and Hamming graphs, not edge-punctured balanced complete tripartite graphs. General Laplacian pseudoinverse updates are standard and are used here as a tool, not claimed new. Canonical endpoint norms for *intact* complete multipartite graphs are also treated as background, rather than a novelty claim. What is determined here is the complete **one-edge-deletion response** on the balanced tripartite family, its strict sign for all \(m\ge3\), and the two distinct sharp maximizing-orbit transitions. No claim is made that the general existence of edge-insertion nonmonotonicity is new.

## Limitations

The conclusions apply to real, unweighted complete balanced tripartite graphs with exactly one edge deleted between distinct parts, and to their **canonical orthogonal** projections. They do not determine unrestricted projection minima or cover unbalanced multipartite graphs, multiple deletions, arbitrary weights, or Banach-valued Lipschitz extensions. Search of accessible literature cannot rule out every equivalent specialized calculation.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first public version 2023-05-21. https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first public version 2018-07-10. https://arxiv.org/abs/1807.03814
