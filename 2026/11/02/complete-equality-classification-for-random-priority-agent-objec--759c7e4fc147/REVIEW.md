# Scientific assessment

## Correctness — PASS

The result concerns a finite domain of exactly \(24^4=331{,}776\) labeled strict rankings with outside options. An auditable C++17 verifier enumerates every profile and all 24 priorities with integer arithmetic, determines all agent and object unassignment marginals, evaluates each acceptable pair, and checks both the exact waste histogram and all six complete symmetry orbits. It also verifies unique maximizing pairs and the six normal forms. An independently implemented Python verifier uses a different simulation representation and an exactly justified sixfold object-label quotient of 55,296 profiles, reproduces the histogram and proves the common priority-by-priority outcome pattern. No extrapolation from a finite sample to a larger domain is made. Critical cases, the empty acceptable set, and the outside-option cutoff are handled explicitly.

## Originality — PASS, with publication-priority caveat

Basteck and Ehlers (2026), *Strategy-Proof and Minimally Wasteful Random Assignment*, Section 3 and Appendix B, explicitly prove the sharp \(1/6\) RSD bound and show an example with four agents and three objects. Those facts are **known**, not novel. Inspection of their full accessible text found an upper-bound argument and one witness, but not the complete orbit-normal-form classification, the count of equality profiles, the full histogram or the unique extremal pair statement. Searches of related random-assignment work and published mathematical records did not reveal a statement implying this classification. The exact-priority probability enumerations, rather than keyword/title differences, are the basis of the comparison. There remains a risk of unindexed earlier finite calculations or alternate naming.

## Value — PASS

A sharp worst-case efficiency bound alone leaves open which markets attain it and how robustly. The answer is unusually restrictive here: only six symmetry classes, exactly \(1/768\) of labeled full-domain profiles under impartial culture, a unique triggering pair, and six different rankings sharing exactly the same random assignment lottery even priority by priority. This identifies the entire equality boundary of a natural scarcity-induced efficiency defect rather than producing another instance of the already known worst case. It supplies interpretable representative markets and an exact benchmark for finite random-assignment implementations.

## Scope and residual scientific risks

The enumeration is complete only for four agents and three objects; no larger-market conclusion follows. The probability measure \(1/768\) presumes independent uniform strict full-domain rankings. Publication-priority verification cannot exclude an unindexed exact classification. The available text of Martini (2016) was not fully inspected, although the directly relevant recent primary article was read in its definitions, result, and proof sections.

Self-review: passed. Independent audit: not yet performed.
