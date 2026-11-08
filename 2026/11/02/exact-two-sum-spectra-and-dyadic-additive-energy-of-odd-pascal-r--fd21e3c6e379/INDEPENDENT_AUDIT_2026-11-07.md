# Independent mathematical audit

## correctness

PASS

Lucas mod-2 identifies A_n with bit submasks. Each maximal run of consecutive one bits gives interval 0..2^ell-1; two summands in that block yield triangular ordered multiplicities min(v+1,2m-1-v). The separating zero bits ensure that the largest differing block outweighs all lower block differences (strict <2^h), proving unique integer sum-vector decomposition despite carries within runs. Squared triangular counts sum to (2m³+m)/3. First-run decomposition of all r-bit binary words gives F=1+zF+W+zWF with W=(6z-16z²)/(1-10z+16z²), producing rational GF (1-4z)/(1-11z+20z²). Empty support n=0 and all r>=0 included. Independent complete direct 2-sums for n<128 agree; universal proof is combinatorial, not inferred from finite rows.

## originality

PASS

Lucas submask characterization and general run-length transforms are established prior technique. No direct formula for this ordinary-integer two-sum multiplicity spectrum and dyadic aggregate was found in Resultary and the compared Pascal/parity literature; broader run-transform theory might encode an equivalent recurrence implicitly. Best-of-knowledge qualified PASS.

## value

PASS

The exact ordinary-integer two-sum representation spectrum and fourth Fourier/additive moment of natural Pascal parity sets distinguish arithmetic carries from the binary-vector cube. The evaluated dyadic aggregate is a natural complete invariant across all rows, not a one-off numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
