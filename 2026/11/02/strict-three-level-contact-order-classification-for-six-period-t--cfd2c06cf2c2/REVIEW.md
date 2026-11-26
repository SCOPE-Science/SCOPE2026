# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 15–80 and the supplied checker.py by inspection. The Jacobians are the stated symmetric X,Y. Cyclic rotation preserves the characteristic polynomial by det(zI−AB)=det(zI−BA), including the singular case α=β, and reversal transposes the product. Independent exact enumeration of all 20 balanced words partitions them into the 6,12,2 dihedral classes with representative products G=X³Y³, M=X²YXY², A=(XY)³. Symbolic multiplication verifies the two differences p_G−p_M=−4u²v⁴z(z−K_GM), p_M−p_A=−2u²v⁴z(z−K_MA), and the strictly positive gaps tr(M)/3−K_GM=u²(u²v²+8v⁴/3), tr(A)/3−K_MA=u²(u²v²+7v⁴/2). Perron radii of the nonnegative products are positive real roots and bound trace/3 from above, so the polynomial differences are strictly negative at ρ(M) and ρ(A). A monic real characteristic polynomial cannot be negative at a point at or above its spectral radius, proving both strict steps for the full domain, including u≤v. At u=4/5,v=149/500, q=(5/4,3/2,1) yields q−XYq=(899/250000,9/2500,3/1250)>0; hence ρ(A)<1. Independent exact arithmetic gives det(I−M)=−667551319210915426403604273201/931322574615478515625000000000000<0 and thus ρ(M),ρ(G)>1. The independent SymPy replay is in /workspace/branches/a18cd6e7-1956-46ac-afad-59381828cef0/independent_check.py, lines 25–82; uploaded checker was not run. The conclusions concern disease-free mean-field linearization, not persistence in a stochastic chain.

## originality

PASS

Existing propagator criteria and the exact alternating model are antecedents, and a same-day analogous three-level ordering is real structural overlap. The inspected results do not cover this complete strict three-class comparison of six balanced steps in the two-edge path matrices for the entire rate domain, or the threshold split within that comparison. Best-of-knowledge judgment, not priority certification.

## value

PASS

This is a motivated complete classification on the three-vertex path with two competing edges, not an isolated recomputation of an alternating multiplier. For identical per-edge contact counts it certifies three distinct schedule classes across both positive-definite and indefinite factor regimes, and gives an exact parameter witness where schedule alone changes the mean-field invasion verdict. It does not extrapolate to bigger graphs, arbitrary word lengths, heterogeneous edges or stochastic persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
