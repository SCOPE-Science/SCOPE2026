# Review status

Mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The proof correctly separates optimal labelings according to whether a whole part is positive. In the full-positive-part case, totality and the defender requirement force the one-part strategy \(A=m+1+\lceil(N-m-1)/2\rceil\). Otherwise every zero vertex must see a positive defender outside its part; reducing to two defender parts yields the exact integer minimization in the package, and the one-unit saving occurs precisely in the stated odd--odd parity case when a third non-singleton part supplies the needed positive neighbor. Explicit constructions attain both lower bounds. A separate direct label enumeration agrees with the formula on representative small multipartite graphs, while the repository verifier exhausts all part-size types through the stated ranges.

Originality: PASS. The complete 19-page Nazari-Moghaddam--Soroudi--Sheikholeslami--Yero paper introducing total strong Roman domination was inspected. It establishes general bounds, characterizes several equality cases, and studies trees, but gives no complete-multipartite exact formula. Targeted searches for total strong Roman domination plus complete multipartite graphs found the introducing paper and neighboring variants, but no prior theorem matching the assigned parity-sensitive formula. Resultary likewise returned the assigned theorem as the exact match.

Scientific value: PASS. Complete multipartite graphs are a standard test class for domination parameters, and the optimum is not a single immediate degree bound: it has two competing structural strategies and a genuine parity correction controlled by a third non-singleton part. The closed formula covers complete graphs, stars, bicliques and all multipartite orders uniformly.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
