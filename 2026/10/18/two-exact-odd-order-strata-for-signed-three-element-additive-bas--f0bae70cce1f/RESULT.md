# Two exact odd-order strata for signed three-element additive bases

## Finding
Let \(h=12k+11\) for an integer \(k\geq0\), and put
\[
N=\frac{h^2+6h+1}{4}.
\]
For a three-element set of integers \(A\) containing a negative element, let \(\ell_h(A)\) be the largest \(n\geq0\) for which every integer in \([0,n]\) is a sum of exactly \(h\) elements of \(A\), with repetitions allowed. Put \(n_h^{\flat}(2)=\max_A\ell_h(A)\). Then
\[
\boxed{n_h^{\flat}(2)=N-3\quad\text{if }5\nmid(k+1),}
\]
and
\[
\boxed{n_h^{\flat}(2)=N-4\quad\text{if }5\mid(k+1)\text{ and }7\nmid(k+1).}
\]
The respective optimal sets are \(\{-2,3,(h-3)/2\}\) and \(\{-3,4,(h-5)/2\}\). There is no assertion about the remaining values where \(35\mid(k+1)\).

## Assumptions and scope
The interval convention is inclusive; \(hA\) consists of sums of **exactly** \(h\) elements of the set, not at most \(h\). Three distinct integers are required and only the least must be negative. The theorem applies to \(h\equiv11\pmod{12}\) with \(h\geq11\), and the stated divisibility conditions are ordinary integer divisibility. The primary mathematical classification is additive number theory, MSC 11B13.

## Proof
Write \(h=2m+1\), so \(m=6k+5\), \(Y=m+1=6(k+1)\), and \(N=m^2+4m+2\). We give a construction lemma and then two upper bounds.

**Construction lemma.** Suppose integers \(t\geq1\), \(m\geq2t+1\) satisfy \(\gcd(2t+1,m+1)=1\). Then
\[
A_t=\{-t,t+1,m+1-t\}\quad\text{satisfies}\quad
\ell_{2m+1}(A_t)=m^2+4m+1-t=N-t-1.
\]
Indeed set \(R=2t+1\) and \(Y=m+1\). The sums using \(q\) copies of the largest element and \(s\) copies of the middle element, with \(q+s\leq h\), are
\[
-ht+qY+sR,\qquad 0\leq q\leq h,\quad 0\leq s\leq h-q.
\]
Because \(Y\) is invertible modulo \(R\), each residue class modulo \(R\) corresponds to exactly one \(q_0\in[0,R-1]\); all its admissible indices are \(q=q_0+iR\). For fixed \(q\), the represented members of that residue class fill the arithmetic progression, with difference \(R\), between
\[
L_q=-ht+qY\quad\text{and}\quad U_q=-ht+qY+R(h-q).
\]
The progression for \(q+R\) starts no later than one step after \(U_q\) precisely when \(q\leq m+1\), since \(L_{q+R}-U_q=R(q-m)\). Thus each residue class is filled continuously, in steps of \(R\), from \(L_{q_0}\) through \(U_{q_*}\), where \(q_*\) is its unique representative in \([m+2,m+1+R]\). Here \(q_*\leq h\), since \(m\geq R\). Initial points satisfy
\[
L_{q_0}\leq-ht+(R-1)Y=t<R,
\]
so no nonnegative point of that residue class precedes its first represented point. The next index \(q_*+R\), if admissible, starts at least two progression steps after \(U_{q_*}\), and every still later index starts even farther right; therefore the first omitted nonnegative point of that residue class is \(U_{q_*}+R\). Finally, \(U_q=h(t+1)+q(m-2t)\) increases with \(q\). As the \(q_*\) range over \([m+2,m+1+R]\), the first omitted nonnegative integer overall is
\[
U_{m+2}+R=N-t.
\]
This proves the lemma, including attainment and sharpness for each displayed construction.

**Upper bounds.** Suppose some \(A=\{a,a+x,a+y\}\) with \(a<0\), \(1\leq x<y\) covers \([0,N-d]\), for \(d\in\{2,3\}\). As \(N-d\geq h+1\), the elementary gap and gcd constraints for three-stamp interval bases imply \(y\leq h+1\) and \(\gcd(x,y)=1\): otherwise the first \(h+2\) consecutive integers cannot all be represented. These constraints also follow from Lemma 2.2 of van Doorn, Monticone and Nathanson (2026).

Consider the residue \(ha-x\pmod y\). A represented integer in this residue requires at least \(y-1\) copies of \(a+x\), because \(x\) is invertible modulo \(y\). Taking one representative in \([0,y-1]\), and another in \([N-d-y+1,N-d]\), gives, respectively,
\[
ha\leq U=(y-1)(1-x),\qquad
ha\geq L=N-d-hy+(y-1)(y-x-1).
\]
Consequently \(U-L=d-(y-m-2)^2\geq0\). Because \(d\leq3\), one must have \(y=m+2+j\) where \(j\in\{-1,0,1\}\). Put \(r=x-1\), and let \(v=U-ha\). Thus
\[
0\leq r\leq m+j,\qquad 0\leq v\leq d-j^2,
\]
and integrality of \(a\) forces
\[
(1+2j)r+2v\equiv0\pmod h.
\]
For \(j=0\), the nonnegative quantity \(r+2v\) is smaller than \(h\) when \(d=2\) and \(m\geq5\), or when \(d=3\) and \(m\geq29\). Hence \(r=v=0\), which implies \(a=0\), a contradiction.

For \(j=-1\), the congruence is \(-r+2v\equiv0\pmod h\); its absolute value is less than \(h\), so \(r=2v\). The choice \(v=0\) again forces \(a=0\). If \(d=2\), then \(v=1\), whence \(x=3\), but \(y=m+1=6(k+1)\), contrary to \(\gcd(x,y)=1\). If \(d=3\) and \(5\mid(k+1)\), then \(v\in\{1,2\}\), giving \(x\in\{3,5\}\); each shares a factor with \(y=6(k+1)\), again impossible.

For \(j=1\), the nonnegative quantity \(3r+2v\) is strictly below \(2h\) under the same respective conditions \((d=2,m\geq5)\) or \((d=3,m\geq29)\). The zero case gives \(a=0\), so the congruence requires \(3r+2v=h\). Thus \(r\) is odd and \(x=r+1\) is even. But \(y=m+3=6k+8\) is also even, contradicting \(\gcd(x,y)=1\).

We have proved that no eligible set covers \([0,N-2]\), giving \(n_h^{\flat}(2)\leq N-3\) for every \(k\geq0\). If \(5\mid(k+1)\), then \(m\geq29\) and the argument with \(d=3\) likewise shows that \([0,N-3]\) cannot be covered, giving \(n_h^{\flat}(2)\leq N-4\).

When \(5\nmid(k+1)\), take \(t=2\) in the construction lemma: \(\gcd(5,Y)=1\), so \(A_2=\{-2,3,m-1\}\) attains \(N-3\). If \(5\mid(k+1)\) and \(7\nmid(k+1)\), take \(t=3\): \(\gcd(7,Y)=1\) and \(m\geq29\), so \(A_3=\{-3,4,m-2\}\) attains \(N-4\). Both claimed equalities follow. \(\square\)

## Verification
Run `python3 verify.py` (Python standard library only). The program directly forms each finite sumset for representative cases, checks the construction lemma in small ranges, and independently enumerates all possible high-range candidates allowed by the stated inequalities to test the obstructions. The analytic proof, rather than these finite checks, establishes the infinite theorem.

## Relationship to prior work
Van Doorn, Monticone and Nathanson (arXiv:2610.19470v1, October 14, 2026) prove that \(n_h^{\flat}(2)<n_h(2)\) for every odd \(h\) and establish the classical benchmark, but do not evaluate the signed optimum on the infinite congruence families above. The current proof adapts their residue obstruction, retaining the slack at distances two and three, and combines it with a new explicit progression-covering lemma. Nathanson (arXiv:2605.26425v1, May 26, 2026) introduces related interval-basis invariants but does not imply these signed odd-order equalities. Classical ordinary postage-stamp results for nonnegative denominations cannot cover these exact negative-denomination extrema. A prior unindexed construction or equivalent treatment remains possible.

## Limitations
The remaining congruence subfamily \(35\mid(k+1)\) is not classified. The proof is specific to odd \(h\equiv11\pmod{12}\) and three-element bases; it makes no assertion about four or more elements or the interval-shifted variant. No independent external audit has been performed.

## References
1. W. van Doorn, P. Monticone, M. B. Nathanson, *Positivity and negativity for h-bases for n*, arXiv:2610.19470v1, October 14, 2026, https://arxiv.org/html/2610.19470v1 (especially Lemma 2.2 and Theorem 4.1).
2. M. B. Nathanson, *Problems in additive number theory, VII: The structure of additive h-bases for n*, arXiv:2605.26425v1, May 26, 2026, https://arxiv.org/html/2605.26425v1 (Sections 2 and 4).
3. A. Stöhr, *Gelöste und ungelöste Fragen über Basen der natürlichen Zahlenreihe. I, II*, J. Reine Angew. Math. 194 (1955), 40–65, 111–140.
