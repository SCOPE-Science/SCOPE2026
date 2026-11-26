# Independent mathematical audit

## correctness

PASS

For h=mn/2, the graph-state coefficient array has entries p^{-h} ω^{uᵀDv}. Grouping u by the image of Dᵀ gives p^r orthogonal Fourier characters on B and orthogonal sums on A, each sum of p^{h−r} computational basis states. This gives the stated flat Schmidt spectrum and entropy. The full adjacency has rank 2r. The frozen local-algebra proof checks out: τ=x+x^{-1}+y+y^{-1} factors as (x+y)(1+xy)/(xy). After separating p-parts P,Q and prime-to-p parts M,N, there are 2gcd(M,N)−4 one-branch points of length min(P,Q), plus two crossings. At a crossing the module with s^P=0 is free on 1,t by the monic relation t²=s²(1+t)/(1+s). It has t^{2P}=0; for Q>P, Q≥3P makes t^Q redundant. For P=Q the additionally imposed t^P generates a one-dimensional socle ideal, as it is a unit times s^{P−1}t. The same reasoning includes P=Q=1 and symmetry covers Q<P. An independent proof of the all-size nullity avoids the local computation: up to a unit shift the adjacency is (I+S)(I+H), where S,H are the (1,−1) and (1,1) shifts. Conjugation by multiplication by (−1)^i gives A=I−S and B=I−H. Each shift has g orbits, labeled by i+j and i−j modulo g respectively. Nullity of AB equals g+dim(ker A ∩ im B). On ker A, testing im B amounts to pairing with the orbit indicators in ker Bᵀ. Two labeled orbits have intersection 0 for different parity and 2mn/g² for the same parity: the map (i,j)↦(i+j,i−j) mod g has a two-element kernel on residues and image the equal-parity pairs. Hence the test matrix has two constant blocks, of total rank 2 when p∤2mn/g² and rank 0 otherwise. For odd p this is precisely the equal-valuation dichotomy. Nullity of the full adjacency is 2g−2δ, yielding all stated example ranks and entropies without any large-size extrapolation.

## originality

PASS

The supported distinct content is the closed odd-prime toroidal adjacency nullity, equivalently exact checkerboard entanglement, and its one-dit valuation switch. The same-graph binary formula, the standard graph-state cut-rank reduction and characteristic-p convolution machinery are not new. No verified checked source covers the odd-prime switch for this graph and these side-length hypotheses, including inseparable periods. This is a bounded comparative judgment, not a priority certificate.

## value

PASS

Checkerboard entropy is a natural invariant of the periodic grid state. The formula isolates the exact departure from the generic deficit at fixed geometry, distinguishes equal nonzero valuations from unequal ones, and explains why a semisimple character count is insufficient. It settles a complete arithmetic classification for this cut rather than a tabulation of examples or a repackaging of the usual cut-rank identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
