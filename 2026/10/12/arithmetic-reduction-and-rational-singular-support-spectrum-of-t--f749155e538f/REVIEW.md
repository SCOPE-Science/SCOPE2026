# Scientific review: arithmetic decagonal 61-line specialization

## Correctness — PASS

The claim is for the stated cyclotomic tangent-coordinate integral model. All \(61\) lines are independently reconstructed from the ten decagon tangents and \(45\) intersections. Exhaustive exact cyclotomic arithmetic gives \(551\) geometric points, stabilizer-derived field-degree frequencies \(7,20,524\), and a full \(35{,}990\)-triple determinant census. All nonzero determinant norms have prime factors only among \(2,3,5,11,19\), proving stability simultaneously for every other characteristic; finite-field exhaustive checks handle these five exceptions. The \(\mathbb F_p\)-rationality formula follows from the Frobenius permutation on \(\zeta_5\). The attached `verify.py` reconstructs the entire claim from scratch, without stored line/point tables. Bounds: the statement concerns reduced geometric supports and does not claim modular freeness or Jacobian lengths.

## Originality — PASS

Pokora–Roulleau, arXiv:2403.20024v1, §2 Remark 2.5, previously constructed the complex \(61\)-line arrangement, proved freeness, and discussed a projective realization over \(\mathbb Q(\sqrt5)\). Kühne–Roulleau, arXiv:2312.03470v1, develop polygonal line operators and matroid realization spaces. These results and the complex arrangement are excluded from novelty. Direct primary-text comparisons and indexed mathematical-record searches for the decagon operator, characteristic reduction, sharp exception primes and Galois-point spectra did not reveal the theorem about this **fixed** integral model. The original printed last high-order incidence value is inconsistent with the universal line-pair identity; the new proof derives the relevant entry independently. Unindexed prior arithmetic computations remain a genuine bibliographic risk; searches alone do not certify priority.

## Value — PASS

The theorem classifies every residue characteristic of a canonical arithmetic representation of a recognized rigid polygonal arrangement. Its five exceptional incidence degenerations and sharp Frobenius rational-point spectrum represent complete, natural invariants of this coordinate model, not an arbitrary finite test or a generic stability slogan. The stated model dependence is essential: this is not an assertion about intrinsic minimal projective-realization field or freeness in positive characteristic.

## Literature and limitations

Sources: Pokora–Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1; Kühne–Roulleau, *Regular polygons, line operators, and elliptic modular surfaces as realization spaces of matroids*, arXiv:2312.03470v1. The proof determines geometric reduced line arrangements and fields of point coordinates for the specified cyclotomic normalization only. No independent mathematical audit or priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
