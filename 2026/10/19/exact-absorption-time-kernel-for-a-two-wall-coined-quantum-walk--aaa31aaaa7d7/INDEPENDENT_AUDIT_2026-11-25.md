# Independent mathematical audit

## correctness

PASS

The interior compression K is a contraction. For a unit-modulus eigenvector the left lost channel is zero by norm equality, and the leftmost surviving R channel has no predecessor. The nonzero cos(theta) then forces the leftmost L amplitude to vanish. Propagating the same eigenvector equations through successive sites forces all components to vanish, proving rho(K)<1. This makes the integrated survival sum convergent and the equation Q-K†QK=I uniquely solvable. An independent SymPy block check gave zero residual in all 12 component cases (onsite, separation 2, generic larger even separation) and checked the zero extension at both missing directional channels, including both shifted indices at the same sink. Opposite parity vanishes by parity preservation and swapped positions follow by transpose. The tail-sum identity counts the detecting step and gives the stated localized quadratic form, with real cross term 4ux Re(conj(alpha) beta) and scalar midpoint block. Q gives the integrated survival operator, not a list of per-step survival kernels.

## originality

PASS

Earlier work gives the same discrete monitored model and methods for obtaining exit probabilities or first-hit distributions; no inspected result evaluates the finite two-wall integrated survival operator or gives the same all-site mean. Continuous-time kernels indexed nearby use different generators and detection.

## value

PASS

The finite-line lifetime is a standard observable, and the evaluated operator removes recurrence solving for every choice of initial state, including coherent superpositions across sites. Its explicit parity, phase and coin dependence and the exactly coin-independent midpoint mean give quantitative information not supplied by eventual detection probabilities or a generic Lyapunov representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
