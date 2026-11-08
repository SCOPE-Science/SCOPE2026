# Independent mathematical audit

## correctness

PASS

PASS. The area-preserving change t=(x-y) mod 1 and s=min(t,1-t) reduces consecutive visits to A3 to two equal-length vertical fiber families. The exact first-visit interval has length 1/2-s, giving S1=1/4. Two-step dynamics preserves t and translates y by ±(1-4s) mod1. The explicit two-visit intervals and restriction from four visits rule out additional mod-one wraps, so repeated intersection successively clips one endpoint: the even/odd surviving widths are triangular with apex 1/4 and roots ((k-1)/(4k-3), k/(4k-1)) and ((2k-1)/(2(4k-1)),(2k+1)/(2(4k+1))) respectively. Both sides contribute equally; triangle integration yields S_2k=(2k-1)/(4(4k-1)(4k-3)), S_(2k+1)=k/(2(16k²-1)), hence n S_n→1/16. Initial A3 probability 1/4 gives Pr(tau>=n)=4S_n, first exit =4(S_n-S_(n+1)), divergent mean. Boundary/singularity fibers are null. Independently checked 98 rational triangle/base area identities; examined the original-map integer grid comparator for up to 13 visits. Exact all-n result rests on the fiber-induction proof, not numerical agreement.

## originality

PASS

PASS, qualified by strong same-model antecedent. Myers Hill–Sturman–Wilson 2023 treat the identical neutral branch A3 in this toral shear map, partition escape times into cells A^k with explicit boundary lines (Section 3/Figure 5, appendix), and obtain 1/n correlation-order obstructions via triangular wedges (Section 6.2). Their paper therefore already supplies essential geometry; it does NOT follow just from O(1/n) that the exact global survivor area has the two parity formulas or asymptotic coefficient 1/16. The inspected text evaluates wedges restricted to a subannulus for correlation lower bounds, not the complete two-sided surviving A3 fiber measure for every n. The assigned proof makes the all-branch integration and first-exit distribution explicit. The prior polygon partition may facilitate a shorter derivation and is a substantive possibility of corollary coverage, expressly retained as a risk.

## value

PASS

PASS. Consecutive trapping survival in a parabolic neutral branch is a natural dynamical invariant of a known polynomial-mixing map. Complete finite-time parity formulas, the exact 1/16 tail coefficient and divergent conditional mean sharpen the previously established escape partition/correlation-rate geometry and could be used as precise renewal-tail inputs. Does not claim a new global mixing theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
