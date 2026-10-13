# Scientific review: jump-and-symmetry minimum rank

## Correctness — PASS

The claim quantifies over every integer \(n\ge2\), every \(1\le h<n\), and every active subset \(A\); it includes empty and full patterns. The subgroup \(H(A)\) is an exact semigroup symmetry, so the original rank equals its orbit count times the quotient rank. The quotient pattern has trivial stabilizer. The letter actions on residue classes modulo \(d=\gcd(n/|H(A)|,h)\) are bijections, giving the lower bound. Aperiodicity is used precisely to choose an active predecessor and inactive right endpoint of any proper jump-cycle interval, yielding an exact inverse-image identity. Conjugate partial jumps then collapse each residue class, proving attainability. The boundary \(d=m\) is handled separately. The independently implemented subset-BFS and constructive replay report `VERIFY_OK` on the stated finite domains. Finite replay does not substitute for the proof.

## Originality — PASS, subject to residual risks

Kari–Ryzhikov–Varonka give a length bound conditional on the minimum rank, not the present computation of minimum rank. Volkov and Rystsov–Szykuła provide structural synchronization theorems, but their inspected claims do not determine rank for an arbitrary active pattern and a possibly noncoprime jump. The unit-jump stabilizer formula and singleton-active-set synchronization cases are covered by earlier work; they are not claimed separately as new. The present genuinely mixed \(h\) and \(A\) regime is neither implied by those restricted cases nor covered by the inspected primary sources. Searches used the equivalent formulations minimum rank, cyclic partial translation, jump/gcd, necklace stabilizer and circular automaton. An unindexed equivalent theorem remains possible; semantic-search absence alone does not establish novelty.

## Value — PASS

The theorem provides an exact, parameter-free classification across all active patterns and all nonzero cyclic jumps, including the unsynchronizing regimes. The separation \(|H(A)|\gcd(n/|H(A)|,h)\) isolates two independent structural obstructions to rank reduction. It determines an intrinsic finite-automaton invariant without subset-graph enumeration, and settles the interaction not explained by its unit-jump and single-active-point special cases. No shortest-word complexity claim is made.

## Sources and scientific limitations

The primary full texts inspected were Kari–Ryzhikov–Varonka (2019, Section 4.2 and Theorem 3), Volkov (arXiv:2306.13317v1, synchronization theorems), and Rystsov–Szykuła (arXiv:2307.01302v1, Sections 4.2–4.3). An undetected equivalent or stronger theorem is the main outstanding originality risk. The verifier covers finite domains only. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
