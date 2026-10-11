# Independent mathematical audit

## correctness

PASS

Affine normalization reduces the support to four coefficients of \(P(X,Y)=a+bX+cX^2+eY\) on the nine pairs \((X,Y)\in\mu_3^2\), with all four coefficients nonzero. For each fixed \(X\), the polynomial is affine with nonzero coefficient in \(Y\), hence has at most one zero in that row and at most three zeros total; therefore local Fourier support is at least six. The four supplied coefficient choices have exactly 0, 1, 2 and 3 zeros, respectively, and fresh exact arithmetic in \(\mathbb Q(\omega)\) independently reproduced those zero counts. Frequencies restrict to the two-dimensional span in equal fibers of size \(3^{d-2}\), proving the scaling and exhaustiveness.

## originality

PASS

Bonami-Ghobber and Delvaux-Van Barel determine or study global uncertainty minima and equality/rank-deficiency phenomena on product Fourier matrices. They do not give the full attainable Fourier-support spectrum for this fixed four-point geometry. Bonami-Ghobber's Section 4 shows that for \(\mathbb F_3^2\), the global function \(\theta(k,G)\) concerns support of size at most \(k\), and its equality classification is a minimum problem; that does not determine exact-support size four on a prescribed line-plus-point set. The closest published SCOPE five-point result concerns a different exact support cardinality and geometry.

## value

PASS

The line-plus-one set is the basic non-collinear four-point geometry in \(\mathbb F_3^d\). Determining every attainable Fourier-support size on that fixed support gives a complete exact-support uncertainty slice and complements the existing global-minimum and neighboring-support-size classifications. The proof is short but structural, not a mere table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
