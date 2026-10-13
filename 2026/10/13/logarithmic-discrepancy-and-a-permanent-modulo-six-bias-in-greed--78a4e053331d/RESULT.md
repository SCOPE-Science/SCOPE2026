# Logarithmic discrepancy and a permanent modulo-six bias in greedy coprime records

## Finding
Define the permutation \(f\) by \(f(1)=1\), \(f(2)=3\), and, for every integer \(n\ge3\), by taking \(f(n)\) to be the least positive integer not used previously and relatively prime to \(f(n-1)\). A *record* is a value \(f(n)\) at a turning point \(n>3\) with \(f(n)-f(n-1)>1\). Let \(R\) be the set of records and, for \(a\in\{1,5\}\), set
\[
C_a(X)=\#\{r\in R:r\le X,\ r\equiv a\pmod6\}.
\]
There exist positive constants \(\delta_1,\delta_5\) such that, as real \(X\to\infty\),
\[
C_a(X)=\delta_a X+O(\log X) \quad(a\in\{1,5\}).
\]
They have explicitly convergent rational series described below, with certified finite truncations. The two densities are *not equal*; indeed
\[
\delta_1-\delta_5>\frac1{35},
\]
and the following strict rational certificate applies:
\[
\frac{379045337581044}{13082761331670030}
<\delta_1-\delta_5<
\frac{379045337581046}{13082761331670030}.
\]
Thus their difference is approximately \(0.028972884849888\). No other residue class modulo \(6\) contains any record.

## Assumptions and scope
Write \(p_k\) for the \(k\)-th prime and \(P_k=\prod_{i=1}^k p_i\). For every positive integer \(t\), let \(\lambda(t)\) be the least prime not dividing \(t\). The record list starts with \(5\) and satisfies the previously known recurrence
\[
r_{j+1}=r_j+\lambda(r_j-1)-1.
\]
This recurrence is equivalent to the turning-point definition above, not a new claim. For \(n\ge3\) and \(a\in\{1,5\}\), define
\[
 w_n(a)=\#\{r\in R:p_{n+1}\le r\le P_n+1,\ r\equiv a\pmod6\}
\]
and, for \(k\ge4\), define
\[
 s_k(a)=\#\{r\in R:p_k\le r<p_{k+1},\ r\equiv a\pmod6\}.
\]
All statements are unconditional, with no upper restriction on the record size or the prime index. The asymptotic bound concerns counts among *all* positive integers, not the relative density among primes.

## Proof
**Prime records and primorial replication.** Every prime \(q\ge5\) belongs to \(R\). Indeed, if consecutive records \(r<r'\) skipped such a prime \(q\), then with \(t=r-1\) the integer \(q-t\) would satisfy \(1<q-t<\lambda(t)\) and \(\gcd(q-t,t)=\gcd(q,t)=1\), contradicting the defining least-nondivisor property of \(\lambda(t)\). The initial record list through \(31\) is
\[
5,7,11,13,17,19,23,25,29,31.
\]
In particular \(P_3+1=31\) is a record. Inductively suppose \(P_n+1\) is a record and put \(P=P_n\) and \(q=p_{n+1}\). If \(0<t<P\), some prime dividing \(P\) does not divide \(t\), so \(\lambda(t+P)=\lambda(t)\). Also \(\lambda(jP)=q\) for each \(1\le j<q\). The deterministic record path from \(q\) to \(P+1\) therefore repeats translated by \(jP\), for every \(0\le j<q\); successive translated blocks join at \(jP+1\), followed by a gap of non-records up to \(jP+q\). Consequently \(P_{n+1}+1=qP+1\) is a record and there is an **exact disjoint union**
\[
R\cap[p_{n+1},P_{n+1}+1]
=\bigsqcup_{j=0}^{p_{n+1}-1}
 \left((R\cap[p_{n+1},P_n+1])+jP_n\right).
\]
The intervals on the right are separated by gaps, so no additional record is omitted. This proves the induction and the primorial replication directly from the record recurrence. Every record lies in one of the two classes \(1,5\pmod6\): the initial \(r=5\) does, and \(r-1\) is even so \(\lambda(r-1)\) is odd; if \(r\equiv1\pmod3\), then \(3\mid(r-1)\) so \(\lambda(r-1)\ne3\) and \(r^{\prime}=r+\lambda(r-1)-1\not\equiv0\pmod3\), whereas if \(r\equiv2\pmod3\), then \(\lambda(r-1)=3\) and \(r^{\prime}\equiv1\pmod3\). In each case the next record remains odd and coprime to \(6\).

**Residue-specific recurrence and limiting densities.** Since \(6\mid P_n\), all translates above preserve the residue modulo \(6\). Removing records below the new lower endpoint yields, for every \(n\ge3\),
\[
 w_{n+1}(a)=p_{n+1}w_n(a)-s_{n+1}(a).
\]
The base counts are \(w_3(1)=5\) and \(w_3(5)=4\). Therefore \(w_n(a)/P_n\) decreases to
\[
\delta_a=\frac{w_3(a)}{30}-\sum_{k=4}^{\infty}\frac{s_k(a)}{P_k}.
\]
Because every \(p_k\) with \(k\ge4\) is odd,
\(0\le s_k(a)\le(p_{k+1}-p_k)/2<p_k/2\) by Bertrand's postulate. Using \(P_k\ge 2P_{k-1}\), the exact tail satisfies
\[
0\le e_n(a):=w_n(a)-P_n\delta_a
=P_n\sum_{k=n+1}^{\infty}\frac{s_k(a)}{P_k}<1.
\]
The base values show \(\delta_1>4/30\) and \(\delta_5>3/30\). From the recurrence also
\[
p_{n+1}e_n(a)=s_{n+1}(a)+e_{n+1}(a).
\]

**Logarithmic counting error.** Define \(E_n(a)=\max_{0\le x\le P_n}|C_a(x)-\delta_a x|\), initially for integer \(x\); allowing real \(x\) changes the bound by at most \(1\). The exact replicated blocks show that every full interval \((jP_n,(j+1)P_n]\), \(1\le j<p_{n+1}\), contains exactly \(w_n(a)\) records in residue \(a\): the endpoint \(jP_n+1\) replaces the omitted endpoint \(P_n+1\) of the copied base block. With \(q=p_{n+1}\), \(P=P_n\), and \(x=tP+u\), \(1\le t\le q-1\), \(0\le u<P\), one obtains, when \(u\ge q\), the **exact identity**
\[
C_a(tP+u)=t\,w_n(a)+C_a(u).
\]
Set \(H_a=C_a(q-1)\), so \(0\le H_a\le q-1\). For \(1\le u<q\), no new translated record occurs after \(tP+1\), hence the other **exact identity** is \(C_a(tP+u)=H_a+t w_n(a)\). At \(u=0\), subtract \(1\) from the right-hand side only when \(a=1\), as the record \(tP+1\) is then beyond the endpoint; this also applies when \(t=q\), giving the endpoint \(x=qP\). Since \(0\le\delta_a<1\) and \(t e_n(a)\le s_{n+1}(a)+1\) for \(t\le q\), the small-initial-segment cases contribute at most \(s_{n+1}(a)+2q\), whereas \(u\ge q\) contributes at most \(E_n(a)+s_{n+1}(a)+1\). Therefore
\[
 E_{n+1}(a)\le\max\bigl(E_n(a)+s_{n+1}(a)+1,\ s_{n+1}(a)+2p_{n+1}\bigr).
\]
The base record list gives \(E_3(a)\le5<2p_4\). Since \(s_{n+1}(a)\le(p_{n+2}-p_{n+1})/2\), and successive odd primes differ by at least \(2\), induction yields the **explicit bound**
\[
 E_n(a)\le2p_{n+1}\qquad(n\ge3).
\]
For \(P_n\le X\le P_{n+1}\), it follows that \(|C_a(X)-\delta_a X|\le2p_{n+2}+1\). Finally, the prime number theorem gives \(p_{n+2}=O(\log P_n)=O(\log X)\), proving the claimed \(O(\log X)\) error for every real \(X\ge2\).

**Strict bias and certified digits.** Two steps of the recurrence give
\(w_4(1)=34\), \(w_4(5)=28\), \(w_5(1)=374\), and \(w_5(5)=307\). Hence
\[
\delta_1-\delta_5
=\frac{67-e_5(1)+e_5(5)}{2310}
>\frac{66}{2310}=\frac1{35}.
\]
Continuing the exact recurrence through \(n=14\) uses only the finite prime-gap record counts \(s_k(a)\), never enumeration up to \(P_{14}\). It produces \(P_{14}=13082761331670030\), \(w_{14}(1)=2117724294581810\), and \(w_{14}(5)=1738678957000765\). Since both errors lie in \([0,1)\), the displayed strict rational enclosure of \(\delta_1-\delta_5\) follows.

## Verification
The standalone Python 3 standard-library file `verify.py` independently generates the greedy permutation to \(10000\) inputs and compares its \(2949\) turning-point records with the prime-nondivisor recurrence. It directly verifies the primorial-copy identity for levels \(3\) through \(6\), checks the class counts by full enumeration through level \(7\), and verifies the symbolic recurrence from short prime-gap counts through level \(14\). Exact integer and rational assertions reproduce the strict bias certificate. It also tests the derived discrepancy bound on every integer through the level-seven primorial. Run `python3 verify.py` in the directory containing this result's artifacts; `verification_output.txt` records an actual successful run. The unbounded result rests on the proof above, not these finite tests.

## Relationship to prior work
Basistha and Ionascu introduced and studied this greedy coprime permutation, proved the prime-record and primorial-translation structure, and established the natural density of the **union** of record classes. Their global density \(\kappa=\delta_1+\delta_5\) does not determine the two summands separately, nor provide the present logarithmic counting-error estimate. The OEIS record sequence gives the recurrence and initial terms but not this residue-class distribution. Finite studies of long runs of records divisible by \(5\) address a different, local pattern. The contribution here is the complete modulo-six density split with a strict signed bias, an effective rational series, and a uniform logarithmic error.

## Limitations
The constants are specified by infinite convergent series and rational enclosures, not claimed to be rational or to have elementary closed forms. The classification is for the two nonempty classes modulo \(6\); a distribution theorem for all moduli is not asserted. The error constant implicit in the asymptotic is absolute for these two classes. An equivalent result in literature not captured by the searched bibliographic and sequence resources remains possible. No external independent audit is claimed.

## References
1. A. K. Basistha and E. J. Ionascu, *A special sequence and primorial numbers*, arXiv:2302.02838v1, publicly submitted 2023-02-06; revised arXiv:2302.02838v5 (2023-11-22). https://arxiv.org/abs/2302.02838
2. A. K. Basistha and E. J. Ionascu, *A special sequence and primorial numbers*, Rev. Roumaine Math. Pures Appl. 70 (2025), 235–255, DOI:10.59277/RRMPA.2025.235.255. https://imar.ro/journals/Revue_Mathematique/pdfs/2025/3-4/4.pdf
3. OEIS A261271, greedy least-prime-nondivisor sequence, https://oeis.org/A261271
