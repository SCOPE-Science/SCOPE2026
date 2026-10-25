# Scientific review: Kummer biplane minimum supports

## Correctness — PASS

The construction is precisely the block complex of sixteen translates of the size-six difference set. The finite field calculation proves that facial triples are exactly those whose symplectic pairing is one. The explicitly defined edge cocycle vanishes on all 320 facial triangles and evaluates to one on all 240 omitted triangles. The binary boundary rank is 104, while the full complete-graph cycle space is 105-dimensional, establishing a unique nonzero first-homology class. The Gram-matrix bound excludes noncarriers of more than six vertices. The standalone verifier reconstructs 65536 induced subsets and independently establishes the sixteen maximal six-point exceptions, the complete enumerator, all 60 isotropic planes, and the affine orbit. The finiteness of the domain is essential; no asymptotic or infinite claim is made.

## Originality — PASS with residual risk

The closest previously published computation gives the exact integral homotopy type \(\mathbb{RP}^2\vee\bigvee^{55}S^2\) for the same block complex. Therefore its first mod-two Betti number is prior knowledge, not a new theorem. Its available full RESULT text does not classify three-point homology supports or seven-point universal carrier thresholds. White's biplane surface embedding and Matsushita's general fundamental-group theory do not imply these exact cycle supports either. The new statements require the cochain and binary symplectic incidence analysis. Targeted searches for equivalent minimal homology supports, missing triangles, and Kummer biplane neighborhood-complex systoles identified no covering statement. An unindexed equivalent statement cannot be ruled out, and the historical first-release day of White's 2004 publication is not verified.

## Mathematical value — PASS

The exact support profile answers a natural structural question that the known homotopy type cannot resolve: which smallest vertex sets geometrically detect its nontrivial first-homology class? The result identifies every shortest representative, explains its symmetry through isotropic geometry, and proves a sharp universal seven-vertex guarantee with exactly sixteen maximal exceptions. This is a complete classification of a natural invariant rather than an arbitrary parameter slice or a recomputation of the Betti number.

## Reproducibility and limitations

`artifacts/verify_kummer.py` is executable with Python 3.9+ standard library alone. It performs exhaustive finite checks, including a direct \(\mathbb F_2\) boundary-rank elimination; these establish the listed finite facts, not an unclaimed integral classification or extension to other designs. Relevant historical work is identified in the references in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
