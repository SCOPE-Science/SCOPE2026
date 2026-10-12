# A multiplicative counterexample scheme for Pongsriiam’s divisor-sum progression converse

## Finding
For real \(s\), define
\[
\sigma_s(n)=\sum_{d\mid n}d^s.
\]
Pongsriiam's Problem 2 asks whether \(ad=bc\) and
\[
\sigma_s(an+b)<\sigma_s(cn+d)\qquad(n\ge1)
\]
force \(a\mid c\), or at least \(\gcd(a,b)\mid\gcd(c,d)\). The answer is no for every real \(s\).

More generally, let \(u,v,q,r\in\mathbb N\) such that every prime divisor of \(uv\) divides \(q\), \(\gcd(r,uv)=1\), \(u\nmid v\), and \(\sigma_s(u)<\sigma_s(v)\). Put
\[
a=uq,\quad b=ur,\quad c=vq,\quad d=vr.
\]
Then \(ad=bc\), the strict divisor-sum inequality holds for every \(n\ge1\), and both proposed divisibility conclusions fail.

For every real \(s\), one may take
\[
(a,b,c,d)=
\begin{cases}
(12,2,18,3),&s>0,\\
(18,3,12,2),&s<0,\\
(36,2,162,9),&s=0.
\end{cases}
\]

## Assumptions and scope
Here \(\mathbb N=\{1,2,3,\ldots\}\). The divisor-power sum \(\sigma_s\) is multiplicative for every real \(s\). The notation \((a,b)\) in the focal paper denotes \(\gcd(a,b)\). The result settles Problem 2, the proportional case \(ad=bc\); it does not address the distinct sign-change questions for linearly independent vectors.

## Proof
Let \(m_n=qn+r\). If \(p\mid uv\), then \(p\mid q\) and \(p\nmid r\), so \(p\nmid m_n\). Hence \(\gcd(m_n,uv)=1\). Also
\[
an+b=u m_n,\qquad cn+d=v m_n.
\]
Therefore multiplicativity gives
\[
\sigma_s(an+b)=\sigma_s(u)\sigma_s(m_n)
<\sigma_s(v)\sigma_s(m_n)=\sigma_s(cn+d)
\]
for every \(n\ge1\). Moreover,
\[
ad=(uq)(vr)=(ur)(vq)=bc.
\]
Since \(a=uq\) and \(c=vq\),
\[
a\mid c\iff u\mid v.
\]
Also
\[
\gcd(a,b)=u\gcd(q,r),\qquad \gcd(c,d)=v\gcd(q,r),
\]
so
\[
\gcd(a,b)\mid\gcd(c,d)\iff u\mid v.
\]
Thus \(u\nmid v\) makes both proposed conclusions false.

If \(s>0\), choose \((u,v,q,r)=(2,3,6,1)\). Then \(1+2^s<1+3^s\), giving \((a,b,c,d)=(12,2,18,3)\). If \(s<0\), choose \((3,2,6,1)\); then \(1+3^s<1+2^s\), giving \((18,3,12,2)\). If \(s=0\), then \(\sigma_0=\tau\); choosing \((2,9,18,1)\) uses \(\tau(2)=2<3=\tau(9)\) and gives \((36,2,162,9)\). These cases cover all real \(s\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic for
\[
s\in\{-3,-2,-1,0,1,2,3\}
\]
and checks the appropriate explicit progression through \(n=1000\) in each case. It also checks the algebraic side conditions for the three templates. The replay reports `VERIFY_OK` after 7,000 exact progression inequalities and 24 algebraic template checks. These finite checks are regression evidence only; the proof above is universal.

## Relationship to prior work
Pongsriiam's Example 2.2 gives a sufficient construction with \(a\mid c\), and Problem 2 asks whether the implication can be reversed, perhaps only at the gcd level. The construction above shows that a shared coprime progression can factor out of both divisor sums, leaving a fixed local comparison \(\sigma_s(u)<\sigma_s(v)\) even when \(u\nmid v\).

Later papers by Ding, Pan and Sun and by Wang solve other questions from the same source concerning sign changes or cumulative comparisons such as \(30n\) versus \(30n+k\). Their stated results do not imply the proportional-case converse. Targeted searches for Problem 2, the three explicit progressions, and the shared-factor mechanism did not locate an equivalent result.

## Limitations
The theorem disproves the two proposed converse conclusions but does not classify all proportional pairs having a permanent divisor-sum inequality. The explicit quadruple depends on the sign of \(s\). The principal originality risk is an unindexed informal observation of the same elementary multiplicative construction.

## References
1. Prapanpong Pongsriiam, “Sums of divisors on arithmetic progressions,” arXiv:2110.00237v1 (2021); *Periodica Mathematica Hungarica* 88 (2024), 443–460, DOI 10.1007/s10998-023-00566-x.
2. Yuchen Ding, Hao Pan, and Yu-Chen Sun, “Solutions to some sign change problems on functions involving sums of divisors,” *Periodica Mathematica Hungarica* 90 (2025), 299–306, DOI 10.1007/s10998-024-00620-2.
3. Rui-Jing Wang, “On a problem of Pongsriiam on the sum of divisors,” *Bulletin of the Australian Mathematical Society* 111 (2025), 13–18, DOI 10.1017/S0004972724000492.
4. Rui-Jing Wang, “On a problem of Pongsriiam on the sum of divisors, II,” arXiv:2408.00979v1 (2024).
