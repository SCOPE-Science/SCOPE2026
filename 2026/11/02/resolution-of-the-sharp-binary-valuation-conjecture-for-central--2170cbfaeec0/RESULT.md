# Resolution of the sharp binary valuation conjecture for central Delannoy numbers

## Finding

Let \(D_n\) be the \(n\)-th central Delannoy number, defined for every integer \(n\geq 0\) by
\[
D_n=\sum_{k=0}^{n}\binom{n}{k}^{2}2^{k}.
\]
For every integer \(n\geq1\),
\[
\nu_2(D_n-1)=
\begin{cases}
1,&n\text{ odd},\\
2,&n\equiv 2\pmod4,\\
3\nu_2(n),&4\mid n.
\end{cases}
\]
In particular, the third case proves Conjecture 3 of Lengyel (2021), and hence the first equality in his Conjecture 1. The exponent is exact: for each positive \(n\) divisible by four, the quotient \((D_n-1)/n^3\) is a \(2\)-adic unit (a rational number with odd numerator and denominator after cancellation of powers of two).

## Assumptions and scope

All sums indexed by \(k\) in the definition of \(D_n\) are finite integer sums. The valuation \(\nu_2\) is normalized by \(\nu_2(2)=1\). Rational series below converge in the complete field \(\mathbb Q_2\); no real convergence at their evaluation point is asserted. The theorem is for all positive integer indices, with the nontrivial cubic case restricted exactly to \(4\mid n\). The value \(n=0\) is excluded because \(D_0-1=0\).

## Proof

**1. The two smaller classes.** The term with \(k=1\) in \(D_n-1\) is \(2n^2\), and every term with \(k\ge2\) is a multiple of four. Thus for odd \(n\), \(D_n-1\equiv2\pmod4\). If \(n=2u\) with \(u\) odd, the first term is a multiple of eight and the \(k=2\) term is \(4\binom n2^2\equiv4\pmod8\); the remaining terms are multiples of eight. This establishes the first two cases.

**2. A vanishing dyadic dilogarithm.** Write \(\operatorname{Li}_2(z)=\sum_{j\ge1}z^j/j^2\) and \(\log(1-z)=-\sum_{j\ge1}z^j/j\), as power series about zero over \(\mathbb Q\). Formal differentiation, followed by evaluation at zero, proves
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac{z}{z-1}\right)
=-\frac12\log^2(1-z).
\]
For \(z=2\), both dilogarithmic series converge in \(\mathbb Q_2\); the substitution \(2/(2-1)=2\) is valid and \(\log(-1)=0\), since the \(2\)-adic logarithm vanishes on torsion. Consequently
\[
\sum_{j\ge1}\frac{2^j}{j^2}=0\qquad\text{in }\mathbb Q_2. \tag{1}
\]

**3. An interpolation identity.** Define polynomials
\[
P_j(t)=\prod_{i=1}^{j-1}\left(1-\frac{t}{i}\right)^2
=\sum_{m=0}^{2j-2}p_{j,m}t^m, \qquad P_1(t)=1.
\]
For every positive integer \(n\) and every \(j\le n\),
\[
\binom nj^2=\frac{n^2}{j^2}P_j(n).
\]
For \(j>n\) the factor with \(i=n\) vanishes, hence \(P_j(n)=0\). It follows exactly that
\[
D_n-1=n^2\sum_{j\ge1}\frac{2^j}{j^2}P_j(n).
\]
After subtracting (1),
\[
\frac{D_n-1}{n^3}
=\sum_{j\ge1}\frac{2^j}{j^2}\sum_{m=1}^{2j-2}p_{j,m}n^{m-1}.
\tag{2}
\]
The estimates below prove uniform \(2\)-adic convergence of the expanded double series for \(n\in4\mathbb Z_2\), justifying regrouping and reduction modulo two.

**4. Exactly one surviving linear term.** Since \(p_{j,1}=-2\sum_{i=1}^{j-1}1/i\), for \(j\ge2\) we have
\[
\nu_2\left(\frac{2^j}{j^2}p_{j,1}\right)
\ge j+1-2\nu_2(j)-\lfloor\log_2(j-1)\rfloor.
\]
This is at least one except possibly \(j=4\): checking \(2\le j\le15\) directly shows the sole zero lower bound is \(j=4\), and for \(j\ge16\) the bound is greater than one because \(j+1-3\log_2j>1\). At \(j=4\), \(p_{4,1}=-11/3\), so the coefficient \((2^4/4^2)p_{4,1}=-11/3\) is odd. Every other linear contribution in (2) is even.

**5. All nonlinear terms cancel modulo two.** For \(j\ge2\), list the multiset
\[
\mathcal V_j=\{\nu_2(i),\nu_2(i):1\le i<j\}
\]
in decreasing order as \(v_1\ge\cdots\ge v_{2j-2}\). The elementary symmetric coefficient formula gives
\[
\nu_2\left(\frac{2^j}{j^2}p_{j,m}n^{m-1}\right)
\ge E(j,m):=j-2\nu_2(j)+2(m-1)-\sum_{h=1}^m v_h
\tag{3}
\]
for \(n\in4\mathbb Z_2\), \(2\le m\le2j-2\). Since \(v_h\) is nonincreasing, a lower bound valid for all these \(m\) is
\[
E(j,m)\ge j-2\nu_2(j)-2-2\sum_{h\ge3}\left\lfloor\frac{j-1}{2^h}\right\rfloor=:B(j).
\tag{4}
\]
Indeed, rewriting (3) as \(j-2\nu_2(j)-2+\sum_{h=1}^m(2-v_h)\), only the entries \(v_h>2\) can contribute negatively, and their total negative contribution is \(-2\sum_{h\ge3}\lfloor(j-1)/2^h\rfloor\).

For \(j\ge32\), the geometric-series bound gives
\[
B(j)>\frac{j-3}{2}-2\log_2j>1,
\]
where the last inequality holds at \(j=32\) and its left side is strictly increasing thereafter. For the finite interval \(9\le j\le31\), direct substitution into the explicit integer expression (4) gives \(B(j)\ge4\). For \(2\le j\le8\), direct sorting in (3) shows that the minimum over \(m\ge2\) is respectively \(2,3,0,3,2,5,0\), with equality to zero only for \((j,m)=(4,2)\) or \((8,2)\). These are finite integer comparisons, fully reproduced in the standalone checker.

It remains to evaluate those two possible odd terms. Exact multiplication of the defining polynomials gives
\[
p_{4,2}=\frac{193}{36},\qquad p_{8,2}=\frac{2105161}{176400}.
\]
Writing \(n=4u\), their combined contribution to (2) is
\[
u\left(\frac{193}{9}+\frac{2105161}{11025}\right),
\]
which is even in \(\mathbb Z_2\), because both displayed rational summands are \(2\)-adic units. Every other nonlinear contribution has valuation at least one by (3)–(4). For each fixed valuation threshold the bounds grow with \(j\), so the infinite sum is legitimate modulo two.

Therefore (2) is congruent to the single linear contribution \(-11/3\equiv1\pmod2\). Thus \((D_n-1)/n^3\) is odd in \(\mathbb Z_2\) for every \(4\mid n\), proving \(\nu_2(D_n-1)=3\nu_2(n)\). \(\square\)

## Verification

`VERIFIER.py` uses exact integer and rational arithmetic, without numerical approximations to the claimed valuations. It independently reconstructs Delannoy numbers using the classical Legendre three-term recurrence and verifies the theorem for the first 4096 positive integers. It separately checks the binomial definition, rational coefficients \(p_{4,1}\), \(p_{4,2}\), \(p_{8,2}\), all finite coefficient-bound cases \(2\le j\le31\), and vanishing of the dilogarithmic series modulo selected powers of two. The finite tests corroborate the argument; the proof for all indices is the non-Archimedean identity and coefficient bounds above.

## Relationship to prior work

Lengyel's *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers* (2021), §§2–3, proves only the lower bound \(\nu_2(D_{a2^r}-1)\ge2r+2\) for \(r\ge2\) and odd \(a\). Its Conjecture 3 explicitly proposes the sharp equality \(\nu_2(D_{2m}-1)=3\nu_2(2m)\) for even \(m\), exactly the nontrivial part proved here. Its Lemma 3 already supplies the two easier parity cases, which are re-proved for completeness. Mikić (2023) treats \(3\)-adic valuations of \(D_n\), and the later Legendre-value paper of Alekseyev–Amdeberhan–Shallit–Vukusic (2025) concerns \(\nu_p(P_n(p))\), not the difference \(P_n(3)-1\) at \(p=2\). Wang–Zhong (2025) studies weighted finite sums of Delannoy numbers, not this individual-term valuation identity. The inspected statements do not imply the sharp equality. No absolute priority claim is made beyond these comparisons.

## Limitations

The result does not settle Lengyel's separate conjectures about \(\nu_2(D_n+1)\) or successive-index differences, nor other prime valuations. Bibliographic searches cannot eliminate every unindexed or unpublished solution.

## References

1. T. Lengyel, *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers*, INTEGERS **21** (2021), #A86, published 2021-08-27, particularly Conjectures 1 and 3 and Lemma 3. https://math.colgate.edu/~integers/v86/v86.pdf
2. J. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623 (first posted 2023-11-24), https://arxiv.org/abs/2311.14623
3. M. A. Alekseyev, T. Amdeberhan, J. Shallit and I. Vukusic, *On the p-adic valuations of values of Legendre polynomials*, arXiv:2505.08935 (2025), https://arxiv.org/html/2505.08935v1
4. R.-H. Wang and M. X. X. Zhong, *Congruences for sums of Delannoy numbers and polynomials*, arXiv:2505.05728 (2025), https://arxiv.org/html/2505.05728v1
