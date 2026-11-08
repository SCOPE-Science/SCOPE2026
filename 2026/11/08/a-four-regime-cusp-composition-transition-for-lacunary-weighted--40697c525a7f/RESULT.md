# A four-regime cusp-composition transition for lacunary weighted Hardy spaces

## Finding

Fix real \(0<\theta<1\), an integer \(b\ge 2\), real \(\alpha>0\) and \(\gamma\in\mathbb R\), and write \(\kappa=1/\theta\). Define \(N_j=b^j\), \(j\ge1\), and the coefficient weights
\[
\beta_n=\begin{cases}
\min\{1,N_j^{-\alpha}[\log(e+N_j)]^{-\gamma}\},&n=N_j,\\
1,&n\notin\{N_j:j\ge1\}.
\end{cases}
\]
On the complex Hilbert space \(H^2(\beta)\), the analytic composition symbol \(\psi_\theta(z)=1-(1-z)^\theta\), with the principal analytic branch, has the following **complete classification**:

- **Hilbert–Schmidt:** \(\alpha<\kappa\) (any \(\gamma\)), or \(\alpha=\kappa\) and \(\gamma<-1\).
- **Compact but not Hilbert–Schmidt:** \(\alpha=\kappa\) and \(-1\le\gamma<0\).
- **Bounded but noncompact:** \(\alpha=\kappa\) and \(\gamma=0\).
- **Unbounded:** \(\alpha>\kappa\) (any \(\gamma\)), or \(\alpha=\kappa\) and \(\gamma>0\).

In the unbounded cases, composition on polynomials has no bounded extension to \(H^2(\beta)\). Define the positive constant
\[
A_\theta=\frac{\Gamma(1+1/\theta)}{\pi[2\cos(\pi\theta/2)]^{1/\theta}}.
\]
At the bounded/noncompact endpoint, \(\|C_{\psi_\theta}\|_{\mathrm{ess}}\ge\sqrt{A_\theta}\). The two Hilbert–Schmidt blow-up boundaries have **exact residues**:
\[
\lim_{\alpha\uparrow\kappa}(\kappa-\alpha)\,
 \|C_{\psi_\theta}:H^2(\beta_{\alpha,0})\to H^2(\beta_{\alpha,0})\|_{S_2}^{2}
 =\frac{A_\theta}{\log b},
\]
\[
\lim_{\gamma\uparrow-1}(-1-\gamma)\,
 \|C_{\psi_\theta}:H^2(\beta_{\kappa,\gamma})\to H^2(\beta_{\kappa,\gamma})\|_{S_2}^{2}
 =\frac{A_\theta}{\log b}.
\]
The limits approach the indicated boundaries from their Hilbert–Schmidt side. No exact formula for the endpoint essential norm is claimed.

## Assumptions and scope

The inner product of \(H^2(\beta)\) is defined by
\[
\Big\|\sum_{n\ge0}a_n z^n\Big\|_\beta^2=\sum_{n\ge0}\beta_n|a_n|^2.
\]
All indices are nonnegative integers; the exceptional levels start at \(j=1\), and \(\log\) is the natural logarithm. Since \(\log\beta_n=o(n)\), every element defines a holomorphic function on the unit disk and polynomials are dense. The operator \(C_{\psi_\theta}\) initially maps polynomials by \(f\mapsto f\circ\psi_\theta\). Since \(1-(1-z)^\theta\) has strictly positive Taylor coefficients whose sum is one, \(\psi_\theta(0)=0\) and \(\psi_\theta\) is an analytic disk self-map. All bounded extensions agree with pointwise composition.

The spaces are complex, and the classification concerns this single explicit symbol, not all disk self-maps or all Schatten exponents. No monotonicity of the coefficient weights is assumed.

## Proof

**1. Precise boundary-power norms.** Set \(U_n=\|\psi_\theta^n\|_{H^2}^2\) for \(n\ge1\). Positivity of the symbol's Taylor coefficients shows that \(|\psi_\theta(e^{it})|<1\) away from \(t=0\). At the unique boundary contact,
\[
1-|\psi_\theta(e^{it})|^2
=2\cos(\pi\theta/2)|t|^\theta+o(|t|^\theta).
\]
The normalized boundary integral and dominated Laplace scaling give
\[
U_n=\frac1{2\pi}\int_{-\pi}^{\pi}|\psi_\theta(e^{it})|^{2n}\,dt
\sim A_\theta n^{-\kappa},\qquad
\|\psi_\theta^n\|_{H^1}=O(n^{-\kappa}).\tag{1}
\]
Indeed, \(\int_0^\infty e^{-u t^\theta}\,dt=\Gamma(1+1/\theta)u^{-1/\theta}\) for \(u>0\). The contact is unique, so the part of the integral away from zero decays exponentially. As \(\kappa>1\), \(\sum_{n\ge1}U_n<\infty\).

**2. Output weights do not change the leading term.** Let \(V_n=\|\psi_\theta^n\|_\beta^2\). Paley's lacunary coefficient theorem says that for fixed \(b\ge2\), every \(h\in H^1\) satisfies
\[
\sum_{j\ge1}|\widehat h(N_j)|^2\le C_b\|h\|_{H^1}^2.
\]
Because all \(0<\beta_n\le1\), and only the exceptional coefficients are reweighted, (1) yields
\[
0\le U_n-V_n\le\sum_{j\ge1}
 |\widehat{\psi_\theta^n}(N_j)|^2
\le C_b\|\psi_\theta^n\|_{H^1}^2=O(n^{-2\kappa}).\tag{2}
\]
The implicit bound is independent of \(\alpha,\gamma\). Therefore
\[
V_n=A_\theta n^{-\kappa}(1+o(1))\tag{3}
\]
uniformly over the full family of weights. For the normalized input monomial \(e_n=z^n/\sqrt{\beta_n}\), its image has squared norm \(\beta_n^{-1}V_n\).

**3. Hilbert–Schmidt classification and residues.** For an operator between Hilbert spaces, its squared Hilbert–Schmidt norm is the sum of squared image norms of any orthonormal basis. Thus
\[
\|C_{\psi_\theta}\|_{S_2}^2
=\sum_{n\ge0}\beta_n^{-1}V_n,\tag{4}
\]
interpreted as \(+\infty\) if the series diverges. The contribution from \(n\notin\{N_j\}\) is at most \(1+\sum_{n\ge1}U_n<\infty\). Beyond finitely many exceptional levels, (3) gives
\[
\beta_{N_j}^{-1}V_{N_j}
\sim A_\theta b^{j(\alpha-\kappa)}
 [\log(e+b^j)]^\gamma
\sim A_\theta b^{j(\alpha-\kappa)}(j\log b)^\gamma.
\tag{5}
\]
Consequently (4) converges precisely for \(\alpha<\kappa\), or \(\alpha=\kappa,\gamma<-1\); convergence produces a bounded Hilbert–Schmidt extension, and therefore compactness. To compute the first limit, multiply the exceptional sum at \(\gamma=0\) by \(\varepsilon=\kappa-\alpha\) and use (2) and the Abelian geometric-sum limit
\[
\lim_{\varepsilon\downarrow0}\varepsilon\sum_{j\ge1}b^{-j\varepsilon}
=\frac1{\log b}.
\]
For the second, use the analogous Dirichlet-series limit
\[
\lim_{\delta\downarrow0}\delta\sum_{j\ge1}(j\log b)^{-1-\delta}
=\frac1{\log b}.
\]
The uniform error in (2), together with the parameter-independent asymptotic of \(U_n\), justifies both passages; the ordinary-coordinate contributions vanish after multiplication by the small parameters.

**4. Boundedness on the critical power line.** Fix \(\alpha=\kappa,\gamma=0\), and split the input orthogonally into the closed span \(E\) of exceptional monomials and its orthogonal complement \(F\). On \(F\) the source norm is the ordinary \(H^2\) norm. Littlewood subordination (here \(\psi_\theta(0)=0\)) makes \(C_{\psi_\theta}:F\to H^2\) bounded; in fact this restriction is Hilbert–Schmidt since \(\sum_{n\notin\{N_j\}}U_n<\infty\). On \(E\) the normalized images in \(H^2\) are
\[
g_j=b^{j\kappa/2}\psi_\theta^{b^j}.
\]
By (1), with \(n\) replaced by \((b^j+b^k)/2\), there is a finite constant \(C\) such that
\[
|\langle g_j,g_k\rangle_{H^2}|
\le C\frac{(b^jb^k)^{\kappa/2}}{(b^j+b^k)^\kappa}
\le C b^{-\kappa|j-k|/2}.\tag{6}
\]
Each row and column of this Gram matrix has a uniformly summable absolute majorant; the Schur test gives a bounded synthesis map \(E\to H^2\). Since \(\|h\|_\beta\le\|h\|_{H^2}\) for every \(h\in H^2\), both parts also map boundedly to the weighted target. This proves critical-line boundedness at \(\gamma=0\). For \(\gamma<0\), outside finitely many exceptional coordinates the images of normalized input monomials are \([\log(e+b^j)]^{\gamma/2}g_j\); this factor is uniformly bounded, so the same argument proves boundedness.

**5. Compactness and obstruction.** At \(\alpha=\kappa,\gamma<0\), the factors \([\log(e+b^j)]^{\gamma/2}\) tend to zero. Hence the exceptional-input operator factors as a compact diagonal on \(\ell_2\) followed by the bounded synthesis map of step 4; the complement restriction remains Hilbert–Schmidt. Thus the full operator is compact. At \(\gamma=0\), the normalized exceptional monomials are an orthonormal, weakly null sequence, but (3) gives their image norms squared tending to \(A_\theta>0\). Therefore \(C_{\psi_\theta}\) is not compact and its essential norm is at least \(\sqrt{A_\theta}\). When \(\alpha>\kappa\), or when \(\alpha=\kappa,\gamma>0\), (5) shows that the norms of these unit input vectors tend to infinity, excluding any bounded extension. The divergence of (4) gives the remaining non-Hilbert–Schmidt assertions. Together these steps exhaust the stated parameter range.

## Verification

The companion `check_finite.py` performs 817 finite assertions involving exact rational Taylor recurrences for \(\theta=1/2\), convolution identities, finite partial norm comparisons, boundary scaling and geometric/logarithmic endpoint checks. Run it with `python check_finite.py`; expected output is `CUSPIDAL_LACUNARY_FINITE_OK 817`. Its checks are supplementary only: (1)–(6), Paley's lacunary inequality and the compactness argument provide the infinite-dimensional proof. Numerical truncation is not used to infer infinite tail convergence.

## Relationship to prior work

Cruz-Zamorano, Dellepiane and Seco's 2026 article establishes broad equalities of compact and Hilbert–Schmidt composition-symbol *classes* for lacunary coefficient-weighted Hardy spaces, notably Theorem 1.3; it also makes fundamental use of Paley's lacunary coefficient theorem. In contrast, the result here concerns one explicitly prescribed fractional-cusp symbol and obtains a complete, symbol-specific four-regime answer with the sharp transition at \(\alpha=1/\theta\), compact/non-Hilbert–Schmidt intermediate range and two exact residues. A statement that classes of symbols are unequal at some weight does not imply the behavior of this particular symbol. Older studies of lens-symbol composition and of multiplying a composition operator by an analytic weight concern different operators/spaces and do not directly provide (1)–(6). The Paley estimate, Laplace integral and Schur test are established tools, not claimed as new.

## Limitations

This is a concrete symbol-specific theorem for a coefficient-weighted Hilbert space; it does not classify all composition symbols, determine exact essential norms at the noncompact endpoint, or determine \(S_p\) membership for \(p\ne2\) in the compact/non-Hilbert–Schmidt regime. The construction assumes geometric exceptional frequencies and real \(0<\theta<1\). The checked literature does not establish publication priority; a general older kernel/Carleson or cusp-composition theorem might imply part of the result under an equivalent formulation. No independent mathematical audit has been performed.

## References

1. F. J. Cruz-Zamorano, E. Dellepiane, and D. Seco, *Compact and Hilbert–Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1 (first publicly posted October 29, 2026), https://arxiv.org/html/2610.40148v1, particularly Sections 1, 4 and 6.
2. R. E. A. C. Paley, *On the lacunary coefficients of power series*, Ann. of Math. (2) **34** (1933), 615–616 (lacunary \(H^1\)-coefficient inequality, quoted as Theorem 4.1 of reference 1).
3. P. Lefèvre, D. Li, H. Queffélec, and L. Rodríguez-Piazza, *Compactification, and beyond, of composition operators on Hardy spaces by weights*, arXiv:1904.06992 (2019), https://arxiv.org/abs/1904.06992.
4. P. Lefèvre, D. Li, H. Queffélec, and L. Rodríguez-Piazza, *Some new properties of composition operators associated with lens maps*, arXiv:1201.0636 (2012), https://arxiv.org/abs/1201.0636.
