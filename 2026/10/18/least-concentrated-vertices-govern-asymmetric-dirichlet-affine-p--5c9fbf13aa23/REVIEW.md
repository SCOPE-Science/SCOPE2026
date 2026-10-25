# Independent mathematical audit

## correctness

PASS

PASS. Orthogonal projection of Dirichlet L² onto span of barycentric affine coordinates has Gram G_ij=(alpha_i alpha_j+delta_ij alpha_i)/[A(A+1)] and inverse diagonal A(A+1)/alpha_i minus rank-one A, giving kernel K(x,y)=A(A+1)sum_i x_i y_i/alpha_i-A. The L∞ and L¹ norms both equal max_x E|K(x,Y)| by symmetry and kernel duality; strict nonvertex inequality follows from mixed signs of K(e_i,Y), K(e_j,Y) on an open positive-measure region. The vertex integral uses beta marginal Y_i~Beta(a,A-a) and cutoff a/(A+1), yielding the stated F_A(a). For a<b<A, independent gamma splitting gives E[Z_a|Y_b]=Z_b and strict Jensen because the conditional split has mass on both sides of the sign threshold. Thus F_A strictly decreases and only least-concentrated vertices maximize; equal alpha uniquely minimizes fixed-total norm. As a↓0, Y_a/a→0 in probability and bounded negative part yields nonattained sup 1+2A. For a=Ap fixed proportions, beta CLT plus uniform integrability of |Z_a|/sqrt A gives sqrt(2/pi)*sqrt((1-p)/p). Independently evaluated incomplete beta integrals for A=8: alpha_min=1 gives 6.0153981763, balanced 8/3 gives 3.48181400685; inspected exact Gram and beta numerical checker covering 241 cases. Boundaries require m>=2, alpha_i>0, fixed proportions for A→∞, not higher degree.

## originality

PASS

Best-of-knowledge PASS for asymmetric sharp L¹/L∞ norm, unique worst-vertex characterization, total-concentration minimax and sharp Gaussian-growth coefficient. Known Dirichlet degree-one kernel and uniform-simplex equal-shape case are explicitly treated as covered inputs. The strict gamma-splitting convex-order comparison and its norm extremizers are the distinct extension.

## value

PASS

PASS. Projection stability in L∞ and L¹ governs error amplification for affine least-squares on simplices, a natural numerical-approximation invariant. Exact determination for all asymmetric concentration vectors, rigorous unique balancing for prescribed total concentration, and a sharp high-concentration growth law characterize the effect of least-concentrated vertices and are not a mere recomputation of the known degree-one kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
