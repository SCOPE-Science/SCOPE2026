# Exact periodicity of the strict greedy 2-sumfree family \(S_{f,2f+1}\)

## Result

For integers \(f\ge 5\), let \(S_{f,2f+1}\) be the strict greedy 2-sumfree sequence beginning with \(f,2f+1\): after the prescribed first two entries, each next entry is the least larger integer that is not a sum of two distinct earlier entries. Put
\[
M=5f+1.
\]
Then
\[
\boxed{
S_{f,2f+1}
=\{f\}\cup[2f+1,3f]\cup\bigcup_{k\ge0}(X_k\cup Y_k\cup Z_k),
}
\]
where integer intervals are understood inclusively and
\[
X_k=\{4f+1+kM,\;4f+2+kM\},
\]
\[
Y_k=\{6f+kM,\;6f+1+kM\},
\]
\[
Z_k=[7f+3+kM,\;8f+kM].
\]

Consequently the first-difference sequence has minimal preperiod length \(f+1\) and minimal period length \(f+2\). A period is
\[
\boxed{(1,\;2f-2,\;1,\;f+2,\;\underbrace{1,\ldots,1}_{f-3\text{ times}},\;f+2)}.
\]
Its sum is \(5f+1=M\), so the eventual characteristic pattern is periodic modulo \(M\).

In the notation of van Berkel and Bosma, this proves their period-length Conjecture 5 on the entire infinite line
\[
d=g-f=f+1,\qquad f\ge5,
\]
for which Definition 3 predicts period length \(\mathcal L_f(f+1)=f+2\). Their paper proves periodicity for the neighboring region through \(g\le 2f\) and supplies computational evidence beyond it; the family \(g=2f+1\) is therefore the first uniform line immediately beyond that proved boundary.

## Proof

Let
\[
Q=[2f+1,3f],\qquad P=\{f\}\cup Q.
\]
The proposed periodic tail has residue set modulo \(M\)
\[
R=A\cup B\cup C,
\]
where
\[
A=\{f-1,f\},\qquad B=[2f+2,3f-1],\qquad C=\{4f+1,4f+2\}.
\]
Indeed, in each period the residues in \(C\) occur first, those in \(A\) occur after adding \(M\), and those in \(B\) occur after adding \(M\).

### 1. The displayed set is strict 2-sumfree

First consider sums involving only the finite prefix \(P\). We have
\[
f+Q=[3f+1,4f],
\]
and the sums of two distinct members of \(Q\) form
\[
Q\mathbin{\widehat{+}}Q=[4f+3,6f-1].
\]
Neither interval meets \(P\), and neither meets the proposed tail: the first tail entries are \(4f+1,4f+2,6f,6f+1\), with no tail entries in between.

Next, sums of a prefix residue with a tail residue avoid \(R\) modulo \(M\). The possibilities lie in
\[
\begin{aligned}
f+A&=[2f-1,2f],\\
f+B&=[3f+2,4f-1],\\
f+C&\equiv\{0,1\}\pmod M,\\
Q+A&=[3f,4f],\\
Q+B&\equiv[4f+3,5f]\cup[0,f-2]\pmod M,\\
Q+C&\equiv[f+1,2f+1]\pmod M.
\end{aligned}
\]
All of these are disjoint from
\(R=\{f-1,f\}\cup[2f+2,3f-1]\cup\{4f+1,4f+2\}\).

Finally, tail-plus-tail residues also avoid \(R\). Allowing even equal residues (which only strengthens the exclusion),
\[
\begin{aligned}
A+A&\subseteq[2f-2,2f],\\
A+B&\subseteq[3f+1,4f-1],\\
A+C&\equiv\{5f,0,1\}\pmod M,\\
B+B&\equiv[4f+4,5f]\cup[0,f-3]\pmod M,\\
B+C&\equiv[f+2,2f]\pmod M,\\
C+C&\equiv[3f+1,3f+3]\pmod M.
\end{aligned}
\]
Again every displayed residue lies outside \(R\). Hence no proposed tail element is a sum of two distinct proposed sequence elements. Together with the prefix check, the whole displayed set is strict 2-sumfree.

### 2. Every omitted candidate is forced to be skipped

Because the proposed set is 2-sumfree, every displayed element is eligible when reached. It remains to show that every omitted integer larger than the prescribed second seed is already a sum of two distinct earlier displayed elements.

Between the prefix and the first periodic block,
\[
[3f+1,4f]=f+Q.
\]
After \(X_0\), the first gap is
\[
[4f+3,6f-1]=Q\mathbin{\widehat{+}}Q,
\]
the full distinct-pair sum interval of \(Q\).

For every \(k\ge0\), the gap after \(Y_k\) and the gap after \(Z_k\) are respectively
\[
[6f+2+kM,7f+2+kM]=Q+X_k,
\]
\[
[8f+1+kM,9f+1+kM]=Q+Y_k.
\]
For \(k\ge1\), the gap after \(X_k\) is
\[
[4f+3+kM,6f-1+kM]=Q+Z_{k-1}.
\]
Each equality follows because the sum of the indicated consecutive intervals is consecutive; where a two-point set is used, the two adjacent sum intervals overlap. In every representation the two summands are distinct and smaller than the represented integer.

These gaps, together with the displayed blocks \(X_k,Y_k,Z_k\), partition all integers after \(Q\). Thus induction through the integers shows that the greedy construction selects exactly the displayed set.

### 3. Minimal preperiod and period

The differences through the finite prefix and into the first tail block are
\[
f+1,\;\underbrace{1,\ldots,1}_{f-1\text{ times}},\;f+1.
\]
After that, the differences repeat as
\[
W=(1,2f-2,1,f+2,1^{f-3},f+2).
\]
Hence a preperiod of length \(f+1\) and a period of length \(f+2\) exist.

For \(f\ge5\), the value \(f+1\) does not occur in \(W\), so the last preperiod difference cannot belong to any periodic tail; the preperiod length is therefore minimal. Also \(2f-2\neq f+2\) and occurs exactly once in \(W\). Its successive occurrences in the infinite tail are separated by exactly \(f+2\), so no shorter period is possible. Thus both lengths are minimal.

## Context and significance

Van Berkel and Bosma formulate the conjecture that every strict greedy 2-sumfree sequence is eventually periodic and give explicit conjectures for all period lengths. They report exact proofs in a substantial region, including the boundary \(g=2f\), and computational verification over large finite parameter ranges. The theorem above advances that boundary by proving the next uniform line \(g=2f+1\) for every \(f\ge5\), and it gives the complete sequence rather than only its period length.

The case \(f=3,g=7\) is already worked out explicitly as an example in their paper. Small \(f\) have exceptional behavior in their conjectural period tables, so the theorem is stated only for the uniform regime \(f\ge5\).

## Verification

The proof is general and does not depend on computation. The accompanying standard-library script constructs the greedy sequence and checks the closed form for \(5\le f\le80\) through the first 300 sequence terms for each \(f\), as well as the predicted eventual difference period.

## Limitations

Originality is asserted only to the best of our knowledge. The source conjecture is very recent, so indexing of simultaneous or immediately subsequent work may be incomplete. Searches for the exact family \(S_{f,2f+1}\), the equivalent condition \(g=2f+1\), the displayed block formulas, and follow-up work located no proof of this infinite family. The theorem settles one parameter line, not the general periodicity conjecture.

## References

1. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522 (2026). https://arxiv.org/abs/2609.18522
2. D. van Berkel and W. Bosma, *On t-sumfree sequences*, arXiv:2609.16843 (2026). https://arxiv.org/abs/2609.16843
