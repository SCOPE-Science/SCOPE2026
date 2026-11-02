# Independent mathematical audit

## correctness

PASS

A denominator uv (u,v distinct primes) is an edge of a simple prime graph. After multiplying by the product P of all appearing primes, p must be a vertex and every vertex v != p must have degree at least two, since modulo v a degree-one incident term would be nonzero while all others vanish. With four distinct edges this forces target degree one or two and the only connected configurations are a paw (p pendant to a prime triangle) or C4; isolated extraneous vertices cannot occur by construction. In C4, exact algebra gives b=a+c and p=ac-a-c, forcing one of a,c=2 and (p,q,b)=(3,5,7), hence {6,14,15,35}. In a paw, parity forces triangle vertex 2, and exact partial fractions reduce reversibly to (2q-p)(2r-p-2)=p(p+6), generating exactly the stated positive odd divisor t parameters with q,r,p distinct odd primes. For p=2 four smallest distinct squarefree semiprimes 6,10,14,15 have sum 17/42<1/2, excluding solutions; at p=3 no admissible paw. Independently symbolically factored the paw rational difference, checked p=5 set {6,62,93,155} and p=13 set {14,262,917,1703}, and exact-fraction substitution for other small primes. Checked actual RESULT.md and verify.py blob paths; finite verification is corroboration rather than an infinite completeness argument.

## originality

PASS

Li 2026 gives unrestricted finite-term existence of squarefree-semiprime Egyptian expansions for squarefree rational denominators and encodes terms by prime graphs, but does not in accessible abstract classify exactly four distinct terms with target 1/p. Earlier indexed three-term prime-reciprocal classification has separate condition p+1=(q-1)(r-1), not the new paw factorization p(p+6) with C4 exception. Czenky et al. study denominators with restricted few prime supports, not every denominator a distinct squarefree semiprime edge. Complete exact four-edge graph topology plus divisor formula appears not implied by the inspected statements; Li full primary paper inaccessible so priority remains qualified.

## value

PASS

An exact natural minimal-term Egyptian-fraction classification for a prime reciprocal has content beyond a generic existence theorem: the only cycle and the entire infinite paw family are characterized by a finite primality/divisor test. The prime-incidence graph approach exposes a sharp topology restriction at four terms, and produces computable exact representation counts for every input p. No unjustified claims about density/existence for all primes or higher term counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
