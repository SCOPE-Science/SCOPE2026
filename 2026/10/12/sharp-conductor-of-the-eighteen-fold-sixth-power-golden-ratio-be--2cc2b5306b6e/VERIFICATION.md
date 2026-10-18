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

PASS: Exact published Theorem 4.3 of Pongsriiam 2022 gives infinite coverage of (h+1)B(phi^m) for even m>=4 beyond h^4+2h^3-h^2-h+1; h=floor(phi^6)=17 yields all integers >=93042 in 18B. To exclude 93041, the floor-of-sum inequality for eighteen positive terms restricts total index N to 5185 or 5186, using exact neighboring floors 93023,93041,93058,93076. The Pell relation 2889^2-5*1292^2=1 establishes theta=9-4sqrt(5)=18/323+delta with 0<n delta<1/323 for 1<=n<=5186. Thus ceil(theta n)=(18n+r(n))/323 where r(n)=323-(18n mod323) in 1..323. For N=5185, summing yields only 17 across eighteen positive residues, contradiction. N=5186 yields 18*323-1, requiring 17 positive multiples of 323 and one index congruent to 18 mod 323, giving N>=5509>5186. Independent exact integer-square-root floor/residue checks for every n through 5186 corroborate the arithmetic. Eventual coverage rests on the inspected published theorem, not finite membership tests.

## originality

PASS

Pongsriiam 2022 already proves the full upper-coverage threshold for every even exponent m>=4 and explicitly conjectures its sharpness for m>=6; the assessment credits that premise. The new nonmembership argument establishes the first remaining even case m=6, so the conductor and Frobenius number become exact. Wythoff sumsets at powers 1 and 2 and effective additive-basis decidability do not yield this evaluated eighteen-summand exceptional integer.

## value

PASS

Pongsriiam explicitly singled out exactness of the 18-fold golden-ratio-power bound as a conjecture. The first open even exponent m=6 has a natural small parameter fixed by that conjecture, and the submitted Pell congruence shows the known global upper threshold is sharp. Resolving the exact conductor/final gap is a mathematically motivated exact invariant, not a random enumeration slice; it supplies a new proof ingredient absent from the prior global inclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
