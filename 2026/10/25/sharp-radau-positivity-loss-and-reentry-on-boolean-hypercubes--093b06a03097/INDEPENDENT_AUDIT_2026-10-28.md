# Independent mathematical audit

## correctness

PASS

Walsh characters diagonalize L_d with eigenvalues 2j, giving stability factors rho_j=(6-4jh)/(6+8jh+4j²h²) and Hamming-distance Krawtchouk kernels. Reconstructed all 14 rational kernels at d=1..4 exactly from the character sum. At d=3 the only numerator negative coefficient is absorbed by strictly positive 12h²-14h+22; d<=2 follow by coordinate marginalization. At h=3/2 rho_1=0 and rho_j<0 for j>=2, and the d4 diagonal is exactly -3/1804; termwise binomial monotonicity extends negativity to all d>=4. At d4 all four offdiagonal numerators have positive coefficients, while diagonal is octic P(h) divided by positive quadratics. Descartes two sign changes and signs at h=0,3/2,infty imply exactly two positive roots alpha 1.46546725520286 and beta 5.52994947048244, yielding [0,alpha] union [beta,infty). The linear mass eigenvector is preserved, giving row and column sums one. Independent exact SymPy recalculation verifies rational identities and root location; infinite frontier uses the analytic argument.

## originality

PASS

Numipedia supplies the Radau IIA2 third-order rational stability function and zero absolute-monotonicity radius; this general method datum does not fix graph-specific positivity in any hypercube dimension. Zappavigna et al. examine Padé transformations of positive systems and conditions for general positive system preservation; their 2010 full PDF is specifically diagonal [p/p] Padé rather than this Radau [1/2] graph family, and 2012 examples concern general matrices/second-order Padé. Related published SCOPE positivity examples concern other integrators or graphs. The sharp d=4 loss/reentry polynomial and all-dimension bad step remain distinct best-of-knowledge findings.

## value

PASS

Positivity is essential for diffusion on product graphs; exact dimension frontier and disconnected Q4 admissible timestep set exhibit a concrete nonmonotone structural phenomenon invisible to scalar absolute-monotonicity radii. A natural infinite graph family and sharp finite-dimension boundary are classified without claiming the unresolved full time-set for d>=5.

The dated certificate retains the supplied scientific assessment, sources and limitations.
