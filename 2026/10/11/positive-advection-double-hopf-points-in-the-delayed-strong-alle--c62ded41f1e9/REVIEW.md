# Independent mathematical audit

## correctness

PASS

At α=0 the Neumann/Dirichlet spatial spectrum gives μ_n=d((2n−1)π/(2L))²; normalizing x=μ1/3 yields μ2/3=9x and μ3/3=25x. The source modal characteristic equation λ+μ+3exp(−λτ)=0 yields Hopf functions H_j(y)=(acos(−y)+2πj)/sqrt(1−y²) and G(x)=H1(x)−H0(9x). G(1/25)>0 and G→−∞ at 1/9; differentiating gives H1′(x)<2.1 and 9H0′(9x)>10 on (1/25,1/9), hence one simple zero. At that zero 9x<1<25x, two simple imaginary pairs and no higher-mode pair; scalar characteristic derivative cannot vanish since that would force sin(ωτ)=0, contradicting sin(ωτ)=ω/3>0. Spatial gauge φ=e^(αx/(2d))y leads to y′(0)=α y(0)/(2d), y(L)=0 with simple spatial roots; implicit function theorem and nonzero G′ carry the point to all sufficiently small α>0. Independent high precision root/characteristic substitution checked displayed numerical values but is not the existence proof.

## originality

PASS

The primary source asserts absence of simultaneous d/τ Hopf–Hopf after only comparing the earliest stability boundary. Its own entire modal Hopf ladder admits a higher-first-mode/first-second-mode transverse intersection; this is logically different from and contradicts the source’s blanket exclusion.

## value

PASS

An explicit transverse two-frequency point contradicts a strong published spectral exclusion for the identical PDE and changes its codimension-two bifurcation landscape. Modes, branch indices, and advection persistence are structural rather than arbitrary numerics; no nonlinear normal-form results are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
