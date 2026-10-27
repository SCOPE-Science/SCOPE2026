# Polyphase essential spectrum and Schatten threshold for polynomially weighted nonlinear dilations

## Finding
Fix integers \(q\ge2\), \(n\ge0\), real indices \(\beta_1,\beta_2\), and a nonzero complex polynomial \(P(z)=\sum_{j=0}^{d}p_jz^j\). For the operator
\[
(Tf)(z)=P(z)f^{(n)}(z^q):\mathcal D_{\beta_1}\longrightarrow\mathcal D_{\beta_2},
\]
put \(\Delta=\beta_2-\beta_1-2n\). For each residue \(0\le r<q\), form the polynomial
\[
P_r(\zeta)=\sum_{h\ge0}p_{r+qh}\zeta^h,\qquad H(\zeta)=\sum_{r=0}^{q-1}|P_r(\zeta)|^2,\qquad c_q=q^{(1-\beta_2)/2}.
\]
(Absent coefficients are zero.) The following trichotomy is complete:

1. **Unbounded region.** If \(\Delta<0\), \(T\) has no bounded Hilbert-space extension.
2. **Critical region.** If \(\Delta=0\), \(T\) is bounded and noncompact, with exact essential norm and essential positive spectrum
\[
\|T\|_{\mathrm{ess}}=c_q\sqrt{\max_{|\zeta|=1}H(\zeta)},\qquad
\sigma_{\mathrm{ess}}(T^*T)=
[c_q^2\min_{|\zeta|=1}H(\zeta),c_q^2\max_{|\zeta|=1}H(\zeta)].
\]
Its range is closed **if and only if** the polynomials \(P_0,\ldots,P_{q-1}\) have no common zero on the unit circle.
3. **Compact region.** If \(\Delta>0\), then \(T\) is compact. There are positive constants \(a,b\), depending on the fixed symbols and indices, such that for all sufficiently large integers \(N\),
\[
aN^{-\Delta/2}\le s_N(T)\le bN^{-\Delta/2}.
\]
Consequently, for every \(0<p<\infty\), \(T\in\mathcal S_p\) **if and only if** \(p\Delta>2\). No endpoint equality is included.

**Alias-sensitive example.** On Hardy space (\(\beta_1=\beta_2=1\), \(n=0\), \(q=2\)), both \(P(z)=1+z\) and \(P(z)=1+z^2\) have two unit coefficients. The first has \(H\equiv2\) and \(T^*T=2I\): its range is closed. The second has \(H(\zeta)=|1+\zeta|^2\) and \(\sigma_{\mathrm{ess}}(T^*T)=[0,4]\): its range is not closed. Thus polynomial residue placement, not coefficient magnitudes alone, controls the boundary lower singular-value behavior.

## Assumptions and scope
For every real \(\beta\), the precise coefficient normalization is
\[
\mathcal D_\beta=\big\{f(z)=\sum_{k\ge0}a_kz^k:\sum_{k\ge0}(k+1)^{1-\beta}|a_k|^2<\infty\big\},\qquad
\|f\|_{\mathcal D_\beta}^2=\sum_{k\ge0}(k+1)^{1-\beta}|a_k|^2.
\]
All operator assertions concern the polynomial map extended (when bounded) by continuity, not a priori an unbounded maximal-domain operator. The positive operator \(T^*T\) acts on the **source** Hilbert space. Essential spectrum means Fredholm essential spectrum, which coincides with the complement of isolated finite-multiplicity eigenvalues for this self-adjoint operator. At the critical index, \(\ker T\) consists exactly of polynomials of degree less than \(n\); for \(n=0\), its kernel is zero. The polynomial \(P\) is not allowed to vanish identically.

## Proof
**1. Coefficient reduction.** The normalized monomials are \(e_k^{(\beta)}=(k+1)^{(\beta-1)/2}z^k\). For \(\ell\ge0\), direct differentiation gives
\[
Te_{\ell+n}^{(\beta_1)}=
\sum_{j=0}^{d}p_j\frac{(\ell+n)!}{\ell!}
(\ell+n+1)^{(\beta_1-1)/2}
(q\ell+j+1)^{(1-\beta_2)/2}
e_{q\ell+j}^{(\beta_2)}.
\]
The first \(n\) input basis elements map to zero. For each fixed \(j\), the coefficient divided by \(p_j\) equals
\[
c_q\ell^{-\Delta/2}(1+O(\ell^{-1}))
\quad (\ell\to\infty).
\]
Since the finitely many output indices \(q\ell+j\) are distinct **within a given column**, its squared norm is the sum of squared displayed coefficients. Thus its norm grows unbounded when \(\Delta<0\). Conversely, if \(\Delta\ge0\), each polynomial band is a bounded weighted shift and their finite sum is bounded.

**2. Polyphase Fredholm model at the critical index.** Discard the finite-dimensional source kernel, identifying the remaining input coefficients with \(H^2\). Group each target coefficient by its exponent modulo \(q\), identifying the target with \((H^2)^q\). The summand \(j=r+qh\) becomes \(S^h\) in output component \(r\), multiplied on the right by a diagonal operator whose entries converge to \(c_qp_j\). Therefore the transformed \(T\) differs by a compact operator from \(c_q\mathcal M\), where
\[
(\mathcal Mf)(\zeta)=(P_0(\zeta)f(\zeta),\ldots,P_{q-1}(\zeta)f(\zeta)).
\]
This establishes a compact-equivalence, not an exact equality, for general Dirichlet indices and positive differentiation order. It follows that the transformed \(T^*T\) is a compact perturbation of \(c_q^2\mathcal M^*\mathcal M=c_q^2T_H\), with \(T_H\) the scalar Hardy Toeplitz operator of the real continuous trigonometric-polynomial symbol \(H\).

**3. Exact essential invariants.** Let \(m=\min_{\mathbb T}H\) and \(M=\max_{\mathbb T}H\). For every \(f\in H^2\), the quadratic-form identity
\[
\langle T_Hf,f\rangle=\int_{\mathbb T}H(\zeta)|f(\zeta)|^2\,dm(\zeta)
\]
puts its full spectrum inside \([m,M]\). Conversely, for any \(\eta\in\mathbb T\), normalized Szegő kernels approaching \(\eta\) are weakly null, and their \(L^2\) mass concentrates at \(\eta\). Because \(T_H=P_+M_H|_{H^2}\), they are approximate eigenvectors for \(H(\eta)\); hence \(H(\eta)\in\sigma_{\mathrm{ess}}(T_H)\). The continuous image \(H(\mathbb T)=[m,M]\) proves equality. Invariance under compact perturbations gives the asserted essential spectrum of \(T^*T\). The Calkin-algebra \(C^*\)-identity yields \(\|T\|_{\mathrm{ess}}^2=\|T^*T\|_{\mathrm{ess}}=c_q^2M\). Since \(P\ne0\), \(M>0\), so the critical operator is noncompact.

If \(m>0\), then \(T_H\ge mI\); the compact perturbation \(T^*T\) is Fredholm, and \(T\) has closed range. If \(m=0\), zero belongs to the essential spectrum of \(T^*T\); yet \(T\) has only the finite-dimensional differentiation kernel. A closed-range operator with finite kernel is bounded below on the orthogonal kernel complement, and its \(T^*T\) has an essential spectral gap at zero. This contradiction proves failure of closed range. The equivalence \(m>0\iff\bigcap_r\{\zeta\in\mathbb T:P_r(\zeta)=0\}=\varnothing\) is immediate.

**4. Exact Schatten threshold away from criticality.** Suppose \(\alpha=\Delta/2>0\). The output coefficient matrix has at most \(d+1\) diagonally shifted bands, each with tail coefficients bounded by \(C(\ell+1)^{-\alpha}\). Removing the first \(N\) input columns leaves an operator of norm at most \(CN^{-\alpha}\). By the Hilbert-space approximation-number definition, \(s_{N+1}(T)\le CN^{-\alpha}\). Hence \(T\) is compact.

For the reverse bound, choose a positive integer \(L\) with \(qL>d\) and retain input basis columns indexed by \(\ell=Lm\). Their output supports \(\{qLm+j:p_j\ne0\}\) are pairwise disjoint, making their images orthogonal. Every such image has norm at least \(c(m+1)^{-\alpha}\) for all large \(m\), because at least one \(p_j\) is nonzero. An \(N\)-dimensional span of consecutive sufficiently late selected columns therefore has minimum expansion at least \(c'N^{-\alpha}\). The min–max characterization of singular values gives \(s_N(T)\ge c'N^{-\alpha}\). Thus \(s_N(T)\asymp N^{-\alpha}\), and the series \(\sum_Ns_N(T)^p\) converges precisely if \(\alpha p>1\), including \(0<p<1\).

## Verification
The standalone `verify.py` computes exact polynomial residue blocks and coefficient matrices in finite Hardy examples, checks their Gram Toeplitz diagonals and predicted correlations, and numerically checks normalized coefficient asymptotics for five index choices. It completed **2,741** deterministic assertions. These are supplementary checks; no finite truncation establishes the infinite-dimensional spectral identities or Schatten threshold, which follow from the proof above.

The critical Hardy examples admit a separate direct calculation: \(f(z^2)(1+z)\) has disjoint even/odd outputs and \(T^*T=2I\); in contrast \(f(z^2)(1+z^2)\) is unitarily equivalent to multiplication by \(1+z\) with two-step embedding, giving the tridiagonal Toeplitz Gram matrix with diagonal \(2\) and adjacent entries \(1\).

## Relationship to prior work
Sun and Liu's 2026 paper, especially its Theorem 9.2, treats the same coefficient-normalized weighted Dirichlet spaces and gives exact results for **monomial weights with linear inner symbols** \(\phi(z)=\rho z\), together with broad Schatten criteria. The boundedness and Schatten exponent thresholds here share the established index-counting mechanism, and those aspects alone are not a claim of novelty. The present scope instead has **nonlinear power composition** \(\phi(z)=z^q\), arbitrary polynomial multipliers, nonorthogonal image columns, and an exact polyphase description of the essential *positive spectrum* and its closed-range boundary.

Barik, Sen and Paul treat general weighted composition–differentiation maps by Carleson/Nevanlinna methods, obtaining essential-norm estimates and Hilbert–Schmidt conditions, but not this explicit polyphase essential spectral classification. Stević and Jiang address order boundedness of polynomial differentiation composition maps, a different invariant. Pau and Pérez study essential norm, Schatten membership, and closed range for unweighted composition operators on weighted Dirichlet spaces; their results provide important qualitative context but do not directly include polynomial multipliers and differentiation between arbitrary coefficient-normalized source and target indices. The Toeplitz and finite-band operator tools used in the proof are classical.

## Limitations
This is a classification only for **integer power symbols** and **polynomial weights**; it does not provide a formula for the full spectrum of \(T\), its ordinary norm, the exact leading coefficient in the compact singular-value asymptotics, or general analytic multipliers. The compact-region estimate is two-sided comparison rather than a limit. The derivation is analytic and self-contained modulo standard Hilbert-space compact-operator, Hardy Toeplitz, and minimax principles; the finite checker is not an independent mathematical audit. Equivalent implicit formulations in historical operator or block Toeplitz literature remain a publication-priority risk.

## References
1. Jihua Sun and Junming Liu, *Weighted composition–differentiation operators on mixed-norm, derivative Hardy and F(p,q,s) spaces*, arXiv:2610.19658v1 (first public October 14, 2026), especially Section 9 and Theorem 9.2. https://arxiv.org/abs/2610.19658
2. Somdatta Barik, Anirban Sen and Kallol Paul, *Composition-differentiation operators on weighted Dirichlet spaces*, arXiv:2605.00213v1 (first public April 30, 2026). https://arxiv.org/abs/2605.00213
3. Stevo Stević and Zhi-jie Jiang, *Order bounded polynomial differentiation composition operators between weighted Dirichlet spaces*, Journal of Inequalities and Applications 2026, article 65 (April 2, 2026). https://doi.org/10.1186/s13660-026-03469-w
4. Jordi Pau and Patricio A. Pérez, *Composition operators acting on weighted Dirichlet spaces*, Journal of Mathematical Analysis and Applications 401 (2013), 682–694. https://hdl.handle.net/2445/96788
