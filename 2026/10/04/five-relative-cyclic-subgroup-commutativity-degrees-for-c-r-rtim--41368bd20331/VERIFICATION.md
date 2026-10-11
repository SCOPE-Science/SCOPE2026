---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The subgroup classification is exhaustive. With kernel \(A=C_r\) and cyclic complement \(B=C_{pq}\), subgroups containing \(A\) are inverse images of subgroups of \(B\), while subgroups disjoint from \(A\) inject into \(B\) and are cyclic of order \(1,p,q,pq\). Fixed-point-freeness gives normalizers \(N_G(P)=N_G(Q)=N_G(B)=B\), so each nonnormal cyclic type has exactly \(r\) conjugates and \(|L_1(G)|=3r+2\). The only permuting partners of a nonnormal cyclic subgroup are \(1,A\) and the three cyclic subgroups in its unique complement, hence exactly five. Summing partner counts over \(L_1(H)\) gives every displayed formula. Independent algebra reproduces the four successive positive differences \(3(r-1)/(2L)\), \(3(r-1)/(4L)\), \(3(r-1)(r-6)/(4(r+2)L)\), and \(12r(r-1)/((r+2)L^2)\); since \(pq\mid r-1\) with distinct primes, \(r\ge7\). The packaged finite semidirect-product checks are corroborative only.

## originality

PASS

Originality passes decisively against the motivating literature. The published final Filomat paper was read through its further-research section. It explicitly singles out the Frobenius group \(C_r\rtimes C_{pq}\), with distinct primes and \(pq\mid r-1\), states that one must compute exactly the six nontrivial relative cyclic subgroup commutativity degrees appearing in the audited theorem, and leaves their comparison to future work. The audited proof performs that requested calculation and shows the six types collapse pairwise to four nontrivial values plus 1. The later paper with 'five relative commutativity degrees' studies the different elementwise invariant \(d(H,G)\), so it is not covering.

## value

PASS

The theorem resolves the exact infinite Frobenius family singled out in the foundational paper as a difficult three-nonnormal-class test case. It determines the entire relative cyclic subgroup commutativity function on every subgroup type and reveals nonobvious pairwise collapses. That is a directly motivated completion of an explicit research problem, not a narrow arbitrary invariant computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
