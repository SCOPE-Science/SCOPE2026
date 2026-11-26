# Independent mathematical audit

## correctness

PASS

A constant word allows indefinitely many shifted candidate blocks in its repetitions, as do two distinct rotations in the code: repeat the first word in the true framing and the rotated word in the false one. All other length-five words are primitive, leaving six necklaces and at capacity exactly 5^6 selections. At offset r in 1..4 each candidate word spans two neighboring true words; a run of d candidates corresponds to d overlap edges and conversely concatenating the d+1 true words realizes the run. The false ending differs from a true boundary by r modulo five and hence violates the condition; an aligned run never violates it. A directed cycle permits arbitrary walk lengths, while the longest directed path in an acyclic graph gives the last failing d, with zero edges corresponding to delay one. Complement preserves edges and reversal reverses edges and takes offset r to 5−r. An independent exhaustive implementation uses r-bit prefix states instead of full-word vertices: match a true word’s (5−r)-suffix to the candidate’s prefix, allowing the candidate’s remaining r bits to be the next true word’s prefix. Every such walk lifts because each transition chooses a new true word with the required prefix. Topological elimination and longest-path propagation on these states recover 6421, 86, 5546, 3116, 456 for infinity and delays 1–4. The 9204 finite rows match the frozen CSV byte-for-byte, SHA-256 8f42b6607925826293bfdc79878c2a8c0a11051d1e1cc45f6dc28e8d382e8ea6. Independent stabilizer and Burnside counts give size-two/size-four splits (17,1378), (10,774), (0,114) at delays 2–4, hence 1395, 784, 114 orbits. The Lyndon selection has delay two and certifies attainable capacity six. Replay: python3 /workspace/branches/independent_delay.py with the frozen catalogue.csv path as its sole argument. Both packaged verifiers were inspected, not executed. Delay counts error-free candidate blocks, not elapsed bits, and the census is only for binary length five at capacity.

## originality

PASS

Pass is for the exact new delay-2–4 spectrum and orbit decomposition at capacity, together with the complete finite versus unbounded split under the stated block-count convention. Neither capacity six nor the delay-one stratum is credited as original. The precise delay-one census is verified in a different same-day indexed record, but the wording ‘known previously’ does not establish earlier publication of that count; the inspected classical passages establish the capacity and construction, not the count. This bibliographic distinction does not affect the mathematical spectrum or the explicitly excluded scope of novelty. No inspected exact or implication-equivalent delayed spectrum dominated the supported distinct result.

## value

PASS

Length five is a natural primitive-necklace capacity case with a known comma-free boundary. The exact classification quantifies the choices opened up by allowing finite rather than immediate resynchronization at the same optimal size, determines the maximum attainable finite delay, and provides a replayable full catalogue with equivalence counts. These are different framing tradeoffs at fixed capacity, not a bit-error or throughput assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
