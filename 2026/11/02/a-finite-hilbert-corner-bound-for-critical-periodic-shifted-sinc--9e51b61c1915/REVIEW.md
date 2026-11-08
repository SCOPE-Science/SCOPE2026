# Independent mathematical audit

## correctness

PASS

For p>=4, in the balanced + then - sign sequence at frequency shifts ±1/4, same-sign columns are exactly orthonormal. The Gram spectrum gives A_blk=1-||C||. A reversed L-by-L cross corner (L=floor(p/2)) has frequencies j+k+1/2; its geometric-sum phases factor into row and column phases and its positive magnitude K_{jk}=1/[p sin(pi(j+k+1/2)/p)]>=H_L(j,k)/pi. Perron positive eigenvector bounds ||C||>=lambda_max(H_L)/pi. All sign Fourier frequencies are distinct mod p, so A_p>0. De Bruijn–Wilf asymptotic pi-lambda_max(H_L)~pi^5/(2 log(L)^2) yields the stated limsup <= pi^4/2. Independent direct numerical eigenspectra for periods 4,5,6,8,12,24,48 all obey finite bound; finite experiments do not prove asymptotic.

## originality

PASS

A finite Hankel-corner comparison plus known Hilbert largest-eigenvalue asymptotic yields a concrete one-sided rate for the same critical periodic shifted-sinc problem. The closest 2026 preprint abstract describes finite matrix formulation and step-pattern vanishing but does not explicitly give logarithmic rate. Full paper inaccessible here, hence priority risk stated rather than inferred negative coverage.

## value

PASS

One-sided quantitative resolution of the critical periodic shifted-sinc degeneration: explicit sharp-form finite comparison to a classical spectral model and O((log p)^-2) rate; a motivated mathematical boundary theorem rather than a trivial numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
