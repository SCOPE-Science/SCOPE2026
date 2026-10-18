# Sharp endpoint Hodge projection norms on the three-rail infinite strip

## Finding

Let \(G=P_3\square\mathbb Z\) be the infinite, unweighted three-row square-lattice strip, with the two vertical edges in each column and three horizontal edges between successive columns. Choose any fixed orientation of its edge set \(E\). Let \(D:\ell_2(E;\mathbb R)\to\ell_2(V;\mathbb R)\) be the incidence operator and let \(Q\) be the Euclidean orthogonal projection onto \(\overline{\operatorname{ran}D^*}\). Its complement \(C=I-Q\) is the orthogonal projection onto \(\ker D\). Both extend uniquely to bounded real \(\ell_1(E)\) operators, with sharp norms
\[
\boxed{\|Q\|_{1\to1}=\frac73+\frac1{\sqrt5}-\frac1{\sqrt{21}}},\qquad
\boxed{\|C\|_{1\to1}=2+\frac2{\sqrt{21}}}.
\]
By symmetry of the matrices, these are also the \(\ell_\infty\) operator norms of their canonical adjoint extensions.

The formulas are attained by single-edge inputs, but by *different edge orbits*: for \(Q\), any outer horizontal edge; for \(C\), any vertical edge. Here is the complete absolute-column-sum table, with entries for \(Q\) and \(C\), respectively:

| Edge orbit | Cut projector \(Q\) | Cycle projector \(C\) |
| --- | --- | --- |
| Vertical edge | \(1+1/\sqrt5+5/\sqrt{21}\) | \(2+2/\sqrt{21}\) |
| Outer horizontal edge | \(7/3+1/\sqrt5-1/\sqrt{21}\) | \(4/3+2/\sqrt5\) |
| Middle horizontal edge | \(7/3\) | \(4/3+4/\sqrt{21}\) |

All identities are exact for the *infinite* strip. No global minimum over arbitrary nonorthogonal projections is claimed.

## Assumptions and scope

The vertex set is \(\{0,1,2\}\times\mathbb Z\). Edges of unit weight join vertices one grid step apart, without any periodic identification across rows. The \(\ell_2\) projections are defined using the ordinary counting-measure Euclidean inner products on edge and vertex spaces. The transverse path has three vertices and no diagonal edges. The edge-orbit table does not involve finite-strip boundary conditions; finite-strip computations serve only as independent checks.

The divergence \(D\), its adjoint \(D^*\), and \(Q\) are defined on real \(\ell_2\). Since the graph has uniformly bounded degree, \(D\) is bounded, and the closed subspaces in the finding are well-defined. The operator \(Q\) is projected onto the *closure* of the gradient space; we do not incorrectly assume that the unclosed gradient range is closed on an infinite graph. Edge orientations only conjugate these matrices by diagonal signs, leaving all stated norms unchanged.

## Proof

**1. Transverse spectral decomposition and Green function.** The row Laplacian for \(P_3\) has the orthonormal eigenvectors
\[
 u_0=(1,1,1)/\sqrt3,\quad
 u_1=(1,0,-1)/\sqrt2,\quad
 u_3=(1,-2,1)/\sqrt6,
\]
with respective eigenvalues \(0,1,3\). The longitudinal Laplacian acts on a sequence by \(2f(k)-f(k-1)-f(k+1)\). For \(\lambda\in\{1,3\}\), set
\[
 s_\lambda=\sqrt{\lambda(\lambda+4)},\quad
 q_\lambda=(\lambda+2-s_\lambda)/2,\quad
 g_\lambda(k)=\frac{q_\lambda^{|k|}}{s_\lambda}.
\]
Then \(0<q_3<q_1<1\), and \(g_\lambda\) is the unique decaying Green function for the massive longitudinal operator \(2+\lambda-S-S^{-1}\). Moreover,
\[
\sum_{k\in\mathbb Z}g_\lambda(k)=1/\lambda,\qquad
\sum_{k\ge0}(g_\lambda(k)-g_\lambda(k+1))=1/s_\lambda.
\]
Put \(d_\lambda=(1-q_\lambda)/s_\lambda=(1-\lambda/s_\lambda)/2\) and \(e_\lambda(r)=(1-q_\lambda)^2q_\lambda^r/s_\lambda\) for \(r\ge0\). Thus \(\sum_{r\ge0}e_\lambda(r)=d_\lambda\). The transverse zero mode has no contribution for an injected *vertical* edge. For an injected horizontal edge from column zero to one, its longitudinal gradient is zero except at that one bond, where the zero-mode gives the current \(1/3\) on each row. These statements follow by Fourier transforming the longitudinal variable in the orthogonal decomposition; the zero-mode's phase derivative cancels its sole massless pole. Consequently the formulas below compute the matrix columns of the genuine \(\ell_2\) orthogonal projection.

**2. Vertical source.** Inject a unit current from the middle row to an outer row in column zero. Apart from overall sign, the three row potentials at longitudinal coordinate \(k\) are
\[
\phi(k)=\bigl((g_1(k)+g_3(k))/2,\ -g_3(k),\ (-g_1(k)+g_3(k))/2\bigr).
\]
The two vertical currents are \((g_1+3g_3)/2\) and \((g_1-3g_3)/2\). The second is negative exactly at \(k=0\) and is positive when \(|k|\ge1\). Indeed \(g_1(0)<3g_3(0)\), \(g_1(1)>3g_3(1)\), and \(q_1>q_3\) propagates the latter inequality to every larger index; the two strict numerical inequalities follow directly from \(s_1=\sqrt5\), \(s_3=\sqrt{21}\). The total absolute vertical current is therefore \(1+3/s_3-1/s_1\).

The horizontal current magnitudes at any longitudinal edge are determined by \(\lvert\Delta g_1\rvert\) and \(\lvert\Delta g_3\rvert\). Since \(d_1>d_3\) and \(q_1>q_3\), one has \(\lvert\Delta g_1\rvert>\lvert\Delta g_3\rvert\). Summing the three row magnitudes and then the two halves of the line gives total absolute horizontal current \(2/s_1+2/s_3\). Hence
\[
 \|Qe_{\mathrm v}\|_1=1+1/s_1+5/s_3.
\]
The source-edge diagonal coefficient is \(Q_{ee}=1/(2s_1)+3/(2s_3)\). Because \(C=I-Q\), for any source edge \(e\) the exact identity \(\|Ce\|_1=1+\|Qe\|_1-2Q_{ee}\) applies (the source diagonal is positive). This gives \(\|Ce_{\mathrm v}\|_1=2+2/s_3\).

**3. Outer horizontal source.** Let \(h_\lambda(k)=g_\lambda(k)-g_\lambda(k-1)\). For a horizontal source in the upper row, the nonzero transverse-mode potential is
\[
 \phi(k)=\bigl(h_1(k)/2+h_3(k)/6,\ -h_3(k)/3,\ -h_1(k)/2+h_3(k)/6\bigr).
\]
The sum of absolute vertical currents is \(2/s_1\), since \(\lvert h_1(k)\rvert>\lvert h_3(k)\rvert\) for every integer \(k\). On the source horizontal bond, the zero mode adds \(1/3\) to every row current, and all three resulting currents are nonnegative; their sum is exactly one. On every horizontal bond away from the source, the three row current magnitudes sum to \(e_1(r)+e_3(r)/3\), where \(r\ge0\) denotes distance from the source on either side. Hence their sum is \(2d_1+2d_3/3\). Combining contributions yields
\[
 \|Qe_{\mathrm{out}}\|_1=1+2/s_1+2d_1+2d_3/3
 =\frac73+1/s_1-1/s_3.
\]
At the source bond, \(Q_{ee}=1-1/(2s_1)-1/(2s_3)\), which gives \(\|Ce_{\mathrm{out}}\|_1=4/3+2/s_1\).

**4. Middle horizontal source.** Here only the transverse eigenvalue-three mode survives, with potential \((-h_3(k)/3,2h_3(k)/3,-h_3(k)/3)\). The absolute vertical currents sum to \(4/s_3\); the horizontal currents across the source bond sum to one, and the remaining longitudinal bonds contribute \(8d_3/3\). Therefore
\[
 \|Qe_{\mathrm{mid}}\|_1=1+4/s_3+8d_3/3=7/3.
\]
Since \(Q_{ee}=1-2/s_3\), we obtain \(\|Ce_{\mathrm{mid}}\|_1=4/3+4/s_3\).

**5. Norms and sharpness.** Every edge lies in exactly one of the three orbits above, up to graph translations/reflections and orientation. The column formulas are absolutely summable, uniformly over all edge locations, so \(Q\) and \(C\), initially restricted to finitely supported edge inputs, extend as bounded operators on \(\ell_1(E)\). They agree with the \(\ell_2\) orthogonal projections on the common dense domain, and the identities \(Q^2=Q\), \(C^2=C\), and \(QC=0\) persist by density. The \(\ell_1\) operator norm is the supremum of the \(\ell_1\) norms of coordinate columns, and it is attained by the corresponding coordinate unit vector. In fact
\[
 \|Qe_{\mathrm{out}}\|_1-\|Qe_{\mathrm v}\|_1
 =\frac43-\frac6{\sqrt{21}}>0,
\]
while \(\|Qe_{\mathrm v}\|_1>\|Qe_{\mathrm{mid}}\|_1\). For the cycle projection, \(2+2/\sqrt{21}\) exceeds each horizontal-orbit entry; the inequalities follow, for example, from \(\sqrt5>2\) and \(\sqrt{21}<5\) together with the exact formulas. The matrices are symmetric on \(\ell_2\) and have uniformly summable rows as well as columns, so the adjoint \(\ell_\infty\) extensions have the same operator norms. This proves the theorem.

## Verification

The standalone standard-library program `verify_strip3.py` independently evaluates the exponentially convergent Green-kernel columns, compares all six results with the displayed radical formulas, and solves exact-rational grounded finite-strip Laplacian systems at lengths eleven and fifteen. The latter are independent approximations to the infinite-strip values, not proofs of the limits. A complete execution prints `VERIFY_OK`. The infinite all-edge statement is proved by the preceding spectral argument; the finite computations are additional diagnostic evidence only.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii establish a general setting for cycle subspaces and orthogonal/invariant projections in transportation-cost Banach spaces, including finite Hamming and torus examples; their projection results motivate examination of an infinite quasi-one-dimensional strip. Klenke studies random spanning trees on ladder-like graphs and the transfer-current context. A published finite-volume rung-kernel calculation for the two-row weighted ladder explicitly recovers the two-row Green-function boundary/bulk structure. These results provide related operators or methods, but neither the two-row kernel nor the inspected general projection statements imply the displayed three-orbit \(\ell_1\) norms of both complementary projectors for \(P_3\square\mathbb Z\), or the fact that the two worst-case edge orbits differ. This is a comparison of inspected statements, not a claim that literature search proves uniqueness.

## Limitations

Only the canonical *orthogonal* projection and its complement are evaluated; the theorem does not assert that either minimizes norm over all bounded projections onto the same subspace. Results are for the unit-weight, open-transverse three-row strip on real edge spaces, not for arbitrary strip widths, periodic row boundary conditions, or arbitrary edge weights. Potential equivalences in the extensive electrical-network and graph Riesz-transform literature remain a residual bibliographic risk. Self-review is not independent validation.

## References

1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, “Cycle Spaces: Invariant Projections and Applications to Transportation Cost,” arXiv:2305.12582 (first posted 21 May 2023), primary MSC 46B04.
2. A. Klenke, “The Random Spanning Tree on Ladder-like Graphs,” arXiv:1704.00182 (2017).
3. “Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees,” mathematical result and proof (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-volume-rung-kernel-and-boundary-bulk-split-for-weig--647fc3f7ee8c .
