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

The one wild pole of order 4 gives different exponent 30, genus 9, and 7-rank 0 by Deuring–Shafarevich. A relative compactification check is the homogeneous equation Y^7−YZ^24=X^4+aX²Z^14+bXZ^21 in weights (7,4,1) for (X,Y,Z). On Z≠0 the y derivative is −1. At infinity X,Y are invertible; dehomogenize by the degree-one unit W=Y²/X, put t=Z/W and v=Y/W^4, and obtain v^7−vt^24=v^8+av^4t^14+bv²t^21. At t=0 there is just v=1 and the v derivative of the equation is −1. This gives a smooth proper family, with x=v²/t^7 and y=v/t^4; differentiating the chart equation gives dv/dt of order 23 and dx of order 16. The nine monomial forms with 7i+4j≤16 are therefore regular and form a fiberwise, hence relative, basis. Relative Cartier goes to the Frobenius-twisted basis, extracts the x-degree 6 mod 7, and leaves scalar coefficients from the base unchanged. Expanding y=y^7−f therefore computes the transpose Hasse–Witt matrix over k[a,b], not its Frobenius power; on perfect fibers this is the seventh power of the inverse-semilinear Cartier coefficients. Sparse symbolic expansion gives unit multiples of a,b in I₁, a²,ab,b² in I₂, and a³,a²b,ab² in I₃. Every nonzero cubic minor uses rows 1 and 2 and one of rows 3,6; the last row forces column 5, so row 2 contributes −a. Rows 3,6 cannot give separate pivots, so I₄ vanishes. Rank is 3,2,0 on the stated strata and the a-number is 9 minus this rank. The canonical embedded contribution is the kernel (a)/I₃ of the quotient to the reduced line, of length 3. In the Finding the prose describing the order of the two ideals in that quotient is reversed, but the displayed quotient, scheme, and claimed length are correct.

## originality

PASS

Published geometric overlap is substantial: characteristic-seven exclusion of a=8, rank-two linear perturbations and superspecial monomial case. The independently supported remainder is the exact universal relative minors and embedded defect in this specific family, which are not determined by geometric a-number alone.

## value

PASS

The relative scheme equations distinguish first-order and embedded degeneracies invisible to a-number tables. They give the full rank stratification and infinitesimal structure of a natural one-pole normal-form family, beyond the previously known special fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
