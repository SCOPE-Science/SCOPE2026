# Higher local cyclotomic prime extraction

## Statement

Let \(n>1\) be squarefree, with prime divisors
\[
p_1<p_2<\cdots<p_k.
\]
For \(1\le j<k\), put
\[
m_j=p_1\cdots p_j,\qquad r_j=n/m_j,\qquad q=p_{j+1}.
\]
Let \(x\ne0\) be an integer, let \(\ell\mid x\) be prime, and set
\[
a=\nu_\ell(x),\qquad C=\Phi_n(x),\qquad A_j=\Phi_{m_j}(x).
\]
Then the corrected cyclotomic residual satisfies the exact local identity
\[
\boxed{\nu_\ell\!\left(CA_j^{-\mu(r_j)}-1\right)=qa.}
\tag{1}
\]
The expression inside the valuation is a rational \(\ell\)-adic unit; \(A_j\) is coprime to \(\ell\).

If \(\ell\) is odd, the unknown sign \(\mu(r_j)\) can be eliminated entirely:
\[
\boxed{\left\{\nu_\ell(C-A_j),\,\nu_\ell(CA_j-1)\right\}=\{a,qa\}.}
\tag{2}
\]
More precisely,
\[
\begin{array}{c|cc}
 & \nu_\ell(C-A_j) & \nu_\ell(CA_j-1)\\ \hline
\mu(r_j)=+1 & qa & a\\
\mu(r_j)=-1 & a & qa.
\end{array}
\tag{3}
\]
Thus, once the first \(j\) prime divisors are known, the next one is read from two integer valuations:
\[
\boxed{p_{j+1}=\frac1a\max\{\nu_\ell(C-A_j),\nu_\ell(CA_j-1)\}.}
\tag{4}
\]
The branch attaining the maximum also gives the parity of the number of prime factors remaining through \(\mu(r_j)\).

At the binary base \(x=2\), a particularly clean complete recursion holds for every odd squarefree \(n\). If \(C=\Phi_n(2)\), then
\[
\boxed{p_1=\nu_2(C+1)}
\tag{5}
\]
and, for \(1\le j<k\),
\[
\boxed{p_{j+1}=\max\{\nu_2(C-A_j),\nu_2(CA_j-1)\},\qquad A_j=\Phi_{m_j}(2).}
\tag{6}
\]
Indeed the unordered pair in (6) is exactly
\[
\boxed{\left\{\nu_2(C-A_j),\nu_2(CA_j-1)\right\}=\{p_{j+1},p_1+1\}.}
\tag{7}
\]
Hence all prime divisors of an odd squarefree index can be peeled by exact \(2\)-adic integer arithmetic while keeping the target value \(\Phi_n(2)\) fixed. The auxiliary values \(A_j\) involve only the already recovered prefix product, rather than the unrecovered quotient index.

For even squarefree \(n\), (7) remains valid whenever the next prime is greater than \(3\), with the baseline \(p_1+1=3\). The sole collision of the two scales can occur at the initial pair \((p_1,p_2)=(2,3)\); testing \(3\mid n\) resolves that exceptional step.

## Example

For
\[
n=105=3\cdot5\cdot7,
\]
one has
\[
C=\Phi_{105}(2)=473474689919911.
\]
First,
\[
\nu_2(C+1)=3.
\]
With \(A_1=\Phi_3(2)=7\),
\[
\nu_2(C-A_1)=5,\qquad \nu_2(CA_1-1)=4,
\]
so the next prime is \(5\). With \(A_2=\Phi_{15}(2)=151\),
\[
\nu_2(C-A_2)=4,\qquad \nu_2(CA_2-1)=7,
\]
so the final prime is \(7\). The smaller valuation stays at \(p_1+1=4\), as predicted by (7).

## Proof

The Möbius product gives
\[
\Phi_n(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}.
\tag{8}
\]
Because \(n=m_jr_j\) is squarefree and \((m_j,r_j)=1\), for \(d\mid m_j\),
\[
\mu(n/d)=\mu(r_j)\mu(m_j/d).
\]
Consequently the factors in (8) supported entirely on \(m_j\) multiply to
\[
\prod_{d\mid m_j}(x^d-1)^{\mu(n/d)}
=\Phi_{m_j}(x)^{\mu(r_j)}=A_j^{\mu(r_j)}.
\tag{9}
\]
Thus
\[
T:=CA_j^{-\mu(r_j)}
=\prod_{\substack{d\mid n\\d\nmid m_j}}(x^d-1)^{\mu(n/d)}.
\tag{10}
\]
Since \(j\ge1\), both divisor sums
\[
\sum_{d\mid n}\mu(n/d)=0,
\qquad
\sum_{d\mid m_j}\mu(n/d)
=\mu(r_j)\sum_{d\mid m_j}\mu(m_j/d)=0
\]
vanish. Therefore the total exponent in the product (10) is zero and the minus signs cancel, giving the \(\ell\)-adic power-series identity
\[
T=\prod_{\substack{d\mid n\\d\nmid m_j}}(1-x^d)^{\mu(n/d)}.
\tag{11}
\]
Among divisors of \(n\) not dividing \(m_j\), the unique smallest one is \(q=p_{j+1}\). Every other such divisor exceeds \(q\). Expanding (11) in \(\mathbb Z_\ell[[x]]\) therefore gives
\[
T=1-\mu(n/q)x^q+x^{q+1}H(x)
\tag{12}
\]
for some \(H(x)\in\mathbb Z_\ell[[x]]\). Since \(\mu(n/q)=\pm1\), evaluation at an integer \(x\) with \(a=\nu_\ell(x)>0\) shows
\[
\nu_\ell(T-1)=qa,
\]
which proves (1).

Now assume \(\ell\) is odd. Since \(m_j\) is squarefree, the first-term expansion of its cyclotomic polynomial is
\[
A_j=1-\mu(m_j)x+x^2G(x)
\]
with \(G\in\mathbb Z[x]\), so
\[
\nu_\ell(A_j-1)=a.
\]
Also \(A_j\equiv1\pmod\ell\), hence \(A_j+1\not\equiv0\pmod\ell\), and therefore
\[
\nu_\ell(A_j^2-1)=a.
\tag{13}
\]
If \(\mu(r_j)=+1\), then \(T=C/A_j\), so
\[
\nu_\ell(C-A_j)=qa.
\]
Furthermore
\[
CA_j-1=A_j^2T-1=(A_j^2-1)+A_j^2(T-1),
\]
whose two summands have distinct valuations \(a\) and \(qa>a\); hence \(\nu_\ell(CA_j-1)=a\). If \(\mu(r_j)=-1\), then \(T=CA_j\) gives \(\nu_\ell(CA_j-1)=qa\), while
\[
C-A_j=\frac{T-A_j^2}{A_j}
\]
has valuation \(a\). This proves (2)--(4).

For \(x=2\), equation (1) still gives the true-branch valuation \(q\). If \(p_1\) is the least prime of \(m_j\), the known binary least-prime congruence for a squarefree index gives
\[
\nu_2(A_j-1)=1,\qquad \nu_2(A_j+1)=p_1,
\]
so
\[
\nu_2(A_j^2-1)=p_1+1.
\tag{14}
\]
Whenever \(q>p_1+1\), the same two-branch argument therefore gives the pair \(\{q,p_1+1\}\). If \(n\) is odd, then \(p_1\ge3\) and distinct odd primes differ by at least two, so \(q\ge p_1+2\); hence (7) holds at every stage. Equation (5) is the binary least-prime extractor, and (6) follows.

## Relation to recent literature

Shunia's 2026 preprint *Cyclotomic Prime Extractors* proves the local identities
\[
\nu_2(\Phi_n(2)-1)=n/\operatorname{rad}(n)
\]
and, for squarefree \(n\),
\[
\nu_2(\Phi_n(2)+1)=\operatorname{lpf}(n).
\]
It then obtains all prime divisors locally by reapplying the least-prime identity to successively divided quotient indices. For a fixed target value \(\Phi_n(2)\), its successive peeling mechanism is instead Archimedean: it subtracts logarithmic fingerprints from \(\log_2\Phi_n(2)\) and recovers the next scale by rounding. The theorem above supplies an exact local analogue not stated there: after the first prime is known, each later prime is isolated by a pair of integer valuations against the cyclotomic value at the already known prefix product.

The Möbius product and the Archimedean dominance of the smallest divisor are classical. Pomerance and Rubinstein-Salzedo's *Cyclotomic Coincidences* uses those ingredients to compare real cyclotomic values, but does not give the local prefix-residual valuation identities (1)--(7).

## Originality and limitations

To the best of our knowledge, the corrected higher local identity (1), the odd-prime valuation pair (2), and the complete binary recursion (6)--(7) have not previously been stated. Searches covered the exact formulas and synonymous combinations of cyclotomic values, successive prime-factor recovery, local/\(p\)-adic extraction, squarefree indices, and \(\Phi_n(2)\) versus \(\Phi_m(2)\). The full text of the motivating 2026 preprint and the Pomerance--Rubinstein-Salzedo paper were inspected in the relevant sections.

The principal residual originality risk is the recency of arXiv:2609.18480: closely related follow-up work may not yet be indexed. No inaccessible paper was identified whose metadata or available description specifically suggests the same higher local extractor. The result is an exact identity, not a claim of an efficient factorization algorithm; cyclotomic values can be enormous.

## Reproducibility

`artifacts/verify.py` uses only the Python standard library and exact integer arithmetic. It evaluates squarefree cyclotomic values from the Möbius product, checks (2) at several bases and odd local primes for all squarefree indices up to 5000 with at least two prime factors, checks the binary corollary and its nonexceptional even analogue, and verifies the \(n=105\) example. The recorded output is in `artifacts/verify-output.txt`.

## References

1. Joseph M. Shunia, *Cyclotomic Prime Extractors*, arXiv:2609.18480, 2026. https://arxiv.org/abs/2609.18480
2. Carl Pomerance and Simon Rubinstein-Salzedo, *Cyclotomic Coincidences*, Experimental Mathematics 31 (2022), 596--605; arXiv:1903.01962. https://arxiv.org/abs/1903.01962
