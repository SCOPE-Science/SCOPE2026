# Independent audit — 2026-10-01

**Disposition:** passed

## Correctness

The construction is internally consistent. A well-conditioned zonal block of size \(M\) gives \(M\) orthonormal vectors with point peaks of order \(\sqrt{N_k}\). Projecting the rotational Gaussian-beam tight frame to the \(N_k-M\) dimensional complement preserves stable rank comparable to \(N_k-M\); the Spielman–Srivastava restricted-invertibility estimate selects at least \(M\) uniformly conditioned projected beams whenever \(M/(N_k-M)<1\). Orthogonal mixing preserves the zonal peak and, after a sign choice, a uniform Gaussian-beam pairing. Hölder yields the low-\(p\) Sogge exponent, while gradient propagation of the point peak over a radius \(O(k^{-1})\) ball yields the high-\(p\) exponent.

## Originality

Han’s v1, submitted 2026-09-12, states that for every fixed \(p>2\) there is a positive-density subsequence, with density arbitrarily close to one; it does not assert one common subsequence for all \(p\). A later 2026-09-19 revision strengthens this to separate branchwise bases, but that revision postdates the audited record and still does not give one family carrying both mechanisms simultaneously. Resultary found no earlier equivalent common-family theorem.

### Equivalent formulations

The quantifier “same orthonormal family for every \(p\)” is strictly stronger than separate existence for each branch.

### Broader coverage

Separate branchwise bases do not imply a nontrivial intersection.

### Exact database or table comparison

No database/table coverage applies.

### Claim versus prior implication

The common-family conclusion requires an additional construction and is not a stated corollary.

### Source inspections

- **Spherical harmonics with maximal Lp norm growth** — PRIOR_FIXED_P_RESULT_AND_LATER_BRANCHWISE_UPDATE. Material read: v1 primary abstract (submitted 2026-09-12) and current arXiv revision metadata; the branchwise-basis revision is dated 2026-09-19. Evidence location: https://arxiv.org/abs/2609.14023.

- **Spherical harmonics with maximal Lp (2<p<=6) norm growth** — PRIOR_LOW_P_BRANCH. Material read: primary abstract. Evidence location: https://arxiv.org/abs/1404.5016.

- **An elementary proof of the restricted invertibility theorem** — PRIOR_TOOL. Material read: theorem-level prior ingredient identified by the proof. Evidence location: https://arxiv.org/abs/0911.1114.

## Value

A common positive-density family that simultaneously realizes both classical concentration mechanisms answers a natural compatibility question left open by the branchwise constructions. The density \(\rho<1/2\) is a structural threshold of the two-complement construction, not an arbitrary slice.

## Residual risks and limitations

Round spheres only. The construction gives every fixed density below 1/2, not an endpoint or optimal-density theorem, and constants may depend on p, n and the density.
