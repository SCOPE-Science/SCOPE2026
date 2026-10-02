# Independent mathematical audit — 2026-10-01

## Final claim

At the specified Heun point, the normalized equation has differential Galois group \(SL_2(\mathbb C)\); the original equation has group \(\mu_3\cdot SL_2(\mathbb C)=\{g:\det(g)^3=1\}\), so the equation is non-Liouvillian and not dihedral.

## Correctness — PASS

Direct normalization gives \(r=-2(z^2+1)^2/(9z^2(z-1)^2(z+1)^2)\). At \(0,1,-1,\infty\), the double-pole coefficient is \(-2/9\). Kovacic Case 1 has local alpha values \(1/3,2/3\) and maximum candidate degree \(-1/3\); Case 2 has the sole degree \(-2\); the Case 3 necessary sets likewise have negative degree bounds, so all Liouvillian cases are excluded and the normalized group is \(SL_2(\mathbb C)\). For the original equation, the Wronskian is proportional to \(D^{-2/3}\) with \(D=z(z^2-1)\); if \(a^3=D\), then the original Picard–Vessiot field contains \(a=D a^{-2}\), and conversely adjoining \(a\) to the normalized field recovers original solutions. Connectedness of \(SL_2\) gives linear disjointness from the cubic algebraic extension, yielding the stated determinant-\(\mu_3\) extension.

## Originality — PASS

Exact-parameter searches and the published-record semantic search found no prior statement for this Heun point beyond the record itself. Kovacic's 1986 algorithm supplies the general classification and necessary degree tests, but it does not tabulate this point or recover the original equation's cubic determinant character. The exact original-group calculation therefore requires a field-specific normalization, complete case elimination, and Picard–Vessiot descent not supplied by the general algorithm.

### Equivalent formulations

Equivalent formulations as absence of Liouvillian solutions or failure of Kovacic Cases 1–3 agree for the normal form; the original-group determinant statement adds information beyond this equivalence.

### Broader coverage

The general theorem does not supply the local data, degree eliminations, or the \(\mu_3\) determinant extension for this operator without the audited specialization.

### Exact database or table

Search failure is not proof of novelty, so an unindexed classical special-function table remains a residual risk.

### Claim versus prior implication

The prior algorithm makes the computation systematic but does not mechanically state the original equation's exact determinant-restricted group; that field-extension step is specific to the cubic gauge.

## Scientific value — PASS

The point has a natural symmetric placement of singularities and equal one-third finite local data. Determining the full group, while carefully distinguishing the \(SL_2\) normal form from the nontrivial determinant character of the original equation, is an exact invariant of a natural special Heun operator and prevents a common normalization error.

## Sources inspected

- **Jerald J. Kovacic, An algorithm for solving second order linear homogeneous differential equations** — https://doi.org/10.1016/S0747-7171(86)80010-4. GENERAL_ALGORITHM_NOT_EXACT_POINT: The paper gives the decision procedure but no table or theorem for the audited Heun parameters.
- **Published record search for differential-Galois Heun calculations** — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE004. NO_STRONGER_COVERING_RECORD: Related records concern different operators or parameters.

## Checked evidence

- Assigned RESULT.md and artifacts/kovacic_verdict.py from the exact Git tree.
- Fresh symbolic normalization and all local double-pole coefficients.
- Independent field/Wronskian argument for the original Picard–Vessiot group.
- Kovacic primary source and published-record semantic search.

## Residual risks

- No exhaustive historical Heun table was located; originality is best-knowledge.
- The Case 3 exclusion was checked against the degree-bound logic in the assigned proof and Kovacic framework, rather than by searching for a closed-form solution numerically.

## Disposition

**passed**
