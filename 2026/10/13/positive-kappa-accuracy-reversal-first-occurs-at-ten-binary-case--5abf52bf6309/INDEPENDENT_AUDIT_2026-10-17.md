# Independent mathematical audit

## correctness

PASS

For P reference positives, Q=N-P negatives, x=TP, y=TN, M=x+Q-y predicted positives, exact simplification yields kappa=2(Qx+Py-PQ)/[P(N-M)+QM], with positive denominator. Independent rational enumeration of all 4<=N<=10, 2<=P<=floor(N/2), 1<=x<P,1<=y<Q filters kappa>0 and compares every within-P pair: normalized admissible counts (0,1,2,5,9,13,22) and reversal counts (0,0,0,0,0,0,1). Unique N=10 witness is A(X)=3/5,kappa(X)=1/21 and A(Y)=1/2,kappa(Y)=2/27. For any N>=10, X_N=(1,2,N-5,2), Y_N=(2,1,N-7,4) have accuracies (N-4)/N>(N-5)/N and kappas (N-9)/(3(N-3))<4(N-9)/(9(N-4)), by 12(N-3)>9(N-4) iff 3N>0. Infinite family algebraic proof distinct from finite enumeration.

## originality

PASS

Statement/implication comparison, not mere title search. Closest inspected antecedents give related machinery or narrower/scalar/qualitative statements, but not the full asserted theorem; coverage and inaccessible-source limitations are explicit.

## value

PASS

The first nondegenerate positive-agreement sample size at which two familiar assessment statistics impose opposing strict classifier rankings is a motivated exact finite boundary, with unique normal-form witness and an infinite continuation family. The restrictions isolate genuine rather than negative-kappa or empty-cell reversals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
