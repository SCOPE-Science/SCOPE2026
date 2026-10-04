# Review

## Correctness
PASS. For each translation, the STFT row is exactly the Fourier transform of the pointwise product \(f\overline{T_xg}\). With two-point supports, the difference geometry has only two possibilities: four distinct translation differences, giving four one-point rows, or three translation differences with row intersection sizes \(1,2,1\). A nonzero one-point row has full Fourier support. A two-point row has at most one Fourier zero because the nonzero support difference is invertible modulo the prime; it has one zero exactly when the displayed coefficient ratio is a \(p\)-th root of unity. These facts give the three support sizes and their complete equality conditions.

## Originality
PASS relative to the inspected literature and database searches. Krahmer--Pfander--Rashkov give the lower bound that specializes to \(3p-1\), and their extended report displays small-order support data, but neither inspected source states an all-prime two-sparse trichotomy or characterizes equality by support alignment plus a root-of-unity cross-ratio. Nicola classifies the global support-minimizing STFT pairs at level \(p\), a different extremal regime.

## Value
PASS. Two-sparse pairs form the first nontrivial sparse STFT stratum. The result turns a known lower bound into a complete exact support spectrum and isolates separately the additive-geometric obstruction and the coefficient-phase obstruction. This supplies a reusable base case for sparse Gabor-support questions rather than a single numerical instance.

## Closest literature and limitations
The closest result is Proposition 4.3 of Krahmer--Pfander--Rashkov, which supplies the lower bound \(3p-1\) but not the present equality classification. Their 2007 technical report includes finite diagrams for small cyclic groups. Nicola's 2022 preprint classifies the universal minimum \(p\), not the two-sparse level. The theorem does not address higher support sizes or composite cyclic groups.

Same-model review: passed. Independent audit: not yet performed.
