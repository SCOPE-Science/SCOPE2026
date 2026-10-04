---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

A separate finite replay checks the enumerative layer in complementary ways.

First, for every \(1\le k\le14\), it enumerates every binary word of length \(k\) with odd Hamming weight and sends it to a canonical representative under all \(k\) rotations and \(k\) reflections. Counting canonical representatives agrees with the first fourteen terms of
\[
1,1,2,2,4,5,9,12,23,34,63,102,190,325,612,1088,2056,3771,7155,13364.
\]

Second, it evaluates the divisor-sum plus reflection formula from RESULT.md exactly using integer arithmetic through \(k=20\) and obtains the full displayed sequence.

Third, it computes the Babai--Cameron local-order numbers
\[
1,1,2,2,4,6,10,16,30,52,94,172,316,586,1096,2048,3856,7286,13798,26216
\]
through \(k=20\), and verifies throughout that
\[
2f_{N_3}(k)-L(k)=2^{\lfloor(k-1)/2\rfloor}.
\]
It ends with `VERIFY_OK`.

The replay does not independently establish the model-theoretic identification of finite \(N_3\)-types with odd cyclic compositions. That step is checked against Proposition 3.3.2 and Claims 1--2 in the primary paper, together with the explicit realization argument in RESULT.md. No independent audit has been performed.
