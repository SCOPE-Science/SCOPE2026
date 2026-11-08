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

PASS. Reconstructed from the actual frozen 24-cell RESULT.md and nine individual Git blobs. For 24 normalized D4 roots in S^3 and probability-normalized harmonic L2, the addition kernel is (ell+1)U_ell(x dot y); division by sqrt(24) on evaluation yields Gram=(ell+1)/24 M. Independent rational reconstruction enumerated all 24 sign-coordinate roots and verified R^2=I, RB=BR, RC=C, B^2=8I+3B+4C+RB, C^2=6(I+R)+4C, and BC=3(B+RB). Directly formed the five pairwise orthogonal idempotents with traces (1,2,9,4,8), verified the full Chebyshev Gram and branch spectra in degrees 0..6, and independently checked exact branch nonnegativity and ranks over degrees 0..99: (1,4,9,8,11,12,10,12,12,12,11) for ell=0..10, rank12 for ell>=11 in the checked range. No finite cutoff is used as the infinite proof: a=U_ell(1/2) and b=U_ell(0) have absolute value <=1 by periodic sine evaluation; for odd ell>=11 the two active branches 2n+8a and 2n-4a are positive, and for even ell>=12 the minimum of 2n+16a+6b, 2n-8a+6b and 2n-2b is positive (n=ell+1>=13). Direct exact checks resolve 0..10 and show ell10 retains rank11. The asymptotic nonzero squared singular-value scale 1/12+O(1/ell) is n/24*(2n+O(1))/n^2. Conventions distinguish sample Gram 24x24 from E*E on H_ell, whose nonzero spectrum agrees. Formal/expert channels are not performed; the packaged checker is finite corroboration, not proof.

## originality

PASS

PASS, qualified and with significant acknowledged overlap. Fresh comparisons locate a more relevant exact association-scheme source than the assigned self-review: Bernard et al. (2024) §2.3 equations (55)-(61) publish the generalized 24cell 4-class intersection algebra; at formal s=1/2,ell_scheme=2 it reproduces the 24cell multiplication inputs. Martin et al. (2007) already identify the 24cell 4-class Q-antipodal scheme and give a linked-design generalization. Consequently the raw 24cell class algebra, five blocks as generic scheme decomposition, and harmonic-index {2,4,10} vanishing are known/not new. However neither inspected primary states the complete degree-indexed normalized S3 harmonic Gram spectrum, nonmonotone rank table or sharp eventual full-parity cutoff ell=11, and the linked-design construction excludes the formal s=1/2 instance as theorem parameter. These arise by combining a known addition theorem with exact simultaneous spectral evaluation and Chebyshev periodicity for a natural fixed configuration. This particular combined classification survives as a best-knowledge substantive result but with unusually high risk of being considered a direct already-covered eigenmatrix corollary. The 1977 Delsarte–Goethals–Seidel full text was inaccessible; no fabricated whole-document noncoverage is made.

## value

PASS

PASS. Exact per-degree spherical-harmonic sampling on the regular D4 24cell is a natural canonical interpolation problem, not an arbitrary finite slice. The sharp rank cutoff ell=11, return of rank defects at ell6 and ell10 despite earlier full rank, complete five-mode singular spectrum and quantified high-degree near-tightness supply an independently useful conditioning and data-recovery profile, not just a sign/type normalization check. The underlying 24cell association scheme and its intersection counts are known prior work and do not by themselves establish the entire all-degree interpolation theorem or explicitly record its first permanent full rank. No further general theorem or paper-sized downstream claim is asserted. Mathematical value would substantially diminish if an older eigenmatrix table makes the entire application a mechanical known-table substitution; retained as a candid priority/value risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
