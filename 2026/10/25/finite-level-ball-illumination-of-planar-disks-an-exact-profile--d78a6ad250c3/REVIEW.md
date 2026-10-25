# Scientific review: exact finite-level planar ball illumination

## Correctness — PASS

The asserted statement covers every \(0<r<R\) and every finite \(\delta\ge0\), with the radius determined by an explicitly defined strictly increasing function. The proof constructs the complete boundary of the radius-\(R\) ball hull using two internal tangencies and proves equality with the intersection over **all** enclosing disks. A circular-segment decomposition gives the area formula; disk-inclusion yields strict increase; the singleton feasible-center limit proves the terminal area and saturation. Taylor expansions at the two opposite tangency limits yield the two different inverse exponents. These arguments cover endpoints and do not extrapolate from finite data. The bundled independent polar-integration checker tests the defining intersection directly, as supplementary evidence rather than as an infinite proof.

## Originality — PASS, with qualified risk

The directly motivating work of Oliva, Werner and Yalikun (arXiv:2607.13714, first posted 2026-07-15) develops \(R\)-ball illumination bodies, their convexity, and their small-level relative curvature measure. Its leading small-level asymptotic subsumes the small-level leading coefficient here; no independent novelty is claimed for that coefficient. Inspection of its definitions, example section, main theorems, and related proof sections did not identify the exact all-level disk radial inverse, finite saturation level, or quadratic terminal law. Lángi, Naszódi and Talata (arXiv:1110.4823) establish ball/spindle hull foundations but not this specific illumination-area formula. Werner (1994) uses the ordinary convex hull, and geodesic-ball illumination in projective geometries uses a different hull operation. Targeted mathematical searches and published-result searches did not identify an equivalent or stronger radial theorem. This is evidence of noncoverage, not a proof that no unindexed result exists.

## Value — PASS

The disk is a canonical equality and calibration model for relative-affine-area theory. A complete finite-level solution determines the actual illumination bodies, not just their infinitesimal growth, and separates a low-level fractional-power regime from a previously unquantified finite saturation threshold and quadratic approach to it. The parameter \(\delta_*\) is intrinsic, not an arbitrary truncated numerical experiment. Exact statements are useful for testing conjectures and algorithms built from radius-\(R\) ball hulls, while not claiming a general-body theorem.

## Closest literature and limitations

- Oliva–Werner–Yalikun, *Illumination bodies for ball-convex bodies*, arXiv:2607.13714. General construction and small-level theory; leading small-level constant is covered.
- Lángi–Naszódi–Talata, *Ball and Spindle Convexity with respect to a Convex Body*, arXiv:1110.4823. Foundational hull geometry; no full disk illumination area profile identified in inspected mathematical text.
- Werner, *Illumination bodies and affine surface area*, Studia Mathematica 110 (1994), 257–269. Classical convex-hull functional rather than fixed-radius ball-hull functional.
- Assouline–Besau–Werner, *Illumination Bodies in Projective Geometries*, arXiv:2605.25122. Geodesic and projective illumination examples with different hull geometry.

The claim is planar, requires \(0<r<R\), and uses the standard empty-intersection convention. Remaining originality risk is possible unindexed classical circular-arc work; no independent audit has been performed. Mathematical verification in the accompanying script is finite-resolution and does not certify continuous claims.

Self-review: passed. Independent audit: not yet performed.
