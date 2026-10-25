# Independent mathematical audit

## correctness

PASS

The pinned package defines PS as continuous unit-rate eating, RP as average over uniform agent permutations, and each received r-th choice earns n-r Borda points. Object relabeling is free because the first agent has a strict order, reducing all (n!)^n profiles to (n!)^(n-1) canonical profiles with n! multiplicity. An independently written rational PS event simulator and RP recursive Bellman welfare evaluator enumerated all canonical profiles n=2,3,4; n=4 has exactly 13824 reps, giving over all 331776 labelled profiles 87408 positive, 129168 zero and 115200 negative PS-minus-RP values; mean 1283/62208>0. n=3: 36 negatives at -1/12 and mean -1/72; n=2 all zero. The source also cross-checks matrix and direct-welfare implementations. For every n>4, new agents each rank their fresh personal object first and all old agents rank old objects above new ones: both rules preserve old four-agent lotteries and only shift each old Borda score by constant n-4, so the positive and negative four-agent witness signs persist.

## originality

PASS

Classic PS/RP literature and Ortega–Zhao directly discuss efficiency and expected ranks; three-agent disagreement is prior. The exact FOUR-agent signed frequency distribution and opposite signs of profile-majority versus impartial-culture average are not implied by bounds or asymptotic efficiency claims. A previously compiled complete four-agent Borda table remains plausible but was not identified.

## value

PASS

At the smallest postclassical market size, this natural rank-welfare comparison exhibits a sharp mean sign change even though more individual profiles favor the opposite mechanism. The exhaustive exact distribution is an interpretable quantitative decision-theory invariant and the sign-persistence construction shows its robust logical scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
