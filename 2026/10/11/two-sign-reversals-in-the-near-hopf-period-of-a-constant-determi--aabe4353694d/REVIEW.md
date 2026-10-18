# Independent mathematical audit

## correctness

PASS

Starting from frozen exact Selkov polynomial vector field, independently verify equilibrium (b,b/K), det K and trace mu; coordinate transformation q=x+y-b-b/K, v=b-x gives exact scalar q''+Kq=mu q'+2bq q'+b(2K-1)/K*(q')²-q(q')²-(q')³. Fourier Poincaré--Lindstedt order-two Q2=d/2+d cos(2theta)/6+b sin(2theta)/(3sqrt K) and order-three resonant coefficients yield mu2=(1+2K-2K²)/4>0 and nu2=-(2K-1)(4K²+3K-2)/(24sqrt K). Independent SymPy recomputed exactly resonant cosine coefficient (2K-1)(4K²+3K-2)/12, mu2, nu2 and c(K), rather than trusting checker exit. Positive cubic radial stability with transverse eigenvalue crossing gives locally unique stable periodic branch for small mu>0. Denominator of c>0 on (0,1); factors yield roots K*=(sqrt41-3)/8≈0.42539 and 1/2 and three sign regions. Fixed K only, no uniform endpoint or exact isochrony claims.

## originality

PASS

Strogatz 1994 uses the same polynomial vector field and qualitative cycle arguments; the materially inspected 2018 Artés--Llibre--Valls phase-portrait paper establishes qualitative Hopf but not this exact determinant-constrained period coefficient or two neutral points. Al Noufaey 2021 uses a related reaction-diffusion Galerkin oscillator rather than the same time-normalized curve. Selkov 1968 uses a distinct printed rate law. Llibre--Nabavi 2022 is a plausible same-model period source, but its complete article was inaccessible (official abstract/figures read; institutional VPN disconnected), so its potential coverage is a named residual risk. Best-of-knowledge O pass is qualified, not a definitive whole-document exclusion.

## value

PASS

Keeping the linearized determinant/frequency K fixed while varying distance through Hopf isolates a genuinely nonlinear period-sensitivity effect: two exact sign reversals distinguish accelerating from slowing cycles. This natural local bifurcation invariant supplies useful parameter boundaries rather than an arbitrary polynomial computation or a generic statement that a Hopf cycle exists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
