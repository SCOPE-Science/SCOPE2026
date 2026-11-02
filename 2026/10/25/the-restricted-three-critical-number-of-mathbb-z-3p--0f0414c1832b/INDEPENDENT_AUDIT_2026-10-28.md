# Independent mathematical audit

## correctness

PASS

The CRT transforms Z_(3p) into Z3×Fp. The lower witness is all three first-coordinate classes times I=[0,(p+2)/3-1], with p+2 elements; any restricted triple with first residue 1 uses two distinct elements from a single class and one from the next, yielding second sum in [1,p-2] and missing (1,0),(1,p-1). For arbitrary size p+3, let fiber sizes a0+a1+a2=p+3. If all three nonzero, one from each gives all residue-0 targets by Cauchy–Davenport, and for residues 1,2 a strict cyclic fiber-size inequality (sum not divisible by 3) guarantees 2ai+aj-4>=p; Dias da Silva–Hamidoune restricted pairs plus Cauchy–Davenport fill the target class. If exactly one empty fiber, remaining ai+aj=p+3 forces both >=3; mixed restricted pairs cover the two nonzero residues, while the larger fiber M>=(p+3)/2 has 3M-8>=p, so restricted triples cover residue 0. No numerical extrapolation is used. As an independent boundary check all 352716 ten-subsets of Z21 were exhaustively confirmed covering; explicit p+2 lower witnesses tested for p=7,13,19,31. This does not prove other prime residue classes.

## originality

PASS

Best-of-knowledge PASS for proving the infinite odd-composite subfamily of Bajnok’s proposed restricted three-critical formula. Bajnok 2014 Section 7 Proposition 15 proves the relevant lower bound and states the exact general formula as a conjecture; his cited verification through n<=50 covers early instances, not this infinite family. Chen–Huang 2026 offers broader odd-group density bounds, strictly weaker than the exact p+3 threshold for p>=13. The sole new mathematical assertion is sharp upper coverage for all p=1 mod3 using a three-fiber argument.

## value

PASS

This resolves a natural infinite odd-composite subfamily of a published exact-value conjecture with a sharp obstruction at p+2 and matching universal coverage at p+3. The CRT three-fiber mechanism is a reusable additive-combinatorial argument; the result is stronger than general odd-order density estimates and is not merely repeating a small-prime calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
