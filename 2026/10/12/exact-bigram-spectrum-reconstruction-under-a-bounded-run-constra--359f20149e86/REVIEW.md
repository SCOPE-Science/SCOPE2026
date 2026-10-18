# Independent mathematical audit

## correctness

PASS

Frozen RESULT.md d3b07698dfcd6e4a7f250945cf0c8609b917f0af uses transition imbalance u−v∈{−1,0,1}, alternating run numbers, and bounded composition counts B_h(r,k) to count each fiber exactly. For balanced u=v=m, two endpoint cases give B(m+1,a)B(m,b)+B(m,a)B(m+1,b); imbalanced transitions give B(m+1,a)B(m+1,b). Feasible profile rectangles yield exact all-h GF; geometric-sum simplification yields rational expression. At h=2, singleton binomial endpoints give the stated divisibility/residue formula. Inspecting verify_identity.py reveals an exact cleared-denominator polynomial equality for infinite period-12 coefficients, not merely sample enumeration. Independent enumeration of all 2^n binary words n=1..12 with cap h=2 confirmed period-12 M formula, and compared known unrestricted capacity profile; algebraic run decomposition supports all n,h. The h=1 limiting case and n=1 exceptional fiber are handled.

## originality

PASS

Resultary published 2026-10-04 exact UNRESTRICTED binary read-two profile count and singleton classification, which establishes the same endpoint-flow method but does not imply a nontrivial bounded-run h parameter, its rational GF and h=2 congruence singleton law. Kiah et al DNA profile codes and Jacquet et al Markov type enumeration also use profile counts but do not state the exact bounded maximal-run formulas in inspected portions.

## value

PASS

Run-length limits are natural sequence-constraint models for storage channels and run-length-limited coding. An exact admissible-profile capacity, explicit representatives, asymptotic profile loss, and sharp distinction between coded reconstructibility and individual uniqueness give researchers precise channel invariants for every cap h; the h=2 singleton zero congruence is particularly informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
