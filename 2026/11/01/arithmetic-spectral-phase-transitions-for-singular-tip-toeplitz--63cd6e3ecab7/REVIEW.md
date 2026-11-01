# Scientific review: arithmetic spectra of singular-tip Toeplitz compressions

## Correctness — PASS

The full claim is proved using an explicitly normalized Bergman monomial basis, and every statement is reduced to either a one-variable moment identity or the exact arithmetic distribution of \(n+1+(m+1)/\gamma\). For \(\gamma=P/Q\), a modular-congruence argument shows that all positive values \(k/P\) occur with infinite multiplicity; for irrational \(\gamma\), irrational rotations yield a dense, nonrepeating parameter set. The spectral and Fredholm-essential-spectral descriptions then follow directly from the diagonal spectral theorem. The Hausdorff gap constants follow from exact elementary inequalities; rational-to-irrational continuity uses the diverging reduced numerator of any rational approximating sequence. A standalone checker passed 1334 finite diagnostics after the final mathematical definitions were fixed. No infinite claim depends on a numerical test.

## Originality — PASS (historical priority provisional)

The closest prior works provide important **ingredients**, not the stated spectral conclusion. Edholm and McNeal (arXiv:1605.06223, particularly the monomial lattice and projection regularity results) already identify generalized Hartogs domains, their admissible monomials, and the rational/irrational \(L^p\) dichotomy. Balay and collaborators (arXiv:2009.07260, Theorem 1.1 and Corollary 2.7) use exactly the power symbol \(|w|^\beta\), but prove \(L^p\)-regularity statements, not Hilbert-space spectra, infinite versus simple eigenvalue multiplicities, invertibility, or the two Hausdorff discontinuity formulas. Liu, Tang, Tu and Zhang (DOI:10.1007/s11785-023-01331-1; author-posted full text) extend \(L^p\)-to-\(L^q\) mapping estimates in integral-exponent, higher-dimensional domains, not spectral classification in irrational exponents. Lusky (DOI:10.7146/math.scand.a-14316) treats generalized one-variable Bergman–Hardy spaces and thus supplies background, rather than this two-dimensional arithmetic result. The primary remaining risk is a general moment-diagonalization or Reinhardt-Toeplitz theorem that would make some or all of the spectrum classification an implicit corollary without using the same language.

## Mathematical value — PASS

The invariant is not an arbitrary small numerical value: these two positive radial symbols encode vanishing toward a singular tip and observation of that tip. Their spectra simultaneously decide bounded invertibility, sharp stable reconstruction, and the optimal inner-region concentration fraction. Rational exponents have a genuine observation barrier \(R^{2/P}<1\) and a bounded inverse for the vanishing power symbol, while irrational exponents admit arbitrarily concentrated eigenmodes and lose bounded invertibility. The exact Hausdorff gaps provide a quantitative topological counterpart, classifying continuity at every parameter. The contrast adds a Hilbert-space spectral version to the known \(L^p\) geometric arithmetic phenomenon. It does not claim broad downstream applications or a new general theorem for all radial symbols.

## Scientific limits and priority risks

The claim concerns only the unweighted analytic Hilbert Bergman space and the indicated two positive radial symbols. It does not yield a general \(L^p\) regularity classification for \(p\ne2\). In the irrational case the operator has a complete orthonormal eigenbasis, although its spectrum is an interval; hence the result is not an absolutely continuous spectral-measure statement. A general published diagonal spectral formula could imply parts of the conclusions. No independent validation is represented.

Self-review: passed. Independent audit: not yet performed.
