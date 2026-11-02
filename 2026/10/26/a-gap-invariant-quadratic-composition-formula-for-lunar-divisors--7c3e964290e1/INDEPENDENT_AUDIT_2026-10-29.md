# Independent mathematical audit

## correctness

PASS

For binary Boolean multiplication, support of W_hn occupies residues 0 and 1 mod h. For h>=3, if both factors contain a residue-1 term, their sum forces forbidden residue 2; thus one factor is pure residue 0. For a degree n-b support, convolution with a full width-b window covers Q_n iff its ordered gaps are <=b, counted by c_b(n-b). Pure factors contribute one c_b, mixed factors two independent rows contribute c_b^2, summed over b=1..n. All n>=1 and h>=3; h=2,n=2 yields 5 instead of 4. An independently written support-subset enumerator verified all h=3,4,5 and n=1..5, plus the boundary; finite cases do not prove the universal formula.

## originality

PASS

Compared Applegate–LeBrun–Sloane 2011 complete primary Section 6 Theorems 12,14; those treat all-ones binary targets and the one-hole family, providing a bounded-composition lemma but not the periodic two-residue support count or the quadratic sum. Resultary search for Boolean semiring/dismal/lunar aliases gave no equivalent indexed theorem. Classical single-row counting is acknowledged, while the residue-exclusion and two-row decomposition are additional arguments.

## value

PASS

A natural, explicitly defined periodic family of Boolean-polynomial targets has an exact divisor enumeration invariant under arbitrary gaps >=3, with a sharp failure at gap2. The extra quadratic term measures simultaneous factor coverage of two residue rows; it is a structurally motivated extension, not mere reprinting of the known all-ones counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
