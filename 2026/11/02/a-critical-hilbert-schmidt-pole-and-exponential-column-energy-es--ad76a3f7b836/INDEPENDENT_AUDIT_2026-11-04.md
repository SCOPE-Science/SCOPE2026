# Independent mathematical audit

## correctness

PASS

For normalized monomials e_n=z^n/sqrt(v_n(alpha)), HS²=Σ_n S_n/v_n(alpha). Partial fractions give S_n=(H_n/n²)−(ζ(2)−H_n^(2))/n (n>=1), and v_n(2)=((1+H_{n+1})²+H_{n+1}^(2))/(n+1); v_n(alpha)=∫_0^1 t^n(1−log(1−t))^alpha dt. The maximum-of-(n+1)-exponentials representation gives uniformly for alpha in [2,3] v_n(alpha)=n^{-1}(log n)^alpha(1+O(1/log n)). Together with S_n=(log n+O(1))/n² this yields S_n/v_n(2+ε)=1/[n(log n)^(1+ε)]+O(1/[n(log n)^(2+ε)]) uniformly ε∈[0,1]. The remainder is uniformly summable, so integral comparison gives HS²=1/ε+C+o(1), with C as the explicit absolutely convergent renormalized harmonic series; α>2 iff HS. Substituting u=ε log log x in the leading tail density gives normalized Exp(1) weak convergence, with fixed initial columns negligible. Critically this concerns MONOMIAL COLUMN energy, not singular values; pole coefficient depends on the exact stated weight normalization.

## originality

PASS

Identified published Hilbert-matrix boundedness thresholds and supercritical mapping results, but neither source inspected states the exact Hilbert–Schmidt Laurent pole, the normalization-sensitive finite part, or the exponential location law of column energies. Best-of-knowledge novelty is restricted to these quantitative claims; not to boundedness of the matrix. Sources not searched exhaustively.

## value

PASS

Quantifies the divergence of a natural operator ideal at the exact logarithmic boundary, including the nontrivial finite-part invariant and a universal microscopic energy-escape scale. These facts are independent of mapping boundedness and a finite table; the sharp normalization and distributional law could be reused in endpoint operator theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
