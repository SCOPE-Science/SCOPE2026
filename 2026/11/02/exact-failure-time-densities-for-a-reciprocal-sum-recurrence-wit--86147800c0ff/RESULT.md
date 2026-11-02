# Exact failure-time densities for a reciprocal-sum recurrence with shallow finite-field preimage trees

## Finding
For each integer \(h\ge1\), start with an integer \(x_0\ge1\) and let
\[
x_{n+1}=\frac{h^2}{x_0+x_1+\cdots+x_n}\qquad(n\ge0).
\]
Write \(x_n=a_n/b_n\) in lowest positive terms. Call \(n\ge2\) a *failure* when
\[
Q_n=b_n+\frac{2}{h}a_n
\]
is **not the square of a nonnegative integer**. Let \(\mathcal F_h(x_0)\) be the set of failures.

**Theorem.** Assume every prime divisor of \(h\) belongs to
\[
\mathcal P=\{2,5\}\;\cup\;\{p\text{ prime}:p\equiv13,17\pmod{20}\}\;\cup\;\{p\text{ prime}:p\equiv3\pmod4\}.
\]
Then \(\mathcal F_h(x_0)\subseteq\{2,3\}\) for **every** initial positive integer \(x_0\). Define
\[
r=\begin{cases}2/5^{v_5(h)+1},&5\mid h,\\0,&5\nmid h,\end{cases}\qquad
q=\prod_{\substack{p\mid h\\p=2\text{ or }p\equiv13,17\ (\mathrm{mod}\,20)}}\left(1-\frac{c_p}{p^{v_p(h)+1}}\right),
\]
where \(c_2=1\), \(c_p=2\) for odd \(p\), and an empty product equals \(1\). The natural densities of the four **exact** failure sets are
\[
\begin{array}{c|c}
\mathcal F_h(x_0)&\text{density}\\\hline
\varnothing&(1-2r)q\\
\{2\}&r+(1-2r)(1-q)\\
\{3\}&rq\\
\{2,3\}&r(1-q).
\end{array}
\]
Consequently the densities of \(0,1,2\) failures are respectively
\[
\boxed{D_0=(1-2r)q,\qquad D_1=1-q-r+3rq,\qquad D_2=r(1-q),}
\]
and \(D_j=0\) for \(j\ge3\). In fact all these densities are exact counts of congruence classes divided by a period dividing
\[
M=\prod_{\substack{p\mid h\\p=2,5\text{ or }p\equiv13,17\ (\mathrm{mod}\,20)}}p^{v_p(h)+1}.
\]
If \(5\mid h\) and at least one further prime divisor is \(2\) or \(13,17\pmod{20}\), then \(D_2>0\). In the complementary cases every starting value has at most one failure.

For \(h=65=5\cdot13\), the exact counts modulo \(M=4225\) for \(\varnothing,\{2\},\{3\},\{2,3\}\) are \(3507,380,334,4\), respectively. Thus the occurrence of two failures is not only possible but has positive density.

## Assumptions and scope
All parameters and starting values are positive integers. The expressions \(Q_n\) are positive rational numbers; “integer perfect square” does not mean merely a square in \(\mathbb Q\). Natural density is the limit of the number of starts \(1\le x_0\le X\) satisfying the property divided by \(X\), as \(X\to\infty\). The theorem concerns the specified infinite class of \(h\), including arbitrarily many distinct prime factors and arbitrary positive exponents. It does not claim the same bound for arbitrary \(h\) with other primes \(1\pmod4\). Prime divisors congruent to \(3\pmod4\) are allowed but do not affect the density parameters.

## Proof
**1. Reduced numerator recurrence and the square criterion.** Set \(S_m=x_0+\cdots+x_m\) and \(t_m=S_m/h=u_m/v_m\) in lowest positive terms. Initially
\[
(u_0,v_0)=\left(\frac{x_0}{\gcd(x_0,h)},\frac{h}{\gcd(x_0,h)}\right).
\]
The exact recurrence \(t_{m+1}=t_m+1/t_m\) gives
\[
u_{m+1}=u_m^2+v_m^2,\qquad v_{m+1}=u_mv_m,
\]
with no cancellation since \(\gcd(u_m,v_m)=1\). Put \(d_m=\gcd(h,u_m)\). For \(m\ge0\), reduced numerator and denominator of \(x_{m+1}=hv_m/u_m\) are \(a_{m+1}=hv_m/d_m\), \(b_{m+1}=u_m/d_m\); hence for \(m\ge1\),
\[
Q_{m+1}=\frac{u_m+2v_m}{d_m}=\frac{(u_{m-1}+v_{m-1})^2}{d_m}.
\]
If \(d_m=1\), this is an integer square. Conversely let \(p\mid d_m\). If \(p\) is odd, \(p\mid u_{m-1}^2+v_{m-1}^2\) and coprimality imply \(p\nmid u_{m-1}+v_{m-1}\): otherwise \(p\mid2v_{m-1}^2\), a contradiction. Thus the displayed quotient has a negative \(p\)-adic valuation, so is not an integer square. If \(p=2\), then \(u_{m-1}\) and \(v_{m-1}\) are odd, \(v_2(u_m)=1\) since two odd squares sum to \(2\pmod8\), so \(v_2(d_m)=1\); the quotient has odd \(2\)-adic valuation and is not a square. Therefore
\[
\boxed{Q_{m+1}\text{ is an integer square }\Longleftrightarrow\gcd(h,u_m)=1.}
\]
If \(p\mid u_m\), then \(p\nmid v_m\); consequently \(u_{m+1}\equiv v_m^2\ne0\pmod p\) and \(v_{m+1}\equiv0\pmod p\), after which all later numerators remain nonzero modulo \(p\). A given prime can cause only one failure.

**2. Critical initial valuations.** Fix \(p^\alpha\Vert h\). If \(v_p(x_0)<\alpha\), then \(p\mid v_0\), \(p\nmid u_0\) and all later \(u_m\) are nonzero modulo \(p\). The analogous assertion holds if \(v_p(x_0)>\alpha\), now beginning with \(p\mid u_0\), because already \(u_1\equiv v_0^2\ne0\pmod p\). Thus a failure caused by \(p\) is possible only when \(v_p(x_0)=\alpha\). In that case \(u_0,v_0\) are units modulo \(p\), and the initial residue for the finite-field rational map
\[
T(z)=z+z^{-1}
\]
is
\[
z=\frac{x_0/p^\alpha}{h/p^\alpha}\pmod p\in\mathbb F_p^\times.
\]
A failure at index \(m+1\) occurs exactly when the orbit first reaches \(0\) under \(T\) at step \(m\ge1\). A zero maps to infinity in the projective description and can cause no later failure.

**3. Shallow preimage trees at the allowed primes.** If \(p\equiv3\pmod4\), then \(T(z)=0\) has no solution because \(z^2=-1\) has none; the prime is inert for this purpose. For \(p=2\), the only unit \(z=1\) maps to \(0\) at step one.

If \(p\equiv13\) or \(17\pmod{20}\), then \(p\equiv1\pmod4\), and \(T(z)=0\) has exactly the two roots \(s\) with \(s^2=-1\). For a preimage of such a root we would need
\[
z^2-sz+1=0,\qquad\Delta=s^2-4=-5.
\]
Quadratic reciprocity gives \(\left(\frac{-5}{p}\right)=\left(\frac{p}{5}\right)=-1\), because \(p\equiv2\) or \(3\pmod5\). Hence neither root has a preimage in \(\mathbb F_p^\times\): these primes can cause a failure only at index \(2\).

For \(p=5\), the zero preimages are \(2,3\), since \(2^2=3^2=-1\pmod5\). Their respective finite preimages are \(1,4\), since \(T(1)=2\) and \(T(4)=3\). Neither \(1\) nor \(4=-1\) has a finite preimage: the discriminant of \(z^2\mp z+1\) is \(-3\equiv2\pmod5\), a nonsquare. Thus \(p=5\) causes index \(2\) exactly for \(z\in\{2,3\}\), index \(3\) exactly for \(z\in\{1,4\}\), and never any later index. These cases prove \(\mathcal F_h(x_0)\subseteq\{2,3\}\).

**4. Exact residue frequencies and independence.** For each prime \(p^\alpha\Vert h\), the condition \(v_p(x_0)=\alpha\), together with a specified \(z\in\mathbb F_p^\times\), fixes exactly one residue class of \(x_0\pmod{p^{\alpha+1}}\). Thus the stage-two failure probability equals \(1/2^{\alpha+1}\) for \(p=2\), and \(2/p^{\alpha+1}\) for primes \(13,17\pmod{20}\). A factor \(5^\alpha\Vert h\) contributes stage-two and stage-three probabilities each \(2/5^{\alpha+1}=r\), which are disjoint. All other allowed factors contribute zero. The Chinese remainder theorem gives independence across distinct primes. Let \(A\) be the event that some prime other than \(5\) causes a stage-two failure. Then \(\Pr(A)=1-q\). Independently, the \(5\)-component has disjoint events of probability \(r\) at each of stages two and three, and no event with probability \(1-2r\). Their four products give precisely the failure-set table in the Finding, with rational densities equal to proportions among the \(M\) residue classes. Summing table entries by cardinality proves the expressions for \(D_0,D_1,D_2\), and their zero extension to larger \(j\).

## Verification
The accompanying dependency-free `verify.py` checks 38 admissible moduli, 286302 complete reduced-pair instances, and 474 additional instances computed from the original rational recurrence using exact `fractions.Fraction` arithmetic; it compares the directly observed failure sets to the local preimage classifications and all exact CRT counts. It also checks the \(h=65\) example above. Running `python3 verify.py` reports

`VERIFY_OK moduli=38 reduced_pair_inputs=286302 original_fraction_inputs=474 exact_arithmetic=yes`

The unrestricted theorem follows from the proof, not from finite experiments. All probability calculations are rational, with no floating-point approximations.

## Relationship to prior work
Matijasevick, Rodríguez and Salazar (2026), *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, establishes the reduced numerator recurrence and the square criterion (Propositions 2.3 and 4.1), and bounds the number of nonsquare terms by the number of relevant prime divisors (Theorem B). Its Section 7, Question (1), explicitly asks for the proportions of starting values producing \(j\) failures, noting that finite-field preimage trees govern the answer. The present theorem answers that frequency question for a large structured class with shallow rational preimage trees, and gives exact failure-time supports and joint distributions. The recurrence identity and the general one-prime-one-failure observation are not claimed as new.

Jones and Manes (2014), *Galois theory of quadratic rational functions*, treats preimage trees and arboreal Galois groups for related rational maps, including \((z^2+1)/z\). Its general Galois results do not explicitly evaluate these integer-starting-value failure-time frequencies. The motivating paper also cites a 2026 companion preprint by Matijasevick on \(z+k/z\) arithmetic dynamics. Its complete text was not obtainable for direct comparison; this leaves a real publication-priority risk.

## Limitations
The exact distribution is proved only for the stated prime-factor class. For other primes \(1\pmod4\), the tree of finite-field preimages of zero may have more levels, so the conclusion need not hold. No complete classification over all \(h\) is claimed. This is a mathematical proof with independent verification of finite examples, not an externally refereed result. An earlier implicit or explicit classification in arithmetic dynamics could potentially cover part of the theorem; the cited 2026 companion preprint was not directly inspected.

## References
1. Mateo Matijasevick, Santiago Rodríguez and Gregorio Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (first public posting 2026-09-30), https://arxiv.org/html/2610.00765v1, especially Propositions 2.3, 4.1 and Section 7, Question (1).
2. Rafe Jones and Michelle Manes, *Galois theory of quadratic rational functions*, arXiv:1101.4339, https://arxiv.org/abs/1101.4339 (journal publication: *Commentarii Mathematici Helvetici* 89 (2014), 173–213).
3. Mateo Matijasevick, *Arithmetic dynamics of \(z+k/z\): Galois groups, prime divisors of orbits, and zeros of iterates*, cited as a preprint (2026) in Reference [2] of arXiv:2610.00765v1; full text was not available for inspection.
