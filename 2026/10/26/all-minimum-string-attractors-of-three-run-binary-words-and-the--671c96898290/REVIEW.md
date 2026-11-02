# Independent mathematical audit

## correctness

PASS

For every positive a,b,c, distinct letters 0 and 1 force minimum attractor cardinality >=2. For b=1, the unique 1 must be chosen and any position in a longest zero run suffices, yielding 2a choices if a=c and max(a,c) otherwise. For b>=2 the unique 01 and 10 occurrences force the boundary pairs {a,a+b} (a>=c) or {a+1,a+b+1} (c>=a); a full factor-type partition proves sufficiency. Summing these cases gives F(z)=2z^3(1+2z+2z^2)/((1-z)^3(1+z)^2). Exact positive compositions give U_n=binom(n-1,2)-(n-2)-floor((n-2)/2); the pole order at z=1 gives mean 5/2. Independent direct factor-occurrence enumeration verified all 512 triples with run lengths 1..8 and all two-position sets, supplementary only.

## originality

PASS

Qualified best-of-knowledge comparison: the accessible primary works supply originating models or generic techniques but their inspected mathematical statements do not establish this exact complete final result; the four implication checks and specific priority risks below delimit this conclusion.

## value

PASS

The full set of minimum attractors, rather than just the minimum size, is a natural string-combinatorics invariant relevant to indexing and compression. A parameter-wide all-minimizers classification and all-length rational enumerator furnish a reusable exact result, while the rare singleton-middle-run contribution causes the mathematically informative mean-versus-typical gap 5/2 versus 1. It is not an arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
