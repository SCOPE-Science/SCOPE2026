---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

PASS. The falling-factorial 2-adic series F(x)=sum_j (-1)^j P_j(x) converges uniformly because products of j consecutive 2-adic integers have at least floor(j/2) factors of two; its derivative converges uniformly and the integral Taylor remainder gives F(x+h)-F(x)=hF'(x) modulo h^2. From F(x+1)=1-(x+1)F(x) and F'(0)=-sum_{m>=0}m! ≡2 mod4, parity branches have v2(F'(odd))=0, v2(F'(even))=1. For odd x and h divisible2 the linear term dominates; for same even x mod4 and h divisible4 it also dominates with +1 valuation. Hence H(t)=F(1+2t)/2 and G0/G2=(F(4t)-1)/8,(F(2+4t)-1)/8 are isometries Z2->Z2, thus finite quotient permutations and surjections, implying exactly one odd-index preimage for each even output and four even-index preimages for each target ≡1 mod8. Periodicity follows from 1-Lipschitz. Independently checked all 8184 integer index residues for k=3..12; unrestricted law is from the analytic argument. k=1,2 are explicit boundary cases.

## originality

PASS

Best-of-knowledge originality PASS on the exact final claim after new Git-tree proof and computation reconstruction, Resultary semantic searches, checked primary theorem scopes and explicit source risks. Not a claim of comprehensive historical priority, external certification or entire-paper noncoverage where material was inaccessible. All known special-case antecedents are credited.

## value

PASS

PASS. Complete all-exponent images and exact residue multiplicities modulo 2^k for the classical derangement sequence are natural modular arithmetic invariants beyond the well-known recurrence, period and low-bit congruences. The stable five-eighths image proportion and distinct 1-vs-4 target multiplicities have a mathematically motivated 2-adic isometric structural explanation. This is a full infinite-family theorem, not arbitrarily selected small moduli; published modulo-eight base case is explicitly attributed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
