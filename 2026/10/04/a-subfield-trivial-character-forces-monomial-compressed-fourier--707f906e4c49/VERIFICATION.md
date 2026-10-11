---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Since \(m\mid p+1\), the index-\(m\) subgroup \(H\) contains \(\mathbb F_p^\times\), and \(|H/\mathbb F_p^\times|=(p+1)/m\). For a character descending nontrivially to that quotient, decompose \(H\) into prime-field projective lines. The canonical additive-character sum over a line is \(p-1\) on the unique trace-zero line and \(-1\) otherwise. Quotient-character orthogonality then forces each compressed Fourier entry to vanish unless its product orbit is the distinguished trace-zero orbit, where it equals \(p\chi(t_0)\). Hence there is exactly one nonzero entry per row and column, all of modulus \(p\), giving determinant modulus \(p^m\), \(m^2-m\) zero entries, and exactly \((p+1)/m-1\) eligible nontrivial characters. Fresh checks confirmed the subgroup and character-count boundary at \(p=7,m=4\); the universal conclusion rests on the projective-line proof.

## originality

PASS

Garcia-Karaali-Katz introduce the compressed Fourier framework and non-prime-field obstructions; the later Díaz Padilla-Ochoa Arango paper explicitly characterizes the index-3 nontrivial-character case. The present family begins at \(m=4\) and uses the opposite structural situation from the standard proper-subfield obstruction: \(\mathbb F_p^	imes\subset H\), with the character trivial on that subfield group. Current published-finding searches found no theorem giving the resulting monomial support pattern for all \(m\mid p+1\).

## value

PASS

The theorem supplies a uniform infinite higher-index failure mechanism in a program whose published complete classifications are concentrated at small indices. The exact monomial form simultaneously determines support, determinant magnitude, zero-entry count, and the number of affected characters, making it a reusable structural result rather than a finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
