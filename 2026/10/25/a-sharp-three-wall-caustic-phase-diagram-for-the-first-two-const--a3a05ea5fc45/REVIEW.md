# Scientific review

## Correctness

**PASS.** For the exact strictly convex support family, the antipodal contact formula gives Wigner velocity \(D\tau\) and centre-symmetry velocity \(-D'n\), with \(D=-8a\cos3\theta-24b\cos5\theta\). Factoring these two scalar velocities into quadratics in \(\cos^2\theta\) produces the three rational transition ratios. Both discriminants stay strictly positive, excluding interior root collisions. The endpoint factors and one test point per interval prove the full open-region counts; Taylor orders settle the walls. Fourier orthogonality gives the matched oriented areas, and the exact amplitude bound certifies strict convexity. `verify.py` independently checks the algebra and representative configurations. It is not an infinite numerical proof.

## Originality

**PASS under the inspected sources, with residual literature risk.** The 2026 frontal paper gives general local singularity criteria and order lowering but no simultaneous global count for the aligned \(3\)/\(5\) constant-width support family. The 2026 mixed-volume paper gives general oriented area identities but not the explicit same-invariants/different-cusps example. Domitrz–de M. Rios give only the general cusp-count ordering. A nearby published two-mode comparison using an even second harmonic and an odd fifth harmonic always yields five cusps in both loci; the Fourier parity and phase behavior differ essentially. Searches for aliases, the two exact rational walls and the invariant-matching example yielded no claim implying this classification. The possibility of earlier unindexed examples is retained as a risk.

## Value

**PASS.** Harmonics \(3\) and \(5\) are the first two geometrically nontrivial odd Fourier modes for constant-width support functions; a one-mode family cannot exhibit cusp-count transitions. This is therefore the lowest-order model in which the general inequality between Wigner and centre-symmetry cusp counts can change from equality to a strict gap. The theorem classifies its entire generic coefficient-ratio axis, resolves all three degenerate walls, and constructs an exact counterpair showing that five natural global scalar geometric invariants fail to determine cusp topology. The counterpair is not an arbitrary numerical slice but realizes two distinct open cusp phases with invariant equality.

## Closest literature and limitations

General singularity rules: Zwierzyński, arXiv:2609.14653, Theorems 3.3, 3.9, 4.1. Area relations: Zwierzyński, arXiv:2608.11068, §7. Cusp ordering: Domitrz and de M. Rios, 2014, Theorem 7.2. The cosine-phase two-mode family does not cover arbitrary Fourier phases or higher harmonics; source searches do not prove universal priority. Computations verify formulas, not novelty or general algebraic deductions.

Self-review: passed. Independent audit: not yet performed.
