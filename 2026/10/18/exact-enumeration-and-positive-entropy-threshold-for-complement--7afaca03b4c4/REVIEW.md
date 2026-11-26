# Independent mathematical audit

## correctness

PASS

The repaired result keeps the exact finite linear-word theorem. The absence indicator is the product of four correct pairwise inclusion–exclusion factors. For each forbidden triple set the two-bit suffix transfer counts every word, including arbitrary overlapping factors, and lengths zero and one are handled separately. I checked the infinite rational identity by a separate, unsigned exact computation: after starting with the four two-bit suffixes, use states (observed triple mask, suffix), append a letter unless the complementary triple has been seen, and solve H_state=1+z times the sum of continuation series over legal successors. There are 46 reachable states over 35 masks. The mask never loses a bit, so solving each same-mask block in descending size gives exact rational functions and precisely the displayed numerator and denominator, not just initial terms. Formal division gives 4+2b_n for n>=5. The cubic has one real root and a conjugate pair whose reciprocal growth moduli are lambda^(-1/2) by Vieta; the simple positive pole gives the stated C (checked numerically), and the pole at z=1 contributes four. For lengths one and two the direct run counts are correct; inclusion by length-three prefixes and submultiplicativity justify the threshold and the existence of the rate for larger factor lengths. These checks are unchanged by the repaired attribution and narrower claim of contribution.

## originality

PASS

The repaired contribution is the exact enumeration of all finite linear words avoiding complementary triples, including the precise asymptotic amplitude and additive correction. The qualitative positive-entropy boundary already follows from a published morphic construction and elementary small-length cases, and the same algebraic growth base occurs in older antisquare work. The complete word counts were not supplied or mechanically implied by the inspected sources. The repair explicitly credits the overlaps and does not claim the qualitative threshold as a separate contribution.

## value

PASS

Complementary-triple avoidance is the smallest nontrivial exponential member of an independently studied avoidance family. The repaired claim computes its entire finite-word enumeration, not just an existence witness or an already familiar base. The recurrence, exact amplitude, and four-word additive correction quantify finite-length and asymptotic behavior that is not determined by the earlier restricted-language or qualitative results. This is a useful natural counting invariant even without a general formula for larger windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
