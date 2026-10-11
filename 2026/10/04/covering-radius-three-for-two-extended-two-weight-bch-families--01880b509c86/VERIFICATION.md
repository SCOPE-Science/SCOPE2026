---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For either unextended family, two nonzero dual weights imply external distance two, hence Delsarte gives covering radius at most two. Minimum distance three and \(N=n+1<2^r\) exclude radius one by the perfect-code sphere identity, so the punctured radius is exactly two. In the parity extension, the last syndrome bit is error parity. Every nonzero last-zero syndrome therefore has leader weight exactly two; among last-one syndromes the \(N\) distinct parity-check columns have weight one, and every remaining syndrome is represented by two base columns plus the new parity column, hence has leader weight three. Thus \(L_0=1,L_1=N,L_2=2^r-1,L_3=2^r-N\) and the radius is three. Fresh independent arithmetic reproduced \((1,52,255,204)\) for Family A at \(s=2\) and \((1,86,255,170)\) for Family B at \(s=4\).

## originality

PASS

Chen-Xie-Ding explicitly leave the covering radii of their distance-optimal families as Open Problem 8.6. Their Theorems 4.2/6.2 provide the two-weight dual data for the punctured codes and Theorems 4.5/6.5 provide the distance-four extensions, but they do not state the extension radii or coset-leader distributions. Delsarte alone determines only the punctured radius; the parity-syndrome lifting lemma is the additional step that fixes every extended coset. Targeted searches found no earlier theorem or table containing these two exact extended-family results.

## value

PASS

The theorem resolves two infinite families inside a source paper’s explicit covering-radius open problem and gives the entire coset-leader weight distribution, not merely the maximum. The proof is concise because the dual spectra are unusually rigid, but the exact infinite-family classification is a natural coding-theoretic invariant with clear future use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
