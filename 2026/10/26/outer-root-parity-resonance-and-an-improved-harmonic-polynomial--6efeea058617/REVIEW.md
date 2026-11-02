# Independent mathematical audit

## correctness

PASS

The imaginary equation Im H_epsilon=epsilon Im z^n=0 confines all zeros to n lines through the origin; at generic Gaussian coefficients the origin is not a zero, so line counts add without duplicates. Restriction and sign normalization give epsilon x^n+f_j(x), where f_j/sqrt2 is a real Kostlan polynomial. For fixed squarefree f_j with nonzero leading coefficient, simple finite roots persist under small epsilon; after x=epsilon^{-1/(n-m)}y the remaining n-m zeros approach nonzero roots of y^{n-m}=-a_m. Hence an odd degree difference contributes one real outer root per line, while an even difference contributes two precisely when the top real coefficient is negative. For even difference the signs depend on cos(phi+2*pi*((n+m)/2)*j/n), whose repeated cyclic grid has length L=n/g and multiplicity g, giving exactly n or the symmetric n±g law. Its expectation is always n. Kac–Rice gives E(number of finite real Kostlan roots)=sqrt(m) per line. Since each of n line polynomials has at most n real zeros, dominated convergence proves the exact expectation limit. Every regular degree-n real polynomial has real-root count congruent to n modulo two, so the n-line total has parity n; the expectation forces at least R(n,m), the parity-compatible ceiling, in some sample. The n=77,m=5 arithmetic inequality yields 251>249. Independent numerical cosine-grid tests covered all n<80 with multiple phases and strict nonboundary checks, plus arithmetic for 77,5; original verification.py was read and supplies six exact rational Sturm perturbations. These finite checks support but do not replace root-continuity and Kac–Rice proofs.

## originality

PASS

The exact Gaussian perturbation and one-dimensional line reductions were developed by Erik Lundberg in arxiv:2201.00788 (2022; published 2023), which obtains at least ceil(n sqrt m) distinct zeros from finite Kostlan roots. Full source text §§2–4 was read: its perturbation argument restricts roots to bounded real intervals and does not count the n-m roots escaping to infinity. The new calculation determines that outer contribution and arithmetic phase-grid law, yielding an additive n expected root improvement and a parity-adjusted all-degree existential theorem. Earlier Khavinson–Lee–Saez and Lee–Lerario–Lundberg construct other counterexamples and are not claimed as new; m=5 counterexamples might exist by other methods. Standard root escape, Kac–Rice and the Kostlan expectation are known ingredients; the joint arithmetic count and improved consequence are the assessed claims.

## value

PASS

The exact arithmetic classification of escaping real roots is a structural property of an already-motivated Gaussian Kostlan harmonic-polynomial model. Counting them sharpens an existing valence lower bound by an additive n, extends the fixed-coanalytic-degree counterexample range of that construction, and supplies concrete (77,5) numbers. This is mathematically meaningful even though it is existential and not globally optimal; it is neither a mere numerical rerun nor an unsupported claim of first counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
