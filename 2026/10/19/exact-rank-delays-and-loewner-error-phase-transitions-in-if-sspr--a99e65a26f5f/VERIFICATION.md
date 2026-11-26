---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the conjugated equation W'=G(t), with G(t)=e^{-tA}bb^T e^{-tA^T}, the published equation (5) gives increment h(G_left+G_right)/2. In equation (6), the 1/4 entering the intermediate convex combination and the 2/3 entering the final combination give h(G_left/6+G_right/6+2G_mid/3). The order of source evaluations is left, right, midpoint, not the order suggested by the intermediate stage output labels. Composite assembly and conjugation at T reverse a symmetric stencil, leaving N+1 and 2N+1 distinct nodes, respectively. A sum of positive weighted rank-one matrices has kernel the common orthogonal complement of the node vectors, even for b=0. For the chain e^{tJ_d}e_d has coordinates t^r/r! in reversed order; selecting the lowest s powers against s distinct nodes gives a nonsingular Vandermonde minor for s=min(d,node count). The integral is strictly positive on a nonzero polynomial squared, so both step thresholds are sharp including d=1. Cauchy–Binet gives the determinant sum; each d-node minor contributes h^{d(d-1)} divided by the squared factorials and the grid refinement factor, and the weights supply h^d. At consecutive square stencils the integer Vandermonde is the product of the factorials, leaving the recorded products of weights, 1/4 or 2^{N-2}3^{-(2N+1)}, with the stated Simpson refinement factor. On a panel starting at zero the degree-two trapezoid error is h^3(1/2-1/3), and the degree-four Simpson error is h^5((1+4/16)/6-1/5). Translation adds only lower exact powers, so the total errors multiply by N. In powers t^r/r!, the first nonzero entries give the stated rank-one cases; the (0,2) trapezoid and (1,3) Simpson principal matrices each have zero first diagonal and a strictly positive off-diagonal, hence negative determinant. This verifies exactly the claimed sign regimes, not the numbers of positive and negative eigenvalues in all indefinite cases or the signs for generic A. The supplied verification.py was inspected, not executed; its rational chain tests are finite corroboration. The stage-increment, consecutive Vandermonde and scalar panel calculations above give a direct exact replay.

## originality

PASS

Credit the defining methods, their simple reduction for state-independent forcing, and the standard positive-node Gramian factorization and rank ceiling to prior foundations. The supported distinct result is sharp finite-step rank recovery on the chain together with the exact all-mesh signed-error dimension regimes for these particular methods. Strongly overlapping and broader indexed records from November 22 are documented; they are later than the October 19 record and do not establish earlier coverage. No examined antecedent gives those sharp regimes.

## value

PASS

The specified chain is controllable and has strictly positive true covariance at every positive time. Thus the sharp rank-delay result gives a concrete limit on when these PSD methods allow covariance inversion. The exact first dimensions defeating either Loewner bound on every finite mesh distinguish variance ordering from norm convergence. These are natural diagnostic boundaries, not just the textbook positive-weight rank bound or isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
