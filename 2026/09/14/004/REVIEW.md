# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: **PASS**. Direct normalization gives \(r=-2(z^2+1)^2/(9z^2(z-1)^2(z+1)^2)\). At \(0,1,-1,\infty\), the double-pole coefficient is \(-2/9\). Kovacic Case 1 has local alpha values \(1/3,2/3\) and maximum candidate degree \(-1/3\); Case 2 has the sole degree \(-2\); the Case 3 necessary sets likewise have negative degree bounds, so all Liouvillian cases are excluded and the normalized group is \(SL_2(\mathbb C)\). For the original equation, the Wronskian is proportional to \(D^{-2/3}\) with \(D=z(z^2-1)\); if \(a^3=D\), then the original Picard–Vessiot field contains \(a=D a^{-2}\), and conversely adjoining \(a\) to the normalized field recovers original solutions. Connectedness of \(SL_2\) gives linear disjointness from the cubic algebraic extension, yielding the stated determinant-\(\mu_3\) extension.

Originality: **PASS**. Exact-parameter searches and the published-record semantic search found no prior statement for this Heun point beyond the record itself. Kovacic's 1986 algorithm supplies the general classification and necessary degree tests, but it does not tabulate this point or recover the original equation's cubic determinant character. The exact original-group calculation therefore requires a field-specific normalization, complete case elimination, and Picard–Vessiot descent not supplied by the general algorithm.

Scientific value: **PASS**. The point has a natural symmetric placement of singularities and equal one-third finite local data. Determining the full group, while carefully distinguishing the \(SL_2\) normal form from the nontrivial determinant character of the original equation, is an exact invariant of a natural special Heun operator and prevents a common normalization error.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
