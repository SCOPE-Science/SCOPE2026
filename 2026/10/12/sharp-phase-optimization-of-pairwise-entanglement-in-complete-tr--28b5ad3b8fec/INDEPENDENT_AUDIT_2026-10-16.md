# Independent mathematical audit

## correctness

PASS

For qubits A,B joined and connected to c further vertices with identical Ising e^(-i theta ZZ/2) interactions and |+> product input, tracing the c signs gives rho_AB matrix entries 1/4 e^(-i theta(st-s't')/2) cos^c(theta(s+t-s'-t')/2). Direct two-qubit partial transpose diagonalizes into eigenpairs lambda1±=(1-y±sqrt((1-y)^2+16x² sin²theta))/8 and lambda2±=(3+y±sqrt((1-y)^2+16x² cos²theta))/8 for x=cos^c theta,y=cos^c2theta. Second pair nonnegative; first gives exact negativity positive iff sin theta cos theta !=0. In p=sin²theta, q=1-p: 4N²+[1-(1-2p)^c]N=pq^c. Odd-binomial lower bound yields N<1/(2c). At theta=z c^(-2/3), global asymptotic is 1/(2c)-c^(-5/3)[z^4/12+1/(2z²)]+o(c^-5/3); its unique minimum coefficient is 3^(2/3)/4 at z=3^(1/6). Bounds on p_c above and below ensure all maximizers enter a compact positive z interval; hence global optimization, not just local. Independently constructed full state vectors and diagonalized partial transposes for c=1..5, three phases each, plus asymptotic trials at c=100,500,2000; finite checks not a general proof.

## originality

PASS

Hein et al. give general reduced-density machinery for weighted graph states, and Gnatenko covers tripartite correlators and single-vs-rest entanglement, but neither theorem explicitly optimizes traced two-terminal negativity, derives the closed four-eigenvalue spectrum in this specialization, or proves the fractional stage-size asymptotic.

## value

PASS

The natural quantum information task is to choose a uniform Ising interaction phase that maximizes detectable pair entanglement after environment tracing; exact finite-c law, universal upper bound, nontrivial c^(-5/3) correction and optimizer localization supply quantitative engineering and asymptotic content not merely a straightforward partial trace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
