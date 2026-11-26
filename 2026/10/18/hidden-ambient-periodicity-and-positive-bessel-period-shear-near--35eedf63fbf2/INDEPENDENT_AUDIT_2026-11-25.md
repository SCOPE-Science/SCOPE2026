# Independent mathematical audit

## correctness

PASS

Differentiating F=x²+z²-1 gives 2czF, so H=e^(-cx/a)F is conserved by xdot=2az. The same xdot yields the integrating-factor identity for J everywhere without dividing by z; J_y=e^(-Bx)>0 and the planar gradient of H does not vanish on the circle. For the local geometry and period derivative, independently use x=r cos u, z=-r sin u. At H=0 the radial implicit function has nonzero derivative, so for every fixed c there is a smooth periodic r=r(u,h) near 1 for sufficiently small |h|. This produces an annular family of full levels uniform in the angular variable; J determines y uniquely for every real J. The angular speed is 2a-c h exp((c/a)r cos u)cos u/r, uniformly positive on a sufficiently small annulus. The projection must make a full turn for a return, and the axial variable returns at that same time. Differentiating the integral of inverse angular speed gives T(0)=pi/a and T'(0)=c/(4a²) times the circular integral of exp((c/a)cos u)cos u, exactly the stated Bessel expression. Pairing cos u with -cos u proves the sign, and c=0 makes the speed exactly constant. Phase and the two integrals give the local flow as a phase translation with frequency depending only on h: its fixed-period derivative is triangular with all diagonal entries one but with a nonzero shear entry when T' is nonzero. Independent replay `python /workspace/branches/independent_audit_replay.py` compares the polar-period finite difference and the Bessel integral at c<0, c>0, and c=0. This only corroborates the analytic local result; neither global periodicity nor a statement uniform in parameters follows.

## originality

PASS

The polynomial normal form, its cofactor, on-cylinder periodicity, and the isochronous circular case are credited to the literature. In the checked sources, ambient periodicity with nonzero cofactor, the explicit real first-integral pair on this slice, and the physical-time period shear are distinct. Standard integrating factors and period-perturbation methods are not claimed as new.

## value

PASS

For an invariant cylinder with a nonzero algebraic cofactor one should not infer an ambient period annulus or original-time isochrony from the flow restricted to the cylinder. The exact integrals resolve off-cylinder closure and the derivative quantifies the shear that persists despite all multipliers being one. This addresses a specific question left open by the restricted result, on a motivated constant angular coefficient slice, without suggesting that nearby normal-form parameters retain integrability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
