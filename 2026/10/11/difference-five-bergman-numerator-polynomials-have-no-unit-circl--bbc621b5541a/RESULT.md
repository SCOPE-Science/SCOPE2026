# Difference-five Bergman numerator polynomials have no unit-circle zeros

## Finding

For every positive integer \(n\) not divisible by \(5\), let \(m=n+5\) and let \(Q_{m,n}\) be the palindromic diagonal Bergman numerator defined in Edholm--Mathew [1, Theorems 1.3 and 1.5]. Then
\[
Q_{n+5,n}(s)\ne0\qquad (|s|=1).
\]
In fact, if \(s=e^{i\theta}\) and \(x=\cos\theta\), then
\[
e^{-5i\theta}Q_{n+5,n}(e^{i\theta})>0\qquad (-1\le x\le1).
\]
Consequently \(Q_{n+5,n}\) has exactly **five zeros counted with multiplicity** in the punctured open unit disk and five outside the closed disk. The Bergman kernel of every rational Hartogs triangle \(\mathbb H_{(n+5)/n}\) therefore has zeros on the diagonal parameter slice of its two-point domain. This establishes the difference-five case of Conjecture 4.20 of [1].

## Assumptions and scope

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(\mathbb D^*=\mathbb D\setminus\{0\}\), and
\[
\mathbb H_{m/n}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{m/n}<|z_2|<1\}.
\]
The integers obey \(n\ge1\), \(m=n+5\), and \(\gcd(m,n)=1\), equivalently \(5\nmid n\). With \(s=z_1\overline{w_1}\) and \(t=z_2\overline{w_2}\), [1, (1.4)] supplies
\[
K_{m/n}(z,w)=\frac{P_{m,n}(s,t)}{m\pi^2(1-t)^2(t^n-s^m)^2},\qquad
Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s).
\]
These formulas fix the normalization. No assertion is made about all numerator zeros in the two-dimensional \((s,t)\)-domain or about a uniform distance between diagonal roots and the unit circle as \(n\to\infty\).

## Proof

**1. Exact coefficient reduction.** Put \(m=n+5\), and for each integer \(1\le t\le m-1\) define
\[
h_t=\left\lfloor\frac{5t-1}{m}\right\rfloor,\qquad
A_t=m(h_t+1)-5t,\qquad B_t=5t-mh_t.
\]
These satisfy \(0\le h_t\le4\) and \(A_t,B_t>0\). Substituting \(j=t-1\) into the definitions of \(L(j)\) and \(\kappa(j)\) in [1, (1.4h)] gives
\[
L(t-1)=t-h_t,\quad\kappa(t-1)+1=A_t,\quad
m-\kappa(t-1)-1=B_t.
\]
Write \(Q_{m,n}(s)=\sum_{j=0}^{10}c_js^j\). The full formula [1, (1.4c)--(1.4g)] yields the following exact coefficient construction, with all unmentioned initial values zero:
\[
\begin{aligned}
c_5&\mathrel{+}=m^2,\\
c_{h_t}&\mathrel{+}=tA_t, &c_{h_t+1}&\mathrel{+}=tB_t,\\
c_{5+h_t}&\mathrel{+}=(m-t)A_t,
&c_{6+h_t}&\mathrel{+}=(m-t)B_t
\end{aligned}\quad(1\le t<m).
\]
In particular the coefficients are positive at both endpoints, and the palindromicity \(c_j=c_{10-j}\) follows from [1, Theorem 1.5] (and can be checked from this construction).

**2. Four residue classes and an exact cubic identity.** Write \(n=5q+r\) with \(q\in\mathbb Z_{\ge0}\) and \(r\in\{1,2,3,4\}\), so \(m=5(q+1)+r\). For each \(h\in\{0,1,2,3,4\}\), the integers satisfying \(h_t=h\) are precisely
\[
\left\lfloor\frac{hm}{5}\right\rfloor<t\le
\left\lfloor\frac{(h+1)m}{5}\right\rfloor.
\]
Since \(\lfloor hm/5\rfloor=h(q+1)+\lfloor hr/5\rfloor\), every endpoint is affine in \(q\). All coefficient contributions from step 1 are quadratic polynomials in \(t,q\), so the sums of \(1,t,t^2\) on these intervals are polynomials in \(q\) of degree at most three. Therefore *every* \(c_j\), at fixed \(r\), is a polynomial in \(q\) of degree at most three. This degree bound is crucial: checking four exact integer values of \(q\) proves an identity for every \(q\), rather than merely producing a finite experiment.

Let \(T_j\) denote the usual Chebyshev polynomials, so that \(T_j(\cos\theta)=\cos(j\theta)\). By palindromicity,
\[
R_{r,q}(x):=e^{-5i\theta}Q_{m,n}(e^{i\theta})
=c_5+2\sum_{j=1}^{5}c_{5-j}T_j(x),\qquad x=\cos\theta.
\]
Exact summation of step 1 (equivalently, the four-node polynomial-identity certificate in `verify_hartogs.py`) gives
\[
\boxed{R_{r,q}(x)=\left(\frac53q^3+(r+5)q^2\right)F(x)
+q\,\mathcal B_r(x)+\mathcal C_r(x)},
\qquad F(x)=(x+2)(4x^2+2x-1)^2,
\]
where the eight degree-five polynomials are, in descending powers,
\[
\begin{aligned}
3\mathcal B_1&=304x^5+1056x^4+652x^3-288x^2-169x+65,\\
3\mathcal B_2&=448x^5+1392x^4+856x^3-324x^2-238x+71,\\
3\mathcal B_3&=592x^5+1824x^4+1108x^3-432x^2-301x+89,\\
3\mathcal B_4&=736x^5+2352x^4+1408x^3-612x^2-358x+119,
\end{aligned}
\]
\[
\begin{aligned}
\mathcal C_1&=32x^5+144x^4+96x^3-44x^2-26x+14,\\
\mathcal C_2&=64x^5+208x^4+144x^3-40x^2-48x+15,\\
\mathcal C_3&=96x^5+320x^4+208x^3-68x^2-64x+20,\\
\mathcal C_4&=128x^5+480x^4+304x^3-136x^2-80x+33.
\end{aligned}
\]

**3. Strict rational Bernstein certificate.** Partition \([-1,1]\) into eight intervals
\(I_j=[-1+j/4,-1+(j+1)/4]\), \(0\le j\le7\). For any degree-at-most-five polynomial \(G\), map \(I_j\) affinely onto \([0,1]\). The Bernstein expansion on that interval is
\[
G\big(-1+j/4+u/4\big)=\sum_{k=0}^{5}\beta_{j,k}(G)
\binom5k u^k(1-u)^{5-k},\quad 0\le u\le1.
\]
All \(8\cdot6\) coefficients are **strictly positive**, separately for each \(\mathcal B_r\) and \(\mathcal C_r\). The exact *minimum coefficient* over these 48 numbers is:

| \(r\) | \(\min\beta(\mathcal B_r)\) | \(\min\beta(\mathcal C_r)\) |
|---|---:|---:|
| 1 | \(1841/480\) | \(107/20\) |
| 2 | \(29/48\) | \(77/40\) |
| 3 | \(119/480\) | \(81/40\) |
| 4 | \(83/30\) | \(289/40\) |

The identity and all 384 positive coefficients can be reproduced using only exact rational arithmetic by `verify_hartogs.py`; `BERNSTEIN_CERTIFICATE.json` records every coefficient. Because Bernstein basis functions are nonnegative and sum to one, all \(\mathcal B_r,\mathcal C_r\) are strictly positive on the entire closed interval \([-1,1]\). In the same interval \(F(x)\ge0\), and \((5q^3/3+(r+5)q^2)\ge0\). Consequently \(R_{r,q}(x)>0\) for every allowed \(q,r,x\).

**4. Root count and Bergman zeros.** Therefore \(Q_{m,n}\) has no zeros on the unit circle. It is palindromic of degree ten, has a nonzero constant term and leading coefficient, and its roots occur in reciprocal pairs, with multiplicity. Precisely five of its zeros lie inside \(\mathbb D^*\). If \(s\) is any such zero, then \((s,s)\in\mathbb H_{m/n}\) because \(|s|^{m/n}<|s|<1\). As observed in [1, Section 1.2.1], every such pair arises as \((z_1\overline{w_1},z_2\overline{w_2})\) for some \(z,w\in\mathbb H_{m/n}\). On this slice the kernel denominator is nonzero, since \(s\ne0\), \(|s|<1\), and
\(s^n-s^m=s^n(1-s^5)\ne0\). Hence \(K_{m/n}(z,w)=0\).

## Verification

Run `python3 verify_hartogs.py` in the directory containing this document and `BERNSTEIN_CERTIFICATE.json`. The standalone checker reconstructs the source coefficients from [1, (1.4)], derives the Chebyshev expression, verifies all \(4\times4=16\) exact identities at the four nodes \(q=0,1,2,3\), and checks all \(4\times2\times8\times6=384\) rational Bernstein coefficients strictly positive against the certificate. The degree-three argument in step 2 supplies the necessary infinite-family justification; 16 sampled identities without that argument would not suffice. No floating point arithmetic, external math system or numerically truncated root-finding is used.

## Relationship to prior work

The source [1] proved the difference-one and difference-two cases and, in Section 4.3, reported arguments for differences three, four and six. It explicitly singled out difference five as open (its Conjecture 4.20). The present proof supplies all four congruence classes needed for difference five, rather than only isolated pairs or the general existence of infinitely many pairs at each fixed difference. The earlier Edholm--McNeal work [2] determined kernel zeros in particular parameter regimes, but did not cover this complete difference-five family with slopes in \((1,2)\).

## Limitations

The theorem treats only relatively prime pairs with \(m-n=5\), not arbitrary differences. The assertion counts diagonal polynomial roots with multiplicity; it does not claim that they are simple or give their positions. The theorem is conditional on the published exact normalization of the Bergman numerator [1], which is explicitly used and algebraically reconstructed above. It does not claim novelty against unpublished work or against literature not located by the comparisons cited here. No independent audit has been performed.

## References

[1] L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489 (first posted 2025-05-26); *Mathematische Zeitschrift* 313, article 43 (2026). DOI: 10.1007/s00209-026-04059-8. Theorem 1.3, Theorem 1.5, Section 4.3, Conjecture 4.20. https://arxiv.org/abs/2505.20489 ; https://link.springer.com/article/10.1007/s00209-026-04059-8

[2] L. D. Edholm and J. D. McNeal, *Bergman subspaces and subkernels: Degenerate \(L^p\) mapping and zeroes*, *Journal of Geometric Analysis* 27 (2017), 2658–2683. arXiv:1605.06223; DOI: 10.1007/s12220-017-9777-4. For the relation to the presently studied numerator and its known-zero regimes see [1, Section 1.3].
