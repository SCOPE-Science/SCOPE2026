# Independent mathematical audit

## correctness

PASS

Every level is an automorphism class within its rooted half and has constant multiplicities to neighboring levels, so the weighted path recurrence is exact. Starting from uniform color, leaves separate in round 1. Until round a+1 (for a=m<b), induction peels one paired level from the ends each round: the next newly exposed boundary vertices see d copies of the preceding peeled class, and all interior classes not yet touching a peeled class retain their common color (degree d+1). With a=b, at round a only the two roots share the residual color and they are paired by a graph symmetry. With b=a+1 the taller root has d+1 identical branches of height a and the tree is a regular-tree ball; sphere peeling reaches the center at round b. For b>=a+2 the core B_{a+1},...,B_b has L=b-a>=2 classes of the quotient path that share one color at round a+1. At round a+2 its two endpoint signatures see d and 1 copies of the preceding paired color, respectively; interior core members see neither. Thereafter, among core vertices still sharing a color, only the two residual endpoints see an already individualized core neighbor. If distinct they see distinct such colors; if one vertex remains it is already a singleton. Inductively the remaining core block after j peeling steps has length L-2j, until length at most one. The exact core time is a+1+floor(L/2), including L=2,3. Old colors prevent singleton levels from merging or interacting with earlier paired levels. The paired classes first split at a+3 for P_a, which sees the two different core endpoints; then at each step only the next outward pair has a neighbor in a split pair. The final paired leaf class splits at 2a+3. Stable partitions cannot begin before the last strict split; after both clocks stop the discrete level quotient is stable. Colors distinguish these levels and no automorphism can merge distinct stable colors; rooted symmetries are transitive within a level. In the symmetric cases center/central-edge symmetries act transitively within the paired spheres. Fresh independent quotient recurrence checked 192 cases at d=2,3,4 and 1<=a,b<=8, including terminal quotient partitions; the paired clock example (a,b,d)=(1,6,2) and core clock (1,9,2) exercise each regime of the maximum. Supplemental case and recurrence notes: /workspace/branches/a7facf79-0d71-4de0-a9d9-8a84fe715125/record-3-independent-check.md. This is bounded corroboration, not an all-parameter certificate or fresh full-graph enumeration. Read frozen VERIFICATION.md and verify.py without executing the frozen code.

## originality

PASS

The supported new content is the exact three-regime stopping time, especially the delayed return wave in the unequal-height case. Standard results already give the rooted-neighborhood characterization and imply stable colors equal automorphism orbits on a tree. The nearest exact-depth findings handle different graph families or supply a general bound rather than this depth. No inspected comparison covers the formula; the bounded search cannot establish historical priority.

## value

PASS

The exact stabilization depth of root-joined perfect trees is a motivated benchmark for refinement on a natural branching family. The threshold at a height gap of two, delayed re-splitting of the shorter side, and crossover between outward and inward clocks are not captured by order bounds or by reading leaf distance alone. Independence of branching factor d>=2 quantifies a structural phenomenon rather than a table of specially tuned instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
