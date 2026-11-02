# Independent mathematical audit

## correctness

PASS

PASS: Fourier transform over a splitting field is invertible because p=char F_q does not divide n. Bilinear product yields exact idempotence equations y_r=y_(2r)y_(-r), and descent condition y_(qr)=y_r^q. On each H_t orbit nonzero coordinate forces whole orbit nonzero; applying at r and -r yields y_(2r)y_(-2r)=1, hence y_(-r)=y_r^-1 and y_(2r)=y_r². Orbit consistency gives cyclic root group μ_N_t (with t|N_t and the rho map well-defined). Frobenius rotates H_t cosets in cycles e_t and forces z^(q^e)=z^rho(h), leaving exactly gcd(N_t,q^e-a_t) nonzero choices plus zero. These roots lie in requisite splitting field by group-order argument. One binary zero-frequency idempotent gives prefactor 2. Independently exhaustively computed coefficient-basis idempotents over F2 at n=3,5,9, obtaining 8,12,80; source check_idempotents.py and check_prime_census.c were inspected. Finite data not substituted for general Fourier proof.

## originality

PASS

On the inspected primary sources and independent comparison, the specified new exact evaluation/classification is not supplied by a stronger known theorem; scope and residual priority limitations are stated explicitly. The Fourier identity is prior work, and the present count is its finite-field orbit solution with Galois compatibility. Special n=3 count8 in characteristic not3 is previously covered. Deriving the new all-field arithmetic product from a characteristic-zero identity needs genuinely additional H-orbit consistency and Frobenius descent; prior small counts are covered without implying the arbitrary-n formula.

## value

PASS

PASS: An all-odd-n, all-coprime-finite-field exact and arithmetic-sensitive idempotent census/parametrization for a natural nonassociative algebra, with composite n and extension fields. Existing Fourier multiplication identity alone does not determine cyclic root counts or finite-field descent. Examples n11 q2=68 vs q3=24 show nontrivial field dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
