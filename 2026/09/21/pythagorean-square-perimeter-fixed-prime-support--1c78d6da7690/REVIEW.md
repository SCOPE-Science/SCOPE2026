# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. The primitive Pythagorean parametrization gives perimeter \(2m(m+n)\). If this is a square, coprimality and parity force \(m=2U^2\), \(m+n=V^2\), with \(V\) odd and \(\gcd(U,V)=1\); positivity of the second Euclidean parameter is exactly \(\sqrt2\,U<V<2U\). Exact prime support then assigns each odd prime power wholly to either \(U\) or \(V\), and the unique power of two in \(U\) converts this inequality into the stated signed logarithmic fractional-part condition. For counting, the exact relation \(P=2^{2(1-f)}V^4\) with \(f\in(1/2,1)\) permits replacing \(P\le X\) by a fixed-width perturbation of a simplex boundary. Weyl equidistribution of the irrational linear form modulo one supplies the factor \(1/2\), and direct integration of the split-simplex region followed by Vandermonde's identity gives the displayed leading constant. Independent exact enumeration reproduced the construction and approached the predicted constants for one- and two-prime supports.
- Originality: **PASS**. Yiu's full section 6.2 gives exactly the square-perimeter normal form and initial examples, and OEIS records the resulting perimeter sequences. Neither inspected source refines the parametrization by a prescribed finite odd-prime support, proves that every such support occurs infinitely often, or gives the support-wise logarithmic asymptotic. Resultary and targeted searches under prime-support, smooth/S-unit, and asymptotic terminology found no earlier equivalent theorem.
- Scientific value: **PASS**. Prescribing the complete prime support is a natural arithmetic refinement of the classical square-perimeter family. The theorem gives an exact bijection, proves every finite odd-prime support occurs infinitely often, and derives a closed asymptotic whose constant separates support size from the individual prime logarithms. This is a meaningful structural/counting result, not a finite census.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in
`AUDIT.json` and is not relabeled as independent evidence.
