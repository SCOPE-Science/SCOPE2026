# Independent mathematical audit

## correctness

PASS

Block multiplication gives the stated commutator sign XV-UY. Commuting against every pure X or pure Y block forces all noncentral coordinates to vanish; scaled elementary C matrices are commutators, so the derived subgroup is precisely the center. For t independent pairs, concatenate X_i,-U_i as A and V_i,Y_i as B with inner dimension d=2bt. This is a bijection on the noncentral coordinates, including in characteristic two, with q^(2tac) free central coordinates. For rank(C)=r, choose an s-dimensional image of A containing im C via a Gaussian coefficient on the quotient, choose a surjection with independent rows, and lift each of the c columns through A in q^(d-s) ways. Thus the sum is positive exactly for r<=d, with identity length zero and exact maximal width. Character averaging over B forces TA=0, so each column of A contributes q^(-rank T), giving the claimed Fourier and Parseval identities. For the lower TV bound, transpose if needed and use the union over d-dimensional image spaces under the uniform measure; the Gaussian coefficient times q^(-(m-d)M) gives the stated exponent. For the upper bound, full row rank of the shorter-side factor (after transposition if needed) gives exact conditional uniformity. Its failure probability is at most q^(-d)(q^m-1)/(q-1) by a union bound over projective linear forms. These bounds give a bounded-width cutoff uniformly for M>=m and fixed q,b, not exact TV mixing at the first full-support step. For example, in the square case with d=m, the full-rank event has probability p_m² under the product and p_m under uniformity, where p_m=product_{j=1}^m (1-q^(-j)); the difference has a positive limit. An elementary spot check for q=2 and a=b=c=1 gives 10 and 6 dot-product factorizations at d=2 and hence fibers 40 and 24. The archived field/group verifier was inspected, not rerun; its cases corroborate fibers only in the tested parameters.

## originality

PASS

The commutator law is already determined by classical Frobenius inversion applied to the same-group character formulas, and the later Resultary record 65007f7be362 explicitly states the same one-step fiber and exact length. The independent contribution supported here is the explicit rank-factorization/support calculation together with the sharp-in-location, bounded-window total-variation law uniform over rectangular aspect ratios, not character-theoretic priority or undetermined status of the commutator distribution. The inspected earlier statements do not give that quantitative mixing theorem by specialization.

## value

PASS

The group family naturally supplies finite class-two examples with large internal commutator width. Linking rank support to a bounded TV window uniformly over aspect ratios gives more than eventual reachability or a character formula. The first full-support time locates the window, but it is not an exact mixing time; the result is valuable with that distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
