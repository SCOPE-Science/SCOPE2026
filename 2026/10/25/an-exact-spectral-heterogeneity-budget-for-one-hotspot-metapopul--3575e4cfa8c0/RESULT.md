# An exact spectral heterogeneity budget for one-hotspot metapopulation epidemics

## Finding

For the equal-population SIR-network model with one transmission hotspot, the disease-free invasion threshold on **every finite symmetric stochastic mobility network** is governed by one explicit, nonnegative spectral-heterogeneity statistic. It follows that two networks can have **exactly the same journeys to and from the hotspot**, the same population and disease parameters, and the same variance of hotspot traffic, yet have opposite invasion outcomes merely because travel between the other neighborhoods changes.

Fix an integer \(M\ge2\), \(0<r<1\), and \(\zeta>1\). Let \(\Phi\) be any real, symmetric, entrywise nonnegative, row-stochastic \(M\times M\) matrix. Set \(e=e_M\), \(v=\Phi e\), and
\[
K=r\Phi\operatorname{diag}(1,\ldots,1,\zeta)\Phi,
\qquad \zeta_{\mathrm{crit}}=1+\frac{M(1-r)}r.
\]
Choose any real orthonormal eigenbasis \((q_j)_{j=1}^{M}\) of \(\Phi\), with \(q_1=M^{-1/2}\mathbf1\), and let \(\lambda_j\) be its associated eigenvalues, where \(\lambda_1=1\). Define the **hotspot spectral heterogeneity**
\[
H_r(\Phi,e)=\sum_{j=2}^{M}\frac{\lambda_j^2q_j(M)^2}{1-r\lambda_j^2}
= v^{\mathsf T}(I-r\Phi^2)^{-1}v-\frac1{M(1-r)}.
\]
The statistic is independent of the eigenbasis, including at repeated eigenvalues. Then the following equivalence holds, with no graph-connectivity or positive-diagonal assumption:
\[
\boxed{\rho(K)<1\ \Longleftrightarrow\quad H_r(\Phi,e)<\frac{\zeta_{\mathrm{crit}}-\zeta}{M(\zeta-1)(1-r)}.}
\]
Equality in the scalar comparison is equivalent to \(\rho(K)=1\); its reverse strict inequality is equivalent to \(\rho(K)>1\). In particular, \(\zeta>\zeta_{\mathrm{crit}}\) makes suppression impossible for every admissible network, and \(\zeta=\zeta_{\mathrm{crit}}\) permits only criticality, exactly when \(\Phi e=M^{-1}\mathbf1\).

Independently of the remaining mobility pattern,
\[
\rho(K)\ge \frac{r(M-1+\zeta)}M.
\]
For \(\zeta>1\), **equality holds if and only if** \(\Phi e=M^{-1}\mathbf1\). Thus a perfectly uniform hotspot column, not necessarily globally uniform travel, is the complete set of optimal arrangements. If
\(V=\|\Phi e-M^{-1}\mathbf1\|_2^2\), the observable heterogeneity admits the comparisons
\[
V\le H_r(\Phi,e)\le\frac{V}{1-r},
\]
which give immediate sufficient and necessary screening inequalities, although \(V\) alone does not classify invasion.

**Exact opposite-outcome pair.** Take \(M=5\), \(r=4/5\), and \(\zeta=11/5\). For either \(d=1/10\) or \(d=1/5\), construct \(\Phi_d\) with uniform off-diagonal background entry \(d\), hotspot column
\[
(v_1,v_2,v_3,v_4,v_5)
=\left(\frac{17}{50},\frac3{50},\frac15,\frac15,\frac15\right),
\]
and background diagonal \((\Phi_d)_{ii}=1-v_i-3d\) for \(1\le i\le4\). The hotspot diagonal is \(1/5\). Both are symmetric, nonnegative, stochastic, and have identical hotspot traffic and \(V=49/1250\). The critical heterogeneity budget is \(1/24\), while exact inversion yields
\[
\boxed{H_{4/5}(\Phi_{1/10},e)=\frac{529543}{11008272}>\frac1{24}},
\qquad
\boxed{H_{4/5}(\Phi_{1/5},e)=\frac{245}{5956}<\frac1{24}}.
\]
Therefore the first network is **supercritical** and the second **subcritical**. The determinant signs independently agree:
\[
\det(I-K_{1/10})=-\frac{111229704}{152587890625}<0,
\qquad
\det(I-K_{1/5})=\frac{113164}{1220703125}>0.
\]

## Assumptions and scope

The model is the continuous-time SIR-network invasion linearization with \(M\) resident neighborhoods, equal resident populations \(N>0\), equal recovery rate \(\gamma>0\), and homogeneous background transmission \(\beta_0>0\) except at neighborhood \(M\), where transmission is \(\zeta\beta_0\). The notation \(r=\beta_0/\gamma\) obeys \(0<r<1\). Symmetry and row stochasticity of \(\Phi\) imply unit column sums and equal present populations, giving precisely the next-generation matrix above. The hotspot is more transmissive than the background, \(\zeta>1\), and may or may not itself be supercritical. The especially relevant hot-spot-only outbreak regime is \(1/r<\zeta<\zeta_{\mathrm{crit}}\). We mean local invasion at the fully susceptible disease-free state, not final epidemic size or global endemic stability.

The displayed eigenbasis and spectral sum always exist because a symmetric stochastic matrix has eigenvalues in \([-1,1]\). Repeated eigenvalues are permitted. \(H_r\) can be evaluated equivalently by one positive-definite linear solve, so full eigenanalysis is unnecessary.

## Proof

**1. Exact rank-one decomposition.** Write \(D=I+(\zeta-1)ee^{\mathsf T}\). Since \(\Phi\) is symmetric,
\[
K=r\Phi^2+r(\zeta-1)vv^{\mathsf T},\qquad v=\Phi e.
\]
As \(0<r<1\) and \(\|\Phi\|_2\le1\), the matrix \(A=I-r\Phi^2\) is positive definite. Since \(K\) is symmetric positive semidefinite, \(\rho(K)<1\) holds exactly when \(I-K=A-r(\zeta-1)vv^{\mathsf T}\) is positive definite. Congruence by \(A^{-1/2}\) reduces this to a rank-one perturbation of the identity; it is positive definite exactly when
\[
r(\zeta-1)v^{\mathsf T}A^{-1}v<1.
\]
At equality the minimum eigenvalue of \(I-K\) is zero; above equality it is negative. This proves all three threshold directions without approximations.

**2. Split the homogeneous eigenmode.** Let \(q_1=M^{-1/2}\mathbf1\). By stochasticity \(\Phi q_1=q_1\), and \(\langle e,q_1\rangle=1/\sqrt M\). Expanding \(v=\Phi e\) in an orthonormal eigenbasis gives
\[
v^{\mathsf T}A^{-1}v=\sum_{j=1}^M\frac{\lambda_j^2q_j(M)^2}{1-r\lambda_j^2}
=\frac{1}{M(1-r)}+H_r(\Phi,e).
\]
Inserting this identity into the scalar threshold, then rearranging, gives
\[
H_r(\Phi,e)<\frac{M(1-r)-r(\zeta-1)}{Mr(\zeta-1)(1-r)}
=\frac{\zeta_{\mathrm{crit}}-\zeta}{M(\zeta-1)(1-r)}.
\]
The spectral representation also proves nonnegativity and basis independence. Because \(V=\sum_{j\ge2}\lambda_j^2q_j(M)^2\), and \(1\le (1-r\lambda_j^2)^{-1}\le(1-r)^{-1}\), the claimed two-sided variance bound follows.

**3. Optimality and exact equality case.** For \(u=M^{-1/2}\mathbf1\), the symmetric Rayleigh principle gives
\[
\rho(K)\ge u^{\mathsf T}Ku=r\left(1+\frac{\zeta-1}{M}\right).
\]
If equality holds, the unit vector \(u\) must be a top eigenvector. But
\[
Ku=\frac r{\sqrt M}\bigl[\mathbf1+(\zeta-1)\Phi e\bigr].
\]
Since \(\zeta>1\), this is parallel to \(u\) exactly when \(\Phi e=M^{-1}\mathbf1\). Conversely, under that column condition, every row sum of the nonnegative matrix \(K\) equals \(r(M-1+\zeta)/M\); its spectral radius equals that common row sum. This proves both the sharp lower bound and the full optimizer set. It also proves that \(\zeta>\zeta_{\mathrm{crit}}\) implies \(\rho(K)>1\), whereas \(\zeta=\zeta_{\mathrm{crit}}\) gives \(\rho(K)\ge1\) with equality only at a uniform hotspot column.

**4. Exact equal-column reversal.** Put \(p=(17/50,3/50,1/5,1/5)\) and define the two symmetric matrices explicitly by
\[
\Phi_d=\begin{pmatrix}
1-p_1-3d&d&d&d&p_1\\
d&1-p_2-3d&d&d&p_2\\
d&d&1-p_3-3d&d&p_3\\
d&d&d&1-p_4-3d&p_4\\
p_1&p_2&p_3&p_4&1/5
\end{pmatrix},\qquad d\in\{1/10,1/5\}.
\]
All entries are nonnegative (the smallest is \(3/50\)), and direct row sums give one. The fifth columns agree. Substituting \(r=4/5\) and \(\zeta=11/5\) into the budget gives \(\zeta_{\mathrm{crit}}=9/4\) and the critical level \(1/24\). Exact rational inversion of \(I-(4/5)\Phi_d^2\), or ordinary Gaussian elimination, yields the two fractions reported in the Finding. Their differences from \(1/24\) are respectively \(70865/11008272>0\) and \(-19/35736<0\), proving opposite outcomes with exactly the same hub column and hotspot-traffic variance. The attached checker reconstructs both matrices and evaluates these fractions directly.

**5. Uniform-hub subcase and its scope.** If every peripheral node has hub flux \(p\in(0,1/(M-1)]\) and the background block \(B\) is any nonnegative symmetric matrix with constant row sum \(1-p\), the background-constant/hub subspace is invariant. There the flux becomes
\[
T=\begin{pmatrix}1-p&\sqrt{M-1}\,p\\ \sqrt{M-1}\,p&1-(M-1)p\end{pmatrix}.
\]
The remaining background-contrast modes contribute eigenvalues no larger than \(r(1-p)^2\); the dominant two-dimensional block is \(rT\operatorname{diag}(1,\zeta)T\), whose upper-left entry is strictly larger. Consequently, the spectral threshold of the uniform-hub class is independent of all background-to-background edges. This recovers the established fully-connected/star formulas and the families proposed in the motivating article. It is included as a consistency check, **not** the claimed new ingredient: the rank-one budget and same-column reversal apply when the hub column is not uniform, so equitable quotient reduction no longer applies.

## Verification

Run `python verify.py` in a Python 3 environment with SymPy installed. The standalone program verifies the symbolic characteristic identities for the uniform-hub comparison, constructs both five-by-five nonuniform flux matrices using exact rational entries, computes the two spectral budgets with rational matrix inverses, checks strict signs against the critical budget, compares independent exact determinants of \(I-K\), and reproduces eight further full-matrix uniform-hub spectral comparisons. These finite tests validate the printed example and algebra; the theorem for arbitrary \(M\) and \(\Phi\) is proved above, not inferred from a numerical search.

## Relationship to prior work

Das and Stolerman's 2023 preprint (subsequently published in June 2024) formulates the SIR-network next-generation matrix for symmetric travel flux, establishes standard thresholds for star, complete, and other special background classes, and states four conjectures for further **uniform-hub** network classes. The equal-hub subcase above is consistent with those statements, but is not asserted novel in isolation. The classical equitable-partition spectral-radius theorem (You–Yang–So–Xi, 2019) provides a broader linear-algebraic mechanism for that particular reduction, and a general rank-one matrix test is used explicitly here. The contribution assessed here is the **exact eigenmode-weighted critical budget for arbitrary nonuniform hub traffic together with two networks that have identical hotspot mobility but opposite invasion classifications**. The cited works do not report that combined statement or pair. Other metapopulation frameworks (e.g. Meng and Masuda, 2021 preprint / 2022 journal, and Han et al., 2020) have different transport mechanisms; their qualitative mobility effects alone do not settle this exact SIR-network budget.

## Limitations

This is a local disease-free invasion result, not a statement about final attack rates, global SIR solutions, directed mobility, unequal resident populations, multiple distinct hotspot infection rates, or heterogeneous recovery rates. Symmetry and equal populations are essential to the displayed matrix and its simple spectral energy. The theorem's value is not a new rank-one-perturbation identity or a new general equitable quotient theorem, both of which are established tools. Publication priority for this precise model-specific characterization is not independently certified; uninspected later literature might imply it. For degenerate parameters outside \(0<r<1\) and \(\zeta>1\), a different threshold analysis may be required.

## References

1. H. K. Das and L. M. Stolerman, *Epidemic thresholds and disease dynamics in metapopulations: the role of network geometry and human mobility*, arXiv:2308.01998, first posted 2023-08-03; published as *Epidemic Thresholds and Disease Dynamics in Metapopulations: The Role of Network Structure and Human Mobility*, SIAM Journal on Applied Dynamical Systems 23 (2024), 1579–1609, DOI:10.1137/23M1579522. Relevant full-text Sections 2–4, especially Conjectures 1–4.
2. L. M. Stolerman, D. Coombs and S. Boatto, *SIR-network model and its application to dengue fever*, SIAM Journal on Applied Mathematics 75 (2015), DOI:10.1137/140996148. Original SIR-network formulation and epidemic criteria.
3. L. You, M. Yang, W. So and W. Xi, *On the spectrum of an equitable quotient matrix and its application*, Linear Algebra and its Applications (2019), DOI:10.1016/j.laa.2019.04.013. General equitable quotient spectral-radius theorem; background rather than a new contribution here.
4. L. Meng and N. Masuda, *Epidemic dynamics on metapopulation networks with node2vec mobility*, Journal of Theoretical Biology 534 (2022), 110960, arXiv:2106.08080. Related but different travel model.
5. Han et al., *Exploring the Epidemic Spreading in a Multilayer Metapopulation Network by considering Individuals’ Periodic Travelling*, Complexity (2020), article 6782018, DOI:10.1155/2020/6782018. Related mixing thresholds under different dynamics.
