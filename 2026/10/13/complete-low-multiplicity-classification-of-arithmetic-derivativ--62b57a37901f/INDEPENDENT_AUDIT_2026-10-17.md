# Independent mathematical audit

## correctness

PASS

With E(n)=sigma(n)-n-D(n) and D(n)=n sum e_p/p, prime inputs give E=0. For squarefree composites E is the sum of divisor-expansion terms of at least two missing primes and is positive; for p^a (a>=2) it is sum_{j=0}^{a-1}p^j-a p^{a-1}<0. The remaining exponent partitions at Omega<=4 are p^2 q (E=(p+1)-(p-1)q, yielding 12 and 18), p^3 q (forcing q<2), p^2 q^2 (strictly negative for p<q), and p^2qr (odd p parity obstruction, p=2 gives (q-3)(r-3)=16 with distinct odd primes q=5,r=11, hence 220). Every partition exhausted, n=1 explicitly outside scope. Independently verified all symbolic E formulas via SymPy and enumerated admissible 2<=n<=60000: composite solutions 12,18,220. Checked Omega(396)=5 and D(396)=s(396)=696, showing boundary.

## originality

PASS

The equation and all displayed small composite witnesses 12,18,220 are already explicitly in OEIS A212127; discovery of those numbers is not novel. Ufnarovski–Ahlander 2003 gives foundational arithmetic-derivative formulas and differential equations D(n)=a, but its full text does not establish the all-integers classification conditional on Omega(n)<=4 for D(n)=sigma(n)-n. A distinct published SCOPE result studies D(n)-(n-phi(n)), not this aliquot difference. The universal four-factor support theorem is not entailed by a finite OEIS list or generic derivative definition. Residual risk is an obscure earlier minimal-support classification or a trivial reformulation in OEIS comments.

## value

PASS

Arithmetic derivative versus aliquot sum is a naturally recorded number-theoretic coincidence equation. Classifying the entire first four prime-factor multiplicities requires treating all exponent partitions and identifies the first mixed-support composite zeros; Omega=5 admits new witness 396, making the cutoff a natural sharp boundary rather than a random interval of integers. The elementary proof does not turn a known numerical table into new examples; it establishes unbounded exclusion under a structural invariant. Modest standalone value, not a claim to solve the full equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
