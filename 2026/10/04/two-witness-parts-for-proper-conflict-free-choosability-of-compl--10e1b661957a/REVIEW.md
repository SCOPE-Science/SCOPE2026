# Same-model scientific review

## Claim
Every connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\) is proper conflict-free \((\mathrm{degree}+2)\)-choosable. If \(r\ge3\), then \(G\) is proper conflict-free \((\mathrm{degree}+1)\)-choosable.

## Correctness
PASS. The proof uses two witness parts. The first part contains a color \(\alpha\) used exactly once. The second part can avoid the first palette and contains a second singleton color \(\beta\): with offset two its lists have at least \(n_1+2\) colors, and with offset one the existence of a third nonempty part supplies the same inequality. Every later part has more available colors than the number of colors used on earlier parts. Palettes are therefore disjoint across parts, making the coloring proper, while \(\alpha\) and \(\beta\) remain unique neighborhood witnesses. The packaged implementation passed all exhaustive and deterministic stress tests described in `VERIFICATION.md`.

## Originality
PASS. The 2025 source poses the degree-choosability program and the degeneracy conjecture. The 2026 sparse-graph full text states the stronger universal \((\mathrm{degree}+2)\) conjecture and the minimum-degree-three \((\mathrm{degree}+1)\) conjecture, and proves \(K_{2,r}\) as an auxiliary special case. Full-text and targeted database searches found no theorem covering all complete multipartite graphs or the three-or-more-parts offset-one refinement. The closest indexed record concerns non-list proper conflict-free chromatic numbers of crown graphs and does not imply these list-choosability statements.

## Value
PASS. Complete multipartite graphs form a basic dense family that is not covered by the sparse maximum-average-degree theorems. The first clause verifies the recent universal offset-two conjecture throughout this family, strictly extending the published \(K_{2,r}\) slice. The second clause reaches offset one for every multipartite graph with at least three parts, matching the stronger conjectural scale whenever its minimum-degree hypothesis applies and exceeding that hypothesis for some smaller-degree cases.

## Closest literature and limitations
The closest proved primary result located is Proposition 3.2 of arXiv:2601.15611 for \(K_{2,r}\). The same paper gives sparse-class theorems controlled by maximum average degree, which do not cover dense complete multipartite graphs in general. No claim is made that the offsets here are optimal, and complete bipartite offset-one choosability is left open by this argument.

Same-model review: passed. Independent audit: not yet performed.
