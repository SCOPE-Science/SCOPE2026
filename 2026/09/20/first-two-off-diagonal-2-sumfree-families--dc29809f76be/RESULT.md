# Exact periodicity of the first two off-diagonal greedy 2-sumfree families

## Statement

For integers \(f<g\), let \(S_{f,g}\) be the increasing greedy strict 2-sumfree sequence that starts with \(f,g\) and thereafter takes the least larger positive integer that is not a sum of two **distinct** earlier terms.

Fix \(f\ge 5\) and \(\delta\in\{1,2\}\), and put
\[
g=2f+\delta,\qquad M=5f+2\delta-1.
\]
Define
\[
E=\{f\}\cup[\,2f+\delta,\,3f+\delta-1\,]
\]
and, as a set of residues modulo \(M\),
\[
R=\{f-1,f\}
 \cup[\,2f+\delta+1,\,3f+\delta-2\,]
 \cup[\,4f+\delta,\,4f+2\delta\,].
\]

Then
\[
\boxed{
S_{f,\,2f+\delta}
=
E\ \cup\
\{n\ge 4f+\delta:\ n\bmod M\in R\}.
}
\]

Consequently \(S_{f,2f+\delta}\) is ultimately periodic with minimal preperiod length
\[
\boxed{f+1}
\]
and minimal period length
\[
\boxed{f+\delta+1}.
\]
A minimal periodic block of first differences is
\[
\boxed{
(1^\delta,\ 2f-2,\ 1,\ f+\delta+1,\ 1^{f-3},\ f+2),
}
\]
whose sum is \(M\). Its natural density is therefore
\[
\boxed{
\frac{f+\delta+1}{5f+2\delta-1}.
}
\]

These are the first two infinite families immediately beyond the diagonal \(g=2f\) in the parameter plane.

## Context

Van Berkel and Bosma prove periodicity for every \(g\le 2f-1\), and in their subsequent paper prove the diagonal \(g=2f\) for every \(f\ge3\). They formulate a conjecture giving ultimate periodicity and precise period lengths for all \(S_{f,g}\), and verify the conjectured period lengths computationally in a large finite parameter box. The theorem above supplies a direct infinite proof for the next two lines
\[
g=2f+1,\qquad g=2f+2.
\]

Primary sources:

- D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522 (2026), especially Theorems 12, 14, 16, 17 and Conjecture 5:
  https://arxiv.org/abs/2609.18522
- D. van Berkel and W. Bosma, *On \(t\)-sumfree sequences*, arXiv:2609.16843 (2026):
  https://arxiv.org/abs/2609.16843

## Proof

Write
\[
T=E\cup\{n\ge4f+\delta:n\bmod M\in R\}.
\]
We prove that \(T\) is exactly the greedy sequence.

### 1. The initial segment

The two prescribed terms are \(f\) and \(g=2f+\delta\). Before \(f+g=3f+\delta\), no integer can be a sum of two distinct selected terms, so all
\[
2f+\delta,\ldots,3f+\delta-1
\]
are selected. Hence the selected initial set is \(E\).

Every integer in
\[
[\,3f+\delta,\ 4f+\delta-1\,]
\]
is excluded, because this interval is
\[
f+[\,2f+\delta,\ 3f+\delta-1\,].
\]
Thus \(4f+\delta\) is the first possible entry after \(E\).

### 2. No proposed tail entry is a forbidden sum

It is enough to check residue classes modulo \(M\). For finite sets \(A,B\), write \(A+B\) for their modular sumset, and write \(E\widehat{+}E\) when equal summands are omitted. In \(R+R\) equal residue classes must be retained, because two distinct tail integers can have the same residue and differ by a multiple of \(M\).

For \(\delta=1\), so \(M=5f+1\), direct interval arithmetic gives
\[
\begin{aligned}
E\widehat{+}E
={}&[0,f-2]\cup[3f+1,4f]\cup[4f+3,5f],\\
E+R
={}&[0,f-2]\cup[f+1,2f+1]\cup[3f,4f]\cup[4f+3,5f],\\
R+R
={}&[0,f-3]\cup[f+2,2f]\cup[3f+1,4f-1]\cup[4f+4,5f].
\end{aligned}
\]
Here
\[
R=\{f-1,f\}\cup[2f+2,3f-1]\cup[4f+1,4f+2].
\]
Each of the three displayed sumsets is disjoint from \(R\).

For \(\delta=2\), so \(M=5f+3\),
\[
\begin{aligned}
E\widehat{+}E
={}&[0,f-2]\cup[3f+2,4f+1]\cup[4f+5,5f+2],\\
E+R
={}&[0,f-2]\cup[f+1,2f+2]\cup[3f+1,4f+1]\cup[4f+5,5f+2],\\
R+R
={}&[0,f-3]\cup[f+2,2f+1]\cup[3f+1,4f]\cup[4f+6,5f+2],
\end{aligned}
\]
where
\[
R=\{f-1,f\}\cup[2f+3,3f]\cup[4f+2,4f+4].
\]
Again all three sumsets are disjoint from \(R\).

Therefore no member of the proposed periodic tail is a sum of two distinct members of \(T\).

### 3. Every omitted integer is blocked

The gap immediately after \(E\) was already handled by
\[
[3f+\delta,4f+\delta-1]
=f+[2f+\delta,3f+\delta-1].
\]

It remains to cover one residue period after \(4f+\delta\). Every later omitted integer is obtained from one of these witnesses by adding a multiple of \(M\) to a summand whose residue lies in \(R\).

For \(\delta=1\), the omitted integers in the first tail period have the following witnesses:
\[
\begin{array}{rcl}
[4f+3,5f] &=&(2f+1)+[2f+2,3f-1],\\
5f+1&=&f+(4f+1),\\
5f+2&=&f+(4f+2),\\
[5f+3,6f-1]&=&3f+[2f+3,3f-1],\\
6f+2&=&(2f+1)+(4f+1),\\
[6f+3,7f-1]&=&(4f+2)+[2f+1,3f-3],\\
7f&=&f+6f,\\
7f+1&=&f+(6f+1),\\
7f+2&=&3f+(4f+2),\\
8f+1&=&(2f+1)+6f,\\
8f+2&=&(2f+1)+(6f+1),\\
[8f+3,9f]&=&f+[7f+3,8f],\\
9f+1&=&3f+(6f+1).
\end{array}
\]

For \(\delta=2\),
\[
\begin{array}{rcl}
[4f+5,5f+2]&=&(2f+2)+[2f+3,3f],\\
5f+3&=&f+(4f+3),\\
5f+4&=&f+(4f+4),\\
[5f+5,6f+1]&=&(3f+1)+[2f+4,3f],\\
[6f+4,6f+6]&=&(2f+2)+[4f+2,4f+4],\\
[6f+7,7f+1]&=&(4f+4)+[2f+3,3f-3],\\
7f+2&=&f+(6f+2),\\
7f+3&=&f+(6f+3),\\
7f+4&=&3f+(4f+4),\\
7f+5&=&(3f+1)+(4f+4),\\
8f+4&=&(2f+2)+(6f+2),\\
8f+5&=&(2f+2)+(6f+3),\\
[8f+6,9f+3]&=&f+[7f+6,8f+3],\\
9f+4&=&(3f+1)+(6f+3).
\end{array}
\]
An interval with lower endpoint above its upper endpoint is simply empty.

Every displayed pair consists of distinct earlier selected integers. Moreover, in every witness at least one summand is either already a tail term or has residue in \(R\). If
\[
n=n_0+qM,\qquad q\ge1,
\]
replace such a summand \(y\) in the witness for \(n_0\) by \(y+qM\). This remains a selected tail term, stays below \(n\), and gives a distinct-pair representation of \(n\). Hence every integer outside \(T\) is forbidden at the moment the greedy construction reaches it.

Together with Step 2, this proves \(S_{f,2f+\delta}=T\).

### 4. Exact period and preperiod

Ordering one full tail block gives the difference word
\[
(1^\delta,\ 2f-2,\ 1,\ f+\delta+1,\ 1^{f-3},\ f+2).
\]
It contains \(f+\delta+1\) differences and has total sum \(M\).

For \(\delta=1\), the value \(2f-2\) occurs exactly once in the cyclic block when \(f\ge5\); for \(\delta=2\), the value \(f+2\) occurs exactly once. Thus the cyclic word cannot have a smaller period, proving minimality.

There are exactly \(f+1\) entries in \(E\). The transition from the last element of \(E\) to the first tail element has size \(f+1\), while \(f+1\) does not occur in the periodic difference block. Hence periodicity cannot begin earlier, and the minimal preperiod length is \(f+1\).

Finally,
\[
|R|=2+(f-2)+(\delta+1)=f+\delta+1,
\]
so the exact periodic description gives density
\[
\frac{|R|}{M}
=
\frac{f+\delta+1}{5f+2\delta-1}.
\]

## Verification

A standalone exact-integer check is included in `artifacts/verify_off_diagonal_2_sumfree.py`. It compares the theorem with the greedy definition for every
\[
5\le f\le300,\qquad \delta\in\{1,2\},
\]
through eight full tail periods, and separately checks the three modular sumset identities, including the diagonal pairs in \(R+R\). The deterministic output is in `artifacts/verification.txt`.

The computation is corroborative; the theorem is proved by the interval and residue argument above.

## Originality and limitations

To the best of our knowledge, the two infinite families above have not previously been proved. The September 2026 paper explicitly identifies \(g\le2f-1\) as the earlier proven region and presents its \(g=2f\) theorem as the new diagonal extension; the cases beyond the diagonal are supported there by conjectures and finite computations rather than a general proof.

Historical 0-additive work by Raymond Queneau and Steven Finch is directly relevant. Queneau's full 1972 article was not inspected here, so it remains the most important residual originality risk. The recent papers' own historical discussion describes Queneau's explicit cases as largely subsumed by their proven families, and targeted searches for the formulations \(S_{f,2f+1}\), \(S_{f,2f+2}\), and equivalent greedy strict 2-sumfree terminology did not locate an earlier infinite theorem. Finch's 1992 article and OEIS records document additional fixed-base regular sequences, but no coverage of these two variable-\(f\) families was found.

Relevant historical references:

- R. Queneau, *Sur les suites s-additives*, J. Combin. Theory Ser. A 12 (1972), 31–71, DOI: 10.1016/0097-3165(72)90083-0.
- S. R. Finch, *Are 0-Additive Sequences Always Regular?*, Amer. Math. Monthly 99 (1992), 671–673, DOI: 10.1080/00029890.1992.11995911.

The theorem is restricted to \(f\ge5\) and \(\delta=1,2\). It does not prove the general ultimate-periodicity conjecture, does not classify \(\delta\ge3\), and does not claim that the small excluded values of \(f\) follow the same formula.
