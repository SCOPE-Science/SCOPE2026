# Independent mathematical audit

## correctness

PASS

The source minimal H-description has x_i≥1 and upper Σ_{i∈I}x_i≤k[a+b(n−(k+1)/2)] for |I|=k; only k=n−1 is redundant if a=1. Averaging any radius-r center under S_n gives a diagonal radius-r center t1, valid because every offset support inequality is convex. At such center lower clearance t−1 increases and each upper clearance (U_k−kt)/√k decreases. Their intersection yields r_k=[√k/(√k+1)](A+b[n−(k+1)/2]), A=a−1. Let y=√k and C=A+b(n−1/2); derivative of r(y)=y(C−by²/2)/(y+1) has sign C−(b/2)y²(2y+3), strictly decreasing on y>0. Thus r(y) first increases then decreases and minimum on [1,√n] occurs at y=1 or √n: min{(A+b(n−1))/2, [√n/(√n+1)](A+b(n−1)/2)}. Their comparison is A=b(√n+1), giving exactly the two claimed facet contact phases; intermediate k strictly above. In the coordinate phase active x_i≥1+r and x_i≤a+b(n−1)−r force the unique midpoint; in total-sum phase n lower bound inequalities plus full-sum bound force x_i=1+r coordinatewise. Equal endpoints give both families; rational √n for integer A,b forces n a square. n=2,a=1 redundant k=1 causes no problem since total-sum phase strictly controls. Finite LP checks only supplement this symbolic all-parameter proof.

## originality

PASS

Hanada et al. determine this family’s vertices, all upper cardinality-facets and volume; their primary PDF Proposition 3.6 supplies the facet input but contains no inradius or Chebyshev-center result. Bayer et al. extend to arbitrary parking-function parameter vectors and identify polymatroids/generalized permutahedra (Theorems 2.3,4.3), but their full text focuses on combinatorial/circuit diameters, not Euclidean inballs. The new statement is metric and realization-sensitive; an integral-equivalence theorem does not preserve Euclidean radius. Nearby Resultary findings compute CIRCUMSPHERES or Löwner ellipsoids of parking polytopes, distinct outer optimization rather than the claimed insphere. The one-peak clearance collapse and sharp tangency phase have not been found in these source results.

## value

PASS

This computes a natural intrinsic metric invariant, the Euclidean inball, of a well-studied classical and generalized parking-function polytope, with a sharp analytic phase transition and a discrete change in touching facet orbits. The fact that exponentially many subset facets reduce to only endpoint orbit competitors in all dimensions is an explanatory geometric structure, not an arbitrary small-instance evaluation. Its realization sensitivity and exact contact classification would be reusable when comparing metric realizations or designing polyhedral sphere bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
