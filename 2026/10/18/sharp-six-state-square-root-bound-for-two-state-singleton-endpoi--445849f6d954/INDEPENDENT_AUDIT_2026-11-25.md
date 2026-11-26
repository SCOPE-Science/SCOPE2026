# Independent mathematical audit

## correctness

PASS

Membership of the doubled word is the Boolean (s,t) entry of M(w)^2. A path of unordered pairs lifts to two labeled runs: at each letter choose the matching that realizes the pair transition and swap labels as necessary to agree with the preceding step. Thus the two possible midpoint states for s≠t are implemented by independent three-state components, [s,s] to [s,t] and [s,t] to [t,t], with language terms m_ss·m_st and m_st·m_tt. For s=t the required terms are m_ss or m_su·m_us; the three-state pair component from [0,1] to itself admits also m_00·m_11, which is already covered by the ordinary two-state m_ss component. Disjoint union is epsilon-free and accepts the empty word exactly when s=t. I independently simulated the doubled concatenations in the two-state source by propagating reachable sets, without Boolean matrix multiplication or the uploaded checker. The six rows are 110000, 010000, 111000, 111100, 111110, 111111. All diagonals are one and no opposite off-diagonal pair is simultaneously one. Mark a state after each prefix in its chosen accepting run: equality of two marks would splice both cross-concatenations, a contradiction even with multiple initial states. This proves six states are required for the binary witness.

## originality

PASS

The exact ordinary-NFA small-source bound with a binary witness is not supplied by the general cubic theorem or the closest same-size parity or deterministic results. Credit is for existential-path state complexity under the stated endpoints, not for the general square-root construction or the standard fooling-set technique.

## value

PASS

Square root is a standard language operation, and two source states are the first nontrivial case. The sharp binary witness and endpoint-dependent pair compression give a justified exact gap from the general cubic upper bound; the witness is not a table lookup or a substitution in the known large-state theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
