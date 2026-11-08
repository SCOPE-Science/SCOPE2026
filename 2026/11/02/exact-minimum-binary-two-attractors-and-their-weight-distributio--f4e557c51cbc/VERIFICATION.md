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

For every nonempty linear binary word w, coverage of both distinct length-one and length-two factor TYPES by marked positions has gamma2=1 for constant words and >=2 for nonconstant. A mark touches at most the two adjacent digrams; all distinct-pair possibilities from length-3 windows are {00,01}, {00,10}, {01,10}, {01,11}, {10,11}; {00,11} is impossible for one mark. If all four digrams appear, two marks cover them iff both 001 and 110 occur or both 100 and 011 occur; their two central positions also cover both letters. Avoidance together with occurrence of both 00 and 11 forces precisely 0^a(10)^b1^c or its complement with a,c>=2,b>=1. Three positions cover remaining 00,11 plus both transitions, proving sufficiency. If any digram absent, explicit runs or alternating cases yield two marks. Composition constraints t=b+c, n-t=a+b give two choices of orientation and exactly 2max(0,min(t-2,n-t-2)) for each n,t. Geometric series gives the bivariate rational generating function, and summation yields N3(n)=2 floor((n-4)^2/4) for n>=6. Fresh fully independent word-to-factor incidence subset search on all 2^(1)+...+2^(12) nonempty binary words checked trichotomy and counts; finite check is corroboration only.

## originality

PASS

Best-of-knowledge PASS for exact binary fixed-alphabet 2-attractor obstruction languages and weight refined enumerator; general algorithms, NP-completeness for unbounded alphabets and full string attractor results address genuinely different assertions.

## value

PASS

This solves a natural fixed-binary boundary of a general difficult string-indexing/hitting-set problem: a complete optimum trichotomy, two regular-language obstruction families and exact length/weight distribution for every length. Unlike a tiny computation, the universal classification and rational generating function give directly reusable statistics on all binary texts. The theorem deliberately does not address full-length, circular, or sharp attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
