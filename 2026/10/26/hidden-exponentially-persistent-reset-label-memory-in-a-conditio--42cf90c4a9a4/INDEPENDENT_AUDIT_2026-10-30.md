# Independent mathematical audit

## correctness

PASS

Starting at +a the flip probability at duration u is f_a(u)=J_a(gamma u)^2/2+sum_{n>a}J_n(gamma u)^2. Exponential waiting yields p_a=b_a/2+sum_{n>a}b_n, b_n=(lambda/(pi gamma))Q_{n-1/2}(1+lambda^2/(2gamma^2)). First-reset conditioning gives C(t)=e^-lambda t+(lambda e^-lambda u(1-2f_a(u)))*C(t); kernel is nonnegative with integral 1-2p_a<1. Integrating yields 1/(2lambda p_a), not a single exponential in clock time. p_a-p_{a+1}=(b_a+b_{a+1})/2>0 proves strict increasing memory. The positive Legendre integral at cosh eta has Laplace endpoint asymptotic Q_{n-1/2}~sqrt(pi/(2n sinh eta))e^-n eta; a geometric ratio bound justifies summing the tail and fixes the coefficient (gamma/lambda^2)sqrt(2pi a sinh eta)tanh(eta/2)e^{a eta}. Bessel Taylor and one-reset conditioning give the t^{2a+1} onset; repeated-reset paths have higher order. Independently compared Bessel-integral and Legendre flip transforms for bounded rates and n, including positivity/order; large-a finite samples are not a proof of uniform asymptotics.

## originality

PASS

The original conditional-reset tight-binding paper specifies the model, position probabilities and Bessel/Legendre transforms; these are acknowledged prior. Its studied one-time occupations do not by themselves supply the event-anchored two-time reset-sign persistence and sharp integer-distance asymptotic. General renewal identities from Perfetto and Rose furnish tools, not the evaluated model-specific p_a and its onset/monotonicity. Primary Acharya–Gupta material was inspected for the reset rule and spectral transform. No claim of original general renewal equations. Remaining risk of model-specific two-time calculations under hidden-memory terminology.

## value

PASS

An experimentally meaningful two-time classical reset record can remember the initial sign exponentially longer as reset locations separate despite a symmetric one-time sign law. The exact integrated lifetime, non-Markovian clock distinction and high-order onset distinguish two protocols with otherwise identical symmetric one-time statistics; the distance exponent and prefactor supply a nontrivial quantitative phase-space relation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
