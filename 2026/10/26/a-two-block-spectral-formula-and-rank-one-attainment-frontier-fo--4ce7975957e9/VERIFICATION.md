---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any real factors u,v, choose sign supports I={i:u_i≥0}, J={j:v_j≥0}. ReLU(uv^T) has two nonnegative rank≤1 diagonal rectangles (I,J) and (Ic,Jc) and zero cross rectangles. Conversely any such block matrix is achieved by choosing nonnegative rank-one factors on each diagonal rectangle and assigning opposite signs on complements, including zero/empty cases. Each fixed block cone is closed by 2x2 minors and nonnegativity; the finite union is closed, and distance to a nonempty closed subset of Euclidean matrix space is attained. For nonnegative block data the Perron nonnegative top singular vectors achieve its best nonnegative rank-one Frobenius fit with gain sigma1^2, giving the stated maximum over I,J. Independent 20 matrix/SVD partition reconstructions agree. To verify the critical rank-two 3x3 boundary without relying solely on an inaccessible paper, independently constructed X=[[1,1,1],[1,1,2],[4,3,0]] and real rank-two Theta_e=[[1,1,1],[1,1+e,2],[4,3,4-1/e]] for 0<e<1/4: det Theta_e=0, ReLU Theta_e→X, whereas every exact preimage of X has det=1 and cannot rank≤2. Thus the rank/dimension frontier is genuinely sharp. Identity matrix formula E1(I_n)=max(n−2,0) follows from at most one unit spectral gain per diagonal block.

## originality

PASS

Best-of-knowledge PASS for the universal rank-one output-set closedness and exact pair-of-block singular-value objective, and the minimality consequence. Gillis–Porcelli–Seraghiti 2025/2026 full text expressly says general direct ReLU well-posedness was open and proves attainment only for its example; Seraghiti–Vandaele–Gillis October 2026 establishes NP-hardness at rank one and general nonattainment but the complete original text could not be accessed. This missing highly relevant primary article creates a material risk that a rank-one sign-partition reduction is already implicit in the hardness proof. The scientific formulas were independently derived rather than taken from its abstract.

## value

PASS

The direct Frobenius ReLU low-rank problem can be ill-posed at rank two even on a 3x3 matrix. Establishing rank-one output closedness for arbitrary dimensions and an exact global optimization over two paired spectral blocks resolves the natural first well-posedness case and identifies the smallest dimension/rank where nonattainment can occur. The exponential partition search is compatible with NP-hardness, and the structural closedness result is useful independently of algorithmic speed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
