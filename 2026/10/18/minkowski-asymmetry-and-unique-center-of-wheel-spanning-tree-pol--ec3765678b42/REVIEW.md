# Independent mathematical audit

## correctness

PASS

In the affine hull x(E)=n, reflection at dilation s is equivalent to (s+1)c−1_T belonging to sP for every tree T. The minimum count is zero for both the rim and each hub triangle: the spoke star avoids the former, and deleting one triangle leaves both its rim endpoints attached through the complementary rim vertices and their spokes. The rim and the summed triangle inequalities give 2n ≤ (s+1)c(R) ≤ s(n−1). At s=2n/(n−1), the proposed scaled center has spoke weight (n+1)/(n−1) and rim weight 2. Against any tree, the reflected vector has the correct total and is nonnegative. For a hub-containing proper vertex set with k selected rim vertices in q runs, deleting its induced edges isolates L=sum max(run length−2,0) interior vertices; the remaining vertices are all connected through the hub. Every spanning tree uses at least L deleted edges, and k≤2q+L supplies the induced-set rank inequality. For hub-free proper rim subsets the edge count is at most k−1, and the whole rim gives the binding bound. The spanning-tree description thus proves attainment for all n≥4. At equality every triangle inequality is tight. For the hub plus three consecutive rim vertices, the minimum tree count is one (exactly one isolated vertex upon deletion), and the summed inequalities are also tight. Subtracting a triangle equality gives c(p_{i+2})+c(r_{i+1})=1, forcing the claimed coordinates individually, without assuming symmetry. These connectivity arguments apply at n=4 as well. The frozen verification records 3,532 trees and 1,390,868 induced-set checks at n=4–8. The accompanying checker was inspected, not executed; those counts are corroboration, not the proof.

## originality

PASS

Within the inspected results and literature, no prior statement or specializable stronger formula covers the exact simple-wheel asymmetry together with global center rigidity. The standard tree-polytope inequality description is prior; the two binding support families, run estimate and equality analysis are the wheel-specific content.

## value

PASS

Wheels are a natural infinite family of simple graphic matroids with both a cycle orbit and a cut-adjacent spoke orbit. The exact affine invariant and the unique nonuniform center are useful comparison data for base polytope geometry. The result exhibits a strictly decreasing approach to 2 and proves why symmetry averaging alone is insufficient: it neither determines the relative orbit weights nor excludes nonsymmetric minimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
