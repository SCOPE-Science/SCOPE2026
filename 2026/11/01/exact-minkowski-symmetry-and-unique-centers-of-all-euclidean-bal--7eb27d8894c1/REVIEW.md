# Scientific review

## Correctness — PASS

The nonstandard step is the sharp lower constraint from the upper rim of the spherical truncation. For any reflected inclusion, the pole imposes \(z_1+\lambda\le a\). Maximizing the squared transverse length over the full rim yields \((z_1-\lambda a)^2+(\|z_\perp\|+\lambda\sqrt{1-a^2})^2\le1\). For \(\lambda\) above the proposed value the first inequality forces the sharp scalar contradiction \(\lambda^2-a\lambda\le(1-a)/2\). The candidate translation \(z=(a-\lambda_a)e_1\) satisfies the whole ball and halfspace inclusion directly for every point, with equality at the required contacts. At equality, no transverse or axial slack remains, proving uniqueness. The parabolic blowup is checked directly by its own apex/rim constraints. The proof covers every finite \(d\ge2\), every \(-1<a<1\), and the separate full-dimensional paraboloid. The standalone code independently returned 106,853 successful diagnostic checks; no infinite statement is inferred from samples.

## Originality — PASS, qualified

The exact half-ball value \(1/\sqrt2\) and its unique center are **previously known** (Belloni--Freund 2008, Section 3.2), so the claim explicitly does not assert that instance as new. Belloni--Freund prove general properties but do not present the complete truncation-position curve. Den Hertog--Pauphilet--Soali (2023/24) give a robust optimization formulation and other explicit classes, not this one-halfspace-clipped sphere. Xiong--Freund (2026, arXiv:2608.30876) prove a universal rounding inequality assuming an input symmetry number, not an evaluated symmetry for each cap height. Brandenberg--González Merino--Grundbacher (2026, arXiv:2607.27041) study general stability near simplex extremality. Searches for circular segment, truncated ball, spherical cap, parabolic cap, Minkowski symmetry, their reciprocals and elliptical-cap affine equivalents found no broader covering formula. Published mathematical records about *outer* asymmetry of translated disks have a different invariant. Residual priority risk remains because a short calculation may have appeared in older geometric optimization or stereological sources.

## Value — PASS

The reflection symmetry of a one-halfspace-clipped ellipsoid is a natural geometric input to symmetry-dependent rounding and to computational Minkowski-center benchmarks. An explicit continuously varying all-dimensional profile is not determined by knowing the one half-ball case. The sharp contact geometry and uniqueness provide exact parameterized test instances; the dimension-independent golden-ratio value of the thin-cap paraboloid is a nontrivial geometric endpoint that cannot be read off from the degenerating point without affine blowup. The claim does not assert a general rounding optimum and is not a trivial naming change.

## Limitations and nearest literature

Only one non-tangent clipping hyperplane is considered. Equivalent older evaluations remain possible; publication priority has not been independently established. The half-ball subcase is prior. All arguments are analytic and explicitly separate the degenerate cap from its affine blowup.

Self-review: passed. Independent audit: not yet performed.
