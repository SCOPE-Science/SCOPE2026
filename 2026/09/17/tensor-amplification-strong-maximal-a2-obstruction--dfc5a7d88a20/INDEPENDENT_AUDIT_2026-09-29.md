# Independent audit — 2026-09-29

Record: `2026/09/17/tensor-amplification-strong-maximal-a2-obstruction--dfc5a7d88a20`  
Assigned and audited source tree: `ef2c52e724988bc0021241267e62abb80ab2162d`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The tensor amplification is correct. For product weights, rectangular averages of W and W^{-1} factor exactly, so the strong A2 characteristic is multiplicative. For tensor-product test functions, the strong maximal function also factors pointwise because the rectangle choices in the coordinate blocks are independent; weighted L2 norms then factor. Tensoring m=floor(d/2) copies of Lerner's two-dimensional family gives characteristic comparable to theta^{-m} and norm lower bound theta^{-m}(log(1/theta))^{m/2}. The two-sided characteristic comparison converts this to A(log A)^{m/2} with dimension-dependent constants. Adding an unweighted odd coordinate leaves the characteristic unchanged and cannot lower the test-function ratio. Therefore any linear-power upper estimate with logarithmic exponent gamma must have gamma>=m/2.

## Originality

**qualified_tensor_amplification**. Lerner supplies the two-dimensional A sqrt(log A) obstruction, and Ombrosi-Rey supply recent all-dimensional power-type upper bounds. The product identities are elementary and not new. Targeted searches did not locate the explicit higher-dimensional tensor lower family A(log A)^{floor(d/2)/2}; the novelty claim is therefore limited to this amplification and its near-linear logarithmic-exponent consequence, with substantial concurrency risk because both source preprints appeared in September 2026.

## Scientific value

**useful_dimension_growing_obstruction**. The result shows that the new two-dimensional failure of linear A2 control compounds independently across coordinate pairs, producing a dimension-growing logarithmic obstruction. It materially sharpens what can be true within the linear-power scale, while correctly avoiding any claim of a new pure-power lower exponent or a matching upper bound.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/tensor-amplification-strong-maximal-a2-obstruction--dfc5a7d88a20
- https://arxiv.org/abs/2609.14008
- https://arxiv.org/abs/2609.17246

## Limitations

- The two-dimensional lower family is entirely prior work and is used as an input.
- The result gives a lower obstruction only; it neither proves sharpness of the logarithmic exponent nor a matching near-linear upper bound.
- The amplification is for axis-parallel strong maximal operators and product-coordinate tensor constructions.
- Originality remains qualified because the source papers are extremely recent and the tensorization observation is elementary once Lerner's example is known.
