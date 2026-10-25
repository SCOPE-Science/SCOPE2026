# An infinite prime-shift progression for reciprocal quadratic divisibility

## Finding
For an integer \(k\ge1\), put \(Q_k(T)=T^2-kT+1\). Call \((x,y)\) a reciprocal divisibility pair if \(x,y\ge2\) and
\[
x\mid Q_k(y),\qquad y\mid Q_k(x).
\]

**Theorem (prime-shift progression).** For each integer \(t\ge0\), write
\[
k=41+21t,\quad H=5+4t,\quad u_0=7,\quad u_1=79+49t,
\qquad u_{n+1}=H u_n-u_{n-1}+k\quad(n\ge1).
\]
Then \(u_n\) is a strictly increasing sequence of positive integers, every adjacent pair \((u_n,u_{n+1})\) is coprime and satisfies both reciprocal divisibilities, and thus every parameter \(k\equiv41\pmod{21}\), \(k\ge41\), has infinitely many positive reciprocal divisibility pairs. Infinitely many of these parameters also satisfy that \(k+2\) is **prime**: choose the infinitely many primes \(p\equiv1\pmod{21}\) with \(p\ge43\), and set \(k=p-2\). The exceptional-prime-shift assertion is a uniform infinite family, not merely an individual example.

## Proof
We use the classical Vieta-chain method, without asserting it is new. A general elementary lemma suffices. Let integers \(k,d\ge1\), \(2\le a<b\) and \(H\ge2\) satisfy
\[
Q_k(a)=-db,\qquad b=Ha+d+k.
\]
Set \(u_{-1}=-d,\ u_0=a,\ u_1=b\) and \(u_{n+1}=Hu_n-u_{n-1}+k\). On the conic
\[
F(X,Y)=X^2+Y^2-k(X+Y)+1-HXY=0
\]
we have \(F(-d,a)=Q_k(a)+d(Ha+d+k)=0\). Viewed as a monic quadratic in \(X\), the two roots are \(X\) and \(HY+k-X\). Therefore \((X,Y)\mapsto(Y,HY+k-X)\) preserves \(F=0\). Consequently \(F(u_{n-1},u_n)=0\) for every \(n\ge0\), equivalently
\[
Q_k(u_n)=u_{n-1}u_{n+1}.
\]
The initial inequalities imply all later terms increase, since
\[
u_{n+1}-u_n=(u_n-u_{n-1})+(H-2)u_n+k>0.
\]
The identity at consecutive indices gives the two required divisibilities. Moreover, \(\gcd(u_n,u_{n+1})=1\), because any common divisor of those terms divides both \(u_n\) and \(Q_k(u_n)\equiv1\pmod{u_n}\). Increasingness makes the pairs distinct.

For \(k=41+21t\), choose \(d=3\), \(a=7\), \(b=79+49t\), \(H=5+4t\). Direct calculation gives
\[
Q_k(7)=50-7(41+21t)=-3(79+49t),
\]
and
\[
7(5+4t)+3+(41+21t)=79+49t.
\]
Thus all hypotheses of the lemma hold. Finally, \(k+2=43+21t\) runs through the arithmetic progression of positive integers congruent to \(1\pmod{21}\). Because \(\gcd(1,21)=1\), Dirichlet's theorem guarantees infinitely many primes in this progression, proving the prime-shift conclusion.

## Assumptions, comparison, and limits
All assertions concern positive integers and the exact progression \(k=41+21t\); they do not classify other prime-shift parameters, all solution orbits, or the density of solution pairs. The Vieta recurrence, coprimality mechanism, and broad shifted-composite existence statement are **not new**. In *A system of quadratic Diophantine equations*, W. H. Mills (1953), final section on systems with finitely many positive solutions, proved that composite \(k+2\) for \(k>8\) already forces infinitely many positive solutions, and exhibited \(k=41\) as a prime-shift exception. Therefore the previously proposed density-one parameter consequence and its shifted-composite range follow from Mills's theorem plus standard prime-density estimates; they are intentionally **not presented as new findings** here. The specific all-\(t\) progression and the infinitely many prime-shift parameters were not explicitly identified in the inspected Mills paper. Given the general arithmetic-chain framework, equivalent implicit consequences or unindexed prior work remain historical originality risks.

The arithmetic identity, strictly increasing orbit, and progression are proved here for every \(t\ge0\). Finite checks of initial terms are corroborative only. Dirichlet's theorem is invoked, not reproved. The result does not imply that primality of \(k+2\) is sufficient or necessary for finiteness; it explicitly exhibits a positive-density-in-primes collection of exceptions among the primes \(p\equiv1\pmod{21}\).

## Primary references
1. W. H. Mills, *A system of quadratic Diophantine equations*, Pacific Journal of Mathematics **3** (1953), 209–220, especially p. 220. https://msp.org/pjm/1953/3-1/pjm-v3-n1-p15-p.pdf
2. M. A. Alekseyev and D. I. Khomovsky, *Congruence Jumping in Polynomial Divisibility Systems: Arithmetic Structure and Solution Sets*, arXiv:2610.00808 (2026), §4, §7.1. https://arxiv.org/abs/2610.00808
3. Dirichlet's theorem on primes in reduced residue classes (standard arithmetic theorem).
