# Independent mathematical audit

## correctness

PASS

Set a=n^2, offsets 1,n+1,n+2. For each residue r in [0,a), write r=q(n+1)+s, 0<=s<=n, q<=n-1, with q=n-1 implying s=0. The offsets represent r in L=max(q,s) terms, so the nonnegative semigroup has a representative w=aL+r<=n^3+n^2-2 in every residue. Therefore all integers m>=n^3-1 are representable by subtracting multiples of a; if w>m then w>=m+a>n^3+n^2-2. Conversely n^3-2 must use <=n-1 nonbase generators; offset t is congruent a-2 modulo a and below 2a-2, forcing t=a-2. If L<=n-2 then t<=a-4. For L=n-1, reducing n-1 largest offsets by n is impossible: only changes 1 or n+1 are available and n copies of the former cannot fit. Hence F=n^3-2. Separate independent modular Dijkstra/Apéry computations confirm all n=2,...,40, not the infinite assertion.

## originality

PASS

A concrete exact Frobenius number for a natural adjacent-offset quadratic four-generated family is not contained in the materially inspected published eventual quasipolynomial theorem, which applies to different parameter ranges/generator counts. Four generators are genuinely minimal for n>=3; the finite n=2 redundancy is disclosed. No matching older formula found in bounded searches, which is not proof of priority.

## value

PASS

The exact all-n conductor of a simple quadratic four-generator numerical semigroup resolves a natural parametric Frobenius instance beyond the principal published three-generator EQP theory. Its adjacent-offset structure and boundary-case proof make it a self-contained useful exact invariant; no general four-generator conjecture is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
