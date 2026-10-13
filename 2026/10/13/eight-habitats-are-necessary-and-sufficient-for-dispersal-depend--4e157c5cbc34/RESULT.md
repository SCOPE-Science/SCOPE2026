# Eight habitats are necessary and sufficient for dispersal-dependent edge-synchrony rankings on trees

## Finding

**Theorem (sharp eight-habitat onset and complete small-tree classification).** Under the model specified below, every tree with \(2\le n\le7\) habitats has a fixed weak ordering of the stationary Pearson synchrony values on its edges, for all positive dispersal intensities. Of the \(23\) unlabelled eight-habitat trees, exactly \(6\) have an edge pair whose ordering strictly reverses as dispersal varies. Across one representative of each eight-habitat isomorphism class there are exactly \(11\) reversing edge pairs, each crossing precisely once at a positive intensity. Thus the smallest connected acyclic dispersal network admitting this phenomenon has eight habitats.

For the tree with vertex set \(\{0,1,2,3,4,5,6,7\}\) and edges \(\{01,12,05,23,24,56,57\}\), the two adjacent-edge correlations \(\rho_{01}\) and \(\rho_{12}\) reverse ranking exactly at
\[
 t_*=2+\sqrt{5}.
\]
In particular, \(\rho_{12}<\rho_{01}\) for \(0<t<t_*\), with equality at \(t_*\), and \(\rho_{12}>\rho_{01}\) for \(t>t_*\).

## Assumptions and scope

A habitat network is a finite, connected, unweighted, undirected **simple tree** \(T=(V,E)\) with \(n=|V|\ge2\). Write \(L\) for its graph Laplacian. The centered population-fluctuation vector \(X\) follows the Ornstein–Uhlenbeck system
\[
 \mathrm dX(s)=-(aI+dL)X(s)\,\mathrm ds+\sigma\,\mathrm dW(s),
 \qquad a,d,\sigma>0,
\]
where \(W\) has independent standard components and the system is considered in stationarity. The dimensionless coupling parameter is \(t=d/a\). For an edge \(uv\in E\), define
\[
 \rho_{uv}(t)=\frac{\operatorname{Cov}(X_u,X_v)}{\sqrt{\operatorname{Var}(X_u)\operatorname{Var}(X_v)}}.
\]
A **strict rank reversal** of edges \(e,f\) means the strict inequality \(\rho_e<\rho_f\) holds at one positive value of \(t\), while \(\rho_e>\rho_f\) holds at another. No claim is made for nonadjacent vertex pairs, weighted or cyclic graphs, correlated noise, heterogeneity, or a classification of trees with more than eight vertices.

## Proof

**1. Exact stationary covariance.** Since \(aI+dL\) is symmetric positive definite, the stationary Lyapunov equation \((aI+dL)\Sigma+\Sigma(aI+dL)=\sigma^2I\) has solution
\[
 \Sigma=\frac{\sigma^2}{2a}(I+tL)^{-1}.
\]
Put \(K(t)=I+tL\). It is an irreducible nonsingular symmetric \(M\)-matrix, so all entries of \(K(t)^{-1}\) are strictly positive. The scalar factor drops out of Pearson correlations.

**2. Exact forest/minor representation.** Define \(A_v(t)=\det K(t)_{V\setminus\{v\}}\) and, for an edge \(e=uv\), \(B_e(t)=\det K(t)_{V\setminus\{u,v\}}\). Empty minors have determinant \(1\). The unique \(u\)--\(v\) path in a tree is the edge \(uv\), hence the off-diagonal cofactor identity is
\[
 \operatorname{cof}_{uv}K(t)=tB_{uv}(t).
\]
The inverse-adjugate formula therefore yields
\[
 \rho_{uv}(t)^2=\frac{t^2B_{uv}(t)^2}{A_u(t)A_v(t)}. \tag{1}
\]
All minors in (1) are strictly positive when \(t>0\).

Every needed principal minor has a positive-integer-coefficient forest formula. For \(S\subseteq V\) with at most two elements, let \(\mathcal F(T)\) be all spanning subforests, obtained by choosing subsets of the tree edges. If \(\mathcal C(F)\) is the set of vertex components of \(F\), then
\[
 \det K(t)_{V\setminus S}=\sum_{F\in\mathcal F(T)}t^{|E(F)|}
 \prod_{C\in\mathcal C(F)}w_S(C),\qquad
 w_S(C)=\begin{cases}|C|,&C\cap S=\varnothing,\\1,&|C\cap S|=1,\\0,&|C\cap S|\ge2.\end{cases} \tag{2}
\]
This follows by adjoining an auxiliary root with unit-weight edges at all unpinned vertices, and applying the rooted matrix-tree identity: each component either has its unique pinned root or may choose exactly one of its own vertices as root. Formula (2) is independently checked against integer Bareiss determinants for two positive coupling values in the certificate.

**3. A sign certificate for comparing edges.** For \(e=uv\) and \(f=xy\), define
\[
 P_{e,f}(t)=B_e(t)^2A_x(t)A_y(t)-B_f(t)^2A_u(t)A_v(t). \tag{3}
\]
By (1), the sign of \(P_{e,f}(t)\) for \(t>0\) equals the sign of \(\rho_e(t)-\rho_f(t)\): the denominators and the correlations themselves are strictly positive. If every nonzero coefficient of \(P_{e,f}\) has one sign, no reversal is possible. If it has mixed coefficient signs, the exact certificate verifies that it factors as \(Q(t)R(t)\), where \(R(t)\) is strictly one-signed for \(t>0\), and \(Q\) is one of
\[
\begin{gathered}
 t^3-5t^2-5t-1,\quad t^2-4t-1,\quad t^4-3t^3-10t^2-6t-1,\\
 t^2-2t-1,\quad t^3-3t^2-4t-1,\quad 2t^2-2t-1.
\end{gathered} \tag{4}
\]
Each polynomial in (4) has one and only one strictly positive zero: its constant term is negative, its leading coefficient is positive, and its descending coefficient sequence has one sign change, so the intermediate-value theorem and Descartes' rule of signs apply. Therefore each mixed case is exactly one strict reversal.

**4. Finite but exhaustive classification.** The accompanying standard-library Python checker generates *every* labelled tree with \(2\le n\le8\) by the Prüfer bijection, computes its canonical unlabelled representative using the center-rooted tree code, evaluates the exact integer forest polynomials (2), and checks (3) for every pair of edges. The counts of unlabelled trees for increasing orders \(2,\ldots,8\) are exactly
\[
 (1,1,2,3,6,11,23).
\]
Across these \(47\) tree representatives, the checker processes exactly \(733\) edge-pair comparisons: \(201\) are identically tied, \(521\) have one strict sign throughout, and \(11\) change sign. All changing pairs occur in exactly \(6\) distinct eight-vertex tree classes, with \(1,2,2,3,1,2\) changing comparisons, respectively, in canonical-class order. For complete reproducibility, the six center-rooted class encodings and one complete set of edges for each are regenerated by `verify.py`; its reported encodings are:

```
(((()()))((())))
(((())())((())))
(((()))((()))())
[((()()()))((()))]
[((()())())((()))]
[((()()))((()()))]
```

This is a finite, exhaustive proof of the statements for orders through eight, not an inference from sampling or a claim about higher orders.

**5. Explicit exact witness.** For \(E=\{01,12,05,23,24,56,57\}\), direct substitution in (1) gives
\[
 \rho_{01}(t)^2=\frac{t^2(t^2+4t+1)^2}{(t^3+8t^2+6t+1)^2},
\]
\[
 \rho_{12}(t)^2=\frac{t^2(t^3+8t^2+6t+1)}{(t^2+4t+1)(t^3+12t^2+7t+1)}.
\]
Their exact difference is
\[
 \rho_{12}(t)^2-\rho_{01}(t)^2=
 \frac{t^3(4t+1)(t^2-4t-1)(2t^3+12t^2+7t+1)}
 {(t^2+4t+1)(t^3+8t^2+6t+1)^2(t^3+12t^2+7t+1)}.
\]
All factors other than \(t^2-4t-1\) are positive on \((0,\infty)\), giving the stated threshold \(t_*=2+\sqrt5\). The checker independently reconstructs the two rational identities and confirms the crossing polynomial from integer minors.

## Verification

Run `python3 verify.py` (Python 3.10 or later; no third-party packages). It reports `VERIFY_OK shape_counts=1,1,2,3,6,11,23 mixed_shape_count=6 mixed_edge_pairs=11 all_pair_comparisons=733 identically_tied=201`. The certificate uses exact integer/rational arithmetic and evaluates the auxiliary minors by both (2) and a separate fraction-free determinant algorithm. The analytic steps above justify (1), (2), the Prüfer exhaustion, and the uniqueness of each crossover; exact integer calculations provide the complete finite case split.

## Relationship to prior work

Engen, Lande, Sæther and Bregnballe (2005) analyze ecological synchrony, regional stochastic forcing and migration with continuous spatial scaling and statistical inference. Lande, Engen and Sæther (1999) derive a population-synchrony spatial scale relation; Liebhold, Johnson and Bjørnstad (2006) study heterogeneity of density dependence and synchrony. These works motivate the stochastic ecological setting but do not present the normalized edge-by-edge classification for unweighted finite trees under a homogeneous common dispersal parameter.

The inverse-Laplacian kernel itself and rooted-forest representations are **not new**: Chebotarev and Shamis's published graph-accessibility work and forest-metric studies investigate the very matrix \((I+tL)^{-1}\). Their forest distances depend on combinations such as \(K^{-1}_{uu}+K^{-1}_{vv}-2K^{-1}_{uv}\), whereas our Pearson criterion is the normalized ratio \(K^{-1}_{uv}/\sqrt{K^{-1}_{uu}K^{-1}_{vv}}\). Their formulas facilitate the present proof but do not directly state the sharp eight-vertex limit or the six exceptional topology classes. Bolin, Simas and Wallin study related metric-graph Gaussian Markov fields with different precision constructions. A stronger comparison theorem elsewhere might nonetheless subsume the enumeration; an independent literature audit remains outstanding.

## Limitations

The theorem is a mathematical characterization for a symmetric, independently forced linear stochastic model. It does not establish ecological generality under nonlinear dynamics or real observations. The numerical count of eleven reversing edge pairs is taken across one *unlabelled representative* per eight-vertex tree; it is not a count of all labelled networks. The result does not classify larger graphs or arbitrary vertex pairs. The forest kernel and determinant methods were established previously, and novelty depends on the precise ranking theorem and its exhaustive sharp bound. Independent external validation has not been performed.

## References

- Engen, S., Lande, R., Sæther, B.-E., and Bregnballe, T. (2005). *Estimating the pattern of synchrony in fluctuating populations*. Journal of Animal Ecology 74, 601–611. First online 23 June 2005. DOI: https://doi.org/10.1111/j.1365-2656.2005.00942.x .
- Lande, R., Engen, S., and Sæther, B.-E. (1999). *Spatial Scale of Population Synchrony: Environmental Correlation versus Dispersal and Density Regulation*. American Naturalist 154, 271–281. DOI: https://doi.org/10.1086/303240 .
- Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H., and Fagan, W. F. (2000). *Dispersal, Environmental Correlation, and Spatial Synchrony in Population Dynamics*. American Naturalist 155, 628–636. DOI: https://doi.org/10.1086/303350 .
- Liebhold, A. M., Johnson, D. M., and Bjørnstad, O. N. (2006). *Geographic variation in density-dependent dynamics impacts the synchronizing effect of dispersal and regional stochasticity*. Population Ecology 48, 131–138. DOI: https://doi.org/10.1007/s10144-005-0248-6 .
- Chebotarev, P. and Shamis, E. *The Matrix-Forest Theorem and Measuring Relations in Small Social Groups* (original 1997, arXiv copy `math/0602070`); and *The Forest Metrics for Graph Vertices* (arXiv `math/0602573`, first deposited 2006). Full texts: https://arxiv.org/pdf/math/0602070 and https://arxiv.org/pdf/math/0602573 .
- Bolin, D., Simas, A. B., and Wallin, J. *An explicit link between graphical models and Gaussian Markov random fields on metric graphs*. arXiv:2501.03701. https://arxiv.org/abs/2501.03701 .
