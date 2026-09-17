# same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately as correct, original to the best of our knowledge, and useful. This is not independent validation or peer review.

## Correctness audit

The proof was attacked at the points most likely to fail:

1. **Symmetrization convention.** The generator is explicitly in column convention. Detailed balance \(L_{ij}\pi_j=L_{ji}\pi_i\) makes \(RLR^{-1}\), with \(R=\operatorname{diag}(\pi_i^{-1/2})\), symmetric. The kernel maps from \(\pi\) to \(\sqrt\pi\).
2. **Large mutation rates.** \(I+\varepsilon L\) need not be entrywise nonnegative for large \(\varepsilon\), but \((I+\varepsilon L)D(s)\) remains Metzler because only its diagonal can become negative. The Perron spectral bound remains positive because the reversible Rayleigh quotient tested on \(\sqrt\pi\) is positive.
3. **Strict substrate monotonicity.** The argument does not assume \(I+\varepsilon A\) is positive semidefinite. It uses only positivity of the maximizing quotient and strict decrease of every diagonal entry of \(D(s)^{-1}\).
4. **Critical equality.** The Lyapunov functional \(p^Tx\) has zero derivative on \(x=0\) and on the slice \(s=s_{in}\), but the latter slice is not invariant when \(x\ne0\). Boundedness plus LaSalle gives \(x\to0\), and the scalar substrate equation then gives \(s\to s_{in}\). A separate estimate proves Lyapunov stability, so the equality claim is genuinely global asymptotic stability rather than attraction alone.
5. **Equilibrium uniqueness.** Irreducible Metzler Perron--Frobenius forces any nonzero nonnegative equilibrium vector to be strictly positive and associated with the spectral bound. Strict monotonicity of that bound in substrate then gives a unique substrate level and the substrate balance gives a unique biomass scale.

A compact numerical script reproduces the motivating five-species example and checks the spectral identities on random reversible networks. The proof does not depend on those computations.

### Correctness limitations

The theorem does **not** establish local or global stability of the coexistence equilibrium for arbitrary mutation intensity. It also does not cover nonreversible mutation generators or general substrate-dependent exchange matrices.

## Originality audit

### Internal SCOPE overlap

Immediately before publication, repository searches were run for the source title/chemostat mutation language, growth-weighted chemostat terminology, reversible mutation generators, and critical dilution. No current SCOPE record covering this result was found. GitHub code search is not an exhaustive semantic index, so this is evidence against collision rather than a guarantee.

### External literature checked

- Alvarez-Latuz--Bayen--Coville, arXiv:2501.08011 / DOI 10.1016/j.nonrwa.2025.104509. The inspected preprint states that for the substrate-dependent Section 4.2 example the sufficient condition gives \(\bar\varepsilon=1/2\), says extension beyond that range is not straightforward in general, and reports only numerical verification that the relevant Perron root remains increasing in substrate for larger \(\varepsilon\). Its Proposition 3.2 gives washout stability at \(u=u_c\) and global asymptotic stability only for \(u>u_c\). Its Section 4.2 matrix is exactly the symmetric cycle specialization \(T(s)=LD(s)\).
- Bayen--Cazenave-Lacroutz--Coville, arXiv:2110.09582, treats a constant mutation matrix, not the substrate-dependent growth-weighted form here.
- Altenberg (PNAS 2012), DOI 10.1073/pnas.1113833109, proves a broad reduction phenomenon showing that increased conservative mixing lowers spectral growth. This covers the direction of the mutation-intensity effect in broad form and is therefore not claimed as new here.
- Searches for exact/synonymous formulations involving `T(s)=L D(s)`, growth-weighted/growth-dependent mutation, reversible/detailed-balance mutation matrices, critical dilution, and harmonic-mean limits did not expose a theorem giving all-rate substrate monotonicity plus the chemostat equilibrium/washout conclusions above.

### Uninspected sources and residual risk

1. **Final journal/HAL version of the motivating paper:** DOI `10.1016/j.nonrwa.2025.104509`, HAL `hal-04860652v2`. The bibliographic record was verified, but the final HAL v2 full text was not accessible through the inspected route. The accessible full text was the 2025 preprint. A later revision could contain overlapping results.
2. **Claude Lobry, *La compétition dans le chémostat* (2013), Section 4.2.** The motivating paper explicitly says its system is closely related to this section. The available record did not expose the section text, so this is the most important historical residual risk.
3. Standard reversible Markov-chain spectral theory may contain the symmetrization/Rayleigh identity in equivalent language. The record therefore does not claim novelty for that identity alone.

Given the explicit gap in the inspected primary source and the absence of located coverage after synonymous/equivalent searches, originality is assessed **PASS to the best of our knowledge**, with the residual risks above.

## Value audit

The result converts a numerical observation in a recent chemostat paper into an exact theorem for all positive mutation rates, removes a parameter restriction for that example, extends the mechanism from a cycle to arbitrary finite irreducible reversible mutation networks, and sharpens the washout threshold at equality. It also cleanly separates what is solved (threshold and washout) from the still-open all-rate stability question for coexistence. This is assessed as a substantive, reusable contribution rather than a parameter-only increment.
