# Scientific review: sharp variance reversal in incidence-based accumulation

## Correctness

**PASS.** The claim fixes deterministic incidence tables without zero rows or columns, the uniform-without-replacement sampling law, common row-occupancy multisets, and strict variance ordering at two distinct interior sample depths. The variance identity is derived from indicator covariances and independently reconstructed by direct subset enumeration. The no-go theorem is proved for one or two sites, at most two species, and three sites with at most three species. At the total-size-seven boundary, an exhaustive canonical-mask construction covers all \(42\) species-and-site relabeling classes in each admissible dimension, verifies all same-profile pairs, and returns exactly four reversing pair-orbits. Exact rational results agree between two computational methods. The standalone `verify.py` source is included and was executed successfully.

## Originality

**PASS, subject to the stated residual risk.** Ugland, Gray and Ellingsen (2003, DOI `10.1046/j.1365-2656.2003.00748.x`) provide the general conditional covariance formula for sample-based accumulation, and Colwell, Mao and Chang (2004, DOI `10.1890/03-0557`) provide the mean-curve theory and a highly relevant pair of incidence matrices with identical occupancy spectra but differing patchiness (Table 2). These prior results are fully acknowledged: neither the covariance formula nor mean-curve blindness to incidence arrangement is presented as new. Inspection of the relevant proofs, tables, and discussion did not reveal the sharp seven-vertex crossing threshold or the four complete minimal pair-orbits. Published mathematical research on iid species discoveries addresses a different site-versus-individual sampling structure. A broader unindexed small-matrix classification remains a risk, so absence from the inspected sources is not treated as a proof of global novelty.

## Value

**PASS.** Precision of sample-based species richness is meaningful for biodiversity inventories and effort planning, and identical expected accumulation curves do not determine which of two communities will have a more variable observed richness at different effort levels. The smallest possible configuration, complete classification of all its reversing examples, and exact three-site diagnostic replace an arbitrary example with a structural boundary. This is a limited but self-contained fact, not a claim about empirical prevalence or statistical confidence intervals.

## Closest literature and limitations

The nearest literature is Ugland et al. (2003), particularly Appendix I, and Colwell et al. (2004), particularly the incidence examples in Table 2 and the interpolation discussion. The former supplies the general variance formula, and the latter already demonstrates nonidentification of incidence arrangement from mean accumulation curves. Neither directly supplies the boundary classification. The claim is limited to uniformly sampled fixed binary inventories with possible species occupancy duplicates; it neither estimates unknown community richness nor handles sampling/measurement error. External independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
