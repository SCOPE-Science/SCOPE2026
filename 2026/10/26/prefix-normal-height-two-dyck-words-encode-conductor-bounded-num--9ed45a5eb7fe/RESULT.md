# Prefix-normal height-two Dyck words encode conductor-bounded numerical semigroups

## Finding

For each integer \(n\ge1\), there is a canonical **bijection** between binary Dyck words of semilength \(n\), maximum height at most two, and prefix normal with respect to the up-symbol \(0\), and numerical semigroups \(S\subseteq\mathbb N_0\) with conductor at most \(n\). Explicitly, if \(H(j)\) denotes the height after the first \(j\) symbols, the correspondence is
\[
 S(w)=\{0\}\cup\{i:1\le i<n,\ H(2i)=0\}\cup\{i:i\ge n\}.
\]
Thus the number of such words is the known numerical-semigroup cumulative count \(a(n-1)\) in OEIS A326083. For \(n=1,\ldots,14\) the counts are
\[
1,2,3,5,7,12,16,27,37,58,80,131,171,277.
\]
The bijection preserves three natural statistics: if \(g(S)\) is the number of positive gaps of \(S\), then exactly \(g(S)\) internal even-indexed Dyck heights equal two, and the path's sum-of-heights area \(\sum_{j=1}^{2n-1}H(j)\) is \(n+2g(S)\); the first return to zero occurs after \(2m(S)\) symbols, where \(m(S)\) is the multiplicity; and the conductor is one plus the last internal even-height-two index, or zero when none exists.

For each \(g\ge0\), let \(P_{n,g}\) count the words in the class with exactly \(g\) internal even-height-two vertices, and let \(N_g\) be the total number of numerical semigroups of genus \(g\). Then
\[
P_{n,g}=\#\{S:g(S)=g,\ c(S)\le n\},\qquad
P_{n,g}=N_g\quad(n\ge\max(1,2g)).
\]
For every \(g\ge1\), the stabilization bound \(n=2g\) is **sharp**: \(P_{2g-1,g}<N_g\). This gives a complete conductor-filtered genus classification of these constrained prefix-normal words.

## Assumptions and scope

A binary Dyck word \(w=w_1\cdots w_{2n}\) uses \(0\) for a height-increment of \(+1\) and \(1\) for \(-1\), with \(H(0)=H(2n)=0\), \(H(j)\ge0\), and \(\max_jH(j)\le2\). It is **prefix normal with respect to \(0\)** if, for every pair of integers \(\ell,a\) with \(0\le \ell\le2n\) and \(0\le a\le2n-\ell\), the substring of length \(\ell\) beginning immediately after position \(a\) has no more zeros than \(w_1\cdots w_\ell\). A numerical semigroup is a cofinite, addition-closed subset of \(\mathbb N_0\) containing zero. Its genus \(g\) is the number of nonnegative integers outside it; its conductor \(c\) is the smallest nonnegative integer above which every integer is included; its multiplicity \(m\) is the least positive included integer. For the full semigroup \(\mathbb N_0\), take \(g=c=0\) and \(m=1\).

All claims hold for every integer \(n\ge1\) and for all indicated genus values, not only for experimentally enumerated instances. There is no assertion here that the counting sequence of numerical semigroups, the abstract prefix-normal characterization, or the genus conductor bound is new.

## Proof

**1. Height-two encoding.** A Dyck path with height in \(\{0,1,2\}\) has \(H(2i+1)=1\) for \(0\le i<n\). Every internal even height \(H(2i)\), \(1\le i<n\), is independently either zero or two, and \(H(0)=H(2n)=0\). Conversely, these values yield unique valid successive up/down steps. Thus all height-two Dyck words are uniquely parametrized by the subset \(T=\{i\in\{1,\ldots,n-1\}:H(2i)=0\}\).

**2. Prefix normality becomes truncated addition closure.** Let \(Z(j)\) count zeros in the first \(j\) positions. Because each zero raises height by one, \(2Z(j)=j+H(j)\). Consequently the prefix-normal inequality for a substring \((a,a+\ell]\) is exactly
\[
H(a+\ell)-H(a)\le H(\ell).
\]
If \(\ell\) is odd, its right-hand side is one, whereas the left-hand side is at most one by height parity and the height-two restriction. If \(\ell\) is even and \(H(\ell)=2\), the inequality is automatic because all heights lie between zero and two. If \(\ell=2k\) and \(H(2k)=0\), parity makes the inequality automatic for odd \(a\), because both odd-index heights are one; at even starting positions \(a=2i\), its sole possible violation is \(H(2i)=0\) and \(H(2(i+k))=2\).

Therefore prefix normality holds precisely when
\[
\bigl(i,k\in T\cup\{0,n\},\ i+k<n\bigr)\implies i+k\in T\cup\{0\}
\]
with the operational interpretation that only \(1\le i,k<n\) are nontrivial; \(i=0\) gives an identity and \(k=n\) is outside the allowed sum range. More simply, \(T\cup\{0\}\) is **closed under sums strictly below \(n\)**. At a length \(2k\) with \(k=n\), there is no nontrivial starting position. This covers every quantifier of the original prefix-normal condition.

**3. Bijection.** Given the heights, set \(S=\{0\}\cup T\cup[n,\infty)\cap\mathbb Z\). It is cofinite and contains zero. Sums of elements with value at least \(n\) stay in the tail; sums less than \(n\) are covered by the closure condition in Step 2. Hence \(S\) is a numerical semigroup. Conversely, any semigroup of conductor at most \(n\) yields \(T=S\cap\{1,\ldots,n-1\}\), a sum-closed truncated set, so the unique height-two path constructed in Step 1 is prefix normal by Step 2. The two maps are inverse.

**4. Statistics and finite counts.** The positive gaps of \(S\) are precisely the integers \(i\) in \([1,n-1]\) with \(H(2i)=2\). There are \(n\) odd-indexed vertices of height one, and the internal even vertices contribute height \(2\) exactly at the gaps; this proves the area identity. Positive even-indexed returns occur exactly at indices of \(S\), and \(n\in S\); hence the first return time is \(2m(S)\). The maximum gap is the last lifted internal even index, with conductor one more than it; when there are no gaps, the conductor is zero. These identifications prove the genus-refined counting formula. The total number of truncated sum-closed subsets of \(\{1,\ldots,n-1\}\) is precisely A326083 at index \(n-1\), which also equals the count of numerical semigroups with conductor at most \(n\).

**5. Sharp stabilization.** Let \(S\ne\mathbb N_0\) have largest gap \(F=c(S)-1\) and \(g\) gaps. For each \(i\in\{0,\ldots,F\}\), at least one of \(i\) and \(F-i\) is a gap; if both belonged to \(S\), their sum \(F\) would belong to \(S\), a contradiction. Pairing these \(F+1\) numbers gives \(2g\ge F+1=c(S)\). Thus every genus-\(g\) semigroup satisfies \(c(S)\le2g\) for \(g\ge1\), proving stabilization. For each \(g\ge1\), the semigroup \(S_g=\langle 2,2g+1\rangle=\{0,2,4,\ldots\}\cup\{2g+1,2g+3,\ldots\}\) has gaps \(1,3,\ldots,2g-1\), genus \(g\), and conductor \(2g\). It is absent from \(P_{2g-1,g}\) but present in \(P_{2g,g}\), proving sharpness. The genus-zero case has the unique semigroup \(\mathbb N_0\), present for every \(n\ge1\).

## Verification

The standalone Python 3 checker `verify.py` constructs all height-two Dyck paths for semilengths \(1\) through \(14\) from independent even-height choices (\(16{,}383\) paths), applies the **original substring prefix-normal predicate** without assuming the theorem, and compares it with a separate brute-force semigroup sum-closure test. It checks both inverse counting signatures, genus, conductor, multiplicity, and area; verifies OEIS A326083 counts through index \(13\); and tests sharp genus stabilization through genus \(7\). Run `python3 verify.py`, whose successful completion prints `HEIGHT_TWO_PREFIX_NORMAL_SEMIGROUP_PASS`. The proof above, not the finite tests, establishes the infinite claims.

## Relationship to prior work

Fici and Lipták (2018, arXiv:1805.12405), *On Prefix Normal Words*, introduced the requisite prefix-normal language and provided the general prefix-count inequality (Proposition 1). Their work does not state the height-two Dyck restriction or the resulting numerical-semigroup bijection. Bras-Amorós and de Mier (2007), and Ferrari, Giannini and Pinzani (2022, DOI:10.2478/puma-2022-0029), develop a **different** numerical-semigroup-to-Dyck-path encoding: a genus-\(g\) semigroup maps injectively into a path of semilength \(g\) using membership at consecutive integers. Their published correspondence is not the conductor-bounded, height-two, prefix-normal bijection here. OEIS A326083 has the cumulative sum-closed-subset **counts** already; these numbers are explicitly treated as known, not as a new integer sequence. The new statement is the exact word-language equivalence with statistic transport and the sharp genus-filtered stabilization. These comparisons do not exclude an uncatalogued equivalent theorem.

## Limitations

The bijection is restricted to Dyck words of maximum height at most two and to prefix normality with respect to the symbol \(0\). No formula for unrestricted prefix-normal Dyck words is claimed. The genus counts \(N_g\) are imported as well-defined numerical-semigroup counts rather than given a new closed form; their general enumeration remains difficult. The ordinary conductor-genus inequality and the OEIS sequence are prior knowledge. Finite verification through semilength \(14\) alone does not certify the all-length result, which follows from the proof. An independent mathematical audit has not been performed, and equivalent results under alternate additive-language terminology may exist.

## References

1. G. Fici and Z. Lipták, *On Prefix Normal Words* (first public 2018-05-31), arXiv:1805.12405, https://arxiv.org/abs/1805.12405 .
2. L. Ferrari, A. Giannini and R. Pinzani, *Classes of Dyck Paths Associated with Numerical Semigroups*, Pure Mathematics and Applications 30 (2022), 110–119, DOI:10.2478/puma-2022-0029, https://doi.org/10.2478/puma-2022-0029 .
3. M. Bras-Amorós and A. de Mier, *Representation of Numerical Semigroups by Dyck Paths*, arXiv:math/0612634, https://arxiv.org/abs/math/0612634 .
4. OEIS Foundation, A326083, *Number of subsets of {1..n} containing all of their pairwise sums <= n*, https://oeis.org/A326083 .
