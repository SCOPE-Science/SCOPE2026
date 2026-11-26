# Independent mathematical audit

## correctness

PASS

For an old primorial L and new prime q, lift each old unit by a+tL for 0≤t<q. The discarded lifts are exactly qb with b an old unit, since q is coprime to L. This gives U_(Lq)(X)=U_L(X)Σ_t X^(tL)−U_L(X^q). If q≡1 (mod mr), the noninitial summands split in the quotient ring into (q−1)/r identical blocks of r summands, and m divides the number of blocks. The initial summand is 1 and X^q=X, so the two terms cancel, regardless of gcd(r,L). The substitution X↦X^s preserves the quotient ideal even when gcd(s,r)>1, propagating the zero to later stages. Dirichlet applies to the reduced class 1; m=1 is trivial, and q≥3 when m>1, so a nonempty preceding primorial is available. For odd m the order of 2 allows an evaluation homomorphism; the confirmed binary invariant removes 2 and adds 2^(P_k+1). Modulo 17 the order is 8, 137 is the 33rd prime, and multiplication of P_k by any odd prime congruent to 3 modulo 4 toggles P_k modulo 8 between 2 and 6. Infinitely many toggles give both stated state residues infinitely often. The independent replay compared direct and inclusion-exclusion count vectors in 96 bounded cases, and checked p_33 and the two endpoint expressions 7 and 6 after 137 and 139. These corroborate, but do not replace, the proof.

## originality

PASS

The earlier state encoding and the general primorial-wheel setup are established work. The inspected recurrence paper's modular criterion describes a normalized state and detects a prime gap; it does not give the unnormalized eventual odd-modulus residues. The wheel-gap recurrence tracks a different statistic. The supported distinct result is full coordinatewise annihilation, including incompatible-length cases r not dividing P_k, with persistence and its odd-state application. This is a best-of-knowledge comparison, not a priority certification.

## value

PASS

The theorem supplies an exact invariant of all sampled residue coordinates of a natural sieve object, not just Euler's totient or the CRT-divisor case. It gives a simple residue law for otherwise enormous prime-generating states without computing the state itself, and an explicit fixed odd modulus where eventual support of size two does not mean stabilization. This is a modest but useful arithmetic application of the wheel transition, with no claim to a sharp least threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
