# Independent mathematical audit

## correctness

PASS

Reaudited the unequal-total theorem in repairs/3/RESULT.md; the original proof is also mathematically sound. The recursion comes from additions c I_j and b+(a-b) I_j and total size T_0+cj+(a+b-c)R_j. Conditioning on all rules is legitimate because the drawing uniforms are independent; it makes the future damping weights deterministic and gives a squared L² tail O(1/K) once all factors are positive. For finite λ the centered weighted Bernoulli sum has variance O(ε_N), and E[ξ_j R_j]=ε_N+(j−1)ε_N² gives the indispensable inverse-total error O(ε_N+ε_N² log N)=o(1). The sum of squares is o_P(1). For λ=∞ the deterministic upper linear bound on T_j gives divergence without this finite-window error estimate. Coupling the first K draws and then sending K to infinity proves the endpoint result with the stated initial Beta parameters. Boundedness gives the moment formulas. The recorded finite checker output was inspected, not executed; its large-row diagnostics are balanced, not evidence of convergence for unequal totals. Replay for those original diagnostics is python checker.py in the source package; the repaired proof itself needs no computation.

## originality

PASS

For the repaired unequal-total claim only. The original unqualified crossover contribution materially overlapped the Oct. 18 archive theorem: on its positive-addition balanced regime the two-colour endpoint and moments are already a consequence of that stronger path result. The repair explicitly credits that overlap and isolates c≠a+b. The prior path theorem assumes deterministic row totals and neither its statement nor its proof can be specialized by setting parameters to produce the unequal-total urn. No exact coverage of the repaired claim was established in the comparisons below.

## value

PASS

Unequal replacement totals are natural in mixed urns. They remove deterministic normalization and could alter the integrated drift; the repair proves exactly why and when that does not happen, while recovering the limiting random distribution rather than only its mean. This supplies a substantial robustness result and not a restatement of the balanced path law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
