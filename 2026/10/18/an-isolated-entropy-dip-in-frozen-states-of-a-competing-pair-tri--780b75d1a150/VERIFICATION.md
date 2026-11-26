---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Flipping the center of abcde changes the two adjacent pair terms and the three containing triplets, giving ΔH/(2J)=c(b+d−r(ab+bd+de)); strict positivity and N≥5 are used. The only possible nonnegative zeros are 0, 2/3, 2. A labeled periodic spin configuration corresponds to a unique closed walk with fixed starting site in the four-spin overlap graph, even when its primitive period divides N. Independent replay: for p/q=0,1/3,2/3,1,2,3, indexed words − as 0 and + as 1, formed edges by the integer test c[q(b+d)−p(ab+bd+de)]>0, computed transitive closure for SCCs and characteristic coefficients by c_k=−(Σ_{j=1}^k c_{k−j} tr(A^j))/k with c_0=1. All six polynomials agree with RESULT.md; cyclic component sizes are (1,1), (6,1), (6), (11), (10), (12), and the dominant component in each positive-r case contains the all-minus loop. Direct recomputation of the whole Hamiltonian after each single-spin flip agreed with the transfer traces in all 30 cases over N=5,…,9. At zero there are exactly two uniform configurations; otherwise primitivity gives a single dominant positive eigenvalue and the trace has its exponential rate. In the last regime the factor x⁹−x³−1 has its positive root below δ because at δ, y=δ³>2 and y³−y−1>0. Edge inclusion and strict component extension were verified for the 6-to-11 and 10-to-11/12 inclusions, proving α<β and γ<min(β,δ) by strict Perron monotonicity. Also β<73/50<δ: for the r=1 irreducible block A, v=A⁴⁴1>0 satisfies 50Av<73v coordinatewise by exact integer arithmetic, and the cubic at 73/50 has numerator −2433. The finite replays corroborate the all-volume transfer and Perron arguments, not vice versa.

## originality

PASS

The distinct result is the finite mixed-coupling phase diagram for strict single-spin minima, especially the entropy value at r=2 being below both adjacent open regimes. The pure triplet growth base δ is already known; the r>2 local word set is exactly the pure triplet one because r>2 dominates every pair field. Neither the pure comparison, the published constrained pair dynamics nor the closest indexed weak/exchange blocking statements supplies the mixed threshold graph and its entropy dip. This is a bounded statement-level assessment, not a priority certification.

## value

PASS

A natural one-dimensional competing Hamiltonian has a complete finite-ratio classification, and ties at one isolated ratio remove exponentially many strict minima relative to nearby couplings on both sides. This is a structural discontinuity in the count, not merely a numerically precise root or a claim about quench kinetics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
