# Independent mathematical audit

## correctness

PASS

PASS: Arithmetic independently recomputed in F_41[u]/(u²−3): 3^20≡−1 mod41; λ=2+16u has λ^840=40, λ^560=20+25u, λ^336=18, λ^240=15+26u, so exact multiplicative order 1680. Root α has α^(41²)=α+32u, giving 41 distinct F_(41²)-Frobenius conjugates, hence irreducibility degree41. Eliminating u gives minimal G(Z)=Z^82+2Z^42+4Z^41+Z²+4Z+15 over F41. Independently checked 83|41^82−1 and polynomial modular exponentiation Z^((41^82−1)/83) mod G = 1 in exact integer arithmetic (433-bit exponent). Thus roots are not primitive. The proof is finite algebraic, not statistical experimentation. Revision caveat: the later Oct18 v3 paper no longer displays the historical v2 universal Conjecture 4.2, so this refutes that historical assertion, not an existing v3 existential claim.

## originality

PASS

PASS best-of-knowledge for this explicit nonprimitive irreducible degree41 trinomial with primitive coefficient and index divisible by 83. Historical v2 2026 abstract expressly asserts universal primitivity for every primitive λ over F_{p²}; later v3 changes its conjectural scope to an existential form. A counterexample to the former does not disprove the latter. No previously tabulated p=41, λ=2+16u, factor83 witness identified in genuine Resultary/literature searches; unlocated earlier witnesses remain possible.

## value

PASS

PASS: A concrete counterexample to a published historical universal finite-field conjecture separates irreducibility, primitive constant term and root primitivity via an exact cyclotomic divisor. Its independent reproducible 433-bit certificate at the first prime beyond the older tabulation is a motivated obstruction, not a random polynomial statistic. Do not infer the revised existential conjecture fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
