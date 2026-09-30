# Independent audit — 2026-09-29

Record: `2026/09/16/completing-the-eventual-saturation-spectrum-of-the-five-leaf-berge-star--09064b2edd45`  
Audited source tree: `da0e802810048bcdae41cb638fa76e6a216501a4`  
Disposition: **passed**

## Correctness

The link-SDR characterization and deficiency reduction are correct, and the top-end residue analysis is consistent with the claimed spectrum. Independently of the archived verifier, this audit parsed artifacts/seeds.json and directly recomputed the Berge degree as a bipartite edge-to-neighbor matching: all 28 seeds for residues 1,2,3,4 and deficits 5 through 11 are Berge-K_{1,5}-free and saturated, across 4,084 missing triples. A separate brute-force enumeration of all 9-edge 3-graphs on six vertices reproduced the required zero-witness exclusion. The lantern/K5 padding arithmetic then realizes every deficit >=5 in the needed upper interval, while the small residual components account for the exceptional top deficits. The resulting maximum edge counts give ex_3(5q+r,Berge-K_{1,5})=10q+binom(r,3), exactly as stated.

## Originality

Bushaw–English–Heath–Johnston–Rombach (arXiv:2502.17686) explicitly state that the 3-uniform Berge-K_{1,5} saturation spectrum is completely determined when 5 divides n, and only all-but-constantly-many values are determined in the general l>=5 setting. The audited result fills the four nonzero residue classes for l=5. A focused search found no prior all-residue completion; this is evidence for a genuine completion but is not treated as an absolute priority proof.

## Scientific value

The result upgrades the earlier divisible-by-five theorem to an eventual exact spectrum for every order and simultaneously determines the corresponding extremal number. The finite certificates are small enough to audit directly, while the padding argument turns them into an infinite theorem.

## Limitations

- The larger finite exclusions on 7–9 vertices were supported by inspection of the archived independent edge-branching verifier rather than fully re-executed in this audit; the six-vertex exclusion and all 28 positive seed certificates were independently recomputed.
- The theorem is eventual; the construction bound supplies a sufficient large-n threshold and does not classify every small order.
- The novelty assessment is comparative rather than a priority guarantee.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/16/completing-the-eventual-saturation-spectrum-of-the-five-leaf-berge-star--09064b2edd45
- https://arxiv.org/abs/2502.17686
