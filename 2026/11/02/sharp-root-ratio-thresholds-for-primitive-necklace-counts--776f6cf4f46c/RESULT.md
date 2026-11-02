# Sharp root-ratio thresholds for primitive-necklace counts

## Finding

For an integer alphabet size \(q\ge2\), let \(M_n(q)\) denote the number of primitive rotational necklaces of length \(n\) over \(q\) symbols. Equivalently,
\[
M_n(q)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d},\qquad n\ge1.
\]
All these numbers are positive integers. Put \(A_n(q)=M_n(q)^{1/n}\) and \(B_n(q)=A_{n+1}(q)/A_n(q)\). Define
\[
T(q)=\begin{cases}
14,&q=2,\\
8,&q=3,\\
6,&q=4\text{ or }5,\\
4,&q\ge6.
\end{cases}
\]
**Theorem.** For every integer \(q\ge2\), the sequence \(B_n(q)\) is strictly decreasing at every index \(n\ge T(q)\):
\[
B_{n+1}(q)<B_n(q)\quad(n\ge T(q)).
\]
The cutoff is sharp in the strong sense \(B_{T(q)}(q)>B_{T(q)-1}(q)\). Thus it gives the exact smallest index from which all successive root ratios decrease. For a prime-power \(q\), the same statement concerns the degree-counts of monic irreducible polynomials over \(\mathbb F_q\); these exact cutoffs were proposed in Remark 1.1 of Zhi-Wei Sun's 2012 paper [1]. The necklace formulation also covers non-prime-power alphabet sizes.

## Assumptions and scope

All alphabet sizes are **integers** \(q\ge2\), not arbitrary real parameters. All indices are positive integers; the inequality starts with \(n\ge4\), or later at the stated exceptional alphabets. \(\mu\) is the classical Möbius function. The number \(M_n(q)\) is an integer because a word of minimal period \(n\) has an orbit of size \(n\) under rotation. When \(q\) is a prime power it also equals the number of monic irreducible polynomials of degree \(n\) over \(\mathbb F_q\).

Set
\[
g_n(q)=\frac{\log M_n(q)}n,\qquad D_n(q)=g_{n+2}(q)-2g_{n+1}(q)+g_n(q).
\]
Because \(\log B_{n+1}-\log B_n=D_n\), strict decrease means \(D_n<0\). This equivalence fixes the orientation of every inequality. The finite comparison can be performed using only integers:
\[
D_n(q)<0\iff M_n(q)^{(n+1)(n+2)}M_{n+2}(q)^{n(n+1)}<M_{n+1}(q)^{2n(n+2)}.
\]
No floating-point comparisons are used in the finite certificate.

## Proof

**1. Uniform error control.** For \(n\ge4\), separate the leading term of Möbius inversion:
\[
nM_n(q)=q^n(1+r_n),\qquad r_n=q^{-n}\sum_{\substack{d\mid n\\d>1}}\mu(d)q^{n/d}.
\]
Every exponent in the remaining sum is a distinct integer at most \(\lfloor n/2\rfloor\). Geometric-series comparison gives
\[
|r_n|<\frac{q^{1-n/2}}{q-1}\le\frac12.
\]
Consequently, with \(h(x)=-\log(x)/x\), we have
\[
g_n(q)=\log q+h(n)+e_n(q),\qquad
|e_n(q)|=\frac{|\log(1+r_n)|}{n}<\frac{2q}{(q-1)nq^{n/2}}.
\]
Here the logarithmic inequality follows from \(|\log(1+t)|\le2|t|\) for \(|t|\le1/2\). Define
\[
L(n)=\frac{2\log n-3}{(n+2)^3},\qquad
E(n,q)=\frac{2q}{(q-1)nq^{n/2}}(1+2q^{-1/2}+q^{-1}).
\]
For \(n\ge6\), \(h''(x)=(3-2\log x)/x^3<0\) for all \(x\ge n\), and its magnitude is bounded below on \([n,n+2]\) by \(L(n)\). Since
\[
h(n+2)-2h(n+1)+h(n)=\int_0^1\!\int_0^1 h''(n+s+t)\,ds\,dt,
\]
it follows that
\[
D_n(q)<-L(n)+E(n,q).\tag{1}
\]
The error bound uses the three coefficients \(1,2,1\), the monotone envelope \(q^{-j/2}/j\), and the inequality \(j\ge n\).

**2. Two uniform tails.** For any \(n\ge6\) the ratio \(L(n+1)/L(n)\) exceeds \(((n+2)/(n+3))^3\). For fixed \(q\),
\[
\frac{E(n+1,q)}{E(n,q)}=\frac n{n+1}q^{-1/2}<q^{-1/2}.
\]
Moreover, for fixed \(n\), \(E(n,q)\) decreases as \(q\) increases. At \(n=6\), elementary logarithm bounds give
\[
L(6)>\frac1{1024}>\frac2{2187}=E(6,9).
\]
For every \(n\ge6\), \(((n+2)/(n+3))^3\ge(8/9)^3>1/3\). Induction on \(n\) therefore shows \(L(n)>E(n,9)\ge E(n,q)\) for \(q\ge9\). By (1),
\[
D_n(q)<0\quad(n\ge6,\ q\ge9).\tag{2}
\]
A second starting point controls *all* alphabets. At \(n=23\), \(\log23>3\) and \(\sqrt2>7/5\) imply
\[
L(23)>\frac3{15625}>\frac{29}{164864}>E(23,2).
\]
The final inequality follows by rewriting \(E(23,2)=(1+3/(2\sqrt2))/11776\). For all \(n\ge23\),
\[
\left(\frac{n+2}{n+3}\right)^3\ge\left(\frac{25}{26}\right)^3>\frac1{\sqrt2}.
\]
The same ratio induction and decrease of \(E(n,q)\) in \(q\) yield
\[
D_n(q)<0\quad(n\ge23,\ q\ge2).\tag{3}
\]
All inequalities in these two inductions are strict.

**3. The small-index universal signs.** Direct Möbius inversion gives
\[
M_3=\frac{q^3}{3}(1-q^{-2}),\quad M_4=\frac{q^4}{4}(1-q^{-2}),\quad
M_5=\frac{q^5}{5}(1-q^{-4}),
\]
\[
M_6=\frac{q^6}{6}(1-u),\qquad u=q^{-3}+q^{-4}-q^{-5}.
\]
First, \(h(5)-2h(4)+h(3)>0\), since \(4^{15}>3^{10}5^6\). With \(t=q^{-2}\in(0,1/4]\),
\[
D_3=\bigl(h(5)-2h(4)+h(3)\bigr)+\frac1{30}\log(1-t)+\frac15\log(1+t).
\]
The last two terms sum to a function vanishing at \(t=0\) with derivative \((5-7t)/(30(1-t^2))>0\) on \([0,1/4]\). Hence
\[
D_3(q)>0\quad(q\ge2).\tag{4}
\]
For the next index, \(h(6)-2h(5)+h(4)<0\), since \(5^{24}<6^{10}4^{15}\). Using \(\log(1-z)\le-z\), \(-\log(1-z)\le z/(1-z)\) and discarding the negative \(\log(1-u)\) term,
\[
D_4<\bigl(h(6)-2h(5)+h(4)\bigr)-\frac1{4q^2}+\frac2{5(q^4-1)}<0
\]
because \(5(q^4-1)>8q^2\) for all integers \(q\ge2\). Thus
\[
D_4(q)<0\quad(q\ge2).\tag{5}
\]
Finally, for \(q\ge6\), the two negative corrections from \(M_5\) and \(M_7\) give
\[
D_5(q)<\bigl(h(7)-2h(6)+h(5)\bigr)+\frac{u}{3(1-u)}.
\]
The function \(u=q^{-3}+q^{-4}-q^{-5}\) decreases with \(q\ge6\) and \(u\le41/7776\), whence \(u/(3(1-u))\le41/23205<1/400\). On the other hand, writing \(z=1/6\),
\[
-\bigl(h(7)-2h(6)+h(5)\bigr)
=\frac{\log6}{105}+\frac{\log(1-z)}5+\frac{\log(1+z)}7.
\]
The elementary atanh and alternating-log expansions give
\[
\log6>\frac{89}{50},\qquad
-\log(1-z)<\frac{2363}{12960},\qquad
\log(1+z)>\frac{799}{5184};
\]
indeed \(\log2>56/81\) and \(\log3>263/240\) give the first bound; the final two follow by truncating power series with one-sided tails. Thus
\[
-\bigl(h(7)-2h(6)+h(5)\bigr)>\frac{541}{216000}>\frac1{400}.
\]
It follows that
\[
D_5(q)<0\quad(q\ge6).\tag{6}
\]
In combination, (4)–(6) establish both the sharp witness at \(n=3\) and the two missing small indices for every \(q\ge6\), while (2) completes their infinite tails.

**4. Finite exact certificate and sharpness.** It remains to treat \(2\le q\le8\) in the intervals not covered by (2), (3), (5), or (6). The standalone \(\texttt{verify.py}\) computes \(M_n(q)\) by integer Möbius inversion and compares exact integer powers using the equivalent inequality in the scope section. It verifies **all 115 pairs** \(T(q)\le n\le22\), \(2\le q\le8\), and confirms \(D_{T(q)-1}(q)>0\) for each of these seven values of \(q\). (The universal formula (4) establishes the witness for all \(q\ge9\).) The program also tests \(q^n=\sum_{d\mid n}dM_d(q)\) at 168 further pairs. No approximate roots, floating-point logarithms, probabilistic tests, or time-limited enumeration are used. Combined with (3), these finite exact tests prove the remaining infinite assertions. This also establishes that none of the four cutoff levels can be reduced.

## Verification

From the folder containing this document, run \(\texttt{python3 verify.py}\) with standard Python 3. The successful deterministic certificate prints:

```text
VERIFY_OK finite_suffix=115 exact_witnesses=7 inversion_cases=168
CHECK_OK analytic_rational_inequalities=8
```

The source is included in full. The assertions prove 115 strict signed integer inequalities, seven reverse inequalities, the Möbius inversion identities on a separate grid, and key rational comparisons in the analytic proof. For the infinitely many untested index/alphabet pairs, the argument is the explicit analytic bound and ratio induction above, not numerical extrapolation.

## Relationship to prior work

Zhi-Wei Sun [1, Theorem 1.1 and Remark 1.1] gave an eventual root-ratio monotonicity theorem for monic irreducible polynomial counts only past \(n\ge5.835\times10^{14}\), then proposed the exact four cutoff regimes exhibited here. The present proof supplies those exact thresholds and their sharp witnesses, and holds for all integer alphabet sizes, not only finite-field orders. It uses a different short two-tail estimate plus finite exact certificates; the basic Möbius estimate is classical and was also stated by Sun.

Chebolu, Mináč, Nguyen, and Tân [2, Theorems 1.1–1.3 and 5.6] established monotonicity in the real alphabet parameter and eventual log-convexity of the **unrooted sequence** \(M_n(x)\), with a sharp \(x=8\) boundary for a different second-order question. The present sign concerns \(\Delta^2(\log M_n(q)/n)\), so neither their log-convexity theorem for \(\log M_n\) nor their first-order monotonicity theorem directly supplies these index-by-index root-ratio thresholds. In particular the claimed sign of the rooted second difference is negative where unrooted log-convexity is positive. The 2012 numerical cutoff conjecture and the 2026 results are credited rather than claimed as new.

## Limitations

The theorem is for **integer** \(q\ge2\); no real-parameter sharp cutoff classification is claimed. Its exact small-index signs require the embedded integer certificate, whose assertions should be independently reproduced for external validation. Priority comparisons considered the directly relevant 2012 paper and a 2026 necklace-polynomial paper together with public searches; equivalently phrased earlier results in less visible literature cannot be excluded. The proof and computations have been reviewed within this package, but **independent mathematical audit has not been performed**.

## References

[1] Zhi-Wei Sun, *On irreducible polynomials over finite fields*, arXiv:1210.1562 (initial public posting October 4, 2012), especially Theorem 1.1, Lemmas 2.1–2.2, and Remark 1.1. https://arxiv.org/abs/1210.1562

[2] Sunil K. Chebolu, Ján Mináč, Tung T. Nguyen, and Nguyen Duy Tân, *Analytic Properties of Necklace Polynomials*, arXiv:2605.11445 (May 12, 2026), especially Theorems 1.1–1.3 and 5.6. https://arxiv.org/abs/2605.11445

[3] C. Moreau, *Sur les permutations circulaires distinctes*, Nouvelles annales de mathématiques, 2e série, 11 (1872), 309–314 (classical necklace enumeration).
