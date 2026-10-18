# Scientific review: integral height-two tree homology module

## Correctness — PASS

The graph family and permitted faces are defined by induced-component size. The link of the central root has the exact simplicial decomposition into the full leaf simplex and the cones over all complementary leaf simplices. With at least two nonempty branches, these complements are nonempty and allow a symmetry-compatible deformation retraction to the full leaf simplex; attaching the cone on the link does not change the underlying homotopy type. The root-deletion inclusion is symmetry-equivariant, giving integral equivariant homology isomorphisms. Each star factor has circle-wedge homology equal to the leaf permutation augmentation kernel. The join Künneth theorem yields a free tensor product in degree \(2a-1\), and the parity of interchanging two degree-one join classes gives the positive branch-swap sign. The tensor-cycle trace identity proves the general character formula. A separate sequential distinguished-leaf matching has exactly the predicted top-dimensional critical faces and is acyclic. No finite test is substituted for the infinite argument. Boundary cases \(a=2\), \(b_i=1\), and equal/unequal branch sizes have been checked.

## Originality — PASS, qualified

The nearest earlier general formula is Deshpande–Singh, Theorem 5.6, which already settles the **nonequivariant homotopy type** in the balanced perfect-ary subfamily. Theorem 3.10 does not apply because this tree's root has no leaf neighbor. Ghosh–Selvaraja (2025, Theorem 4.8) already prove shellability for all diameter-four trees, including this entire family. Sawant's May 2026 theorem gives vertex decomposability for all trees, not the precise integral representation, wreath action, or characters. Abdelmalek et al. study decomposability, not this action. Published-results searches for the object under its higher-independence and three-path-free names, augmentation tensor modules, branch permutations, and stronger families did not identify an equivalent formula. The substantial remaining risk is undiscovered published or unpublished representation calculations; a negative search is not proof of uniqueness. The claim neither renames the balanced formula nor presents it as new.

## Value — PASS

The integral homology module is a natural complete symmetry invariant of an entire graph family, including nonuniform branching. It detects within-arm permutations and nontrivial branch-exchange actions, which no nonequivariant wedge rank determines. The explicit cycle-wise character evaluates every automorphism without chain-matrix computation, and the homotopy multiplicity gives an exact threshold between contractibility and a uniform-dimensional sphere wedge. These facts address a motivated equivariant topological gap distinct from generic shellability or homotopy existence.

## Independent validation and limitations

The code exhaustively verifies nine finite profiles, their augmented Hasse acyclicity, mod-two Betti numbers, and representative full-simplicial Lefschetz traces. It does not prove arbitrary parameter values. No external audit, integral lattice verification by an independent specialist, or exhaustive priority certification has occurred.

Self-review: passed. Independent audit: not yet performed.
