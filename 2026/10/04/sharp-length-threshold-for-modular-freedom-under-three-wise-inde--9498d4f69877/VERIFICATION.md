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

The universal statement is proved analytically. The accompanying
`verify_threewise_modular_threshold.py` uses only Python standard-library exact
rational arithmetic.

For each replayed residue vertex it:

1. constructs the sharp low-variance zero-skew lattice law;
2. constructs the four-point higher-variance zero-skew law;
3. interpolates exactly to variance \(n/(4q^2)\);
4. maps the lattice variable back to a Hamming-weight law in one residue class;
5. checks support, nonnegative masses, total mass one, and all first three
   factorial moments;
6. checks that at most five Hamming weights are used.

It separately replays the nearest-lattice second-moment obstruction below the
pairwise barrier and the explicit cubic third-moment obstruction at
\(q^2-1\), \(q^2\), and \(q^2+1\).

Replay result:

`VERIFY_OK construction_cases=20094 support_points=100075 pairwise_obstruction_checks=173558 third_moment_boundary_checks=591`

Finite replay is not used as a proof for untested moduli. The proof in
`RESULT.md` supplies the universal inequalities.

Originality was assessed by statement-level comparison with the cited
limited-independence, discrete-moment, and orthogonal-array literature.
Independent audit has not been performed.
