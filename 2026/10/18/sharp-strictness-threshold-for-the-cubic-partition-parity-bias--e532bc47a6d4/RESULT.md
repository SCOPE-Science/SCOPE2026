# Sharp strictness threshold for the cubic partition-parity bias

## Finding
Let \(E_3(n)\) and \(O_3(n)\) count partitions of the nonnegative integer \(n\) into positive integer cubes with an even and odd number of parts, respectively; the empty partition has zero parts. Set
\[
A_3(n)=(-1)^n(E_3(n)-O_3(n)).
\]
Then \(A_3(n)\ge0\) for all \(n\ge0\), and its complete zero set is
\[
\{8,9,10,11,12,13,14,15,24,25,26,40,41,42,67,68,69,
94,95,96,121,122,123\}.
\]
In particular, \(A_3(n)>0\) for every \(n\ge124\). The strictness threshold \(124\) is optimal, because \(A_3(123)=0\).

## Assumptions and scope
Partitions are unrestricted multisets of parts from \(\{m^3:m\ge1\}\), with integer \(m\); the sign refers to the parity of the number of parts, while the compensating factor is \((-1)^n\). The claim covers all \(n\ge0\), not just an asymptotic range. All identities below are identities of formal power series with integer coefficients.

## Proof
**Step 1: nonnegative subset representation.** Put \(G(q)=\sum_{n\ge0}A_3(n)q^n\). By the signed partition product,
\[
G(q)=\prod_{m\ge1}\frac{1}{1+(-q)^{m^3}}.
\]
Write each positive integer uniquely as \(m=2^a u\), where \(u\) is odd and \(a\ge0\). For a fixed odd \(u\), set \(z=q^{u^3}\). The associated factors give
\[
\frac{1}{1-z}\prod_{a\ge1}\frac{1}{1+z^{2^{3a}}}
=\prod_{\substack{j\ge0\\j\notin3\mathbb Z_{>0}}}(1+z^{2^j}).
\]
The equality follows from the formal binary product \(1/(1-z)=\prod_{j\ge0}(1+z^{2^j})\), followed by exact cancellation. Hence
\[
\boxed{G(q)=\prod_{\substack{u\ge1\ \mathrm{odd}\\j\ge0,\ j\notin3\mathbb Z_{>0}}}(1+q^{2^ju^3}).}
\]
Thus \(A_3(n)\) counts subsets of the **distinct** allowable weights
\(\mathcal W=\{2^ju^3:u\text{ odd and positive},\ j=0\text{ or }3\nmid j\}\)
with sum \(n\). Distinctness follows from uniqueness of the \(2\)-adic valuation and positive odd cube root. In particular \(A_3(n)\ge0\).

**Step 2: exact small exceptions.** The weights in \(\mathcal W\) not exceeding \(123\) are exactly
\[
L=(1,2,4,16,27,32,54,108).
\]
The complete \(2^8=256\) subset sums of this list miss precisely the twenty-three indices displayed in the finding within \([0,123]\). This is an exhaustive finite statement, computed by the recurrence \(B_0=\{0\}\), \(B_{i+1}=B_i\cup(B_i+w_i)\) for successive listed weights \(w_i\). It may be verified independently by the included \(\texttt{verify.py}\). In particular \(123\) is not representable.

**Step 3: a finite solid interval.** Append the two allowable weights \(125\) and \(128\) to \(L\), obtaining
\[
L'=(1,2,4,16,27,32,54,108,125,128).
\]
Its \(2^{10}=1024\) subsets cover every integer in the entire interval \([124,373]\). This is again an exact finite certificate using the same recurrence, not an extrapolation. The interval ends at \(373\) for this initial solid run (\(374\) is absent), although some larger sums are also represented.

**Step 4: an infinite interval extension.** The weight \(250=2\cdot5^3\) is allowed. Translating the covered interval by \(250\) gives \([374,623]\), adjoining \([124,373]\) without a gap. The weight \(343=7^3\) extends the covered interval to \([124,966]\), since the translated interval begins at \(467\le623+1\). The next odd cube \(729=9^3\) is at most \(966-123\), so it also extends coverage.

More generally, suppose a set of allowed weights covers every index in \([124,R_u]\), having added all odd cubes from \(7^3\) through \(u^3\), where \(u\ge7\) is odd. For the next cube \(v^3\), where \(v=u+2\), its translated interval starts at \(124+v^3\). It overlaps the existing interval whenever \(v^3\le R_u-123\). This is true for \(u=7\), since \(9^3\le966-123\). After appending \(v^3\), the upper bound becomes \(R_v=R_u+v^3\), and the overlap margin for the *following* cube changes by
\[
(R_v-123-(v+2)^3)-(R_u-123-v^3)=2v^3-(v+2)^3.
\]
For every integer \(v\ge9\), this is positive: it equals \(v^3-6v^2-12v-8\), equals \(127\) at \(v=9\), and is strictly increasing thereafter (its derivative is \(3v^2-12v-12>0\)). Therefore all successive overlaps hold. Since the sum of the successive positive cubes diverges, these overlapping intervals cover **every** integer \(n\ge124\). Combined with Step 2, this proves the theorem. \(\square\)

## Verification
Running \(\texttt{python3 verify.py}\) independently enumerates the \(256\) small subsets and \(1024\) base subsets, verifies the complete exceptional set and the solid interval, checks the symbolic induction bases, and compares \(2049\) exact coefficients computed by two independent algorithms: a signed unrestricted-partition recurrence and subset-count dynamic programming. The executable is supporting finite evidence only; the infinite statement follows from the formal-series identity and overlap induction.

## Relationship to prior work
Ciolan, *Equidistribution and inequalities for partitions into powers* (first arXiv publication February 13, 2020; arXiv:2002.05682), proves general coefficient nonnegativity by a related product and eventual strict positivity for every fixed exponent. Its Sections 3 and 7 do not state an effective cubic strictness threshold or the above full exceptional set. The present argument does **not** claim originality for the nonnegative product interpretation; it determines the exact cubic strictness boundary by an additional finite-cover and infinite-extension proof. OEIS A292560 records signed cubic-partition coefficients (initial entry September 19, 2017) and supplies a finite table through \(n=20000\); entries identify numerical zeros but a finite table does not imply global strictness. OEIS A339368 and A339369 separately count the even- and odd-part cubic partitions. Related strictness cutoffs for square and fourth-power partitions do not imply the cubic statement because their permitted powers differ.

## Limitations
The exact threshold and equality set concern cubes alone. No uniform threshold in the power exponent is asserted. The original generating-product and eventual-positivity theorems are prior work; the new mathematical claim is the sharp **effective** threshold and complete zero classification. The database search is not proof of priority; unindexed or differently framed antecedents remain possible. No independent mathematical audit has been performed.

## References
- A. Ciolan, *Equidistribution and inequalities for partitions into powers*, arXiv:2002.05682, first public version 2020-02-13, https://arxiv.org/abs/2002.05682 (especially Sections 2, 3, and 7).
- OEIS A292560, *Expansion of Product of reciprocal cube factors*, entry dated 2017-09-19; https://oeis.org/A292560 and exact finite table https://oeis.org/A292560/b292560.txt.
- OEIS A339368 and A339369, even- and odd-length cube partitions, https://oeis.org/A339368 and https://oeis.org/A339369.
