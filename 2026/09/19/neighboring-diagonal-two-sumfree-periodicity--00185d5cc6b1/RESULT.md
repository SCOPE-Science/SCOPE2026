# Exact periodicity for the neighboring-diagonal family \(S_{f,2f+1}\)

## Result

Let \(S_{f,g}\) be the strict greedy \(2\)-sumfree sequence: it starts with
\(f<g\), and every subsequent term is the least larger positive integer that is
not a sum of two distinct earlier terms. For every integer \(f\ge 3\), put
\[
M_f=5f+1.
\]
Then
\[
\boxed{
S_{f,2f+1}
=
\{f\}\cup[2f+1,3f]\cup
\bigcup_{k\ge0}\left(
\{4f+1,4f+2,6f,6f+1\}\cup[7f+3,8f]+kM_f
\right),
}
\]
where intervals contain all integers in their endpoints and \(A+kM\) denotes
translation of every element of \(A\) by \(kM\).

Equivalently, from \(4f+1\) onward membership is periodic modulo \(M_f\), with
residue set
\[
R_f=[f-1,f]\cup[2f+2,3f-1]\cup[4f+1,4f+2]
\pmod{M_f}.
\]

The first-difference sequence has preperiod
\[
(f+1,\underbrace{1,\ldots,1}_{f-1},f+1)
\]
and thereafter repeats
\[
\boxed{
(1,\;2f-2,\;1,\;f+2,\;
\underbrace{1,\ldots,1}_{f-3},\;f+2).
}
\]
Thus its minimal preperiod length is \(f+1\). Its minimal period length is
\[
\boxed{
\begin{cases}
5,&f=3,\\
2,&f=4,\\
f+2,&f\ge5.
\end{cases}}
\]
For \(f\ge5\), the minimal characteristic-sequence period is \(5f+1\); for
\(f=3\) it is \(16\), and for \(f=4\) it is \(7\). In all cases \(f\ge3\), the
natural density exists and equals
\[
\boxed{\frac{f+2}{5f+1}}.
\]

## Relation to the recent conjectures

Van Berkel and Bosma's 2026 preprint *Periodicity conjectures for all
2-sumfree sequences* proves special families through the diagonal \(g\le2f\)
and conjectures ultimate periodicity for every pair \((f,g)\). Their
Conjecture 5 predicts the exact period length via a function
\(\mathcal L_f(d)\), where \(d=g-f\). On the first strip beyond the proved
diagonal, \(d=f+1\), that conjecture predicts \(f+2\) for \(f\ge5\), with the
listed exceptional value \(2\) at \(f=4\); the \(f=3\) example has period \(5\).
The theorem above proves this entire strip for \(f\ge3\) and gives a closed
form for the sequence itself.

The earlier paper *On \(t\)-sumfree sequences* proves periodicity when
\(f+1\le g<2f\). Hence the family \(g=2f+1\) lies immediately beyond the
previously proved region.

## Proof

Write
\[
Q=[2f+1,3f],\qquad
A=[f-1,f],\quad
B=[2f+2,3f-1],\quad
C=[4f+1,4f+2],
\]
and let
\[
R=A\cup B\cup C\subset\mathbb Z/M_f\mathbb Z.
\]

### 1. The eventual residue set is sumfree

All possible sums of two residues from \(R\), reduced modulo \(M_f=5f+1\),
fall in the following ranges:
\[
\begin{aligned}
A+A&=[2f-2,2f],\\
A+B&=[3f+1,4f-1],\\
A+C&=\{5f,0,1\},\\
B+B&=[4f+4,5f]\cup[0,f-3],\\
B+C&=[f+2,2f],\\
C+C&=[3f+1,3f+3].
\end{aligned}
\]
For \(f\ge3\), every one of these sets is disjoint from \(R\). Therefore
\[
(R+R)\cap R=\varnothing.
\]
This statement is stronger than needed because it also allows equal residues.

### 2. The prefix interval fills exactly the complementary residues

A direct interval calculation gives
\[
\begin{aligned}
Q+A&=[3f,4f],\\
Q+B&=[4f+3,5f]\cup[0,f-2]\pmod{M_f},\\
Q+C&=[f+1,2f+1]\pmod{M_f}.
\end{aligned}
\]
Consequently
\[
\boxed{Q+R=(\mathbb Z/M_f\mathbb Z)\setminus R.}
\]
This complement identity is the mechanism forcing the periodic tail.

### 3. The finite beginning

Starting from \(f,2f+1\), no sum of two distinct available terms can occur
before \(3f+1\). Hence greediness inserts the whole block \(Q\).

The next omitted block is
\[
[3f+1,4f]=f+Q.
\]
The two integers \(4f+1,4f+2\) are therefore admitted. The sums of two
distinct elements of the interval \(Q\) fill exactly
\[
[4f+3,6f-1],
\]
so this entire block is rejected and \(6f,6f+1\) are admitted. Next,
\[
[6f+2,7f+2]=Q+\{4f+1,4f+2\},
\]
and hence the following admitted block is \([7f+3,8f]\). This is precisely
the claimed formula through \(8f\).

### 4. Induction for the periodic tail

Consider an integer \(n\ge8f+1\).

If \(n\bmod M_f\in R\), then \(n\) cannot be a sum of two distinct earlier
candidate terms. Two eventual-tail terms are excluded by
\((R+R)\cap R=\varnothing\). The term \(f\) also represents a residue in
\(R\), so \(f\) plus a tail term is excluded by the same fact. A term from
\(Q\) plus a tail term has residue in \(Q+R=R^c\). Finally, the possible
prefix-prefix sums are confined to
\[
f+Q=[3f+1,4f],\qquad
Q\mathbin{\widehat+}Q=[4f+3,6f-1],
\]
where the hat denotes sums of distinct terms; neither range reaches a
candidate tail value with residue in \(R\). Thus every proposed tail member
is admissible.

If \(n\bmod M_f\notin R\), the complement identity supplies
\(p\in Q\) and \(r\in R\) such that
\[
n\equiv p+r\pmod{M_f}.
\]
Put \(y=n-p\). Since \(p\le3f\) and \(n\ge8f+1\),
\[
y\ge5f+1>4f+1.
\]
Also \(y\bmod M_f=r\), so \(y\) is an earlier tail member, while
\(y>p\). Hence \(n=p+y\) is a sum of two distinct earlier members and must
be rejected.

Induction now proves the closed formula for all terms.

### 5. Minimal periods

Reading successive gaps beginning at \(4f+1\) gives
\[
1,\quad 2f-2,\quad 1,\quad f+2,\quad
1^{\,f-3},\quad f+2,
\]
whose sum is \(5f+1\).

For \(f\ge5\), the value \(2f-2\) occurs exactly once in this cyclic word,
so no proper shorter word can generate it; the minimal difference period is
therefore \(f+2\). For \(f=3\) the word is
\((1,4,1,5,5)\), which has minimal period \(5\). For \(f=4\) it is
\((1,6,1,6,1,6)\), whose minimal period is \((1,6)\).

Before the periodic part, the difference word is
\[
(f+1,1^{\,f-1},f+1).
\]
For \(f\ge4\), its last value \(f+1\) does not occur in the eventual period,
so the preperiod cannot be shortened. The \(f=3\) case is checked directly:
starting one difference earlier would require the fourth difference \(4\)
to agree five places later, where the value is \(5\). Thus the minimal
preperiod length is \(f+1\) in every case.

The density is the number of eventual residue classes divided by the
modulus:
\[
|R|=(2)+(f-2)+(2)=f+2,
\]
which gives \((f+2)/(5f+1)\).

## Verification

A standalone exact-integer script in `artifacts/verify_family.py` checks the
modular identities for every \(3\le f\le500\), and independently regenerates
the greedy sequence for every \(3\le f\le100\), comparing 1200 terms with the
closed formula and checking the predicted minimal preperiod and period. All
checks pass. These computations are supplementary; the theorem is proved
above for every \(f\ge3\).

## Limitations

This result does not settle ultimate periodicity for arbitrary \(S_{f,g}\),
does not treat the exceptional starting families \(f=1,2\), and does not
prove any other off-diagonal strip. It proves only the family \(g=2f+1\),
although the residue-complement identity may be useful for further families.

Originality is asserted only to the best of our knowledge. The motivating
preprint is very recent, so contemporaneous or not-yet-indexed work remains
a residual risk.

## References

1. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree
   sequences*, arXiv:2609.18522v1 (2026).
2. D. van Berkel and W. Bosma, *On \(t\)-sumfree sequences*,
   arXiv:2609.16843v1 (2026).
3. A. Fokkink et al., discussion of greedy sumfree sequences and earlier
   literature in *Journal of Integer Sequences* 28 (2025), Section 5.
