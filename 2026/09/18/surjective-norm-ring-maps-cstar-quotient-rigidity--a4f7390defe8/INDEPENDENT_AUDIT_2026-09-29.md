# Independent audit — 2026-09-29

Record: `2026/09/18/surjective-norm-ring-maps-cstar-quotient-rigidity--a4f7390defe8`  
Assigned and audited source tree: `eb149dc932ad28137d0c26bb7632a6a7e85e63ea`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The quotient-rigidity argument is sound. Surjectivity plus the Fischer–Muszely norm equation gives additivity. Writing u=T(1), the product-norm identity makes left multiplication by u isometric, and the cited bijective-paper functional-calculus step yields a self-adjoint symmetry. The centrality repair does not use injectivity: for x in pBq, surjectivity gives T(a)=x, x^2=0 gives T(a^2)=0, and the two factorizations of 1-a^2 imply ||1±2x||=1; summing the resulting positive inequalities forces xx*=0. After normalization Φ=uT, the positivity argument, C*-identity and product-norm identity give a global contraction. Its kernel is then a closed two-sided *-ideal, and the induced bijection A/ker Φ→B satisfies Matsuzaki's hypotheses; unitality forces the central symmetry in that quotient theorem to be 1. The converse and the exact quotient norm follow.

## Originality

**qualified_supported**. Matsuzaki's current September 16, 2026 theorem is explicitly for bijections, while Shibata–Matsuzaki–Miura likewise work in a bijective norm-ring setting. Targeted searches did not locate the same surjective C*-quotient classification. The contribution is therefore supported narrowly as the quotient extension of that very recent theorem, not as a new Fischer–Muszely additivity theorem or a new general result on C*-quotients. Broad nonlinear-preserver literature remains a residual prior-art risk.

## Scientific value

**meaningful_strict_extension**. The result identifies the exact and only noninjective behavior permitted by the three norm/involution identities: passage to a C*-ideal quotient. It also yields the simple-domain collapse and exact distance-to-kernel formula. The value is as a clean structural extension of a new bijective theorem, with no claim for nonsurjective or approximate maps.

## Evidence and literature checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/surjective-norm-ring-maps-cstar-quotient-rigidity--a4f7390defe8
- https://arxiv.org/abs/2609.18121
- https://arxiv.org/abs/2608.03426
- https://doi.org/10.5486/PMD.2003.2725

## Limitations

- The classification still assumes surjectivity.
- The proof deliberately imports Matsuzaki's bijective theorem after quotienting rather than replacing it.
- Originality is qualified because older nonlinear-preserver literature is broad and terminology varies.
