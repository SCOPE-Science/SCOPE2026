# Independent mathematical audit

## correctness

PASS

For q=min(k,n-k)>=2 and c=n-q>=q, the independently inspected RESULT.md uses the rectangular hook-length count D(q,c)=(qc)! product_{i=1}^{q-1}(i!)/product_{j=c}^{c+q-1}(j!) and the Schubert-cell count E(q,c)=binom(q+c,q). At q=2 the degree is Catalan C_c; c=2,3,4 yield (D,E)=(2,6),(5,10),(14,15), and c=5 gives (42,21). The exact ratio inequality reduces to 3c^2+c-4>0 for c>=5. For q>=3 the q-by-q square admits an injective tableau extension from a 3-by-q rectangle, and the three-row count F_q=2(3q)!/[q!(q+1)!(q+2)!] exceeds binom(2q,q): F_3=42>20, and the ratio inequality reduces to 23q^3+32q^2-q-6>0. For fixed q, the degree side-extension ratio product_{j=1}^q(qc+j)/(c+j) exceeds the Euler extension ratio (c+q+1)/(c+1), because qc>c+q for q,c>=3 and other factors exceed one. Therefore strictly D>E for all q>=3, with no equality. Independently rechecked the ratio polynomial and finite exact hook-degree normalization, and read the actual package verifier; finite checks are not an infinite proof.

## originality

PASS

The primary Eremenko–Gabrielov formula identifies degrees and rectangular standard tableaux, while the Euler characteristic is the independent Schubert-cell count. The published Resultary log-concavity cutoff concerns comparing D_{n,k-1},D_{n,k},D_{n,k+1} at fixed n, not comparison with Euler for every (n,k). Their formula plus the cell count alone determines both integers, but neither inspected source gives or mathematically entails without further cross-parameter inequalities the three-exception classification; the proof supplies exactly those strict growth comparisons. This is a best-of-knowledge non-covered global threshold rather than a claim that rectangular-tableau folklore is exhaustively known.

## value

PASS

The two invariants are canonical quantities for the same Grassmannian/Bruhat rectangle: number of Schubert cells versus saturated maximal chains. The exact all-parameter, strict crossover with three smallest line-Grassmannian exceptions and no equality is a natural structural inequality between distinct enumerative invariants, not a mere table row or substitution; the proof gives stable threshold propagation across both rectangle dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
