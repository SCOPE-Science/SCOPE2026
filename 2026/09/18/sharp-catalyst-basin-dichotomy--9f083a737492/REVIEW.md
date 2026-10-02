# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The proof closes all asymptotic branches under the stated source hypotheses. The quadratic energy of the first and third components dissipates both spatial gradients and the catalyst-weighted reaction gap. Positive-time parabolic regularity justifies gradient decay; Poincare-Wirtinger reduces the first and third components to their means. The energy decomposition forces the catalyst-complement mean to converge, leaving only the positive and boundary equilibrium branches. A mean-zero energy estimate gives convergence of the catalyst field. If initial total catalyst is positive, boundary convergence would eventually make the reaction gap uniformly positive and force exponential growth of the catalyst mean, contradicting its conserved-mass bound. Zero initial catalyst instead gives the invariant catalyst-free face.

Originality: PASS. The primary Nguyen-Tang article was inspected in accessible full text around the coexistence discussion. It explicitly states that boundary instability does not rule out a trajectory returning and converging to the boundary, labels that possibility unknown, and formulates global attraction as a conjecture. The audited theorem resolves exactly that open branch and identifies the invariant zero-catalyst face omitted by the literal conjecture. Searches found no later source-specific proof with the same basin decomposition.

Scientific value: PASS. The exact basin boundary is a natural global-dynamics question explicitly left open in the motivating primary paper. The theorem converts local instability plus the Lyapunov identity into a complete coexistence-regime selection result and sharpens the conjecture by isolating the necessary invariant-face exception.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
