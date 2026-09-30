# Independent audit — 2026-09-29

**Record:** `2026/09/18/optimal-affine-grid-radius-equivelar-octahedron--6a52f1a9c045`
**Disposition:** **PASSED**

## Correctness

**PASS** — The lattice argument is exact. The difference lattice has index 60, the displayed B also has determinant 60, and A=B^{-1} sends all 24 published vertices to integer points, so every integer-valued coordinate row lies in the stated dual lattice. The finite inverse-matrix bound reduces all covectors relevant to radii below 84/90 to q in [-3,3]^3; exact enumeration gives the claimed short-width directions. Three independent rows therefore force width at least 168, while the displayed translate attains radius 84. The eight possible low-width independent triples all fail the orthogonality test for the conjugated C4 action, and the displayed commuting map attains radius 90.

## Originality

**PASS** — The current Mizhaev paper publishes the exact integer realization and C4 symmetry but does not claim coordinate minimality. Searches did not locate an affine-lattice width optimization or the sharp radii 84 and 90. The older 2020 precursor remains a specific overlap risk: open-access discovery did not yield inspectable full text in this run, and the authorized Oxford retrieval repeatedly timed out, so no claim is made about its contents.

## Scientific value

**PASS** — The result gives a sharp and reusable arithmetic normalization theorem for a newly published polyhedral certificate. It improves radius 300 to the exact affine optimum 84 and quantifies the additional cost, to 90, of preserving the published order-four symmetry as Euclidean.

## Independent checks

- Recomputed the gcd of all full-rank 3x3 minors of the 23 difference vectors as 60 and checked det(B)=60 and integrality of A v_i.
- Enumerated q in [-3,3]^3: only +/- (1,0,0) have width below 168; below 180 there are exactly the five projective directions listed in the record.
- Enumerated all eight independent triples of those five directions and checked exactly that M T M^{-1} is never orthogonal; checked the exhibited affine maps attain radii 84 and 90.

## Findings

- The lower bounds are finite exact certificates, not heuristic coordinate searches.
- The distinction between global realization minimality and minimality inside the published affine-equivalence class is stated correctly.
- The 2020 precursor could not be read; this is recorded as a literature limitation rather than silently treated as negative evidence.

## Literature evidence

- https://arxiv.org/abs/2609.17700 — Ruslan Mizhaev, Integer Realization of an Equivelar Octahedron of Genus 3; current arXiv abstract confirms the 24-vertex, 36-edge, eight-nonagon integer realization and C4 symmetry.
- https://doi.org/10.31219/osf.io/hvtey — Mizhaev 2020 precursor. Open-access discovery did not yield inspectable full text during this audit; authorized Oxford retrieval job 2732e2de8e503159f92ee1eb0feb5c7f timed out on repeated revisits. Its contents are therefore not claimed as read.

## Limitations

- The radius 84 is only optimal inside the affine-equivalence class of the published realization; it is not a global optimum over all realizations of the abstract map.
- The radius 90 theorem additionally fixes the conjugacy class of the published C4 action as a Euclidean symmetry.
- The 2020 precursor full text was inaccessible in this audit, leaving an explicit historical-overlap risk.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
