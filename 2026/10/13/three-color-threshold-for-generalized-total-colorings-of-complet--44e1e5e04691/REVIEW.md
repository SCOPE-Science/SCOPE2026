# Independent mathematical audit

## correctness

PASS

Both the frozen coloring arguments and the narrowed theorem are mathematically correct. In K_{3,n} with n>=3, the shores have disjoint vertex palettes. With three colors, if both shores are monochromatic then all edges receive the remaining color and contain a four-cycle. Otherwise one shore uses two colors, of which one repeats, and the other uses one color; edges from two equally colored vertices to two vertices of the other shore are forced to the same third color, again a four-cycle. Fewer than three colors are impossible at an incident edge and its endpoints. With four colors, the opposite shore is colored 4, the smaller shore gets 1,2,3, and the respective full incident stars get 2,3,1. Every nonempty edge class is one star and every edge avoids both endpoint colors. For n>=5, two forests on n+3 vertices can cover at most 2(n+2)<3n edges, so a four-color construction cannot use disjoint edge and vertex palettes. The repaired result and verification notes state these scopes accurately.

## originality

PASS

PASS for the repaired claim only. The frozen finding's headline three-color threshold fails originality: the actual 2016 Theorem 6 sharpness example K_{3,3}-e forces failure for all m,n>=3 by subgraph inheritance, while Theorem 1 covers K_{2,n} from an acyclic three-coloring and stars are immediate. The narrowed exact value four for K_{3,n} retains the original nonplanar upper-bound contribution and explicitly credits prior support for the lower bound. The checked general acyclic-coloring theorem gives five from four acyclic vertex colors; the four-color upper bounds in the checked papers are for planar graphs. They do not give the uniform four-color upper bound for the nonplanar family.

## value

PASS

The repaired theorem computes the sharp invariant on the first complete-bipartite shore size excluded by the old three-color criterion. This is a natural nonplanar test family for the same four-color invariant studied in the planar literature. For n>=5, simply putting the vertex and edge colors in disjoint palettes cannot attain four; the explicit rotation of the three star colors solves that obstruction for every n. Thus the exact family value is useful independently of the already implied three-color threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
