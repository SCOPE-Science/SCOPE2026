# Independent mathematical audit

## correctness

PASS

For the literal model the partials have no common zero with a zero coordinate, and multiplying the three gradient equations in the torus would give 1=(-3)^3=3 in F5. In the dual chart Z=uX+vY the quartic coefficients are (u^3,1+3u^2v,3uv^2,u+v^3,v). For u=0, the X^3Y coefficient is 1 despite a zero X^4 coefficient, excluding a square. For u!=0, the monic quadratic factor has coefficients beta=B/(2A), gamma=(4AC-B^2)/(8A^2); matching the last two quartic coefficients gives the asserted P,Q. The independent exact resultant reproduction /workspace/reproductions/1.py (Python 3/SymPy) factors the nonzero-u eliminant and checks Frobenius irreducibility and both square equations at v=-u^26 in each residue field. There are 28 distinct candidates from degrees 1,3,6,6,6,6 with multiplicities one. The classical odd-characteristic bitangent count exhausts them, including any omitted chart; directly, X=0 restricts to Y^3 Z, and Y=kX in that chart has an XZ^3 term but no Z^4 term. The sole linear factor u+1 gives v=-1 and X+Y+Z=0. The reproduction evaluates beta^2-4gamma and its field Euler power as -1 on the linear factor and +1 on every other factor: all discriminants are nonzero, with the rational line's two contacts exchanged over F5 and each other pair split over its line field. Each split point individually needs its line field, since its tangent line descends with the point on a smooth curve. The orbit lengths give the stated extension counts and the common splitting extension F_(5^6), which contains F25 and is required by the degree-six line orbits. The reproduction certifies only this model and characteristic, not twists or other primes.

## originality

PASS

The supported distinct contribution is the exact arithmetic spectrum for this characteristic-five model together with the complete contact-field behavior. The model, named line, its contact quadratic and geometric symmetry are classical. Two distinct later-dated catalogue records cover the line calculation, one by an equivalent elimination and one as a row of a broader classification; neither is credited as a distinct line invariant of this record relative to that later content, and neither gives the contact-field classification. No earlier statement or direct implication of the complete arithmetic split was verified in the inspected sources.

## value

PASS

For this canonical smooth quartic, the arithmetic fields of theta/bitangent data and of their tangent points are natural separate invariants. The complete arithmetic census gives both the minimal field for the configuration and a specific descent distinction: the unique rational bitangent has no rational contact, but every nonrational line already splits its two contacts over its own field. The degree-three orbit is particularly not decided by knowing that everything is defined over F_(5^6) or by the geometry of the classical named line. This is more than confirming the classical line or recomputing a geometric orbit size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
