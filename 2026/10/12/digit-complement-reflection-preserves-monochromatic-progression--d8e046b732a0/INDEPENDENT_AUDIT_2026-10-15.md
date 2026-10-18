# Independent mathematical audit

## correctness

PASS

The actual theorem quantifies over integer base b≥2, modulus m≥2, nonextreme length-r pattern v (r≥1), each d≥1, and finite progression lengths; leading-zero padding counts overlapping occurrences. In a fixed K-digit word, complementation exactly maps occurrences of v to occurrences of bar(v). The complemented integer b^K−1−n has K leading (b−1)-digits through the padded zone, so its canonical leading-zero convention adds exactly χ(bar(v)) boundary occurrences, where χ=1 iff bar(v)=0^t(b−1)^(r−t) with 1≤t<r. This yields the full INTEGER identity e_barv(b^K−1−n)=e_v(n)+χ(barv) for n<b^(K−r). Choosing K larger than n+(L−1)d reflects an entire finite arithmetic progression, reversing its order while uniformly translating its residues; applying the same construction in reverse proves equality of all attainable constant-color lengths, hence the two suprema, including infinite cases. No assertion for all-zero or all-maximum-digit patterns or fixed initial point. Independent fresh digit-count implementation validated 16,080 padding identities for bases 2..5, lengths 1..3, 60 inputs/pattern; these finite checks corroborate but do not replace the two-step universal proof.

## originality

PASS

The assigned reflection identifies an explicit finite-word complement symmetry not established by the inspected Sobolewski Problem 4, which asks for the values of d where the equality holds. Stronger automatic-sequence progression results in searched published records did not imply the displayed residue-shift trace transfer for arbitrary b,m,v,d. Best-of-knowledge originality passes with caveat that older digit-reflection identities outside those sources might contain the same transformation.

## value

PASS

Sobolewski explicitly formulated the nonextreme binary complement pattern equality of monochromatic progression maxima for all positive differences as a problem. The explicit boundary-corrected reflection answers it, and the proof simultaneously extends to every base and modulus with a reusable bijection of finite traces. This is a motivated structural theorem, not a mere relabeling of a single digit-pattern example; it does not purport to compute particular maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
