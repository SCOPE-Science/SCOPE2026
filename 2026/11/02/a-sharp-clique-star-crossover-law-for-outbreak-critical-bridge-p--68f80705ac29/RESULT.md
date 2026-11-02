# A sharp clique–star crossover law for outbreak-critical bridge placement

## Finding

Fix integers \(r\ge3\) and \(s\ge1\). Form the connected graph \(T_{r,s}\) by taking a clique \(K_r\) with a marked vertex \(a\), a star \(K_{1,s}\) with hub \(c\), and the single edge \(ac\). All existing edges have unit weight. For each real \(q>\rho(A_{T_{r,s}})\), define the diagonal resolvent score
\[
D_u(q)=\bigl[(qI-A_{T_{r,s}})^{-1}\bigr]_{uu}.
\]
Here \(\rho\) is the adjacency spectral radius. Let
\[
\zeta_r=\frac{r^2-3r+4+(r-2)\sqrt{r^2-2r+5}}2.
\]
The complete classification of maximizers \(\arg\max_uD_u(q)\) is:

1. For \(1\le s\le r-1\), the unique maximizer is the clique connector \(a\), for every permissible \(q\).
2. For \(r\le s<\zeta_r\), put \(q_*=s(r-2)/(s-r+1)\). Then \(q_*>\rho(A_{T_{r,s}})\); the unique maximizer is \(a\) when \(\rho(A_{T_{r,s}})<q<q_*\), both \(a,c\) tie at \(q=q_*\), and the unique maximizer is the star hub \(c\) when \(q>q_*\).
3. For integers \(s\ge\zeta_r\), the unique maximizer is \(c\) for every permissible \(q\).

The result converts directly to an exact epidemic-invasion bridge-placement rule. Let \(H\) be any finite connected undirected graph with nonnegative symmetric adjacency weights and \(q>\max\{\rho(A_{T_{r,s}}),\rho(A_H)\}\). Add a **single** new edge of weight \(w\ge0\) from an arbitrary \(u\in T_{r,s}\) to a fixed \(v\in H\). The spectral SIS/NIMFA disease-free state crosses its linear invasion threshold precisely at
\[
w_{\rm crit}(u,v;q)=\frac1{\sqrt{D_u(q)\,D_v^H(q)}},\qquad
D_v^H(q)=\bigl[(qI-A_H)^{-1}\bigr]_{vv}.
\]
The endpoint making the threshold smallest is exactly the maximizer in the preceding classification, **independently of the recipient graph and its fixed receiving vertex**. If \(H\) has larger spectral radius than \(q_*\), its stability-domain restriction can hide the low-\(q\) side of the crossover; the intrinsic ranking law on \(T_{r,s}\) is unaffected.

For a seven-vertex sharp example, take \((r,s)=(3,3)\). The crossover is \(q_*=3\), and
\[
\begin{array}{c|cc}
q&D_a(q)&D_c(q)\\\hline
5/2&78/31&70/31\\
3&2/3&2/3\\
4&39/118&20/59
\end{array}
\]
All three displayed values of \(q\) lie above \(\rho(A_{T_{3,3}})=2.368649\ldots\). Hence increasing the recovery-to-transmission ratio can reverse which of two equally available endpoints creates the smaller critical cross-community contact weight. The entire crossover region is sharp: outside the stated integer leaf-count range no reversal occurs.

## Assumptions and scope

This is a finite-dimensional result about **undirected symmetric contact networks** and a **single weighted cross-network edge**. The parameter \(q=\delta/\beta\) is the homogeneous recovery-to-unit-contact transmission ratio in continuous-time first-order SIS mean-field (N-intertwined) dynamics, with \(\beta,\delta>0\). Each existing edge transmits at rate \(\beta\); the new edge at rate \(\beta w\). The disease-free Jacobian is \(\beta A-\delta I\), so strict local stability is equivalent to \(\rho(A)<q\). No statement here identifies a positive endemic stationary probability for the exact finite stochastic SIS chain. The spectral criterion is a model-specific linear stability statement, not an exact stochastic extinction theorem.

The fixed receiving vertex \(v\) in \(H\) may be arbitrary. If both endpoints can be chosen, the optimal pair independently maximizes the two diagonal resolvent scores. Repeated cross-links, directed transmissions, nonuniform recovery rates and temporal network changes are outside the claim.

## Proof

**1. General single-edge criterion.** Let \(G,H\) have real symmetric nonnegative adjacency matrices and suppose \(q\) exceeds both spectral radii. Then \(P=qI-A_G\) and \(Q=qI-A_H\) are positive definite. After adding the weighted edge \(uv\), the shifted adjacency operator is
\[
\mathcal M(w)=\begin{pmatrix}P&-w e_u e_v^{\mathsf T}\\-w e_v e_u^{\mathsf T}&Q\end{pmatrix}.
\]
Its Schur complement in \(P\) is \(Q-w^2D_u^G(q)e_ve_v^{\mathsf T}\). The rank-one positive-definiteness criterion gives
\[
\mathcal M(w)\succ0\quad\Longleftrightarrow\quad w^2D_u^G(q)D_v^H(q)<1.
\]
Equality makes \(\mathcal M(w)\) singular; above it the symmetric matrix has a negative eigenvalue. Because the joined adjacency matrix is nonnegative, the loss of positive definiteness of \(qI-A\) is precisely the upward crossing of its Perron eigenvalue through \(q\), proving the formula. Optimizing the bridge endpoint on one side therefore maximizes the corresponding diagonal resolvent.

**2. Reduction to the two connector vertices.** Put
\[
f=\bigl[(qI-A_{K_r})^{-1}\bigr]_{aa}
=\frac{q-r+2}{(q+1)(q-r+1)},\qquad
g=\bigl[(qI-A_{K_{1,s}})^{-1}\bigr]_{cc}=\frac q{q^2-s}.
\]
The clique's off-diagonal inverse entries are \(k=1/[(q+1)(q-r+1)]\), with \(0<k<f\). The star's hub–leaf inverse entries equal \(1/(q^2-s)\), and a leaf diagonal equals \((q^2-s+1)/(q(q^2-s))\). Since \(q>\rho(A_{T_{r,s}})>\max\{r-1,\sqrt{s}\}\), all denominators below are positive and \(fg<1\).

The block inversion formula for the existing unit edge \(ac\) gives
\[
D_a=\frac{f}{1-fg},\qquad D_c=\frac{g}{1-fg}.
\]
For any other clique vertex \(b\), its diagonal changes from \(f\) to \(f+gk^2/(1-fg)\), so
\[
D_a-D_b=\frac{g(f^2-k^2)}{1-fg}>0.
\]
For any star leaf \(\ell\), the star hub–leaf comparison after attachment gives
\[
D_c-D_\ell
=\frac{s-1}{q(q^2-s)}
+\frac{f}{1-fg}\frac{q^2-1}{(q^2-s)^2}>0.
\]
This strict inequality includes \(s=1\), because \(q>r-1\ge2\). Therefore **no** nonconnector vertex can maximize the score.

**3. Exact connector comparison.** A common positive denominator yields
\[
\operatorname{sgn}(D_a-D_c)
=\operatorname{sgn}(f-g)
=\operatorname{sgn}\bigl(s(r-2)+(r-1-s)q\bigr).
\]
If \(s\le r-1\), the last expression is strictly positive. If \(s\ge r\), it changes sign once at \(q_*=s(r-2)/(s-r+1)\), provided this value lies in the admissible interval above \(\rho(A_{T_{r,s}})\).

For \(s\ge r\), elementary rearrangement shows \(q_*>\max\{r-1,\sqrt{s}\}\) if and only if \(s<(r-1)^2\). On that interval \(f(q_*)=g(q_*)=q_*/(q_*^2-s)\). Since the positive decreasing function \(f(q)g(q)\) crosses \(1\) exactly at \(q=\rho(A_{T_{r,s}})\), the prospective switch occurs above the spectral radius exactly when \(f(q_*)g(q_*)<1\), or equivalently \(q_*^2-q_*-s>0\). Multiplication by the positive quantity \((s-r+1)^2/s\) makes this inequality
\[
C_r(s):=-s^2+(r^2-3r+4)s-r+1>0.
\]
Now \(C_r(r)=r(r-1)(r-3)+1>0\) and \(C_r((r-1)^2)=-(r-2)^2(r-1)<0\). The larger zero of the concave quadratic \(C_r\) is precisely \(\zeta_r\), lying strictly between \(r\) and \((r-1)^2\); its lower zero is below \(r\). Consequently \(q_*>\rho(A_{T_{r,s}})\) exactly when \(r\le s<\zeta_r\). Otherwise \(q_*\) is outside the admissible range and the star hub wins throughout. All equality and boundary cases in the stated classification follow.

**4. Explicit sharp example.** At \(r=s=3\), the polynomial whose largest positive zero is \(\rho(A_{T_{3,3}})\) is
\[
(q+1)(q-2)(q^2-3)-q(q-1)=q^4-q^3-6q^2+4q+6.
\]
The two connector diagonals simplify to the rational functions above, and their difference is \((3-q)/(q^4-q^3-6q^2+4q+6)\). Exact substitution at \(q=5/2,3,4\) proves the stated strict reversal and tie. Choosing any isolated vertex as \(H\) makes all three values permissible for the two-network bridge problem. This completes the proof.

## Verification

The accompanying standalone `verify_bridge.py` uses only Python's standard library and rational arithmetic. Run `python3 verify_bridge.py` in the directory containing the file. It independently constructs the adjacency matrices, inverts shifted matrices using Gauss–Jordan elimination, checks positive definiteness by rational \(LDL^{\mathsf T}\), compares all vertex diagonals against the proposed maximizers, checks the sharp seven-vertex values, and tests the rank-one Schur threshold on one-, two-, and three-vertex receiving networks. The integer parameter ranges and actual observed counts are in `VERIFICATION.md`.

These finite tests do **not** establish the infinitely quantified theorem; the block-matrix and quadratic-sign proof above is the mathematical justification.

## Relationship to prior work

Dung and Phuc (2026) define community-level spectral SIS threshold sets and prove that a global network threshold cannot exceed an induced community's threshold. Wang et al. (2013) already establish the general weighted interconnection spectral-NIMFA framework, with global threshold \(1/\rho(A+\alpha B)\), bounds and perturbation rules. Sahneh, Scoglio and Chowdhury (2012) study coupling thresholds of general interconnected networks. The basic Schur-complement and resolvent identities used here are classical; **they are not claimed as new**.

The addition is the explicit **all-size \((r,s)\), all-admissible-\(q\)** maximizer classification for one clique–star community, including the sharp algebraic leaf-count frontier \(\zeta_r\), unique crossover \(q_*\), and exact bridge-weight interpretation for every subcritical receiving network. Earlier spectral-centrality work by Aprahamian, Higham and Higham and cut-vertex analysis by Sharkey motivate comparison of Green-function centrality but do not give this exact family-specific epidemiological placement law in the portions inspected. Generic spectral characterizations alone do not provide the leaf-count phase boundary without further analysis.

## Limitations

The conclusion is about a linearized, homogeneous, symmetric-contact SIS mean-field criterion. It does not establish persistence, prevalence, stochastic survival probability, intervention cost efficiency or an optimization over multiple newly introduced links. The optimal vertex depends on the recovery/transmission ratio. Because the threshold comparison uses strict local stability, equality at \(w_{\rm crit}\) is marginal, not a claim of a stable endemic equilibrium. The comparison with existing research is non-exhaustive and priority cannot be established from negative searches; equivalent unindexed results remain possible. The numerical spectral radius printed for the seven-vertex example is illustrative, while the exact rational comparisons prove its switching behavior.

## References

- H. P. Dung and N. H. Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048, publicly submitted 15 July 2026. https://arxiv.org/abs/2607.14048
- H. Wang, Q. Li, G. D'Agostino, S. Havlin, H. E. Stanley and P. Van Mieghem, *Effect of the Interconnected Network Structure on the Epidemic Threshold*, arXiv:1303.0781, 2013. https://arxiv.org/abs/1303.0781
- F. D. Sahneh, C. Scoglio and F. N. Chowdhury, *Effect of Coupling on the Epidemic Threshold in Interconnected Complex Networks: A Spectral Analysis*, arXiv:1212.4194, 2012. https://arxiv.org/abs/1212.4194
- M. Aprahamian, D. J. Higham and N. J. Higham, *Matching Exponential-Based and Resolvent-Based Centrality Measures*, *Journal of Complex Networks* 4 (2016), 157–176. https://doi.org/10.1093/comnet/cnv016
- K. J. Sharkey, *Localization of Eigenvector Centrality in Networks with a Cut Vertex*, *Physical Review E* 99 (2019), 012315. https://doi.org/10.1103/PhysRevE.99.012315
