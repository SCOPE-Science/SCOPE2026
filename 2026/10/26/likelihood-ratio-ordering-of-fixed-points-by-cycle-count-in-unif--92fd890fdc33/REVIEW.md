# Independent mathematical audit

## correctness

PASS

The exact known joint enumeration J_n(k,f)=binom(n,f)d(n-f,k-f) is correct. Reconstructed the derangement recurrence d(m,r)=(m-1)[d(m-1,r)+d(m-2,r-1)], weighted path matching polynomial P_m(z)=D_m(z)/((m-1)!z), and Jacobi determinant identity det(tI-H)=t^{m-2} P_m(-t^{-2}), yielding positive-rootedness and strict log-concavity of d(m,r) on support. Rederived mixed-size identities R_m(r)=(m-1)T_{m-1}(r-1) and T_m(r)=(m-1)(L_{m-1}(r)+R_{m-1}(r)), hence T>=0 and strict on positive interior. Adjacent minors equal binom(n,f)binom(n,f+1)T_{n-f}(k-f). Shifting interval row supports and ratio telescoping handle nonadjacent minors including the isolated final row and all zero cells. An independently written exact-integer script verified mixed recurrences through m=58 and ALL pairwise minors for n=2..25 (not the package script), agreeing with proof. Finite tests are supportive only; the all-n induction and interval logic prove the theorem.

## originality

PASS

Ma (2012) explicitly gives the whole joint coefficient formula, and Bóna (2006) credits Brenti (1995) with the derangement real-rootedness. Only the cross-size TP2 and consequent MLR order are claimed original. The strongest priority risk is Brenti (1995) broader total positivity of associated Stirling arrays, not available in full: lawful open-access route failed and authorized Oxford access reported VPN disconnected. This access limitation alone is not a scientific failure; its unresolved implicit-coverage risk is explicit.

## value

PASS

Cycles and singleton cycles are canonical statistics for permutations. Global MLR order is materially stronger than covariance positivity or stochastic dominance: it compares all conditional odds and gives monotone threshold tests at every n. The cross-size determinant induction supplies a nontrivial structural order that the known bivariate enumeration and one-row real-rootedness do not mechanically imply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
