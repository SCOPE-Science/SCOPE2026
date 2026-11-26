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

Each nonroot vertex contributes one independent category (a successor of type s with mass lambda*nu_s, or a nonedge); root type and loop are independent of this sample. Depth-zero formulas are exactly evaluable by a type, including arithmetic tests of depth zero. This gives the finite multinomial sum, including n=1 with an empty sample. Finite structural elimination of current-state indicators, even nested indicators of depth-one formulas, leaves Boolean combinations of integer-affine tests in the sample counts. Drift signs are eventually correct with probability tending to one, by LLN. Zero coefficient rows are evaluated as constants, not passed to the CLT. On nonzero balanced rows the bounded offset disappears under sqrt(n-1) scaling: the covariance in the type basis is positive definite, since u^T Sigma u>=lambda(1-lambda)*sum(nu_s*u_s^2). The finitely many zero hyperplanes are simultaneously null, so there is joint convergence of the Boolean sign predicates, and averaging over root and loop gives a finite weighted cone expression. Every nonempty strict sign cell is open and has positive mass; homogeneity makes strict feasibility equivalent to a rational unit-margin LP. Testing true feasible cells for zero and false feasible cells for one handles both endpoints and a vacuous family of tests. The witness's one-vertex contribution has covariance (1/2,1/2;1/2,3/2), from which the orthant formula gives the stated angle. If alpha/pi were rational then 2cos(2alpha)=2/3 would be a rational algebraic integer, impossible. An independent small rational-bias check of this formula's finite census, using convolution and direct enumeration of increment sequences at lambda=3/5 and type masses (1,2,3,1)/7 in order 00,01,10,11, gives matching truth probabilities 17/35, 397/1225, 12122/42875, 440893/1500625 for n=1..4. Inspected but did not execute the frozen checker. The finite computation does not certify the limit or the LP equivalence; no assertion extends to nested successor counts.

## originality

PASS

Limited to the effective endpoint classification for the full stated depth-one fragment at rational graph parameters. Fair-model convergence and its drift/CLT/Gaussian-cone mechanism are already obtainable from Ghosh–Schwarzentruber through edge-marker translation; the orthant calculation is an instance of their general method. The new part supported by the comparison is a uniform rational zero/one decision theorem, with a type-basis normalization, constant-row handling and strict-cell support characterization that works for arbitrary Boolean combinations and arbitrary rational biases. The individual first-moment and LP ingredients are standard.

## value

PASS

A decision theorem for both limiting endpoints is useful even when convergence and approximate integration are known, since neither decides exact equality to zero or one. The result resolves this for a whole syntax fragment with balances, contradictory comparisons, indicators and loops, without having to evaluate any Gaussian integral. The witness demonstrates why this general classification must allow intermediate values and why an exact finite rational census alone does not identify the type of limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
