---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The proof partitions X uniquely by its least entry valuation k. For 2k≥n, X²=0 automatically and the primitive Smith form diag(1,d) over the quotient of length e=n−k gives rank/image length 2e−v(d), counted by GL₂ and rank-one residue determinant fibers. For 2k<n, nonzero square-zero reduction is rank-one nilpotent with a cyclic vector; Cayley–Hamilton plus cyclicity make B²=0 mod π^(n−2k) equivalent to trace and determinant both zero mod that ideal. On a rank-one nilpotent residue chart the trace–determinant map has two independent unit partials and uniform q² lifts per digit; allowed traces have q^k values, and allowed determinant valuation classes contribute exactly the displayed q exponents. Counting every shell yields the polynomial and its total, with no division by two, including ramified/mixed characteristic. Image length r≤n follows from im⊂ker; vanishing homology iff r=n, giving the coefficient. Independently enumerated every 2×2 matrix modulo 2,4,8,16; 3,9,27; and 5,25, computing the defining four square equations and determinant valuation, and matched every coefficient, e.g. Z/16: (1,9,78,168,384). Small enumerations verify only listed rings; the uniform all-chain-ring statement uses algebraic chart proof.

## originality

PASS

Feng–Nóbrega–Kschischang–Silva treat unrestricted finite-chain-ring matrix shapes; Carnevale–Shechter–Voll (full primary author PDF inspected) enumerate trace-zero matrices by image sizes over local valuation rings, but do not impose simultaneous det/trace constraints from X²=0. Brawley 1982 and Bollman–Ramírez count nilpotent/Drazin matrices, potentially including the unrefined total, which is not counted as a new standalone discovery. The joint square-zero image-module-length distribution for every n,q and acyclic stratum remains an identifiable additional calculation. Best-of-knowledge PASS, with incomplete full historical Drazin article coverage expressly acknowledged.

## value

PASS

Image length of a square-zero differential measures image boundaries and determines homology length in a 2-periodic complex of free rank two. A full all-length q-polynomial ranking for a natural nilpotent locus, including ring-independence and rational generating series, gives a reusable exact invariant rather than an arbitrary short table; acyclic count has an independent algebraic/homological interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
