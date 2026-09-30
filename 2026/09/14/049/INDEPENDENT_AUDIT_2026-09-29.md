# Independent audit — 2026/09/14/049

**Date:** 2026-09-29  
**Disposition:** **REPAIRED**  
**Audited tree:** `b081d5a916057ebaf07fcecaf7e5d8d22349c278` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**REPAIRED** — The low-dimensional fiber classification is credible and is supported by the exact F2 census and characteristic-free (1,1)-divisor argument. The filed decomposition-number purity conclusion, however, does not follow from the cited Maksimau result: that paper sets up the parity/canonical-basis theory for Dynkin quivers, and its even-quiver consequences are stated in that Dynkin framework. The wild 3-Kronecker case cannot inherit parity=IC/perversity or characteristic-independent decomposition numbers solely from fiber odd-cohomology vanishing. The repaired record keeps only the independently justified fiber-evenness theorem.

## Originality

**PASS_WITH_CAUTION** — Targeted searches found no exact published classification of all fourteen (2,2) 3-Kronecker Lusztig fibers. Wild-quiver quiver-Grassmannian literature shows that much more complicated geometry occurs in larger dimensions, so this small calculation is not a general theorem. Priority is not claimed.

## Value

**PASS** — The explicit wild-quiver low-dimensional evenness calculation is a useful test case for possible extensions of parity/KLR machinery, provided it is not advertised as a decomposition-number purity theorem.

## Literature/evidence checked

- [Maksimau, Canonical basis, KLR-algebras and parity sheaves](https://arxiv.org/abs/1301.6261): Primary cited source; its setup explicitly assumes a Dynkin quiver.
- [Lorscheid, Representation type via Euler characteristics and singularities of quiver Grassmannians](https://doi.org/10.1112/blms.12272): Shows broad complexity of wild-quiver Grassmannians; context only.

## Limitations of this audit

Literature comparisons are claim-specific and do not constitute an exhaustive priority proof. GitHub was read only. Computations described as independent were reconstructed from stated finite data or supplied artifacts; no inaccessible paper is claimed as read.
