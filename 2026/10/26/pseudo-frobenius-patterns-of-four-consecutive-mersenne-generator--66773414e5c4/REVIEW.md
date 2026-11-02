# Independent mathematical audit

## correctness

PASS

For a=2^m−1 and S=<a,2a+1,4a+3,8a+7>, the coin count C(r) for denominations {1,3,7} has exact minimal greedy form floor(r/7)+floor((r mod7)/3)+(r mod7 mod3). The weight W(r)=a(r+C(r))+r gives the full Apéry set for 0<=r<a because the normalized weight is strictly increasing; C(r+7)=C(r)+1 forces all PF residues into the final seven r values. Testing addition by all three non-a generators and modular wrap produces PF={F,F−1,F−2} if m mod3=1 and PF={F,F−4(a+1)} if m mod3=2, with the stated exact F formulas. Independently recomputed shortest-path Apéry sets and generator membership for all five exponents m=5,7,8,10,11 (m<=11,m mod3≠0); these finite cases corroborate the full all-m Apéry/last-seven-residue proof.

## originality

PASS

Komatsu arXiv:2209.13118 already studies four-generator Apéry/Frobenius formulas, and Liu–Xin–Ye–Yin arXiv:2306.03459 Theorem 3.4 supplies PF for a multiple of seven (m divisible3), the explicitly excluded branch. Their Theorem 6.1 covers Frobenius and genus for a≡3 mod7, including m mod3=2, but does not state the exact two-entry PF set. The inspected full text and relevant published records did not give either remaining branch PF/type formula. This is best-of-knowledge originality restricted to exact PF patterns; the greedy Apéry foundation, Frobenius values, and excluded m divisible3 branch are prior and not claimed novel.

## value

PASS

The complete two-branch PF classification of a naturally truncated Mersenne-generator family determines its Cohen–Macaulay type 3 versus 2 and exact nonconsecutive gaps in one residue class. Such type and maximal-gap data are natural unknown invariants not supplied by published F/genus values alone, and may be reused in semigroup-ring or almost-symmetric analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
