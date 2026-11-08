# Independent mathematical audit

## correctness

PASS

With T selected rim vertices, an unselected rim u has distance ones at precisely its selected neighboring rim vertices, zeros if itself selected and twos elsewhere; the hub has ones to all rim landmarks. If |T|<=2, at least five unselected rim vertices must share at most four binary signatures and cannot all be resolved; for |T|>=3 every omitted rim vertex differs from the hub because it has at most two selected rim neighbors. Empty-signature duplicates arise from two cyclic zero-runs with at least three zeros; nonempty duplicate signatures for m>=7 arise from neighbors of the same selected rim vertex separated by 00100, which is exactly two long (>=2) gaps adjacent in selected-vertex order. Thus admissible gaps are 0..3 with at most one 3 and cyclically nonadjacent long gaps. For k selected vertices there are k/(k-j)*binom(k-j,j) independent j-position long-gap choices on the cycle C_k; each long gap contributes u^2, with option for exactly one 3 contributing factor (1+j*u), while other gaps contribute (1+u)^(k-j). m/k marks/demarks a selected start, deriving all c_{m,k} as integers and P_m=(1+z)R_m. Gap capacity m<=floor(5k/2)+1 yields beta=ceil(2(m-1)/5)=floor(2(m+1)/5), with attainable patterns; deficits at most 2 at minimum k yield the five residue formulas by direct coefficient extraction. Independent BFS-free shortest-path signature enumeration checked all 65,408 rim subsets m=7..15 (with hub equivalence by proof) and every coefficient; separate exact rational computation checked minimum coefficients and integer base formulas m=7..400. Exact SHA-1 Git object reconstruction matched the eight-file assigned source tree. Neither finite check proves m unbounded: that rests on the combinatorial proof. Scope excludes m<7, nonwheel or unlabeled automorphism-orbit counts.

## originality

PASS

A best-of-knowledge PASS only for the closed labeled all-cardinality wheel resolving-set polynomial and five explicit metric-basis multiplicity formulas. Ordinary-wheel metric dimension was known in 2002, and an essentially equivalent rim-gap admissibility characterization is in 2021; neither is counted as new. The inspected older primary texts do not supply the coefficient evaluation or five multiplicities, while the broad minimal-solution enumeration work provides algorithms/complexity rather than this all-size closed form. Related published resolving-polynomial results concern chain graphs, not wheels. No worldwide priority guarantee: nonindexed literature and especially an unknown older enumeration under a different term remain genuine risks.

## value

PASS

A complete natural invariant of an important elementary graph family, the generating polynomial counts resolving landmark designs at every cardinality, not just the previously known minimum count. The five exact formulas for numbers of distinct minimum sets demonstrate real modulo-five fluctuations (e.g. m=10:35, m=11:11, m=12:96) at comparable sizes, quantify redundancy and available optimal configurations, and permit exact benchmark or random-design probabilities. The long-gap independent-cycle structure is a motivated combinatorial technique, not merely a parameter renaming or a one-instance tabulation. A closed form is a self-contained useful contribution even if previous structural feasibility is known; no downstream general theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
