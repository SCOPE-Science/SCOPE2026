# Review of cyclic unit-difference permutations for \(3^a p^b\)

## Correctness

**PASS.** For each prime \(p\ge5\), the explicit CRT cycle modulo \(3p\) has two alternating classes; its vertices and its oriented differences cover these classes bijectively because a primitive root traverses every unit modulo \(p\). The lifting lemma for odd \(q\mid m\) is proved by giving each old vertex \(q\) distinct lifts and by observing that every cyclic edge difference has a nonzero linear slope modulo \(q\). The parity of \(\varphi(m)\) handles the last-to-first edge. Iteration proves the exact domain \(n=3^a p^b\) for arbitrary positive exponents. The `verify.py` replay checks 137 finite moduli, including all cyclic closing edges, but the proof, not the sample, justifies the universal quantifiers.

## Originality

**PASS on accessible evidence; publication priority remains subject to independent literature review.** The directly relevant full-text source, Zhi-Wei Sun, *Some new problems in additive combinatorics*, arXiv:1309.1679, proves only the prime-power case in Theorem 1.4 and expressly conjectures the extension to all odd moduli in Remark 1.4. Composite moduli \(3^a p^b\) have two distinct prime divisors, so this is neither a special case of that theorem nor obtained merely by choosing a different primitive root in a cyclic unit group. The two-page 1975 article by Hugo S. Sun, *Structure of the Reduced Residue System with Composite Modulus*, concerns the multiplicative group decomposition of units, not a single cyclic additive-difference ordering. Targeted mathematical-record searches identified no theorem implying the exact mixed-prime result. The generic complete-mapping framework for the whole additive group is not interchangeable with the required permutation on its unit subset. An unindexed or differently named cyclic-sequencing construction could still have priority.

## Value

**PASS.** The finding provides infinitely many explicitly constructed, non-prime-power moduli in a published conjecture. The odd-prime lifting lemma transfers any instance to all its prime-power thickening, an algebraic mechanism useful independently of this base family. This is not a finite enumeration or a parameter substitution into the primitive-root proof for prime powers; the alternating CRT cycle solves the noncyclic unit-group obstruction at the first mixed-prime layer. It does not resolve the general conjecture for all odd integers.

## Limitations

Results involving moduli with prime support not equal to \(\{3,p\}\), for some odd prime \(p\ge5\), are not asserted. No independent proof review or full bibliographic uniqueness certification has been performed. All checked sources and residual originality risks appear in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
