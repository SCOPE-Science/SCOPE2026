# Independent mathematical audit

## correctness

PASS

Read the entire RESULT.md, check.py, and frozen six auxiliary files. Independently reconstructed B=e^(τLh) with p=(e^−x+e^−3x)/2, q=(e^−x−e^−3x)/2, noise multipliers with E d=1 and E d²=m=e^(ζx), and the exact 2×2 moment map K=[[m u,v],[m v,u]], u=(y+y³)/2,v=(y−y³)/2. Its positive Perron eigenvalue crosses one once as m increases: det(I−K)=1−u−m(u−y⁴), so m_*=(2+y+y²)/(y(1+y+2y²)). Writing F=2+g(x)/x, g=log[(2+y+y²)/(1+y+2y²)], independently verified gʺ=8y(y−1)(y+1)(y⁴+12y³+10y²+12y+1)/[(y²+y+2)²(2y²+y+1)²]<0. Limits are F(0+)=3 and F(∞)=2. The nonnegative initial covariance projects positively onto the Perron eigenvector; at λ+=1 the other eigenvalue is <1, yielding a strictly positive finite limit. Conditional E||U_{k+1}||₁≤e^(−x)||U_k||₁ and summable Markov bounds imply pathwise eventual e^(−γ k), 0<γ<x, by Borel–Cantelli even for signed initial vectors. The semidiscrete Itô second moment generator has leading sign threshold ζ=3. Independent SymPy verified the determinant, curvature factorization, and exact x=log2/log4 witness; not an infinite proof.

## originality

PASS

The original 2023 preprint/2024 Bréhier–Cohen–Ulander forward method gives positivity and fixed-finite-horizon mean-square convergence under CFL; it does not state this repeated fixed-grid exact spectral frontier. General mean-square tensor spectral-radius criteria (Lang–Petersson–Thalhammer, BIT 2017) provide the abstract test but not this specific nontrivial rational/logarithmic formula, monotonicity, and almost-sure/second-moment mismatch; Chen–Dang–Hong concerns another boundary/θ scheme. The classical distinction between almost-sure and mean-square stability is not claimed original. Best-of-knowledge PASS with method-specific caveat; no assertion of exhaustive priority.

## value

PASS

Long-time stability is a natural question left open by finite-horizon convergence of positivity-preserving splitting. The exact all-steps/noise classification provides a sharp demonstrable failure mode: for 2<ζ<3 increasing a time step alone destabilizes second moments although the semidiscrete SDE remains mean-square stable and the numerical scheme remains positive and almost-surely decaying. This is a structural numerical-method counterexample with a full sharp frontier, not an isolated toy simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
