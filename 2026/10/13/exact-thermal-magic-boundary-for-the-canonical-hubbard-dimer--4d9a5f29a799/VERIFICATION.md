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

An independent integer occupation-basis replay checked the fermion signs: on (d₊,s₋) the Hamiltonian is U I/2 + 2t(qZ−X), and the other two levels have energies U and 0. The replay also checked the three commuting Pauli syndromes and the signs of the logical Paulis. The +++ joint eigenspace is exactly the two-level block: the first two Paulis impose the sector and the third splits each complementary occupation pair. An encoded stabilizer mixture passes Pauli postselection; hence the logical block detects nonmembership of the full four-qubit polytope, regardless of weights on the other levels. The reverse implication follows by combining the encoded octahedron decomposition with the two complementary stabilizer projectors. The conditioned qubit has Bloch vector (1,0,−q)tanh(2tg/T)/g, yielding the claimed iff test, with the zero-temperature limit and U=0 case handled. At q>0 the test crosses once in T. For L=atanh(g/(1+q)), L'=(q−1)/(2qg); the derivative sign of g/L is the sign of qL/g−(q−1)/(2q), positive for q≤1 and also for q>1 by L>g/(1+q). Under q↦1/q, L is invariant and g is divided by q. The exact logarithm 2L=log((1+q+g)^2/(2q)) gives both endpoint equivalents and surjectivity, and q_c is exponentially small at low T, so the O(q_c) log correction and O(q_c²t/T) exponent correction go to zero, preserving the inverse prefactor. The free mixing interval has width g/(1+q), uniquely minimized at q=1.

## originality

PASS

The same-sector spectrum, thermal death and its explanation by mixing the two nonstabilizer states are prior. The distinct supported claim is an explicit all-U iff characterization of the full stabilizer boundary, together with its proved threshold properties and sharp inverse onset.

## value

PASS

This closes an explicit boundary question in a previously plotted canonical strong-correlation example. An exact class membership test removes the need to solve a robustness program at every parameter, explains why the other energy levels cannot hide the magic in the selected block, and gives the low-temperature interaction onset with a prefactor that is not reliably read from a phase diagram. The contrast with the minimum-width two-level interval shows that the thermal crossing is not simply controlled by mixing geometry without its energy scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
