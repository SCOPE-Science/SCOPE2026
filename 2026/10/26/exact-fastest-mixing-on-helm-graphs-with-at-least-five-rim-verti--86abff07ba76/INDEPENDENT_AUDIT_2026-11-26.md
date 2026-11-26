# Independent mathematical audit

## correctness

PASS

The dihedral average preserves all constraints and cannot increase the centered spectral norm. In the first nonzero Fourier mode the rim diagonal is at least c(1−1/n−r), and the Rayleigh vector (1,1+sqrt(1−c)) cancels r because −c+2t−t²=0. Equality for this vector forces both hub and rim budgets tight and then the eigenvector equation fixes r=ρ. The solution is positive; the bound ρ≤δ/2+pc/(2δ) from the displayed denominator gives ρ<1/2 for 5,6 and for n≥7 separately by the stated sine bounds. This leaves q>0. The attained first Fourier eigenvalue is M and is the largest nonzero-mode eigenvalue by the ordering in cosine. The quadratic positivity check gives M≥1−p; shifting the block at cosine −1 by (1−p)I gives a positive matrix in semidefinite order, its determinant being ρ(2−p−2ρ). The two radial eigenvalues are the roots of z²−(1−p−2ρ)z−p(1−ρ); evaluating at 1−ρ, 0 and −p−ρ locates both within [−M,M]. This verifies two-sided SLEM and only invariant uniqueness. Expanding δ=√2π/n+O(n^−3) gives the stated second-order optimum gap and pendant limit. With all three weights 1/n the radial roots are 1−2/n+O(n^−2) and O(n^−1), and all Fourier eigenvalues are uniformly positive for sufficiently large n since those blocks equal I+O(n^−1) uniformly in mode. Their largest occurs at k=1 and has gap (3−sqrt(5))/(2n)+O(n^−2), giving the stated ratio. Supplied symbolic and numerical checks and their recorded scope were inspected, not executed; the proof, not the 40 finite spectra, certifies the family.

## originality

PASS

The strongest inspected SLEM precedents solve the wheel (no leaves) and the sunlet (no hub); the exact-helm match minimizes a different objective. The universal leaf-corona theorem also has a different structural hypothesis: the helm adds leaves to the rim only, and the wheel is not regular or vertex-transitive for the sizes in scope. The supported distinct contribution is the exact two-sided helm optimum and invariant edge weights under the hub and rim constraints together, not symmetry averaging or Fourier reduction.

## value

PASS

Adding one hub and private leaves produces competing transition constraints on a standard graph family. The exact all-size SLEM resolves those constraints simultaneously, shows that zero holding at the hub and rim is forced for the invariant solution, and quantifies a roughly 31% asymptotic gain over maximum-degree weighting. An exact calibrated example of this three-orbit fastest-mixing problem is useful even without a general theorem for other graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
