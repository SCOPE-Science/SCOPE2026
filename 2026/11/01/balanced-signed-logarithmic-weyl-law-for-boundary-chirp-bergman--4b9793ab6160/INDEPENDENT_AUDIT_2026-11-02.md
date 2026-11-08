# Independent mathematical audit

## correctness

PASS

PASS: The weighted beta moment in the monomial basis and s=t/(1-t) substitution give L_n=e^{ic} Gamma(n+alpha+2) U(n+1,-alpha,-ic)/Gamma(alpha+1). The DLMF 13.8.11 fixed-argument large-first-parameter expansion and K-Bessel asymptotic at the principal nonreal z=-ic yield a nonzero complex leading magnitude a^(alpha/2+1/4)exp(-sqrt(2ca)) and phase sqrt(2ca)+c/2-pi(alpha/2+1/4)/2. The error is complex relative O(a^-1/2), hence an absolute normalized real-error rather than a spurious cosine-relative bound. An integral comparison gives O_v(sqrt(N)) phase exponential sums for v≠0, proving sqrt(n) equidistribution. Lower/upper logarithmic² cutoffs and density 1/2 of positive/negative phases yield N±~log²/(4c); exponential damping gives all Schatten classes. Independent exact hyperu moment vs leading computations for alpha=-1/2,0,1 at n=20,80,250 show shrinking relative error; numerical phase fractions approach 1/2. Neither finite tests nor saved VERIFY_OK prove the infinity result.

## originality

PASS

PASS, best-of-knowledge: Looi 2026 constructs oscillatory radial Toeplitz symbols with nonzero essential spectrum and an essential-positivity counterexample, not the compact root-exponentially damped signed counting law. Li–Wang gives qualitative compactness criteria, Rozenblum disk results assume different support conditions and Bargmann examples use a different model, and Rozenblum–Vasilevski considers trace-class form criteria. DLMF 13.8.11, diagonalization and Weyl criterion are credited, not claimed as original. El-Fallah–Mahzouli–Marrhich–Naqos 2016 eigenvalue-decay source remains inaccessible beyond abstract and a material priority risk; Oxford authorized retrieval reported VPN disconnected.

## value

PASS

PASS: The explicit oscillatory bounded symbol has no boundary limit and does not decay, yet cancellation produces membership in every Schatten class with infinitely many eigenvalues of BOTH signs. The sharp signed logarithmic² spectral distribution, exact coefficient and phase/weight universality are natural quantitative operator invariants that go beyond qualitative compactness. The theorem does not assert a universal radial-symbol Weyl law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
