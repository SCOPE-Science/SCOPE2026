# Multinomial least-common-multiple law and exact specialization at one

## Finding
For integers \(n\ge1\) and \(r\ge2\), let \(\mathcal C_{n,r}\) be the set of ordered \(r\)-tuples of nonnegative integers with sum \(n\). For \(\mathbf k=(k_1,\ldots,k_r)\in\mathcal C_{n,r}\), put
\[
M_{n,\mathbf k}(q)=\frac{[n]_q!}{\prod_{i=1}^r[k_i]_q!},\qquad
[t]_q!=\prod_{j=1}^t\frac{1-q^j}{1-q},\quad [0]_q!=1.
\]
The quotients are monic polynomials in \(\mathbb Z[q]\). Write \(\Phi_d(q)\) for the \(d\)-th cyclotomic polynomial, and define
\[
E_d(n,r)=\min\left\{\left\lfloor\frac nd\right\rfloor,
\left\lfloor\frac{r(d-1)-(n\bmod d)}d\right\rfloor\right\}\quad(d\ge2).
\]
Then the **complete polynomial least-common-multiple factorization** is
\[
\boxed{\operatorname{lcm}_{\mathbf k\in\mathcal C_{n,r}}M_{n,\mathbf k}(q)
=\prod_{d=2}^{n}\Phi_d(q)^{E_d(n,r)}.}
\tag{1}
\]
Moreover, specialization at \(q=1\) **commutes exactly with this polynomial least common multiple**:
\[
\boxed{\operatorname{lcm}_{\mathbf k\in\mathcal C_{n,r}}\frac{n!}{k_1!\cdots k_r!}
=\prod_{p\le n\;\mathrm{prime}}p^{\sum_{j\ge1}E_{p^j}(n,r)}
=\left.\operatorname{lcm}_{\mathbf k\in\mathcal C_{n,r}}M_{n,\mathbf k}(q)\right|_{q=1}.}
\tag{2}
\]
In particular, the simultaneous optimization of every base-\(p\) carry depth is possible within **one** composition of \(n\) into \(r\) parts. For \(r=2\), (1) reduces to the known Guo identity; for \(r\ge3\) prime-power cyclotomic factors can have exponent greater than one (for example \(E_4(8,3)=2\)).

## Assumptions and scope
All tuples are ordered and may contain zero parts. The integer \(n\) is positive and \(r\ge2\) is an integer. The least common multiple of the Gaussian multinomial polynomials is the monic least common multiple in \(\mathbb Z[q]\); the second LCM concerns positive integers. Empty products equal one, so \(n=1\) is covered. Formula (2) does **not** assert an analogous commutation after substituting arbitrary integers \(q\ge2\).

## Proof
**Cyclotomic factors.** For \(d\ge2\), the exponent of \(\Phi_d(q)\) in \([t]_q!\) is \(\lfloor t/d\rfloor\), since \([j]_q=\prod_{d\mid j,\,d>1}\Phi_d(q)\). Consequently
\[
\nu_{\Phi_d}(M_{n,\mathbf k})=
\left\lfloor\frac nd\right\rfloor-\sum_{i=1}^r\left\lfloor\frac{k_i}d\right\rfloor
=\frac{\sum_{i=1}^r(k_i\bmod d)-(n\bmod d)}{d}\ge0.\tag{3}
\]
This proves polynomial integrality, and all factors are monic.

**Sharp local maximum.** Set \(s=n\bmod d\). The sum of the \(r\) residues \(k_i\bmod d\) is at most \(\min\{n,r(d-1)\}\) and is congruent to \(s\pmod d\). The largest possible value of this sum is therefore
\[
s+d\min\left\{\left\lfloor\frac nd\right\rfloor,
\left\lfloor\frac{r(d-1)-s}{d}\right\rfloor\right\}.
\]
It is attained: any integer from zero through \(r(d-1)\) is a sum of \(r\) integers in \([0,d-1]\), and the remaining nonnegative multiple of \(d\) can be added to the first part. Thus the maximum in (3), over all compositions, is precisely \(E_d(n,r)\). Pairwise distinct cyclotomic polynomials are irreducible and coprime in \(\mathbb Q[q]\), so the monic LCM has precisely their maximal exponents. This establishes (1).

**Carry-maximum lattice lemma.** Fix a prime \(p\), let \(L=\lfloor\log_p n\rfloor\), and write \(n=\sum_{j=0}^L n_jp^j\). For any composition \(\mathbf k\), define
\[
c_j(\mathbf k)=\left\lfloor\frac{\sum_i(k_i\bmod p^j)}{p^j}\right\rfloor
\quad (1\le j\le L),\qquad c_0=c_{L+1}=0.
\]
These are the simultaneous base-\(p\) carry amounts, not merely indicators. They satisfy
\[
0\le n_j+p c_{j+1}-c_j\le r(p-1)\qquad (0\le j\le L).\tag{4}
\]
Conversely, any nonnegative integer vector \((c_0,\ldots,c_{L+1})\) with zero endpoints satisfying (4) is realized by some composition: independently at each digit position express the integer \(n_j+p c_{j+1}-c_j\) as the sum of \(r\) digits from \(\{0,\ldots,p-1\}\). The resulting \(r\) integers add to \(n\), by telescoping the weighted digit sums.

The feasible carry vectors are closed under **coordinatewise maximum**. Indeed, for two feasible vectors \(a,b\), fix an edge \(j\to j+1\). If the maxima of the two coordinates come from the same vector, (4) is inherited. In the crossing case, without loss of generality \(a_j\ge b_j\) and \(b_{j+1}\ge a_{j+1}\). Then
\[
0\le n_j+p a_{j+1}-a_j\le n_j+p b_{j+1}-a_j
\le n_j+p b_{j+1}-b_j\le r(p-1).
\]
Thus the coordinatewise maximum again satisfies (4), proving closure and realization.

For every \(j\), the sharp local maximum argument applied with \(d=p^j\) shows that \(\max_{\mathbf k}c_j(\mathbf k)=E_{p^j}(n,r)\). Take one maximizing composition for each of the finitely many \(j\) and repeatedly take coordinatewise maxima of their feasible carry vectors. By closure, one composition simultaneously realizes every maximum.

**Specialization.** Legendre's factorial formula and (3) give
\[
\nu_p\!\left(\frac{n!}{\prod_i k_i!}\right)
=\sum_{j\ge1}\left(\left\lfloor\frac{n}{p^j}\right\rfloor-
\sum_i\left\lfloor\frac{k_i}{p^j}\right\rfloor\right)
=\sum_{j\ge1}c_j(\mathbf k).
\]
The preceding lemma implies that the maximum of this sum equals \(\sum_{j\ge1}E_{p^j}(n,r)\). Every prime dividing a multinomial coefficient is at most \(n\). Meanwhile \(\Phi_d(1)=p\) when \(d\) is a positive prime power \(p^j\), and \(\Phi_d(1)=1\) for other \(d>1\). Evaluate (1) at one and compare the prime exponents to obtain (2).

## Verification
The self-contained script `verify_multinomial_lcm.py` checks all ordered compositions for \(1\le n\le18\) and \(2\le r\le\min\{5,n\}\) against both exponent laws, and independently checks the factorization of Gaussian multinomial evaluations at \(q=2,3\) for \(n\le10\). Run `python3 verify_multinomial_lcm.py` alongside this file. The recorded result was `VERIFY_OK row_compositions=42310 q_factorizations=2610`. All calculations use exact integers. This is finite corroboration; the proof above establishes the infinite family.

## Relationship to prior work
Farhi (2009) evaluated the ordinary binomial-row LCM for two parts. Guo (arXiv:0907.2870, first posted 2009-07-16) proved its polynomial Gaussian analogue and the coincidence at \(q=1\) when \(r=2\); his paper's Theorem 2 and Section 3 do not include any \(r\ge3\) formula. Howard (1974) studied the full divisibility-counting problem for ordinary multinomial coefficients via generating functions; this provides a more general route to individual integer valuation frequencies, but no Gaussian polynomial LCM factorization or coordinatewise-carry lattice specialization theorem is stated in the inspected sections. Bergman (arXiv:0806.0607) studies common divisors of selections of multinomial coefficients, not their row LCM. The existing generalized Kummer valuation formula is used here, not claimed as new.

## Limitations
The results are exact but do not establish uniqueness of a maximizing tuple: several extremizers may exist. The finite script is not a substitute for the carry-lattice proof. The searched record is incomplete; an equivalent result in unindexed literature or derivable from earlier unpublished arguments remains a priority risk. The polynomial LCM specialization statement concerns only \(q=1\), not arbitrary numeric evaluations. No independent mathematical audit has been performed.

## References
1. Victor J. W. Guo, *On the least common multiple of q-binomial coefficients*, arXiv:0907.2870v1 (2009), https://arxiv.org/pdf/0907.2870.
2. B. Farhi, *An identity involving the least common multiple of binomial coefficients and its application*, American Mathematical Monthly (2009), as cited in Guo (2009).
3. F. T. Howard, *The number of multinomial coefficients divisible by a fixed power of a prime*, Pacific Journal of Mathematics 50 (1974), 99–111, https://msp.org/pjm/1974/50-1/pjm-v50-n1-p12-s.pdf.
4. George M. Bergman, *On common divisors of multinomial coefficients*, arXiv:0806.0607 (2008), https://arxiv.org/abs/0806.0607.
