# Independent mathematical audit

## correctness

PASS

Walsh characters diagonalize the unit-weight Laplacian with eigenvalues 2k. Grouping by overlap with the differing coordinates gives precisely the Hamming-shell formula (including the 2⁻ᵈ factor). The scalar rational multiplier is strictly positive and is 1 on constants, giving positive definiteness and preservation of mass but not entrywise positivity. Independent exact integer convolution reproduced all off-diagonal numerator factorizations: N₁=−864hP₁, N₂=−864h²P₂, N₇=90720h⁷P₇; the other reduced shell polynomials have strictly positive coefficients. Descartes' rule and the opposite signs at zero and infinity give one simple positive root of each sign-changing polynomial. Exact evaluations are P₇(1/20)=−92179451/16000000, P₇(1/10)=2007369/250000, P₁(1/2)=−207094797/1024, P₁(1)=36753129, and P₂(1)=−18333623. Thus the shell-2 upper bound lies above the shell-1 upper bound and the required closed window is exactly the one claimed; h=0 gives the identity. Numerical Horner bisection agrees with the stated approximations. For the dimension assertion, the Padé recurrence gives c₁,…,c₇=1,1/2,1/6,1/24,1/144,0,−1/1728. Distance r≤5 contributes r!cᵣ at its first possible degree. At distance 6, cube parity forces exactly six edge moves and one diagonal stay in degree seven, giving −7d·6! before multiplication by c₇; at distance 7 the seven moves give 7! and a negative leading term −35h⁷/12. This is a proof for all fixed d, not a finite-dimensional scan. The original replay path artifacts/verify_hypercube_pade.py is present and was read but not executed. VERIFICATION.md reports a package run; the three not_performed fields concern different channels and are not evidence of that run.

## originality

PASS

The exact nonnegative step set on Q₇, including which distance shell controls each endpoint, is supported as distinct. The seventh-order Padé obstruction itself is not new, and the small-step dimension assertion overlaps verbatim in substance with the dimension-twelve cube record. The pass does not credit that shared assertion as independently novel, nor infer priority from catalog dates.

## value

PASS

At the first dimension where refining the step fails to ensure a nonnegative heat update, the result supplies the complete set of usable steps, not merely a negative-entry witness or an example of a usable step. Exact endpoints and their controlling shells matter to a practitioner selecting a positivity-preserving step and to comparisons of graph classes. The cube is a natural reversible, highly symmetric benchmark. The result is not a universal stability bound or an all-dimension all-step classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
