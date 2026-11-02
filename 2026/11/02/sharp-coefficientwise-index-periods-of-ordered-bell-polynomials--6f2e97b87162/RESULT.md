# Sharp coefficientwise index periods of ordered-Bell polynomials at every modulus

## Finding

Let \(G_n(X)=\sum_{k=0}^n k!S(n,k)X^k\) be the ordinary ordered-Bell (Fubini, geometric) polynomial, where \(S(n,k)\) denotes a Stirling number of the second kind. For every modulus \(m\ge2\), set
\[
R(m)=\max_{p^a\parallel m} a,\qquad L(m)=\lambda(m),
\]
where \(\lambda\) is Carmichael's exponent of the unit group. Then the sequence \((G_n\bmod m)_{n\ge0}\) in \((\mathbb Z/m\mathbb Z)[X]\) has **exact least eventual index period** \(L(m)\) and **exact least preperiod** \(R(m)\):
\[
G_{n+L(m)}(X)\equiv G_n(X)\pmod m\quad(n\ge R(m)).
\]
Any positive eventual period is divisible by \(L(m)\); no positive period works for all \(n\ge N\) when \(N<R(m)\). Thus the two sharp invariants apply simultaneously to *every polynomial coefficient*, not merely to evaluation at a fixed integer.

## Assumptions and scope

The index \(n\) is a nonnegative integer. Set \(S(0,0)=1\), \(S(n,0)=0\) for positive \(n\), and \(S(n,k)=0\) outside \(0\le k\le n\). Congruence of polynomials means coefficientwise congruence; it is stronger than congruence of the induced polynomial functions. The convention \(0^0=1\) is used only in the inclusion–exclusion formula for the zero index. The theorem concerns every integer modulus \(m\ge2\); modulus one is intentionally excluded because all residues then agree.

For a prime power \(p^a\), \(\lambda(p^a)=(p-1)p^{a-1}\) for odd \(p\), and \(\lambda(2^a)\) is \(1,2,2^{a-2}\) for \(a=1,2,a\ge3\), respectively. For general \(m\), take the least common multiple over its exact prime-power factors.

## Proof

**1. Inclusion–exclusion and an eventual period.** Write \(c_{n,k}=k!S(n,k)\). The surjection-counting formula gives, for every \(n,k\ge0\),
\[
c_{n,k}=\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}j^n.
\]
Fix \(p^a\). Once \(n\ge a\), terms with \(p\mid j\) vanish modulo \(p^a\). Every remaining \(j\) is a unit, hence \(j^{n+\lambda(p^a)}\equiv j^n\pmod {p^a}\). This proves coefficientwise periodicity for every \(k\) and every \(n\ge a\). The Chinese remainder theorem supplies the asserted period from \(n\ge R(m)\).

**2. No shorter eventual period at odd prime powers.** Suppose \(T>0\) is a period of the coefficient sequence modulo \(p^a\) for all sufficiently large indices. Taking \(k=1,\ldots,p-1\) in the inclusion–exclusion formula and inducting upward on \(k\) forces
\[
j^T\equiv1\pmod {p^a}\qquad(1\le j\le p-1).
\]
Indeed, after the relations for smaller \(j\) are known, the remaining difference is \(j^n(j^T-1)\), and \(j^n\) is invertible. For odd \(p\), these integers represent all nonzero residues modulo \(p\), so \(p-1\mid T\).

If \(a\ge2\), at least one of these representatives, say \(u\), obeys \(u^{p-1}\not\equiv1\pmod {p^2}\). Otherwise all \(p-1\) distinct residue representatives would be roots of the monic polynomial \(Z^{p-1}-1\) modulo \(p^2\). Their pairwise differences are units, so repeated factor division would force their sum to vanish modulo \(p^2\), contrary to
\[
\sum_{j=1}^{p-1}j=\frac{p(p-1)}2\not\equiv0\pmod {p^2}.
\]
Thus \(\nu_p(u^{p-1}-1)=1\). The lifting-the-exponent identity at odd \(p\) gives \(\nu_p(u^{(p-1)p^v}-1)=1+v\) for \(v\ge0\). Since \(p-1\mid T\) and \(u^T\equiv1\pmod {p^a}\), necessarily \(p^{a-1}\mid T\). Therefore \(\lambda(p^a)\mid T\). For \(a=1\), the residue-group argument alone proves this.

**3. No shorter period at powers of two.** For \(a\ge2\), use the coefficient
\[
c_{n,3}=3^n-3\cdot2^n+3\qquad(n>0).
\]
Once \(n\ge a\), any eventual period \(T\) implies \(3^T\equiv1\pmod {2^a}\). The order of \(3\) modulo \(2^a\) equals \(\lambda(2^a)\), so this divides \(T\). The case \(a=1\) is immediate. Applying steps 2–3 to every prime-power factor of \(m\) proves \(L(m)\mid T\) for every eventual period modulo \(m\).

**4. Optimality of the starting index.** Choose any \(p^a\parallel m\) with \(a=R(m)\). If \(a=1\), the constant coefficient of \(G_0\) is \(1\), whereas it is \(0\) for every \(G_T\) with \(T>0\): no period starts at zero. Suppose \(a\ge2\). Every eventual period \(T\) modulo \(m\) is divisible by \(\lambda(p^a)\) by steps 2–3. At \(n=a-1\), examine coefficient \(k=p\). For \(1\le j<p\) the differences \(j^{n+T}-j^n\) vanish modulo \(p^a\), while the \(j=p\) term contributes
\[
c_{a-1+T,p}-c_{a-1,p}\equiv p^{a-1}(p^T-1)\equiv-p^{a-1}\not\equiv0\pmod {p^a}.
\]
The \(j=0\) contribution is zero at these positive indices. Hence no eventual period can begin at or before \(a-1\). Together with step 1, this proves both claimed sharp invariants.

## Verification

The standalone standard-library verifier `verify_geometric_period.py` constructs coefficients by the independent Stirling recurrence \(S(n,k)=kS(n-1,k)+S(n-1,k-1)\). For every modulus \(2\le m\le100\), it checks the asserted periodicity across consecutive indices, the failure of every shorter positive period, and the failure of every positive period up through \(L(m)\) at the proposed sharp boundary. A second computation checks \(630\) inclusion–exclusion coefficient identities. Execution: `python3 verify_geometric_period.py`. Observed result:

`VERIFY_OK moduli=99 period_pairs=6070 minimal_preperiod_checks=99 independent_coefficient_identities=630`

These finite checks test normalization and boundaries, but are not evidence for the universal quantifiers; steps 1–4 establish the result for all moduli.

## Relationship to prior work

The inclusion–exclusion expression and eventual periodicity of each fixed Stirling column modulo prime powers are classical; Zhao, Hong and Zhao discuss this explicitly. Mező studied last-digit periodicity of several combinatorial numerical sequences, including Fubini numbers. Mihoubi and Taharbouchet established congruences for generalized Fubini polynomials, notably a prime-modulus index reduction. Those results provide the background, not a claim of discovering coefficientwise periodicity itself.

A later general Stirling-transform periodicity preprint of Danesh describes a Carmichael-type *eventual period* for broad sequences. Such an upper-period statement includes or closely parallels the upper bound here, but by itself does not determine either least period or first valid starting index. The distinct claim here is the **simultaneous exact period and preperiod at every modulus**. One archived research record gives sharper, shorter periods for fixed scalar evaluations near a special residue; evaluation can shorten a period and therefore does not imply or contradict the coefficientwise theorem.

## Limitations

The result concerns polynomials as formal coefficient vectors modulo a modulus. It does not assert that \(\lambda(m)\) is the least period of \(G_n(t)\) for every integer \(t\), nor that it is the least period of the polynomial functions on \(\mathbb Z/m\mathbb Z\). Literature overlap remains possible, especially in exact-period refinements of integer-valued Stirling transforms. No independent validation has been performed.

## References

1. J. Zhao, S. Hong, W. Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, arXiv:1209.6284v1 (first public version 2012-09-27), https://arxiv.org/abs/1209.6284.
2. I. Mező, *Periodicity of the last digits of some combinatorial sequences*, arXiv:1308.1637v1 (2013), https://arxiv.org/abs/1308.1637.
3. M. Mihoubi, S. Taharbouchet, *Identities and congruences involving the Fubini polynomials*, arXiv:1706.08950v1 (2017), https://arxiv.org/abs/1706.08950.
4. P. Danesh, *A Valuation Criterion for Totient-Periodic Stirling Transforms*, viXra:2608.0078v1 (2026), https://vixra.org/abs/2608.0078.
