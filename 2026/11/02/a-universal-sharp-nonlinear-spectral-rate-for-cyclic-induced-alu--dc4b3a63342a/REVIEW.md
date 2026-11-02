# Self-review

## Correctness (PASS)

The statement specifies a strictly positive fixed-period scalar bilateral shift, a normalized operator monotone representing function with derivative strictly in \( (0,1) \), and the exact induced polar mean. The polar factor is the unitary bilateral shift. Strict internality and positivity force convergence on each cyclic profile. The centered logarithmic Jacobian is the normal circulant \(B=\lambda I+(1-\lambda)S\). Its exact zero-mean spectral norm is \(\rho_m(\lambda)\). The nonlinear remainder is quadratic near consensus, and variation of constants, using \((\rho+\eta)^2<\rho\), upgrades the local envelope to \(O(\rho^k)\); the scalar-coordinate drift is smaller. Sharpness is certified analytically for each mean by an initial small Fourier-mode perturbation: its rotating leading coefficient differs from the initial amplitude by \(O(\varepsilon^2)\), thus cannot vanish. The unique zero-rate case has quadratic centered convergence. No finite tests are used in place of a limiting argument. The standalone exact checker ran 54,076 finite diagnostics covering multiple scalar means, both symmetric and nonsymmetric.

## Originality (PASS, residual uncertainty)

Yamazaki's arXiv:1912.08452 (submitted 2019-12-18) already establishes scalar perspective recurrences for generalized Aluthge maps and binomial weighted arithmetic/harmonic iterations; these are not claimed new. The September 5, 2024 preprint by Osaka and Yamazaki proves **qualitative** induced-Aluthge convergence for invertible centered operators and develops the cyclic mean construction, but neither its Theorems 2.3/4.4 nor the inspected supporting sections yield the sharp worst-case nonlinear spectral rate and mean-derivative universality. Yamazaki's 2021 paper and Rion's 2011 thesis give earlier explicit arithmetic/geometric ordinary Aluthge specializations; these are excluded from the claim of novelty. Pálfia and Petz (2014) consider a different multivariable mean iteration. Searches of related published summaries, publicly archived research claims, and prior recorded claims found no statement implying the universal quantitative theorem. The residual risk of an equivalent theorem under nonlinear cyclic consensus or matrix-mean contraction terminology remains; absence from search results is not independent certification.

## Mathematical value (PASS)

A qualitative operator-theoretic convergence theorem is sharpened to a sharp, optimal quantitative theorem valid for the entire scalar Kubo–Ando class. The rate is unexpectedly controlled only by the derivative of the representing function, despite nonlinear full dependence of the limit; the proof provides near-equilibrium sharp witnesses, handles the supergeometric degeneracy, and identifies the optimally balanced means. The restriction to fixed periodic positive scalar symbols is natural for the underlying induced Aluthge operator framework, rather than an arbitrary finite example. It supplies a concrete structural bridge between operator means and cyclic Fourier consensus.

## Material consulted and limitations

- Osaka–Yamazaki, arXiv:2409.03338v1: public manuscript with statements and proof of qualitative convergence, particularly Theorems 2.3 and 4.4; first public 2024-09-05.
- Yamazaki, *A generalization of the Aluthge transformation in the viewpoint of operator means*, arXiv:1912.08452 (first public 2019-12-18), §5: original full HTML including the scalar recurrence and special weighted iteration formulae.
- Yamazaki, *The induced Aluthge transformations*, Linear Algebra Appl. 628 (2021), §5: author-uploaded complete text with special-case formulae.
- Rion, *Dense orbits of the Aluthge transform* (2011), pp. 51–52: binomial exact iterates, viewed as full manuscript pages.
- Pálfia–Petz, *Weighted multivariable operator means of positive definite operators* (2014): bibliographic materials and accessible excerpts only, not an entire source inspection.
- Antezana–Pujals–Stojanoff, *The iterated Aluthge transforms of a matrix converge*, Advances in Mathematics 226 (2011), §6.1–6.2: the full available manuscript text discusses spectrum-dependent exponential convergence for certain finite matrices but no universally sharp derivative-rate theorem across all Kubo–Ando scalar means.

Analytical correctness is within the stated scalar hypotheses. Broader nonperiodic/noncommuting models, exact limiting constants for general means, and an external independent review are not established.

Self-review: passed. Independent audit: not yet performed.
