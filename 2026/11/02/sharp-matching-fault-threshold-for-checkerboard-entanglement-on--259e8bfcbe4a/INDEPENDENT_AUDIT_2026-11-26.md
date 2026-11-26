# Independent mathematical audit

## correctness

PASS

The binary cut matrix determines the flat nonzero Schmidt spectrum and hence the entropy, including all ordinary positive Rényi orders. The even-d adjacency squares to zero; multiplication by the nonzero linear form in the square-zero group algebra has half rank, giving r=2^(d-2) for B and identifying each parity image with the opposite transpose kernel. The cited minimum distance can also be checked directly: split on one cube coordinate and let S be the (d-1)-cube adjacency. S^2=I over F2 and the full adjacency image consists of (z,Sz). If the smaller block has weight k<=d/2, the other has weight at least k(d-1)-4 binom(k,2), since two distinct cube vertices share at most two neighbors and for t incidences the binary parity count is at least t-2 binom(t,2). The total is at least k(d+2-2k)>=d for 1<=k<=d/2; if both blocks are larger, the bound is immediate. A neighborhood attains d. Thus for k<d the distinct endpoint indicators are independent modulo the two images. In bases reducing B to an identity block and zero block, the full-rank quotient projections let block-triangular operations remove the upper parts of both update factors without changing B, giving the exact rank increment k. At k=d the neighborhood matching has just the all-ones endpoint relation on both sides. The projected kernel is the even-sum hyperplane; the candidate nonzero relation would require the all-ones vector plus a single indicator to be in this hyperplane, impossible for even d. This gives nullity r-d+1. The replacement changes the full endpoint sum by two coordinate vectors of weight two, which is below the code distance, so it is no longer in the image; translation gives the other side and the increment d. Interpreted in the usual positive-order Rényi domain: the wording does not justify finite negative-order full-space traces in the presence of zero eigenvalues. Inspected RESULT.md, VERIFICATION.md, checks/verify.py and checks/verification_output.txt. The logged 4,031 comparisons include exhaustive Q4 sizes 1–3, sampled larger cubes and both witnesses; the replay path is python3 checks/verify.py, not rerun here.

## originality

PASS

The supported distinct result is the all-placement interval up to d-1 for every even d>=4, together with the first two rank values witnessed at k=d. Flat cut rank, the base rank and code distance are prior ingredients. The 4-cube one-edge instance is covered by the 4 by 4 torus calculation. The strongest same-cube indexed comparison produces subsets of a particular matching, not the universal quantifier or the dependent threshold witness. A same-day projective-plane threshold theorem concerns a different incidence matrix. No priority beyond these comparisons is asserted.

## value

PASS

Disjoint omitted gates are a natural ideal fault model, and the question is whether their cut-entanglement effects superpose regardless of placement. The exact first placement-sensitive size, including both constructive outcomes there, is a useful boundary that cannot be inferred from a table of examples or a bound on single-edge effects. It makes no operational claim for noisy gates or fault-tolerance protocols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
