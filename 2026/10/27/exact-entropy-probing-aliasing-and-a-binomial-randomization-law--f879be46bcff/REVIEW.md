# Scientific review: exact cycle graph-entropy probing law

## Correctness — PASS

The domain is all integers \(m\geq3\), \(L\geq2\) with the normalized Laplacian of the unweighted cycle of length \(mL\). The proof directly computes the discrete Fourier support of every periodic color indicator. This reduces the probing error to a difference of two equally spaced quadratures of the continuous periodic function \((1-\cos\theta)\log(1-\cos\theta)\). Exact Fourier coefficients \(1/[k(k^2-1)]\), valid for \(k\geq2\), give the convergent positive series, strict size ordering, and sharp \(\zeta(3)\) coefficient. The signed-pair law is derived from an exact circulant antipodal entry, giving independent fair signs, exact binomial masses, moments, and a central limit theorem. The saved standalone verifier passed 1175 finite checks. Neither the infinite Fourier result nor the limit is inferred from the finite tests.

## Originality — PASS, with publication-priority risk

The closest direct published source is Benzi, Rinelli, and Simunec, arXiv:2212.09642, Section 3.1, which establishes graph-entropy probing as a lower bound and derives a generic polynomial error bound; its Lemma 3.5 also includes an exact matrix power series. The latter is an important ingredient, but does not directly give a finite-cycle Fourier alias, sharp \(m^{-3}\) coefficient, sharp envelope across cycle lengths, or the finite stochastic law.

Frommer, Rinelli, and Schweitzer, arXiv:2308.07722, Sections 2--3, analyze Rademacher probing and general variance and sign-based pathwise comparisons. Those general facts are acknowledged as prior results. The asserted additional step is the exact entropy-dependent aliasing coefficient, which makes the antipodal finite distribution and risk fully explicit. Frommer, Schimmel, and Schweitzer, arXiv:2009.01589, give general probing analysis; relevant material contains no covering cycle-specific entropy formula. Classical Fourier coefficients, graph-cycle eigenvalues, and Rademacher sums are not separately claimed as new. Exact wording and implication checks found no inspected theorem encompassing the combined exact law. Publication priority remains uncertain beyond the accessed sources, and generic identities could make the result accessible by further specialization.

## Mathematical value — PASS

The 2022 graph-entropy study states that its uniform polynomial bound can be pessimistic. This result supplies a natural, connected, regular, exactly solvable benchmark where the leading error constant is sharp, the decay improves from the general quadratic upper-bound scale to cubic, and the largest possible error over multiples of the coloring period is determined exactly. With precisely the same number of matrix-function quadratic forms, its paired-color randomized estimator has a complete finite binomial distribution and an exact root-mean-square improvement factor \(\sqrt m\) over deterministic bias. These quantities allow checking trace-probing implementations and variance estimates on a canonical family rather than only observing qualitative convergence.

## Closest literature and limitations

- M. Benzi, M. Rinelli, I. Simunec, *Computation of the von Neumann entropy of large matrices via trace estimators and rational Krylov methods*, arXiv:2212.09642, https://arxiv.org/abs/2212.09642.
- A. Frommer, M. Rinelli, M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722, https://arxiv.org/abs/2308.07722.
- A. Frommer, C. Schimmel, M. Schweitzer, *Analysis of probing techniques for sparse approximation and trace estimation of decaying matrix functions*, arXiv:2009.01589, https://arxiv.org/abs/2009.01589.

The identities require unweighted cycles and a specified coloring. The binomial law requires antipodal classes of exactly two vertices and independent vertex signs. No claim is made for arbitrary sparse matrices, finite-precision quadratic forms, or a general fixed-matrix query-complexity exponent. The remaining originality risk is an unlocated equivalent cycle specialization or an independently known exact error constant.

Self-review: passed. Independent audit: not yet performed.
