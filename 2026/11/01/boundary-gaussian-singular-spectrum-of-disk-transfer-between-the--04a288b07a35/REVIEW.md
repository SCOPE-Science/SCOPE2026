# Independent mathematical audit

## correctness

PASS

Gaussian orthonormal bases are u_n=z^n/sqrt(n!) in L0 and v_n=z^n(n+1-|z|²)/sqrt((n+1)!) in L1, plus v_-1=conj(z). Angular orthogonality diagonalizes the interlevel disk operator. The coefficient equals the radial integral int_0^x t^n(n+1-t)e^(-t)dt/sqrt(n!(n+1)!) = e^(-x)x^(n+1)/sqrt(n!(n+1)!) by differentiation of t^(n+1)e^(-t). It is strictly positive, decays factorially, so gives the complete singular sequence and all S_p. Ratio a_(n+1)/a_n=x/sqrt((n+1)(n+2)) proves log-concavity and modal ties. Summing squares matches x e^(-2x) I1(2x). Maximizing each n at x=n+1 gives b_n increasing strictly to C=(2pi)^(-1/2), so for each finite x max_n a_n<C and limit norm is C. The Poisson representation a_n=sqrt(n+1)P(Pois(x)=n+1) with Stirling and entropy H(y)=y log y-y+1 gives Gaussian local profile and uniform tail control for every fixed p>0; Riemann sums establish the Schatten edge and level counting. Fixed-mode decay plus uniform norm proves strong limit zero despite norm nonconvergence. The verifier is finite corroboration, not the proof.

## originality

PASS

Best-of-knowledge comparison of exact statements and implications: Checked aliases interlevel Toeplitz, polyanalytic Fock, Hermite-window STFT, magnetic Landau disk and Poisson boundary mass. A known same-window localization diagonalization does not yield the cross-level singular laws as a theorem without extra boundary identification. General Toeplitz calculus or diagonal Landau level concentration does not, without further calculation, imply a sharp all-x cross-block norm and all-p edge law. The claim includes an identified cross-level block, a strict norm ceiling and fixed-p spectral-edge laws that are not proved by the inspected prior theorems. Caveat: an equivalent cross-level formula in physics could exist under another normalization.

## value

PASS

This gives exact singular values for a natural discontinuous spectral projection between two distinct Landau levels, unifying sharp finite-radius inequalities and a universal Gaussian edge. The all-p Schatten and counting laws and strong-but-not-norm convergence are useful independent operator facts, not a mere basis normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
