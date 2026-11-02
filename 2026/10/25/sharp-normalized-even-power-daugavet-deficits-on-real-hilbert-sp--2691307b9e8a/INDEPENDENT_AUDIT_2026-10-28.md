# Independent mathematical audit

## correctness

PASS

Write normalized rank-one T=u⊗v with ||u||=||v||=1 and c=<u,v>. Then T^m=c^(m-1)T and ||T^m||=a^(m-1), a=|c|, for each even m>=2; T^m has nonnegative trace a^m. On span{u,v}, I+T^m is unitarily represented by an upper-triangular 2x2 block with diagonal 1+a^m,1 and off diagonal a^(m-1)sqrt(1-a^2). From determinant 1+a^m and squared Frobenius norm 2+2a^m+a^(2m-2), its largest singular value is (sqrt(4+4a^m+a^(2m-2))+a^(m-1))/2; the untouched orthogonal complement is no larger. Thus the claimed F_m(a) is exact for all dimensions >=2, including a=0,1. At m=2 direct differentiation gives unique a*=1/sqrt5, beta2=1-2/sqrt5 and rationalized exact quadratic rigidity. For c=m(1-a), a^(m-1)<=e^(-c/2) ensures compactness of maximizing c; uniform convergence mF_m(1-c/m)-> c/(2e^c+1) yields unique critical c*=1+W(1/(2e)) and limit m beta_m=W(1/(2e)), all maximizing selections. Independent 2x2 singular-value checks at seven degrees and 8 overlaps plus bounded numerical maximizations through m=2000 agreed: gamma=0.15718495148, m beta_2000 about 0.15722342, optimal c about 1.15714. These checks do not replace uniform tail analysis.

## originality

PASS

Best-of-knowledge original quantitative normalized Hilbert rank-one positive-even-power deficit profile, exact m=2 rigidity and Lambert-W asymptotic. The Langemets 2026 primary Theorem 2.2 and Kadets–Martín–Merí 2007 characterize qualitative signed rank-one-square Daugavet identities in general Banach spaces; they do not calculate Hilbert-space best finite gap, parameter-dependent norm or high-degree boundary layer. An indexed Resultary sharp rank-one Davis–Wielandt result optimizes a different functional.

## value

PASS

The Daugavet property and the rank-one-square characterization motivate measuring its exact quantitative obstruction on real Hilbert spaces, where strict convexity precludes the full property. The sharp m=2 gap, global stability around the optimum, and universal even-high-power Lambert-W boundary layer are natural operator-theoretic benchmarks not a mere renaming of a qualitative theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
