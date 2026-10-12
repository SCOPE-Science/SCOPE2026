# Self-review

## Correctness
**PASS.** The claim reduces the continuous local-basis optimization to an exact collision formula derived from the complete Pauli correlation tensors of the Higuchi–Sudbery state. The Boolean-cube Parseval normalization was reconstructed explicitly. The four-vector Gram determinant identity and the frame-operator bound imply the global inequality \(\sum_s p_s^2\le1/6\) for arbitrary unit Bloch axes, not merely sampled axes. Equality analysis is also complete: saturation forces rank one of the frame operator, hence a common Bloch line, and such bases attain the bound. The included standard-library checker independently evaluates all required Pauli tensors exactly and verifies the Gram polynomial identity.

## Originality
**PASS.** The 2015 defining paper reports \(S^{\mathrm{RIU}}_2(HS)=\log6\) in a section explicitly based on further numerical tests, and the 2016 survey marks the same table entry as conjectured from numerical calculations. The accepted contribution is therefore not the numerical value itself, but an exact proof over all local product bases plus a complete equality characterization. The original Higuchi–Sudbery work concerns average bipartition entropy, while geometric-measure work concerns the largest single product overlap, not the order-two collision sum. Targeted searches using RIU, decomposition-entropy, collision/index-of-coincidence, local-basis, and \(1/6\) aliases found no implication-equivalent analytic proof. Residual risk remains that a later derivation is poorly indexed or uses different terminology.

## Value
**PASS.** The source identifies order-two RIU entropy with an experimentally meaningful two-copy coincidence statistic, while the exact HS value was left at the numerical/conjectural level. The theorem removes the continuous four-local-unitary numerical optimization for this canonical four-qubit state and replaces it with a short invariant Gram inequality. The equality classification additionally identifies all optimal measurement geometries. This is a substantive structural certification rather than a recomputation of a table entry.

## Closest literature and limitations
The closest source is arXiv:1506.04788, which defines the functional and reports the HS order-two value numerically. The 2016 survey DOI:10.1088/1742-6596/698/1/012003 explicitly marks that value as numerically conjectured. arXiv:quant-ph/0005013 and arXiv:0905.2094 optimize different entanglement quantities and do not imply the product-basis collision bound. The present result does not establish the broader global-maximizer conjecture for \(q\ge2\).

Self-review: passed. Independent audit: not yet performed.
