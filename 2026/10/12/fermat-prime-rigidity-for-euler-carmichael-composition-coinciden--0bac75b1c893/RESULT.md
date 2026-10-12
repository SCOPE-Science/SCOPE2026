# Fermat-prime rigidity for Euler–Carmichael composition coincidences on \(2^a p^b\)

## Finding
For every odd prime \(p\), and all integers \(a\ge1\), \(b\ge2\), define
\[
Q_{p,a,b}=\frac{\varphi(\lambda(2^a p^b))}{\lambda(\varphi(2^a p^b))}.
\]
Here \(\varphi\) is Euler's totient and \(\lambda\) the Carmichael function. Then \(Q_{p,a,b}\) is a positive integer, independent of \(b\). There is a complete equality classification:
\[
\varphi(\lambda(2^a p^b))=\lambda(\varphi(2^a p^b))
\iff p=3\quad\text{or}\quad
\bigl(p=2^t+1\text{ prime},\ t\ge2,\ a\ge t+2\bigr).
\]
For \(p=2^t+1\) prime (including \(p=3\) with \(t=1\)), the quotient is exactly
\[
Q_{p,a,b}=2^{\max\{0,t+2-\max(a,3)\}}.
\]
When \(p-1\) has an odd factor greater than one, \(Q_{p,a,b}\) is even, so equality is impossible. The classification gives all permitted exponents, not merely a finite search.

## Assumptions and scope
Throughout, \(p\) is an odd prime, \(a\) and \(b\) are integers with \(a\ge1\) and \(b\ge2\). Write \(p-1=2^t u\), with \(t=\nu_2(p-1)\ge1\) and \(u\) odd. For the Carmichael function on powers of two define
\[
c(j)=\nu_2(\lambda(2^j))=
\begin{cases}0,&j=1,\\1,&j=2,\\j-2,&j\ge3.\end{cases}
\]
Set \(S=a+t-1\), \(T=\max(t,c(a))\), and write \(\lambda(u)=2^hK\), where \(h\ge0\) and \(K\) is odd. Put \(E=\max(t,c(S),h)\) and \(H=u\varphi(u)/\operatorname{lcm}(u,K)\). All functions at \(1\) take their usual value \(1\), and \(h=0\) when \(u=1\).

## Proof
**Step 1: an exact local composition formula.** For odd prime powers, \(\lambda(p^b)=\varphi(p^b)=p^{b-1}(p-1)\). Because \(\lambda(2^a)=2^{c(a)}\),
\[
\lambda(2^a p^b)=2^T p^{b-1}u,
\qquad
\varphi(2^a p^b)=2^S p^{b-1}u.
\]
Since \(u<(p-1)<p\) and \(\lambda(u)\le u\), the prime \(p\) divides neither \(u\) nor \(\lambda(u)\). Thus applying \(\varphi\) to the first equality and \(\lambda\) to the second gives
\[
\varphi(\lambda(2^a p^b))=2^{T+t-1}p^{b-2}u\varphi(u),
\]
\[
\lambda(\varphi(2^a p^b))=2^E p^{b-2}\operatorname{lcm}(u,K).
\]
Consequently
\[
\boxed{Q_{p,a,b}=2^{T+t-1-E}\frac{u\varphi(u)}{\operatorname{lcm}(u,K)}}.
\]
This identity holds for every allowed \(a,b,p\), and the right side has no \(b\)-dependence. Moreover, \(K\mid\lambda(u)\mid\varphi(u)\), so \(H\) is an integer.

**Step 2: integrality and a parity obstruction.** Put \(L=T+t-1\). We have \(L\ge t\ge1\). The bound \(c(S)\le L\) holds in three cases: for \(a=1\), \(S=t\) and \(c(t)\le t-1\le L\); for \(a=2\), \(S=t+1\) and \(c(t+1)\le t\le L\); for \(a\ge3\), \(S=a+t-1\ge3\), hence \(c(S)=a+t-3\le T+t-1=L\). Thus \(E\le\max(L,h)\).

If \(u>1\), let \(f=\nu_2(\varphi(u))\ge1\). Since \(\lambda(u)\mid\varphi(u)\), \(h\le f\), and \(K\) and \(u\) are odd, \(\nu_2(H)=f\). Therefore
\[
\nu_2(Q_{p,a,b})=L+f-E
\ge L+f-\max(L,f)=\min(L,f)\ge1.
\]
Because \(H\) is integral, this also proves \(Q_{p,a,b}\) is an even integer when \(u>1\).

If \(u=1\), we have \(h=0\) and \(H=1\); the bound \(E\le L\) proves integrality in this case as well. The exact quotient reduces to
\[
Q_{p,a,b}=2^{\max(t,c(a))+t-1-\max(t,c(a+t-1))}.
\]
Evaluating the three cases \(a=1\), \(a=2\), and \(a\ge3\) with the explicit formula for \(c\) yields
\[
Q_{p,a,b}=2^{\max\{0,t+2-\max(a,3)\}}.
\]
For \(t=1\), the only prime \(p=2^t+1\) is \(3\), and this exponent is zero for every \(a\ge1\). For \(t\ge2\), it is zero precisely when \(a\ge t+2\). Conversely, every such choice makes the ratio one, so the equality classification is both necessary and sufficient. This completes the proof.

## Verification
The standalone `verify.py` uses elementary integer factorization and independent implementations of \(\varphi\) and \(\lambda\). It evaluated both compositions directly for all odd primes below \(300\), each \(1\le a\le10\) and \(b\in\{2,3,4\}\): 1830 exact cases. It checked integrality, the closed formula, the equality classification, and independence from \(b\). Separate exact tests cover the Fermat primes \(257\) and \(65537\) at both sides of the threshold. Successful output begins `VERIFY_OK cases=1830`. This finite computation is only a consistency check; the proof above handles all primes and exponents.

## Relationship to prior work
Banks, Luca, Saidak and Stănică, *Compositions with the Euler and Carmichael Functions* (2005), establish global lower and upper counting estimates for \(\varphi(\lambda(n))=\lambda(\varphi(n))\) and a normal-order theorem for the quotient. Their explicit lower-bound construction produces particular solutions but does not classify all solutions in the entire unbounded two-prime-power family \(2^a p^b\) with \(b\ge2\). Their results do not imply the parity obstruction, \(b\)-independence, or Fermat-prime equivalence here. OEIS A123101 records the same equality as an integer sequence and supplies finite tables and code, not an infinite characterization. The related Banks–Friedlander–Luca–Pappalardi–Shparlinski paper on *Coincidences in the values* (2006) studies images of the two functions, rather than the two orderings of their composition.

## Limitations
The theorem does not classify inputs outside \(2^a p^b\) with \(a\ge1,b\ge2\); it does not determine whether infinitely many Fermat primes exist. The ratio may be greater than one even for Fermat primes below the indicated exponent threshold. Prior-work coverage is assessed from accessible primary results and database records; the possibility of an unindexed equivalent elementary derivation remains. The exact initial online posting date of the original 2005 paper is not established by its journal issue label.

## References
1. W. D. Banks, F. Luca, F. Saidak, and P. Stănică, *Compositions with the Euler and Carmichael Functions*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **75** (2005), 215–244. DOI: 10.1007/BF02942044. Open author copy: https://uncg.edu/~f_saidak/hamburg.pdf.
2. OEIS Foundation, A123101, *lambda(phi(n))=phi(lambda(n))* (entry credited to R. J. Mathar, 2006-09-27), https://oeis.org/A123101.
3. W. D. Banks, J. B. Friedlander, F. Luca, F. Pappalardi, and I. E. Shparlinski, *Coincidences in the values of the Euler and Carmichael functions*, Acta Arithmetica **122** (2006), 207–234. DOI: 10.4064/aa122-3-1.
4. MaRDI mathematical publication record Q2581052, bibliographic exact-date record 2006-01-10 for reference 1, https://portal.mardi4nfdi.de/wiki/Compositions_with_the_Euler_and_Carmichael_functions.
