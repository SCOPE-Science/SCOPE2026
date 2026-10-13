# A quadratic-form transfer modulo eight for partitions with distinct even parts

## Finding
For every integer \(n\geq0\), let \(\mathcal P_e(n)\) be the set of partitions of \(n\) in which **each even part occurs at most once** (odd parts are unrestricted), and put
\[
W(n)=\sum_{\lambda\in\mathcal P_e(n)}\left(\sum_{j\in\lambda,\;j\ \mathrm{odd}}j-\sum_{j\in\lambda,\;j\ \mathrm{even}}j\right),\qquad W(0)=0.
\]
Let \(b_4(n)\) be the number of partitions of \(n\) with no part divisible by \(4\). For \(h\in\{1,2\}\) and positive integer \(M\), let
\[
R_h(M)=\#\big\{(x,y)\in\mathbb Z_{>0}^2:x\ \mathrm{odd},\;4\mid y,\;x^2+h y^2=M\big\}.
\]
The exact coefficientwise **modulo-eight quadratic-form reduction** is
\[
\boxed{W(n)\equiv n\,b_4(n)-4\big(R_1(8n+1)+R_2(8n+1)\big)\pmod8.}\tag{1}
\]
For every prime \(p\equiv5\) or \(7\pmod8\) such that \(\nu_p(8n+1)\) is odd, the correction in (1) vanishes modulo \(8\). Thus
\[
\boxed{W(n)\equiv n\,b_4(n)\pmod8.}\tag{2}
\]
Combining (2) with the known \(4\)-regular partition congruences yields the following **ten** progression congruences, valid for every integer \(t\ge0\):
\[
\boxed{W(25t+r)\equiv0\pmod8\quad(r\in\{8,13,18,23\}),}\tag{3}
\]
\[
\boxed{W(49t+r)\equiv0\pmod8\quad(r\in\{13,20,27,34,41,48\}).}\tag{4}
\]

## Assumptions and scope
All generating functions below are formal power series with integer coefficients unless reduced modulo \(2\) or \(8\). The prime-factor criterion requires an odd exponent of a prime in either residue class \(5\) or \(7\) modulo \(8\), and asserts a congruence for the weighted statistic, **not** an exact integer identity. The universal reduction (1) has no primality hypothesis. The source-defined statistic agrees with \(S(2\mathbb N,n)\) in Rausch--Stumpenhusen; the result concerns neither unrestricted partitions nor partitions with distinct odd parts.

## Proof
**1. Weighted generating function.** Define \(B(q)=\sum_{n\ge0}b_4(n)q^n\). The Euler product, together with \(1+q^{2m}=(1-q^{4m})/(1-q^{2m})\), gives
\[
B(q)=\prod_{m\ge1}\frac{1+q^{2m}}{1-q^{2m-1}}=\frac{\prod_{m\ge1}(1-q^{4m})}{\prod_{m\ge1}(1-q^m)}.
\]
Consequently, the same product counts partitions with distinct even parts, and their unweighted cardinality is \(b_4(n)\). Every partition of \(n\) contributes weight \(n-2E\), where \(E\) denotes its sum of even parts. Marking even parts separately in the product yields the exact integral identity
\[
\sum_{n\ge0}W(n)q^n=qB'(q)-4B(q)\sum_{m\ge1}\frac{m q^{2m}}{1+q^{2m}}.\tag{5}
\]
Indeed, the even part \(2m\) is present at most once, so the marked contribution is \(2m\,q^{2m}/(1+q^{2m})\); multiplying by the weight correction \(-2E\) produces the factor \(-4\) in (5).

**2. Parity of the correction.** Reduction modulo \(2\) of the Euler product uses \((1-u)^4\equiv1-u^4\pmod2\); hence
\[
B(q)\equiv\prod_{m\ge1}(1-q^m)^3
\equiv\sum_{j\ge0}q^{j(j+1)/2}\pmod2,\tag{6}
\]
where the second congruence is Jacobi's cubic identity \(\prod(1-q^m)^3=\sum_{j\ge0}(-1)^j(2j+1)q^{j(j+1)/2}\). Also,
\[
\sum_{m\ge1}\frac{m q^{2m}}{1+q^{2m}}
\equiv\sum_{k\ge1}\sigma(k)q^{2k}
\equiv\sum_{a\ge1}\big(q^{2a^2}+q^{4a^2}\big)\pmod2.\tag{7}
\]
The first congruence expands the denominators and groups by divisors. The second follows from the exact characterization that \(\sigma(k)\) is odd precisely when \(k\) is a square or twice a square; these two classes are disjoint. The coefficient of \(q^n\) in the product of (6) and (7), modulo \(2\), is therefore the parity of solutions of
\[
n=\frac{j(j+1)}2+2a^2\quad\text{or}\quad n=\frac{j(j+1)}2+4a^2,
\qquad j\ge0,\ a\ge1.
\]
Upon setting \(x=2j+1\) and \(y=4a\), these equations become \(8n+1=x^2+y^2\) and \(8n+1=x^2+2y^2\), respectively. Substitution in (5) proves (1) coefficientwise for all \(n\ge0\).

**3. Inert-prime vanishing.** Fix \(M=8n+1\) and a prime \(p\equiv5,7\pmod8\) with odd \(\nu_p(M)\). Since \((-2/p)=-1\), divisibility of \(x^2+2y^2\) by \(p\) forces \(p\mid x\) and \(p\mid y\). Dividing by \(p^2\) inductively shows that a represented integer can only have even \(p\)-adic valuation. Thus \(R_2(M)=0\).

Let \(\chi_4\) be the real character modulo \(4\), and set \(D(M)=\sum_{d\mid M}\chi_4(d)\). Jacobi's two-square theorem gives \(r_2(M)=4D(M)\) representations by \(x^2+y^2\) with signed and ordered coordinates. Because \(M\equiv1\pmod8\), any representation has one odd and one coordinate divisible by \(4\). Splitting the two choices of which coordinate is odd, the four independent sign choices for a nonaxial positive solution, and the two possible axial sign choices when \(M\) is a square, gives
\[
D(M)=2R_1(M)+\mathbf1_{\{M\text{ is a square}\}}.\tag{8}
\]
Here \(M\) is not a square, as its \(p\)-adic exponent is odd. If some prime \(\ell\equiv3\pmod4\) divides \(M\) to odd valuation, then \(D(M)=0\). Otherwise multiplicativity gives
\[
D(M)=\prod_{\ell\equiv1\;(\mathrm{mod}\;4)}\big(\nu_\ell(M)+1\big),\tag{9}
\]
with only prime divisors of \(M\) appearing in the finite product. If \(p\equiv7\pmod8\), then \(p\equiv3\pmod4\) itself forces \(D(M)=0\). If \(p\equiv5\pmod8\), the condition \(M\equiv1\pmod8\) forces the number of primes \(\ell\equiv5\pmod8\) with odd valuation in \(M\) to be even: primes \(3\) or \(7\pmod8\) have even exponent in the nonzero case and hence contribute \(1\pmod8\); primes \(1\pmod8\) also contribute \(1\), whereas each \(5\pmod8\) prime to odd exponent contributes \(5\). Since \(p\) is one such prime, there is at least one **other**. Each of these two factors in (9) is even, and hence \(4\mid D(M)\). In either case, (8) implies \(2\mid R_1(M)\). Therefore \(R_1(M)+R_2(M)\) is even, proving (2) from (1).

**4. Arithmetic progressions.** In the first family write \(r=8+5j\) with \(j\in\{0,1,2,3\}\). Then
\[
8(25t+r)+1=5(40t+13+8j),
\]
and the second factor is nonzero modulo \(5\) for each of these four \(j\), so the valuation at \(5\) is exactly one. In the second family write \(r=13+7j\), \(j\in\{0,1,2,3,4,5\}\). Then
\[
8(49t+r)+1=7(56t+15+8j),
\]
where the second factor is nonzero modulo \(7\), so the valuation at \(7\) is exactly one. Apply (2) in each case. Ballantine--Merca's Theorem 5.1 states \(16\mid b_4(25t+r)\) for all four listed residues, and their Theorem 5.4 states \(64\mid b_4(49t+r)\) for all six listed residues. Thus \(8\mid n\,b_4(n)\) in all ten progressions, proving (3)--(4). \(\square\)

## Verification
Run the bundled standard-library program `verify.py`. It independently computes the weighted statistic using odd-part unlimited and even-part distinct recurrence rules, computes \(b_4(n)\) from its forbidden-multiples-of-four product, enumerates representations by both quadratic forms, and verifies the exact congruence for every \(0\le n\le2400\). It additionally checks Jacobi's two-square normalization at all \(2401\) indices, checks the inert-prime transfer at \(1019\) eligible indices, directly enumerates partitions for \(0\le n\le25\), checks all ten progression classes through \(n=2400\), and compares the two partition-count products. Expected output is supplied in `verification_output.txt`. This finite computation corroborates, but does not replace, the proof for unbounded \(n\).

## Relationship to prior work
Rausch and Stumpenhusen (arXiv:2606.16585v1, June 15, 2026) introduced and studied the weighted statistic \(S(2\mathbb N,n)\), established its generating function, and proved \(S(2\mathbb N,4n)\equiv0\pmod4\); they did not state (1)--(4). Ballantine and Merca (arXiv:2111.10702v2), in Theorems 5.1 and 5.4, proved the requisite **unweighted** \(4\)-regular congruences modulo \(16\) and \(64\); (3)--(4) are not asserted for that same unweighted function but for the different *weighted* \(W\). Bardhan and Saikia (arXiv:2606.31264v1), Theorem 4.1, prove the general modulo-four observation that every partition weight equals its size modulo \(4\), which only gives \(W(n)\equiv n b_4(n)\pmod4\), not the quadratic correction modulo \(8\) or the prime-factor transfer. The classical Jacobi identities and two-square formula are used as established mathematical inputs, not claimed as discoveries.

## Limitations
The result makes no claim of a complete characterization of all modulo-eight zero progressions, higher-power congruences, or a factorization of \(R_2(M)\) at arbitrary primes. The congruences for \(b_4\) are cited prior results. Equivalence to an independently published, unindexed weighted congruence cannot be excluded by literature searching alone. The replayed finite calculations do not certify infinite arithmetic assertions.

## References
1. K. Rausch and J. Stumpenhusen, *The difference of the sums of odd and even parts of restricted partitions*, arXiv:2606.16585v1 (first public June 15, 2026), especially Theorem 1.6 and Sections 4--5. https://arxiv.org/abs/2606.16585
2. C. Ballantine and M. Merca, *4-Regular partitions and the pod function*, arXiv:2111.10702v2 (2022), Theorems 5.1 and 5.4. https://arxiv.org/html/2111.10702v2
3. G. Bardhan and N. Saikia, *Some new congruences and identities for SOME, DSOME, overpartition SOME functions and analogues*, arXiv:2606.31264v1 (2026), Section 4. https://arxiv.org/html/2606.31264v1
4. Classical Jacobi cubic and sum-of-two-squares identities, as recorded in standard treatments of theta series and partitions.
