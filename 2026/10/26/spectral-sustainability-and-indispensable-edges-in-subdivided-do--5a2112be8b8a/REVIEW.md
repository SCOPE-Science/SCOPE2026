# Independent mathematical audit

## correctness

PASS

For each pendant-edge deletion the allowed changes are precisely reattachments of that leaf. The Schur complement gives the new spectral radius as the root t=R_w(t) above the core spectral radius, with R_w positive and decreasing. The path-continuant concatenation identity gives the stated spine difference. At the original spectral radius with a>=b+2 one has t>sqrt(a)>=2 by strict Perron monotonicity of the proper embedded K_(1,a); the bracket lower bound is strictly positive by t>2 and e-f>=1 even for f=1. The other center is also strictly worse by the endpoint difference. Every candidate pendant attachment is worse than attachment to its own center: for a core pendant w adjacent to c, R_w=1/t+R_c/t^2, and R_c>t/(t^2-1) by the walk expansion and the additional neighbors of c over the single edge cw. Every spine edge meets a degree-two vertex; reattaching the cut branch across that vertex's uncut incident edge does not lower the radius, by the degree-two shift lemma. The endpoint comparison works for sustainable smaller-side or equal-center leaf moves even if t<=2, since P_(ell-1)(t)>0 above the core radius. Unit imbalance gives an isomorphic restoration for a larger-center leaf, and degree-two centers give the remaining cases. For ell=1 and proper centers a,b>=3, the central-edge cut gives two stars. The joining-root condition is R_v R_w=1 above both component radii, and each star's center has strictly greater diagonal resolvent than any leaf there: with d>=2 leaves the center-to-leaf ratio is t^2/(t^2-d+1)>1. Thus any different cross-edge decreases the radius, as the thesis also shows. The all-parameter conclusions are analytic; the packaged 75-case floating-point script was inspected but not run and does not cover ell=1.

## originality

PASS

The supported distinct claim is the full ell>=2 center-degree balance criterion with exact localization and count of every failing leaf edge. The one-edge double-star obstruction is already proved in the publicly retrievable 2025 thesis and is not new. The degree-two edge lemma, a high-degree obstruction, and the subdivided balanced subfamily B(2,k,k-1) are also prior.

## value

PASS

The theorem gives an unbounded three-parameter classification for a motivated family and identifies precisely which edges force failure, even when the available high-maximum-degree test is silent. The sharp one-degree balance boundary is useful independently of the known proper double-star example and prior sustainable subfamily.

The dated certificate retains the supplied scientific assessment, sources and limitations.
