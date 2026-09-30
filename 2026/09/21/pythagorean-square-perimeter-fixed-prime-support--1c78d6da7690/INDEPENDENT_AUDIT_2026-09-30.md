# Independent audit — 2026-09-30

**Record:** `2026/09/21/pythagorean-square-perimeter-fixed-prime-support--1c78d6da7690`  
**Audited source tree:** `0ce8ba6dd5a632469c5d7374f2ad9276c06c6da0`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

## Correctness — PASS

PASS. I reconstructed the Euclidean-parameter reduction. Since P=2m(m+n) is a square and gcd(m,m+n)=1, primitive parity forces m=2U^2 and m+n=V^2 with V odd, gcd(U,V)=1, and sqrt(2)U<V<2U; then P=(2UV)^2. Exact odd-prime support therefore partitions each prescribed prime power wholly between U and V, giving the signed logarithmic condition and unique a=floor(L_A). For the counting theorem, P=2^(2(1-f))V^4 differs from V^4 by a bounded factor, so the perimeter cutoff and fixed-width s-t inequality alter only lower-order boundary layers. Weyl summation in any exponent coordinate gives the factor 1/2, and the normalized polytope volume is 1/[r(k-1)!(r-k)!]. I independently checked the Vandermonde sum for r=1,...,7 and the stated sample triangles.

## Originality — PASS

PASS, cautiously. Yiu's recreational-number-theory treatment and the corresponding OEIS entries give the square-perimeter normal form and examples, which the record explicitly credits. I found no accessible source giving the exact fixed-prime-support fractional-part classification, the assertion that every prescribed finite odd-prime support occurs infinitely often, or the support-wise (log X)^r asymptotic with the stated constant. Because the underlying parametrization is elementary and old, differently phrased recreational or S-unit literature remains a genuine residual priority risk.

## Scientific value — PASS

PASS. The record turns a classical parametrization into a complete support-wise classification and a quantitative asymptotic for every finite prescribed support. The equidistribution/counting theorem is substantially more informative than listing square perimeters and gives a reusable arithmetic description.

## Independent checks

- Re-derived the square-perimeter normal form from Euclid's parametrization and parity valuations.
- Checked uniqueness of the support allocation and the fractional-part inequalities.
- Recomputed the polytope volume and Vandermonde identity for r through 7.
- Rechecked the S={3} and S={5} numerical examples exactly.

## Literature evidence

- https://web.bogazici.edu.tr/topcu/RecreationalMathematics.pdf — Yiu, Recreational Mathematics, §6.2: classical primitive square-perimeter parametrization.
- https://oeis.org/A120089 — Square perimeters of primitive Pythagorean triangles.
- https://oeis.org/A120090 — Square roots of the corresponding square perimeters.

## Limitations

- The asymptotic counts primitive triangles, not distinct perimeter values.
- Originality is vulnerable to older problem/recreational literature using different terminology.

The assigned record package was compared file-by-file against the current default-branch package for its research, review, verification, and listed artifact files; the inspected Git blobs are unchanged. No GitHub write was performed by this audit chat. The guarded change-set below only stages independent-audit evidence and the independent-audit channel of `VERIFICATION.md`.
