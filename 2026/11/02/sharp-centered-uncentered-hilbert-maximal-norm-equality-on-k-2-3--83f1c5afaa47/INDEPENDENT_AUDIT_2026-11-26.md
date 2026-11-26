# Independent mathematical audit

## correctness

PASS

Every uncentered selector chooses a containing ball separately at each vertex; taking coordinatewise maxima on nonnegative data commutes with maximizing the squared output norm over selectors. Moreover the top matrix norm of a nonnegative selector can be attained on a nonnegative right vector by taking absolute values. I separately enumerated the balls from the explicit bipartition (five singletons, five opposite-part closed neighborhoods, whole set) and formed all 4500 legal row products. With T=60A, an independent rational Schur-complement elimination checked that all five pivots of 6156I−TᵀT were positive for every selector except the stated one, with smallest pivot 448884/1139; this uses exact rational elimination rather than the frozen Bareiss code. To replay: construct incidence rows Tᵢⱼ=60/|Sᵢ| for j∈Sᵢ, enumerate their Cartesian product, exclude the displayed A₀, and iterate Mᵢⱼ←Mᵢⱼ−MᵢₖMₖⱼ/Mₖₖ on the trailing block, testing every pivot. This gives a strict squared norm bound 171/100 below (8+sqrt(55))/9. The exceptional Gram matrix acts by 1 on the A antisymmetric direction and 1/9 on the B mean-zero plane; the two part-constant coordinates have matrix [[5/3,1/3],[2/9,1/9]], hence characteristic equation 9λ²−16λ+1=0 and simple positive top ray with c=(sqrt(55)−7)/3. At that ray the winning singleton and size-three averages are both centered and strictly beat the alternatives. Since the centered operator is pointwise bounded by the uncentered one, this gives equality of their norms; only the strict winning selector and its top eigenspace can give equality, and independent coordinate signs are immaterial.

## originality

PASS

Best-of-knowledge pass for global optimality of the candidate at K₂,₃ for the uncentered operator, the resulting exact centered/uncentered equality, and full equality classification. The strongest earlier catalogue results already give the exact candidate norm and two-level ray after substituting m=2,n=3, but only prove that they are globally optimal for a sufficiently large part and for the centered operator. Their lower-bound selector, which applies here, is not the contribution being credited. The retrieved literature gives exact Hilbert results for neighboring graph families, not the required upper bound or rigidity here.

## value

PASS

K₂,₃ is the first irregular two-connected bipartite graph by vertex count, so the graph is selected by a structural cutoff rather than chosen arbitrarily for an enumeration. There are strictly more allowed uncentered local averages, yet the global Hilbert norm does not increase, and equality still forces a single modulus ray. This exact comparison at the first irregular case is an independently useful benchmark between the star, complete-graph, and eventual unbalanced bipartite results. The meaningful new fact is the strict global optimization over all uncentered choices, not computing a two-by-two eigenvalue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
