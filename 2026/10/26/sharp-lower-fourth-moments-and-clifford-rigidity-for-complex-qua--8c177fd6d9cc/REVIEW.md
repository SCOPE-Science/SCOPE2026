# Scientific review

## Correctness — PASS

Every complex degree-two spherical harmonic has a unique symmetric trace-free quadratic matrix. For normalized sphere measure, Gaussian radial decomposition gives the second moment \(2t/[n(n+2)]\). Extraction of the fourth-order Gaussian quadratic-form moment gives numerator \(4|\operatorname{tr}A^2|^2+8t^2+32\|A^2\|_F^2+16\operatorname{tr}[(AA^*)^2]\). The nonstandard identity \(\|A^2\|_F^2+\operatorname{tr}[(AA^*)^2]=2\operatorname{tr}(B^2+C^2)^2\) converts this expression into an exact three-term sum-of-squares deficit. The equality matrix conditions force anticommuting symmetric involutions and hence even dimension, and their orthogonal normal form gives every optimizer. The standalone polynomial-monomial checker evaluates 84 deterministic cases in exact arithmetic and explicitly attains equality in dimensions 2, 4, 6, and 8. The proof, rather than the finite checks, establishes all-dimensional validity.

## Originality — PASS, best knowledge

Relevant primary studies of spherical harmonic concentration, high-degree reverse Hölder upper bounds, and Fourier-extension extremizers were compared with the actual statement and quantifiers. The closest publicly available degree-two sharp fourth-moment result is an *upper* bound with real zonal maximizers (published-finding corpus record `d4106097159f`, full RESULT.md inspected). Its proof does not state the sharp lower bound, the nonnegative Clifford deficit, or the all-even-dimension equality orbit. Neither an upper norm bound nor an upper asymptotic concentration statement logically implies a sharp lower bound. Searches targeting complex quadratic lower fourth moments, anticommuting-matrix formulations, and the numerical coefficient did not surface a covering result. Risks: older matrix-moment/Clifford-system literature may contain an equivalent result; the entire 1981 Stanton–Weinstein paper was unavailable, and its abstract alone does not exclude such coverage. This is best-knowledge priority, not an independence or novelty certificate.

## Mathematical value — PASS

The question asks how flat a nonzero degree-two Laplace eigenfunction can be on the sphere under fixed \(L^2\) energy. The sharp ratio \(2(n+2)/(n+6)\), its exact tensor deficit, and the even-versus-odd equality obstruction together resolve a natural lower endpoint in every even ambient dimension. The extremizers form a single explicit orthogonal-and-scalar orbit of square-zero complex quadratic forms. This provides quantitative rigidity not supplied by generic Jensen, upper reverse-Hölder estimates, or high-degree asymptotics. The unknown odd-dimensional sharp coefficient is explicitly outside the finding.

## Closest literature and limits

Speckbacher–Hrycak (arXiv:1909.01670v1) concerns spatial concentration of bandlimited spherical harmonics. Flock–Stovall (arXiv:2204.10361v1) concerns extremizing sequences of the spherical Fourier extension operator. Dai–Feng–Tikhonov (arXiv:1408.1877v1) concerns degree-asymptotic upper reverse-Hölder norm ratios. Stanton–Weinstein (1981) treats local maximization. The public degree-two sharp upper theorem (`d4106097159f`) is the closest statement-level comparator and was inspected in full. These are different questions from the exact lower fourth moment for complex quadratic harmonics. An earlier equivalent matrix-invariant identity cannot be categorically excluded without wider expert bibliography review.

Self-review: passed. Independent audit: not yet performed.
