# Independent mathematical audit

## correctness

PASS

For B_n (n≥3), b is cyclic rotation, c fixes 0 and sends all other states to 1. The pair {0,1} persists under c, but c collapses any distinct pair avoiding 0. When k≤n−2 Bob responses have length ≤n−3. Alice first uses c, then if the response pair avoids 0 chooses c; if it is {0,1}, she uses b, forcing {1,2}, and a bounded response either collapses or leaves a pair avoiding 0, so the third move c wins. If k≥n−1, Bob indefinitely preserves a distinguished two-token pair {0,j} by responding after b with b^(n−1−j), length≤n−2, or the empty word after c / appropriate b, proving nonwin. No length≤2 word resets; cbc resets, so minimum worst-case Alice turns is exactly 3. Unary synchronizability is equivalent to a constant power, giving no hierarchy separation; binary is minimal. Independently computed entire subset-game attractors for n=3..7 and k=1..n+1, exactly matching the threshold and three-turn worst case. Finite enumeration does not establish all n; explicit strategies do.

## originality

PASS

Lipin–Volkov (arxiv:2601.18362 §2.2, Lemma 2.1/Corollary 2.2) already constructs strict adversarial synchronization levels with three-letter E_n, whose b,c maps match B_n but with an additional d action. Removing d changes both Alice and Bob action sets; their strictness proof does not by itself prove the exact binary threshold n−2, as witnessed by the different cutoff. Other alphabet-restricted results in §3 do not supply the all-level two-letter witness. The binary minimum and explicit all-n cutoff survive the checked prior implications; older binary-game constructions remain priority risk.

## value

PASS

The least alphabet size maintaining every strict level of the synchronization-game hierarchy is a natural exact complexity parameter. This gives the sharp bound two versus one, a uniform family for every level, and exact three-turn Alice strategy/Bob invariant. The result is not merely a renaming of the known three-letter witness because deleting d alters both participants’ legal dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
