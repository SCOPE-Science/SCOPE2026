# Independent mathematical audit

## correctness

PASS

PASS: Rebuilt R_s=(I-sQ)^(-1) as the cyclic geometric resolvent with r=s/(1+s), C=2R_s-I. Differentiating R_s gives C^2=I+4sR_s prime and every off-diagonal coefficient has sign of jS_n-rS_n prime; j=1 is the sharp one, F_n. The diagonal of C^2 is strictly positive from the circulant product. F_n decreases with the unique n>=4 root and limiting r=1/2. For fixed odd k, s->infinity gives C^k->2J/n-I, with negative diagonal for n>=3. For even k=2m>=2 and n>=4, its adjacent coefficient is -2m(n-3)/(ns)+O(s^(-2)), hence negative for large s. Direct independent sympy inversions/matrix powers tested 84 small n/r and high-s k cases; exact h=4 n=3 and n=4 witnesses reproduced. The analytical asymptotic, not finite experiments, handles unbounded h and all k.

## originality

PASS

Best-of-knowledge original classification of entrywise nonnegative fixed powers of the unfiltered Crank–Nicolson Cayley map on a unit-rate directed finite cycle. The generic M-matrix/Cayley identity and the one-step resolvent return test are prior work. The new point is that the *square* is positive at every step on the oriented three-cycle, every even power shares that exception, and for n>=4 the exact two-step boundary is a unique cyclic polynomial zero while every fixed power fails at sufficiently large step. No broader result inspected implies this parity classification.

## value

PASS

PASS: Entrywise positivity is mandatory for a Markov transition approximation to avoid negative probabilities. A negative Crank–Nicolson single step followed by a second equal step is genuinely recoverable for the directed three-cycle at every step size, while the exact dimension-four and higher cutoff proves the boundary of this mechanism. This gives a motivated parity/dimension classification and sharp step-size frontier rather than routine verification of a named small matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
