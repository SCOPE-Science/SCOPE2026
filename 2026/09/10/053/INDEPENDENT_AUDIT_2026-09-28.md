# Independent Audit — 2026/09/10/053

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `04e430c64e1368d81934c2d8d4b5e3535beae18a`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS

The central geometric correction is correct. The unit square P*=conv{(1,1),(2,1),(1,2),(2,2)} has ordinary area 1, four boundary lattice points and no interior lattice points by Pick, hence the dual four-valent vertex has weight 0; each side is primitive, hence all incident tropical edge weights are 1. With one square plus unimodular triangles filling 4Δ2 (area 8), area counting forces 14 triangles. The dual graph therefore has V=15; side-incidence counting gives 17 bounded/interior dual edges, so b1=17-15+1=3. Lee–Len Theorem 4.4 states that a genus-3 tropical plane quartic has seven bitangent classes, each of multiplicity 1. Thus a multiplicity-2 mother cannot occur for the named subdivision. Splitting the primitive square along either diagonal gives two unimodular triangles, so the local smoothing remains genus 3; regularity of either circuit refinement follows by a sufficiently small signed perturbation of the square heights.

## Originality

**Verdict:** PASS

Lee–Len supply the general multiplicity theorem, but the inspected source does not evaluate the named central unit-square subdivision or diagnose the target’s erroneous genus-2 premise. Searches for the exact central-parallelogram configuration did not locate an earlier statement of this instance-level impossibility. The contribution is therefore an application/diagnosis rather than a new general bitangent theorem.

## Scientific value

**Verdict:** PASS

The correction is scientifically useful because it invalidates the proposed wall-crossing experiment at its premise: the target object does not carry the multiplicity-2 class whose daughters were to be compared. This prevents an incorrect genus-drop interpretation and cleanly separates weight-zero four-valent degenerations from genuinely genus-dropping walls. Its scope is narrow but directly tied to a motivated tropical-quartic construction.

## Limitations

- Only the specified central primitive unit square is covered; other parallelograms with interior lattice points or higher edge weights may have genus drop and higher bitangent multiplicities.
- No claim is made about real lifting of the seven multiplicity-1 classes.
- The novelty is instance-specific application of Lee–Len plus elementary lattice/Euler calculations, not a new general multiplicity theorem.

## Literature and evidence

- [Lee–Len, Bitangents of non-smooth tropical quartics](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/20199/Bitangents_of_non_smooth_quartics.pdf?sequence=1): Theorem 4.4 gives multiplicities 2^(3-g)-1 and 2^(3-g); in particular genus 3 has seven multiplicity-1 classes. The source does not evaluate the named P* subdivision.
- [Cueto–Markwig, Combinatorics and Real Lifts of Bitangents to Tropical Quartic Curves](https://doi.org/10.1007/s00454-022-00445-1): Open-access smooth-quartic bitangent shape/lift theory; it does not supply the nodal unit-square genus computation claimed here.

- Independent Pick/area/dual-Euler computation gives genus 3 and primitive edge weights.
- Lee–Len Theorem 4.4 was checked in open-access full text.
- Repository research files were read at the assigned tree; no GitHub writes were made.

Repository evidence was read from `SCOPE-Science/SCOPE2026`. No repository writes were made by this audit.
