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

The proof is symbolic. For \(D\subseteq V(\operatorname{Cr}_n)\), the decisive data are the two selected shore-index sets \(P,Q\). The analytic checks are:

1. connected domination is impossible when \(|P|\le1\) or \(|Q|\le1\);
2. when \(|P|,|Q|\ge2\), domination always holds;
3. in that range the induced graph is disconnected exactly when \(|P|=|Q|=2\) and \(P=Q\);
4. subtracting those \(\binom n2\) exceptional degree-four sets from the independent choices of at least two vertices on each shore gives the stated polynomial.

The standalone script `verify.py` reconstructs crown adjacency and the definitions of domination and induced connectivity. It exhaustively enumerates every subset for \(3\le n\le8\), compares the literal cardinality counts to the closed formula, checks the structural criterion subset-by-subset, and verifies the minimum and total-count consequences. Its recorded output is in `verification_output.txt`.

The finite checks do not establish the arbitrary-order theorem; they only stress-test the proof and boundary cases.
