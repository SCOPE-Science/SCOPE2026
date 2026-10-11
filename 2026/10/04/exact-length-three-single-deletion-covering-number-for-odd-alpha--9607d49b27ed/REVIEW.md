# Independent mathematical audit

## correctness

PASS

Every length-three word has at most three distinct length-two deletion descendants, giving the lower bound ceil(q^2/3). For q congruent 3 mod 6, q>=9, choose the cycle C_q as a partial-triple-system leave; for q congruent 1 or 5 mod 6 choose C_{q-1} plus one isolated vertex. The Colbourn–Rosa theorem applies because all leave degrees are zero or two, the necessary parity/divisibility conditions hold, and the lone exception C4 union C5 is never selected. Two opposite words per triangle cover all six orientations of its three edges; one word (v_i,v_{i+1},v_i) per cycle edge covers both orientations plus loop (v_i,v_i), and the isolated symbol uses (z,z,z). The counts simplify to ceil(q^2/3). q=3 is covered by the explicit three-word cycle code. Fresh independent checks reproduce complete coverage and exact size for q=5,7,9,11,13.

## originality

PASS

The recent deletion-covering paper proves asymptotic tightness of the elementary counting lower bound as alphabet size grows and gives asymptotically optimal constructions, but the accessible primary material does not state the exact odd-q length-three formula. The classical partial-triple-system theorem supplies exactly the design-existence ingredient but does not formulate deletion covering codes. Exact-value searches returned no prior all-odd theorem. The complete recent preprint body could not be obtained in this run; one authorized fallback returned a transport-level unavailable/request-invalid error, retained as a residual risk.

## value

PASS

The theorem exactly closes the elementary counting bound on an infinite, arithmetically natural half of the alphabet sizes. It converts a classical leave theorem into an explicit synchronization-error covering construction and provides a clean finite-length benchmark complementary to recent asymptotic deletion-covering theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
