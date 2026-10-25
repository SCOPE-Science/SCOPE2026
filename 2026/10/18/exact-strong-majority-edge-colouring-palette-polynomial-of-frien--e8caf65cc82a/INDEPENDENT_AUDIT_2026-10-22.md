# Independent mathematical audit

## correctness

PASS

PASS: For friendship graph F_n, each triangle base edge has two spoke neighbours and forces its spoke colours to differ. For a spoke edge colour beta and test colour alpha, adjacent alpha count is S_alpha - 1_{alpha=beta} + 1_{alpha=c_i} out of 2n neighbouring edges. Since a fixed alpha occurs at most once in each triangle, S_alpha<=n; the only possible violation is choosing a base colour alpha with S_alpha=n. Thus each triangle base has q-k available colours where k=0,1,2 are universally present spoke colours. Inclusion-exclusion on q(q-1) ordered spoke pairs per triangle gives A0,A1,A2 and P_n(q)=q^n A0+(q-1)^n A1+(q-2)^n A2. P_n(2)=0 and fixed pair of spoke colours plus a third base colour works, so index is 3; this index was previously known.

## originality

PASS

PASS (best of knowledge): Kalinowski et al Proposition21 already implies index three for Eulerian friendship graph with 3n edges, and Antoniuk et al and Pękała–Przybyło improve general upper bounds. Those existence theorems are expressly credited and do not imply the full labelled-palette counting polynomial, with every number q of named colours. The universal-spoke-colour filtration is a new exact counting detail in the bounded comparisons.

## value

PASS

PASS: The friendship/windmill graph is a standard infinite triangle family and strong-majority edge colouring a newly developed nonproper colouring invariant. An exact named-palette counting polynomial is a natural enumerative strengthening of its already-known chromatic threshold, resolving multiplicities and asymptotic growth, not merely recomputing the index 3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
