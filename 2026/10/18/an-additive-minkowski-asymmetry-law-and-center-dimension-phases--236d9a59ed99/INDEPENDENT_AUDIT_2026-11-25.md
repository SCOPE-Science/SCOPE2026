# Independent mathematical audit

## correctness

PASS

For a defining form f(x)≤b with min f=h, reflected containment at scale s is equivalent to f((s+1)c)≤sb+h. Independently checked the minima: a single nonzero row k supported on the first j columns at level A_k attains the coordinate and prefix-gap extrema, and zero attains the top-prefix minimum. With y=(s+1)c, use slack coordinates z_k=y_(k,m)−A_k and w_(i,j)=Y_(i,j)−Y_(i,j+1)−A_i. They give an invertible affine coordinate change and are nonnegative. The top inequalities become sum_(k≤i)z_k + sum_(j<m)w_(i,j) ≤ (s−m+1−r_i)A_i. Thus s≥m−1+ρ; z=w=0 attains it and yields the stated center, which is interior. At equality in the scale, exactly the z_k with k≤L and w_(i,j) with i∈T are forced to zero. Set all remaining slacks equal to one sufficiently small positive constant: the non-tight top inequalities have positive margins and the other floors, in columns j<m, have original slack (m−j)a_k>0. This proves no other affine equations and gives the center dimension. All members of the scaled feasible set are interior by positive floors, positive gaps and the strict top margin after rescaling. Uniform weights, n=1, and both examples at n=3,m=2 agree; the latter have r_3=3/2 and 103/100 respectively.

## originality

PASS

The multichain family itself is prior, including for m≥2. The distinct claim is its weighted asymmetry law and its tight-prefix classification of the full center locus. The closest unweighted center theorems cannot cover the whole family even up to affine equivalence: they have integer asymmetry, whereas the verified straight shape (n,m,a)=(2,2,(1,1)) has asymmetry 5/2.

## value

PASS

This is an exact invariant and center-locus classification of an established polytope family across continuous weight data. It replaces an optimization over vertices or centers by explicit prefix statistics and identifies ties that change the affine dimension even at the same optimal scale. That distinction is useful when the freedom in choosing a center matters, unlike merely applying a generic linear feasibility test to one example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
