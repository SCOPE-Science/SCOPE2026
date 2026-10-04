# Central-window local limit theorem for 2-bridge knot signatures
## Finding
Let \(K(c)\) be the set of \(c\)-crossing 2-bridge knots with the convention used by Baker--Cohen--Dam--Felber--Madras--Saha--Thackrah, and let \(k(c,2n)\) denote the number having signature \(2n\). Define
\[
\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}.
\]
Then for every fixed \(A>0\),
\[
\sup_{|2n|\le A\sqrt c}
\left|
\frac{\sqrt c}{2}\frac{k(c,2n)}{|K(c)|}
-\phi\!\left(\frac{2n}{\sqrt c}\right)
\right|\longrightarrow0
\qquad(c\to\infty).
\]
Thus the signature distribution satisfies a uniform local central limit theorem throughout every bounded central window, not only the cumulative central limit theorem proved in the source.

In particular, for every fixed integer \(r\),
\[
\frac{k(c,2r)}{|K(c)|}
\sim\sqrt{\frac{2}{\pi c}},
\]
and since \(|K(c)|\sim 2^{c-3}/3\),
\[
k(c,2r)
\sim
\frac{2^{c-3}}{3}\sqrt{\frac{2}{\pi c}}.
\]
The same leading asymptotic therefore holds for every fixed even signature, including signature zero.

## Assumptions and scope
The set \(K(c)\), the proxy multiset \(T(c)\), and the functions \(k(c,\sigma)\) and \(s(c,\sigma)\) are exactly those of the 2026 source. The source counts signature values on the even lattice and proves a global central limit theorem after scaling signature by \(\sqrt c\).

The argument uses only the source's exact formulas for \(s(c,2n)\), its exact formulas for \(|K(c)|\) and \(|T(c)|\), its relation
\[
2|K(c)|=|T(c)|+|T_p(c)|,
\qquad
2k(c,2n)=s(c,2n)+s_p(c,2n),
\]
and the standard local De Moivre--Laplace estimate for a fair binomial law.

The local theorem is asserted only on windows \(|2n|\le A\sqrt c\) for fixed \(A\). No moderate- or large-deviation estimate is claimed.

## Proof
First consider even crossing number \(c=2m\). The source proves
\[
s(2m,2n)=
\sum_{i=0}^{m-|n|-2}
\binom{2m-4-2i}{m+n-2-i}.
\]
Put
\[
N_i=2m-4-2i,
\qquad
q_N(d)=2^{-N}\binom{N}{N/2+d}
\]
when the binomial coefficient is defined. Then
\[
\frac{s(2m,2n)}{|T(2m)|}
=
\sum_i w_{m,i}q_{N_i}(n),
\qquad
w_{m,i}=\frac{2^{N_i}}{|T(2m)|}.
\]
Because
\[
|T(2m)|=\frac{2^{2m-2}-1}{3},
\]
for each fixed \(i\),
\[
w_{m,i}\longrightarrow\frac34\,4^{-i},
\]
and these limiting weights sum to one.

The local De Moivre--Laplace estimate, obtained uniformly on bounded standardized windows from Stirling's formula, is
\[
q_N(d)=
\sqrt{\frac{2}{\pi N}}
\exp\!\left(-\frac{2d^2}{N}\right)
\left(1+o(1)\right)
\]
uniformly when \(|d|\le B\sqrt N\) for fixed \(B\). Therefore, for every fixed \(i\) and uniformly in \(|2n|\le A\sqrt{2m}\),
\[
\frac{\sqrt{2m}}{2}q_{N_i}(n)
-
\phi\!\left(\frac{2n}{\sqrt{2m}}\right)
\longrightarrow0.
\]

It remains to justify summing over \(i\). For a fair binomial distribution, its maximal point mass is at most \(C/\sqrt N\) for an absolute constant \(C\). For \(i\le m/2\), this gives
\[
\frac{\sqrt{2m}}{2}q_{N_i}(n)\le C'
\]
uniformly in \(n\). Meanwhile \(w_{m,i}\) is bounded by a constant times \(4^{-i}\). Hence the tail after any fixed \(I\) is uniformly controlled by a geometric series. For \(i>m/2\), the total weight itself is exponentially small. The moving upper limit \(m-|n|-2\) removes only such exponentially small weights when \(|n|=O(\sqrt m)\). Dominated convergence for this geometric mixture proves
\[
\sup_{|2n|\le A\sqrt{2m}}
\left|
\frac{\sqrt{2m}}{2}
\frac{s(2m,2n)}{|T(2m)|}
-
\phi\!\left(\frac{2n}{\sqrt{2m}}\right)
\right|\to0.
\]

Now let \(c=2m+1\). Except for the source's additive \(1\) when \(n=1\), its formula is
\[
s(2m+1,2n)=
\sum_i
\binom{2m-3-2i}{m+n-3-i}.
\]
Here the binomial row has length
\[
N_i=2m-3-2i
\]
and the lower index differs from \(N_i/2\) by \(n-3/2\). Also
\[
|T(2m+1)|=\frac{2^{2m-1}+1}{3},
\]
so the same limiting geometric weights \((3/4)4^{-i}\) occur. The identical local-binomial and geometric-tail argument gives a Gaussian with argument shifted by \(3/\sqrt c\). On every fixed central window this shift tends uniformly to zero, and the exceptional additive \(1\) contributes only \(O(2^{-c})\). Thus
\[
\sup_{|2n|\le A\sqrt{2m+1}}
\left|
\frac{\sqrt{2m+1}}{2}
\frac{s(2m+1,2n)}{|T(2m+1)|}
-
\phi\!\left(\frac{2n}{\sqrt{2m+1}}\right)
\right|\to0.
\]

Finally transfer from \(T(c)\) to \(K(c)\). Write \(T_p(c)\) for the palindromic subset. From the source identities,
\[
\left|
\frac{k(c,2n)}{|K(c)|}
-
\frac{s(c,2n)}{|T(c)|}
\right|
\le
2\frac{|T_p(c)|}{|T(c)|}.
\]
The exact formulas for \(|K(c)|\) and \(|T(c)|\) give
\[
|T_p(c)|=2|K(c)|-|T(c)|=O(2^{c/2}),
\qquad
|T(c)|\asymp2^c.
\]
Hence the right side is \(O(2^{-c/2})\), even after multiplication by \(\sqrt c\). This proves the asserted local limit theorem for \(K(c)\).

For fixed \(r\), substitute \(n=r\). Since \(2r/\sqrt c\to0\) and \(2\phi(0)=\sqrt{2/\pi}\), the fixed-signature asymptotic follows. The source's exact enumeration gives \(|K(c)|\sim2^{c-3}/3\), yielding the final counting formula.

## Verification
The primary source was inspected at Theorems 1.1 and 1.2, the exact cardinality formulas for \(K(c)\) and \(T(c)\), the definition and size relation for the palindromic subset, and the proof transferring its cumulative central limit theorem from \(T(c)\) to \(K(c)\). It states primary MSC \(57K10\) and is dated 2026-04-22.

The local step was reconstructed independently from Stirling's formula. The key boundary checks are: lattice spacing is \(2\), giving the prefactor \(\sqrt c/2\); the geometric mixture weights converge to \((3/4)4^{-i}\), whose total is exactly one; the odd-row center shift is bounded and therefore disappears on the \(\sqrt c\) scale; and the palindromic correction is exponentially smaller than a local mass of order \(c^{-1/2}\).

The bundled finite regression checks the source's exact rows, the palindromic-size correction, and numerical convergence of both parity subsequences. It prints:

`VERIFY_OK even_errors=0.00860810,0.00422818,0.00209576,0.00104337 odd_errors=0.07352973,0.05164790,0.03645998,0.02573190 palindromic_ratio_checked_c20_to120=true`

Those finite calculations are not the infinite proof.

## Relationship to prior work
Baker--Cohen--Dam--Felber--Madras--Saha--Thackrah prove the cumulative central limit theorem
\[
\frac{k(c,\le t\sqrt c)}{|K(c)|}\to\Phi(t)
\]
and derive exact binomial-sum formulas for each lattice mass. Their proof uses the cumulative De Moivre--Laplace theorem. The paper does not state a local central limit theorem, a uniform point-mass asymptotic on bounded central windows, or the fixed-signature asymptotic above.

Earlier work of Cohen--Lowrance--Madras--Raanes derives recurrences and consecutive-row binomial identities and computes the average absolute signature. Several fixed columns of the proxy signature triangle are catalogued in OEIS, but those records do not supply the uniform knot-theoretic local limit over \(K(c)\).

Targeted searches for `2-bridge` together with `local central limit`, `fixed signature asymptotic`, `signature zero asymptotic`, and equivalent point-probability formulations did not locate a prior statement. The global central limit theorem does not imply this result: weak convergence of rescaled lattice distributions does not control individual lattice masses at order \(c^{-1/2}\).

## Limitations
The theorem is local only in bounded \(\sqrt c\)-scale windows. It does not provide a moderate-deviation expansion, a uniform estimate over the full signature range, or an explicit convergence rate.

The proof uses the exact combinatorial formulas specific to 2-bridge knots and does not assert a local limit theorem for other random-knot models.

The primary source is a 2026 preprint. A later revision or an unindexed note could independently add the same local refinement.

## References
1. C. Baker, M. Cohen, H. Dam, R. Felber, N. Madras, R. Saha, and D. Thackrah, *A central limit theorem for the signatures of 2-bridge knots*, arXiv:2604.21107v1, first posted 2026-04-22.
2. M. Cohen, A. M. Lowrance, N. Madras, and S. Raanes, *Average signature and 4-genus of 2-bridge knots*, arXiv:2406.17738, 2024.
3. The On-Line Encyclopedia of Integer Sequences, entries A006134, A057552, A371964, A079309, and A371965, fixed columns cited by the 2026 source.
