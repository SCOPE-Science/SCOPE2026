# A sharp two-edge safety window for opinion depolarization

## Finding

For a fixed undirected weighted social network with Laplacian \(L\), let a proposed simultaneous strengthening of its links be represented by another Laplacian \(B\succeq0\). With \(H=I+L\), the expressed Friedkin–Johnsen opinions under intervention intensity \(t\geq0\) are
\[
z_t=(H+tB)^{-1}s,\qquad P_s(t)=\|z_t\|_2^2,
\]
for any mean-centered innate opinions \(s\perp\mathbf 1\). The intervention is guaranteed never to increase polarization at any intensity for **every** such \(s\) if and only if the anticommutator
\[
\boxed{HB+BH\succeq0\quad\text{on }\mathbf{1}^\perp.}
\]

For the three-vertex path with existing positive link weights \(a\) on \(1\!\! -\!\!2\) and \(b\) on \(2\!\! -\!\!3\), simultaneously increase those weights by \(tu\) and \(tv\), where \(u,v>0\). Put
\[
K=14ab+8a+8b+4,\qquad
\rho_\pm=\frac{K\pm\sqrt{K^2-4a^2b^2}}{2b^2}.
\]
Then the following classification is exact:
\[
\boxed{\text{Polarization is nonincreasing for every centered }s\text{ and all }t\geq0
\ \Longleftrightarrow\ \rho_-\leq u/v\leq\rho_+.}
\]
Inside this closed interval, polarization is in fact strictly decreasing for every nonzero centered \(s\) as \(t\) increases from any positive intensity, and \(P_s(t)<P_s(0)\) for all \(t>0\). Outside it, some centered innate opinion profile has \(P_s'(0)>0\), hence polarization initially increases. Strengthening either path edge **alone** is never universally safe: for each individual edge there are centered profiles that initially polarize further. Consequently, two individually risky updates can jointly produce guaranteed depolarization at all intensities.

The first nontrivial example has existing weights \((a,b)=(1,2)\) and equal increases \((u,v)=(1,1)\). Its universal-safety interval is \([7-\sqrt{195}/2,\,7+\sqrt{195}/2]\). Both isolated edge updates admit profiles with increasing polarization, although their equal joint update decreases it for every nonunanimous profile and at every positive intensity. An unbalanced joint increase \((u,v)=(15,1)\) instead permits increasing polarization.

## Assumptions and scope

A weighted undirected graph has finitely many vertices, symmetric nonnegative link weights, and its ordinary combinatorial Laplacian satisfies \(L\mathbf 1=0\). The intervention \(B\) is another finite nonnegative-weight graph Laplacian on the same vertices. We fix innate opinions \(s\) throughout the intervention, assume \(\mathbf{1}^{\mathsf T}s=0\), and use the standard Friedkin–Johnsen equilibrium rule \(z_t=(I+L+tB)^{-1}s\). The polarization measure is the **expressed-opinion variance sum** \(P_s(t)=\sum_i(z_t)_i^2\), not polarization plus edge disagreement and not the spectral-gap-based maximum obtained by allowing the innate profile to change after every intervention. The general criterion holds on any finite graph, including disconnected networks. The sharp two-edge specialization assumes exactly the weighted path on three labeled vertices, \(a,b,u,v>0\), with no direct \(1\!\!-\!\!3\) edge. The parameter \(t\geq0\) is an intervention weight, not opinion-evolution time.

## Proof

**1. An exact matrix-order characterization.** Write \(A_t=H+tB\). The matrix \(A_t\) is symmetric positive definite for every \(t\geq0\), and \(A_t\mathbf{1}=\mathbf{1}\). Differentiating the inverse gives \((A_t^{-1})'=-A_t^{-1}BA_t^{-1}\), and therefore
\[
\begin{split}
P_s'(t)&=-s^{\mathsf T}\bigl(A_t^{-1}BA_t^{-2}+A_t^{-2}BA_t^{-1}\bigr)s\\
&=-y_t^{\mathsf T}(A_tB+BA_t)y_t,
\qquad y_t=A_t^{-2}s.
\end{split}
\]
The map \(s\mapsto y_t\) is a bijection of \(\mathbf{1}^\perp\), since \(A_t\) preserves that subspace and is invertible there. Also
\[
A_tB+BA_t=HB+BH+2tB^2.
\]
If \(HB+BH\) is positive semidefinite on \(\mathbf{1}^\perp\), then so is the right-hand side for every \(t\geq0\), proving \(P_s'(t)\leq0\) for every centered \(s\). Conversely, if this is not positive semidefinite, choose \(y\perp\mathbf{1}\) with \(y^{\mathsf T}(HB+BH)y<0\), set \(s=H^2y\), and obtain \(P_s'(0)>0\). Differentiability then gives \(P_s(t)>P_s(0)\) for all sufficiently small \(t>0\). Because the inequality is quadratic in \(s\), such a witness can be rescaled to any prescribed nonzero bound on the maximum absolute innate opinion. This proves necessity and sufficiency, with every quantifier explicit.

**2. Reduce the two-edge path to one quadratic inequality.** Set
\[
E_{12}=\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&0\end{pmatrix},\quad
E_{23}=\begin{pmatrix}0&0&0\\0&1&-1\\0&-1&1\end{pmatrix},
\]
so \(H=I+aE_{12}+bE_{23}\) and \(B=uE_{12}+vE_{23}\). Let \(Q=HB+BH\). Direct multiplication, or expansion in the two edge Laplacians, yields
\[
\operatorname{tr}Q=2\bigl[(4a+b+2)u+(a+4b+2)v\bigr]>0
\]
and the sum of its three principal \(2\times2\) minors is
\[
\sigma_2(Q)=3\left[(14ab+8a+8b+4)uv-b^2u^2-a^2v^2\right].
\]
Because \(Q\mathbf{1}=0\), its eigenvalues are \(0,\lambda_1,\lambda_2\) and \(\lambda_1+\lambda_2=\operatorname{tr}Q>0\), while \(\lambda_1\lambda_2=\sigma_2(Q)\). Thus \(Q\) is positive semidefinite on \(\mathbf{1}^\perp\) exactly when \(\sigma_2(Q)\geq0\). Dividing by \(3v^2>0\), this is
\[
b^2(u/v)^2-K(u/v)+a^2\leq0,
\]
whose roots are \(\rho_-\) and \(\rho_+\). They are distinct and strictly positive since \(K>2ab>0\). The general criterion therefore proves the full closed safety interval and its sharp failure outside.

**3. Strictness and individually unsafe edges.** For \(u,v>0\), the update \(B\) is the Laplacian of a connected weighted three-path and is positive definite on \(\mathbf{1}^\perp\). Hence, if the safety inequality holds, then \(Q+2tB^2\) is positive definite on \(\mathbf{1}^\perp\) for every \(t>0\). This gives \(P_s'(t)<0\) for every nonzero centered \(s\) and \(t>0\), including the two sharp interval endpoints. Continuity at \(t=0\) and integration show \(P_s(t)<P_s(0)\) for every \(t>0\).

If only the first edge is strengthened, \(v=0\), then \(\sigma_2(Q)=-3b^2u^2<0\). If only the second is strengthened, \(u=0\), then \(\sigma_2(Q)=-3a^2v^2<0\). Since \(\operatorname{tr}Q>0\) in each case, \(Q\) has a negative eigenvalue on \(\mathbf{1}^\perp\). The first step of the proof supplies the required adverse innate profiles.

**4. Rational witnesses and an exact safety window.** For \((a,b)=(1,2)\), \(K=56\), giving
\[
\rho_\pm=7\pm\frac{\sqrt{195}}2.
\]
Thus \((u,v)=(1,1)\) lies strictly inside the safe interval, whereas \((15,1)\) lies outside. For either the first-edge-only intervention \((1,0)\) or the unbalanced joint intervention \((15,1)\), the centered innate profile \(s=(0,-1,1)^{\mathsf T}\) has the exact initial derivative
\[
P_s'(0)=\frac{10}{2197}>0.
\]
For the second-edge-only intervention \((0,1)\), the centered profile \(s=(-1,1,0)^{\mathsf T}\) has the same derivative. Both examples use innate values in \([-1,1]\). The equal joint intervention \((1,1)\) has \(\sigma_2(Q)=153>0\) and reduces the polarization of **every** nonzero centered profile at every positive intensity. This establishes the claimed two-edge synergy using strict, exact inequalities.

## Verification

The accompanying standalone Python 3 program `verify.py` uses SymPy rational and symbolic arithmetic. It reconstructs the edge matrices and the anticommutator, checks the trace and principal-minor polynomial identically, differentiates the resolvent identity symbolically, and checks the three rational adverse profiles and their exact slopes. It also performs 96 exact-rational finite profile tests in the safe case. Run `python verify.py` with SymPy installed. The symbolically verified identities and the analytical sign/eigenvalue argument establish the infinite theorem; the finite profile tests are auxiliary reproducibility checks, not a substitute for proof.

## Relationship to prior work

Rácz and Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks* (first arXiv posting June 17, 2022), analyze the same expressed-polarization quadratic functional, give an exact **single-edge** update formula in Lemma 4.3 and Proposition 4.5, and discuss cases where adding just one edge can raise polarization. Their Section 6 explicitly identifies characterization of more substantial graph perturbations as open. The present result instead treats a simultaneously strengthened Laplacian direction, proves a uniform-in-opinions **if and only if** criterion, and completely solves the smallest connected two-edge support, including the boundary and the counterintuitive jointly-safe/individually-unsafe regime.

Bhalla, Lechowicz, and Musco, *Local Edge Dynamics and Opinion Polarization* (first posted November 28, 2021), define the same expressed polarization but derive update bounds particularly for polarization **plus disagreement** and single-edge operations, not a universally quantified multi-edge sign classification. Zhou, Neumann, Garimella, and Gionis, *Modeling the Impact of Timeline Algorithms on Opinion Dynamics Using Low-rank Updates* (first posted February 15, 2024), model grouped interventions but optimize the combined polarization–disagreement objective; that inverse-first-power objective is Loewner monotone under every positive-semidefinite increment and does not imply the inverse-square result proved here. Zhu, Bao, and Zhang's 2021 link-recommendation theorem likewise concerns the combined objective, not the individual polarization sign. Our all-profile pointwise criterion also differs from a monotonicity statement about a worst-case polarization **maximum**, which allows the maximizing innate profile to change with the graph.

## Limitations

The classification is for the linear undirected Friedkin–Johnsen equilibrium model with fixed innate opinions, symmetric weighted edges, and a fixed relative strength ratio during the two-edge intervention. It does not assert an analogous guarantee for signed, directed, time-dependent, or state-dependent influence, nor for interventions that vary \(u/v\) with \(t\). The general anticommutator criterion gives a finite matrix semidefiniteness test, not a closed-form classification for arbitrary large graph topologies. The literature comparison did not establish exhaustive novelty against every potentially unindexed treatment of multi-edge matrix-monotonicity; independent mathematical audit and broader specialist searching remain appropriate.

## References

1. M. Z. Rácz and D. E. Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks*, arXiv:2206.08996, first public June 17, 2022. Sections 4.2, 4.3, 6, and Appendix A. https://arxiv.org/abs/2206.08996
2. N. Bhalla, A. Lechowicz, and C. Musco, *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020, first public November 28, 2021. Sections 2.3–3.2. https://arxiv.org/abs/2111.14020
3. T. Zhou, S. Neumann, K. Garimella, and A. Gionis, *Modeling the Impact of Timeline Algorithms on Opinion Dynamics Using Low-rank Updates*, arXiv:2402.10053, first public February 15, 2024. Sections 2, 4, 5 and appendices. https://arxiv.org/abs/2402.10053
4. L. Zhu, Q. Bao, and Z. Zhang, *Minimizing Polarization and Disagreement in Social Networks via Link Recommendation*, NeurIPS 34 (2021), pp. 2072–2084. https://proceedings.neurips.cc/paper/2021/hash/101951fe7ebe7bd8c77d14f75746b4bc-Abstract.html
