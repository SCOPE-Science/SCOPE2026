---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The three positive-descent reductions preserve residue modulo a=2n²+2n+1; terminal region L_n contains exactly a pairs and is residue-complete via the b-multiples since gcd(a,b)=1. Every nonterminal representative descends; any second representative has a last reversed reduction, so the least available reversal cost gives delta*n. Maximization over the three disjoint pieces gives 506 for n=3, 6n³+26n²+43n+22 for n=4,5, and 8n³+20n²+16n-2 for n>=6. Independent priority-queue enumeration of all coefficient pairs through the second Apéry threshold verified every residue and every formula for n=3..16; the general proof is the reduction argument, not enumeration.

## originality

PASS

Yin–Mu–Komatsu study generalized-star numbers with q>=4, expressly excluding centered squares q=2. Chatterjee–Narula 2025 has exactly the centered-square generators but the accessible abstract describes ordinary Frobenius and Sylvester numbers, not p=1; its full text was inaccessible due to disconnected authorized VPN. No claim that the unread paper is non-covering. Best-of-knowledge the full second Apéry layer and piecewise first generalized threshold are not supplied by sources read.

## value

PASS

The exact second Apéry layer is a complete natural semigroup representation-threshold invariant for a canonical consecutive centered-square triple, strictly stronger than a single Frobenius maximum. Its n=3 and n=4,5 boundary regimes and stabilization at n>=6 are mathematically meaningful, not arbitrary finite slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
