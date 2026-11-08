---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

PASS. All definitions and normalizations reconstructed from assigned RESULT.md and seven fetched Git blobs, including p>=2,q>=1 and q=1 zero-multiplicity boundary. Direct disintegration: given lower x, upper y_j are independent uniform on [max x,1+min x]; writing R=max x−min x, the minimum-range Jacobian is p(p−1)r^(p−2), with remaining factor (1−r)^(q+1). This gives vol=p!(q+1)!/(p+q)! and R~Beta(p−1,q+2), while A=(1−R)T with T uniform independent. Randomly place lower endpoints and p−2 independent uniform interior coordinates; center C=A+R/2. With E(1−R)^2=s and ER²=t, conditional lower centered diagonal variance t(p+4)/(12p), off diagonal −t/[2p(p−1)], and upper diagonal extra s/12. Total covariance exactly gives stated five coordinate classes, lower contrast (p+1)(p+2)/[12(n+1)(n+2)], upper contrast s/12, and two-dimensional mean block M. Its determinant is [p s²+(q+1)(p−2)st/p]/144>0. Independent scratch calculation (not executing the source checker) computed 11 exact rational full covariance determinants from the extrema mixture and compared them with the claimed block eigenvalues; all matched. Direct polynomial chamber integrals checked 7 moments for (p,q)=(2,1), obtaining volume 2/3 and covariance [[3/40,1/40,1/20],[1/40,3/40,1/20],[1/20,1/20,1/10]]. Asymptotics: beta concentration R→alpha, two independent centered bounded uniform-sum CLTs, Slutsky, and exact independence of T prove the JOINT limit (beta(U−1/2),N(0,1/12)) with independent coordinates; beta=1−alpha. Trace/determinant M show eigenvalues n beta²/12 and alpha beta/12 (leading scales), contrast limits alpha²/12,beta²/12; Stirling yields L→1/sqrt(12) and kappa/n→beta²/min(alpha²,beta²). An independent symbolic n→∞ check at alpha=2/5 confirms both mean-mode eigenvalue limits. Finite calculations corroborate but do not establish infinite claims; the analytic conditional measure, CLT and Stirling argument supplies them. No John/Löwner metric assertion is implied.

## originality

PASS

Best-of-knowledge PASS with credit for known two-sided poset-Lipschitz construction, alcoved volume methods and ranked central symmetry. Inspected the direct 2017/2018 source full-text and three related published original RESULT mathematical proofs. None of the inspected results implies complete p,q coordinate covariance, two-scale joint CLT, isotropic-constant limit, and sharp linear condition-number behavior. Search absence is not proof; exact volume may be obtainable from earlier general permutation statistics and is not asserted as new in isolation. Nonobvious equivalences and general moment theorems remain priority risks.

## value

PASS

PASS. The ordinal sum of two antichains is a canonical non-tree poset family for Lipschitz polytopes, and its entire Euclidean-coordinate inertia—not merely volume or a contact ellipsoid—is a natural geometric invariant. The result determines exact all-size covariance and reveals distinct mechanisms for persistent common translation (uniform component) and Gaussian inter-level gap with parameter-free variance. The cube-limit affine isotropic constant coexisting with linear condition-number divergence is a motivated, nontrivial shape phenomenon; this explicit contrast is not a routine consequence of prior central symmetry or lattice-volume combinatorics. No general-poset result or downstream application is needed to make the exact structural classification worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
