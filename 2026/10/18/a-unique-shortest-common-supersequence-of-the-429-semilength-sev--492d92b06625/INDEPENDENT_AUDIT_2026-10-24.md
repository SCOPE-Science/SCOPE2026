# Independent mathematical audit

## correctness

PASS

D7 is the 429 Catalan balanced-parenthesis words of semilength7. The provided verify_exhaustive.cpp genuinely iterates all 2^21 and 2^22 unrestricted binary hosts; its Dyck recursion is one-to-one, first-two-target prefilter sound, and greedy subsequence predicate necessary and sufficient. Source inspected rather than accepting printed output alone. A wholly independent C++ implementation using reversed generation order and high-bit-first host enumeration was compiled and executed and found 429 targets, ZERO universal length-21 hosts and exactly ONE universal length-22 host, (()(()()()()()()())()). Padding rules out every shorter length. The BFS program and its prefix-state merging were also inspected, including unique minimum and no 3-million-state cutoff at the claimed 1,690,893 states. Finite claim exhaustively proved by complete search over its finite domain.

## originality

PASS

General shortest-common-supersequence complexity and fixed-resource variants are established; Clifford et al. 2010 restrict hosts to preassigned letter multisets rather than demand a universal cover of all Dyck7 targets with unrestricted host counts. Resultary matching on exact 429/length22/Dyck gives other automatic-language and subsequence universality problems but no same exact pair. An older specialized Catalan table under another name could still cover it; no exhaustive priority certification.

## value

PASS

The complete 429-word Catalan family is canonical; minimum scattered-subsequence cover length and uniqueness form natural exact compression invariants. Exhausting 6,291,456 hosts with a sound all-target oracle gives the nontrivial semilength-seven cutoff and unique extremizer, not a routine substitution or tiny toy computation. An exact finite benchmark is independently useful even absent asymptotic n-theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
