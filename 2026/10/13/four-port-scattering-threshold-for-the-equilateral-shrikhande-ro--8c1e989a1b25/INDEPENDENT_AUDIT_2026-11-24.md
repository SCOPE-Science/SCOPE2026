# Independent mathematical audit

## correctness

PASS

For s=sin(kℓ)≠0 the finite-edge endpoint derivative at u is k(f_v−cos(kℓ)f_u)/s. With ordered lead inclusion P, amplitudes a,b, and z=6cos(kℓ), Kirchhoff therefore reads (zI−A)f=isP(b−a), with Pᵀf=a+b. At the stated resolvent energies, define G=Pᵀ(zI−A)⁻¹P. This gives S=−(I+isG)(I−isG)⁻¹, where the denominator is invertible because G is real symmetric. The inverse map G=(is)⁻¹(S+I)(S−I)⁻¹ is defined since S−I=−2(I−isG)⁻¹. In particular the proof does not need G itself invertible or a separate Dirichlet nonresonance assumption at the contact set. Multiplication by zI−A, using A²=4I+2J and AJ=6J, proves the claimed resolvent expansion. Its ordered port block depends injectively on A[T] since its A[T] coefficient is 1/(z²−4), nonzero. Both graphs have an edge and a nonedge; common-neighbor counts give a triangle and an induced path, and union-of-neighborhood bounds give a one-edge triple and an independent triple. All labelings are admissible, so these exhaust equality through three ports. Any rook row is a K4; the Shrikhande neighborhood is a chordless six-cycle by Cayley differences and precludes a K4. At kℓ=π/3 the K4 resolvent has off-diagonal 1/15, whereas any four Shrikhande contacts have a pair with entry −2/15. Independent replay: python3 /workspace/replay/contact_profiles.py verifies exact strongly regular identities by bit masks, the integer-multiplied z=3 inverse, and exhausts the ordered adjacency profiles (support sizes 1,2,8 in both, then 54 versus 63 at four). The all-allowed-frequency result follows from the analytic reduction, not this finite check. No assertion at excluded energies or for every four-port layout.

## originality

PASS

Scattering via a boundary matrix, the strongly regular identities, and the clique contrast are known inputs. The supported distinct result is a sharp threshold for the sets of experimentally attainable ordered responses for this canonical pair, with an injective reduction to induced contact patterns throughout the stated frequency domain. The inspected literature and comparable records do not supply the induced-pattern classification of the scattering responses or the minimum-port theorem.

## value

PASS

Rook versus Shrikhande is a natural fixed test of how local probes distinguish a globally cospectral pair. The result establishes a sharp information limit for arbitrary layouts with fewer leads and an exact realizable four-lead design usable at a single frequency, rather than presenting only a numerical distinguishing example. The sets-of-responses distinction is explicitly narrower than identifying the graph for an arbitrary layout.

The dated certificate retains the supplied scientific assessment, sources and limitations.
