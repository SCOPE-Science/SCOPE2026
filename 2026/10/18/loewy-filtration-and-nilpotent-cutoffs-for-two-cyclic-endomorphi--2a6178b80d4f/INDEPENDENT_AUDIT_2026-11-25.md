# Independent mathematical audit

## correctness

PASS

For unequal exponents the mod-p diagonal map is multiplicative since both cross terms contain p^d, and its kernel K has corner weights 1,0,d,1 in row order. For a path in a corner product, each opposed pair of crossings replaces two diagonal steps and changes weight by d-2; an unmatched crossing has cost 0 in the upper-right and d in the lower-left. Minimize with no opposed crossings for d>=2 and maximize the number of opposed pairs for d=1. These minima generate the full corner ideals: pick the single-corner factors on a minimizing path and multiply, getting the corresponding power of p (possibly zero at its output modulus), then take additive multiples. Row reduction is compatible with this multiplication, because the lower-left coefficient converts any discrepancy divisible by p^a to one divisible by p^b. K is nilpotent and has semisimple quotient, hence equals J. Counting corner residues proves every displayed order; layer zero has |R/J|=p^2 in the unequal case. The unequal quotient is reduced, so every nilpotent lies in J. The minimal vanishing powers are sharp on diag(0,p) for d>=2 and on the off-diagonal map f with entries 1 and p for d=1, since f^2=pI. For equal exponents the semisimple mod-p quotient gives J=pR; reducing any nilpotent matrix gives square zero, whence its 2b-th power vanishes, and f^(2b-1) has the nonzero upper-right entry p^(b-1). An independent exhaustive program formed the full corner sets via additive closure of all products for ten small rings across all regimes at p=2,3, scanning every endomorphism for nilpotency; every set and maximal cutoff agreed. The frozen checker was inspected, not used as independent evidence.

## originality

PASS

Credit the explicit all-power valuation profile and sharp distinction between equal, adjacent and separated exponents as a combined statement. The classical matrix form, the first radical, and the equal-case reduction argument are not independent novelty. Inspected square-zero results do not treat powers of the radical or classify the longest nonzero nilpotent iterate. The strongest plausible older chapter was inaccessible after the DOI and identified Springer PDF route; no inference of noncoverage is drawn from that limitation.

## value

PASS

This is the complete power filtration for the simplest group family with a nontrivial exponent gap, not a numerical list at a particular p. It detects exactly when alternating crossings propagate longer than diagonal steps and locates a sharp change in the maximal individual nilpotency index. The difference between ideal and element nilpotence at equal exponents is useful for interpreting the cutoff. The exact corner ideals allow layer sizes and vanishing bounds to be read off without enumerating the ring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
