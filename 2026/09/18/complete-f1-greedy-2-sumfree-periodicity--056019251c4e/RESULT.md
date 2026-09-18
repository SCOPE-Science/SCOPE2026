# Complete periodicity of the \(f=1\) greedy strict 2-sumfree family

## Statement

Let \(S_{1,g}\) be the increasing greedy sequence beginning with \(1<g\), where each later term is the least larger positive integer that is not the sum of two **distinct** earlier terms. Then \(S_{1,g}\) is ultimately periodic for every \(g\ge 2\). Moreover, its minimal period and preperiod lengths are exactly those conjectured by van Berkel and Bosma in arXiv:2609.18522.

For odd \(g\),
\[
S_{1,g}=\{1\}\cup\{g,g+2,g+4,\ldots\}.
\]
Thus the minimal period length is \(1\); the preperiod length is \(0\) for \(g=3\) and \(1\) for odd \(g\ge5\).

The small even cases have the exact descriptions
\[
\begin{aligned}
S_{1,2}&=\{1,2\}\cup\{n\ge3:n\equiv1\pmod3\},\\
S_{1,4}&=\{1,4,6,8\}\cup\{n\ge9:n\bmod12\in\{1,4,6,11\}\},\\
S_{1,6}&=\{1,6,8,10,12\}\cup\{n\ge13:n\bmod9\in\{1,6,8\}\}.
\end{aligned}
\]
Their minimal (preperiod, period) lengths are respectively
\[
(2,1),\qquad (4,4),\qquad (5,3).
\]

For every even \(g\ge8\), put
\[
M=4g+3
\]
and define the residue set
\[
R_g=
\{1,3,4g,4g+2\}
\cup\{g,g+2,\ldots,2g-2\}
\cup\{2g+5,2g+7,\ldots,3g+1\}
\subset \mathbb Z/M\mathbb Z.
\]
Then
\[
\boxed{
S_{1,g}
=
\{1\}
\cup\{g,g+2,\ldots,2g\}
\cup\{2g+3\}
\cup
\{n\ge2g+4:n\bmod M\in R_g\}.
}
\]
Consequently the characteristic sequence is periodic modulo \(4g+3\) after the displayed finite prefix, with
\[
\boxed{
Q(g-1,1)=\frac g2+3,\qquad
P(g-1,1)=g+3.
}
\]
This proves Conjectures 5 and 9 of van Berkel--Bosma for the complete column \(f=1\), not only for the finite ranges previously checked computationally.

## Proof

### 1. Odd \(g\)

Suppose \(g\) is odd. Once \(1\) and \(g\) are selected, every even integer \(n>g\) is excluded as
\[
n=1+(n-1),
\]
where \(n-1\) is the preceding selected odd integer. Conversely, a sum of two selected odd integers is even, and \(1\) plus a selected odd integer is even, so no odd integer \(n\ge g\) is excluded. Hence
\[
S_{1,g}=\{1\}\cup\{g+2k:k\ge0\}.
\]
For \(g=3\) the entire difference sequence is \(2,2,\ldots\); for odd \(g\ge5\) it is \(g-1,2,2,\ldots\). This gives the asserted minimal lengths.

### 2. The main even family

Let \(g\ge8\) be even. Write
\[
A=\{1,3\},\quad
B=\{g,g+2,\ldots,2g-2\},\quad
C=\{2g+5,2g+7,\ldots,3g+1\},\quad
D=\{4g,4g+2\},
\]
so \(R_g=A\cup B\cup C\cup D\).

Two elementary residue facts drive the proof.

**Lemma 1 (sum exclusion).**
\[
(R_g+R_g)\cap R_g=\varnothing\qquad\text{in }\mathbb Z/M\mathbb Z.
\]

Indeed, using representatives in \([0,M-1]\), the ten unordered component sums lie in the following sets:
\[
\begin{array}{c|c}
\text{pair}&\text{residues modulo }M\\ \hline
A+A&\{2,4,6\}\\
A+B&\{g+1,g+3,\ldots,2g+1\}\\
A+C&\{2g+6,2g+8,\ldots,3g+4\}\\
A+D&\{0,2,4g+1\}\\
B+B&\{2g,2g+2,\ldots,4g-4\}\\
B+C&\{3g+5,3g+7,\ldots,4g+1\}\cup\{0,2,\ldots,g-6\}\\
B+D&\{g-3,g-1,\ldots,2g-3\}\\
C+C&\{7,9,\ldots,2g-1\}\\
C+D&\{2g+2,2g+4,\ldots,3g\}\\
D+D&\{4g-3,4g-1,4g+1\}.
\end{array}
\]
Every listed residue is outside \(R_g\).

**Lemma 2 (four-shift covering).** If
\[
E=\{1,g,2g,2g+3\},
\]
then
\[
\boxed{
(\mathbb Z/M\mathbb Z)\setminus R_g
=
\bigcup_{e\in E}(e+R_g).
}
\]
For completeness, the four shifts are
\[
\begin{aligned}
1+R_g={}&\{0,2,4,4g+1\}
 \cup\{g+1,g+3,\ldots,2g-1\}
 \cup\{2g+6,2g+8,\ldots,3g+2\},\\
g+R_g={}&\{g-3,g-1,g+1,g+3\}
 \cup\{2g,2g+2,\ldots,3g-2\}
 \cup\{3g+5,3g+7,\ldots,4g+1\},\\
2g+R_g={}&\{2,4,\ldots,g-2\}
 \cup\{2g-3,2g-1,2g+1,2g+3\}
 \cup\{3g,3g+2,\ldots,4g-2\},\\
(2g+3)+R_g={}&\{5,7,\ldots,g+1\}
 \cup\{2g,2g+2,2g+4,2g+6\}
 \cup\{3g+3,3g+5,\ldots,4g+1\}.
\end{aligned}
\]
Their union is exactly the complement of \(R_g\). In particular, each of these shifts is disjoint from \(R_g\).

Now define \(T_g\) by the boxed formula in the statement. We show that it is exactly the greedy sequence.

Up to \(2g+3\), greediness is immediate. Starting from \(1,g\), every odd integer from \(g+1\) through \(2g+1\) is excluded by adding \(1\) to the preceding selected even integer. No sum of two distinct selected terms can exclude the even integers
\[
g+2,g+4,\ldots,2g,
\]
while
\[
2g+2=g+(g+2)
\]
is excluded. The next integer \(2g+3\) cannot be represented as a sum of two distinct selected terms. Thus the selected prefix is precisely
\[
\{1\}\cup\{g,g+2,\ldots,2g\}\cup\{2g+3\}.
\]

The first block after this prefix is also explicit. In
\[
2g+4\le n\le4g+6
\]
the selected terms are exactly
\[
\{2g+5,2g+7,\ldots,3g+1,\ 4g,\ 4g+2,\ 4g+4,\ 4g+6\}.
\]
Every omitted even \(n\in[2g+4,3g+2]\) is \(1+(n-1)\). Every omitted odd \(n\in[3g+3,4g-1]\) is \(g+(n-g)\). Every omitted even \(n\in[3g+4,4g-2]\) is \(2g+(n-2g)\). Finally,
\[
4g+1=1+4g,\qquad
4g+3=2g+(2g+3),\qquad
4g+5=1+(4g+4).
\]
All these representations use distinct earlier selected terms.

For all later integers, Lemma 2 closes the induction. If \(n\ge4g+7=M+4\) and \(n\bmod M\notin R_g\), choose \(e\in E\) with
\[
n-e\bmod M\in R_g.
\]
Because \(e\le2g+3\),
\[
n-e\ge2g+4,
\]
so \(n-e\in T_g\); also \(n>2e\), hence \(e\ne n-e\). Thus
\[
n=e+(n-e)
\]
is a forbidden sum of distinct earlier selected terms.

It remains to check that no proposed term is accidentally excluded. Lemma 1 prevents a sum of two terms whose eventual residue classes lie in \(R_g\) from returning to \(R_g\). The two exceptional prefix terms \(2g\) and \(2g+3\) also cannot create a selected tail term: the explicit formulas above show
\[
(2g+R_g)\cap R_g=((2g+3)+R_g)\cap R_g=\varnothing,
\]
and
\[
2g+(2g+3)=M\not\equiv R_g.
\]
A sum of two ordinary selected terms can equal the exceptional value \(2g\) only as \(g+g\), which repeats the same term and is therefore allowed by the strict rule; it cannot equal \(2g+3\). The self-sums of the exceptional terms are likewise irrelevant because the definition forbids only sums of distinct earlier terms. Hence every member of \(T_g\) survives, completing the greedy induction.

### 3. Minimal period and preperiod

The residue set has
\[
|R_g|=g+3.
\]
Its circular gaps, in increasing residue order, consist of \(2\)'s together with the three nontrivial gaps
\[
g-3,\qquad 7,\qquad g-1.
\]
For \(g\ge10\), the gap \(g-1\) is the unique largest circular gap, so no nonzero translation of \(\mathbb Z/M\mathbb Z\) can stabilize \(R_g\). For \(g=8\), the two gaps of size \(7\) are distinguished by the unique gap of size \(5\). Thus \(R_g\) again has trivial translation stabilizer.

Therefore \(M=4g+3\) is the minimal eventual period of the characteristic sequence. One characteristic period contains \(g+3\) selected integers, so the minimal period length of the first-difference sequence is \(g+3\).

The finite prefix contains
\[
1+\left(\frac g2+1\right)+1=\frac g2+3
\]
selected terms. Periodicity begins immediately afterward. It cannot begin earlier: the last exceptional selected value \(2g+3\) has residue \(2g+3\notin R_g\), whereas any earlier onset of eventual periodicity would force a later selected translate of that value by an eventual period. Hence the minimal preperiod length is \(g/2+3\).

### 4. Small even values

The three displayed descriptions for \(g=2,4,6\) are verified by the same two ingredients: the indicated eventual residue set has no residue sum returning to itself, and every complementary residue is a translate of the residue set by a selected prefix term. A direct finite check of the initial prefix then gives the stated minimal lengths. Explicitly, the eventual residue sets are
\[
\{1\}\pmod3,\qquad
\{1,4,6,11\}\pmod{12},\qquad
\{1,6,8\}\pmod9.
\]
Their circular gap words have respectively \(1,4,3\) entries, and the exceptional prefixes contain respectively \(2,4,5\) selected terms.

This completes the proof for every \(g\ge2\).

## Consequences

Writing \(d=g-1\), the theorem proves the complete \(f=1\) column of the two principal quantitative conjectures in arXiv:2609.18522:
\[
P(d,1)=L_1(d),\qquad Q(d,1)=K_r(d,1).
\]
In particular, for odd \(d\ge7\),
\[
P(d,1)=d+4,\qquad Q(d,1)=\frac{d+7}2,
\]
while for even \(d\ge4\),
\[
P(d,1)=1,\qquad Q(d,1)=1.
\]
The exceptional values \(d=1,2,3,5\) agree with the special values stated in that paper.

The exact descriptions also give the natural density:
\[
d(S_{1,g})=
\begin{cases}
\frac12,&g\text{ odd},\\[1mm]
\frac13,&g\in\{2,4,6\},\\[1mm]
\frac{g+3}{4g+3},&g\ge8\text{ even}.
\end{cases}
\]

## Verification

The accompanying standalone program directly generates the greedy sequence and compares it with the formulas above for every \(2\le g\le120\) through at least twelve eventual characteristic periods. It also checks, for every even \(8\le g\le200\), the two finite residue identities used in the proof:
\[
(R_g+R_g)\cap R_g=\varnothing,
\qquad
(\mathbb Z/M\mathbb Z)\setminus R_g=\bigcup_{e\in E}(e+R_g).
\]
These computations are supporting checks; the theorem is proved by the residue argument above.

## Relation to prior work and limitations

Van Berkel and Bosma, *Periodicity conjectures for all 2-sumfree sequences* (arXiv:2609.18522v1, submitted 16 September 2026), formulate the general period and preperiod conjectures. Their Theorem 12 covers \(g\le2f-1\), which gives no case with \(f=1\), while their Theorems 16 and 17 establish only finite computational ranges: both period and preperiod for \(f,d\le250\), and period for \(f,d\le500\). Their Definition 3 and Definition 8 give the precise \(f=1\) predictions proved here.

The preceding preprint van Berkel--Bosma, *On \(t\)-sumfree sequences* (arXiv:2609.16843), supplies the earlier \(g<2f\) family and a finite-repetition criterion, but does not cover the infinite \(f=1\) family treated here.

Originality is claimed only to the best of our knowledge. Searches for the exact family \(S_{1,g}\), the modulus \(4g+3\), the period \(g+3\), the \(f=1\) column, and synonymous greedy strict/weakly sum-free formulations found no proof of this complete family. The motivating preprints are extremely recent, so unindexed contemporaneous work remains a residual risk. No inaccessible paper was identified whose metadata specifically suggests the same theorem.

## References

1. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1 (2026), https://arxiv.org/abs/2609.18522.
2. D. van Berkel and W. Bosma, *On \(t\)-sumfree sequences*, arXiv:2609.16843 (2026), https://arxiv.org/abs/2609.16843.
