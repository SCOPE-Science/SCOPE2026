---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS — Correctly distinguishes total 4-hooks across partitions into odd parts a4(n) and distinct parts b4(n), with the empty partition zero. Inspected Craig–Dawsey–Han Theorem 2.1 all-hook generating identities used as a cited lemma; algebra yields difference q^7(1-q)R(q)Q(q)/((1-q^6)(1-q^8)) with R=1-q+q²+q³+2q⁴+2q⁷+2q⁸+q⁹-q¹⁰. Define K=(1-q)Q/((1-q^6)(1-q^8)); monotonicity Q_n from odd-parts injection gives K_n>=0. Bidar 2012 Lemma3 proves e_n=Q_n-2Q_{n-1}+Q_{n-2}>=0 for n>=5. The only negative low e values e1=e4=-1 are paired injectively within each degree >=11 to e9 or e5 and e12 or e0 in 6,8-step convolution, proving K_n>=K_{n-1} there. Consequently every coefficient n>=27 is nonnegative by displayed R expansion; independent direct Ferrers hook enumeration n=0..26 reproduced [0,0,0,0,0,0,0,1,-1,1,2,1,2,2,4,6,7,7,11,13,17,22,27,31,40,48,57]. Only n=8 is negative (-1), so sharp terminal N4=8 is proved globally, not inferred from finite data.

## originality

PASS

PASS — The exact four-hook endpoint N4=8 was explicitly CONJECTURED, not proved, by Ballantine et al (2023), Conjecture1.7 Figure2; that paper proves only h=2,3. Craig–Dawsey–Han (preprint 2023, later revisions) proves asymptotic eventual hook bias all fixed h but explicitly calls its method non-effective (Remark1.3), so it does not determine the sharp endpoint h=4. The use of their hook generating function and Bidar convexity is openly credited; new mathematical input is the coefficient-pairing and finite exact endpoint.

## value

PASS

PASS — Resolves the first unproved low hook length in an explicit numerical conjecture, obtaining an exact all-n sign characterization and sharp exceptional size, as opposed to a mere computational extension. This endpoint is intrinsically motivated by the partition hook-bias phenomenon and can serve as an exact test of uniform asymptotic bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
