# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/boundary-averaged-zeros-split-equilibria-rossler-zero-hopf--e55f9e3b5fad`  
Assigned and audited source tree: `a397b4b1a472bd543cadcd49c8f9d5aec52bb7f8`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `c036b4128e03aebf1e66fd71c3d46bd5c4f63cc6`  
Disposition: **passed**

## Correctness

**independently_supported**. The correction is mathematically sound. Solving the exact equilibrium equations gives x_sigma=(c+sigma sqrt(c^2-4ab))/2 and the O(epsilon) splitting stated in the record. Independent symbolic solution of the source's linear coordinate map on the equilibrium line gives exactly u=v=0 and w=-(2-a^2)(x-a)/a^2, so after the source blow-up the two equilibria converge to the two R=0 averaged roots with opposite labels. Independently expanding the Cartesian characteristic polynomial gives the stated slow eigenvalue and the real/imaginary first-order corrections of the complex pair; dividing the real rates by the fast angular frequency matches the two eigenvalues of the averaged boundary Jacobian. Therefore the boundary roots are quantitatively accounted for by exact equilibria, and first-order polar averaging at R=0 cannot by itself establish two additional nonconstant cycles.

## Originality

**qualified_source_specific_correction**. The source preprint of September 2026 publicly claims three distinct bifurcating periodic-orbit families. General warnings about polar singularities, zero-Hopf averaging domains and Rössler normal forms are prior art. Targeted searches did not locate the specific identity that the source's two boundary roots are precisely the scaled split equilibria together with the matching first-order spectral drifts. The originality claim is therefore appropriately limited to this correction of the current source's inference.

## Scientific value

**high_source_specific_corrective_value**. The source advertises the three-family count as a principal extension of earlier one-orbit work. Showing that two of its first-order roots shadow equilibria materially changes what that calculation proves, while carefully preserving the positive-radius interior candidate and leaving open smaller-amplitude cycles.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/boundary-averaged-zeros-split-equilibria-rossler-zero-hopf--e55f9e3b5fad
- https://arxiv.org/abs/2609.17336v1
- https://doi.org/10.1088/1361-6544/ab8bae
- https://doi.org/10.1142/S0218127420300505
## Limitations

- This is not a nonexistence theorem for all small periodic orbits near the split equilibrium branches.
- The interior R>0 averaged root is not challenged.
- The result is tied to the source's unfolding and coordinate normalization.
- It does not independently settle every non-integrability claim in the source.
