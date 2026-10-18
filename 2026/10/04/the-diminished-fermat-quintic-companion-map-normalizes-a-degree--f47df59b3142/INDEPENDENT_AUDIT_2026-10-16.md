# Independent mathematical audit

## correctness

PASS

The exact six quintics from Kabat–Strycharz-Szemberg are base-point free by their Lemma 5, hence induce P²→P⁵ with pullback O(5). Any positive-dimensional fiber contains a curve, impossible since O(5) has positive degree on every curve; the morphism is finite onto its image. Direct substitution at [1:2:1] yields [4:12:−4:39:0:−35]. In chart C=1 the cross equations factor as 4(A−1)(A⁴+A³+6A²+A+1), 4(15A³−B⁵+5B²−3), 5(39A³−4B³−7), −20B²(A−1)(A²+A+1); when A≠1 the other equations contradict B=0 or A³=1, while A=1 forces B²=4,B³=8, hence B=2. Jacobian of normalized first and third equations at that point is −480, verifying a reduced singleton fiber. Finite degree-one map from normal P² gives normalization, and (5L)^2=degree(X)=25. Independently recomputed all five exact cross-polynomial factorisations and the Jacobian with SymPy, not just accepted VERIFY_OK.

## originality

PASS

Kabat–Strycharz-Szemberg 2020 actually provide these six forms and Lemma 5 base-point freeness, then explicitly propose investigating the companion surface; no birationality, normalization, or image degree. Di Gennaro et al. 2022 arXiv:2101.07346 full text contains degree-25 companions for a DIFFERENT root-system morphism in section 4 and degree m²+m+1 for an augmented ordinary Fermat arrangement in section 5. Those do not use this six-dimensional diminished-Fermat system; matching degree 25 is insufficient for implication. Published Resultary search first found only the assigned record.

## value

PASS

The exact degree and normalization answer the concrete companion-surface question raised by the authors; a reduced singleton-fiber certificate is nontrivial and clarifies geometry of the explicit morphism without asserting unsupported smoothness or embedding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
