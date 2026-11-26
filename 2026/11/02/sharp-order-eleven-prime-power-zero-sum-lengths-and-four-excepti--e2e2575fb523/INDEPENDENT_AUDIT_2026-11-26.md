# Independent mathematical audit

## correctness

PASS

The unique order-eleven subgroup of the unit group modulo p^k maps bijectively to the subgroup modulo p, since the kernel is a p-group. Thus q−1 is a unit, the full geometric sum gives length eleven, and the minimal lengths cannot decrease with depth. Any shorter sum gives a polynomial g with nonnegative integer coefficients of mass 1–10 and degree at most ten. Cyclotomic irreducibility excludes g being a multiple of Phi_11, whose own coefficient mass is eleven. The resultant is nonzero; over the ten complex embeddings its absolute value is at most 10^10. The integral resultant identity evaluated at q yields p^k divisibility, so for k≥2 only p≤100000 must be checked. A separately written exact replay (not execution of the uploaded C++) enumerated the 352715 multisets via nondecreasing exponent tuples, obtained exact order-eleven roots by powering then simple-root lifting, and evaluated dot products in signed 64-bit integer arithmetic (each sum is less than 10^11 in the tested range). All 945 eligible prime squares reproduced precisely 23:5, 67:8, 89:9, 683:9 and eleven elsewhere. The six deeper checks reproduced 9,9,11 at p=23 and k=3,4,5, and eleven at p=67,89,683 and k=3. The displayed witnesses are consistent with the modular tests. Monotonicity and the upper bound finish all remaining levels; the p=23,k=4 short sum makes the exponent five sharp. Private replay: run `python3 /workspace/branches/f4c8b734-5e9b-4264-a8a9-843992f64fac/order11_replay.py --full` with NumPy; output `replay_full.txt` in the same directory, final REPLAY_OK at line 38. The ancillary length-three/four determinant table was also replayed but is not needed for the classification. The replay is not formal proof-assistant verification.

## originality

PASS

The supported distinct contribution is the exhaustive prime-square classification, in particular the additional short-sum prime 683 and the proof that no other prime occurs. The general norm barrier and several specific minima are antecedents. A distinct same-date catalogue record gives the complete k≥3 theorem and the same sharp stabilization exponent; those components cannot be credited as exclusive, and the date alone gives no ordering. The literature and catalogue inspected do not supply the whole prime-square classification, on which this pass rests.

## value

PASS

The cited literature specifically studies this least-length invariant, and the square-level classification closes a concrete gap left by its selected rows: it decides for every prime not only whether lifting leaves any short relation, but the exact minimum when one survives. The new exceptional prime 683 differs even from its known minimum three over the field. A researcher can use the resulting exhaustive exception list without running a fresh search or guessing from norm valuations. No value claim rests on recomputing the known cutoff or the same-date higher levels alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
