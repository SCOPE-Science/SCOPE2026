# Independent mathematical audit

## correctness

PASS

Euclidean projection reduces to minimizing the squared error over an output vector length r∈[0,t], t=||u||₂, with scalar outputs max(x_i,r). On an exterior chart with k active scalars, dr=(sum_active dx_i+v·du)/(k+1), v=u/t; the vector Jacobian block is αI+[(k+1)^−1−α]vvᵀ, α=r/t. The scalar row maximum (1+√q)/2 comes from k=1 and equal coordinate magnitudes in v. Vector absolute row sums are convex in α. At α=0 they are |v_j| times the scalar row norm, strictly below the scalar maximum for q≥2 (equality there would need both |v_j|=1 and equal magnitudes across q coordinates). At α=1 the row sum is 1+k/(k+1) times the increment a(1−a+sum_{i≠j}|v_i|), with the 1 outside the product. Equal magnitudes of the other coordinates maximize the latter at fixed a=|v_j|; k=p and α approaching one give the second sharp branch. All interior chart parameters used by the witnesses are realizable. For the global bound the finitely many switching walls have ambient measure zero: at fixed x, each wall confines t to one of finitely many specified radii. Almost every parallel translate of a segment meets those walls in a null set of segment parameters, so absolute continuity and passage to the limit give the claimed global bound. The phase refers to which row-type supremum gives the norm; in the vector-dominant regime the optimizing vector row is approached at a switch, not attained as a smooth-chart row. For q=1 both increments vanish and an identity chart attains one. For q≥2 the derivative of the H_q objective is strictly decreasing, and its zero lies between 1/2 and 1/√2; the second derivative has size comparable to √q there, giving a_q−1/√2=O(q^−1/2) and the stated phase asymptotic. Checked H_6=4/3 at a=2/3 directly, hence Λ_(2,6)=17/9; independent scalar maximization gives p_*(13)≈2.029335. Inspected the finite script without executing it.

## originality

PASS

The Euclidean projector's radius equation is established prior work, and p=1 is background rather than part of the distinct contribution. The supported distinct claim is the sharp coordinatewise optimization for the unordered extended cone with multiple scalar coordinates and its row-type phase. A later-dated ordered-cone record has the identical numerical modulus and overlapping sharpness mechanisms, with a reduction for the numerical modulus via sorting chambers. This is significant formula-level coverage, but not evidence of earlier priority for the ordered result, and it does not present the audited unordered-cone phase classification and asymptotic. The identified pre-existing projection and order-theoretic sources do not supply the sharp row optimization.

## value

PASS

The coordinate maximum norm models simultaneous componentwise input errors, and Euclidean nonexpansivity gives only a coarse bound in that norm. The exact invariant shows when this projection can amplify such errors and which type of output is most sensitive as the two dimensions vary. The sharp phase and its √q scale provide information not available from the underlying scalar projection algorithm alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
