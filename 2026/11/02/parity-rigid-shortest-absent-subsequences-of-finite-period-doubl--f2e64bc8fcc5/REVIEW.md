# Independent mathematical audit

## correctness

PASS

PASS: The substitution mu(0)=01,mu(1)=00 gives q_{k+1}=2^k-q_k ones and q_k=(2^k-(-1)^k)/3. Each one has a disjoint preceding zero, so (01)^q_k embeds, proving q_k-universality. There are only q_k ones, giving the opposing nonuniversality bound. For even k the last zero appends the witness U_q=(01)^q0, whose only missing (q+1)-word is 1^(q+1). For odd k>=3 the last-eight suffix 01000101 embeds V_q=(01)^(q-2)00101, whose shortest absent set is established by simultaneous induction with universal S_q=1V_q. The 3 exceptional candidates also fail in P_k from the last-one and penultimate-one suffix constraints. The rank-one P1=01 case is separate. Independent exhaustive greedy subsequence enumeration for ranks1..5 confirms missing counts 3,1,3,1,3, and exact words. Infinite statement rests on the substitution/induction, not finite checks.

## originality

PASS

PASS best-of-knowledge: Kosche–Koß–Manea–Siemer provide general SAS/arch-factorization definitions and polynomial-delay enumeration for arbitrary words (Theorem 4.19), but that does not state or mechanically imply a fixed substitution family has exactly one versus three SAS and these explicit word forms at all ranks. Parreau et al. study contiguous 2-Abelian complexity of period-doubling, a different invariant. Published Resultary general binary SAS extremal results concern maxima across all length-n words, not the particular P_k language.

## value

PASS

PASS: The precise universality index and complete shortest-absent language of all period-doubling iterates are natural substitution-word invariants. A parity-rigid tiny SAS set despite exponentially growing universality index is structurally informative and reusable in subsequence universality and automatic word research. This is a complete all-rank classification, not a single finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
