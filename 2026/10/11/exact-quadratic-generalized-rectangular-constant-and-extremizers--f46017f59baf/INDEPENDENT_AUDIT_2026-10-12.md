# Independent mathematical audit

## correctness

PASS

PASS: In real L4, Birkhoff–James orthogonality of unit x and y equals integral x³y=0. Put A=integral x²y², B=integral xy³. The exact quartic expansion is 1+lambda⁴+6A lambda²+4B lambda³, and Cauchy–Schwarz centered at A gives |B|<=sqrt[A(1-A²)]. The lower moment envelope D(A,lambda) is attained for every interior A by an explicit two-point distribution on any two positive finite-measure sets, with correct four moments and orthogonality. Fix lambda>0: strict concavity of sqrt[u(1-u²)] yields unique A minimizing D, parameterized by lambda(u)=3 sqrt[u(1-u²)]/(1-3u²), 0<u<1/sqrt3. An independent SymPy derivation checks the rational optimized G(u) and its exact derivative factor with quartic P(u)=9u⁴+9u³-12u²-3u+1; endpoint derivative and strict monotonicity give its unique root u*=0.200994344840... and sharp mu2=1.38784956695846... . Equality in Cauchy–Schwarz and uniqueness forces ratio y/x to take exactly the stated t± and L4 weights w±; no other maximizers. All conclusions require real L4 with at least two disjoint finite positive-measure sets, not complex L4 or mu1 or mu4.

## originality

PASS

PASS with informed best-of-knowledge primary comparisons: Gastinel–Joly 1970 was obtained via authorized Oxford access and its complete 40-page PDF was inspected in sections 7, 10 and 11; it defines the alpha-orthogonal-number family and studies the classical alpha=1/Lp bounds but does not present the exact mu2(L4) formula or full extremizer classification. Baronti–Casini–Papini 2022 likewise describes the generalized parameters and bounds, especially exponent-matched mu_p(ell_p); the published related mu4(ell4²) is a different objective. General moment Cauchy envelope is common method, but the optimized quadratic numerator and equality family are distinct. Some unindexed paper might still compute the exact same constant.

## value

PASS

PASS: An exact all-measure-space Banach-orthogonality constant and full L4 equality classification fills the parameter gap between known mu1 and mu4 examples, with a rigorous two-atom reduction and algebraic optimizer. The exact value/attainers are natural, motivated nonlinear norm geometry invariants, rather than a routine substitution of known mu_p formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
