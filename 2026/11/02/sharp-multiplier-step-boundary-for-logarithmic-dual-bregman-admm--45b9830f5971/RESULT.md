# Sharp multiplier-step boundary for logarithmic-dual Bregman ADMM on additive-cost transport

## Finding
For the logarithmic-dual-update entropy Bregman alternating-direction method for discrete optimal transport, the multiplier interval \(0<s<2\) is **exactly sharp** even on strictly positive, feasible product initializations, with zero initial multiplier and arbitrarily large fixed penalty. The boundary is witnessed by every nonconstant column-additive cost \(C_{ij}=c_j\), on any rectangular grid with at least two rows and columns.

In this class, the method has a closed-form full trajectory. For every integer \(k\geq1\),
\[
Y^{k}=ab^{\mathsf T},\qquad
X^k_{ij}=a_i w_j^{(k)},\qquad
w_j^{(k)}=\frac{b_j\exp[-c_j(1-s)^{k-1}/\rho]}{\sum_{\ell=1}^{n}b_{\ell}\exp[-c_{\ell}(1-s)^{k-1}/\rho]}.
\]
The exact multiplier contrasts are
\[
Z^k_{ij}-Z^k_{i\ell}=-(c_j-c_\ell)\bigl[1-(1-s)^{k-1}\bigr]\quad(k\ge1).
\]
For \(0<s<2\), the full primal-dual sequence converges, with exact asymptotic primal rate \(|1-s|\) when \(s\ne1\). At \(s=1\), the two primal matrices coincide with the balanced product by the second \(X\)-iterate. At \(s=2\), \(X\) alternates between two distinct strictly positive matrices and cannot converge. For every \(s>2\), the even and odd subsequences of \(X\) tend to distinct boundary product distributions supported on the maximum-cost and minimum-cost columns, respectively; dual contrasts are unbounded. The column normalization \(Y^k\) is the same feasible and optimal coupling at every iteration, despite the failure of \(X^k\) when \(s\ge2\).

## Assumptions and scope
Let integers \(m,n\ge2\) and let \(a\in\mathbb R_{>0}^m\), \(b\in\mathbb R_{>0}^n\) each sum to one. Choose a vector \(c\in\mathbb R^n\) with at least two distinct entries; nonnegative or strictly positive entries are allowed. Let \(C_{ij}=c_j\), choose any \(\rho>0\), any \(s>0\), and initialize \(X^0=ab^{\mathsf T}\), \(Z^0=0\).

Define \(\mathcal C_b(W)_{ij}=W_{ij}b_j/\sum_h W_{hj}\) and \(\mathcal R_a(W)_{ij}=W_{ij}a_i/\sum_\ell W_{i\ell}\) for strictly positive matrices. Consider precisely the three-update numerical method
\[
Y^{k+1}=\mathcal C_b(X^k\odot e^{Z^k/\rho}),\qquad
Z^{k+1}=Z^k+s\rho(\log X^k-\log Y^{k+1}),
\]
\[
X^{k+1}=\mathcal R_a\bigl(Y^{k+1}\odot e^{-(C+Z^{k+1})/\rho}\bigr).
\]
Exponentials, logarithms, and products in these displays are entrywise. This is Algorithm 1, equations (2.13a–c), in the motivating paper; it is not ordinary overrelaxed Sinkhorn balancing. The transport objective \(\langle C,P\rangle=\sum_j b_jc_j\) is constant across the entire feasible polytope, so all feasible couplings are optimal. This degeneracy is deliberate: it isolates the multiplier-step instability from any need to resolve a difficult transport optimum.

## Proof
First, \(Y^1=\mathcal C_b(ab^{\mathsf T})=ab^{\mathsf T}\) and \(Z^1=0\); the row normalization then yields
\[
X^1_{ij}=a_i\frac{b_je^{-c_j/\rho}}{\sum_\ell b_\ell e^{-c_\ell/\rho}}.
\]
Suppose \(X^k_{ij}=a_iw_j^{(k)}\) and \(Z^k_{ij}=z_j^{(k)}\), with the latter independent of the row. Column normalization cancels each multiplier \(e^{z_j^{(k)}/\rho}\), and the factor \(w_j^{(k)}\), so \(Y^{k+1}=ab^{\mathsf T}\) exactly. The dual update is columnwise:
\[
z_j^{(k+1)}=z_j^{(k)}+s\rho\log(w_j^{(k)}/b_j).
\]
If \(\delta_k=(1-s)^{k-1}\), the asserted softmax formula gives, for every two columns \(j,\ell\),
\[
\log\frac{w_j^{(k)}/b_j}{w_\ell^{(k)}/b_\ell}=-\frac{(c_j-c_\ell)\delta_k}{\rho}.
\]
Thus the dual contrast obeys the scalar recurrence
\[
z_j^{(k+1)}-z_\ell^{(k+1)}=z_j^{(k)}-z_\ell^{(k)}-s(c_j-c_\ell)\delta_k.
\]
Since all initial contrasts vanish, summing the finite geometric progression gives the announced exact contrast formula for every \(k\ge1\). The subsequent row normalization, using \(Y^{k+1}=ab^{\mathsf T}\), gives
\[
w_j^{(k+1)}\ \propto\ b_j\exp[-(c_j+z_j^{(k+1)})/\rho].
\]
The effective differences of \(c+z^{(k+1)}\) are \((c_j-c_\ell)(1-s)^k\), proving the softmax expression by induction. All normalizers are positive for each finite integer \(k\), with no numerical assumptions.

For \(0<s<2\), \(\delta_k\to0\). The softmax tends to \(b\) and the contrast vector tends to \(-c\) up to a common gauge. The row-independent common gauge itself converges: choose a reference column and use the dual increment \(s\rho\log(w_j^{(k)}/b_j)=O(|1-s|^{k-1})\), which is summable. A Taylor expansion at \(\delta=0\) gives
\[
w_j(\delta)-b_j=-\frac{b_j(c_j-\overline c)}{\rho}\delta+O(\delta^2),\qquad \overline c=\sum_\ell b_\ell c_\ell.
\]
The leading vector is nonzero because \(c\) is nonconstant, so the geometric factor \(|1-s|\) is sharp when \(s\ne1\). If \(s=1\), \(\delta_k=0\) for all \(k\ge2\), giving finite exact primal termination.

If \(s=2\), \(\delta_k=(-1)^{k-1}\), so the two distinct softmax vectors for \(\delta=1\) and \(\delta=-1\) alternate; they are different because \(c\) is nonconstant and \(\rho\) is finite. If \(s>2\), \(\delta_k\) alternates sign with magnitude tending to infinity. For \(\delta_k\to+\infty\), the softmax concentrates on \(\arg\min c\), with weights proportional to \(b_j\) among tied minimizers; for \(\delta_k\to-\infty\), it concentrates on \(\arg\max c\), with the same tie rule. The two support sets are disjoint. The multiplier contrast formula grows without bound whenever \(c_j\ne c_\ell\). This completes the exhaustive step-size classification for the stated family.

## Verification
A standalone Python standard-library verifier (`verify.py`) independently implements the three matrix recurrences and checks the closed-form trajectory, including nonuniform marginals, several cost vectors, all three regimes, and the precise dual contrasts. It also checks algebraic normalization identities and the distinct endpoint limits. These finite checks support, but do not replace, the induction and asymptotic argument above. Run with `python3 verify.py`.

## Relationship to prior work
Hou and Toh's 2026 paper introduces the exact entropy-BADMM updates above and proves global linear convergence of the primal-dual sequence for every \(s\in(0,2)\), provided the fixed penalty is sufficiently large and initialization is strictly positive feasible with zero multiplier. Its stated theorem does not prove failure at \(s\ge2\). The present result proves that extending the **universal** step interval beyond two is impossible even for any fixed positive penalty and a constant-on-feasible-set transport objective. The paper's Proposition 2.4(ii), expressing the multiplier through column-marginal logarithms, is acknowledged as prior groundwork; the exact full closed-form trajectory and sharp endpoint obstruction are the additional assertion.

Earlier work on overrelaxed Sinkhorn and matrix balancing studies a different iterative map, and its step-size boundary does not by itself imply this BADMM orbit classification. Classical linear-relaxation spectral arguments supply analogies, not the full nonlinear positive-matrix trajectory. Priority remains subject to an independent full historical review.

## Limitations
The example's cost depends only on the destination column, so the transport objective does not distinguish feasible couplings. The result is a **universal impossibility certificate** for \(s\ge2\), not a claim that every nonadditive cost diverges there. It does not establish finite-precision behavior, computational optimality, or a necessary penalty condition for general costs. The dual multiplier has an additive-column gauge and the proof controls gauge-invariant contrasts; for \(0<s<2\) the full dual matrix also converges by summability. An independent audit of originality and mathematical correctness has not been performed.

## References
1. D. Hou and K.-C. Toh, *A Logarithmic-dual-update Bregman ADMM for Optimal Transport*, arXiv:2610.08087v1, first posted October 6, 2026. https://arxiv.org/abs/2610.08087. Relevant: Algorithm 1, Proposition 2.4, Theorem 3.1.
2. A. Thibault, L. Chizat, C. Dossal, and N. Papadakis, *Overrelaxed Sinkhorn-Knopp Algorithm for Regularized Optimal Transport*, arXiv:1711.01851, first posted November 6, 2017. https://arxiv.org/abs/1711.01851. A comparator involving a different relaxed scaling update.
