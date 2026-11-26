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

For a proper even border b let v=v₂(b)<k. Its comparison shift d=2^k−b has v₂(d)=v. Every interval of b≥2^v indices contains an i with i+1≡2^{v−1} mod 2^v. At i and i+d the defining valuation is v−1 and the odd quotient changes by 2 modulo 4, toggling the symbol independently of the instructions. This is an independent equivalent proof of the frozen induction and excludes every proper even border. For an odd border of length 2h+1 the shift changes parity: at offsets 0,2,…,2h one compares consecutive symbols in the decimated word against the alternating even lane. A length-four alternating segment in any decimated word is impossible, since its two absolute even positions differ, so h≤2. At length five the same lane gives w₀=w₄ and the border gives w₄=w_{N−1}. Thus five is possible only with a one-border. These arguments cover k=2 and all start parities. Direct substitution at positions 3,4,5 and N,N+1,N+2 gives 001 for both triples in the zero-instruction word for N divisible by eight, proving shortest length three. The frozen checker was inspected, not executed; its local-rule check alone would not exclude even borders for already bordered words. An independent bounded check (python3 /workspace/audit_checks.py, check 4) generated the words by interleaving folding levels and examined every border in 246,784 finite windows across all 256 depth-eight instruction choices. The infinite statement follows from the parity proof, not the enumeration.

## originality

PASS

The supported distinct result is the per-factor dyadic certificate and exclusion of every proper even border for all instruction streams, not factor complexity, automatic recognizability, or a count for the regular word. The inspected generalized factor theorem, regular least-period theorem, and indexed analogues do not imply those assertions. No exhaustive priority claim is made.

## value

PASS

Dyadic lengths are the natural scale of folding. A sharp boundary-only certificate at those lengths, uniform over arbitrary instructions and starts, gives strictly more local structural information than finiteness or aggregate factor counts. The length-three witness shows that endpoints alone fail; the even-border obstruction rules out a whole class of periods even for words with an odd border. The claim is useful without enumerating all unbordered factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
