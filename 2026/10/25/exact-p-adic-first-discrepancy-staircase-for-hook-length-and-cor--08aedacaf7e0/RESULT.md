# Exact p-adic first-discrepancy staircase for hook-length and core-partition series

## Finding
Let \(p\) be any prime and let \(a\ge1\) be an integer. Set \(t=p^a\). Define integer sequences \(H_t(n)\) and \(C_t(n)\) by
\[
\sum_{n\ge0}H_t(n)q^n=\prod_{m\ge1}(1-q^m)^{t^2-1},\qquad
\sum_{n\ge0}C_t(n)q^n=\frac{\prod_{m\ge1}(1-q^{tm})^t}{\prod_{m\ge1}(1-q^m)}.
\]
For every positive integer \(r\), let \(d_{p,a}(r)\) be the least nonnegative index \(n\) for which \(H_t(n)\not\equiv C_t(n)\pmod{p^r}\), with value \(\infty\) if no such index exists. Then
\[
\boxed{d_{p,a}(r)=\begin{cases}
\infty,&1\le r\le a+1,\\
p^{\max(0,2a-r+1)},&r\ge a+2.
\end{cases}}
\]
In particular, the largest prime-power modulus dividing every coefficient difference is **exactly** \(p^{a+1}\). More precisely, for every integer \(j\) with \(0\le j<a\),
\[
\boxed{H_t(p^j)-C_t(p^j)\equiv-p^{2a-j}\pmod{p^{2a-j+1}}},
\]
while every earlier coefficient difference is divisible by \(p^{2a-j+1}\). Thus \(\nu_p(H_t(p^j)-C_t(p^j))=2a-j\). The first failure of the stronger congruence modulo \(p^{a+2}\) occurs at the exact index \(p^{a-1}\).

## Assumptions and scope
The identities hold for **every** prime \(p\), every integer \(a\ge1\), all positive congruence exponents \(r\), and every indicated index \(j\). No analytic convergence is needed: every product and quotient is taken in the formal power-series ring \(\mathbb Z[[q]]\). The inverse of a series with constant coefficient \(1\) again has integral coefficients. The coefficients \(H_t(n)\) are those of the Nekrasov--Okounkov hook-length specialization \(F_{t^2}(q)\), and \(C_t(n)\) count \(t\)-core partitions.

## Proof
Write \(E(q)=\prod_{m\ge1}(1-q^m)=1-q+O(q^2)\). The two generating functions are \(E(q)^{p^{2a}-1}\) and \(E(q^{p^a})^{p^a}/E(q)\). Their difference therefore equals \(E(q)^{-1}\Delta(q)\), where
\[
\Delta(q)=E(q)^{p^{2a}}-E(q^{p^a})^{p^a}.
\]
Because \(E(q)^{-1}\) is a unit with constant term one, multiplication by it preserves both divisibility of the *entire* series by \(p^r\) and the first nonzero coefficient index modulo \(p^r\). Moreover, if coefficients of \(\Delta\) below degree \(n\) vanish modulo \(p^r\), then the degree-\(n\) coefficients of \(\Delta\) and \(E^{-1}\Delta\) agree modulo \(p^r\).

We use two elementary integral-series facts. For \(U(q)\in1+q\mathbb Z[[q]]\), the characteristic-\(p\) Frobenius identity gives
\[
U(q)^{p^h}\equiv U(q^{p^h})\pmod p\qquad(h\ge0).
\]
Also, if \(V,W\in1+q\mathbb Z[[q]]\) satisfy \(V\equiv W\pmod p\), then
\[
V^{p^k}\equiv W^{p^k}\pmod{p^{k+1}}\qquad(k\ge0).
\]
The latter follows by expressing \(V/W=1+pZ\) and repeatedly raising to the \(p\)-th power: a unit congruent to one modulo \(p^m\) has its \(p\)-th power congruent to one modulo \(p^{m+1}\), including at \(p=2\).

Apply the second fact to \(V=E(q)^{p^a}\), \(W=E(q^{p^a})\), and \(k=a\). Frobenius supplies \(V\equiv W\pmod p\). We obtain
\[
E(q)^{p^{2a}}\equiv E(q^{p^a})^{p^a}\pmod{p^{a+1}}.
\]
Thus \(\Delta\), and hence every difference \(H_t(n)-C_t(n)\), is divisible by \(p^{a+1}\).

To determine exact first discrepancies, fix \(0\le j<a\). Apply the same two facts to \(E(q)^{p^j}\) and \(E(q^{p^j})\), raising them to \(p^{2a-j}\). This gives
\[
E(q)^{p^{2a}}\equiv E(q^{p^j})^{p^{2a-j}}
\pmod{p^{2a-j+1}}.
\]
The right side is \(1-p^{2a-j}q^{p^j}+O(q^{2p^j})\). In particular, all positive-degree coefficients strictly below \(p^j\) vanish modulo \(p^{2a-j+1}\), while its degree-\(p^j\) coefficient is \(-p^{2a-j}\). Since \(p^j<p^a\), the second summand \(E(q^{p^a})^{p^a}\) of \(\Delta\) is constant through degree \(p^j\). Therefore
\[
[q^{p^j}]\Delta\equiv-p^{2a-j}\pmod{p^{2a-j+1}},
\]
and all positive-degree coefficients of \(\Delta\) below \(p^j\) vanish modulo \(p^{2a-j+1}\). Multiplication by \(E^{-1}\) preserves both conclusions. This proves the stated exact valuations and earliest indices.

For \(a+2\le r\le2a+1\), set \(j=2a-r+1\), so \(0\le j<a\). The preceding paragraph shows that the first incongruence modulo \(p^r\) occurs at \(n=p^j\). If \(r\ge2a+1\), the coefficient at \(q\) of the two generating functions differs by exactly \(-p^{2a}\), and the constant coefficients agree; hence the first failure remains at \(n=1\). The two formulas agree at the common endpoint \(r=2a+1\). Finally, the case \(r\le a+1\) was established by uniform divisibility. This exhausts every \(r\) and proves the theorem.

## Verification
The standalone standard-library program `verify.py` uses the logarithmic-derivative coefficient recurrence for integral powers of the Euler product, a separate convolution construction of the core-partition series, and (for small degrees) direct multiplication of Euler factors as an independent consistency check. It checks the exact coefficient residues and least failure indices for fourteen prime-power parameters: \(p=2\) with \(1\le a\le5\), \(p=3\) with \(1\le a\le4\), \(p=5\) with \(1\le a\le3\), and \(p=7\) with \(1\le a\le2\). Run `python3 verify.py` in the directory containing this report. The observed output is `VERIFY_OK 14 parameter cases`. These finite calculations are checks only; the unrestricted theorem follows from the proof above.

## Relationship to prior work
Meenu Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and t-Core Partitions* (arXiv:2610.01422v1, first submitted 2026-10-01), proves coefficientwise congruence modulo \(p^a\) for prime-power \(t=p^a\), and modulo \(p^2\) in the prime case \(a=1\). Its treatment of non-prime-powers concerns a different obstruction. The theorem here determines the **maximal uniform prime-power congruence for every \(a\)** and the full staircase of **first failure indices at every prime-power modulus**, including sharp leading residues. For \(a=1\), the uniform \(p^2\) congruence was already known; the broader first-discrepancy classification is the point of this result.

The older work of Guo-Niu Han (arXiv:0805.1398v1) establishes the hook-length and core generating-function framework. Guo-Niu Han and Ken Ono (arXiv:0805.2461v1) establish equality of the *zero sets* of the two coefficient series for \(t=3\), not an all-parameter p-adic threshold. Classical Frobenius lifting is the proof mechanism; the possibility that the entire specialized staircase has been recorded elsewhere is a remaining novelty risk.

## Limitations
This is an exact arithmetic statement only for \(t\) that is a prime power, not a classification of the corresponding congruence filtration for mixed-prime \(t\). It does not determine the valuation of the coefficient difference at *every* index, nor the asymptotic density of any exceptional set. The proof uses standard formal-series facts, and there remains a risk that the specialized full statement is implicit in broader eta-quotient literature. No independent mathematical audit is claimed.

## References
1. Meenu Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and t-Core Partitions*, arXiv:2610.01422v1 (2026), https://arxiv.org/html/2610.01422v1 .
2. Guo-Niu Han, *The Nekrasov--Okounkov hook length formula: refinement, elementary proof, extension and applications*, arXiv:0805.1398v1 (2008), https://arxiv.org/pdf/0805.1398 ; Ann. Inst. Fourier 60 (2010), DOI:10.5802/aif.2515.
3. Guo-Niu Han and Ken Ono, *Hook Lengths and 3-Cores*, arXiv:0805.2461v1 (2008), https://arxiv.org/pdf/0805.2461 .
