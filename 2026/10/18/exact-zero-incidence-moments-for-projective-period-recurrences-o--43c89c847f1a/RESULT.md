# Exact zero-incidence moments for projective-period recurrences over odd prime-power rings

## Finding

Let \(p\) be any odd prime, \(d\ge3\) an integer with \(\gcd(d,p-1)=1\), and \(L=(p^d-1)/(p-1)\). Let \(A\) be a \(d\)-by-\(d\) integral matrix whose reduction modulo \(p\) has irreducible characteristic polynomial and multiplicative order exactly \(L\). Suppose \(A^L=I+pB\), where the reduction of \(B\) is not a scalar matrix. Let \(\ell\) be any integer row whose reduction modulo \(p\) is nonzero. For each \(k\ge1\), let \(\mathcal C_k\) be the cycles of \(x\mapsto Ax\) on the primitive vectors of \((\mathbb Z/p^k\mathbb Z)^d\), and put \(Z_k(C)=|\{0\le t<|C|:\ell A^t x\equiv0\pmod{p^k}\}|\), for any \(x\in C\).

Every cycle has exactly \(Lp^{k-1}\) states, the number of cycles is \((p-1)p^{(d-1)(k-1)}\), and uniformly over these cycles,

\[\mathbb E Z_k=\frac{p^{d-1}-1}{p-1},\qquad \operatorname{Var}(Z_k)=(p^{d-2}-1)(k-1).\]

Equivalently, the exact second raw moment is the square of this mean plus \((p^{d-2}-1)(k-1)\). In particular, the mean is independent of prime-power depth, whereas the variance grows linearly in that depth. The result applies to **any primitive linear observable**, not just one coordinate.

## Assumptions and scope

Here primitive means not divisible by \(p\) in all coordinates, and the hypothesis on \(B\) is a genuine non-scalar lift condition; without it, the stated period need not hold. There are no distributional or random-matrix assumptions. The uniform measure is on distinct complete orbits, each weighted once; equal orbit length makes this equivalent to uniform primitive states. The coprimality condition makes the order-\(L\) subgroup meet the scalar group trivially. The claim holds for every positive exponent \(k\), including \(k=1\), when the variance is zero.

## Proof

Write \(V_k=(\mathbb Z/p^k\mathbb Z)^d\) and \(U_k=|V_k\setminus pV_k|=(p^d-1)p^{d(k-1)}\). Reduction of \(A\) acts as multiplication by an element \(\alpha\in\mathbb F_{p^d}^\times\) of order \(L\). Since \(\gcd(L,p-1)=\gcd(d,p-1)=1\), for every \(h\) not divisible by \(L\), the two rows \(\bar\ell\) and \(\bar\ell\bar A^h\) are independent over \(\mathbb F_p\): proportionality would say \(\alpha^h\) is a scalar over \(\mathbb F_p\), contradicting the trivial scalar intersection. This argument works for every nonzero linear functional \(\bar\ell\), because the trace pairing identifies such a functional with a nonzero element of the field.

The matrix \(B\) commutes with \(A\). The centralizer of \(\bar A\) is the field \(\mathbb F_{p^d}\); consequently \(\bar B\) acts as multiplication by some element \(\beta\notin\mathbb F_p\). The rows \(\bar\ell\) and \(\bar\ell\bar B\) are therefore independent as well. In particular, \(\bar B\) is invertible.

For odd \(p\), binomial expansion of \(A^L=I+pB\) proves inductively that

\[A^{Lp^a}=I+p^{a+1}B_a,\qquad B_a\equiv B\pmod p\quad(a\ge0).\]

For \(t=p^a u\) with \(p\nmid u\), expansion again yields

\[A^{Lt}=I+p^{a+1}C_t,\qquad C_t\equiv uB\pmod p.\]

For any primitive vector, these identities imply that its period is exactly \(T_k=Lp^{k-1}\): reduction modulo \(p\) forces the exponent to be a multiple of \(L\), and \(B\bmod p\) is invertible so no shorter positive multiple fixes a primitive vector. Therefore the number of cycles is

\[|\mathcal C_k|=U_k/T_k=(p-1)p^{(d-1)(k-1)}.\]

Let \(N_h\) count primitive vectors \(x\in V_k\) satisfying the **two** congruences \(\ell x=\ell A^h x=0\pmod{p^k}\), where \(0\le h<T_k\). Single-incidence counting gives

\[N_0=(p^{d-1}-1)p^{(d-1)(k-1)},\qquad \mathbb EZ_k=T_k N_0/U_k=\frac{p^{d-1}-1}{p-1}.\]

If \(L\nmid h\), the two independent mod-\(p\) rows extend to a unimodular row transformation over \(\mathbb Z/p^k\mathbb Z\), and hence

\[N_h=(p^{d-2}-1)p^{(d-2)(k-1)}.\]

There are \((L-1)p^{k-1}\) such lags. For the remaining nonzero lags \(h=Lt\), put \(j=1+\nu_p(t)\), so \(1\le j\le k-1\). The first equation is \(\ell x=0\), and subtracting it from the second reduces the other equation to \(p^j\ell C_t x=0\pmod{p^k}\). As the two reductions \(\bar\ell\) and \(\bar\ell\bar C_t\) are independent, row operations put the system into the form \(x_1=0\) and \(p^j x_2=0\). Its primitive solutions satisfy \(x_2\equiv0\pmod{p^{k-j}}\), while the remaining \(d-2\) coordinates include a unit. Thus

\[N_h=(p^{d-2}-1)p^{(d-2)(k-1)+j}.\]

There are exactly \((p-1)p^{k-j-1}\) lags with this \(j\). Therefore

\[\sum_{h=0}^{T_k-1}N_h=p^{(d-1)(k-1)}\big[(p^{d-1}-1)+(L-1)(p^{d-2}-1)+(k-1)(p-1)(p^{d-2}-1)\big].\]

Counting ordered zero-hit pairs along all cycles, with the first hit fixing a state and the second fixing a lag, gives \(\mathbb E[Z_k^2]=(T_k/U_k)\sum_h N_h\). Since \(T_k/U_k=1/[(p-1)p^{(d-1)(k-1)}]\), and direct algebra gives

\[\frac{(p^{d-1}-1)+(L-1)(p^{d-2}-1)}{p-1}=\left(\frac{p^{d-1}-1}{p-1}\right)^2,\]

the second moment is exactly the claimed squared mean plus \((k-1)(p^{d-2}-1)\). Subtracting \((\mathbb EZ_k)^2\) completes the proof. Each step uses finite congruence counts, not a limit argument.

## Verification

Run `python VERIFY.py` with Python 3 and no third-party dependencies. This enumerates complete primitive-vector cycles for the cubic Padovan companion matrix at \(p=3\), exponents \(1\) through \(4\), and at \(p=29\), exponent \(1\). It also checks the explicit irreducible quintic companion matrix at \(p=3\), exponents \(1\) and \(2\), independently reconstructing first and second moments using exact rational arithmetic. It checks mod-\(p\) matrix orders and the non-scalar lifts modulo \(p^2\). It prints `VERIFY_OK` on success.

For the cubic example, \(A=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}\), at \(p=3\) the periods are \(13\cdot3^{k-1}\), the mean is \(4\), and the variance is \(2(k-1)\). At \(p=29\), the same matrix has period \(871\cdot29^{k-1}\), mean \(30\), and variance \(28(k-1)\). An independent quintic example at \(p=3\) has period \(121\cdot3^{k-1}\), mean \(40\), and variance \(26(k-1)\). These finite checks are not substitutes for the general proof.

## Relationship to prior work

Ghorpade, Hasan, and Kumari (arXiv:0904.1331, first posted April 8, 2009) explain finite-field Singer-cycle and feedback-register structure; their inspected arXiv paper does not present the prime-power orbit-averaged second-moment law. Kamlovskii (2009, 2013) studies frequency characteristics and estimates for recurrences over Galois rings; abstracts and bibliographic information were accessible, but full texts were not, so their detailed theorems cannot responsibly be declared non-covering. The result here concerns the **exact covariance of zero incidences over all primitive cycles**, distinct from an estimate for one recurrence orbit. Independent checking of possible implicit coverage remains important.

## Limitations

The theorem assumes odd prime, degree at least three, coprimality of degree with \(p-1\), order exactly \(L\), an irreducible reduction, and a non-scalar first lift. It does not classify matrices satisfying those hypotheses, give the complete distribution of \(Z_k\), or address arbitrary characteristic polynomials. Accessible literature searching does not prove priority; the 2009 and 2013 Galois-ring papers should be independently compared in full when accessible. Self-review is not independent audit.

## References

1. S. R. Ghorpade, S. Ul Hasan and M. Kumari, *Primitive Polynomials, Singer Cycles, and Word-Oriented Linear Feedback Shift Registers*, arXiv:0904.1331 (first posted 2009-04-08), https://arxiv.org/abs/0904.1331.
2. O. V. Kamlovskii, *Frequency characteristics of linear recurrence sequences over Galois rings*, Sbornik Mathematics 200 (2009), 499–519, https://doi.org/10.1070/SM2009v200n04ABEH004006.
3. O. V. Kamlovskii, *Frequency characteristics of coordinate sequences of linear recurrences over Galois rings*, Izvestiya Mathematics 77 (2013), 1130–1154, https://doi.org/10.1070/IM2013v077n06ABEH002672.
