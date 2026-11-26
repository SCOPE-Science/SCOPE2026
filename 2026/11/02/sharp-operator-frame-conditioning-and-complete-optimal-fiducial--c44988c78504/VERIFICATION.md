---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently decomposed the real Hermitian frame by the four sign characters. Write Q=sum |v_i|^4 and U=(a conjugate(b))^2+(b conjugate(c))^2+(c conjugate(a))^2. The diagonal block is a circulant with diagonal 4Q and off-diagonal 2(1-Q), hence eigenvalues 4, 6Q−2, 6Q−2. Each oriented off-diagonal coordinate pair has a real two-by-two block equal to eight times the sum of the three real-imaginary outer products of a conjugate(b), b conjugate(c), c conjugate(a); the two eigenvalues are 2(1−Q) ± 4|U| in each of the three blocks. The trace is twelve and the scalar eigenvalue is four. Thus lower-frame equality or singular-value condition-number equality forces all eight other eigenvalues to be one, equivalent to Q=1/2 and U=0, also for zero coordinates. At the given seed the squared moduli are 2/3,1/6,1/6 and the real part of the square of either small coordinate is −1/48, giving U=0. Pairing the second moment against X tensor Y verifies the equivalence to S(X)=X+tr(X)I. The sum of all intensities is 4tr(X), giving the 1/16 correction. The only divisor of twelve compatible with spanning nine Hermitian dimensions is twelve; real seeds miss all imaginary-skew directions. Inspected check_a4.py and VERIFICATION.md; the recorded symbolic run was not rerun. The proof above is not limited to the script's seeds.

## originality

PASS

The general tight-measurement/design equivalence, trace obstruction, and canonical inversion are antecedents. The supported distinct claim as of the frozen record is the completed fixed-representation quartic classification with exact attainment by this signed-cycle tetrahedral qutrit orbit. A later-dated catalogue entry gives exact equivalent coverage of the core and a full spectrum; no inspected evidence places it before the frozen claim. This is not exclusive or absolute priority.

## value

PASS

The complete equality test and explicit attainable qutrit seed give an exact example of covariant informationally complete tomography over a natural nonabelian orbit rather than another generic frame inequality. The example differs from four mutually unbiased bases: the signed element fixing the hub coordinate and negating the others gives squared overlap 1/9. This is useful as a non-MUB benchmark; no statistical or phase-retrieval gain is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
