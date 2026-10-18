# A scale-invariant componentwise efficiency bound for disconnected exact α-potential games

## Finding

Consider the exact detailed-balance regime of Hu, Wang, Zhang, and Di's decentralized game, with independent player policies and dynamics, nonnegative constituent costs, and no interaction across distinct connected components. Assume the social optimum is positive. On each nontrivial interaction component \(S_k\), choose any positive detailed-balance vector \(q^{(k)}\), and put
\[
M_k=\max_{i\in S_k}q_i^{(k)},\qquad
m_k=\min_{\substack{i<j\text{ in }S_k\\ \lambda_{ij}+\lambda_{ji}>0}}
\frac{q_i^{(k)}q_j^{(k)}}{q_i^{(k)}+q_j^{(k)}},\qquad
B_k=\frac{M_k}{m_k}.
\]
For an isolated singleton component set \(B_k=1\), and define \(B_{\rm comp}=\max_k B_k\). Then every minimizer \(\phi^p\) of the exactly rescaled potential obeys
\[
\boxed{\operatorname{InEff}(\phi^p)\le B_{\rm comp}.}
\]
The complete minimizer set and each \(B_k\) are invariant under independent positive rescaling of detailed-balance weights on the components.

When at least one interacting edge exists, the stronger *interaction-restricted* coefficient certificate
\[
G_E(p)=\frac{\max_i p_i}{\displaystyle\min_{i<j:\,\lambda_{ij}+\lambda_{ji}>0}\frac{p_ip_j}{p_i+p_j}}
\]
satisfies the exact optimization formula
\[
\boxed{\inf_{c_k>0}G_E((c_kq_i^{(k)})_i)=B_{\rm comp},}
\]
where isolated singleton weights may also be freely scaled. In particular, the interaction-restricted certificate can be normalized without affecting selected policies. This is **not** a claim that \(B_{\rm comp}\) equals the optimal normalization of the *all-pair* expression displayed in Corollary 4.8 of the source.

## Assumptions and scope

This statement uses Assumption 2 (disjoint interaction components), Theorem 4.5's exact detailed balance, the source's playerwise policy decomposition, Proposition 4.7's nonnegativity conditions, and \(\mathrm{SC}_{\mathrm{opt}}>0\). It concerns the exact case \(r^\star=0\), not the approximate \(\alpha>0\) setting. Interacting edges are precisely pairs with \(\lambda_{ij}+\lambda_{ji}>0\). The function \(G_E\) is defined only when an interacting edge exists. If every vertex is isolated, the potential minimizes the social cost componentwise and the first bound gives \(\operatorname{InEff}=1=B_{\rm comp}\). These bounds are coefficient certificates, not assertions that the actual price of stability equals them.

## Proof

By Assumption 2, both the social cost and the exact rescaled potential split into sums indexed by connected interaction components. Because the policy class is the Cartesian product of playerwise policies and dynamics do not couple different components, the set of potential minimizers is the product of component minimizer sets. Multiplying every detailed-balance weight on one component by \(c_k>0\) multiplies its potential by \(c_k\) and leaves its argmin unchanged.

On a nontrivial component, every player-specific nonnegative cost term has potential-to-social coefficient ratio \(q_i^{(k)}\). Detailed balance gives \(q_i^{(k)}\lambda_{ij}=q_j^{(k)}\lambda_{ji}\); the ratio for a nonzero pair term is consequently
\[
\frac{q_i^{(k)}\lambda_{ij}}{\lambda_{ij}+\lambda_{ji}}
=\frac{q_i^{(k)}q_j^{(k)}}{q_i^{(k)}+q_j^{(k)}}.
\]
Since these pair ratios are at least \(m_k\) and strictly below the larger endpoint weight, \(m_k\le M_k\). Nonnegativity of all cost contributions yields, for every component policy \(\phi_k\),
\[
m_k\,\mathrm{SC}_k(\phi_k)\le\Phi_k(\phi_k)\le M_k\,\mathrm{SC}_k(\phi_k).
\]
At a component potential minimizer \(\phi_k^p\), compare with its social-cost minimizer \(\phi_k^*\) to obtain
\[
\mathrm{SC}_k(\phi_k^p)\le (M_k/m_k)\,\mathrm{SC}_k(\phi_k^*).
\]
For an isolated singleton, potential and social cost differ only by a positive scalar, so its selected policy minimizes social cost. Summing the component bounds and dividing by the positive optimum proves \(\operatorname{InEff}(\phi^p)\le B_{\rm comp}\). Both \(M_k\) and \(m_k\) scale by \(c_k\), proving invariance.

Every positive detailed-balance vector on a connected interaction component is unique up to a positive scalar, since edge balance fixes the ratio of weights at adjacent vertices. For any global rescaling, the global numerator in \(G_E\) is at least \(c_kM_k\), and its denominator is at most \(c_km_k\), so \(G_E\ge B_k\) for each nontrivial component. Also \(G_E\ge1\). Thus \(G_E\ge B_{\rm comp}\). Conversely choose \(c_k=1/M_k\) on every nontrivial component and choose positive singleton scales no larger than 1. The global numerator is then 1, and the minimum interacting-pair ratio is \(\min_k(m_k/M_k)=1/B_{\rm comp}\). This attains \(G_E=B_{\rm comp}\), proving the optimization formula.

## Boundary of the optimization assertion

The denominator in the source's printed Corollary 4.8 runs over **all distinct player pairs**, not only interacting pairs. Denote that expression by
\[
G_{\rm all}(p)=\frac{\max_i p_i}{\min_{i<j}p_ip_j/(p_i+p_j)}.
\]
It can satisfy \(\inf_cG_{\rm all}>B_{\rm comp}\). For example, take two disconnected two-player interaction components, each having balanced weights \((1,10)\) and positive edge coefficients satisfying detailed balance, such as \(\lambda_{12}=10\) and \(\lambda_{21}=1\) in each component. Then \(M_k=10\), \(m_k=10/11\), and \(B_{\rm comp}=11\). For arbitrary component scales \(c_1,c_2>0\), rescale globally so that \(\min(c_1,c_2)=1\) and \(\max(c_1,c_2)=t\ge1\). The maximum weight is \(10t\). The two weights of size \(1\) and \(t\) lie in distinct components and contribute an all-pair harmonic coefficient \(t/(1+t)\); hence \(G_{\rm all}\ge10(1+t)\ge20\). Equality occurs at \(t=1\), when the four weights are \((1,10,1,10)\), the minimum pair harmonic ratio is \(1/2\), and \(G_{\rm all}=20\). Thus
\[
\boxed{\inf_{c_1,c_2>0}G_{\rm all}=20>11=B_{\rm comp}.}
\]
This corrects an erroneous identification of the source's all-pair Corollary-4.8 expression with the interaction-restricted coefficient expression. It does not affect the intrinsic componentwise inefficiency bound or the valid optimization of \(G_E\).

A separate example with two disconnected symmetric components \(q^{(k)}=(1,1)\) has \(B_{\rm comp}=2\). Taking scales \(C\ge1\) and 1 gives \(G_{\rm all}=2C\), despite leaving all component potential minimizers unchanged; this illustrates the gauge artifact without claiming optimality of the all-pair expression.

## Verification and limitations

The coefficient-ratio identities, componentwise minimization, and sharp optimization of \(G_E\) are proved for arbitrary admissible positive weights; representative rational examples independently check normalization. The explicit two-component counterexample proves that the broader all-pair optimization assertion cannot be retained. The result does not cover signed cost terms, approximate \(\alpha>0\) games, cross-component interactions, or an equality between the coefficient bound and the actual price of stability.

## Relation to earlier results

Hu, Wang, Zhang, and Di, *Decentralized Decision-Making among Heterogeneous Autonomous Vehicles: An α-Potential Game Framework* (arXiv:2609.38731v1), give Assumption 2, the exact-balance criterion in Theorem 4.5, coefficient comparisons in Proposition 4.7, and an all-pair bound in Corollary 4.8. The present corrected claim applies the source's nonnegative coefficient comparison separately to disconnected components, identifies its invariant interaction-restricted optimum, and explicitly distinguishes this from the less sharp printed all-pair formula. Guo, Li, and Zhang's general 2025 α-potential theory gives a broader framework but does not, in the inspected material, state the source-specific component-normalization result. A more general decomposition result may exist; no absolute novelty assertion is made.
