# Independent audit — SCOPE-20260914-011

Date: 2026-09-28 (UTC)  

## Disposition: REPAIRED

### Correctness
The counterexample is correct, but the committed cusp verifier was not formally rigorous because it converted saved decimal interval endpoints to binary64 before reconstructing mpmath.iv boxes. I independently rebuilt the cusp cross-section directly from the saved decimal Krawczyk boxes, face pairings and peripheral-curve integers and obtained Re(theta_6)=[0.4654775688468905,0.4654775688495280] and Im(theta_6)=[1.1939928091790021,1.1939928091826787]. I also checked strict K(X) subset int(X) from the saved endpoints; the smallest coordinate margin exceeds 9.99997e-9. Thus N_6 remains a certified counterexample. The repair makes the cusp parser exact-decimal and fixes repository-relative paths.

### Originality
Moderate as an explicit certified value/counterexample. Martelli-Petronio classify exceptional fillings of the magic manifold and Purcell studies cusp-shape deformation generally, but the retrieved literature does not provide this certified theta_6 enclosure.

### Scientific value
Moderate-to-high: it rigorously resolves the admitted uniform-band claim by a concrete hyperbolic filling and leaves a reusable interval certificate.

### Repair
Replace RESULT.md and METADATA.json to state the independently reconstructed enclosure and correct artifact paths; replace artifacts/lane1841_cusp.py so saved interval endpoints are parsed directly as decimal intervals rather than narrowed through binary64; replace the derived cusp JSON with a conservative certified enclosure.

### Sources checked
- Martelli and Petronio, Dehn filling of the magic 3-manifold: https://arxiv.org/abs/math/0204228 — Classification context for fillings of the magic manifold; it does not supply the certified cusp-modulus enclosure used here.
- Purcell, Cusp shapes under cone deformation: https://arxiv.org/abs/math/0410233 — General cusp-shape deformation background; not a covering computation of theta_6.
- SnapPy complex cusp-cross-section source: https://github.com/3-manifolds/SnapPy/blob/master/src/snappy/geometric_structure/cusp_neighborhood/complex_cusp_cross_section.py — Used to independently reconstruct the exact cusp-translation accumulation from the stored topology and interval shapes.

### Limitations
- Only n=6 is certified.
- The interval computation uses mpmath.iv without a second-library cross-check.
- The slope convention is the fixed standard SnapPy framing.
