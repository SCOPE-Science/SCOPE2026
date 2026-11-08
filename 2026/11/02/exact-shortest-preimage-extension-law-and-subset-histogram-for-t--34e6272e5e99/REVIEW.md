# Independent mathematical audit

## correctness

PASS

PASS. For the explicitly labeled Cerny automaton a(q)=q+1 mod n, b(0)=1 and fixes other states, inverse b adds 0 exactly when membership at state 1 is one and 0 is zero. Inverse rotations preserve size, and a non-growing initial inverse b can be deleted by monotonicity without losing eventual growth. Therefore a shortest extending word must be ba^j for the first cyclic 0-to-1 boundary. Prefix count 1^k0^(j+1-k) gives (j+1)2^(n-j-2) subsets at j<n-1 and n-1 endpoint subsets at j=n-1; sum/mean/limit verified symbolically. Independent reverse-subset BFS through n=10 reproduced each individual length and the full histogram; uniqueness also follows from deletion plus the first-boundary rule. The claim concerns first size increase, not reset rank.

## originality

PASS

PASS, best of knowledge with material access risk. Miccinesi 2026 treats extending-word certificates and specifically notes existence of hard Cerny subsets, while Berlinkov–Ferens–Szykula study preimage complexity and small examples. Their accessible statements do not imply that every subset has unique shortest ba^j, the entire histogram, or the exact endpoint family. Original Miccinesi full text could not be lawfully fetched (institutional VPN disconnected), so equivalence in its lemmas or appendix remains a substantial risk.

## value

PASS

PASS. The all-size exact distribution of a natural preimage-extension invariant refines an explicit obstruction discussed in recent synchronizing-automata research, distinguishes n hard subsets from typical bounded length, and classifies unique shortest witnesses. It does not assert a new universal reset bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
