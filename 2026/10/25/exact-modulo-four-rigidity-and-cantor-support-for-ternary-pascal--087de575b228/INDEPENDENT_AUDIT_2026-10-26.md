# Independent mathematical audit

## correctness

PASS

Lucas digit factorization for residues c_j=C(n,j) mod3 and parity (-1)^j factors the signed nonzero-indicator U and quadratic character V over ternary digits. Digit values 0,1,2 contribute local (U,V) factors (1,1),(0,0),(1,3). Therefore alternating sum A=(3U−V)/2 equals 0 if any 1 digit and (3−3^r)/2 otherwise, with r number of digit twos. Since 3^j≡(−1)^j mod4, T(n)≡A mod4, equal 1 iff only digits 0,2 and r even; never 2 or 3. Even parity words count 2^(k−1) on 0<=n<3^k; product generating series and Θ(X^log_3 2) follow. Independent checks: Independently generated and tested 1100 Pascal rows modulo 3 using a recurrence and compared signed sums with Lucas factorization and T(n) modulo 4; all matched. Inspected actual verifier.py Git blob 4624099d52b889870ba68b2eb2f976f0cf41ee80. Verified separately why division by 2 must occur before reducing mod4 (uses 3^r mod8); finite tests do not prove arbitrary n.

## originality

PASS

Mathonet–Rigo–Stipulanti–Zénaïdi arXiv:2201.06636 defines identical base-3 Pascal-row number and develops Lucas digit recurrences; inspected 24-page lawful institutional/open PDF, especially defining introduction and Lucas/digital sections, and found no statement of exact modulo-4 digit-parity criterion. OEIS A173019 explicitly already records the weaker implication 2|a(n)=>4|a(n), so absence of residues 2 must NOT be claimed fully new on its own; the exact residue-one digit classification and fractal count are the surviving original result. Residual limits explicitly listed in originality.residual_risks.

## value

PASS

Determines every parity/residue-four outcome in a canonical studied digital sequence, identifying its precise Cantor-language support and exponent log_3 2. The digit classification strengthens a recorded parity observation by classifying all rows and counting their rare residue-one indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
