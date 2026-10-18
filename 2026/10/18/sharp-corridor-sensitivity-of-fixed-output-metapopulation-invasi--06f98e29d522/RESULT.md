# Sharp corridor sensitivity of fixed-output metapopulation invasion

## Finding
Consider any finite connected undirected simple habitat network \(G\) with \(n\ge3\) patches, positive extinction rates \(m_i\), and an absent edge \(uv\). Each occupied patch exports potential colonists at a fixed total rate, divided uniformly among its current neighbors. With extinction rates held fixed, the ratio between the linear invasion capacities after and before adding \(uv\) obeys the strict, universal bound
\[
\frac{\rho(K_{G+uv})}{\rho(K_G)}>\frac1{\sqrt2},\qquad
K_G=\operatorname{diag}(m_i^{-1})A_G\operatorname{diag}(d_i^{-1}).
\]
There is no finite universal upper bound. More precisely, as \(G\), \(uv\), and all positive extinction rates vary, **the exact set of attainable ratios is \((1/\sqrt2,\infty)\)**. Every value is already attained by changing the path on three patches into a triangle. These are the smallest possible networks permitting the operation. Thus an additional dispersal corridor may make a species' local invasion harder, but cannot increase its critical colonization rate by a factor of \(\sqrt2\) or more in this model; it can make invasion arbitrarily easier. The strict lower endpoint is an infimum, not an attainable value.

## Assumptions and scope
Let \(G=(V,E)\) be a connected, simple, undirected graph with \(V=\{1,\ldots,n\}\), \(n\ge3\), adjacency matrix \(A_G\), and degrees \(d_i\ge1\). Let \(m_i>0\) be arbitrary heterogeneous local extinction rates, identical before and after the corridor addition. Write \(q_i=1/m_i\) and \(D_G=\operatorname{diag}(d_i)\). Consider the deterministic independent-occupancy approximation
\[
\dot p_i=-m_i p_i+c(1-p_i)\sum_{j:\,ij\in E}\frac{p_j}{d_j},
\qquad 0\le p_i\le1,\quad c>0.
\]
The fixed-output assumption is essential: adding \(uv\) changes the degrees and **redistributes**, rather than increases, the export budget of the two endpoints. The theorem concerns only the linear instability of the empty equilibrium, not exact finite-population stochastic survival or global nonlinear recovery time. Here \(K_G=\operatorname{diag}(q_i)A_G D_G^{-1}\), \(\rho\) denotes spectral radius, and \(c_*(G)=1/\rho(K_G)\) is the critical colonization rate.

The Jacobian at \(p=0\) is \(J(c)=-\operatorname{diag}(m_i)+cA_G D_G^{-1}\). At \(c=c_*\), a strictly positive Perron vector of \(K_G\) is a zero eigenvector of \(J(c)\); the irreducible Metzler comparison principle, equivalently the nonsingular \(M\)-matrix criterion for \(\operatorname{diag}(m_i)(I-cK_G)\), makes \(J(c)\) Hurwitz for \(c<c_*\) and unstable for \(c>c_*\).

## Proof
**Symmetric reduction.** Put \(S_G=\operatorname{diag}(\sqrt{q_i d_i})\). Direct multiplication gives
\[
S_G^{-1}K_GS_G=H_G,
\qquad (H_G)_{ij}=(A_G)_{ij}\sqrt{\frac{q_iq_j}{d_i d_j}}.
\]
The real symmetric, nonnegative, irreducible matrix \(H_G\) has Perron root \(\rho(K_G)\) and a strictly positive unit Perron vector \(z\).

**Universal strict bound.** Let \(G'=G+uv\), with \(uv\notin E\). Only \(d_u\) and \(d_v\) change, each increasing by one. Because \(uv\) was absent, every *old* edge is incident with at most one of \(u,v\). Its new symmetric weight is therefore at least \(1/\sqrt2\) of the old weight: for an endpoint of degree \(d\ge1\), the factor is \(\sqrt{d/(d+1)}\ge1/\sqrt2\). Every other old weight is unchanged; a new strictly positive entry appears at \(uv\) and \(vu\). Consequently
\[
H_{G'}-\frac1{\sqrt2}H_G\ge0
\]
entrywise, with strict positivity in the newly created two entries. Since \(z_u,z_v>0\), the Rayleigh quotient gives
\[
\rho(K_{G'})\ge z^{\mathsf T}H_{G'}z>
\frac1{\sqrt2}z^{\mathsf T}H_Gz=
\frac1{\sqrt2}\rho(K_G).
\]
In particular equality is impossible for any allowed finite graph and positive extinction rates.

**Three patches attain every other ratio.** Take the path \(1-2-3\), add the missing edge \(1-3\), and set \((q_1,q_2,q_3)=(1,b,1)\), with any \(b>0\). On the path the two nonzero symmetric weights are \(\sqrt{b/2}\), hence \(\rho(K_G)=\sqrt b\). On the triangle the two center-to-leaf weights are \(\sqrt b/2\) and the leaf-to-leaf weight is \(1/2\). The Perron eigenvector is symmetric in leaves \(1\) and \(3\), giving the exact Perron root
\[
\rho(K_{G'})=\frac{1+\sqrt{1+8b}}4.
\]
Therefore the ratio is
\[
R(b)=\frac{1+\sqrt{1+8b}}{4\sqrt b}
=\frac14\left(b^{-1/2}+\sqrt{8+b^{-1}}\right).
\]
Both terms on the right decrease strictly in \(b\). Moreover \(R(b)\to\infty\) as \(b\downarrow0\), \(R(b)\to1/\sqrt2\) as \(b\to\infty\), and \(R(1)=1\). Continuity and strict monotonicity show that the image of \((0,\infty)\) is precisely \((1/\sqrt2,\infty)\), and the corridor hinders invasion exactly when \(b>1\) in this family. A connected simple graph on one or two vertices has no missing edge; thus three patches are minimal. This completes the proof.

## Verification
The accompanying `verify_capacity.py` independently constructs the degree-normalized symmetric matrix and evaluates its largest eigenvalue using a numerical symmetric eigensolver. It checks the three-patch formulas across seven parameter values, verifies the reversal at \(b=1\), and tests the strict lower bound over **769,905** comparisons: every connected labelled graph with three to five vertices, each nonedge, and every positive patch-quality assignment from \(\{1/3,1,3\}^n\). The observed minimum ratio on this finite grid was approximately \(0.7464269719\). Run `python verify_capacity.py` with Python 3 and NumPy; the output ends with `All numerical tests passed.` These finite checks are corroboration only: the universal inequality and exact open range follow from the symbolic argument above, not from the enumeration.

## Relationship to prior work
Hanski and Ovaskainen (2000) introduced the spectral metapopulation capacity of a fragmented landscape. Grilli, Barabás and Allesina (2015, Methods and Supporting Information) consider patch occupancy and a symmetric dispersal kernel whose edge contribution is tied to patch values and distance. In their matrix, adding an additional positive coupling does not require dividing all exports from its endpoints by their changed degrees; their spectral and patch-removal conclusions therefore do not imply this edge-addition bound. Shtilerman and Stone (2015) study how dispersal network topology, in/out-degree correlations, and symmetry control a spectral persistence index; their regular-network benchmark has eigenvalue equal to degree, unlike the degree-normalized fixed-export matrix here, which has eigenvalue one under homogeneous extinction. Gilarranz and Bascompte (2012) compare abundance on different network families and demographic ratios, rather than a sharp universal ratio for a fixed total exporting budget. Eldan, Rácz and Schramm (2015) study the normalized-Laplacian *spectral gap* after adding an edge, not the positive eigenvalue of a heterogeneously quality-weighted transition matrix. The particular sharp factor, complete ratio range, and three-patch saturation have not been identified in the inspected work.

## Limitations
The fixed-output normalization and unchanged positive local extinction rates are necessary; replacing the export rule by an added independent per-edge export term changes the conclusion. The theorem is an exact linear invasion-capacity result within a deterministic occupancy approximation, not a result about almost-sure persistence in finite stochastic models. The sharp lower ratio is approached only as a quality ratio becomes unbounded; it is never attained at strictly positive finite quality parameters. Although directly relevant full primary material on spectral landscape capacities was inspected, some related ecology articles were accessible only as abstracts or previews, leaving a residual possibility of an equivalent result stated elsewhere, perhaps with different stochastic-network terminology. Nothing here establishes biological effect size under measured habitat parameters.

## References
- Hanski, I., and Ovaskainen, O. (2000). “The metapopulation capacity of a fragmented landscape.” *Nature* 404, 755–758. DOI: `10.1038/35008063`. First public date verified as 2000-04-13.
- Grilli, J., Barabás, G., and Allesina, S. (2015). “Metapopulation Persistence in Random Fragmented Landscapes.” *PLOS Computational Biology* 11(5), e1004251. DOI: `10.1371/journal.pcbi.1004251`. Full open-access article.
- Shtilerman, E., and Stone, L. (2015). “The effects of connectivity on metapopulation persistence: network symmetry and degree correlations.” *Proceedings of the Royal Society B* 282, 20150203. DOI: `10.1098/rspb.2015.0203`.
- Gilarranz, L. J., and Bascompte, J. (2012). “Spatial network structure and metapopulation persistence.” *Journal of Theoretical Biology* 297, 11–16. DOI: `10.1016/j.jtbi.2011.11.027`.
- Eldan, R., Rácz, M. Z., and Schramm, T. (2015). “Braess's paradox for the spectral gap in random graphs and delocalization of eigenvectors.” arXiv:`1504.07669` (first posted 2015-04-28).
