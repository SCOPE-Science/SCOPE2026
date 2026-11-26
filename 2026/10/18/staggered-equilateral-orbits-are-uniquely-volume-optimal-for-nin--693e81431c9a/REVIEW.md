# Independent mathematical audit

## correctness

PASS

For the exact unnormalized linear map on Herm_3, the angular Fourier transform at each orbit has real row norms 1/sqrt(3), 1/sqrt(6), 1/sqrt(6) with orthogonal rows, giving the claimed sqrt(3)/18 Jacobian. The diagonal block has determinant Delta_2/2, and the complex off-diagonal block has determinant of modulus (r1 r2 r3)/2 times |−Au1+Bu2−Cu3|. Its modulus squares in real coordinates, with an additional factor 2^-3 from the Hilbert–Schmidt coordinates. Combining the Gaussian and Fourier factors gives 81 sqrt(3)/8. Factoring B−A−C gives the strictly positive Vandermonde in the radii; both triangle-inequality equality conditions are exact since A,B,C>0. At the maximizing phases, the radial log-objective has Hessian at most −6I on the convex ordered cone. The Gaussian and the vanishing wall factors give an interior maximum, strict concavity gives uniqueness, and differentiating in the scale direction gives 6 sum(r_i^2)=18. Independent replay: cd /workspace && python3 branches/53273f2a-7a63-45a2-a594-a07aa39a8daa/reproduce_radii_volume.py. It gives radii (0.4195865012772835,0.9258607660691042,1.4024011586560459), squared sum 3, and direct volume 0.0082399703668547333; this checks the decimals, not global optimality. Frozen support was inspected, not executed. Statistical interpretation is the fixed-noise linear-design one (e.g. independent Gaussian additive noise with common variance), not a general noise/conditioning theorem.

## originality

PASS

The strongest inspected indexed design is close at the level of nine points on three triangles and angular determinant optimization, but answers a different problem: it evaluates analytic Hardy polynomials and repeats an inner radius, whereas this theorem evaluates a real Hermitian Gaussian intensity lift with three distinct positive radii. Its phase law and determinant do not transfer. None of the actual inspected statements gives the frozen factorization, angle equalities, and radial uniqueness for this measurement map. Pass is for that scoped result, not three-orbit designs or information-complete tomography generally, and not exhaustive historical priority.

## value

PASS

A saturated equally weighted nine-measurement design on the full Hermitian space is a natural constrained tomography problem. The determinant quantifies how choices of offsets affect the linear measurement volume, even though all offsets are informationally complete, and gives both sharp orientation requirements and a reproducible unique radial optimum. This is useful within the stated three-orbit family without claiming optimal design over arbitrary placements or noise models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
