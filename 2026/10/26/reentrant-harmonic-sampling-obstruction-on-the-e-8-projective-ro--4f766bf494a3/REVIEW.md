# Scientific review

## Correctness — PASS
The claim is one complete even-degree rank classification for degree-\(\ell\) spherical-harmonic sampling at the 120 projective \(E_8\) root lines. The exact 120-line root enumerator checks each pair and every common-neighbor count, establishing the finite \((120,63,30,36)\) graph data. The addition theorem gives the rank correspondence and the three algebraic levels. Direct Gegenbauer expansions settle even degrees 0 through 10. For the infinite range \(\ell\ge12\), a positive-coefficient polynomial identity proves strict diagonal dominance without a numerical extrapolation. The degree-eight normalization and condition number are recomputed from exact integer dimensions. All critical steps are explicit in RESULT.md, with finite arithmetic reproducible from check_e8.py.

## Originality — PASS under bounded literature comparison
The prior exact characteristic-matrix identity and the projective \(E_8\) adjacency parameters are fully credited. Their published statements do not report the all-even-degree rank classification, the nonmonotone rank-120 / rank-119 transition between degrees 8 and 10, or the proof that rank 120 holds at every even degree at least 12. Published research-record searches for the same spectrum, degree-ten defect and alternative terminology returned no equivalent statement. The main residual risk is an uncatalogued representation-theoretic treatment or a previously derived specialization of the general Delsarte formula; neither a failed search nor the local partition establishes global uniqueness.

## Mathematical value — PASS
The 120 projective roots are a distinguished exceptional tight design. The exact answer gives a nontrivial interpolation threshold and a reentrant failure: a single homogeneous harmonic degree 8 spans all 120 data directions, degree 10 misses the constant data vector, and every even degree at least 12 recovers full interpolation. The degree-eight sharp singular conditioning quantifies stability, not just algebraic rank. This is a complete natural spectral classification, not an arbitrary parameter slice or a generic addition-theorem restatement.

## Closest literature and limitations
Delsarte–Goethals–Seidel (1977), Theorems 3.3, 3.6 and Example 8.4, establish the addition theorem and tight design; Coulangeon (2006) relates E8 lattice layers to spherical designs; Schmidt (2022), Section 3.1, identifies the 120-line strongly regular graph. General formulas are not misrepresented as new. The result is restricted to even degrees and is not independently verified. A published implicit treatment using the same Bose–Mesner algebra may exist.

Self-review: passed. Independent audit: not yet performed.
