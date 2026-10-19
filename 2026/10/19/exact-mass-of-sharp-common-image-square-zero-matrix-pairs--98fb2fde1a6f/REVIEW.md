# Scientific review: exact mass at the sharp common-image bound

## Correctness — PASS

The claim concerns an explicitly defined positive-rank locus, with \(\dim V=4r\) and \(\operatorname{rank}(AB)=\operatorname{rank}(BA)=r\). The proof first forces both square-zero factors to have rank \(2r\), then identifies their intersection and the common kernel of the products. It reconstructs every pair from an invertible quotient-space parameter, computes the simultaneous stabilizer as an upper triangular four-by-four block group, and sums finite-field orbit sizes. The derivation uses neither genericity assumptions nor division by the field characteristic. The independent finite enumerations for \(q=2\) and a fixed first factor for \(q=3\), plus centralizer computations for three cases in dimension eight, agree with the formulas. Finite checks do not prove the arbitrary-rank assertion; the constructive argument does.

## Originality — PASS, with material risk

The sharp upper bound on product rank is explicitly due to Mohammadian (2012). The general string/band-module theorem of Crawley-Boevey explicitly covers the full algebra \(k\langle x,y\rangle/(x^2,y^2)\) and already provides a broad classification of its finite-dimensional module types. Hence no priority is claimed for an abstract invertible-similarity parameterization by itself. The narrower assessed contribution is the exact finite-field **mass** of the locus saturating the common-image bound, including its explicit centralizer formula and fixed-first-factor count. The inspected accessible statements do not supply those numerical identities. A general module classification could plausibly be specialized to obtain the count, but doing so requires identifying this equality locus and performing the stabilizer computation rather than merely quoting the published theorems. The full text of the paper proving the upper bound was not accessible without an additional authorization step; an equality-case calculation in it remains a real literature-priority risk. The unavailability of that full text is not used as positive evidence of uniqueness.

## Value — PASS

The common-image inequality has a natural saturation problem: determine how abundant sharp pairs are, not just whether the bound is attainable. The closed mass \(q^{-3r^2}\lvert\mathrm{GL}_{4r}(q)\rvert\), together with the fixed-first-factor count \(q^{r^2}\lvert\mathrm{GL}_{2r}(q)\rvert\), answers this throughout all finite fields and dimensions divisible by four. Its uniformity arises from a genuine cancellation of nontrivial similarity-class centralizer weights. This is a natural enumerative invariant of a rank-extremal matrix-equation locus, rather than a specially selected finite table or an unmotivated parameter slice.

## Closest sources and limitations

A. Mohammadian, *Sums and Products of Square-Zero Matrices* (2012), DOI `10.1080/00927872.2011.613423`: accessible publisher abstract establishes the upper bound; complete equality-case material could not be inspected. W. Crawley-Boevey, *Classification of modules for infinite-dimensional string algebras*, arXiv:`1308.6410`, especially the statement including \(k\langle x,y\rangle/(x^2,y^2)\) and Theorems 1.2–1.3: broad prior module classification, not an identified exact sharp-rank finite-field count. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:`math/0211293`: zero-product locus rather than the sharp positive-rank locus. A previously published equality-case calculation or a specialized band-module mass formula could affect originality. No claim of global bibliographic uniqueness or independent mathematical validation is made.

Self-review: passed. Independent audit: not yet performed.
