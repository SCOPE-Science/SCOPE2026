# Independent mathematical audit

## correctness

PASS

PASS. The complement T of a proper P3-convex set is nonempty and has induced minimum degree ≥2r−1. Induct on number r of cyclic factors. Base r=1 requires an adjacent edge, with exactly k cyclic pairs. Slice along a maximum-length coordinate K and write M=N/K. If a slice is empty, the next nonempty slice must contain every vertex of the connected (r−1)-dimensional product and its following slice must also be full, forcing |T|≥2M with equality exactly two adjacent full slices. If every slice is nonempty, each induces minimum degree ≥2r−3, so induction gives at least 2M/L vertices per slice for L≤K the largest remaining factor, yielding total ≥2KM/L≥2M. Equality forces K=L and every slice to be a minimum lower-dimensional two-layer slab; each vertex then has exactly 2r−3 intralayer neighbors and must have both cyclicly neighboring slice copies, making every slice identical. Thus all minimizers are precisely tK distinct two-layer slabs. Every nonpercolating seed closure is a proper convex superset, so equality forces that seed itself to be one of these. Independent exhaustive search checked all nonempty subsets up to the sharp bound for C4,C5,C4□C4,C4□C5 and found only 4,5,8,5 expected slabs; the proof, not these samples, covers arbitrary r and side lengths.

## originality

PASS

PASS qualified. Saraf–Borse–Mundhe Lemma 2.5/Corollary 2.6 already give sharp minimum-degree core size and construct a minimum width-two slab, so neither the scalar threshold nor any example is claimed new. Their stated theorem does not identify the complete equality locus; forcing every optimal solution to a slab in all dimensions, with tK tied-factor count, needs an equality-case induction. Dourado P3-convex counting does not assert torus-specific rigidity.

## value

PASS

PASS. Equality-case classification of an already sharp extremal theorem is an independently meaningful structural result: all worst-case 2-neighbor nonpercolating seeds are explicitly known, including tied longest-factor symmetry and exact multiplicity. The proof discovers a rigidity not contained in merely knowing one optimal slab.

The dated certificate retains the supplied scientific assessment, sources and limitations.
