# Independent mathematical audit

## correctness

PASS

Direct independent enumeration from the 32 exact STELLAR triangles (not execution of the submitted verify.py) reconstructs f=(12,48,32). GF(2) triangle equations have rank 31, so dim Z1=17; vertex coboundaries rank 11, so dim H1=6. Explicitly generated all 2^11=2048 coboundaries and 2^6=64 quotient representatives, checked disjoint 2048-element cosets exhaust 131072 cocycles; 63 nonzero class weights/counts are 16*(6,1), 24*(10,4), 6*(12,8), 16*(14,18), 1*(16,12). Generated 192 permutations from four generators printed in Köhler–Lutz Table 13, verified every element preserves the complete facet set. Their computed H1-orbits have sizes 16,24,6,16,1 with those constant profiles; transported all minimizing cochains and recovered support-orbit splits [16], [48,48], [24,24], [96,192], [12]. Reconstructed pinned Git source tree SHA, including nested artifact tree. All quantifiers concern one 12-vertex complex over F2 with edge-support weight; no analytic/infinite extrapolation.

## originality

PASS

Qualified best-of-knowledge originality. The primary Köhler–Lutz source identifies exactly this triangulation and its 192-automorphism group, and the STELLAR table gives all 32 facets, but neither source tabulates cochain coset-leader minima, the five H1-orbits, multiplicities or minimum-support orbits. Four semantic Resultary queries returned the exact assessed finding itself and other finite-complex invariants, not an independent covering result. General genus-three topology gives dim H1=6 but no edge-support spectrum. Historical realization papers use the same named object but their available abstracts concern embeddings, not cocycle support. The priority risk of an unindexed exact computation and incomplete access to geometry papers is genuine; neither by itself defeats the positive judgement.

## value

PASS

The exact 12-vertex Dyck regular map is a canonical and unusually symmetric triangulation of a genus-three surface, and the edge-support one-cosystolic metric is a mathematically natural H1 quotient-code invariant. Its full 63-class spectrum, stabilizer orbits and minimizing-support decompositions provide a complete finite classification with meaningful distinctions (unique invariant weight-16 class and sixteen uniquely represented weight-6 classes). Genus/Bettis and automorphism-group order alone do not force these data, and a researcher comparing combinatorial systolic behavior or quotient cochain codes could use this reproducible exact benchmark. The computation is bounded, but neither an arbitrary slice nor a known-table recomputation. No broader theorem or triangulation-independent claim is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
