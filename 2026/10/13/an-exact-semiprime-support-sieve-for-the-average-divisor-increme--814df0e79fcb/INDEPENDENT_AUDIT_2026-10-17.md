# Independent mathematical audit

## correctness

PASS

For n=pq (distinct primes) σ(n)=(p+1)(q+1), τ(n)=4; thus the increment equality becomes 4σ(pq+1)=5(p+1)(q+1). If p,q are odd, pq+1 is even and σ(pq+1)>3(pq+1)/2, implying (p−5)(q−5)<24. This excludes p≥11, leaves two explicit p=7 failures, and the stronger even/odd-divisor split excludes p=5. For p=3 an even divisor bound and congruences force q≡11 (mod12); putting q=12r+11 gives m=3q+1=2(18r+17), reducing the equation reversibly to σ(18r+17)=20(r+1). For p=2, m=2q+1≡3 (mod4), its divisor sum is a multiple of 4, forcing q≡15 (mod16). Every logical reversal and strict-boundary condition has been checked against the provided proof. An independent divisor summation tested 4,822 prime pairs up to product 100,000 and verified larger witnesses 753 and 148173; finite tests do not prove unbounded exclusion.

## originality

PASS

OEIS A066176 exactly defines and tabulates the increment equality but does not state any unbounded squarefree-semiprime least-prime obstruction or reversible p=3 reduction. Literature on arithmetic numbers classifies integrality of σ/τ alone; results about consecutive equal divisor sums are distinct equations. Searches of the published corpus did not identify a stronger covered statement.

## value

PASS

A066176 defines a natural divisor-increment property. The result converts an infinite squarefree-semiprime search into just two least-prime possibilities, sharply constrains their residue classes, and gives a reversible exact odd-divisor-sum condition for p=3. This is useful arithmetic structure of a natural sequence, not a mere recomputation of known terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
