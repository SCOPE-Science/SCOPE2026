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

Summing the M characters of the even modulation subgroup annihilates entries except those with i≡j modulo M. Normalization |g|²=1/N gives diagonal k/2 and off-diagonal C_j/2 in M independent Hermitian two-coordinate blocks. Their eigenvalues give exactly the stated extrema, including the nonframe case. Half-shift conjugacy holds for w, and any unimodular sequence with this property is realizable with normalized phases w_j on the first half and 1 on the second. Vanishing moving sums is equivalent to invariance by shift k and a zero sum on a period d=gcd(N,k): subtract adjoining sums and then group their k summands into k/d periods. For odd k, d is odd and divides M, so conjugacy forces signs and prohibits zero mean with any flat phases. For even k and even M the alternating sign sequence works and a constant alphabet fails. For even k and odd M, d=2h, h=gcd(M,k/2) odd and M≡h mod 2h. Balance reduces to a sum of h real parts; binary signs cannot balance, ternary real parts 1 and −1/2 balance exactly with h/3 ones, and the conjugate halves consisting of i and −i always balance. All constructed sequences are realizable in the claimed alphabets, including the N=2 boundary and k=N. The supplied numerical comparison and finite search code were inspected, not executed; the universal result is analytic.

## originality

PASS

The supported distinct claim is the minimum root-of-unity order across all consecutive translation lengths, with odd-length impossibility even for unrestricted flat phases and the exact ternary resonance. The block spectrum is explicitly not credited as original: it is a direct specialization of Asipchuk–De Carli–Rodriguez, Corollary 5.1(a). The exact overlapping two-translation catalogue result covers k=2 here, but its different domain (two translates at arbitrary step) does not cover the longer consecutive translation masks or the ternary regime. No full-domain phase-order classification was established in the checked sources; residual bibliographic risk remains.

## value

PASS

For a natural quantized constant-amplitude frame design constraint, the result exactly specifies when perfect conditioning is attainable and the smallest root order required at every even dimension and admissible consecutive mask length. The ternary resonance even for odd half-length and the impossibility for all flat phases at odd translation counts are actionable structural distinctions, not merely spectrum recomputation or a restatement of the generic block criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
