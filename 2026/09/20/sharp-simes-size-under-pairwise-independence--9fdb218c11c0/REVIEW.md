# Review status

Scientific audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The Simes event depends only on the four interval labels \(A,B,C,D\) with widths \(r,r,r,1-3r\), where \(r=lpha/3\). Pairwise independence fixes all ten second factorial moments of the occupancy counts. The three displayed dual coefficient vectors were independently checked on all 20 occupancy types and give the three polynomial upper bounds. The three exchangeable count distributions were independently rechecked for normalization, all ten pair laws and their rejection polynomials. Conditional independent uniform draws inside the assigned intervals then produce exactly uniform continuous marginals while preserving pairwise independence. The branch crossings occur at \(r=1/5\) and \(r=1/4\), giving the stated \(lpha=3/5\) and \(lpha=3/4\) breakpoints. This is a finite exact certificate embedded in a complete probabilistic reduction, not a heuristic computation.

Originality: PASS. Simes proves exact size under mutual independence. Hommel's complete 1983 paper was inspected in full: its arbitrary-dependence sharp method uses harmonic-adjusted ordered critical levels, not the unadjusted Simes event under pairwise independence. Samuel-Cahn studies anticonservativeness under dependence classes but does not provide the pairwise-independent three-uniform envelope in its accessible statement. Ramachandra--Natarajan's complete arXiv paper gives sharp or improved bounds for single-threshold sums of pairwise-independent Bernoulli variables; it does not treat the multilevel Simes rejection event. No inspected source states or implies the assigned piecewise envelope.

Scientific value: PASS. Pairwise independence is a natural intermediate dependence model, and the theorem exactly quantifies how far a canonical multiple-testing procedure can exceed nominal level in the smallest nontrivial case. The exact sharp envelope and continuous extremizers are reusable in limited-independence multiple testing and are not a routine numerical check.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
