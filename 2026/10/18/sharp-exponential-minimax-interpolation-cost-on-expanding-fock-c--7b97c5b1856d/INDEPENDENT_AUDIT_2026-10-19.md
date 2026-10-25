# Independent mathematical audit

## correctness

PASS

For the normalized kernel Gram matrix with data inner product N^-1 sum, the Fourier eigenvalues are precisely the N Poisson-congruence masses. This gives Q=1/min p. A finite alias cutoff plus Stirling two-sided mass bounds yields p_min~N^-1/2 exp(-N max_t min_l J_rho(t+l)) up to constant factors for fixed rho. J(x+1)-J(x)=log(B(x)/rho), B strictly increasing, forces one transition at rho=e^-1 and the identric tie for rho>e^-1. The boundary alias k=0 is handled separately and the selected minimizer has strictly positive asymptotic arguments, sustaining the sqrt(N) prefactor. Independent Python log-sum-exp checks at N=400 and rho=.1,e^-1,.5,1,2,3 produced rates and residues consistent with the claimed branches, not a proof of all N.

## originality

PASS

The precise Poisson-congruence eigenvalues and circulant Gram diagonalization are preexisting, credited to Horoshko et al. (2016), Eq. (9). The final claim instead uniformly minimizes over growing Fourier residue classes as radius^2=rho N and identifies the sharp exponent, polynomial prefactor, identric phase boundary and worst-mode localization. The inspected full original gives the same spectral input but its main analysis is circular-state entanglement, not the stated asymptotic minimax optimization. Resultary search found related Gabor/Slepian/Fock spectral topics, no statement proved to dominate this claim. The 2024 Optimal circular states full text was inaccessible; priority risk remains.

## value

PASS

Quantifies the worst-case norm-amplification cost of exact interpolation at a natural regular-polygon family in a classical RKHS and identifies a nontrivial universal sharp transition and extremizing harmonic. An exact exponential rate and sqrt(N) prefactor, rather than only reusing the known Fourier eigenvalue identity, are mathematically useful for finite sampling stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
