# Independent mathematical audit

## correctness

PASS

For omega(n)=3 and Omega(n)=4 the only exponent pattern is (2,1,1). Odd support cannot be 2-near-perfect: sigma(n)/n<= (13/9)(6/5)(8/7)=624/315<2. For even n, prime ordering reduces to 4pq,2p²q,2pq². Reconstructed sigma(n)-2n formulas (7-p)q+7(p+1), (3+3p-p²)q+3(p²+p+1), (3-p)q²+3(p+1)(q+1); positivity, q divisibility, and distinct-divisor sums bound candidates to a finite set. An independent exact divisor-pair enumeration of all numbers <=1000 satisfying omega=3 and Omega=4 reproduced precisely ten asserted n and unique omitted pairs; infinite exclusions follow from inequalities, not finite search. The candidate enumerator in verify.py checks every remaining finite prime pair and distinct omitted-divisor pair.

## originality

PASS

Fearon et al. 2025/2026 full primary text Section 6.2 lists initial three-prime examples and poses families with three prime supports as future work; its theorems classify only two-prime support. Aryan et al. 2024 similarly handle 2^k p^m. Published SCOPE squarefree 2pq case has Omega=3 and is disjoint. An existing 2p²q classification does cover four of the ten examples but cannot imply the six 4pq cases or absence of 2pq² and odd forms. OEIS A341475 enumerates examples, not the unconditional exclusion theorem.

## value

PASS

The smallest nonsquarefree three-prime-support layer is a motivated next classification after squarefree and two-prime-support work; exact ten-element solution with unique omitted pairs closes that natural exponent stratum rather than extracting arbitrary instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
