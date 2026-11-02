# Scientific review of the constrained deletion-packing profile

## Correctness — PASS

The finite theorem is supported by a complete, exact certificate at every length from one to seven. The integer lower bounds are explicit codes checked by deletion-shadow disjointness. At lengths one through five, equally sized deletion-output transversals give matching upper bounds. At lengths six and seven, rational primal and dual shadow-packing certificates prove fractional optima four and six, and weighted conflict-clique covers of total weight \(15/4\) and \(23/4\) establish strict integer upper bounds four and six, respectively. Every required clique adjacency and covering inequality is reconstructed from source words by `artifacts/verify.py`; the separate `artifacts/census.py` independently computes all seven finite integer optima. Both programs passed their current-package executions. Nothing outside the finite range is claimed.

## Originality — PASS (with historical-priority risk)

The primary full text of Kulkarni–Kiyavash, arXiv:1211.3128, Sections V–VI, concerns general constrained-source fractional bounds and a run-length-limited family with endpoint restrictions, not the exact integer/fractional profiles of binary words avoiding `11` with free endpoints. The unrestricted table there cannot yield these numerical equalities. The primary full text of Cullina–Kulkarni–Kiyavash, arXiv:1211.4056, treats full and constant-weight deletion graphs and coloring constructions, not this simultaneous Fibonacci-source matching profile. Search comparisons for constrained deletion codes, equivalent formulations, bounds, and finite tables did not reveal an identical or logically dominating result. Bours (1994), Cheng et al. (2012), and Palunčić et al. (2012) remain abstract-level comparisons only, so uninspected historical results remain a genuine priority risk. Absence of a retrieved duplicate is not a claim of exhaustive literature coverage.

## Value — PASS

The question is directly motivated by the fractional-transversal methodology for single-deletion codes with run-length constraints. Unlike an arbitrary finite slice, the first loss of exactness of that natural relaxation is an intrinsic boundary: the fractional optimum exceeds the integral code capacity by a factor \(4/3\) at the earliest possible length, and a second exact discrepancy at the next length shows the obstruction is not an isolated numerical artifact. The finite certificates show precisely which kind of additional conflict-clique inequalities are needed beyond individual deletion-output capacities. They provide a reproducible benchmark for constrained synchronization coding and relaxation design, without claiming an asymptotic advance.

## Closest literature and limitations

Relevant primary papers are cited in `RESULT.md`. The claim does not cover longer source lengths, different endpoint restrictions, or independent historical validation. Some older construction papers could not be assessed from full text.

Self-review: passed. Independent audit: not yet performed.
