# Independent mathematical audit

## correctness

PASS

For each of the 10! permutations of exponents 1,...,10 assigned to bases 1,...,10, integer residues i^{sigma(i)} mod 10 determine a 10-bit support mask. The source proves a finite injection-state recurrence D_i(J,R); an independently written exhaustive lexicographic C++ loop enumerated all 3,628,800 permutations and reproduced histogram [K=5:9792,K=6:537408,K=7:1822464,K=8:1175040,K=9:84096], zero outside these K, including no K=10 and exact 84096/3628800=73/3150. The exhaustive finite domain is the entire claim, with no extrapolation.

## originality

PASS

Leonetti (2018 and 2026) proves precise existence/nonexistence of nice residue-permutation systems and specifically rules out n=10 because n=2p with p-1 non-squarefree. The 2026 five-page article was read fully, including Theorem 1.3 and the construction proof: no distribution for K=5,...,9 is given. These boolean existence results cannot yield the five support-size counts without additional computation. Targeted Resultary and exact-number search found no identical spectrum, but unpublished enumeration remains possible.

## value

PASS

Modulus 10 is the first even 2p case where p prime but p-1 squareful, precisely a natural boundary of the complete power-permutation criterion. The exact collision spectrum measures HOW non-nice it is, including the sharp frequency of nine residues. A full finite classification of this first arithmetic obstruction is intrinsically motivated, though narrow; it asserts no general congruence family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
