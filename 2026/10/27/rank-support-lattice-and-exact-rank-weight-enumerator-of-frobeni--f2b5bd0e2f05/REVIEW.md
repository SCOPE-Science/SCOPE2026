# Independent mathematical audit

## correctness

PASS

The splitting condition implies p does not divide |A| and d divides m. Covariance under Frobenius and Fourier inversion identify the spectra with base-field functions; an orbit of length ℓ_i contributes a free seed in F_{q^{ℓ_i}} and its entire conjugate span. The normal basis realizes Frobenius as a cyclic shift of d independent vectors, so the ambient module is F_q[T]/(T^d−1) even when p divides d. Every invariant subspace is the ideal of (T^d−1)/f in that module, equivalently W_f of dimension deg f. The sum of seed spans is the ideal for the lcm of their annihilators. Independently, containment of the whole support in W_f is equivalent to each seed lying in the intersection W_f∩W_{T^{ℓ_i}−1}=W_{gcd(f,T^{ℓ_i}−1)}. Thus the cumulative count is q^{Σ_i deg gcd(f,T^{ℓ_i}−1)}. It factors over primary exponents; consecutive differences within each chain give the stated exact-support factors, including the one zero choice at exponent zero. The character of full exponent N has orbit length d, so the factors are positive for all exponent choices. The top-chain difference divided by its cumulative count is 1−q^{-deg(P)t_P}. The trivial group has d=1 and one seed, giving 1+(q−1)z. A separate small check at q=2, A=C_3 has orbit lengths 1 and 2 and a single repeated factor (T+1)^2; the cumulative counts 1,4,8 give 1+3z+4z² and full-rank probability 1/2, matching the captured output.

## originality

PASS

The contribution is the exact field-value rank-support census of the complete Fourier code, a modest synthesis of Fourier orbit descent and finite-field module counts. Neither the orbit seed description, the cyclic Frobenius lattice in itself, nor the single-seed q-order/totient law is new. The claimed joint statistic counts heterogeneous orbit seeds by the subspace generated together, rather than by separate span dimensions or nonzero positions. The inspected sources do not give this joint census or a stronger such census with the same heterogeneous subfield constraints.

## value

PASS

The objects and weight arise naturally from complete base-field Fourier spectra and the rank metric, and positional statistics cannot answer the rank question. The result gives which field-value subspaces are possible, the number at each particular support, and a sharp full-support probability from orbit lengths, including cases where reducing Frobenius to a square-free spectrum would lose information. It gives exact populations without exhaustively enumerating q^{|A|} inputs, rather than a small-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
