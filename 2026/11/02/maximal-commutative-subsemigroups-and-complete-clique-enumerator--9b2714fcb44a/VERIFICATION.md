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

# Reproduction and limits

Run `python verify.py` with Python 3.9 or later. No third-party libraries are used. The script constructs each finite group by an explicit multiplication operation; it forms Brandt products directly, compares products in both orders for every pair, enumerates all cliques by a recursive extension algorithm, and separately checks whether each clique is inclusion-maximal. It then computes the predicted polynomials from integer multinomial coefficients, inclusion–exclusion and finite polynomial multiplication. The two methods are independent in their construction of the tested graph and the prediction.

The code checks the groups \(C_1,C_2,C_3,C_4,C_2\times C_2,S_3\), with the index sizes shown in each printed case, for a total of ten configurations. It also checks all ordered pairs of labeled nonzero elements in \(B_2(C_4)\) against those of \(B_2(C_2\times C_2)\) under an explicit label bijection. The expected final output ends with `GRAPH_ISOMORPHISM_OK C4_vs_V4 n=2` and `VERIFY_OK 10 independent finite multiplication checks`.

These computations exhaust the **specified finite configurations only** and establish neither the theorem for arbitrary groups nor publication priority. The universal statement is proved in `RESULT.md` from direct semigroup multiplication, closure of maximal commuting sets, and a finite inclusion–exclusion identity. No independent audit has been performed.
