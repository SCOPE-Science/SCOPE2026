# Scientific review

## Correctness

**PASS.** The exact nonnegative localization spectrum follows from the cited Fourier–Wigner Laguerre identity, checked independently against the Charlier formula. The fixed-order Charlier generating function and Stirling formula yield the compact-uniform local eigenvalue limit; polynomial recurrences and Poisson tail estimates prevent maximizing indices escaping this central scale. The resulting finite maxima of Hermite–Gaussian densities give the asymptotic norm and full maximizing-set characterization. For the first excited Hermite window, the first Stirling correction has opposite signs at the two peaks, and local curvature places every maximizing integer at a bounded distance from the lower peak. The extracted checker passed 160 assertions. No finite test is taken as a proof of the unrestricted limit.

## Originality

**PASS with residual risk.** Abreu and Gröchenig (arXiv:1012.4283) provide the Hermite-window STFT framework; Agorram et al. (arXiv:1506.07084) give the overlap formulas; Abreu–Gröchenig–Romero (arXiv:1404.7713) treat expanding localization domains; and Maximenko–Tellería-Romero (arXiv:1905.00978) give a general radial multiplier formula, so the underlying diagonalization and integral representation are not new. What is additionally determined is the *global maximal eigenvalue and its maximizing degrees* for a fixed-area annulus receding to infinity, together with a first-order bias selecting the lower of two leading-order bands at window order one. The inspected portions do not state this combination or a directly dominating asymptotic theorem. Residual priority risk includes earlier radial Toeplitz and Charlier local-limit treatments, and Daubechies' foundational 1988 localization article was not inspected in full.

## Mathematical value

**PASS.** Fixing phase-space area while moving the annulus to arbitrarily large radii differs from the common expanding-domain regime: many Hermite modes compete on the square-root radius scale. The theorem identifies the universal sharp norm constant and the entire finite argmax set for any fixed Hermite order. The order-one theorem resolves a nontrivial degeneracy via asymmetric lower-order statistics and predicts the optimal frequency band quantitatively. This informs exact localization design beyond routine computation of the already known radial spectrum.

## Limits

The order and area are fixed, no all-radius exact mode staircase is claimed, and independent assessment of publication priority remains outstanding.

Self-review: passed. Independent audit: not yet performed.
