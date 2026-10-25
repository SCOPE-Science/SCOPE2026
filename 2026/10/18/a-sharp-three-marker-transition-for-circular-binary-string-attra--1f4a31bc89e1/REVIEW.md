# Independent mathematical audit

## correctness

PASS

For cyclic w=0 1^a 0 1^b 0 1^c with 1≤a<b<c, every two-position attractor must include a zero and a one. Unique 1^c forces the one into the c-run, and unique 0 1^a 0 and 0 1^b 0 occurrences force the zero to shared Z1. Unique factors 1^(a+1)0 and 1^(a+1)0 1^(a+1) force necessary c−a≤j≤a+1. The sufficiency proof explicitly splits the unmarked circle after marking {Z1,X_j} into arcs A=1^b 0 1^(j−1) and B=1^(c−j)0 1^a. Pure ones, factors with ≥2 zeros, and single-zero factors 1^u 0 1^v exhaust all nonempty cyclic factors: every candidate occurrence confined to A or B has a translated occurrence covering a marked position at Z1 or X_j. When c≥2a+2 no j exists and the explicit triple {Z1,X_(a+1),X_(c−a)} covers all factors by analogous arcs. Therefore pair sets precisely j=c−a,...,a+1, count max(0,2a+2−c), γ*_c(w)=2 below the threshold and 3 above, independent of middle b. Separately implemented direct circular-occurrence bitmask enumeration checked all 56 distinct triples a<b<c≤8 with 20 two-phase and 36 three-phase cases and every pair, plus the three-point witnesses; finite check supplements the all-parameter arc argument.

## originality

PASS

Best-of-knowledge PASS: 2021 Mantaci–Restivo–Romana–Rosone–Sciortino provides foundational circular attractors and a characterization of *consecutive* size-two attractors for primitive Sturmian words; 2023 Romana gives a general linear verification and NP-completeness. Neither statement determines the nonconsecutive two-marker pairs for a distinct three-gap circular family, its exact count, or the b-independent 2-to-3 transition. Equivalent transformations of ordinary, noncircular attractors are not valid because wrap-around factors differ. Unindexed structural family results remain possible.

## value

PASS

This is a complete infinite-parameter classification for a natural simplest nontrivial family of sparse-zero cyclic words. The exact threshold c=2a+1, all optimal pairs and the surprising cancellation of b give a small meaningful structural invariant, potentially useful as a test case for circular-attractor algorithms and extremal constructions. Not merely finite census or relabeling of a known consecutive-position result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
