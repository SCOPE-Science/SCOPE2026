# Independent mathematical audit

## correctness

PASS

On unordered pair states the rotation and collision letter define a finite absorbing Markov chain with unique finite first and second hitting-time solutions. Starting from the specified pair, the first-step equations are (I-P)e=1 and (I-P)s=2e-1. The source splits ordinary self-loop stretches from four exceptional transitions, verifies Gusev’s first moment, and reduces second moments to 2X_l-X_(l-1)-X_(l+1)=D_l with X_0=0 and reflection boundary X_m-X_(m-1)=H_m. Summation yields X_m=mH_m+sum_{l=1}^{m-1}lD_l and subtraction of E² gives the claimed polynomial. Independent exact rational solves of the ORIGINAL unordered-pair system for n=3,5,7,9 agree with both formulas. An independent symbolic summation proves the terminal polynomial identity for arbitrary m (unlike merely checking sample cases). These checks substantiate computations; the global pair-state recurrence and absorbing-chain argument provide the all-odd-n proof.

## originality

PASS

Best-of-knowledge PASS for the second merger-time moment. The strongest primary antecedent is Gusev (2014), which analyzes the same random-input fixed Černý pair and derives the cubic expected time, but its read proof does not calculate the second moment. An expectation, deterministic reset threshold, and optimized synchronization probability do not imply the variance of a fair input hitting time. Searches for the exact polynomial, odd-pair variance and absorbing-chain second moment found no covering public record. Earlier equivalent Markov-chain variance calculation could exist under alternative notation, and search failure does not prove priority.

## value

PASS

Random-input synchronization is a canonical probabilistic probe of a slowly synchronizing automaton. The exact variance and nonvanishing limiting coefficient of variation determine the actual dispersion scale, which is not inferable from the previously known expectation or deterministic reset-word bounds. This is a mathematically motivated infinite-family exact invariant, rather than a routine tiny-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
