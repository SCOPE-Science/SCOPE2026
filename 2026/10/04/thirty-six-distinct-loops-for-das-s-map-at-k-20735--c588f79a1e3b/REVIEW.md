# Same-model scientific review

## Correctness
PASS. For odd \(k\ge3\), Das's Lemma 2.2 implies that every loop contains a prime at most \(k\). Starting from such primes, trajectories stay inside \(2\le x\le2k+2\), making the census finite and exhaustive. The packaged checker scans every odd \(k\le20735\), canonicalizes cycles, and verifies exactly 36 at \(k=20735\) with the stated period histogram. A separate implementation independently reproduced the \(k=20735\) count and histogram.

## Originality
PASS. Das's source reports only \(k\le5000\), with maximum loop count \(14\) at \(k=4479\), and asks whether loop counts are unbounded. Later work by Dubickas proves broader boundedness and periodicity results but does not state this updated record in the inspected material. Targeted semantic and exact searches did not locate the \(20735\), \(36\)-loop result. Residual risk remains for unindexed or private computations.

## Value
PASS. The finding directly advances the empirical frontier of a stated open issue and more than doubles the published lower bound on attainable loop counts. The endpoint is a strict record parameter in the exhaustive odd-\(k\) scan, and the complete record sequence and period profile are reusable benchmarks.

## Closest literature and limitations
The closest prior work is Angsuman Das, “A Family of Iterated Maps on Natural Numbers,” arXiv:2312.06629, together with Artūras Dubickas, “A Class of Bounded Iterative Sequences of Integers,” *Axioms* 13 (2024), 107. The present result is finite, covers only odd \(k\) beyond the published range, and does not prove unboundedness.

Same-model review: passed. Independent audit: not yet performed.
