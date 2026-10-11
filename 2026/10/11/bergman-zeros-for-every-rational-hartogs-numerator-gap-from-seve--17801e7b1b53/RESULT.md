# Bergman zeros for every rational Hartogs numerator gap from seven through seventeen

## Finding
Let \(k\) be any integer with \(7\le k\le17\), let \(n\ge1\) satisfy \(\gcd(n,k)=1\), and put \(m=n+k\). For the rational generalized Hartogs triangle
\[
\mathbb H_{m/n}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{m/n}<|z_2|<1\},
\]
write \(P_{m,n}\) for the explicit Bergman-kernel numerator of Edholm–Mathew and
\[
Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s).
\]
Then for every real \(\theta\),
\[
\boxed{e^{-ik\theta}Q_{m,n}(e^{i\theta})>0.}
\]
Consequently this degree-\(2k\) reciprocal polynomial has exactly \(k\) roots in \(0<|s|<1\) and exactly \(k\) in \(|s|>1\), counted with multiplicity. In particular the Bergman kernel of \(\mathbb H_{m/n}\) has an interior zero, so the domain is not Lu Qi-Keng. This verifies the stated unit-circle nonvanishing conjecture simultaneously for all eleven consecutive gaps \(k\in\{7,\ldots,17\}\), for infinitely many coprime pairs in each gap.

## Assumptions and scope
All integers are positive as above, and the first coordinate of \(\mathbb H_{m/n}\) may vanish. The statement concerns the diagonal numerator polynomial, not zeros of the kernel on the diagonal \(z=w\) (the positive definite kernel cannot vanish there). Equality in the displayed strict inequality is excluded. We use the original unweighted Bergman kernel and the normalization of Edholm–Mathew, whose positive prefactor does not affect its zeros. In the arguments below, \(\theta\in\mathbb R\) and \(x=(1+\cos\theta)/2\in[0,1]\).

## Proof
Edholm–Mathew, equation (3.21), gives the following reindexed form. For \(1\le j\le m-1\) put
\[
e_j=\left\lfloor\frac{kj-1}{m}\right\rfloor,\qquad
\tau_j=kj-me_j\in\{1,\ldots,m-1\}.
\]
The final inclusion uses \(\gcd(k,m)=1\). Then
\[
Q_{m,n}(s)=m^2s^k+\sum_{j=1}^{m-1}
 s^{e_j}\bigl(j+(m-j)s^k\bigr)\bigl(m-\tau_j+\tau_js\bigr).
\tag{1}
\]
Indeed, replacing the source's index \(j-1\) by \(j\) yields \(e_j=j-L(j-1)\) and \(\kappa(j-1)+1=m-\tau_j\); expanding the last two factors exactly reproduces its four sums. The source proves that \(Q_{m,n}\) is reciprocal of degree \(2k\) with positive leading and constant terms.

Write \(n=kq+r\), where \(q\ge0\), \(1\le r<k\), and \(\gcd(r,k)=1\); hence \(m=k(q+1)+r\). For each \(a\in\{0,\ldots,k-1\}\), the indices with \(e_j=a\) are the consecutive integers
\[
\left\lfloor\frac{am}{k}\right\rfloor+1
\le j\le \min\left(m-1,\left\lfloor\frac{(a+1)m}{k}\right\rfloor\right).
\tag{2}
\]
Because \(m=k(q+1)+r\), both endpoints are affine in \(q\). On each block the summands in (1) are quadratic polynomials in \(j\), with coefficients of degree at most two in \(q\). The elementary formulas for sums of \(1,j,j^2\) over affine endpoints therefore show that every coefficient of \(Q_{m,n}\), with \(k,r\) fixed, is a polynomial in \(q\) of degree at most three. **Thus four exact values \(q=0,1,2,3\) determine the formula for all integers \(q\ge0\).** No inference from a finite sample to an infinite set is used without this degree lemma.

Let \(T_j\) denote the Chebyshev polynomial of the first kind, and let \(c_0,\ldots,c_{2k}\) be the coefficients of \(Q_{m,n}\). Reciprocity gives, on \(s=e^{i\theta}\),
\[
F_{k,r,q}(x):=s^{-k}Q_{m,n}(s)
=c_k+2\sum_{j=1}^{k}c_{k-j}T_j(2x-1).
\tag{3}
\]
Thus \(F_{k,r,q}\) is a real polynomial of degree at most \(k\) in \(x\). Exact cubic interpolation using (1) at the four values of \(q\), for each of the \(84\) reduced-residue pairs \((k,r)\) under consideration, yields the identity
\[
F_{k,r,q}(x)=A_{k,r}(x)+qB_{k,r}(x)
 +\left((k+r)q^2+\frac{k}{3}q^3\right)H_k(2x-1),
\tag{4}
\]
where \(A_{k,r},B_{k,r}\) are explicitly recovered polynomials of degree at most \(k\) in the standalone checker and
\[
H_k(t)=(2+t)\left(k+2\sum_{j=1}^{k-1}(k-j)T_j(t)\right)
=(2+t)\left|\sum_{j=0}^{k-1}e^{ij\theta}\right|^2\ge0,
\quad t=\cos\theta\in[-1,1].
\tag{5}
\]
The two high-degree coefficient identities in (4) are exact polynomial identities, separately checked coefficient-by-coefficient for every \((k,r)\), not numerical approximations.

It remains to prove \(A_{k,r}(x)>0\) and \(B_{k,r}(x)>0\) simultaneously on \([0,1]\). On every dyadic subinterval of length \(2^{-L_k}\), represent each of these polynomials in the Bernstein basis of degree \(k\). Exact rational de Casteljau subdivision proves that **every Bernstein coefficient exceeds \(1/200\)**. The certified subdivision levels are:

| \(k\) | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(L_k\) | 4 | 6 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 9 | 9 |

Bernstein basis functions are nonnegative and sum to one on each subinterval. Hence \(A_{k,r}(x)>1/200\) and \(B_{k,r}(x)>1/200\) on the entire interval. As \(q\ge0\), combining (4) with the nonnegative Fejér factor (5) gives
\[
F_{k,r,q}(x)>\frac{1+q}{200}>0.
\]
This is the claimed unit-circle nonvanishing. Since the polynomial is reciprocal of degree \(2k\) and has no unit-circle roots, its \(2k\) nonzero roots pair under \(s\mapsto 1/s\), leaving exactly \(k\) strictly inside the unit circle, counted with multiplicity.

For any such interior root \(s\ne0\), the identity \(P_{m,n}(s,s)=s^{2n-1}Q_{m,n}(s)=0\) gives a zero of the holomorphic kernel factor at \((s,s)\in\mathbb H_{m/n}\) because \(|s|^{m/n}<|s|<1\). The kernel denominator is nonzero there. Factorizing the products \(s=z_1\overline{w}_1=z_2\overline{w}_2\) with suitable \(z,w\in\mathbb H_{m/n}\) then gives a genuine Bergman-kernel zero. This is also the equivalence established in Edholm–Mathew's Corollary 2.17 and Proposition 2.18.

## Verification
Run `python3 verify_hartogs_gaps_7_to_17.py` with Python 3 (standard library only). The checker constructs (1) with exact integers, computes (3) using exact Chebyshev recurrences, obtains \(A,B\) and the remaining cubic coefficients by rational finite differences, checks both identities in (4) against (5), and computes every degree-\(k\) Bernstein coefficient after the stated number of dyadic subdivisions. All comparisons are performed using exact fractions. It covers all \(84\) reduced-residue families and includes two non-interpolation consistency checks at \(q=4,13\); these are auxiliary checks, not the argument for all \(q\). The program was executed and all its assertions passed. Its relevant actual file is included in this package.

## Relationship to prior work
Edholm and Mathew provide the kernel numerator, palindromicity, and the implication from interior roots to kernel zeros. Their published Theorem 1.7 treats gaps one and two; their Section 4.3 mentions separate arguments for gaps three, four, and six and poses Conjecture 4.20 for all coprime pairs. Their statement that infinitely many pairs are accessible for each fixed gap does not assert coverage of **every** pair in any gap from seven through seventeen. Earlier elementary-Reinhardt kernel formulas address rational kernel representations without the present eleven-gap strict trigonometric positivity conclusion. The new content is the uniform verification for all parameters in each of eleven successive gaps, including the first gap with sixteen reduced residue classes.

## Limitations
The result does not resolve Conjecture 4.20 for gaps \(k\ge18\), does not address irrational exponents, and does not assert simplicity, exact locations, or counts of all off-diagonal Bergman-kernel zeros. It is a finite-gap theorem with an exact rational algebraic certificate, not a purely conceptual proof for arbitrary \(k\). Any independent mathematical assessment and search for unindexed equivalent results remain outstanding.

## References
1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489 (first public version 2025-05-26); *Mathematische Zeitschrift* **313**, article 43 (2026), DOI:10.1007/s00209-026-04059-8. Relevant: Theorem 1.3, Corollary 2.17, Proposition 2.18, equations (3.16) and (3.21), Sections 4.1–4.3, Conjecture 4.20.
2. D. Chakrabarti, A. Konkel, M. Mainkar, and E. Miller, *Bergman kernels of elementary Reinhardt domains*, *Pacific Journal of Mathematics* **306** (2020), 67–93, DOI:10.2140/pjm.2020.306.67.
