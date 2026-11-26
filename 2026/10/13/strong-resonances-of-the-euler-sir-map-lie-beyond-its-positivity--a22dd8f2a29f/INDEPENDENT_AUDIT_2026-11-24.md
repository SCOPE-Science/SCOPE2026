# Independent mathematical audit

## correctness

PASS

Let k=d+r and R=Aλ/(dk)>1. At the endemic fixed point the Jacobian has entries 1−hdR, −hk, hd(R−1), 1, in row order. Thus det J−1=hd[hk(R−1)−R]. For h>0 the determinant-one locus has hk=R/(R−1)>1; the endemic unit-circle pairs in question all have multiplier product one. The infected multiplier 1−hk+hλS vanishes there at S=(k/λ)/R and is negative for smaller S; the next infected coordinate is negative when I>0. This is failure of state-space invariance, not invalidation of the local normal forms or a sufficient positivity test for the whole map. The source equation (1.3), three section 4 resonance examples, and the separate Figure 6 seed and common A,d,r were checked in the original paper. For the rounded 1:3 tuple the exact fraction replay gives I_next=−10256632066707/10^14. The exact determinant at that rounded tuple is 1.0002999324, not 1: RESULT.md explicitly introduces the tuple as rounded; the exact strip theorem and the direct rounded witness must not be conflated. No assertion is needed that the exact rounded pair is a Figure 6 grid node.

## originality

PASS

Credit the original map, endemic characteristic polynomial and resonance loci to the literature. The supported distinct result is the incompatibility of that same map's endemic unit-determinant locus with infected positivity, the exact open strip, and the numerical interpretation check using the paper's phase-diagram seed. No inspected statement already supplies this connection; the primary-literature search was unavailable, so this is a bounded best-of-knowledge judgment.

## value

PASS

The positivity obstruction separates local formal dynamics of an Euler polynomial map from a globally admissible population-state update. It excludes an entire family of endemic strong-resonance boundaries from that interpretation and supplies a strictly positive, source-matched initial state for which the plot protocol's first step is already inadmissible. This is a concrete interpretation check, not merely the reformulation of a known determinant boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
