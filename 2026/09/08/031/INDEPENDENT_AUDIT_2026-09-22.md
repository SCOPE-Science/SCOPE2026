# Independent three-axis audit — 2026-09-23

Source: `2026/09/08/031`; audited source-tree SHA `865bfda598c1e691413c66cfc33bfed2bfe85657`; `RESULT.md` blob `f42436305d3c63197fe44e9f0f931438fdcb59ba`.

## Claim checked
The record classifies the 6-regular undirected circulants on 29 vertices up to multiplier/isomorphism, gives the two-sided and one-sided Ramanujan census, identifies the unique minimizer of the nontrivial spectral radius, and tabulates spectral/energy/characteristic-polynomial separation.

## Correctness — passed
I independently enumerated all `C(14,3)=364` connection triples and quotienting by multiplication in `Z_29^*` produced exactly 26 classes, each orbit size 14. Fresh Fourier evaluation of all 29 adjacency eigenvalues for every class reproduced exactly 12 two-sided Ramanujan types and 20 one-sided types, the unique `lambda*` minimizer `(1,2,7)` at about 3.8766697679, runner-up `(1,2,11)` at about 3.9059816469, and the distinct `lambda_2` minimizer `(1,5,13)`. Independent exact SymPy characteristic polynomials for all 26 integer adjacency matrices were all distinct and all had the `x^27` coefficient `-87`. Energy range, the minimum energy gap pair `(1,2,4)/(1,8,12)`, and the minimum sorted-spectrum L-infinity pair `(1,3,9)/(1,3,11)` also reproduce.

## Originality — passed relative to checked literature
Searches targeted `(29,6)` circulants, 6-regular Ramanujan circulants, prime-order spectral classifications, cospectrality and energy. Hirano–Katata–Yamasaki, arXiv:1310.2130, was inspected in full: it studies valency thresholds that guarantee Ramanujan behavior for odd circulants, not the per-isomorphism-type `(29,6)` census or best-expander/energy table. Conde et al., arXiv:2408.07200, proves the general odd-prime fact that singularly cospectral circulants are isomorphic; this explains the cospectral-singleton shape but does not provide the 26 characteristic polynomials, energies, or spectral ranking. No prior source giving the fixed-stratum table was found.

## Scientific value — passed
The complete small fixed-stratum census is a compact reference dataset at the Ramanujan boundary: it distinguishes one- and two-sided conventions, gives an exact quotient by isomorphism, identifies the extremal spectral witness and quantitative runner-up margin, and supplies independently reproducible characteristic-polynomial/energy fingerprints. These data are useful for benchmarking circulant-search, expander, and spectral-isomorphism computations.

No repair was needed. The relevant comparison papers were available on arXiv/OA; no Oxford fallback was needed. This is an independent AI audit, not a human/expert or Lean attestation.
