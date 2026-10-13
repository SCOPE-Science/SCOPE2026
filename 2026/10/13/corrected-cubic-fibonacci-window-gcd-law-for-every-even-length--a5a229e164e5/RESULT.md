# Corrected cubic Fibonacci window-gcd law for every even length

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For every even integer \(k\ge2\), set
\[
S_n(k)=\sum_{j=1}^{k}F_{n+j}^{3}\quad(n\ge0),\qquad
m_k=\gcd(F_{k+1}^{3}-1,F_{k+2}^{3}-1).
\]
Then the following identities hold, without exceptional positive even lengths:
\[
m_k=\gcd(F_{k+2}-1,3(F_{k+1}-1)),
\qquad
\gcd_{n\ge0}\left(F_{n+k+1}^{3}-F_{n+1}^{3}\right)=m_k,
\]
\[
\boxed{\gcd_{n\ge0} S_n(k)=
\begin{cases}
m_k,&6\nmid k,\\
m_k/2,&6\mid k.
\end{cases}}
\]
Here the gcd of infinitely many nonnegative integers is their positive common gcd; it is well-defined because the proof reduces it to finitely many integer gcds.

The two branches above are the reverse of the Fibonacci-cube branches printed in Question 6.1 of Mbirika--Spilker (2022/2023). For example \(k=2\) gives \(m_2=1\) and gcd \(1\), whereas the printed \(6\nmid k\) branch would give \(1/2\); \(k=6\) gives \(m_6=4\) and gcd \(2\), whereas the printed \(6\mid k\) branch would give \(4\). These examples diagnose the case assignment; the theorem proves the corrected formula for all even lengths.

## Assumptions and scope
All Fibonacci numbers have their standard integer normalization above; all window starting indices satisfy \(n\ge0\); and \(k\ge2\) is even. Gcd values are positive. No claim is made for odd \(k\), general initial conditions, Lucas cube sums, or higher powers. The manuscript establishing the motivating open question has primary MSC2020 classification 11B39, and its first publicly archived version was submitted on 2022-04-26 UTC.

## Proof
Fix an even \(k\). Abbreviate \(a=F_k\), \(v=F_{k+1}\), \(u=F_{k+2}=a+v\), and \(m=\gcd(u^3-1,v^3-1)\). Cassini's identity in this parity reads
\[
v^2-av-a^2=1,\qquad u^2-uv-v^2=-1.\tag{1}
\]

**Lemma 1 (cubic norm rigidity).** For these positive integers, \(m\mid u-1\), and consequently
\[
m=\gcd(u-1,3(v-1)).\tag{2}
\]
To prove the divisibility, work modulo \(m\), where \(u^3=v^3=1\). By the second identity in (1),
\[
u^3=2uv^2+v^3-u-v.
\]
Hence \(2uv^2=u+v\); multiplying by \(v\) gives \(2u=uv+v^2\). Substitution back into (1) yields \(u^2=2u-1\), so \((u-1)^2=0\), and from \(u^3=1\) also \(3(u-1)=0\). Thus for any prime power \(p^e\mid m\) with \(p\ne3\), \(u\equiv1\pmod{p^e}\).

For \(3^e\mid m\), the case \(e=1\) follows from \(u^3\equiv1\pmod3\). If \(e\ge2\), then \(u\equiv v\equiv1\pmod3\), and the elementary lifting identity \(\nu_3(z^3-1)=\nu_3(z-1)+1\) for \(z\equiv1\pmod3\) shows that both \(u-1\) and \(v-1\) are divisible by \(3^{e-1}\). Write \(u=1+\epsilon\), \(v=1+\eta\). Equation (1) becomes
\[
\epsilon-3\eta+\epsilon^2-\epsilon\eta-\eta^2=0.
\]
The terms other than \(\epsilon\) are multiples of \(3^e\), because \(2(e-1)\ge e\). Therefore \(u\equiv1\pmod{3^e}\), proving \(m\mid u-1\). Now reduction of (1) modulo \(u-1\) gives \(v^2+v-2\equiv0\), hence \(v^2+v+1\equiv3\), and
\[
m=\gcd(u-1,v^3-1)=\gcd(u-1,3(v-1)),
\]
which proves the lemma.

**Lemma 2 (all cubic window differences).** Put \(\delta=v-1\) modulo \(m\). By (2), \(u=1\) and \(3\delta=0\) modulo \(m\). The reduced norm identity \(v^2+v-2=0\) now reads \(\delta^2+3\delta=0\), so \(\delta^2=0\) modulo \(m\). Since \(a=u-v=-\delta\) modulo \(m\), the Fibonacci addition identity gives, for each \(r\ge1\),
\[
F_{r+k}=vF_r+aF_{r-1}
\equiv F_r+\delta(F_r-F_{r-1})\pmod m.
\]
Cubing eliminates all nonconstant terms because \(3\delta=\delta^2=0\) modulo \(m\). Thus \(m\mid F_{r+k}^3-F_r^3\) for every \(r\ge1\). At \(r=1,2\), these differences are precisely \(v^3-1\) and \(u^3-1\), whose gcd is \(m\). Consequently their infinite gcd is exactly \(m\). Since \(S_{n+1}(k)-S_n(k)=F_{n+k+1}^3-F_{n+1}^3\),
\[
\gcd_{n\ge0}S_n(k)=\gcd(m,S_0(k)).\tag{3}
\]

**Lemma 3 (the first-window identity).** For every even \(k\ge0\),
\[
4S_0(k)=v^3+a^3-3(v-a)+2
=(v-1)^2(v+2)+a(a^2+3).\tag{4}
\]
At \(k=0\) this equals zero. For induction by two, write \(w=F_{k+3}=a+2v\) and \(u=a+v\). The change in the right-hand cubic expression when \(k\) is replaced by \(k+2\), minus \(4(v^3+u^3)\), is
\[
-3a(a^2+av-v^2+1)=0
\]
by Cassini's first identity in (1). This proves (4) for all even \(k\). Reducing (4) modulo \(m\) and using \(v^3=1\), \(a^3=(-\delta)^3=0\), and \(3(v-a)=3(1+2\delta)=3\) gives
\[
m\mid4S_0(k).\tag{5}
\]

**The exact power of two.** Fibonacci parity has period three: \(F_r\) is even precisely when \(3\mid r\). Thus \(m\) is even exactly when both \(F_{k+1}\) and \(F_{k+2}\) are odd, which, for even \(k\), is precisely \(6\mid k\). If \(6\nmid k\), then \(m\) is odd, and (5) implies \(m\mid S_0(k)\); equation (3) gives \(\gcd S_n=m\).

Now assume \(k=6q\) for \(q\ge1\). With \(T=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), we have \(T^6=\begin{pmatrix}13&8\\8&5\end{pmatrix}\equiv I\pmod4\) and a diagonal matrix modulo \(8\). Therefore \(8\mid a\) and \(v\equiv1\pmod4\); also \(u=a+v\) is odd. Cassini gives \((v-1)(v+1)=au\). Since \(\nu_2(v+1)=1\), the integer \(t=\nu_2(v-1)=\nu_2(a)-1\) is at least two. We also have \(\nu_2(u-1)=t\), because \(u-1=(v-1)+a\) and \(\nu_2(a)=t+1\). By (2), \(\nu_2(m)=t\).

The two summands in the final expression of (4) have respective \(2\)-adic valuations \(2t\) and \(t+1\): indeed \(v+2\) and \(a^2+3\) are odd. As \(t\ge2\), these valuations differ, so \(\nu_2(4S_0)=t+1\) and \(\nu_2(S_0)=t-1\). Equation (5) shows that the odd prime-power part of \(m\) divides \(S_0\). Hence (3) implies \(\gcd(m,S_0)=m/2\), completing the proof.

## Verification
An exact-integer standalone checker, `verify.py`, evaluates all even \(k\) from \(2\) through \(600\), compares the conjectured and actual gcds of the first \(25\) consecutive windows for each, checks the identity in (4), and checks the reduced difference-gcd formula (2). The script performs \(7{,}500\) explicit window-gcd comparisons, as recorded in `verification_output.txt`. Run using `python3 verify.py`; only Python's standard library is required. Finite verification is supplemental and does not prove the unrestricted result.

## Relationship to prior work
Mbirika and Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626v2, Section 6.1, Question 6.1, print a case-split conjecture for the Fibonacci-cube window gcd. Its two conditions on \(6\mid k\) and \(6\nmid k\) are interchanged relative to the actual gcd. This result supplies a corrected complete formula, a reduction of its modulus from two cubes to two linear Fibonacci expressions, and a proof valid for all even \(k\). The point is not merely the small numerical contradiction, but the unrestricted congruence and exact valuation analysis.

Guyer and Mbirika, arXiv:2104.12262v2, prove analogous identities for **first powers** of recurrence terms; this does not imply the cubic norm-rigidity lemma or its parity correction. Frontczak (2018), Proposition 3.5, gives explicit sums of regularly spaced **even-index** cubes (its full open-access PDF sections were inspected), not all-starting-index consecutive cube-window gcds. The 2021 Karcher--Michael study examines selected two-term power sums and prime factors; it does not derive the stated all-length gcd. Bilu et al. (2016) treat divisibility of Lucas power differences by individual Lucas terms, not the exact common divisor of every cubic shift difference together with the initial window. Clary--Hemenway (1993) remains an abstract-only inspected plausible source of power-sum identities; an implicit equivalent there is a bibliographic risk. Published mathematical-record searches for aliases, norm identities, cube windows, and gcd formulas did not identify stronger covering results; these searches alone do not certify uniqueness.

## Limitations
The theorem is confined to even Fibonacci-cube windows with standard initial conditions. It does not settle the Lucas-cube or general-sequence variants of Question 6.1, nor higher powers or odd window lengths. The apparent swap in the motivating paper could be a typographical case reversal. Independent mathematical examination and comprehensive bibliographic verification have not been performed; the supplied checker tests finitely many cases, while the symbolic proof covers all even lengths.

## References
1. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626; public version 1 dated 2022-04-26, version 2 dated 2023-01-13, Section 6.1, Question 6.1. https://arxiv.org/html/2204.12626v2 ; https://arxiv.org/abs/2204.12626 . Primary MSC2020 11B39.
2. Dan Guyer and aBa Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262v2. https://arxiv.org/html/2104.12262v2 .
3. Robert Frontczak, *Sums of powers of Fibonacci and Lucas numbers: A new bottom-up approach*, 2018. https://nntdm.net/volume-24-2018/number-2/94-103/ . Abstract consulted; full text not inspected.
4. Stuart Clary and Paul D. Hemenway, *On sums of cubes of Fibonacci numbers*, 1993, DOI 10.1007/978-94-011-2058-6_12. https://ideas.repec.org/h/spr/sprchp/978-94-011-2058-6_12.html . Abstract consulted; full text not inspected.
5. Spirit Karcher and Mariah Michael, *Prime Factors and Divisibility of Sums of Powers of Fibonacci and Lucas Numbers*, American Journal of Undergraduate Research 17 (2021), 59–69, DOI:10.33697/ajur.2020.036. https://www.researchgate.net/publication/350636633_Prime_Factors_and_Divisibility_of_Sums_of_Powers_of_Fibonacci_and_Lucas_Numbers . Full accessible text inspected; selected prime divisibility problems, not full window gcd.
6. Yuri F. Bilu, Takao Komatsu, Florian Luca, Amalia Pizarro-Madariaga, Pantelimon Stănică, *On a divisibility relation for Lucas sequences*, Journal of Number Theory 163 (2016), 1–18, DOI:10.1016/j.jnt.2015.11.011. https://doi.org/10.1016/j.jnt.2015.11.011 . Full accessible text examined for difference-divisibility coverage.
