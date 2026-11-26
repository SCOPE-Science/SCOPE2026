---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The digit recurrence makes each aligned q-block a permutation. Hence multiples of q give arbitrarily long powers starting at zero. For N=qm+r the centered prefix sum D(N) is F_r(t_q(m))−r(q−1)/2, with |D|≤(q−1)²/2, and F_r(1)−F_r(0)=r for 1≤r<q. In the phase lemma, eventual periodicity of q^u mod h holds even when q and h are not coprime. At sufficiently high paired positions, the q separated unit digits of H_i have total residue q·q^u mod h, equal to the one unit digit at u+1 in L_i. The spacing period can be chosen at least 2 and the gadgets and low seed disjoint, so replacing gadgets changes the digit sum by 1 mod q per replacement without carries and leaves the index residue unchanged. With q−1 gadgets all q phases occur for every low-seeded residue in one finite q-adic block. The high-digit shift only permutes phases, giving uniform coverage in every aligned block and thus a finite computable horizon M(q,h) on every h-progression. On a power the endpoints have D increasing by the constant S−ℓ(q−1)/2. Nonzero increments have magnitude at least 1/2, forcing k≤2(q−1)². Otherwise take g=gcd(q,ℓ) and P=q/g≥2, and select a nonzero remainder occurring every P endpoints. The quotient indices of that subsequence advance by h=ℓ/g, so with k≥PM(q,h)−1 it contains M consecutive quotient indices and therefore two phases with unequal F_r. This contradicts constant D. For example max(2(q−1)², PM(q,h)−2) is an effective all-start upper bound at excluded orders. No finite sample is needed for this proof.

## originality

PASS

The distinct finding supported by comparison is the complete all-base classification of fixed-order unbounded additive exponents and the effective boundedness of the excluded orders. The binary classification is already implied by indexed odd-order cube exclusion plus aligned blocks, and the phase-coverage lemma follows from older digit-sum distribution theory with the q-adic block identity. Neither is credited separately as original. The actual all-base power classification uses the additional bounded-prefix-drift and nonzero-endpoint-residue argument; no compared work supplies that classification or a stronger power theorem implying it.

## value

PASS

Fixing the root length separates a natural periodicity question from existence of high powers with lengths growing with exponent. The radix-divisibility criterion completely answers that question for integer-sum powers of this standard cyclic word; in particular it distinguishes finite-power occurrence from unbounded exponent at nonmultiple orders where cubes do occur. The discrepancy reduction explains why known digit-sum distribution is enough for this new use and gives a computable all-start bound rather than checking only prefixes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
