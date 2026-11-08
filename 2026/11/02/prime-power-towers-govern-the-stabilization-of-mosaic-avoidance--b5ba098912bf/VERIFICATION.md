---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. Reconstructed lambda_S(p^a)=1 if p in S and 1+lambda_S(a) otherwise; for a composite, take the minimum across prime-power factors. Induction gives the unique least depth-i witness M_1=q, M_{i+1}=r^{M_i}. For large i, every other depth-i exponent is >=2M_i (different base s>r, increased exponent or extra factor); depth>i starts at least M_{i+1}. The Euler product is legitimate: tail obstructions at primes p>P have total density <=sum_{p>P}p^{-q}, while finite-prime large-exponent tails are summable. Hence delta_infinity=product B_{S,p}>0. Conditioning on v_r(n)=M_i with all other valuations fully avoiding yields leading density K_S*r^{-M_i}; additional valuations at r are O(r^{-2M_i}) and those at p>=s are O(s^{-M_i}). Identical squeezing gives delta_i-delta_{i+1}. Independent SPF mosaic recursion checked q={2,3} and S={2,3} small witnesses, but finite checks are not the infinite proof.

## originality

PASS

PASS, best-of-knowledge: the exact level-to-infinite-depth leading Euler-product coefficient and iterated-exponential rate for a specified forbidden-prime set were not implied by inspected fixed-depth Euler-product theorems, single-prime full-depth constants or total-height upper bounds. Earlier source gives finite-i delta_i; new object is i->infinity signed gap.

## value

PASS

PASS. The depth-truncation error of a natural multiplicative density is an intrinsic arithmetic invariant; identifying unique tower exponent, positive leading constant, and the sharp iterated-exponential rate answers a meaningful approximation question left by fixed-level results, not a merely renamed known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
