# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed both graph adjacencies from RESULT.md and verify.py, confirmed degree 6 and common-neighbor count 2, all 2^16 vertex masks via independent connected-component cyclomatic test. Exact Sh faces by size 0..7: (1,16,120,528,1440,2352,1952,512); rook: (1,16,120,528,1392,2160,1728,576); no larger forests. Fresh greedy vertex-toggle acyclic Morse DAG has 3370/3204 pairs, respective critical 4-,5-,6-cell counts (2,143,36)/(4,37,72). Independent signed integral Morse differential computation gives ∂6=0, ∂5 ranks 2/4 with unit maximal minors as in source; these kill degree-4 cells primitively. Homotopy cancellation and π5(wedge S5)=Z^k then yield Sh ∨141 S5 ∨36 S6 and rook ∨33 S5 ∨72 S6, not merely rational Betti equality.

## originality

PASS

PASS, best of knowledge: Taylan 2015 develops general devoid simplicial complexes and Morse matchings; Carnero Bravo 2023/2025 develops induced forest filtration and explicit families of paths, cycles, double stars, cactus graphs and selected products, not the two (16,6,2,2) graphs. Existing published Shrikhande/rook independence complex wedge counts use a stricter forbidden-edge predicate and imply neither forest homotopy type. No exact induced-forest pair table located, with unindexed prior-work risk.

## value

PASS

PASS: these are the classic same-parameters nonisomorphic strongly regular pair. Calculating their full torsion-free mixed-dimensional induced-forest homotopy gives a natural structural counterexample to determination by SRG parameters or equal feedback vertex-set number, a mathematically motivated comparison beyond raw enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
