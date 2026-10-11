# Independent mathematical audit

## correctness

PASS

The weighted Gram matrix is exactly diagonalized by the gauge-shifted cyclic characters. Expanding \(\cos^k t=2^{-k}\sum_j\binom{k}{j}e^{i(k-2j)t}\) gives rank-one character terms; two terms are the same character exactly when their binomial indices agree modulo \(N\). Because each character has squared norm \(N\), the nonzero eigenvalue in residue class \(r\) is precisely the fair-binomial residue mass \(p_r\), including zero masses when the residue is absent. For an equiprobable pure geometrically-uniform orbit the pretty-good measurement is minimum-error optimal and the diagonal of \(\sqrt G\) is constant, so the success probability is \(N^{-1}(\sum_r\sqrt{p_r})^2\). The root-of-unity filter has a unique dominant conjugate nonconstant pair of modulus \(c_N=\cos(\pi/N)\); the next Fourier modulus is at most \(c_N^3\), and the first-order square-root term cancels on summation, yielding \(1-P_{N,k}=\tfrac12c_N^{2k}+O(c_N^{3k})\). Finally, the multiple quantum Chernoff theorem reduces the fixed-ensemble exponent to the smallest pairwise pure-state Chernoff distance. On the projective circle of length \(\pi\), some adjacent gap is at most \(\pi/N\), and equality in the resulting exponent bound forces every gap to equal \(\pi/N\). The inspected package verifier directly checks the character eigenvectors and residue weights on a grid; those finite checks corroborate rather than replace the analytic argument.

## originality

PASS

The closest current primary source, Achenbach--Leppäjärvi--Lee--Heinosaari, defines the same regular real-qubit cyclic ensemble and the same Gram matrix and proves PGM optimality, but its Proposition 5.5 explicitly assumes \(n>k\); its table and analytic scaling formula are likewise restricted to that non-aliasing regime. Kvashchuk et al. treat the broader multicopy optimization problem and real-state restrictions, while Krovi et al. provide general GU measurement machinery, but the inspected statements do not evaluate the symmetric-power cyclic spectrum after residue aliasing. A general GU formula still requires the object-specific decomposition that produces the fair-binomial residue law. Ke Li supplies the general multiple-Chernoff theorem; the projective-circle extremal specialization is elementary background to the main finite-copy result rather than the sole novelty. Current Resultary search did not return a stronger same-object arbitrary-\(N,k\) formula among its leading results.

## value

PASS

The recent primary literature explicitly isolates the regular rebit polygon as a central multicopy benchmark and leaves the aliased regime outside its closed formula. Resolving all \(N,k\), identifying the spectrum as a binomial law modulo \(N\), and extracting the sharp fixed-\(N\) error prefactor give a reusable exact benchmark for a current discrimination problem. The exponent consequence also clarifies why this same polygon is asymptotically extremal without claiming the still-open finite-copy global conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
