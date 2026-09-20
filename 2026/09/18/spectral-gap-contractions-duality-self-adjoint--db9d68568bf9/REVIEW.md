# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof is self-contained apart from standard compact-operator Riesz theory.

The duality identity immediately gives
\[
\|Tx\|^2=J(Tx)(Tx)=Jx(T^2x)\le\|x\|\,\|T^2x\|,
\]
hence \(\|T^2\|=\|T\|^2\). Powers remain duality-self-adjoint, so the spectral-radius formula yields \(r(T)=\|T\|\). Eigenvalues are real by conjugate homogeneity of \(J\). A length-two Jordan chain at a nonzero eigenvalue contradicts \(Ju(u)=\|u\|^2\), so nonzero spectral values are semisimple.

For a nonzero eigenvalue \(\lambda\), the Riesz complement \(N_\lambda\) satisfies \(\lambda\notin\sigma(T|_{N_\lambda})\). If \(x=m+z\), with \(m\in E_\lambda\) and \(z\in N_\lambda\), invertibility of \(T-\lambda I\) on \(N_\lambda\) shows \(Jm(z)=0\). This proves \(\|P_\lambda\|=1\).

For an outer finite spectral set \(F\), if the residual spectral radius is strictly smaller than every \(|\lambda|\), then for \(z\) in the residual and \(m_\lambda\in E_\lambda\),
\[
\lambda^kJz(m_\lambda)=J(T^kz)(m_\lambda).
\]
The spectral gap forces \(Jz(m_\lambda)=0\). Hence the residual projection is contractive. Restricting to that residual preserves smoothness and duality self-adjointness, so its norm equals its spectral radius. This yields the exact tail norm. The only possible equal-modulus tie is the real pair \(a,-a\); individual Riesz projections are contractive, giving the stated bounds \(3\) for the norm-greedy partial spectral projections and \(2\rho_n\) for the remainders.

Hidden-hypothesis checks were made for complex conjugate homogeneity, smoothness inheritance by closed subspaces, compactness of restrictions, semisimplicity, and the distinction between an arbitrary Auerbach complement and a canonical invariant spectral complement.

## Originality

**PASS, to the best of our knowledge.** The recent preprint arXiv:2608.06873v1 states the compact duality-self-adjoint spectral expansion. A detailed public review identifies the infinite-dimensional convergence step as unproved because it assumes contractivity or uniform boundedness of residual projections and gives an unrelated smooth-space Auerbach example showing that such contractivity is not automatic.

Targeted searches were made for the arXiv identifier and for synonymous combinations of duality mappings, self-adjoint operators, Riesz/spectral projections, contractive projections, spectral gaps, semisimple eigenvalues, and compact spectral expansions. No source located the spectral-gap argument above, the contractivity of each nonzero Riesz projection in this setting, or the exact modulus-block tail formula. No SCOPE record matched the source paper, claim family, or terminology at the time of the overlap check.

The closest older literature is García-Pacheco's work defining and studying this self-adjointness notion. The 2024 open-access article was inspected for the normalized duality-map conventions and adjoint definition. The 2020 article *Selfadjoint operators on real or complex Banach spaces* is a material residual originality risk because it develops spectral properties of the same operator class; its abstract was inspected but its full text was not. The primary abstract of arXiv:2608.06873v1 was inspected, while theorem-level proof details and the specific convergence objection were inspected through detailed public secondary renderings rather than a directly inspected primary full text.

The originality claim is deliberately narrow: it does not claim the spectral theorem itself, the equality \(r(T)=\|T\|\), or the basic duality-map framework as new. It claims the spectral-gap contraction mechanism, the projection/tail estimates, and the resulting repair of the reported convergence gap.

## Value

**PASS.** The result addresses a load-bearing issue in a recent claimed Banach-space spectral theorem rather than adding a routine parameter variation. It identifies why a generic Auerbach counterexample does not decide the operator-generated case: invariance plus a spectral gap forces one-sided dual orthogonality. The theorem also gives stronger quantitative information than mere convergence, namely contractive nonzero spectral projections, contractive completed-block residuals, uniformly bounded norm-greedy partial projections, and exact remainder norms at completed modulus levels.

## Limitations

The result is specific to self-adjointness defined by \(T^*J=JT\). It does not imply that arbitrary Auerbach residual projections in smooth Banach spaces are contractive.

Exact remainder norms are asserted only after complete modulus blocks. If both \(a\) and \(-a\) occur, an intermediate one-eigenvalue partial sum is controlled by a factor-two estimate instead.

The full text of García-Pacheco's 2020 paper was not inspected and remains the principal older prior-coverage risk. The primary full text of arXiv:2608.06873v1 was also not directly inspected; claims about the specific gap are tied to detailed public reviews of that version. A later revision of the preprint could independently add a repair.
