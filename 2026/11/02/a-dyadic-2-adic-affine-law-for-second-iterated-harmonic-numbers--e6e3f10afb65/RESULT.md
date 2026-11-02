# A dyadic 2-adic affine law for second iterated harmonic numbers

## Finding
Let \(H(n)=\sum_{k=1}^{n}1/k\) and \(G(n)=\sum_{k=1}^{n}1/(kH(k))\). For each integer \(r\ge1\), put \(\Delta_r=G(2^r)-G(2^{r-1})\). All \(G(n)\) belong to \(\mathbb Z_2\), and there are unique \(C,D\in\mathbb Z_2\), with \(C\) odd, such that
\[
\Delta_r\equiv C\pmod{2^r},\qquad G(2^r)-rC\equiv D\pmod{2^{r+1}}\quad(r\ge1).
\]
In particular, these constants have the explicit residues \(C\equiv113\pmod{256}\) and \(D\equiv11\pmod{256}\), and the exact all-scale congruence is
\[
G(2^r)\equiv113r+11\pmod{256}\qquad(r\ge3).
\]
A supplementary exact parity description is \(G(n)\equiv1+\lfloor\log_2n\rfloor\pmod2\) for every \(n\ge1\). The statements concern 2-adic congruences, not integrality over the ordinary integers.

## Assumptions and scope
All indices are positive integers; \(\mathbb Z_2\) is the ring of 2-adic integers, and \(\nu_2\) is the usual valuation of nonzero rational numbers (extended with \(\nu_2(0)=+\infty\)). Congruences between rational numbers with odd reduced denominators are interpreted in \(\mathbb Z_2\). The constants \(C,D\) depend only on the displayed second-iterated-harmonic sequence and are defined by convergent 2-adic limits; no claim of ordinary-real convergence of the normalized sequence is made.

## Proof
**Exact valuations.** Put \(L(k)=\lfloor\log_2 k\rfloor\). The summand \(1/2^{L(k)}\) is the unique term of least 2-adic valuation in \(H(k)\). Hence \(\nu_2(H(k))=-L(k)\), and therefore
\[
\nu_2\!\left(\frac1{kH(k)}\right)=L(k)-\nu_2(k)\ge0.
\]
Equality holds exactly when \(k\) is a power of two. This proves \(G(n)\in\mathbb Z_2\), its parity formula, and that each \(\Delta_r\) is odd: the block \((2^{r-1},2^r]\) contains exactly one power of two.

**A normalized dyadic lifting bound.** For an odd integer \(a\ge1\), write \(\ell=\lfloor\log_2 a\rfloor\), and for \(t\ge0\) define
\[
W_t(a)=2^{\ell+t}H(a2^t),\qquad q_t(a)=\frac1{a2^tH(a2^t)}=\frac{2^\ell}{aW_t(a)}.
\]
The same unique-least-valuation argument makes \(W_t(a)\) an odd 2-adic unit. Splitting the even and odd denominators in \(H(2n)\) gives the exact rational identity
\[
W_{t+1}(a)-W_t(a)=2^{\ell+t+1}
\sum_{\substack{1\le u\le 2a2^t\\ u\ \mathrm{odd}}}\frac1u.
\]
The sum is 2-adically integral, so subtracting the two unit reciprocals proves
\[
\nu_2(q_{t+1}(a)-q_t(a))\ge2\ell+t+1.\tag{1}
\]
Also \(\nu_2(q_t(a))=\ell\) exactly.

**Blocks and convergence.** Every positive integer uniquely factors as \(2^t a\), where \(a\) is odd. For \(r\ge1\), those in the dyadic block \((2^{r-1},2^r]\) are the power \(2^r\) and, for each \(1\le\ell\le r-1\), the integers \(a2^{r-\ell-1}\) with \(2^\ell<a<2^{\ell+1}\) odd. Thus
\[
\Delta_r=q_r(1)+\sum_{\ell=1}^{r-1}
\sum_{\substack{2^\ell<a<2^{\ell+1}\\a\ \mathrm{odd}}}q_{r-\ell-1}(a).
\]
Compare consecutive blocks. The \(a=1\) term changes by an element of \(2^{r+1}\mathbb Z_2\) using (1). An existing term of odd-part scale \(\ell\) changes by an element of \(2^{r+\ell}\mathbb Z_2\) using (1); a newly introduced term at scale \(\ell=r\) lies in \(2^r\mathbb Z_2\). Consequently
\[
\Delta_{r+1}-\Delta_r\in2^r\mathbb Z_2\qquad(r\ge1).\tag{2}
\]
Completeness of \(\mathbb Z_2\) gives a unique limit \(C=\lim_{r\to\infty}\Delta_r\) and (2) gives \(C-\Delta_r\in2^r\mathbb Z_2\). Since every block increment is odd, \(C\) is odd. Similarly \(E_r=G(2^r)-rC\) satisfies \(E_{r+1}-E_r=\Delta_{r+1}-C\in2^{r+1}\mathbb Z_2\); hence \(E_r\) tends to a unique \(D\), with \(D-E_r\in2^{r+1}\mathbb Z_2\). This proves both all-scale congruences.

**Explicit first eight dyadic scales.** Exact rational evaluation modulo \(256\) gives, for \(r=3,4,5,6,7,8\), respectively,
\[
G(2^r)\bmod256=94,207,64,177,34,147.
\]
Thus \(\Delta_r\equiv113\pmod{256}\) for \(4\le r\le8\). Formula (2) makes the same congruence hold for every \(r\ge8\), because \(2^r\) is divisible by \(256\). Therefore \(C\equiv113\pmod{256}\), and starting at \(G(8)\equiv94\pmod{256}\), telescoping yields \(G(2^r)\equiv94+113(r-3)\equiv113r+11\pmod{256}\) for all \(r\ge3\). The limit estimate for \(D\) gives \(D\equiv G(8)-3C\equiv11\pmod{256}\), as the subsequent differences \(\Delta_s-C\) are zero modulo \(256\).

## Verification
The included standalone `verify.py` uses exact rational harmonic numbers and modular arithmetic to check all 512 initial summand valuations and parity residues; all six displayed dyadic residues; the modular block-constancy and adjacent-block divisibility bounds within the computed range; and 64 exact instances of the normalized-harmonic lifting inequality. Run with `python3 verify.py`. The code verifies a finite portion only. The infinite congruences follow from identity (1), block decomposition, and 2-adic completeness, not from finite extrapolation.

## Relationship to prior work
Ash, Ash, Ash, and Plaza introduced these iterated harmonic numbers and reported that the reduced denominators of the second iteration were odd in their computations through index 27,477. Their 2023 preprint establishes the corresponding valuation formula for the **first** harmonic numbers, but it does not present an all-index 2-adic parity proof, an affine dyadic limit, or the explicit modulus-256 congruence. The published 2026 journal abstract continues to describe numerical evidence for the integer-value conjecture; its complete later text was not available for a decisive full-text comparison. The present statement addresses the arithmetic of the second iteration, not the conjecture that its only ordinary integer term is the first one.

## Limitations
The theorem does not prove nonintegrality of any particular \(G(n)\) over \(\mathbb Z\), does not give real asymptotics, and does not assert a formula for analogous higher iterations. The two 2-adic constants are characterized by limits and given modulo 256, not by elementary rational closed forms. An implicit equivalent in the later full journal version or elsewhere cannot be ruled out by finite bibliographic searching.

## References
1. J. Marshall Ash, Michael Ash, Rafael Ash, and Ángel Plaza, *Iterated harmonic numbers*, first publicly posted 2023-03-06, arXiv:2303.02832, https://arxiv.org/abs/2303.02832 (Sections 2, 4 and 5).
2. J. Marshall Ash, Michael Ash, Rafael Ash, Nathan McNew, and Ángel Plaza, *Iterated Harmonic Numbers*, *College Mathematics Journal* 57 (2026), 193–205, DOI:10.1080/07468342.2026.2621673 (publisher abstract inspected; not relied on as full-text novelty evidence).
