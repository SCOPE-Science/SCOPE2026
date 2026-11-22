---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Fresh reconstruction from RESULT.md at exact source-tree 732c0ccf30d82dab62a0ba9951f0fc0d57859b10: center independent edges Y_e=X_e-p and use orthogonality E[Y_TY_S]=delta_{T,S}[p(1-p)]^|T|. For each fixed four-vertex set, expanding its 4 labeled claw or 12 labeled P4 indicator configurations gives explicit support class c2,c3,c4. Independently implemented pattern generation and rational Fourier coefficients (not executing repository verifier); verified all 39 projection values at 13 distinct p=i/12, which establishes degree<=12 polynomial identities, and independently exhaustively enumerated 2^6,2^10,2^15 whole graphs for n=4,5,6 at p=1/3,1/2,2/3 with identical exact covariance. At midpoint c2=c3=0 and c4=-3/256, giving -3/256 binom(n,4). For p=1/2+lambda/n the n^6 c2, n^5 c3, n^4 c4 contributions are (3lambda^2/512,-lambda/256,-1/2048)n^4, yielding (12lambda^2-8lambda-1)/2048. Quadratic roots (2±sqrt7)/6 are simple; analytic compact convergence plus implicit-function theorem gives exactly two local roots with O(n^-2) p corrections and signs. At midpoint, three-vertex support variance coefficients are 1/256 (claw, triangle) and 3/256 (path, three wedges), giving n^5/1536 and n^5/512 and micro n*Corr=sqrt(3)/4*(12lambda^2-8lambda-1). Finite checks are only certificates of finite polynomials; asymptotics and local root statements follow algebraically. Scope limited to n>=4, 0<p<1 and fixed real lambda in compact moving windows; no global all-p zero classification.

## originality

PASS

Best-of-knowledge after actual Resultary queries, related published SCOPE primary results and primary literature. Orthogonal graph-factor decomposition and general induced-subgraph fluctuation tools are prior. The surviving specific contribution is the fully evaluated mixed induced K1,3-P4 covariance and distinct two-root 1/n covariance sign window with explicit second-order correlation. Inspected exact primary statements concern different motif pairs, component versus motif covariances, fixed-p induced count local limits or joint graph-factor limit laws; none mathematically implies the exact pair-specific coefficients and two root constants without further nontrivial local support computation. Inaccessible older full texts remain named priority risks, not proof of coverage or novelty.

## value

PASS

The two counts are canonical connected four-vertex induced graphlets used in motif statistics, so their covariance and correlation have direct natural meaning. The degree-three projection overlap vanishes at p=1/2 despite nonzero individual leading n^5 variances, exposing a truly second-order n^4 covariance from three distinct support sizes. Their competition yields a nontrivial asymmetric pair of n^-1 density sign crossings, unlike routine first-order motif covariance laws or a known graphlet table. The exact all-n moment formula and sharp microscopic sign structure can benchmark rare dependence effects in finite-network motif analysis; no unsupported joint CLT or full-density classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
