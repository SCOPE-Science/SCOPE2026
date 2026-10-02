# Independent mathematical audit

## correctness

PASS

The final claim is the single counterexample at \(A=10\): the resonance function has no zero in the stated closed rectangle. The actual package contains `artifacts/verify_nozero.py`; its complete source was inspected. It propagates the exact transfer matrices with complex midpoint-radius enclosures, asserts the square-root and denominator domains, adaptively subdivides the full rectangle, and excludes zero cell-by-cell by a strict center-minus-radius margin. The exact transfer-matrix identity used to pass from the auxiliary resonance function to the scattering condition is also checked. The computation is finite and covers the whole stated rectangle, not a grid sample. The only implementation-level limitation is its explicit floating-point/libm inflation model; the reported exclusion margin is large relative to machine rounding.

## originality

PASS

No earlier source located in the fresh semantic and literature searches states or implies this exact resonance-free rectangle for the \(A=10\) symmetric square double barrier. The closest cited symmetric-double-barrier paper is numerical and uses a different potential, while the square-well paper concerns a different connected matrix-valued model. The result is therefore best-of-knowledge original as a rigorous single-instance falsification.

## value

PASS

A rigorous counterexample to a universal resonance-window assertion is a mathematically motivated boundary result: it identifies the location estimate, not the resonance width, as the obstruction at the first allowed parameter and prevents a false uniform theorem from propagating. This is more than a tiny type check because it resolves the admitted universal claim by a continuum no-zero certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
