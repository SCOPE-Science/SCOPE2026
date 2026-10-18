# Independent mathematical audit

## correctness

PASS

Averaging independently priced edge conductances over cyclic rotations preserves the price budget and cannot decrease λ2 because λ2 is the minimum of linear Rayleigh quotients over 1⊥, hence concave. For uniform nearest conductance a and next-nearest b, the Fourier eigenvalue at cycle parameter x=4sin²(pi k/n) is a x+b x(4-x), concave as a function of x for b>=0. All nonzero x lie between attained endpoints μ=4sin²(pi/n) and ν=4sin²(pi floor(n/2)/n); therefore the gap is exactly min{μ(a+(4-μ)b),ν(a+(4-ν)b)}. Under n(a+t b)=1 this becomes the minimum of two affine functions; intersecting at a=ηb yields the exact three price phases νr/(nt), μν/[n(t+η)], μ/n, with η=μ+ν-4>0, r=4-ν≥0 and q=4-μ. Equality plateau conditions follow from slope-zero boundary cases t=r or t=q; odd/even behavior from graph connectivity; large-n μ~4π²/n², ν→4 establishes 16π²/(tn³) for fixed 0<t<4. All results n>=5, t>0 are proved analytically rather than by finite numerical searches.

## originality

PASS

Saha and Das (2025) Theorem 3.4 gives the UNWEIGHTED Laplacian spectrum of exactly C_n^2: λ_k=4-2cos(2πk/n)-2cos(4πk/n). Thus Fourier technique and unweighted eigenvalues are prior. Boyd–Diaconis–Parrilo–Xiao (2007) handle SLEM and symmetry reduction in discrete-time fastest mixing; Shakeri et al. (2015) optimize a different fixed-layer interconnection budget; Gerencsér studies random sparse cycle shortcuts. These may suggest the method but neither the particular priced 2-orbit continuous-time feasible set nor the explicit r/q price transition and parity-specific boundary plateaux appear in their inspected statements. Originality is qualified by possible broader circulant SDP cases.

## value

PASS

For a natural network C_n^2 with independently selectable conductances, the answer is a complete all-n price-to-rate function with exact optimal allocations and sharp boundary families. It distinguishes odd cycles (cheap two-hop edges alone retain connectivity) from even cycles (two-hop alone disconnects) and provides the precise factor 4/t in long-network performance. The two-mode reduction turns a global semidefinite optimization into an explicit law, useful for diffusion and consensus design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
