# Independent mathematical audit

## correctness

PASS

A windmill W_{r,m}=K1 join rK_m has pairwise twin omitted peripheral vertices in a blade; if two are omitted, their open-neighborhood signatures coincide, so each blade must omit at most one. For m≥3 this condition is sufficient: ≥m−1≥2 selected/blade gives total domination and separates all same-blade, different-blade and center signatures, with or without center. Each blade contributes x^m+m x^(m−1), center contributes 1+x. For m=2 an omitted center forces all blades full because a lone selected blade vertex otherwise has empty open signature; center included allows at most one deficient blade because two selected solitary vertices would both have signature {c}. Hence enumerator (2r+1)x^(2r)+x^(2r+1). Independent direct bitmask open-signature brute force exactly matched distributions for (r,m)=(2,2),(3,2),(2,3),(3,3),(2,4), including (3,3) {6:27,7:54,8:36,9:10,10:1}. Inspected verify_old_windmills.py checks ten small cases; proof is all-parameter combinatorial.

## originality

PASS

Chellali/Jafari Rad/Seo/Slater (2014) Theorem 3.3 already covers the friendship m=2 MINIMUM scalar gamma^OLD=2r and is credited, not claimed as new. Their classification does not count all such sets or describe general m≥3 windmills. Chakraborty/Foucaud/Parreau/Wagler (2024) prove block-graph algorithms/bounds, including gamma^OLD≤|V|−m_Q−1, which only yields ≤rm here, not equality r(m−1) or the full polynomial. A published Resultary finding about dissociation polynomial of generalized windmills concerns different admissibility predicate. Best-of-knowledge original full OLD-set characterization; known scalar segregated.

## value

PASS

All-set OLD-polynomial and exact minimum multiplicities are natural surveillance/code invariants of canonical block graphs. The friendship m=2 boundary changes qualitative form and demonstrates a real signature collision; formulas give more than generic block-graph algorithm outcomes. A complete exact classification can be useful independently of a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
