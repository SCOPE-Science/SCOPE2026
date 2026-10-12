# Binary-weight-seven Proth semigroups have an exact Frobenius number

## Finding
For every odd positive integer \(k\) of binary Hamming weight \(7\), and every integer \(n\ge1\) with \(k<2^n\), put \(a=k2^n+1\) and define the numerical semigroup
\[
S_{k,n}=\big\langle k2^{n+i}+1:i\in\mathbb Z_{\ge0}\big\rangle.
\]
Then
\[
\boxed{F(S_{k,n})=a(a+5)+3.}
\]
Moreover, the largest element of the Apéry set of \(S_{k,n}\) with respect to \(a\) is \(a(a+6)+3\), attained **uniquely** in residue class \(3\) modulo \(a\). This is an infinite-coefficient, infinite-exponent family; in particular it includes \(k=127\), the first coefficient in the first-two-greedy-digits-zero regime discussed in the cited work.

## Assumptions and scope
Here \(\operatorname{wt}_2(k)\) is the number of ones in the ordinary base-two expansion of \(k\); the hypotheses are \(k\) odd, \(\operatorname{wt}_2(k)=7\), and \(k<2^n\). They imply \(n\ge7\) and \(a\ge127\cdot2^7+1\). The semigroup contains \(a\) and \(2a-1\), which are coprime; thus its complement in the nonnegative integers is finite. Its Frobenius number is the greatest integer outside it. The Apéry element of a residue is the smallest semigroup element in that residue.

All sums below are finite and use nonnegative multiplicities. An exponent \(i=0\) denotes the generator \(a\); other exponents begin at \(i=1\).

## Proof
**1. Binary-power representation lemma.** For even \(T\ge2\) and integer \(C\ge1\), the identity
\[
T=\sum_{j=1}^{C}2^{i_j},\qquad i_j\ge1,
\]
holds for some integer exponents exactly when
\[
\operatorname{wt}_2(T/2)\le C\le T/2.
\]
Necessity follows by dividing by two: any expression of an integer as a sum of powers of two uses at least its binary weight and at most the integer itself. For sufficiency, begin with the ordinary binary expansion of \(T/2\), which uses exactly \(\operatorname{wt}_2(T/2)\) summands. Repeatedly split a term \(2^j\) with \(j\ge1\) into two terms \(2^{j-1}\). Each split increases the number of summands by one, and splitting can continue until there are exactly \(T/2\) unit terms. Hence every intermediate \(C\) is realizable.

**2. Coding the semigroup sums.** For generators with indices \(i_j\ge1\), write \(T=\sum_j2^{i_j}\) and \(C\) for the number of summands. Set \(u=T-C=\sum_j(2^{i_j}-1)\). Their total value is
\[
\sum_j(k2^{n+i_j}+1)=aT-u,\qquad aT-u\equiv-u\pmod a.
\]
By Step 1, any positive integer \(u\) and even \(T\) with \(C=T-u\) satisfying \(\operatorname{wt}_2(T/2)\le C\le T/2\) produce an actual semigroup element \(aT-u\) in residue \(-u\).

**3. One small witness for each residue.** Let \(u\) run through \(0,1,\ldots,a-1\); this indexes every residue class \(-u\pmod a\). Take the zero witness for \(u=0\). For the other residues choose \(T\) by the exhaustive, nonoverlapping cases:
\[
T=\begin{cases}
2u,&1\le u\le(a+1)/2,\\
a+1,&(a+1)/2<u\le a-7,\\
a+3,&a-6\le u\le a-5,\\
a+5,&u=a-4,\\
a+7,&a-3\le u\le a-1.
\end{cases}
\]
Each \(T\) is even. Since \(a=k2^n+1\), the five binary weights relevant to the last four cases and the lower-bound argument are
\[
\begin{aligned}
\operatorname{wt}_2((a-1)/2)&=7,\\
\operatorname{wt}_2((a+1)/2)&=8,\\
\operatorname{wt}_2((a+3)/2)&=8,\\
\operatorname{wt}_2((a+5)/2)&=9,\\
\operatorname{wt}_2((a+7)/2)&=8.
\end{aligned}
\]
Indeed, the high bits of \(k2^{n-1}\) have weight seven and, because \(n\ge7\), are disjoint from the low digits of \(0,1,2,3,4\). For the first case \(C=u=T/2\). For the second \(8\le C=a+1-u\le(a+1)/2\). For the third, \(C\) is respectively \(9\) or \(8\). In the fourth, \(C=9\). In the fifth, \(C\) runs through \(10,9,8\). Thus the representation lemma applies in every case.

Put \(M=a(a+6)+3\). Every constructed witness is at most \(M\), and equality occurs only at \(u=a-3\). To check this explicitly: in the first case \(aT-u=(2a-1)u\le(2a-1)(a+1)/2<M\); in the second case \(aT-u=a(a+1)-u<M\). For the remaining cases the largest values are, in order, \(a(a+2)+6\), \(a(a+4)+4\), and \(a(a+6)+3=M\). In the final case the values for \(u=a-3,a-2,a-1\) are exactly \(M,M-1,M-2\). Hence every Apéry element is at most \(M\), and all residues other than \(3\) have an Apéry element strictly below \(M\).

**4. Sharp obstruction in residue three.** We show that no semigroup element congruent to \(3\pmod a\) is smaller than \(M\). Otherwise remove all summands equal to \(a\); this preserves the residue and weakly decreases the value. The resulting sum uses only exponents \(i_j\ge1\), and Step 2 gives \(u=T-C\ge0\) with \(u\equiv a-3\pmod a\). Therefore \(u=a-3+ta\) for an integer \(t\ge0\).

If \(t\ge1\), then \(u\ge2a-3\) and \(T\ge u+1\) (since \(C\ge1\)); consequently
\[
aT-u\ge(a-1)(2a-3)+a=2a^2-4a+3>M
\]
for \(a>10\), a contradiction.

If \(t=0\), then \(u=a-3\) and the even integer \(T\) satisfies \(T\ge a-1\). A value \(aT-u<M=a(a+7)-(a-3)\) would require \(T<a+7\), so \(T\) is one of \(a-1,a+1,a+3,a+5\). The corresponding proposed term counts \(C=T-(a-3)\) are \(2,4,6,8\), while the required minimum binary weights \(\operatorname{wt}_2(T/2)\) are \(7,8,8,9\). Each is strictly larger than its proposed count, contradicting Step 1. Thus \(M\) is the least element in residue \(3\), and it is uniquely the largest Apéry element by Step 3.

**5. Frobenius conclusion.** Every residue has a semigroup representative at most \(M\), so every integer strictly larger than \(M-a\) lies in the semigroup: choose the representative in the same residue and add a nonnegative multiple of \(a\). On the other hand \(M-a\), being smaller than the least representative \(M\) in residue \(3\), is not in the semigroup. Therefore
\[
F(S_{k,n})=M-a=a(a+5)+3.
\]

## Verification
The accompanying standalone `verify.py` uses integer-only shortest paths on finite residue graphs as an independent check of the proposed Frobenius number and unique maximizing residue, on seven admissible parameter pairs. It also checks the exhaustive piecewise witness inequalities and direct representations on selected boundary residues. The saved exact output is `verification_output.txt`. The unrestricted result rests on the proof above, not on these finite checks.

## Relationship to prior work
Srivastava and Thakkar [1] introduced Proth numerical semigroups and established an embedding-dimension formula and a Frobenius formula for coefficients of the special form \(2^r+1\). Liu, Xin, Ye and Yin [2] give a general description of the Apéry set by a greedy representation in their Theorem 5.2 and explicit Frobenius formulas in Theorems 5.4 and 5.5 conditional on the first or second greedy digit being nonzero. They expressly identify the next regime with both first digits zero and the third nonzero as not covered by those closed formulas (discussion following Theorem 5.5). The coefficient \(k=127=2^6+63\) lies in that regime. The present theorem evaluates the missing maximum in one natural complete Hamming-weight stratum, and proves its unique maximizing residue, independently of the greedy Apéry algorithm. The earlier general Apéry description gives an algorithmic way to determine every case and is therefore important pre-existing coverage; the claim here is the newly explicit closed formula and extremal class for **all** seven-one coefficients, not the computability of the Frobenius number.

## Limitations
No claim is made for coefficients of another binary weight. This statement does not determine genus, type, or all individual Apéry elements. The originality comparison is relative to the cited papers and the searched public research records; an unindexed equivalent closed formula cannot be excluded. Self-review are not independent scholarly validation.

## References
[1] Pranjal Srivastava and Dhara Thakkar, *The Frobenius Problem for the Proth Numbers*, arXiv:2311.12462 (first posted 2023-11-21), especially the embedding-dimension result and concluding question.

[2] Feihu Liu, Guoce Xin, Suting Ye and Jingjing Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459 (first posted 2023-06-06; version 4, 2025-03-06, examined), especially Theorems 5.2, 5.4, 5.5 and discussion after Theorem 5.5.
