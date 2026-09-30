# Independent audit — 2026-09-29

Record: `2026/09/18/finite-field-schreier-multilinear-collapse--b7bca1b352fc`  
Assigned and audited source tree: `9f71d9b753adb51812761efc15529b109eb6d6c5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The rigidity theorem follows cleanly from Kearnes–Moorhead–Szendrei's 2026 classification. Their Theorem 4.1/Lemma 3.1 framework says that a nontrivial locally finite Schreier variety with the stated constant condition is uniformly polynomially equivalent either to G-sets for one finite group or to vector spaces over one finite field, for all members, not only finite ones. The G-set case is impossible here because the original vector addition is a genuinely binary term operation. In the affine/vector-space case, each basic m-ary operation is an affine polynomial c+sum lambda_i x_i in the auxiliary vector-space structure. If m>=2, setting any one input to the original additive zero and varying the remaining inputs forces all coefficients except possibly the fixed coordinate to vanish; doing this in two distinct coordinates forces every coefficient to vanish and the constant to equal the original zero. Thus every extra multilinear operation is identically zero. The converse zero-operation variety is just finite-field vector spaces with named zero operations, so subalgebras of free algebras are free. The unital contradiction and the one-bilinear-operation corollaries follow immediately.

## Originality

**qualified_short_corollary**. The main classification is entirely prior work from September 2026, so this record is best viewed as a concise finite-field multilinear specialization rather than a new classification theorem. Lewin's 1968 result is explicitly for infinite fields, while Burgin's 1974 work treats linear Omega-algebras over commutative rings under homogeneous-identity hypotheses and gives an infinite-field corollary. Those older statements do not by themselves subsume the record's arbitrary locally finite finite-field formulation as audited here, but they materially limit the novelty claim. No broad priority claim is warranted.

## Scientific value

**useful_rigidity_corollary**. The specialization is useful because it gives a very sharp consequence for finite-field multilinear algebra languages: local finiteness plus the Schreier property kills every genuinely higher-arity multilinear operation. It also settles the locally finite unital and zero-product special cases in one line from the modern classification, while making clear why infinite-field Vandermonde arguments are not the mechanism being used.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/finite-field-schreier-multilinear-collapse--b7bca1b352fc
- https://arxiv.org/abs/2609.19651
- https://doi.org/10.1070/SM1974v022n04ABEH001705
- https://doi.org/10.1090/S0002-9947-1968-0224663-5

## Limitations

- The result is a specialization of the 2026 locally finite Schreier classification, not an independent classification theorem.
- Burgin's 1974 paper has overlapping linear-Omega-algebra scope under homogeneous-identity assumptions; the authorized retrieval available in this run exposed bibliographic pages but not enough theorem text to claim exhaustive non-overlap.
- The proof uses polynomial equivalence to an auxiliary finite-field vector-space structure; it does not identify that auxiliary field with the originally named field k, and it does not need to.
- The theorem assumes local finiteness and multilinearity of every extra operation of arity at least two.
