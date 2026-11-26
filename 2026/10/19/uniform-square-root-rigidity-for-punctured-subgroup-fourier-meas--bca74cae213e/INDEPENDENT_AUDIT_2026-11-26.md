# Independent mathematical audit

## correctness

PASS

Independently reconstructed the character sums, Parseval expansion, and sharpness in RESULT.md:44–113. For a=μ(0), each dual coset of H⊥ other than H⊥ averages to a; the nontrivial characters of H⊥ sum to ma−1. Their disk bounds give d≥a and d≥|ma−1|/(m−1), hence d≥r and the two slopes in (1). The two-level law has signs +r off H⊥ and −r on its nontrivial members. Equality of an average with a boundary point of the disk forces every coefficient in that average to coincide, so inversion proves uniqueness. The signed sum in the Parseval cross term is (N−2m)a+1, real. Since N−2m=m(h−2)≥0 also when h=2, the lower bound on a gives the correct inequality direction and the linear coefficient reduces to 2r[(N−1)+(h−2)(m−1)]=2(h−1). Cauchy–Schwarz converts the normalized ℓ² estimate to the claimed TV bound. In the plane, 2(q−1)/(2q−1)≤1 and (q²−1)/(2q−1)²≤1/3 for all q≥2; the missing direction is supplied by a parallel translate disjoint from H. For odd q and v outside H, v and −v are distinct and some character sends v to a nonreal root of unity since characters separate points. The signed two-point perturbation is admissible for |t|≤μ_*(v), changes the coefficients purely in the imaginary direction, and gives d=√(r²+4s²t²), TV=|t|. This proves sharpness of the exponent, not of the prefactor. The radial laws aδ₀+(1−a)Unif(G∖H) give exact attainment of the lower slope for a∈[0,r] and the upper slope for a∈[r,1], with the permitted deficit ranges on those intervals. The Python support was inspected and not executed: its seeded examples test the radial profile, the magnitudes of the proposed optimal spectrum, and the TV bound, not the equality and sharpness arguments; the conclusions rest on the exact proof.

## originality

PASS

The baseline optimum and canonical weights are prior via fastest mixing. The supported distinct result is the explicit near-optimal TV modulus for arbitrary admissible measures on this support, its field-uniform version, and the demonstrated optimal exponent at each fixed odd field size. The inspected stability comparators do not imply this conjunction; priority evidence is bounded.

## value

PASS

The stability question is natural once the exact optimum on the fixed support is known: the explicit estimate controls every nearly optimal law, not merely the balanced or symmetric subclass. The relative-bias form remains informative as the field grows, and the odd-characteristic example identifies a genuine quadratic loss of bias along perturbations whose TV displacement is linear. Thus the half-exponent is a structural constraint rather than an artifact of an upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
