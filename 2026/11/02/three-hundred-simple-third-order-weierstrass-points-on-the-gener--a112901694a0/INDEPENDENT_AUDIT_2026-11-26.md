# Independent mathematical audit

## correctness

PASS

I checked the adjunction trivialization dx/f_y and the determinant-one signed permutation action: the q-canonical Wronskians have weights in O_C(27) and O_C(75), are invariant, and vanish on each simple fixed axis intersection because the lift acts as −1 on its representative. B is itself invariant: the permutation sign in the difference product cancels the sign on XYZ. Dividing by the simple axis divisor and taking invariant lifts by averaging leaves symmetric forms in the squares, giving the residual polynomials in V/U³ of degrees at most 3 and 11. At U=T=0 the squared coordinate ratios are the three distinct cube roots of unity; all coordinates are nonzero, dU and dT are independent there, and the eight points give poles of order three. Thus V/U³ is the degree-24 group quotient. The axis fibres, computed by setting a coordinate to zero or two coordinate squares equal, and the pole fibre account for all ramification by Riemann–Hurwitz. The independent run of `python3 /workspace/review-evidence/ciani_replay.py` used Newton lifting, rational determinants reduced mod 1009, and Lagrange interpolation, and returned the frozen P2 and P3 coefficients at all 36 eligible distinct rational quotient coordinates, with gcds equal to 1 and nonzero P3 values 879,682,112 at the finite branch values (leading coefficient 498). The specialization lifts: choose distinct interpolation points mod 1009 with f_y, B and U units, lift their y-coordinates by Hensel with x fixed and a near 1, and interpolate with unit Vandermonde; all polynomial nonvanishing conditions detected by the replay therefore hold on a nonempty characteristic-zero open set. This proves 36 simple axis points plus 11 unramified 24-point fibres. At each such axis point the tangent contact is even by the local involution (the axis is transverse), so a flex would be a hyperflex. A hyperflex gives a cubic with contact 12, already incompatible with a simple third-order zero, so the forced second-order zeros on those axes are sextactic. The coprime residual polynomials exclude every nonaxis third-order zero from the second-order divisor; rank ten then gives the claimed cubic contact classification. No conclusion is drawn for all smooth parameters.

## originality

PASS

The supported distinct result is the generic symmetric-pencil third-canonical profile, its reducedness and its second-order overlap, not the symmetry-forced axis support, the general plane-quartic count or the known special-member divisors. The strongest same-pencil computation, Nawara at a=3, is materially different and cannot witness the required open conditions. No inspected equivalent generic claim was found.

## value

PASS

For this natural highly symmetric quartic pencil, the ambient generic theorem does not answer whether third-order weights collide. The exact orbit profile, reducedness and second-order overlap are structural data. They distinguish the generic pencil from a studied smooth special member with weight-five hyperflexes and from generic quartics without this symmetry. The quotient calculation supplies a reusable exact test instead of just a count at an isolated parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
