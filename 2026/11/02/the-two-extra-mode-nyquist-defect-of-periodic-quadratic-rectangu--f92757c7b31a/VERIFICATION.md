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

Independently parameterize a cell polynomial by its four corner values, interpolated bilinearly, plus free coefficients c_x,c_y of x^2-1 and y^2-1. This is exactly the six-dimensional total-degree P2 space. In a Fourier character (z,w), continuous vertex values come from one common amplitude V. The two slopes of the bilinear part at the center are a_x=V(z-1)(1+w)/4 and a_y=V(w-1)(1+z)/4. The edge-average derivatives are a_x±2c_x and a_y±2c_y in reference coordinates; physical scales are constant within each direction and cancel. Matching yields 2(1+z)c_x=(z-1)a_x and 2(1+w)c_y=(w-1)a_y. With neither character -1 the two bubbles are determined by V. With just one -1 its equation forces V=0 and leaves precisely its one directional bubble free. With both -1 neither equation restricts V or the two bubbles; bilinear interpolation of the alternating corner values is Vxy. Hence the three listed checkerboard modes are independent and exhaustive in that character. The sum of complex dimensions equals the real dimension on complexification. This derivation also works with two cells in either direction: interfaces are indexed modulo the mesh, with each physical edge and its identification imposed. It supplies the all-size rank proof without running the frozen finite checker.

## originality

PASS

The continuity conditions themselves are established reduced rectangular Morley conditions. The distinct claim is the exact periodic dimension and kernel fiber: bounded rectangular Morley results use different global constraints, and the cited periodic parity comparison concerns P1. No inspected matching source states or directly implies the P2 torus result.

## value

PASS

This is a natural periodic trial space for a physically motivated continuity condition. Exact parity and explicit shapes tell a basis builder when two additional degrees of freedom are required and which local components carry them; the bounded-domain dimension cannot provide this information. This is a dimension mechanism, not a claim of defective Hessian energy or solver instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
