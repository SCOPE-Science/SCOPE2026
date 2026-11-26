# Independent mathematical audit

## correctness

PASS

For a root x, the grounded incidence operator sends a potential to its oriented edge differences, with inverse given by edge-to-vertex path incidence. Hence the inverse Laplacian is the sum over edges e of r_e d_e d_e^T, with d_e the indicator of the downstream set. This proves the Green kernel and S=∑ r_e s_e². Changing the root across uv changes only its own downstream set; equivalently the cut component on the opposite side gains a rank-one r·11^T block, extended by zero for its own root. Expanding the Frobenius norm yields the stated edge bracket. For consecutive u,v,w, splitting at the two path edges cancels both outside Green sums and leaves 4S(C,v)+r[a²+(c+d)²]+s[(a+c)²+d²], strictly positive with arbitrary positive resistances. Thus from a neighbor minimum the objective cannot fall along any path, and two minima cannot lie at distance two or more; adjacent ties are allowed (including the n=2 tree). Only the normalized differences are monotone. For the root objective, the dot product of two downstream indicators is zero for disjoint subtrees, and is the smaller subtree size for nested ones; squaring and summing over edge pairs gives ∑ r_v(2d_parent+r_v)s_v². This root calculation, the postorder subtree sums and the preorder one-edge updates all cost O(n) arithmetic operations with O(n) storage. As a hand check, the 3-vertex path with resistances (2,1) gives J=(21,5,12), normalized differences (-8,7). The five-vertex path (100,1,1,1) independently agrees with all reported objectives and chooses vertex 1 rather than the path 1-median vertex 2. Read RESULT.md, VERIFICATION.md, verify_tree.py and verification_output.txt; the frozen 635 trees and 3798 inversions are recorded finite evidence and were not rerun. Exact tie resolution and arithmetic operation counts do not imply numeric bit complexity or floating-point robustness.

## originality

PASS

The second-order objective itself and general leader-selection algorithms are established. The verified distinct result is the strict resistance-normalized geodesic-gradient law for every positively weighted tree with one grounded leader, plus its exact all-root linear arithmetic algorithm. The weighted-star subclass and the multi-leader unweighted path result are real neighboring results, not prior coverage of that law.

## value

PASS

The result supplies a complete optimizer topology and a practical inversion-free exact computation for a standard but less tractable objective than the classical weighted tree median. It explains when local descent is globally sound and exactly how ties can occur for arbitrary positive tree weights, not just for symmetric examples. A weighted path already separates the two criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
