# Independent mathematical audit

## correctness

PASS

Legendre/Kummer valuation gives v2(multinomial(n;k1,...,kL))=sum_{i>=1}c_i where c_i are binary carry integers, so valuation zero means carry-free digits and exactly L^{s2(n)} ordered tuples. Each odd multinomial squared contributes 1 mod 8. Valuation one means one outgoing carry c_{i+1}=1, forcing b_{i+1}=1, d_i=b_i+2, d_{i+1}=0, yielding precisely binom(L,b_i+2)L^{s-b_i-1} disjoint tuples. Their squares contribute 4; valuation>=2 vanishes mod 8. This gives the full formula. At even h>=4 all even multinomial powers vanish mod8. Lucas parity yields the odd/even-L simplifications, and for L=3 mod4 the independent b0 and upper-bit parity each occur 2^{k-2} times, distributing 1,3,5,7 equally for k>=2. n=0,L=1 are included; even-L residues zero when s>=3. Independent exact factorial enumeration of L<=6,n<=10,h in {2,4,6} gave 198 matches, plus dyadic census for L=3,7,11,15,k=2..9. These are finite checks only.

## originality

PASS

The sequence itself is Sun 2026 and was also studied as Abelian-square lattice-walk counts; these definitions and special Domb/binomial cases are not new. Sun proves prime-index-weighted sums modulo p, not each coefficient modulo eight. Beluhov 2025 gives strong 2-adic valuations of W_d(n)=binom(2n,n)S_d^(2)(n), which do not fix the unit residue among 1,3,5,7 or the exact dyadic distributions. The already-published SCOPE exceptional-branch theorem for Sun considers a weighted sum over n=1..p-1 mod p; its entire public RESULT.md was read and does not cover termwise mod 8. The all-level one-carry and exact finite-block four-class law remain new on the inspected evidence. Risk: Sun arXiv full v3 text was inaccessible this run (only detailed abstract), and authorized Oxford retrieval was blocked by VPN; this is explicitly not a whole-document noncoverage finding.

## value

PASS

The first modulus at which a *single* binary carry survives squaring is 8; the abrupt transition from height two to all larger even heights is mathematically structural. The theorem gives every term for all levels and indices, a uniform exact four-class equidistribution for every level 3 mod4 and sparsity for even levels. It is a motivated arithmetic classification of a published natural family, not a recomputation of the familiar Domb special case or a narrow arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
