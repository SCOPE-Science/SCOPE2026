# Scientific review: sharp bounded-depth process fidelity for two-axis qubit compilation

## Correctness — PASS
The colatitude cap at each tilt depth follows from the spherical triangle inequality and an inductive half-turn construction; the rightmost free phase lifts any reachable Bloch ray to its entire special-unitary stabilizer fiber. The process-fidelity maximization is then the nearest-ray problem for a spherical cap. Haar Bloch colatitude density yields the full distribution and mean; exact Taylor expansion yields the quartic coefficient. The analytic proof covers all stated parameters. The standalone numerical program passed 90 finite assertions and does not replace the universal proof.

## Originality — PASS (best knowledge)
Garbaravičius–Wolf (2026) analyzes the number of switches needed to reach every unitary, and averages over randomly drawn control bases. Hamada (2014) gives a stronger pointwise exact-synthesis factor-count theorem and provides the geometric cap ingredient, which is **acknowledged prior work**. The present object is the exact optimal **process fidelity at insufficient fixed tilt depth** and its Haar-target probability law; these were not found as assertions or stronger coverage in the inspected sources. Aiello et al. (2015) optimizes execution time of exact control words; Peterson et al. (2022) studies a different two-qubit gate set. Six direct published-finding corpus semantic queries and related aliases returned no matching equivalent claim. The closest indexed items concern sampled bang switches, a different Hadamard architecture, and robust multi-copy qubit discrimination. Residual risk is an unlocated general geometric fidelity theorem or derivation using Hamada's exact control synthesis.

## Value — PASS
A fixed budget of tilted-axis pulses is a motivated quantum-control resource, and process fidelity is the directly relevant performance observable for targets outside the reachable set. The complete target law and a sharp quartic mean-versus-quadratic worst-case error distinction quantify a nonobvious practical difference between typical and worst-target compilation. These are exact natural invariants of a standard alternating control architecture, not an arbitrary finite census.

## Limitations and closest literature
The result assumes unrestricted ideal signed pulse angles and first-axis gates at both ends. It does not solve time-optimal control, other word architectures, realistic time/noise bounds, or higher-dimensional synthesis. Hamada's exact synthesis results are not claimed as new; scientific priority of the metric/Haar extension is not independently certified. Main source: Garbaravičius and Wolf, arXiv:2610.17826v1. Principal comparison: Hamada, arXiv:1401.0153, and Aiello et al., arXiv:1410.4975.

Self-review: passed. Independent audit: not yet performed.
