---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The six disjoint (H,CNOT) gate pairs prepare Phi+ tensor six. Independent X(p) errors on both ends of a Bell pair give Psi+ with q=2p(1-p), so Bell correction implements X(q) per teleported qubit. Source Eq.(36) factorizes as |+>_2 tensor [a|00>+sqrt(1-a^2)|01>+sqrt(1-a^2)|10>+a|11>]/sqrt(2); the second party at b=1/sqrt(2) is |+>^3. Overlaps of the two entangled qubits with XX equal 1, with a single X equal 2a sqrt(1-a^2). Summing two independent error parities proves F_Bi=1-2q(1-q)(2a^2-1)^2. At (p,a)=(1/2,0) F=1/2. A common Kraus index gives total norm ((1-p)^12+p^12)I, not CPTP in the interior; a separately defined correlated global-X channel differs. Independent exact rational checks on 25 parameter pairs corroborate, not replace, this symbolic proof.

## originality

PASS

Best-of-knowledge original source-specific correction: standard generalized Pauli-channel teleportation was proved in 2001, but De et al. 2026 explicitly claim unit fidelity throughout their bit-flip figure; the mathematically derived resource factorization and exact family fidelity show its product-noise claim false. The contribution is the concrete analysis of this particular source protocol, not discovery of Pauli channels or Bell-pair parity.

## value

PASS

An exact, parameter-dependent falsification of a published claimed perfect-noise robustness is important for interpreting teleportation performance. The formula provides a physical counterexample under the source's standard local Kraus model and separates it rigorously from a different correlated-noise interpretation; not merely a cosmetic normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
