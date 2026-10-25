# Independent mathematical audit

## correctness

PASS

Using Ferreira–Speziali Theorem 4.4, all q>=5 Sziklai-optimal degree-(q-1) curves with no rational line component are projectively diagonal with three nonzero coefficients summing to zero. Their rational points are exactly (q-1)^2 torus points. Differentiating gives the Gauss bijection to every dual-torus rational line; counting solutions of Ax+By+z=0 with coefficients nonzero yields multiplicities 0×3,(q−2)×(q−1)^2,(q−1)×3(q−1). In F5, coefficient-support cases of the restriction of X4+Y4+3Z4 to a line exhaust 16 ordinary bitangents and 12 hyperflexes; root conditions u4=1,v4=3 and s4=4 or 2 yield exact Frobenius permutation 2^2 4^6. The quartic is smooth because its coordinate derivatives cannot vanish projectively. Source verify.py constructs F_625 and exact Frobenius actions and verify_prime_fields.py checks p=5,7,11,13; logs corroborate but do not prove the q-general implication.

## originality

PASS

Best-of-knowledge statement-and-implication search and material inspection distinguish previously established premises and general frameworks from the additional exact theorem; remaining priority risks are explicit rather than treated as negative proof.

## value

PASS

The two independent natural extrema—maximal Fq rational points at degree q−1 and maximal tangent-line coverage—have a sharp structural incompatibility at every q>=5 with an exact pointwise incidence law. The arithmetic Frobenius cycle is the standard odd-theta Galois invariant of a smooth quartic and determines its bitangent splitting field. Thus both the general incidence obstruction and the special arithmetic distribution answer precise motivated questions, without claiming a new curve classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
