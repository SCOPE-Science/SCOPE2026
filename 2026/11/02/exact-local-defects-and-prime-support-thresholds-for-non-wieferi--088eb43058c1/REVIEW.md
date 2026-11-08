# Independent mathematical audit

## correctness

PASS

LTE at p gives ord_{p^e}(2)=t_p p^max(0,e-h_p) for t_p=ord_p(2), h_p=v_p(2^t_p-1) and p odd. CRT yields ord_n(2)=lcm over p; the p-adic valuation of this lcm is max(0,e_p-h_p,H_p(P)) with H_p=max_{q!=p}v_p(t_q), because p does not divide t_p. LTE again yields v_p(2^ord_n(2)-1)=max(e_p,h_p+H_p). Subtract e_p for the quotient gcd, so non-Wieferich exactly e_p>=h_p+H_p for all p. Lattice-point simplex counting gives the support-restricted asymptotic. Independently checked the original gcd formula for each odd n<=1000, including 21 vs 63; finite calculations complement unrestricted LTE/CRT proof.

## originality

PASS

Siegel arxiv:2610.28685 gives the definition, one-way prime obstructions, sufficient squarefree criteria and global asymptotics, but inspected Lemmas 2.1, 2.2 and 2.4–2.5 do not give arbitrary-exponent exact gcd valuations or full prime-support principal-upset classification. Membership table OEIS A182297 is prior. Franco–Pomerance 1995 original paper was only available through quoted lemma and bibliographic data, so a meaningful implicit-priority risk remains.

## value

PASS

The order-based Wieferich predicate is a natural multiplicative-order arithmetical object; the complete exponent-space description at every odd prime support, including cross-order interactions and anomalous height primes, answers a precise structural classification question. Example P={3,7} has minimum 63 despite 21 being obstructed; the support count is a natural quantitative corollary. The ingredients are classical, but their explicit general-support classification is not an arbitrary small exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
