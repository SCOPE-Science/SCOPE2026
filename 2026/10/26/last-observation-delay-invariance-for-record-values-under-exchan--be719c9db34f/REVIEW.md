# Independent mathematical audit

## correctness

PASS

For adjacent candidate times t,t+1 strictly after nonempty T, the event A that exactly one exceeds max_{i∈T}X_i is invariant under that transposition τ. For any measurable test, change variables by τ on A and use the identity on its complement to see that the conditional swap preserves the full exchangeable law. The smaller value on A cannot beat the full-prefix maximum; the larger contributes the same record height or none, and the running maximum afterward is unchanged. The multiset is preserved, with multiplicity. The retained last-step indicator is exactly transferred, even at ties with the threshold. This yields all delays by adjacent equalities in law, also with the multiset included. It cannot generally preserve the joint law with record times: for a uniform permutation of three ranks with T={1}, full record times (1,3) force the selected count to be 1 for final time 2 and 2 for final time 3. For iid atomless data take t=k+1 by invariance. The successive ascending insertion ranks U_i are independent uniform on {1,…,i} by the rank-permutation bijection, and the comparison J is 1{U_{k+1}>U_k}. Hence E(I_k J)=1/[k(k+1)], E(I_{k+1}J)=1/(k+1), and all other record indicators are independent of J. Subtracting the marginal terms gives 1/[2k(k+1)]; Var(J)=1/4 and summing independent record-indicator variances gives the claimed correlation, also at n=2. The proof is replayable from RESULT.md lines 24–52. The successful finite output is recorded in the frozen VERIFICATION.md; the uploaded code was inspected, not rerun.

## originality

PASS

Bounded pass for the main exchangeable joint-law result, including strict ties and the extra multiset coordinate. Do not credit the adjacent-position covariance in isolation: another indexed record gives its equivalent signed descent covariance. The arbitrary allowed final-time specialization here uses the joint invariance and is not obtained from the adjacent formula alone.

## value

PASS

This is a specific conditional non-identifiability theorem for where a last retained observation was taken, even after the full height list and multiset are revealed. The exact scope matters: revealing timestamps can break it, and moving the earlier sampling point can change the law. The exchangeable result with ties supplies the value; the adjacent covariance, while useful for illustrating location sensitivity, is not the basis for the pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
