# Scientific review: lattice Fourier zeros of the standard 4-simplex

## Correctness — PASS

The exponential-simplex identity expresses the transform as a divided difference of the exponential at five phase nodes. For distinct integer nodes all exponential values equal one, so the divided difference vanishes. For repeated nodes, the confluent-residue expression is a rational-coefficient polynomial in \(s=i/(2\pi)\). Transcendence of \(\pi\) makes a zero equivalent to an identically zero polynomial. The multiplicity partition of five leaves only one tied-maximum case, namely two repeated endpoints and a singleton. Its lowest coefficient vanishes exactly when the singleton is the midpoint; direct residue summation then proves the entire expression is zero. All other repeated patterns have a unique maximal multiplicity and a nonzero lowest coefficient. The exact checker verifies the residue-polynomial identity on a finite window; the proof, not enumeration, covers all integer frequencies.

## Originality — PASS, qualified

The general exponential-simplex formula is classical and is not claimed as new. The inspected 2008 primary source gives Brion's vertex-sum formula and notes that the meromorphic summands' poles cancel. Borda's 2016 paper gives a general Fourier representation for simplices and discusses coincident projections and higher-order residues. The 2024 polytopal zero-set paper rules out entire complex spheres and certain parametrized curves in the zero set; it does not state this discrete integer-lattice classification. Searches for the exact four-dimensional node-multiplicity classification returned nearby finite-group support problems but no same-object statement. A 2023 polyhedral form-factor paper is a plausible adjacent source: its abstract and a related public implementation were inspected, but its full text was not accessible, so priority remains qualified.

## Mathematical value — PASS

The result is a complete infinite classification of exact blind frequencies for a canonical simplex window, not a selected numerical example. It identifies the first dimension where repeated phase nodes can cancel and isolates the only multiplicity geometry responsible for that new resonance. This distinction matters when interpreting reciprocal-lattice samples of simplex indicators in Fourier quadrature and Poisson-summation calculations.

Self-review: passed. Independent audit: not yet performed.

## References

1. V. Baldoni et al., *How to Integrate a Polynomial over a Simplex*, arXiv:0809.2083v1 (2008), Corollary 12 and Remark 15.
2. B. Borda, *Lattice points in algebraic cross-polytopes and simplices*, arXiv:1608.02417v1 (2016), Section 2.3.
3. M. N. Kolountzakis and E. Spyridakis, *Curves in the Fourier zeros of polytopal regions and the Pompeiu problem*, arXiv:2404.03405v1 (2024), Sections 1–3.
4. T. Yang et al., *Form factor of any polyhedron and its singularities derived from a projection method*, J. Appl. Cryst. 56 (2023), 167–177, DOI 10.1107/S160057672201130X (abstract and related public implementation only).
