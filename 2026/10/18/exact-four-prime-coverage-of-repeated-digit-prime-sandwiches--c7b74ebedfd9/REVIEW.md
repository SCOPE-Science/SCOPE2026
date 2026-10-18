# Scientific review: exact four-prime coverage of repeated-digit prime sandwiches

## Correctness — PASS

The identity for the repeated-digit sandwich is exact. For every prime in the nontrivial covering set, both powers of ten and repunits repeat modulo that prime with a period dividing six; thus six padding lengths and six core-length residues exhaust the genuinely infinite parameters. Even and final-5 digits are eliminated directly. The complete \(3003\)-residue classification was computed two independent ways: exact integer sandwich evaluation and prime-local bitmask intersection. They agree on all six rows. The logarithmic and upper/lower natural densities follow from one residue class in each odd digit length. This is a finite arithmetic certificate attached to an infinite modular reduction, not extrapolation from sampled large integers.

## Originality — PASS, with residual risk

Wu (arXiv:1503.08883, first public 2015-03-31) introduced the sandwich operation, proved the even-length/\(11\) family, exhibited \(231,420,759\), and provided a sufficient repunit-gcd procedure. The OEIS A090287 entry records these facts. Neither inspected source explicitly gives the complete \(\{3,7,11,13\}\) residue spectrum over all lengths or the exact densities of odd-length, non-\(11\) certified exceptions. Searches for residue-class reformulations, the specific modulus and classes, and density statements found no matching published theorem. The new result is not an assertion that the known seeds or the general covering test are new. The possibility of another published equivalent classification or the perception that evaluation of Wu's finite test is routine remains a real residual risk.

## Value — PASS

The four odd-prime obstructions are canonical and irredundant for the historical \(231\) example among factors of the six-digit repunit. Their complete joint spectrum identifies how far this low-prime explanation reaches, exactly, without appealing to open primality questions. It turns isolated exceptional examples into a precise family with positive lower natural density even outside the elementary even-length multiple-of-\(11\) mechanism, and determines its upper density and logarithmic density. The result does not classify all prime-free centers.

## Limits and closest prior literature

The coverage result depends on the fixed small-prime certificate, and other prime factors may certify additional cores. Wu's general gcd test is stronger as a search method, while the present classification and density statements are a closed evaluation of a motivated minimal covering subsystem. Independent assessment of originality and scientific utility remains outstanding.

Self-review: passed. Independent audit: not yet performed.
