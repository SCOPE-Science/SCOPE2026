---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Forest Gibbs law is independent bond percolation with p_e=lambda_e/(1+lambda_e), conditioned on no cyclic block all-open. In a cactus, cycles share no edges and the conditioning factors over independent bridge/cycle blocks; two connectivity indicators factor along unique block-tree route, so nonnegative local covariances multiply. On one cyclic block, group edges between 3 or 4 marks; each segment all-open indicator is independent Bernoulli before excluding all-open state. Three distinct marks and noncrossing four-mark pairings have explicit products of nonnegative terms. For crossing four-mark pairings, computed (1-abcd)N_AB-N_A N_B exactly as sum of 21 nonnegative degree-(2,2,2,2) Bernstein basis products with weights 1/8,1/4,1/2,1/4,1/8 on specified cyclic/dihedral orbits. Independent sympy polynomial expansion confirms all coefficients and exact identity; independent weighted enumeration of 8-vertex three-cycle cactus (10 edges, Z=447824916) confirmed all 28×28 pair inequalities. Exact polynomial verification plus block factorization proves general statement, finite graph test alone does not.

## originality

PASS

Çiçeksiz–Ravichandran arXiv:2610.00549 dated 2026-09-30 explicitly presents arbitrary-fugacity positive connectivity as a general conjecture and proves high-fugacity special regimes; there is no published cactus all-fugacity theorem apparent from accessible abstract. The closest original body was inaccessible: arXiv HTML/PDF alternative OA failed and Oxford returned vpn_disconnected; thus no whole-document NOT_COVERING claim, and an unexamined cactus case is a real priority risk. Bauerschmidt–Crawford–Helmuth–Swan 2021 already give arboreal-gas conditioning representation, which alone does not prove positive covariance. Resultary semantic query top12 found only different forest or cactus statements.

## value

PASS

A sharp positive-correlation theorem on all weighted cactus graphs provides a natural nontrivial class for a general arboreal-gas connectivity conjecture, allowing arbitrarily many cycles and heterogeneous fugacities. The difficult crossing-pair event requires a substantive positive Bernstein certificate, not an elementary independent-block statement alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
