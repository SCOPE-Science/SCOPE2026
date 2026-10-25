# Exact first-zero waiting-time law for modular Fibonacci-like recurrences

## Finding
For each integer \(m\ge1\), let \(A_0=a\), \(A_1=b\), and \(A_{t+2}=A_{t+1}+A_t\) modulo \(m\), where \((a,b)\) ranges over every pair of residues. Define the first-zero waiting time
\[
T_m(a,b)=\min\{t\ge0:A_t\equiv0\pmod m\},
\]
with value \(\infty\) when no zero occurs. Write \(F_0=0\), \(F_1=1\), \(F_{t+2}=F_{t+1}+F_t\), and let \(z(d)\) be the least positive integer \(t\) with \(d\mid F_t\). Set \(z(1)=1\), and \(\varphi(1)=1\).

**Exact first-hit theorem.** For every integer \(m\ge1\) and every integer \(t\ge0\),
\[
\boxed{\#\{(a,b)\bmod m:T_m(a,b)=t\}
=\sum_{\substack{d\mid m\\z(d)>t}}\varphi(d).}
\]
This is refined by the following uniformity statement: on the stratum \(\gcd(a,b,m)=m/d\), exactly \(\varphi(d)\) initial pairs have first-zero time \(t\), for each \(0\le t<z(d)\), and no pair on that stratum has any other finite first-zero time.

Consequently the exact number of pairs ever reaching zero and the sum of their finite waiting times are
\[
\sum_{d\mid m}\varphi(d)z(d),\qquad
\frac12\sum_{d\mid m}\varphi(d)z(d)(z(d)-1),
\]
respectively. Thus the mean waiting time conditional on reaching zero is the quotient of these two expressions. The distribution is nonincreasing with \(t\); its drop from time \(t-1\) to \(t\) is \(\sum_{d\mid m,\ z(d)=t}\varphi(d)\). The largest finite first-zero time is \(z(m)-1\).

For \(m=8\), the counts at \(t=0,1,2,3,4,5\) are \(8,7,7,6,6,6\), giving \(40\) pairs that eventually hit zero and \(24\) that never do.

## Assumptions and scope
All residues are taken in \(\mathbb Z/m\mathbb Z\); both initial coordinates are freely chosen, including zero. The first-zero index begins at \(t=0\). Every positive modulus is permitted, including \(m=1\). The integer \(z(d)\) is the rank of apparition of the ordinary Fibonacci sequence and is finite, since the invertible Fibonacci companion map permutes the finite state space. The gcd of residue representatives and \(m\) is independent of the choice of representatives.

## Proof
**1. Reduce a gcd stratum.** Fix \(d\mid m\) and set \(g=m/d\). Every pair with \(\gcd(a,b,m)=g\) can be written uniquely as \((a,b)=g(u,v)\pmod m\), where \(\gcd(u,v,d)=1\). Reducing the recurrence modulo \(d\) preserves the exact set of zero indices: \(A_t\equiv0\pmod m\) if and only if the recurrence from \((u,v)\) has zero at the same time \(t\), modulo \(d\). Therefore it suffices to analyze primitive pairs modulo \(d\).

**2. Return period of the zero-coordinate line.** Let \(U(u,v)=(v,u+v)\) modulo \(d\); its determinant is \(-1\), so it is bijective. For \(e=(0,1)\), induction gives \(U^t e=(F_t,F_{t+1})\). The standard identity \(\gcd(F_t,F_{t+1})=1\) makes \(F_{z(d)+1}\) a unit modulo \(d\). The companion-matrix identity
\[
U^t=\begin{pmatrix}F_{t-1}&F_t\\F_t&F_{t+1}\end{pmatrix}\quad(t\ge1)
\]
shows that \(U^{z(d)}=cI\), with the unit \(c=F_{z(d)+1}\pmod d\) (since \(F_{z(d)-1}=F_{z(d)+1}-F_{z(d)}\)). For \(d=1\), the same assertion is interpreted in the one-element ring. Hence the zero indices in the ordinary Fibonacci sequence are exactly the multiples of \(z(d)\): divide an index by \(z(d)\), use the scalar identity, and invoke minimality of \(z(d)\).

**3. Disjoint classes of primitive first hitters.** Every primitive state with first coordinate zero is \((0,c)\), where \(c\) is a unit modulo \(d\). For every \(0\le j<z(d)\) and unit \(c\), form
\[
P_{j,c}=U^{-j}(0,c).
\]
This state reaches a zero at time \(j\). It cannot reach zero at an earlier \(s<j\), because this would make the nonzero index \(j-s<z(d)\) an ordinary Fibonacci zero modulo \(d\). The states \(P_{j,c}\) are distinct: a collision with distinct indices \(j>k\) would force \(F_{j-k}\equiv0\pmod d\), contradicting minimality; equal indices force equal \(c\). Conversely, any primitive state reaching zero at some time \(t\) can be moved backward using the scalar identity \(U^{z(d)}=cI\) until its first zero lies among indices \(0,\ldots,z(d)-1\). Thus all primitive first-hitters occur exactly once among these states, and there are exactly \(\varphi(d)\) at each time \(j\).

**4. Sum over gcd strata.** The reduction in step 1 is a bijection on each stratum. Summing the primitive counts over all \(d\mid m\) gives the boxed histogram. Summing over times \(j=0,\ldots,z(d)-1\) gives \(\varphi(d)z(d)\) hitters and total waiting time \(\varphi(d)z(d)(z(d)-1)/2\) per stratum. The drop formula follows by subtracting adjacent histogram values. Finally \(z(d)\mid z(m)\) whenever \(d\mid m\), because ordinary Fibonacci zero indices form multiples of their ranks. The \(d=m\) stratum has \(\varphi(m)>0\) states at time \(z(m)-1\); all other finite times are at most this. This completes the proof.

## Verification
A standalone, standard-library-only Python program, `verify.py`, independently computes the first-zero index of every initial pair for moduli \(1\) through \(90\), stopping each search at the first repeated two-coordinate state when no zero exists. It separately computes ranks, totients, gcd-stratum sizes, histograms, and waiting-time totals. The successful replay checked \(247065\) initial pairs, \(5741\) stratum/time cells, and the first \(16\) OEIS A232656 totals. These finite tests corroborate but do not prove the general theorem; the proof above is independent of a finite search.

## Relationship to prior work
OEIS A064414 (submitted in October 2001) asks which moduli force every Fibonacci-like recurrence to contain zero. Avila and Khovanova (2014), *Free Fibonacci Sequences*, introduce OEIS A232656 and study zero-avoiding initial pairs and their behavior. The **aggregate** identity \(\sum_{d\mid m}\varphi(d)z(d)\) was explicitly proposed in A232656 in October 2017 and entered there as an equality in May 2021, so this aggregate identity is **not claimed as original**. Renault (2013), *The Period, Rank, and Order of the (a,b)-Fibonacci Sequence Mod m*, develops companion-matrix and rank methods for recurrences started at zero and one; his rank theory is background, not a claim to an original matrix identity here.

The distinct statement here is the full first-zero **histogram**, its gcd-stratum uniformity, explicit jump sizes and waiting-time moment for **all initial pairs and all moduli**. In the inspected sources, the reported total counts and prime-case waiting-time heuristic do not supply this time-resolved distribution. An equivalent formulation in broader recurrence or finite-dynamical-system literature remains a residual novelty risk.

## Limitations
The theorem concerns Fibonacci-like recurrences with both coefficients equal to one and moduli in the positive integers. It does not give closed elementary evaluations of each rank \(z(d)\), and it does not analyze the actual intervening integer divisions of nonmodular, normalized free-Fibonacci dynamics. Independence of mathematical validation is not claimed. Exhaustive historical novelty is not proven.

## References
1. OEIS A064414, *Numbers that divide at least one term in every Fibonacci sequence*, entry dated October 15, 2001. https://oeis.org/A064414
2. B. Avila and T. Khovanova, *Free Fibonacci Sequences*, arXiv:1403.4614 (2014), especially sections 7, 10 and 11. https://arxiv.org/abs/1403.4614
3. OEIS A232656, *The number of pairs of numbers below n that, when generating a Fibonacci-like sequence modulo n, contain zeros*, original entry November 27, 2013, formula comments by L. Kleinwaks (2017) and R. Ollerton (2021). https://oeis.org/A232656
4. M. Renault, *The Period, Rank, and Order of the (a,b)-Fibonacci Sequence Mod m*, Mathematics Magazine 86 (2013), 372–380. https://webspace.ship.edu/msrenault/fibonacci/RenaultPeriodRankOrderMathMag.pdf
5. OEIS A001177, *Rank of apparition of n in Fibonacci numbers*. https://oeis.org/A001177
6. OEIS A389401, *Composite numbers that divide at least one term in every Fibonacci sequence*. https://oeis.org/A389401
