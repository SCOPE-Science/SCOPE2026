# Independent mathematical audit

## correctness

PASS

For no-flux Legendre H=-(z(1-z)psi′)′, E_n=n(n+1), rational alternatively ordered formal Gram moments, the weighted derivative norms I_j=integral w^{2j}(psi_n^{(j)})^2 satisfy I_{j+1}/I_j=(2j+1)/(2(j+1))*(E-j(j+1))^2/(4E-(2j+1)(2j+3)); division-free form covers vanishing derivatives. Iterate to central-binomial product for every diagonal. Rational moment recurrence plus physical-level interpolation establishes off-spectrum identity, and parity symmetry removes resonance at odd moment steps so all formal matrix entries equal the actual Gram matrix at every physical E_n. In each interval between lambda_j=j^2-1/4 poles, one diagonal has exactly one negative denominator factor except at the single physical squared numerator zero. Thus for all K>=2, 0<=E<(K-1)^2-1/4, away from poles, PSD iff E_n with n<=K-2. An independent SymPy exact-integration check for j=1..4, n=0..7 agrees; finite tests are only supporting checks, not the all-K proof.

## originality

PASS

PASS best knowledge: Sword-Vegh primary full arXiv HTML inspected, paper explicitly reports numerical positivity to K=5 and arbitrary-K proof open (section 4.4). Exact all-j product plus negative single-diagonal arbitrary-size proof not included in inspected prior statements. Matrix ordering and rational off-spectrum normalization tightly specified.

## value

PASS

Resolves the original explicit arbitrary-K positivity question analytically, with factored spectral zeros and poles and a simple certificate; significant upgrade over finite positivity experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
