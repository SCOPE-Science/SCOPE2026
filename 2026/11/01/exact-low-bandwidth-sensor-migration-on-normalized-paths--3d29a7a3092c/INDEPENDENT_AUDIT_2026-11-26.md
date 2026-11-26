# Independent mathematical audit

## correctness

PASS

The degree-weighted cosine modes satisfy the normalized adjacency eigen-equation, including the endpoint recurrence; the sum of degree-weighted squares is 2(n-1) for the extreme modes and n-1 otherwise. Distinct selected spectral values give a nonzero Vandermonde factor independent of location. The remaining ratio is d_j^m times the product of squared cosines, including m=n because the exceptional normalization cancels. By reflection it suffices to compare products on the first half with the endpoint threshold 2^(-m/2). For m=2 monotonicity and cos(pi/3)=1/2 give the cutoff and ties. For m=3 the minor lobe has maximum 2/(3sqrt(6)), and cos(pi/6) gives product sqrt(3)/4 in the increasing-in-cosine major lobe, above both the minor lobe and endpoint threshold. The small orders up to 6 give interior products at most 1/4 (for n=6 use cos(pi/5)cos(2pi/5)=1/4). For m=4 the cubic has stationary values on the signed pieces at y=(5±sqrt(7))/12; the minor-lobe maximum (10+7sqrt(7))/108 is below F(7/8)=21/64, and for n>=10 the first neighbor has y>7/8. The remaining exact products match the listed ties: n=4 interiors are all 1/4; n=5 all 0; n=6 the two (sqrt(5)±1)/16 values are below 1/4; n=7 only j=2,4 give 1/4 and the other internal products vanish; n=9 the odd indices give 1/4 by the half-angle values and the even interiors give zero. At n=8 the three first-half squared cosines lie in the three open intervals stated in the proof; the relevant pieces of F are monotone there with supremum 1/4, so none ties. In the general regime, n-1>2.5m^(3/2) places the first neighbor in the principal lobe and the cosine product exceeds 1-2pi^2/75>1/sqrt(2). Monotonicity is strict before the first zero; beyond it a nearest integer to pi/(2theta) is an admissible k, bounding one absolute cosine and hence the full product by 1/sqrt(2). The first neighbor also beats the endpoint threshold. The finite checker was inspected without execution; it is corroboration rather than the source of these uniform and exact comparisons.

## originality

PASS

The Vandermonde method and sampling framework are prior, and a later-dated Resultary finding explicitly states the identical m=2,3,4 classification including every tie. Another later-dated finding overlaps on the determinant ratio, three-mode transition, and eventual inward migration with a cubic sufficient cutoff. These are substantive equivalences, not independent evidence of earlier priority; catalogue dates alone do not establish research order. No inspected earlier statement supplies the exact low-band spatial table or the all-bandwidth O(m^(3/2)) sufficient cutoff. The full motivating Paley–Wiener paper was accessed for this review, and its relevant path comparisons optimize different quantities or concern different sensor sets. This PASS is limited to the supported normalized-path spatial classification and stronger quantitative localization, not the determinant reduction itself.

## value

PASS

Single-node sampling with equal-variance noise gives a natural determinant design problem. Exact spatial maximizers and ties decide whether sensors belong at the boundary or one vertex inward, and distinguish low-band from full-band behavior; this is not determined by a rank or observability test. The all-bandwidth sufficient threshold is useful even without sharpness because it guarantees inward localization on an explicit smaller-than-cubic length scale. The finding does not purport to maximize the least singular value or optimize the time spacing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
