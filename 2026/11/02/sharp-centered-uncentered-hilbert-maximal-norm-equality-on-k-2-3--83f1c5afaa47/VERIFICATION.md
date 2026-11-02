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
# Verification instructions and limits

Run `python3 verify_k23.py` in the directory containing this document and the script. Only the Python 3 standard library is used. The graph consists of two vertices numbered 0 and 1, three numbered 2–4, and all six cross edges. The code recovers graph-distance balls from that edge list by breadth-first search, then checks every legal uncentered choice of an averaging ball at each output vertex.

The expected successful output is:

`CERTIFICATE_OK selections=4500 strict=4499 exceptional=1 threshold=171/100 root=(8+sqrt55)/9`

The code independently checks five exact integer leading Sylvester principal minors for each of the other 4,499 matrices using fraction-free elimination, and checks the winner's invariant eigenspaces. Here the matrix with integer entries is 60 times the row-normalized ball incidence matrix, and the threshold matrix is 6156 times the identity minus its integer Gram matrix. All tests are strict integer comparisons, not tolerances.

The proof's exact invariant-space calculation gives the winner's Gram eigenvalues \(1\), \(1/9\) twice, and the two roots of \(9\lambda^2-16\lambda+1=0\). An additional exact symbolic calculation of its characteristic polynomial and eigenvector equation returned the stated polynomial and zero residual. The positive eigenvector picks only centered balls, which establishes both norm equality and all equality cases.

These checks pertain only to \(K_{2,3}\), use the stated graph-ball and counting-measure definitions, and do not prove a result for larger bipartite graphs. They are research verification, not an independent scientific audit.
