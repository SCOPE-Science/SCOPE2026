---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Rows 0,1,2,3 give a Vandermonde determinant whose modulus is 64 sin(πa/N)sin(πb/N)sin(πc/N)sin(πd/N)sin(π(a+b)/N)sin(π(b+c)/N) for positive cyclic gaps totaling N. The strictly concave even-about-N/2 function f(t)=log sin(πt/N) gives opposite-gap balancing |a−c|,|b−d|≤1; transferring one unit between opposite pair sums when they differ by ≥3 improves L strictly. Enumerating the remaining balanced integer cases proves gaps (q,q,q,q), three q and one q+1, alternating q and q+1, or one q and three q+1, for N mod4=0,1,2,3. For N≡2 adjacent large gaps have smaller diagonal sine product cos(π/N)<1 than alternating; Hadamard covers divisible-by-four case. Orbit-stabilizer gives N/gcd(N,4) literal optimizers. Independently enumerated all 118755 four-subsets for N=4..28, checking independent six-chord product, maximal values and all predicted sets. Finite census is corroboration only; concavity and case analysis establish all N≥4.

## originality

PASS

Best-of-knowledge comparison of statements/implications from genuinely inspected primary material and the audited claim. Resultary returned temporarily_unavailable/search_completed:false; this failed search supplies NO negative novelty evidence. A continuous four-node Fekete theorem proves the r=0 perfect-square case and an upper bound, but does not imply exact arithmetic gap spacing, the strict difference between adjacent and alternating longer gaps for N≡2, or N/gcd(N,4) maximizer multiplicities on every discretized grid.

## value

PASS

The determinant D(E) is a natural volume measure of nondegeneracy for four-frequency exponential bases on a fixed cyclic sampling grid. An all-N exact optimum, optimizer multiplicity and strict alternating gap requirement in N≡2 mod4 provide a complete natural design classification, not an arbitrary numerical slice. The even-parity distinction changes the actual optimal frequency set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
