# Scientific review

**Correctness (PASS).** The exact Radau IIA stability polynomial produces the stated rational graph update. Symmetry reduces each finite case to an exact polynomial quotient; all numerator/denominator coefficient signs for cycle orders three through nine and noncritical ten-cycle entries have been checked against the embedded full certificate by an independently replayable symbolic program. The opposite-pair ten-cycle numerator is an explicit positive multiple of one sign-changing quintic, proving its unique root; the value at one tenth is a strict negative rational. For all larger cycles the first nonzero Taylor term at graph distance five is negative, while the large-step spectral limit is positive. Finite calculations are not used to infer arbitrary-order claims.

**Originality (PASS, bibliographic risk remains).** Zappavigna–Colaneri–Kirkland–Shorten's Padé-positivity theory concerns diagonal approximants and general sufficient conditions, not the present exact two-stage Radau cycle threshold. Related cycle calculations for fourth-order Gauss methods involve a different stability function and cannot imply the present ten-vertex or reentry statements. Indexed findings about generic Padé and SSP methods concern other rational maps or graph classes. No covering statement was found in the checked material; a historically unindexed Radau-cycle equivalence is possible.

**Value (PASS).** The threshold reveals that making the timestep smaller can *destroy* entrywise positivity for a stable, third-order implicit method on an elementary diffusion network, while increasing it restores positivity. The first failing graph order, unique exact ten-cycle reentry threshold, and infinite family of small-step obstructions give a useful and motivated boundary for structure-preserving numerical integration.

**Limits.** Only completed-step matrices on unweighted cycles are analyzed. The exact complete set of safe steps for cycle orders greater than ten remains open here. The finite certificate uses exact symbolic algebra and its source is supplied. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
