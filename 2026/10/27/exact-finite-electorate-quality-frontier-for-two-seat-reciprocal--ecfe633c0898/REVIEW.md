# Independent mathematical audit

## correctness

PASS

The final RESULT.md in /workspace/repairs/4 centers on the pointwise rEJR comparison and gives a complete proof. No affordability demand can have size above two. An affordable size-two set requires the whole electorate and two unanimously approved unit-quality candidates, since each reciprocal term is at least one. In their absence the feasible sets coincide. In their presence rEJR adds exactly the requirement that the two selected candidates have a joint supporter, beyond rJR, and the unanimous pair attains quality two. In any rJR-optimal pair both members therefore have unit quality; keep either supported candidate and choose a distinct unanimous unit candidate, representing all voters while giving the retained candidate's supporter two approved members. The same works from any unrestricted optimum in this regime. Otherwise, a witnessing unrepresented bloc S for a top-pair rJR violation has n/2<=|S|<=n-1 and common affordable candidate of quality at least tau=n/[2(n-1)]. Retaining the higher-quality original candidate and selecting that candidate represents S and an additional voter, ruling out any further rJR violation and hence rEJR violation. The sharp guarantee follows from the exact nonnegative slack identity with 0<tau<=1. The witness with one voter approving the two unit candidates and n-1 voters approving the tau candidate meets the quota at equality; the two axioms coincide on it, including at n=2. The original verify.py and VERIFICATION.md were inspected, not executed. The independent /workspace/branches/two_seat_replay.py checked the original bound, equality and one-replacement claims on 96,875 exhaustive, 400 sampled and 9 sharp profiles. The new bounded repair verifier was run as python3 /workspace/repairs/4/verify.py; it returned EXACT_OK exhaustive=16551 sampled=240 sharp=9 separation=1, also testing the committee-level criterion and the optimum-preserving replacement. These exact finite runs only corroborate the arbitrary-size, real-quality proof.

## originality

PASS

This pass is only for the repaired rEJR result, not the original joint novelty claim. The original fixed-n rJR fraction is identical after inversion to record fda9761638b2 and its attaining construction specializes BD&KU Example G.1. The rJR-only bound and single-substitution argument are benchmark material, not separately credited. The surviving claim characterizes exactly how the stricter axiom changes feasible committees at two seats and shows that every rJR optimum can be changed to an equally good rEJR optimum while retaining either selected member. It yields a sharp finite-n guarantee with one replacement for rEJR. The sibling and indexed minimum-support theorem concern rJR, not this comparison. The known equal unrestricted worst-case prices and the quality-floor result do not establish equality instance by instance. The bounded inspected literature and index yielded no covering statement for the repaired claim; this is not a priority certification.

## value

PASS

The repaired claim reduces exact optimal-quality selection for a stricter proportionality axiom to the weaker one on every two-seat election. It pinpoints the sole exceptional demand, explains why feasible sets may differ even though the optima do not, and constructs an equally good strong-axiom optimum preserving a chosen member of a weak-axiom optimum. It therefore transfers a sharp finite-electorate guarantee to rEJR with a single-change certificate. This is a structural consequence for a natural small committee size, not credit for repeating the rJR price or the previously supplied family of witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
