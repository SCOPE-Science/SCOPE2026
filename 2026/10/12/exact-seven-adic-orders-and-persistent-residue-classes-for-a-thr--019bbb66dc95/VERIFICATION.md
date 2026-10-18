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

For n=6t+r, powers 64^t and 729^t interpolate to restricted Z_7 series. Direct residue calculation gives 1+2^r+3^r congruent 3,6,0,1,0,3 mod7, so only r=2,4 matter. Dividing F_2 by 7 gives reduced H_2=2+6t mod7 with exact root t=-1/3 (nontrivial 7-adic cube roots sum to -1); uniform integral divided differences force v7(F_2)=1+v7(n). Dividing F_4 by 49 gives reduced H_4=2+6t²=6(t-3)(t-4) mod7 and exact distinct lifted roots t=-1/2 and -2/3, producing 2+v7(n-1)+v7(n). Coefficient divisibility bounds ensure reductions apply to ALL Z_7 arguments, and 7-adic Hensel simple-root factorization covers all n, not just sampled n. Period L_k=6*7^(k-1) follows from 64,729 congruent 1 mod7 and lifting; CRT gives counts R1=2,R2=8,Rk=15 (k>=3). Independent exact modular checks n=1..6999 and full periods k=1..5 matched; all-k result relies on proof.

## originality

PASS

Bayarmagnai–Delger 2022 Remark 10 explicitly records only the exceptional subfamily v7(1+2^(4*7^j)+3^(4*7^j))=j+2. Their general sufficient unboundedness theorem does not give the other n classes, the n−1 valuation branch, or stable per-period counts. General interpolation/regularity results are methodological tools, not the exact three-power formula in the inspected text. Relevant Resultary 7-adic entries concern different sums, not this one.

## value

PASS

A published exceptional three-power valuation problem is closed in every exponent residue class, with all prime-power lifting multiplicities and a persistent exact root count. The distinct simple-root branches and stabilized 15-count provide a concrete natural p-adic exponential-divisibility classification, independently useful as a sharp analogue of isolated published examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
