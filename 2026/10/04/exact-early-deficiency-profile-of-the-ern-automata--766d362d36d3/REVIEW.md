# Independent mathematical audit

## correctness

PASS

Only \(b\) can reduce image size and each application reduces rank by at most one, so deficiency \(s\) needs at least \(s\) effective \(b\)'s. After an effective \(b\), state \(n-1\) is missing. A subsequent effective \(b\) requires at least two intervening \(a\)'s: zero leaves \(n-1\) absent, while one rotates the unique relevant gap so that applying \(b\) cannot reduce cardinality. Thus every such word has length at least \(s+2(s-1)=3s-2\). For the displayed witness, induction gives the exact missing set after each effective \(b\); the range \(s\le\lceil n/2\rceil\) ensures the odd missing states do not wrap into the two states needed for the next contraction. Independently, subset-BFS for all \(3\le n\le11\) and every admissible \(s\) reproduced \(3s-2\) in 34 cases; the package artifact checks through \(n=12\).

## originality

PASS

Classical rank-threshold work gives general polynomial/quadratic upper bounds, including Pin's circular-automaton rank conjecture results and recent Černý-type monoid bounds, but not this exact first-half profile. A relevant published SCOPE result determines the worst prescribed \(k\)-set avoiding threshold \(kn\) in the Černý family; that is a maximum-over-target-sets problem and does not imply the minimum length to lose any \(s\) states. No exact \(3s-2\) profile was located.

## value

PASS

Intermediate rank collapse is a standard refinement of synchronization, and the Černý family is the canonical extremal family. Determining the exact early half of its deficiency profile, with a matching lower-bound mechanism and explicit optimal witnesses, is a natural structural result rather than a finite census. It also separates the cheapest initial contractions from the much slower final reset phase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
