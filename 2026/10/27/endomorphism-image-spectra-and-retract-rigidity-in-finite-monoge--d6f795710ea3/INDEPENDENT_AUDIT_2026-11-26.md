# Independent mathematical audit

## correctness

PASS

A signed word in x traces a walk on the path. If the walk has span b<n, lower endpoint −a and final displacement c−a, it has domain [a,n−1−b+a] on the path and rotation c−a on the cycle. These give distinct triples 0≤a,c≤b<n; span at least n kills the path and leaves k distinct rotations. Any y in the resulting monoid has chains of length at most n and cycles of order dividing k (fixed points when the path restriction is idempotent). The same walks on y depend only on the triple or, for span ≥n, on the displacement modulo k. Thus every y determines a well-defined unital substitution, independently of presentation. Identity, nonterminal idempotents and bottom rotations give image sizes 1, 2 and d+1, respectively. A path translation by ±h on an interval of L=n−b starting vertices has longest chain of 1+ceil(L/h) vertices by restricting to a residue class modulo h, and the y-cycle order is d_h. Counting walk forms for y then gives B(1+ceil(L/h))+d_h, with 2(b−h+1) such translations for fixed b,h. The substitution fixes y if y is a partial identity; for a bottom rotation by u it fixes y iff u²≡u mod k. The latter solutions are 0 or 1 on each prime-power factor, yielding exactly the unitary-divisor subgroup orders. For a nonzero path translation t, idempotence requires t²=t, hence t=1; substituting the span-b walk into its length-(L+1) chain leaves at most max(L+1−b,0) path vertices in the domain, so equality forces b=h=1 and y=x. Surjectivity forces maximum chain length n and group order k, possible only for x and x⁻¹; the latter substitution squares to the identity. This gives the polynomial, counts, retractions, and fixed-k equivalent 3/(2n). The argument includes k=1, where the bottom identity is distinct from the ambient unit and its adjoined-unit monoid has size two. Independent enumeration and pairwise multiplication tests agreed for n=2,3,4 and k=1,2,3; at (2,1) the polynomial is z+3z²+2z⁶ and there are five idempotent endomorphisms.

## originality

PASS

The classical presentation, walk forms and monogenic classification are prior structural input, and the automorphism count is close to their generator classification. The supported distinct content is the jointly quantified unital self-image-size polynomial and retraction census, including the exclusion of proper noncommutative retracts and the unitary-divisor restrictions on group-type retractions. The inspected prior statements do not supply that census.

## value

PASS

The standard finite monogenic inverse monoids form a natural class on which to ask how much of an inverse monoid survives a unital self-map. The result determines image-size multiplicities, not just which sizes occur, and reveals a stronger rigidity property: although noncommutative proper images may occur, proper idempotent images cannot be noncommutative. The latter follows from the interaction between path-width shrinkage and the idempotent congruence on the bottom rotations. This gives a complete calculation for natural self-map invariants beyond the abstract monoid census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
