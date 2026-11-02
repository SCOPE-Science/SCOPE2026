# Scientific review

## Correctness — PASS

The leaf-difference eigenvectors give necessary lower bounds on the number of independently driven leaf vertices. For any eigenvalue other than one, zeros on those leaves propagate through both hubs and along the weighted spine. At eigenvalue one, the remaining Dirichlet path block has simple eigenvalues \(2t(1-\cos(j\pi/L))\), giving exactly the claimed exceptional weights, unique remaining sine mode and its permitted extra sensor positions. The rational list follows from the root-of-unity algebraic-integer argument. Zero forcing is evaluated separately by an explicit propagation proof. The included pure-Python exact-rational verifier passed 1,003 assertions on finite cases; no finite experiment is presented as a proof of the infinite theorem.

## Originality — PASS on inspected evidence, qualified

Monshizadeh–Zhang–Camlibel (2014) address zero forcing and controllability of whole qualitative classes, not the exact gain-dependent minimum sets for a fixed weighted Laplacian. Dai (2023) gives a general \(p(T)-1\) pendant-vertex upper bound, which does not determine this family below the bound or classify which spine sensors work. Parlangeli (2025) gives results for single-hub starlike trees, not two-hub weighted paths. Gupta–Lather–Balaji (2025) already imply the unweighted \(t=1\) multiplicity jump through a distance-mod-three theorem; this known case is explicitly acknowledged. The full positive-weight resonance set, its rational arithmetic reduction and the complete minimum-input location classification were not found in the material inspected. Non-indexed specialist work remains a genuine overlap risk, so search noncoverage is not a uniqueness proof.

## Mathematical value — PASS

The result gives a complete, direct design rule for a natural class of networked control systems with two highly connected endpoints: it replaces a potentially high-dimensional eigenvector and actuator search with a finite list of scalar spectral resonances. It distinguishes exact controllability from the strong structural zero-forcing requirement, identifies infinitely many cases saving one independent actuator, and pinpoints resonant internal positions that can or cannot repair controllability. The rational-weight corollary makes the exceptional set especially easy to implement. No assertion about favorable numerical conditioning near resonance is made.

## Sources and residual risks

Primary materials inspected: arXiv:1403.4868, DOI:10.1049/cth2.12385, arXiv:2507.15472 and preprints:202503.1438. The first three provide respectively the qualitative-class comparison, a general tree upper bound, and coverage of the unweighted extremal multiplicity special case. The fourth concerns single-hub starlike trees. The potential presence of an unindexed two-hub weighted result is not excluded. The stated proof assumes uniform positive spine conductance and unit pendant conductance; no independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
