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

# Finite exact verification

Run the packaged standalone file `verify.py` using Python 3.10 or newer. No external Python packages are required.

For extension degrees \(n=1,2,3,4,5,6\), the exact point counts are \(2,2,77,602,3022,16337\). The two totally ramified poles each contribute one rational point, and each nonzero \(x\) gives five or zero rational lifts according as the trace of \(x^2+x+x^{-1}\) is zero or nonzero.

The full coefficient list in increasing powers of \(T\) is \((1,-4,-4,21,46,-100,-85,-500,1150,2625,-2500,-12500,15625)\). The code verifies the functional-equation completion and \(P_C(1)=3775\), and tests the degree-twelve polynomial modulo \(3\) using the congruence \(T^{3^{12}}\equiv T\) and the two requisite coprimality tests with \(T^{3^6}-T\) and \(T^{3^4}-T\).

For the Newton polygon, the coefficients have \(5\)-adic valuations \((0,0,0,0,0,2,1,3,2,3,4,5,6)\), giving the convex-hull vertices \((0,0),(4,0),(8,2),(12,6)\). This yields the slopes stated in the finding. Script execution returns `VERIFY_OK`.

The finite-field enumeration is exhaustive at six extension degrees, and the standard functional equation proves that those data determine the complete numerator. The code does not establish geometric simplicity, an all-family Newton polygon, or any independent audit.
