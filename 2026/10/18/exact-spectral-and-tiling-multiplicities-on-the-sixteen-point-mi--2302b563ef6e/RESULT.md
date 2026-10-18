# Exact spectral and tiling multiplicities on the sixteen-point mixed cyclic group

## Finding
Let \(G=\mathbb Z_8\times\mathbb Z_2\). For each nonempty \(A\subseteq G\), let \(s(A)\) count all sets \(B\subseteq\widehat G\) such that \(\{\chi_b:b\in B\}\) is an orthogonal basis for complex functions on \(A\), and let \(t(A)\) count all \(C\subseteq G\) such that \(A\oplus C=G\). Both counts distinguish actual subsets, without quotienting translations.

Exactly \(1611\) of the \(65535\) nonempty subsets are spectral, and these split into exactly \(43\) orbits under the \(256\)-element affine group. The exhaustive size profile is:

| \(|A|\) | Spectral subsets | Affine orbits |
| ---: | ---: | ---: |
| \(1\) | 16 | 1 |
| \(2\) | 120 | 5 |
| \(4\) | 732 | 17 |
| \(8\) | 742 | 19 |
| \(16\) | 1 | 1 |

No subset of any other cardinality is spectral. The **complete** nonzero multiplicity distributions are:

| \(|A|\) | \(s(A)\colon\#A\) | \(t(A)\colon\#A\) |
| ---: | --- | --- |
| \(1\) | \(16:16\) | \(1:16\) |
| \(2\) | \(16:64,\ 32:32,\ 64:24\) | \(4:64,\ 16:32,\ 256:24\) |
| \(4\) | \(4:384,\ 8:160,\ 16:32,\ 32:112,\ 64:32,\ 256:12\) | \(4:384,\ 8:160,\ 16:112,\ 32:32,\ 64:32,\ 256:12\) |
| \(8\) | \(2:672,\ 4:56,\ 16:8,\ 256:6\) | \(8:672,\ 16:56,\ 32:8,\ 64:6\) |
| \(16\) | \(1:1\) | \(16:1\) |

For \(|A|=4\), exactly \(1088\) sets have \(s(A)=t(A)=0\); for \(|A|=8\), exactly \(12128\) do. Every remaining non-divisor cardinality has \(s(A)=0\). In particular, for \(|A|=4\), the joint pairs \((s(A),t(A))=(16,32)\) and \((32,16)\) occur respectively \(32\) and \(112\) times: qualitative equivalence of spectrality and tiling does not equate numbers of bases and complements. A complete list of representatives of the \(43\) affine orbits and their exact two multiplicities appears in `census.json`.

## Assumptions and scope
Identify \((x,y)\in G\), where \(0\le x<8\), \(0\le y<2\), with the integer \(x+8y\) from \(0\) to \(15\). Identify the dual via \(\chi_{(u,v)}(x,y)=\zeta_8^{ux+4vy}\), \(\zeta_8=e^{2\pi i/8}\). Spectra, bases and tiling complements are counted as unordered subsets; multiplying characters by a global character or translating complements creates a distinct subset when it changes the subset itself. The empty subset is excluded. These are exact finite statements for this group only, with no assertion about other groups.

## Proof
**Cyclotomic zero criterion.** For a subset \(A\), let \(Z(A)\subseteq G\setminus\{0\}\) be the nontrivial characters with \(\sum_{a\in A}\chi_g(a)=0\), and let \(D(A)=(A-A)\setminus\{0\}\). For each \(g=(u,v)\ne0\), form the eight integer counts
\[
c_j=\#\{(x,y)\in A:ux+4vy\equiv j\pmod 8\},\qquad 0\le j<8.
\]
Because the minimal polynomial of \(\zeta_8\) over \(\mathbb Q\) is \(X^4+1\), its polynomial of degree at most seven vanishes precisely when \(c_j=c_{j+4}\) for all \(0\le j<4\). This is an integer test with no numerical tolerances.

**Exact count identities.** Orthogonality of distinct restricted characters is equivalent to \(D(B)\subseteq Z(A)\), with \(|B|=|A|\) ensuring completeness. Direct-sum tiling is equivalent to \(D(A)\cap D(C)=\varnothing\) and \(|A|\,|C|=16\). Let
\[
h_k(d)=\#\{B\subseteq G:|B|=k,\ D(B)=d\},\quad H_k(z)=\sum_{d\subseteq z}h_k(d).
\]
Represent \(d,z\subseteq G\setminus\{0\}\) as 15-bit masks. Then
\[
s(A)=H_{|A|}(Z(A)),\qquad
 t(A)=H_{16/|A|}((G\setminus\{0\})\setminus D(A))
\]
whenever \(|A|\) divides 16. All values of \(H_k\) are obtained exactly by the Boolean-lattice recursion \(H_k(z)\leftarrow H_k(z)+H_k(z\setminus\{g\})\) for each set bit \(g\) in ascending coordinate order, starting from \(h_k\). The enumeration runs over every one of the \(2^{16}-1=65535\) nonempty masks and all \(k=1,\ldots,16\); for non-divisor cardinalities the computed \(s(A)\) values are all zero. The formulas prove every numeric distribution in the tables, rather than treating a sample as exhaustive.

**Affine classification.** Every automorphism sends the order-eight generator \((1,0)\) to \((a,b)\) with odd \(a\in\{1,3,5,7\}\), \(b\in\mathbb Z_2\); the order-two generator \((0,1)\) must go to \((c,1)\) with \(c\in\{0,4\}\). These \(4\cdot2\cdot2=16\) choices are precisely all group automorphisms, because \(4(a,b)=(4,0)\) and the second image must lie outside the first image's cyclic subgroup. Combining with 16 translations gives 256 affine transformations. For each spectral mask, enumerate its 256 images and remove its entire orbit. The resulting orbits have sizes and invariant multiplicities recorded individually in `census.json`; their cardinalities add up to the corresponding counts above, and their numbers by subset size are \(1,5,17,19,1\).

## Verification
Run `python3 verify.py > reproduced.json`, then compare `reproduced.json` byte-for-byte with `census.json`. The executable uses Python's built-in integer arithmetic only. Its output reports every frequency-zero count, spectra-count histogram, tiling-count histogram, and affine representative. An additional direct test enumerates all proposed spectral bases for every spectral subset of sizes \(2,4,8\) and agrees with the zeta-transform calculation. The group difference-mask recurrence is also compared to direct pair subtraction on deterministic test subsets. The output contains the full \(43\)-representative certificate. This is exhaustive verification of a finite assertion, not a numerical extrapolation.

## Relationship to prior work
Malikiosis (2020 preprint) studies the spectral/tiling relation and roots-of-unity methods for cyclic groups; its cyclic group theorems do not identify the present noncyclic order-16 counts. Zhang (2021 preprint; 2023 journal paper), Theorem 1.5, proves that in **all** groups \(\mathbb Z_p\times\mathbb Z_{p^n}\), including the present \(p=2,n=3\), spectrality is equivalent to translational tiling. Thus **that qualitative equivalence is prior art and not a claim of novelty here**. The precise count \(1611\), the \(43\) affine classes and the spectra/tiling-complement multiplicity profiles are the subject of the present finite classification. Related available scientific tables cover distinct order-16 groups \(\mathbb Z_4^2\) and \(\mathbb Z_4\times\mathbb Z_2^2\), not this mixed exponent-eight group; group order alone does not transfer the table entries.

## Limitations
Originality is a literature-based assessment rather than an absolute priority certificate; an unindexed historical table could contain the same figures. The result applies only to \(\mathbb Z_8\times\mathbb Z_2\). The table classifies affine orbit representatives and pair counts, but does not furnish a uniform formula for larger \(\mathbb Z_{2^n}\times\mathbb Z_2\). No statement of independent validation or publication is made.

## References
1. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800, first submitted 2020-05-12; *Forum of Mathematics, Sigma* 10 (2022), e23. https://arxiv.org/html/2005.05800v3
2. T. Zhang, *Fuglede's conjecture holds in \(\mathbb Z_p\times\mathbb Z_{p^n}\)*, arXiv:2109.08400, first submitted 2021-09-17; *SIAM J. Discrete Math.* 37 (2023), 1180–1197. https://arxiv.org/html/2109.08400v3
3. Related public exact classification records for the nonisomorphic groups \(\mathbb Z_4^2\) and \(\mathbb Z_4\times\mathbb Z_2^2\), indexed in https://github.com/published-finding corpus/2026 . Their indexed conclusions are used only for mathematical comparison of objects, not as a proof for the present group.
