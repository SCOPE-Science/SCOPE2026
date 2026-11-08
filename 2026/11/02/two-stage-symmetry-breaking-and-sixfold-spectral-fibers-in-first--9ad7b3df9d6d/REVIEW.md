# Independent mathematical audit

## correctness

PASS

Read frozen RESULT.md and its assumptions (unit normalized h1, Plancherel Fourier convention, whole frequency axis, a>0, full L2). For fixed x integrate |V_h f(x,xi)|^2 over all xi by Plancherel to obtain exact H_a=M_{F_a}, F_a(t)=∫_{t-a}^{t+a}2u² e^{-u²}/sqrt(pi) du. Derivative w(t+a)-w(t-a) yields unique outer stationary root b=a coth(ab)>a and, for a>1, inner valley u=a tanh(au); center has F_a(0)=8a(1-a²)e^-a²/sqrt(pi), at a=1 first nonzero quartic positive. The outer-versus-central height difference has strictly positive derivative 2[w(a)-w(a+b)] for a>1 and opposite signs at endpoints, establishing unique sharp global switch. On every open monotonic branch, analytic changes of variables make pushforward spectral measures AC, finite nonzero-level fibers show no point spectrum, inverse-branch counts give 2/4/6 a.e. multiplicities. Explicit independent bisections recovered a*=1.07766362837624 and b*=1.23823662176807; numerical evidence is supplemental to the infinite-a derivative proof. No bounded-frequency rectangle or higher Hermite order is claimed.

## originality

PASS

Best-knowledge: distinct precise final statement not implied by inspected prior work; exact comparisons and known subclaims separated. Inaccessibility of some sources alone not a scientific failure; residual risks stated. Checked Hermite Toeplitz equivalences do not themselves furnish the sharp a-dependent global peak switch or sixfold spectral fibers, though unrecognized sliding-window formulas could reformulate this result. General localization/large-sieve norm bounds and quantization machinery do not imply the complete exact multiplier fiber classification in the specified full-frequency strip geometry.

## value

PASS

Complete sharp concentration-norm phase transition in a natural first-excited Hermite localization geometry, including a separated local/global bifurcation, nondifferentiability and the entire continuous-spectrum fiber multiplicity. The exact boundary matters beyond routine evaluation of one integral, including operator spectral type and extremizing-location discontinuity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
