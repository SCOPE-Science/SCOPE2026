---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

The invariant Walsh projection formula gives λ=E|K_N| with K_N=(S_N²−N)/2, where S_N is the sum of N independent signs. By mean zero, its L1 norm is twice the negative central mass. The identity K_N(k)C(N,k)=C(N,2)[C(N−2,k)−2C(N−2,k−1)+C(N−2,k−2)] telescopes over the exact parity-aware negative band to the stated one-boundary binomial difference, then the equivalent rational prefactor follows algebraically. Uniform Stirling in the window r=√N−δ, 0≤δ<2, combined with the prefactor gives cN+c(1/6−(δ−1)²)+O(N^(−1/2)). Subsequence squares δ=0 and squares+1 δ→1 attain the extrema. Fresh independently coded direct exact rational Walsh averages matched the exact boundary formula for N=2..100; N=10000,10001,40000,40001,90000,90001 matched the predicted order-one phase to the stated error scale. This does not use finite checks as an infinite proof.

## originality

PASS

The primary projection-constant paper determines a general invariant Walsh-kernel integral formula and the leading degree-two limit λ/N→c, but not the one-boundary finite formula or the parity-lattice order-one oscillatory correction. A single-boundary Krawtchouk telescoping formula and its limsup/liminf phase appear to be a new best-of-knowledge refinement; Resultary search failed and is explicitly not treated as negative novelty evidence.

## value

PASS

The projection constant is a natural Banach-space invariant; its exact finite degree-two formula and uniform lattice-phase correction sharpen the previously determined leading linear growth, reveal nonconvergence of the order-one remainder and give sharp limsup/liminf. A precise finite-size oscillation is mathematically motivated, useful for comparisons and not mere arbitrary small-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
