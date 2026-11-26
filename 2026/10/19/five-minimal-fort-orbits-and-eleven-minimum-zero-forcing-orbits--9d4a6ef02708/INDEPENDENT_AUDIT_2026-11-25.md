# Independent mathematical audit

## correctness

PASS

Repaired claim: the monotone parallel color-change map reaches all vertices exactly when an ordinary forcing process can. A synchronous batch can be sequentialized by skipping already black targets, and the synchronous terminal set is closed under every possible legal force, so no sequential solution can escape it. Upward closure makes successful single-vertex deletions the exact test against inclusion-minimality. Xor translations and coordinate permutations give all 384 automorphisms: once 0 and its neighbors are fixed, each higher-layer vertex is forced by its predecessor supports. An independent exact replay in `/workspace/branches/0963b538-613f-4568-a887-077afec5d42b/q4_independent_check.py` inspected all 65,536 subsets and agreed mask-by-mask between direct forcing and the complement-fort test, including the original five fort orbits and the forcing polynomial. Its saved `q4_independent_check.json` lists the 11 least forcing representatives, their sizes and times, and confirms exactly 2360 inclusion-minimal sets, all size 8. Inspected the frozen proof, verification scripts and representative table without running the frozen scripts. The corrected package `/workspace/repairs/1/` narrows the finding to the forcing-side census and omits the fort theorem and the aggregate polynomial. Its new checker, `python3 /workspace/repairs/1/verify_minimum_orbits.py`, was executed: 'Checked 65536 subsets: 2360 minimum sets, 11 orbits.' It additionally checks constant synchronous time throughout each orbit, validates the complete corrected table, and gives the four totals 8, 816, 1152 and 384. This is exact finite exhaustion for Q4, not a proof for all cubes. No mathematical falsity was found in the original claim.

## originality

PASS

For the repaired finding only. The original combined claim cannot pass as a distinct contribution in full: the exact five-orbit minimal-fort classification is also covered, with identical masks and orbit sizes, by the distinct indexed record 4b4a85b72c98. Its later catalogue label does not settle historical priority and is not used to infer priority. Remove that component and the already encoded aggregate size polynomial as findings. The exact eleven-orbit forcing census, its time multiplicities, and the absence of larger inclusion-minimal forcing sets survive the comparisons below.

## value

PASS

The repaired finite census answers the published question of enumerating minimum sets on a natural symmetry-rich graph. It supplies automorphism classes and exact times per class, information not delivered by the scalar minimum, aggregate polynomial or examples exhibiting a range. The proof that no larger inclusion-minimal set occurs makes the eleven classes exhaustive also for inclusion-minimal forcing, not just for one selected cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
