---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS, subject to a bibliographic numbering erratum. Cooper–Riasanovsky/OEIS prior support decomposition as p^(4j+1)k² with p≡3 mod 8 prime and p∤k is correctly credited and directly checked. Summing higher j>=1 and spurious p|k principal-stratum terms gives O(sqrt X) each uniformly per progression. For k<=log(X)^(R+4), use the standard strong max_{y<=X} Bombieri–Vinogradov prime theorem at modulus Q with arbitrary log power; the dependence of a k^(-2) on k is absorbed by max over all reduced classes. For k>log^C, the elementary progression upper bound y/m+1, sum_m 1/φ(m)<<log Q and Qsqrt X control tails, so choosing B_R large proves every R. The total coefficient is 1/4 sum_{odd k}1/k²=π²/32. Independent GF(2) series inversion vs prime factorization checked 500 residue-3 indices below 4000; not an asymptotic proof. The cited support characterization is Proposition 26 in the primary paper, not Proposition 16 as written in the source RESULT; citation number must be corrected in a future scientific-file maintenance edit, but does not alter the theorem.

## originality

PASS

PASS, qualified because the transfer argument is elementary once the classical BV theorem and published prime-square support are known. The exact support and density-zero result are old; the new asserted statement gives an explicit main term and averaged growing-modulus level for this canonical parity reciprocal slice. Searches of the relevant published corpus, OEIS, and primary convolution/BV literature revealed no directly dominating statement with the same slice and uniform progression regime. A general convolution-stability theorem may imply the statement without matching notation; this is a real priority and value risk, not a proof of novelty.

## value

PASS

PASS, qualified. The parity reciprocal has a canonical sparse progression slice whose earlier known results identify members but do not quantify their distribution. The exact square-weighted progression asymptotic and level 1/2 provide a natural nontrivial arithmetic statistic with a sharp prime-like leading scale. The argument is a standard BV transfer rather than new sieve technology; its value is in the exact natural slice and the complete uniform statement, not a claim to improve BV itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
