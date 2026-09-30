# Independent audit — 2026/09/12/063
Assigned/current tree: `216b094440eb5975184aabd79b99d1d562bbdf32`  
Disposition: **repaired**

## Correctness

The explicit witness is valid. Independent face tracing gives twenty 4-faces, so V-E+F=14-40+20=-6 and genus 4, equal to Ringel’s minimum. The map g with b_i↦b_{i+1} and phi=(a0 a1) sends every listed cyclic rotation to the corresponding target rotation up to cyclic shift, and g has order 10. Thus the existence claim is proved without the record’s unavailable enumeration artifacts.

## Originality

Literature classifies regular and edge-transitive complete-bipartite maps, especially balanced K_{n,n}, but those results do not directly subsume this unbalanced K(4,10) minimum-genus witness. Focused search did not locate this exact order-10 symmetric quadrangulation. The audit does not claim priority beyond the explicit witness.

## Scientific value

An explicit minimum-genus embedding carrying a prescribed 10-cycle symmetry is a useful construction. The broader enumeration of 5896 symmetric systems in the original text was not reproducible from the committed package and is removed from the repaired claim.

## Independent checks

- Independent face tracing of the printed rotation system produced 20 quadrilateral faces and genus 4.
- Checked cyclic-order preservation under b_i->b_{i+1}, phi=(a0 a1) at every vertex.
- Did not claim or reproduce the unavailable 5896-system enumeration.

## Limitations

- The files output/artifacts/verification.json, verify_witness.py and enumerate.py are absent from the audited Git tree.
- The audit validates the explicit witness but not the original 5896-system exhaustive enumeration claim; that census is removed from the repaired RESULT.md.
- No uniqueness or classification of all symmetric embeddings is claimed.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/063
- https://arxiv.org/abs/0911.4340
- https://doi.org/10.1002/jgt.22176
- https://arxiv.org/abs/1205.4052
