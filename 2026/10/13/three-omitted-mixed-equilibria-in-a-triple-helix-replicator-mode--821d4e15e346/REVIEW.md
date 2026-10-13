# Review

## Correctness
PASS. The source equations reduce at baseline to \(\dot x=x(1-x)(41y+32z-40)\), \(\dot y=y(1-y)(37x+28z-34)\), and \(\dot z=z(1-z)(26-32x-28y)\). Exact case splitting on whether each coordinate is boundary or interior gives only the eight corners, the two face points \((34/37,40/41,0)\) and \((6/37,8/41,1)\), and the fully mixed point \((517/1248,71/156,3329/4992)\). The general interior formula follows from a nonsingular \(3\times3\) linear system. At any admissible fully mixed point, the Jacobian has zero trace and strictly negative determinant, which forces one stable and two unstable spectral directions. The bundled exact checker reproduces these identities.

## Originality
PASS. The motivating 2026 article prints the three affine replicator equations, states that there are eight equilibrium points, and tabulates only the corners; searches within its full text found no mixed- or interior-equilibrium discussion. Exact-form web searches for the three baseline rational coordinates and the source-specific coefficient combinations found no prior statement of this correction. Published-record semantic searches using the DOI, title, aliases such as “interior equilibrium” and “mixed equilibrium,” and the exact baseline fractions returned no matching or stronger result. The 2021 Su–Shi–Zhu–Xin paper does discuss mixed equilibria in a related collaborative-innovation game, but under fixed government strategies and with different payoff equations; it does not imply the 2026 system's omitted points or the unstable-index theorem. The 2025 Peng–Wang–Zhao article studies a different tripartite industrial-internet game and likewise does not dominate the claim.

## Value
PASS. The correction changes the equilibrium inventory of the model used to interpret collaborative-innovation resilience at the paper's baseline parameters. The omitted face saddles have codimension-one local stable manifolds and the omitted fully mixed saddle has a one-dimensional local stable manifold, so these are not decorative algebraic roots: they are local threshold states relevant to how nearby strategy mixtures separate and evolve. The general determinant/trace argument adds a structural conclusion for every admissible fully mixed state in this model family, beyond a one-off numerical correction.

## Closest literature and limitations
The closest directly relevant source is the motivating 2026 article itself, because the claim is a correction and completion of its Eq. (3.13). Su et al. (2021) is methodologically close and explicitly recognizes mixed equilibria in a related collaboration game. Peng et al. (2025) is a recent tripartite evolutionary-game comparison. None contains the source-specific eleven-point baseline census or the universal unstable-index-two statement. The analysis does not claim a complete arbitrary-parameter boundary classification or a global description of basin separatrices.

Self-review: passed. Independent audit: not yet performed.
