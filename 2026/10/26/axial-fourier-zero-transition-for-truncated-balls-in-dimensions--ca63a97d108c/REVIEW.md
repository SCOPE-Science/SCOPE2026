# Independent mathematical audit

## correctness

PASS

Transverse integration yields the unit transverse-ball volume times the stated polynomial integral (conjugation changes no real zero). I checked the decisive identities via Q_s+itQ=(it)^(2m+1)p, so d|Q|²/ds=2p Re((it)^(2m+1) conjugate(Q)). For m=1 this is 2pp′t⁴; for m=2 it is 2pp′t⁸−2pp‴t⁶; for m=3 it is 2pp′t¹²−2pp‴t¹⁰+2pp^(5)t⁸. Integrating from 1 to h with κ=1−h² gives exactly the three factorizations in (3). The first two are strictly positive for t≠0; the zero-frequency integrals are positive. For m=3 solving the quadratic in t² gives the stated high branch, with t=√3/δ−3√3/2+O(δ), δ=1+h. The dominant right endpoint term is 48(it)³; the left endpoint uses p_3(−1+δ)=8δ³+O(δ⁴) and its first three derivatives. The resulting scaled endpoint limits are −144√3 i and 216−72√3 i respectively, so their ratio is e^(iπ/3)+O(δ). The continuous phase difference is 2√3/δ−4√3−π/3+O(δ), hence takes every sufficiently large value 2πn. Those solutions are distinct, must approach −1, and satisfy δ_n=√3/(πn)+O(n⁻²); using t_n(2−δ_n)=2πn+π/3+O(δ_n) gives the reported frequency constant. At fixed proper h the nonzero boundary term of order 1/t dominates the order 1/t² remainder, and analyticity and positivity at zero rule out accumulation in the bounded real interval left over. These arguments are exact. The included script and recorded output were inspected, not executed; the 27 quadratures and three numerical zeros are evidence for those finite instances only.

## originality

PASS

The supported distinct statement is global axial nonvanishing at proper heights in d=3 and d=5 and the explicit d=7 near-full-ball zero sequence. The earlier indexed d=6 construction is a close and material analogue, not a theorem at these dimensions. Fixed-height finiteness and monotone-section nonvanishing are standard consequences and not credited as new.

## value

PASS

Axial nulls are a natural invariant of the cap. The proof settles all proper cuts in two odd dimensions, including the nonmonotone negative-height regime missed by standard monotone-kernel methods, and constructs an exact sequence of genuine nulls in the next odd dimension with explicit phase and cut scales. The result is not a claim about the first zero across all dimensions, nor does it rest on the standard fixed-height tail observation or on finite numerical witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
