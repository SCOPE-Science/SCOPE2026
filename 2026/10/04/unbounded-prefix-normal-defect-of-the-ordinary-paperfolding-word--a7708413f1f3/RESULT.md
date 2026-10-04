# Unbounded prefix-normal defect of the ordinary paperfolding word
## Finding
Let \(\mathfrak p=p_1p_2\cdots\) be the ordinary paperfolding word, where \(p_n=0\) if the odd part of \(n\) is congruent to \(1\pmod 4\), and \(p_n=1\) if it is congruent to \(3\pmod 4\). For every integer \(m\ge2\), define
\[
L_m=\left\lfloor\frac{2^m}{3}\right\rfloor.
\]
Then the factor
\[
p_{L_{m+1}+1}\cdots p_{2^m-1}
\]
has length \(L_m\) and contains exactly \(m-1\) more \(1\)s than the prefix \(p_1\cdots p_{L_m}\). Therefore
\[
F_{\mathfrak p}^{1}(L_m)-P_{\mathfrak p}(L_m)\ge m-1,
\]
so the prefix-normal defect is unbounded. In particular, for every fixed integer \(c\ge0\), the word \(1^c\mathfrak p\) is not prefix normal.

## Assumptions and scope
For an infinite binary word \(w\), let \(P_w(n)\) be the number of \(1\)s in its prefix of length \(n\), and let
\[
F_w^1(n)=\max\{|u|_1:u\text{ is a factor of }w,\ |u|=n\}.
\]
The word \(w\) is prefix normal exactly when \(P_w(n)=F_w^1(n)\) for every \(n\ge1\).

The ordinary paperfolding convention used here is the one in Madill--Rampersad and Cicalese--Lipták--Rossi:
\[
p_n=
\begin{cases}
0,&\text{if the odd part of }n\text{ is }1\pmod4,\\
1,&\text{if the odd part of }n\text{ is }3\pmod4.
\end{cases}
\]
No assertion is made about other choices of paperfolding instructions.

## Proof
Write
\[
S(N)=\sum_{j=1}^{N}p_j.
\]
Separating even and odd indices in the number-theoretic definition gives, for every \(N\ge1\),
\[
S(2N)=S(N)+\left\lfloor\frac N2\right\rfloor
\]
and
\[
S(2N+1)=S(N)+\left\lfloor\frac N2\right\rfloor+(N\bmod2).
\]
These recurrences imply two elementary identities.

First, for every \(m\ge2\),
\[
S(2^m-1)=2^{m-1}-1.
\]
This follows by induction from the second recurrence.

Second, with \(L_m=\lfloor2^m/3\rfloor\),
\[
S(L_m)=\left\lfloor\frac{L_m}{2}\right\rfloor-
\left\lfloor\frac{m-1}{2}\right\rfloor.
\]
Indeed, \(L_{m+1}=2L_m\) when \(m\) is even and \(L_{m+1}=2L_m+1\) when \(m\) is odd. In the first case \(L_m\) is odd, and in the second it is even. Substituting these two alternatives into the prefix-sum recurrences proves the displayed formula inductively, starting at \(m=2\).

Because powers of two are never divisible by \(3\),
\[
L_m+L_{m+1}=2^m-1.
\]
Moreover, exactly one of \(L_m,L_{m+1}\) is odd, so
\[
\left\lfloor\frac{L_m}{2}\right\rfloor+
\left\lfloor\frac{L_{m+1}}{2}\right\rfloor
=2^{m-1}-1.
\]
Hence
\[
S(L_m)+S(L_{m+1})=2^{m-1}-m.
\]

Now consider
\[
W_m=p_{L_{m+1}+1}\cdots p_{2^m-1}.
\]
Its length is
\[
2^m-1-L_{m+1}=L_m.
\]
Its number of \(1\)s is
\[
|W_m|_1=S(2^m-1)-S(L_{m+1}).
\]
Therefore
\[
|W_m|_1-S(L_m)
=(2^{m-1}-1)-S(L_{m+1})-S(L_m)
=m-1.
\]
This proves the exact witness gap and thus
\[
F_{\mathfrak p}^{1}(L_m)-P_{\mathfrak p}(L_m)\ge m-1.
\]

Finally fix \(c\ge0\) and choose \(m\ge c+2\). The length-\(L_m\) prefix of \(1^c\mathfrak p\) contains
\[
c+S(L_m-c)\le c+S(L_m)
\]
ones, while the factor \(W_m\), occurring wholly inside the paperfolding tail, contains
\[
S(L_m)+(m-1)>S(L_m)+c
\]
ones. Thus \(1^c\mathfrak p\) violates the prefix-normal condition at length \(L_m\).

## Verification
The bundled `verify.py` reconstructs the ordinary paperfolding word directly from the odd-part definition. It checks the two prefix-sum recurrences for \(1\le N\le199999\), verifies the closed formulas and the exact witness gap for twenty dyadic levels \(2\le m\le21\), and directly checks the prepending obstruction for \(0\le c\le17\).

These computations are finite consistency checks of the symbolic proof. The infinite conclusion rests on the displayed recurrences and induction, not on extrapolation from the checked range.

## Relationship to prior work
Cicalese, Lipták, and Rossi introduced a systematic study of infinite prefix normal words. They show that every suitable balanced word can be made prefix normal by prepending finitely many \(1\)s, prove specifically that two prepended \(1\)s suffice for the Thue--Morse word, and contrast this with the Champernowne word, for which no finite number suffices. In the same paper they devote a subsection to the ordinary paperfolding word and determine its prefix normal forms from its abelian complexity, but they do not state whether finitely many prepended \(1\)s can make the paperfolding word itself prefix normal.

Madill and Rampersad determine the abelian complexity of the ordinary paperfolding word, prove it is unbounded and \(2\)-regular, and use the same odd-part definition. Their result controls extremal factor populations but does not compare them with the particular initial prefixes needed for the finite-prepending question.

Targeted searches under the finite-prepending formulation, prefix-normal defect terminology, the explicit lengths \(\lfloor2^m/3\rfloor\), and paperfolding maximum-\(1\) formulations did not locate a prior statement of the logarithmic witness family above. This is evidence of non-coverage, not a proof that no unindexed observation exists.

## Limitations
The theorem is for the ordinary paperfolding word with the stated indexing and bit convention. It proves a logarithmically growing explicit lower bound on the prefix-normal defect along the lengths \(L_m\); it does not claim that \(m-1\) is the exact maximum defect at those lengths, nor does it classify arbitrary paperfolding instruction sequences.

Originality remains subject to the possibility of an unindexed note, thesis, or differently phrased consequence of older paperfolding discrepancy formulas.

## References
1. F. Cicalese, Z. Lipták, and M. Rossi, “On Infinite Prefix Normal Words,” arXiv:1811.06273, first public version 2018-11-15; Theoretical Computer Science 859 (2021), 134–148, DOI 10.1016/j.tcs.2021.01.015.
2. B. Madill and N. Rampersad, “The abelian complexity of the paperfolding word,” arXiv:1208.2856, first public version 2012-08-14.
