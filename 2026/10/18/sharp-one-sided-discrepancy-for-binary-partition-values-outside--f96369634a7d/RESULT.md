# Sharp one-sided discrepancy for binary-partition values outside a ternary quadratic form

## Finding
For each integer \(n\geq0\), let \(b(n)\) be the number of unrestricted partitions of \(n\) into powers of two (so \(b(0)=1\)). Set \(q(x,y,z)=x^2+y^2+2z^2\), with integral variables. For integer \(X\geq0\), define
\[
T(X)=\#\{1\leq n\leq X:\ b(2n)\notin q(\mathbb Z^3)\},\qquad D(X)=6T(X)-X.
\]
Then
\[
\boxed{D(X)\leq7\quad(X\geq0),\qquad D(17)=7,}
\]
and
\[
\boxed{\liminf_{X\to\infty}\frac{T(X)-X/6}{\log_2 X}=-\frac14.}
\]
In particular, \(T(X)/X\to1/6\); exactly five-sixths of the positive indices, in natural density, give representable values. Both the positive one-sided bound and the negative logarithmic coefficient are optimal.

There is also an exact digit characterization. Write \(n=4^a(8m+r)\), where \(a,m\geq0\), \(r\in\{1,3,5,7\}\), when \(\nu_2(n)\) is even, and set \(t_m=(-1)^{s_2(m)}\). The exceptional positive indices are precisely
\[
\begin{array}{c|cc}
& t_m=+1&t_m=-1\\ \hline
a=0&r=5&r=1\\
a\geq1&r=3&r=7
\end{array}
\]
No index of odd two-adic valuation is exceptional.

## Assumptions and scope
All counts are exact integer counts with \(X\) a nonnegative integer; \(\log_2 X\) occurs only for \(X>1\). Squares may include zero, and variables in \(q\) may be negative. Binary partitions allow arbitrary multiplicities of \(1,2,4,\dots\). All asymptotics refer to the positive integer index \(n\) in \(b(2n)\), not the ambient size of a represented integer. Two published ingredients are used: the exact local obstruction for \(q\) (Durham, Theorem 2), and the binary-partition valuation and congruences (Sobolewski--Ulas, Propositions 3.1, 3.2 and the last two relations of Proposition 3.7). The first displayed congruence of the latter Proposition 3.7 is not used.

## Proof
**1. Exact exception set.** Durham's theorem says that a positive integer fails to be represented by \(q\) precisely when it is \(4^j(16h+14)\). Sobolewski--Ulas Proposition 3.1 gives \(\nu_2(b(2n))=1\) when \(\nu_2(n)\) is even and \(2\) otherwise. Hence nonrepresentation is exactly the congruence \(b(2n)\equiv14\pmod{16}\). For odd \(u=8m+r\), the published congruences \(b(8v+2)\equiv2t_v\) and \(b(8v+6)\equiv6t_v\) modulo \(16\) give, for \(r=1,3,5,7\), respectively,
\[
b(2u)\equiv(2,6,-2,-6)t_m\pmod{16}.
\]
For every odd \(u\), \(b(8u)\equiv b(2u)+8\pmod{16}\). To check this carefully, put \(u=2v+1\) and use the partition recurrence:
\[
b(16v+8)=b(16v+4)+b(8v+2)+b(8v+4).
\]
If \(v=2m\), Propositions 3.2 and 3.7 evaluate the three terms modulo 16 as \(4t_m,2t_m,4t_m\), whereas \(b(4v+2)\equiv2t_m\). Their difference is \(8t_m\equiv8\). If \(v=2m+1\), those terms are \(-4t_m,-2t_m,4t_m\), whereas \(b(4v+2)\equiv6t_m\); the difference is \(-8t_m\equiv8\). Thus the asserted shift holds. The additional published congruence \(b(16v)\equiv b(4v)\pmod{32}\) implies \(b(2\cdot4^au)\equiv b(8u)\pmod{16}\) for every \(a\geq1\). Comparing to 14 gives exactly the displayed digit table.

**2. Counting recurrences.** For \(Y\geq0\) let \(P_0(Y)\) count the integers \(8m+(5\text{ if }t_m=1\text{ else }1)\leq Y\), and \(P_1(Y)\) count the integers \(8m+(3\text{ if }t_m=1\text{ else }7)\leq Y\). If \(Y=8m+r\), \(0\leq r<8\), then
\[
P_0(Y)=m+\mathbf1_{r\geq(5\text{ if }t_m=1\text{ else }1)},\quad
P_1(Y)=m+\mathbf1_{r\geq(3\text{ if }t_m=1\text{ else }7)}.
\]
Set \(Q(0)=0\), \(Q(Y)=P_1(Y)+Q(\lfloor Y/4\rfloor)\) for \(Y\geq1\). Counting each disjoint layer \(4^a(8m+r)\) gives
\[
T(X)=P_0(X)+Q(\lfloor X/4\rfloor).
\]
Write \(d(Y)=6Q(Y)-Y\). For \(Y=4v+r\) with \(0\leq r<4\), the recurrence reads
\[
d(4v+r)=d(v)+e(p,t,r),\quad p=v\bmod2,\quad t=t_{\lfloor v/2\rfloor}.
\]
Here are **all sixteen weights** in increasing order \(r=0,1,2,3\):
\[
\begin{array}{c|rrrr}
(p,t)&0&1&2&3\\ \hline
(0,+1)&0&-1&-2&3\\
(0,-1)&0&-1&-2&-3\\
(1,+1)&3&2&1&0\\
(1,-1)&-3&-4&-5&0
\end{array}
\]
The next state is \((p',t')=(r\bmod2,t(-1)^{p+\lfloor r/2\rfloor})\). This follows directly by writing \(v=2m+p\), applying the formula for \(P_1\), and noting \(t_{4m+2p+\lfloor r/2\rfloor}=t_m(-1)^{p+\lfloor r/2\rfloor}\).

**3. Two exact finite-state potentials.** On the ordered states \((0,+1),(0,-1),(1,+1),(1,-1)\), define
\[
U=(0,2,-1,3),\qquad H=(-1,-2,-2,0).
\]
Direct checking of the sixteen entries in the displayed table, with the stated state transition, gives two exact inequalities for every edge \(s\to s'\) of weight \(e\):
\[
e\leq U(s')-U(s),\qquad e+3\geq H(s')-H(s).
\]
Read the base-four digits of \(Y\) from the initial state \((0,+1)\); leading zeros cause no issue. Since \(d(0)=0\), telescoping the first inequality proves \(d(Y)\leq U(Y\bmod2,t_{\lfloor Y/2\rfloor})\). Telescoping the second along \(\ell\) base-four digits proves \(d(Y)\geq-3\ell-1\) (the endpoint potential is at least \(-2\), the initial potential is \(-1\)). At \(Y=0\), \(d(0)=0\).

**4. Sharp uniform upper bound.** Write \(X=8m+s\), \(0\leq s<8\), \(t=t_m\), \(Y=\lfloor X/4\rfloor\). The exact formula is
\[
D(X)=d(Y)+C(s,t),\qquad C(s,t)=6\mathbf1_{s\geq(5\text{ if }t=1\text{ else }1)}-s+\lfloor s/4\rfloor.
\]
For \(s=0,1,2,3\), the state at \(Y\) is \((0,t)\), with \(U=0\) or \(2\); for \(s=4,5,6,7\), it is \((1,t)\), with \(U=-1\) or \(3\). Checking these eight \(s\)-values against the two \(t\)-values gives \(D(X)\leq7\) always, with the maximum possible at \(s=1,t=-1\). Directly \(T(17)=4\), hence \(D(17)=24-17=7\). (The four exceptions through 17 are 5, 9, 12, and 17.)

**5. The logarithmic lower tail.** By the lower potential, \(d(Y)\geq-3\log_4(Y+1)-O(1)\); the correction \(C\) is uniformly bounded. Therefore \(D(X)\geq-3\log_4 X-O(1)\), which gives
\[
\liminf_{X\to\infty}\frac{T(X)-X/6}{\log_2 X}\geq-\frac14.
\]
For the reverse inequality, define \(X_k=(768\cdot16^k-28)/5\), a positive integer for every \(k\geq0\). Its base-four digits are \(2(12)^k110\), while \(Y_k=\lfloor X_k/4\rfloor\) has digits \(2(12)^k11\). Reading the exact state table shows \(d(Y_k)=-7-6k\). Moreover \(X_k\bmod8=4\) and \(t_{\lfloor X_k/8\rfloor}=+1\), because the binary digits of \(Y_k\) contain exactly \(2k+3\) ones and end in \(01\). Thus \(C(4,+1)=-3\) and
\[
D(X_k)=-10-6k,\qquad \log_2 X_k=4k+O(1).
\]
It follows that the same liminf is at most \(-1/4\), proving equality. The two bounds together imply \(T(X)=X/6+O(\log X)\) and the asserted natural density.

## Verification
The dependency-free companion `verify.py` checks all sixteen edges of both potential certificates, 60,000 independently computed binary-partition congruences and their cumulative exceptional-index counts, 120,000 state bounds, the sharp witness \(X=17\), and nine members of the explicit negative-discrepancy sequence. Invoke `python3 verify.py` from a directory containing the supplied source file. The symbolic proof above, not the finite numerical range, supplies the all-index assertions. The exact quadratic representation criterion and published partition congruences are cited external theorems, not computationally reproved here.

## Relationship to prior work
Sobolewski and Ulas (arXiv:2211.16622, first released 2022-11-29; *Results in Mathematics* 78, 188 (2023)) study the same binary-partition values for the **different** quadratic form \(x^2+y^2+z^2\). Their Remark 1.1 explicitly names \(x^2+y^2+2z^2\) as an extension and their Proposition 3.7 supplies useful congruences, but their explicit counting and discrepancy theorems in Section 6 concern three equal squares or colored partitions, not this weighted form. The present digit characterization uses their ingredients; the sharp upper discrepancy constant and exact negative-logarithmic liminf require the further count recursion and dual finite-state potentials given above. Durham (arXiv:1509.02590, 2015) proves the exact representation obstruction for the weighted ternary form but says nothing about binary partition values. Consequently neither result alone gives the stated discrepancy law. A broader unlocated automatic-sequence discrepancy theorem could overlap; no independent priority certification is claimed.

## Limitations
The result concerns \(b(2n)\) and the single diagonal form \(x^2+y^2+2z^2\), not all binary-partition values for arbitrary colored multiplicities or other forms. Its lower tail is normalized along integer cutoffs \(X\), and no exact finite-\(X\) minimum is claimed. Searches cannot prove uniqueness or absolute priority. All statements of verification are same-model, not independently audited.

## References
1. B. Sobolewski and M. Ulas, *Values of binary partition function represented by a sum of three squares*, arXiv:2211.16622v1 (2022-11-29); *Results in Mathematics* **78** (2023), article 188. Full text: https://link.springer.com/article/10.1007/s00025-023-01966-8 .
2. G. Durham, *Representation of Integers by Ternary Quadratic Forms: A Geometric Approach*, arXiv:1509.02590v1 (2015-09-09), Theorem 2. Full text: https://arxiv.org/html/1509.02590v1 .
