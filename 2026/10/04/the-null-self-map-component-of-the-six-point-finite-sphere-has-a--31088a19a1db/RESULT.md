# The null self-map component of the six-point finite sphere has an \(S^2\)-core
## Finding
Let \(X_2\) be the canonical six-point minimal finite model of \(S^2\). Label its three levels \(L_0,L_1,L_2\), each with two points, and order distinct points exactly when their levels are strictly ordered. The compact-open self-map space \(X_2^{X_2}\) has exactly \(446\) continuous maps.

The subspace containing the six constant maps and the eight homeomorphisms is a Stong core of \(X_2^{X_2}\). The constants inherit exactly the order of \(X_2\), and all eight homeomorphisms are isolated. Therefore
\[
X_2^{X_2}\simeq X_2\sqcup D_8,
\]
where \(D_8\) denotes an eight-point discrete space. In particular, the component of null-homotopic self-maps strongly deformation retracts onto the constant-map copy of \(X_2\), so that component has the weak homotopy type of \(S^2\).

## Assumptions and scope
The topology on a finite \(T_0\)-space is represented by its specialization order. For finite spaces, the compact-open topology on a function space agrees with the pointwise order. A down beat point is a point whose strict lower set has a maximum; an up beat point is defined dually. Removing a beat point is a strong deformation retract.

The claim is only about the canonical six-point finite sphere model and its ordinary unbased self-map space. It does not assert that finite modeling commutes with classical mapping-space constructions, nor does it classify self-map spaces of larger finite models of \(S^2\).

## Proof
Write the six points as \(0,1,2,3,4,5\) with level function \(0,1\mapsto0\), \(2,3\mapsto1\), and \(4,5\mapsto2\). Thus \(a\le b\) exactly when \(a=b\) or the level of \(a\) is strictly smaller than the level of \(b\).

The accompanying verifier exhausts all \(6^6\) set maps and retains exactly those preserving this order. It finds \(446\) continuous self-maps. These maps are ordered pointwise. Starting with the full map poset, the verifier repeatedly scans maps in lexicographic enumeration order and removes the first available beat point, preferring a down beat point to an up beat point. For every deletion it recomputes the induced strict lower and upper sets and verifies the required unique extremal witness before deleting the point.

After exactly \(432\) valid beat-point deletions—\(352\) down and \(80\) up—the survivors are exactly fourteen maps: the six constants and the eight bijective order maps. Since every beat-point deletion is a strong deformation retract, this fourteen-point subspace is a strong deformation retract of the full function space.

The verifier then checks two independent structural conditions on the survivors. First, the order among the six constants is exactly the original order on \(X_2\), because \(c_a\le c_b\) holds exactly when \(a\le b\). Second, every bijective order map is incomparable with every other self-map already in the full mapping poset, hence is isolated. Finally, the fourteen-point survivor subspace has no beat points. It is therefore a core, homeomorphic to \(X_2\sqcup D_8\).

## Verification
Run `python verify.py`. The program uses only the Python standard library. It reconstructs \(X_2\), enumerates every set map, checks order preservation, constructs the full pointwise order on the \(446\) continuous maps, performs the complete beat-point reduction, and verifies the structure and beat-point-freeness of the surviving subspace.

The expected output begins with `VERIFY_OK` and records `self_maps=446`, `beat_deletions=432`, `core_size=14`, and deletion-sequence SHA-256 `5d3ed002bf3422a74be756d3d44d4d0d75f5bdb08039335624871b65a2614fd1`. The embedded `verification_output.txt` is the output from the packaged verifier.

## Relationship to prior work
Barmak and Minian prove that the canonical \(2n+2\)-point non-Hausdorff sphere is the unique cardinality-minimal finite model of \(S^n\); for \(n=2\) this supplies the six-point object studied here. Barmak's finite-space text proves that the compact-open topology on \(Y^X\) is the pointwise order for finite spaces and that deleting beat points gives strong deformation retracts. Those results provide the framework but do not give this \(446\)-map census or the fourteen-point core.

A previously established self-map classification for the same sphere family determines only connected components: nonhomeomorphisms lie in one homotopy class and the homeomorphisms give isolated classes. Connectedness alone does not determine the strong homotopy type of that large component. The present core computation supplies the missing internal homotopy type: its core is the six-point sphere itself.

Kandola studies topological complexity of minimal finite sphere models and emphasizes that invariants of finite models can differ from those of the classical spheres. That paper does not compute compact-open self-map spaces or their cores.

## Limitations
The proof is a finite exhaustive proof for \(X_2\), not an all-dimensional theorem. The beat-point reduction is deterministic but not claimed to be the only possible reduction sequence; core uniqueness makes the resulting core type independent of that choice. The novelty comparison covered the directly relevant foundational full texts and multiple statement-level database searches, but unindexed literature remains a residual risk.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, submitted 2006-11-06; especially Theorem 2.13 and Corollary 2.14.
2. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, 2011; especially Proposition 1.2.5 and Proposition 1.3.4.
3. S. Kandola, *The Topological Complexity of Finite Models of Spheres*, arXiv:1812.07604v1, 2018.
