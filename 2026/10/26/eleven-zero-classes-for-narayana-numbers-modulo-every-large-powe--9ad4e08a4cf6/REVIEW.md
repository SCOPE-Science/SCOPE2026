# Independent mathematical audit

## correctness

PASS

For state (N_{n+2},N_{n+1},N_n) the given companion matrix has order 7 modulo 2 and M^28=I+8E with E odd in some entries, whereas M^14 is not the identity modulo 8. Successive squaring preserves E modulo 2 in the leading error term. Thus the matrix order is 7*2^(k-1); the first three orbit vectors form an integral basis, ruling out a shorter scalar period. The last row of E has parity (1,1,0), so each vanishing position in classes 4 and 6 modulo 7 has exactly one lift at each step. At k=6 direct recurrence gives one in class 4, two in class 6, and eight on the 28-grid. On that grid L=log(I+8E) converges, and L=8E-32E^2 modulo 64. The identities eEv=2320 and eE^2v odd yield odd first and second coefficients after extracting 32t from e exp(tL)v. Terms of degree at least three before extraction have valuation at least 8 and tend to zero. The resulting restricted series is 1+t modulo 2 and every distinct-pair divided difference is odd, giving a unique odd root and the exact valuation formula. v2(N_140)=8 then implies alpha=5 modulo 8. The congruences for even and odd t each give four positions in an interval of length 2^(k-3), including zero under the stated convention. The least-state periods, zero sets and local residues were separately reproduced for each k=6,...,14 by python3 /workspace/branches/reproduce_1.py, which also gives N_28/8=2320 and v2(N_140)=8. Finite runs were used for the base and corroboration, not extrapolation.

## originality

PASS

The exact period is covered and receives no novelty credit. The frozen text already puts forward the eleven-zero census and the local two-root valuation law, not the period mechanism, as the advance. The closest antecedent period results do not count zeros of the observed coordinate or give its local factorization. There is a later direct valuation overlap, which is recorded explicitly but is not evidence of an antecedent by its catalog date.

## value

PASS

For this classical third-order recurrence, the count of zero positions in a period is a natural invariant not determined by its length. The result reduces infinitely many congruence counts to a stable residue pattern and gives an exact two-root valuation law in the difficult branch where the elementary one-lift criterion does not apply. The density is a direct consequence, not an independent advance. The three off-grid positions can in fact be identified as P_k-8, P_k-3 and P_k-1 by invertible backward extension (N_-8=N_-3=N_-1=0) and the proved census; this observation does not remove the main two-root difficulty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
