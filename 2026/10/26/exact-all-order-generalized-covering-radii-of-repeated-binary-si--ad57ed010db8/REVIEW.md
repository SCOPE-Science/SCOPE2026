# Independent mathematical audit

## correctness

PASS

The binary generator has rank two, and every nonzero binary word has exactly two nonzero blocks, giving [3m,2,2m]_2. For t rows and alphabet V=F_2^t of size Q, any code array has constant block values u,v,u+v, and any three mass-m histograms are realizable as targets. Distance is 3m minus the maximum agreement A(u)+B(v)+D(u+v). Maximize A first, then average B(v)+D(u+v) over v; each of the two integer bounds gives its own ceiling. For m=sQ+r use s of each symbol in each block. At r=0 there are no extras; at 1<=r<=Q/2 place the first two extra sets in an index-two subgroup and the third in its complementary coset, so exactly two but not three extras can align. For r>Q/2 every extra multiplicity can be bounded by one, and the lower bound forces the resulting maximum to attain three extras. This gives the stated ceiling formula in all residue cases. Each ceiling is at least one, and both become one precisely when Q>=2m, so the claimed first order and the fixed-order normalized limit follow. The frozen checker includes exhaustive small histogram and raw-target loops and bounded random checks, not an all-parameter proof. python3 -B /workspace/reproduce_finite.py 5 independently exhausted 5,256 received arrays over six (t,m) pairs using bitwise unions of row disagreement supports, rather than histograms. All six radii matched; no frozen script was run.

## originality

PASS

The block metric and its scalar-extension and geometric interpretations are not new. The supported distinct result is the two-ceiling exact law for every equal repetition and order, including the first order reaching redundancy, not the existence of a terminal redundancy cap. The same-day and other exact covering records concern different code families. The strongest inspected general results and targeted ordinary-radius comparisons do not supply the family-specific sharp construction or evaluation.

## value

PASS

Equal repeats of the three projective directions give a natural family interpolating between a tiny parity-check code and long low-rate codes. Knowing the exact joint covering hierarchy means knowing the worst number of columns needed for simultaneous correction and when extra order finally reaches redundancy. The residue-dependent exact law and additive extremizers convey more than the general redundancy cap or a finite table, without extrapolating to arbitrary repetitions, higher dimensions or other characteristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
