# Independent mathematical audit

## correctness

PASS

For K_n corona K_1 (n>=2), when at least one core vertex is labeled 2, admissible core-leaf local patterns give T=x+3x^2+2x^3+x^4, and subtracting U=x+2x^2+x^3 removes all core-2-free assignments. When no core is 2, only local pairs (0,2),(1,1),(1,2) occur, giving V=2x^2+x^3. Thus R=T^n-U^n+V^n for every n>=2. The minimum n+1 has exactly n labelings, one core 2, its private leaf 0, all other cores 0 and their leaves 1. Direct exhaustive enumeration n=2..5 yields total 42,306,2226,16026, agrees 7^n-4^n+3^n and all coefficients. In particular it rigorously contradicts the earlier published Theorem 3.7, whose n=4 specialization totals 1161 instead of 2226.

## originality

PASS

Critical correction to the source package: 2021 Gangabylaiah et al. Theorem 3.7 (p.364), contrary to RESULT.md self-review, explicitly states an all-weight formula for EXACTLY K_n corona K_1 when n>=3. Its displayed sum is NOT correct under its own Roman domination definition: at n=4 it evaluates to 1161, whereas direct enumerated 3^8 labelings produce 2226, and the complete case-split proves the new formula. Thus the earlier same-graph claim does NOT imply the corrected exact polynomial, and the valid correction plus n=2 boundary remain original best-of-knowledge. The false omission of that source in current RESULT/REVIEW/AUDIT prevents publication until complete bibliographic correction; this private assessment does not misrepresent the original article.

## value

PASS

Correcting an explicit incorrect coefficientwise formula for a canonical corona family is substantive graph-polynomial value: the correction changes the exact count at n=4 by 1065, supplies an all-n necessary-and-sufficient structural case split and sharp minimum multiplicities. This is more than simply substituting parameters into a known valid polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
