# Scientific assessment

## Correctness — PASS

For safe primes \(p\ge11\), the cyclic group order \(2q\) makes its primitive elements exactly the quadratic nonresidues other than \(-1\). The reflection involution pairs all-residue and all-nonresidue length-four runs. Expanding the four quadratic-character factors, using six exact quadratic sums, and explicitly subtracting the four polynomial roots yields the integer quartic-character formula. Excluding at most four placements of \(-1\) yields the all-step count. The squarefree quartic Weil bound makes the baseline count exceed four at every \(p\ge113\). The complete safe-prime list below that cutoff has been independently and exhaustively checked by `check_ap4.py`, including all nonzero differences. This establishes the theorem for all safe primes without assuming infinitude of safe primes.

## Originality — PASS, with residual risk

The motivating 2014 source (Cohen–Oliveira e Silva–Trudgian, arXiv:1410.6210) presents four-consecutive existence as a conjectural problem. Jarso–Trudgian (arXiv:2109.11691), inspected through theorem, algorithms and listed exceptional fields, proves unit-step existence for fields outside an explicit exception list, including safe primes at least \(47\), but neither asserts every prescribed nonzero difference nor supplies the count and its exact exceptional alignment. Scaling by an arbitrary difference can change multiplicative order, so this does not follow formally from unit-step existence. Carella (arXiv:1910.02308), inspected in its offset-configuration and Germain-prime portions, establishes broad asymptotic context; those inspected statements do not imply the sharp all-step threshold and exact formula. Overlap searches did not reveal equivalent published findings. This remains a best-knowledge comparison rather than proof of uniqueness; an unlocated theorem or a stronger general additive-pattern count is a genuine residual risk.

## Mathematical value — PASS

The result addresses a natural fixed-length primitive-root configuration for the highly structured but infinite potential family of safe-prime fields, strengthens existence from one fixed step to every possible step, identifies the precise first field where this uniform property starts, and records all counts by a natural elliptic quartic character sum with an explicit correction. It is structurally more than rephrasing the existing unit-step theorem: primitive-root status is not invariant under arbitrary multiplicative scaling. The finite calculation serves to close a rigorous character-sum reduction, not to present an unmotivated finite census.

## Limits

The result concerns prime fields only and does not settle arbitrary prime fields, higher-dimensional extensions, or longer progressions. Independent mathematical validation is not performed, and literature coverage may be incomplete.

Self-review: passed. Independent audit: not yet performed.
