# Scientific review: maximal midpoint instability

## Correctness — PASS

The proof gives all quantifiers for a complex countable Hilbert-space diagonal unitary. The two-dimensional lemma follows from positive-semidefinite saturation, together with the scalar-diagonal polarization argument; the antipodal obstruction is a rank-one square-zero pair with exactly unit numerical radius. All infinite-dimensional matrix entries of a putative midpoint decomposition vanish by two-coordinate compressions. Approximate antipodal eigenpairs yield numerical-radius contractions whose midpoint tends to the unitary while their separation tends to \(2\). The upper bound \(2\) is immediate from the triangle inequality. Explicit angles are nonzero but tend to zero. The packaged checker verifies numerical identities and finite matrix corners; the infinite proof is analytic.

## Originality — PASS, with risks

The closest primary source, Mal (2022), Theorems 2.7–2.9, proves finite-dimensional diagonal extremality, and Theorem 2.11 treats compact normal operators in infinite dimension. The diagonal infinite-dimensional extremality lemma follows from Mal's compression argument and is **not itself presented as new**. The claimed additional phenomenon is simultaneous exact extremality and full diameter \(2\) in **every** approximate-midpoint neighborhood, which requires an explicit uniform obstruction and is not stated or implied by the inspected finite-dimensional theorem alone. Kadets et al. (2019) treat general strongly extreme points, not this numerical-radius counterexample. Targeted repository and literature searches did not identify an implication-equivalent stronger theorem. Residual risk: another unindexed numerical-radius geometry article could already give this separation, possibly in MLUR terminology.

## Mathematical value — PASS

This distinguishes extreme points from their maximal possible quantitative failure of strong extremality **inside a natural operator norm**. Unlike arbitrary renorming examples, the witness is a simple diagonal unitary and the mechanism is precisely an accumulation of almost-antipodal eigenvalues: no finite-dimensional obstruction exists, yet arbitrarily small midpoint neighborhoods have the entire ball diameter. It supplies a sharp boundary for attempts to infer quantitative stability from finite-dimensional numerical-radius extremality. It makes no unsupported claim of classifying the uniformly separated spectrum case.

## Relationship to literature and remaining limitations

Mal, *Numerical radius norm and extreme contractions of* \(\mathcal L(H)\), arXiv:2210.09734v1 (18 October 2022), §§1–2, Theorems 2.7–2.11; Kadets–Martín–Merí–Pérez–Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257v1, §2. Both primary texts were materially inspected. No result for continuous-spectrum unitaries or uniformly separated diagonal spectra is claimed.

Self-review: passed. Independent audit: not yet performed.
