# Independent mathematical audit

## correctness

PASS

Direct substitution in the specified stages gives aI+ρpJ and aI+ρuJ+ρ²vJ², with u=p²/z, v=p(1−p/z), u+v=p and a+p=1. These coefficients are nonnegative for z>0, and their row and column sums are bounded by a+ρp and a+ρu+ρ²v, respectively, both strictly below 1. The Euclidean norm estimate follows and the dissipativity bound follows from ||J||₂≤1, including d=1 (the scalar, normal boundary case). With h>0 and k fixed, the exact power is exp(−kz) times a polynomial in z and J, while the two numerical powers converge to (ρJ)^k and (ρ²J²)^k. Each surviving shift has norm one. At ceil(d/2)≤k<d, an a-free ETD2 monomial with t linear factors in J has degree 2k−t and order z^(−t), so the first surviving degree is d−1 with t=m=2k−d+1, 1≤m≤k. After scaling by z^m, the sole leading shift is binom(k,m)ρ^(d−1)J^(d−1); terms containing a and the exact power are exponentially small. When k≥d all a-free monomials vanish and the stated algebraic limit is not asserted. At z→0, p=z−z²/2+O(z³), u=z−z²+O(z³), and v=z²/2+O(z³), giving the stated local orders against the exact exponential. Inspected the frozen tests as corroboration, without executing the verifier.

## originality

PASS

The diagonal Schur split, qualitative splitting errors, and the ETD2 scheme predate the record. The supported distinct result is the exact fixed-positive-step, fixed-iterate defect and sharp post-cutoff ETD2 residue for the strongly dissipative repeated-diagonal Jordan family. The closest inspected method and theory do not supply the dimension/iterate thresholds with these norm constants.

## value

PASS

This exact test family separates positivity and strict Euclidean contraction from correct elimination of fast dynamics, in a diagonal split used for exponential methods. The differing depth thresholds and the sharp algebraic residual despite a zero limiting error give a practical mathematical distinction that a scalar stability or conventional local-order check would miss. The result is appropriately limited to two steppers, fixed iterates, and this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
