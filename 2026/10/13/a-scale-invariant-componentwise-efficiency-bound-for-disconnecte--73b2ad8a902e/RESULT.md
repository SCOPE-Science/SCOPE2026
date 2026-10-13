# A scale-invariant componentwise efficiency bound for disconnected exact α-potential games
## Finding
Consider the exact-rescaling case of Hu, Wang, Zhang and Di, in which positive weights satisfy \(p_i\lambda_{ij}=p_j\lambda_{ji}\) on every interacting pair. Their Assumption 2 explicitly allows disconnected interaction components. In that setting the detailed-balance vector on each nontrivial component is determined only up to a positive scalar, and that scalar is a gauge: it does not change the minimizers of the exact potential on that component.

For a nontrivial component \(S_k\), choose any positive detailed-balance vector \(q^{(k)}\) and define
\[
M_k=\max_{i\in S_k}q_i^{(k)},\qquad
m_k=\min_{\{i,j\}\subset S_k:\lambda_{ij}+\lambda_{ji}>0}
\frac{q_i^{(k)}q_j^{(k)}}{q_i^{(k)}+q_j^{(k)}},\qquad
B_k=\frac{M_k}{m_k}.
\]
Assign \(B_k=1\) to an isolated singleton component. Then every global minimizer \(\phi^p\) of an exact rescaled potential satisfies
\[
\operatorname{InEff}(\phi^p)\le B_{\mathrm{comp}}:=\max_k B_k.
\]
Each \(B_k\), and hence \(B_{\mathrm{comp}}\), is unchanged if all detailed-balance weights in component \(S_k\) are multiplied by an arbitrary positive scalar.

More strongly, \(B_{\mathrm{comp}}\) is exactly the minimum, over all such componentwise rescalings, of the first coefficient-comparison expression in Corollary 4.8. Consequently the unnormalized global expression can be a gauge artifact. With two disconnected symmetric two-player components and base weights \(q=(1,1)\) on each, \(B_{\mathrm{comp}}=2\). Scaling the first component by \(C\ge1\) and leaving the second fixed does not change the potential minimizer set, but the global Corollary-4.8 coefficient expression becomes \(2C\).

## Assumptions and scope
The statement uses the source model's decentralized product policy class and independent player state dynamics, Assumption 2 (no interaction edges between distinct components), the exact detailed-balance condition of Theorem 4.5, the nonnegativity hypotheses of Proposition 4.7, and \(\mathrm{SC}_{\mathrm{opt}}>0\). The claim concerns the exact regime \(r^\star=0\), not the approximate \(\alpha>0\) regime.

A nontrivial component means a component containing at least one interacting pair. An isolated singleton has no pair term, so its potential is a positive scalar multiple of its social component and its selected minimizer is socially optimal within that component.

## Proof
Because there are no cross-component interaction coefficients and each admissible policy is assembled from playerwise policies, both the social cost and the exact rescaled potential split as sums over the components. Multiplying every detailed-balance weight in one component by \(c_k>0\) multiplies only that component's potential by \(c_k\). Positive multiplication does not change its minimizer set, and the product structure therefore makes the global minimizer set independent of the component-scale choices.

For a nontrivial component \(S_k\), write its potential in the coefficient form of equations (4.12)--(4.13). A player-specific term \(C_i\) has potential/social coefficient ratio \(q_i^{(k)}\). For an interacting pair, detailed balance gives
\[
q_i^{(k)}\lambda_{ij}=q_j^{(k)}\lambda_{ji}=:w_{ij},
\]
so the potential/social ratio of the pair term is
\[
\frac{w_{ij}}{\lambda_{ij}+\lambda_{ji}}
=\frac{q_i^{(k)}q_j^{(k)}}{q_i^{(k)}+q_j^{(k)}}.
\]
Because every cost component is nonnegative, all coefficient ratios in component \(S_k\) lie between \(m_k\) and \(M_k\). Thus, for every admissible component policy \(\phi_k\),
\[
m_k\,\mathrm{SC}_k(\phi_k)\le \Phi_k(\phi_k)\le M_k\,\mathrm{SC}_k(\phi_k).
\]
If \(\phi_k^p\) minimizes \(\Phi_k\) and \(\phi_k^{\mathrm{opt}}\) minimizes the component social cost, then
\[
\mathrm{SC}_k(\phi_k^p)
\le \frac{1}{m_k}\Phi_k(\phi_k^p)
\le \frac{1}{m_k}\Phi_k(\phi_k^{\mathrm{opt}})
\le \frac{M_k}{m_k}\mathrm{SC}_k(\phi_k^{\mathrm{opt}}).
\]
Summing over components and bounding each factor by \(B_{\mathrm{comp}}\) gives the claimed global inefficiency bound. The isolated-singleton case contributes factor \(1\).

Both \(M_k\) and \(m_k\) are multiplied by \(c_k\) under component scaling, so \(B_k\) is scale invariant. It remains to identify the best normalization of the source's global first coefficient bound. Every positive detailed-balance solution has the form \(p_i=c_k q_i^{(k)}\) on \(S_k\), because detailed-balance edge ratios determine the positive vector on each connected support component up to one scalar. For any such scales,
\[
G(c)=\frac{\max_i p_i}{\min_{\lambda_{ij}+\lambda_{ji}>0} p_i p_j/(p_i+p_j)}
\ge \frac{c_kM_k}{c_km_k}=B_k
\]
for every nontrivial component, hence \(G(c)\ge B_{\mathrm{comp}}\). Conversely choose \(c_k=1/M_k\) on each nontrivial component, and choose isolated-component scales no larger than \(1/M_k\) in the numerator normalization. Then the global numerator is \(1\), while the global pair denominator is \(\min_k m_k/M_k=1/B_{\mathrm{comp}}\). Therefore \(G(c)=B_{\mathrm{comp}}\), proving exact optimality of the normalization.

For two disconnected symmetric two-player components with base weights \(q=(1,1)\), each has \(M=1\), \(m=1/2\), and \(B=2\). Scaling one component by \(C\ge1\) gives global numerator \(C\) and global pair denominator \(1/2\), so the source expression is \(2C\) although the component minimizers are unchanged.

## Verification
The proof uses only the source's coefficient decompositions and exact detailed-balance relation. The bundled `verify.py` checks the scale invariance of \(M_k/m_k\), the two-component gauge example, and the optimizing normalization on several explicit component vectors. It is supplementary to the symbolic proof rather than a finite substitute for it.

## Relationship to prior work
Hu, Wang, Zhang and Di explicitly allow disconnected interaction groups in Assumption 2, characterize exact rescaling by detailed balance/Kolmogorov cycle balance in Theorem 4.5, and derive a global coefficient-comparison social-efficiency bound in Proposition 4.7 and Corollary 4.8. Their displayed exact-regime bound uses global extrema of the rescaling vector and does not isolate the component-scale gauge. The result here applies their coefficient comparison componentwise, proves that the resulting certificate is invariant under that gauge, and identifies it as the exact optimum of the Corollary-4.8 coefficient expression over all component scalings.

The earlier general \(\alpha\)-potential framework of Guo, Li and Zhang develops approximate-potential dynamic games but does not supply this disconnected-component normalization of the source-specific social-efficiency certificate. Searches of the published-finding corpus record for the source title, detailed balance, component rescaling, social efficiency, and equivalent formulations returned no statement implying this componentwise bound.

## Limitations
This does not claim that \(B_{\mathrm{comp}}\) is the exact price of stability or the sharp actual inefficiency of the model; it is the exact best value obtainable from the source's first coefficient-comparison bound under the component-scale freedom. The result does not address \(r^\star>0\), graphs with cross-component interactions, signed cost components, or settings outside the source's decentralized product-policy structure. No independent audit has been performed.

## References
1. A. Hu, Z. Wang, Y. Zhang, and X. Di, “Decentralized Decision-Making among Heterogeneous Autonomous Vehicles: An \(\alpha\)-Potential Game Framework,” arXiv:2609.38731v1, 2026. See Assumption 2, Theorem 4.5, Proposition 4.7, and Corollary 4.8. https://arxiv.org/abs/2609.38731v1
2. X. Guo, X. Li, and Y. Zhang, “An \(\alpha\)-Potential Game Framework for \(N\)-Player Dynamic Games,” SIAM Journal on Control and Optimization 63(4), 2964–3005, 2025. https://doi.org/10.1137/24M1707316
