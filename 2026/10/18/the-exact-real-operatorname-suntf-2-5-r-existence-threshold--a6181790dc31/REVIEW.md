# Independent mathematical audit

## correctness

PASS

The doubled-angle projector formula converts each layer's tightness to zero sum of five unit phasors, and converts a phasor real inner product x to squared overlap (1+x)/2. The proposed triplet and pair have real sums s and -s, with s^2=3/2; cycling the triplet preserves tightness. Reconstructing the three accumulated overlaps gives (s^2-3)/2 within the triplet, -s^2/2 across the blocks, and 3(s^2/2-1) in the fixed pair. All are -3/4, so the squared overlaps average 3/8 for all ten pairs. The two pentagonal frequency rows have zero sum; the real part of the sum over the four nontrivial fifth roots yields the required two-frequency sum -1/2 at every nonzero offset. Stacking the size-2 and size-3 constructions generates every R>=2 while preserving the weighted average and all layer identities. Tightness makes the one-layer constant 3/8, so the doubled-angle Gram matrix would have eigenvalue 5/4 four times and rank four in a plane, impossible.

## originality

PASS

The strongest checked literature explicitly leaves R=3 open for the identical real (2,5) SUNTF definition. The distinct indexed pentagon and qubit results address different properties or layer counts. The supported new case is R=3; the rest of the classification follows by stacking and a known one-layer obstruction.

## value

PASS

An exact real solution to the explicit three-layer open case gives the missing generator for all possible layer counts, establishing a sharp threshold rather than adding an arbitrary example. The small radical construction can be reused without relying on numerical optimization or tolerance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
