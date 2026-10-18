# Independent mathematical audit

## correctness

PASS

PASS: The four given Kraus matrices form a CPTP qubit map. Explicit serial Choi matrix under diagonal K, after partial transpose, has one critical 2×2 block determinant proportional to BC(k²A+D)²-k²p². Minimizing by AM-GM yields the iff criterion and optimal k²=D/A up to an overall admissible contraction scale. Independently rebuilt the two-step Choi from Kraus matrices for the rational witness: trace=2227/3200, smallest PT eigenvalue approximately -0.00421546, exact central determinant -34453431/25600000000. For arbitrary intermediate U, axial symmetry reduces Euler angles to one polar angle u∈[-1,1]; source derived the four PT elementary symmetric polynomials. Independently re-expanded its quartic numerator P(2y-1) into degree-four Bernstein coefficients (257974593536,177204577664,456454468448/3,86373743024,2755782416), all positive; e2/e3 decrease with u yet remain positive at u=1, e1=1. Positive symmetric polynomials force all real Hermitian eigenvalues positive because det(zI+H) has positive coefficients for z≥0. Separately sampled 1001 intermediate unitary angles, positive minimum corroboration only; the Bernstein proof certifies the continuum. Branch is selective trace-decreasing; no CPTP theorem claimed.

## originality

PASS

PASS (best knowledge): Lami–Giovannetti arXiv:1411.2517 analyzes unfiltered EB indices and CPTP intermediate filters/conjecture; the present trace-nonincreasing single-Kraus conditional branch lies outside the conjecture’s class. Cuevas et al. arXiv:1707.00161 studied unitary amendments for rotated channels and some zero-temperature amplitude-damping experiment, not a general comparison proving all unitaries fail for a thermal GAD while one heralded measurement branch succeeds. Filippov–Rybár–Ziman parallel-channel entanglement annihilation and Goswami/Ghosh/Majumdar pre-/post-filter protection do not supply the exact serial all-unitary certificate. General probabilistic filtration equivalence remains possible but no dominating published theorem established in inspected primary material.

## value

PASS

PASS: The theorem identifies a precise structural separation between unitary deterministic intervention and physically valid heralded success in finite-temperature qubit damping, with a sharp diagonal class phase boundary and a rational witness. The exact all-angle polynomial positivity certificate rules out every unitary, not just those tested numerically, and clarifies why this does not refute a conjecture restricted to CPTP filters. The mechanism is meaningful for selective entanglement preservation without misreporting success as unconditional recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
