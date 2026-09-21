# Exact maximum size and structure of length-five non-overlapping codes

Let \(S(q,n)\) denote the largest cardinality of a \(q\)-ary non-overlapping code of length \(n\): no nonempty proper prefix of any codeword is a suffix of any (not necessarily distinct) codeword. Let \(N(q,n)\) denote the number of maximum codes over a fixed labelled alphabet of size \(q\).

## Theorem

For length five,
\[
S(2,5)=2,\qquad S(3,5)=17.
\]
For every \(q\ge 4\), put
\[
\ell=\left\lfloor\frac{4q+2}{5}\right\rfloor,
\qquad a=q-\ell=\left\lfloor\frac{q+2}{5}\right\rfloor.
\]
Then
\[
\boxed{S(q,5)=a\ell^4
      =\left(q-\left\lfloor\frac{4q+2}{5}\right\rfloor\right)
       \left\lfloor\frac{4q+2}{5}\right\rfloor^4.}
\]
Moreover, every maximum code for \(q\ge4\) has one of the following two forms. Partition the alphabet as \(\Sigma=A\sqcup B\), where \(|A|=a\) and \(|B|=\ell\). Then the code is either
\[
A B^4
\quad\text{or}\quad
B^4 A.
\]
Consequently,
\[
\boxed{N(q,5)=2\binom{q}{a}=2\binom{q}{\ell}\qquad(q\ge4).}
\]

Thus Blackburn's 2015 conjecture that, for each fixed length, the \(k=n-1\) construction is maximum for all sufficiently large alphabets holds at length \(5\), in fact for every \(q\ge4\). The two smaller alphabets are genuine exceptions to that structural conclusion.

## Proof

Stanovnik--Moškon--Mraz characterize maximum non-overlapping codes by the integer program SQN. For \(n=5\), write its variables as \((x_i,y_i)_{i=1}^4\):
\[
S(q,5)=\max\sum_{i=1}^4 x_i y_{5-i},
\]
subject to
\[
x_1+y_1=q,
\qquad
x_i+y_i=\sum_{j=1}^{i-1}x_jy_{i-j}\quad(2\le i\le4),
\]
with \(x_1,y_1>0\) and all variables nonnegative integers. Their left-right symmetry lets us assume
\[
a=x_1\le b=y_1,
\qquad a+b=q.
\]
Set
\[
P=ab,\qquad c=x_2,\qquad y_2=P-c.
\]
Then
\[
Q=x_3+y_3=a(P-c)+cb=aP+c(b-a).
\]
Writing \(d=x_3\), \(y_3=Q-d\), and
\[
R=x_4+y_4=a(Q-d)+c(P-c)+db,
\]
write \(e=x_4\), so \(y_4=R-e\). The objective is
\[
\Phi=a(R-e)+c(Q-d)+d(P-c)+eb.
\]
Because \(b\ge a\), \(\Phi\) is maximized in \(e\) at \(e=R\). After substitution,
\[
\Phi=a^3b^2+2ab^2c-ac^2+d(b^2-2c).
\]
Hence the optimum in \(d\) is an endpoint:
\[
d=Q\quad\text{if }c\le b^2/2,
\qquad
d=0\quad\text{if }c\ge b^2/2.
\]
The corresponding objective functions are
\[
F_0(c)=a(a^2b^2+2b^2c-c^2)
\]
and
\[
F_1(c)=a^3b^2+a^2b^3+(-2a^2b+ab^2+b^3)c+(a-2b)c^2.
\]

### 1. The unbalanced regime

Suppose \(a\le b/3\). Then \(0\le c\le P=ab\le b^2/3\), so only the \(F_1\) branch can be optimal. Since \(F_1\) is concave, its real vertex is
\[
c_*=rac{b(b-a)(2a+b)}{2(2b-a)}.
\]
A direct simplification gives
\[
c_*\ge ab\iff a\le b/3.
\]
Therefore \(F_1\) is increasing throughout \([0,P]\), and
\[
\Phi\le F_1(P)=ab^4.
\]
Equality forces \(c=P\), then \(d=Q\) and \(e=R\). Thus equality in this regime gives exactly the size vector corresponding to the code \(AB^4\), or its left-right reversal.

### 2. The balanced regime

Suppose \(a\ge b/3\). First,
\[
F_0(c)\le F_0(P)=2a^2b^3,
\]
because \(F_0'(c)=2a(b^2-c)\ge0\) on \([0,P]\).

For \(F_1\), evaluation at its real vertex gives
\[
F_1(c)\le
\frac{b^4(5a^2+2ab+b^2)}{4(2b-a)}.
\]
Put \(r=a/b\in[1/3,1]\). Since \(q=(1+r)b\), the two normalized bounds are
\[
g(r)=\frac{5r^2+2r+1}{4(2-r)(1+r)^5},
\qquad
h(r)=\frac{2r^2}{(1+r)^5}.
\]
Their derivatives are
\[
g'(r)=\frac{5(r-1)(4r^2-r+1)}{4(2-r)^2(1+r)^6}\le0,
\]
and
\[
h'(r)=\frac{-2r(3r-2)}{(1+r)^6}.
\]
Therefore
\[
g(r)\le g(1/3)=\frac{81}{1024},
\qquad
h(r)\le h(2/3)=\frac{216}{3125}<\frac{81}{1024}.
\]
Every feasible solution in the balanced regime consequently satisfies
\[
\Phi\le\frac{81}{1024}q^5. \tag{1}
\]
Equality in (1) is possible only through the \(F_1\) bound with \(r=1/3\) and \(c=P\), which is again the simple \(AB^4\) size vector.

### 3. Comparison with the simple construction

For a partition with \(|A|=t\) and \(|B|=q-t\), the code \(AB^4\) has size
\[
f_q(t)=t(q-t)^4.
\]
The continuous function has its unique maximum at \(t=q/5\). Comparing the two adjacent integers in the five residue classes modulo \(5\) gives the unique integer maximizer
\[
t=a=\left\lfloor\frac{q+2}{5}\right\rfloor,
\qquad
q-t=\ell=\left\lfloor\frac{4q+2}{5}\right\rfloor.
\]
For \(q\ge10\), the nearest integer to \(q/5\) differs from \(q/5\) by at most \(2/5\), hence \(t/q\in[4/25,6/25]\). Since \(u(1-u)^4\) increases up to \(u=1/5\) and then decreases,
\[
\frac{f_q(t)}{q^5}
\ge\min\left\{
\frac4{25}\left(\frac{21}{25}\right)^4,
\frac6{25}\left(\frac{19}{25}\right)^4
\right\}
>\frac{81}{1024}.
\]
For \(q=4,5,6,8,9\), direct substitution gives the same weak comparison with (1); equality occurs only at \(q=4,8\), where the equality conditions above again force the simple size vector.

The remaining value \(q=7\) is small enough to settle exactly. With \(a\le b\), the possibilities are \((a,b)=(1,6),(2,5),(3,4)\). The first gives \(6^4=1296\). For \((2,5)\),
\[
F_1(c)=-8c^2+135c+700\quad(0\le c\le10),
\]
whose integer maximum is \(1268\). For \((3,4)\), the two branches have maxima \(1088\) and \(1152\). Hence \(S(7,5)=1296\), again attained only by the simple construction and its reversal.

Combining the unbalanced and balanced cases proves the formula and the uniqueness of the optimal SQN size vector up to left-right reversal for every \(q\ge4\). When \(c=P,d=Q,e=R\), the recursive partitions are forced to be
\[
L_2=L_1R_1,\quad L_3=L_2R_1,\quad L_4=L_3R_1,
\]
with the corresponding \(R_i\) empty, so the resulting code is exactly \(AB^4\). The reversed vector gives \(B^4A\).

Finally, the counting formula of Stanovnik--Moškon--Mraz applies because \(n=5\) is odd. Once \(A=L_1\) is chosen, all later partitions in either optimal size vector are forced. There are \(\binom qa\) choices for \(A\), and two orientations, proving
\[
N(q,5)=2\binom qa.
\]

For \(q=2\), direct evaluation of SQN gives \(S(2,5)=2\). For \(q=3\), symmetry reduces to \((a,b)=(1,2)\); the three possibilities \(c=0,1,2\) yield objective maxima \(12,17,16\), respectively. Hence \(S(3,5)=17\).

## Reproducibility

`artifacts/verify_length5.py` independently evaluates the length-five SQN objective on finite parameter ranges. It exhausts the endpoint-reduced SQN for \(2\le q\le60\), performs a fuller nested enumeration for \(2\le q\le7\), verifies uniqueness of the stated orientation for \(4\le q\le60\), and checks the integer maximizer formula through \(q=1000\). `artifacts/verification_output.txt` records the verified output.

The computation is a finite sanity check; the all-\(q\) result rests on the proof above.

## Prior literature and originality

Blackburn introduced a broad construction and proved exact formulas only through length three; his Conjecture 2 states that for every fixed \(n\), the \(k=n-1\) construction should be maximum for all sufficiently large \(q\). Stanovnik, Moškon and Mraz later characterized all maximal non-overlapping codes and gave the exact SQN integer optimization formulation. They proved the exact length-four formula and reported computational solutions for \(q\le6\) at larger lengths, while explicitly noting that no simple formula was then available for larger codeword length and that the Blackburn construction fails at length five for some small parameters.

The 2025 follow-up by the same authors concerns balanced and run-length-constrained variants and still cites the 2024 finite computations for unrestricted maximum codes. Searches through the present under `non-overlapping`, `cross-bifix-free`, `mutually uncorrelated`, `strong comma-free`, exact length-five notation, and formula variants did not locate the theorem above, its sharp threshold \(q=4\), or the classification/count of all maxima. A 2026 paper on generalized \((t_1,t_2)\)-overlap-free codes addresses a broader overlap constraint family rather than an exact unrestricted \(S(q,5)\) determination.

Accordingly, originality is claimed **to the best of our knowledge**. A residual risk remains that the same fixed-length consequence has appeared under older synchronization terminology or as an unstated special case of another extremal formulation.

## Scientific limitations

The theorem is specific to block length five. It uses the exact SQN characterization of Stanovnik--Moškon--Mraz as its starting structural theorem. It does not determine \(S(q,n)\) for \(n\ge6\), nor does it classify the exceptional maximum-code structures at \(q=2,3\).

## References

1. S. R. Blackburn, *Non-overlapping codes*, IEEE Transactions on Information Theory 61 (2015), 4890--4894. DOI: https://doi.org/10.1109/TIT.2015.2456634 ; arXiv: https://arxiv.org/abs/1303.1026
2. L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), 1299--1326. DOI: https://doi.org/10.1007/s10623-023-01344-z
3. L. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, Computational and Applied Mathematics 44 (2025), 109. DOI: https://doi.org/10.1007/s40314-024-03055-0
4. H. Yang, Y. Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, IEICE Transactions on Fundamentals E109-A (2026), 757--762. DOI: https://doi.org/10.1587/transfun.2025EAL2050
