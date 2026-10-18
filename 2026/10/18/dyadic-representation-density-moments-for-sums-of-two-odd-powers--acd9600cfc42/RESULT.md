# Dyadic representation-density moments for sums of two odd powers

## Finding

For every **odd integer** \(k\ge3\), every \(n\ge1\), and every residue \(r\in\mathbb Z/2^n\mathbb Z\), put
\[
R_{k,n}(r)=\#\{(x,y)\in(\mathbb Z/2^n\mathbb Z)^2:x^k+y^k\equiv r\pmod{2^n}\}.
\]
The following formulas determine **every** representation count. For odd \(r\),
\[R_{k,n}(r)=2^n.\]
For even \(r\) and \(1\le n\le k\),
\[
R_{k,n}(r)=2^{n-1}+\mathbf 1_{r=0}\,2^{2n-2}.
\]
For even \(r\) and \(n>k\),
\[
R_{k,n}(r)=2^{n-1}+\mathbf 1_{2^k\mid r}\,2^{2k-2} R_{k,n-k}(r/2^k).
\]
In the last term, when \(2^k\mid r\), the quotient is taken modulo \(2^{n-k}\). Thus all \(2^n\) residue classes are representable, but their representation multiplicities are not uniform.

Let \(\mathbb Z_2\) carry normalized Haar measure \(\mu\). For \(a\in\mathbb Z_2\setminus\{0\}\), the stabilized local representation density
\[
\rho_k(a)=\lim_{n\to\infty}2^{-n}R_{k,n}(a\bmod 2^n)
\]
exists. Write \(v_2(a)=jk+s\), where \(j\ge0\) and \(0\le s<k\), and put \(B=2^{k-2}\). Then
\[
\rho_k(a)=
\begin{cases}
\dfrac12\displaystyle\sum_{i=0}^{j-1}B^i+B^j,&s=0,\[5pt]
\dfrac12\displaystyle\sum_{i=0}^{j}B^i,&1\le s<k.
\end{cases}
\]
The first sum is empty when \(j=0\). At \(a=0\), the normalized finite-level counts diverge to \(+\infty\). Therefore the density formula defines a finite measurable function almost everywhere.

For **every real** \(q>0\), its exact integrability criterion is
\[
\boxed{\int_{\mathbb Z_2}\rho_k(a)^q\,d\mu(a)<\infty
\quad\Longleftrightarrow\quad q<\frac{k}{k-2}.}
\]
More precisely, the upper tail has power-law order
\[
\mu\{a:\rho_k(a)>t\}=\Theta_k\bigl(t^{-k/(k-2)}\bigr)
\qquad(t\to\infty).
\]
The mean density is one for every odd \(k\ge3\). In the cubic case,
\[
\boxed{\int\rho_3^2\,d\mu=\frac74,
\qquad\operatorname{Var}(\rho_3)=\frac34.}
\]
For every odd \(k\ge5\), the second moment and variance are infinite. Thus the family has a sharp variance transition between cubes and fifth powers, despite full residue representability in every case.

## Assumptions and scope

Counts include **ordered** pairs with both coordinates arbitrary residues, including zero. The exponent \(k\) is any fixed odd integer at least three; it need not be prime. In the recurrence, a divisibility condition on \(r\) is well defined because \(n>k\). The local density uses the normalization \(2^{-n}R_{k,n}\), corresponding to the push-forward of product Haar measure on \(\mathbb Z_2^2\). The limit at nonzero \(a\) is pointwise, and moment integration is over the target variable \(a\) with normalized Haar measure. No claim of convergence in every \(L^q\), nor of a density finite at \(a=0\), is made.

## Proof

**1. Unit permutation and parity split.** The finite unit group \((\mathbb Z/2^n\mathbb Z)^\times\) has order \(2^{n-1}\). Since \(k\) is odd, exponentiation by \(k\) is a bijection on this group. If \(r\) is odd, exactly one coordinate is odd. Choose the even coordinate in \(2^{n-1}\) ways; its complement \(r-y^k\) is odd and has exactly one \(k\)th root. Either coordinate can be the odd one, giving \(2^n\) ordered representations. If \(r\) is even, both variables are odd or both are even. In the odd-odd case each of the \(2^{n-1}\) choices of odd \(x\) uniquely determines odd \(y\), contributing \(2^{n-1}\) uniformly.

**2. Exact even-even reduction.** If \(1\le n\le k\), both even powers vanish modulo \(2^n\), producing \(2^{2n-2}\) pairs at \(r=0\) and none elsewhere. If \(n>k\), write \(x=2u\), \(y=2v\). Such a pair can contribute only if \(2^k\mid r\). For such \(r\), the necessary and sufficient condition is \(u^k+v^k\equiv r/2^k\pmod{2^{n-k}}\). The variables \(u,v\) originally range modulo \(2^{n-1}\), so each ordered solution modulo \(2^{n-k}\) has exactly \(2^{2(k-1)}\) lifts. Adding the odd-odd term proves the complete finite-level recurrence.

**3. Stabilized pointwise density.** Dividing the even-residue recurrence by \(2^n\) gives the transformation
\[
2^{-n}R_{k,n}(r)=\frac12+2^{k-2}\,2^{-(n-k)}R_{k,n-k}(r/2^k)
\]
when \(2^k\mid r\). For a nonzero \(a\in\mathbb Z_2\), repeated division by \(2^k\) reaches either an odd value (whose normalized count equals one) or an even value not divisible by \(2^k\) (whose normalized count equals one half). Once \(n>v_2(a)+k\), all relevant finite-level conditions have stabilized. Iteration yields the claimed geometric sums. For \(a=0\), the same recurrence repeats with multiplier \(2^{k-2}>1\), hence the normalized counts tend to infinity.

**4. Complete moment threshold.** The set of nonzero \(2\)-adic integers of valuation \(v\ge0\) has Haar measure \(2^{-v-1}\). Uniformly over \(v=jk+s\), \(0\le s<k\), the explicit density has constants depending only on \(k\) bounding it above and below by positive multiples of \(B^j\), where \(B=2^{k-2}\). Consequently, for every real \(q>0\),
\[
\int\rho_k^q\,d\mu<\infty
\Longleftrightarrow
\sum_{j\ge0}2^{-kj} B^{qj}<\infty
\Longleftrightarrow 2^{-k+q(k-2)}<1.
\]
At equality the geometric summands remain bounded away from zero, so the borderline diverges. The same valuation inequalities give the asserted \(\Theta_k\) tail order.

**5. Mean and cubic variance.** Since \(k-2<k\), the first moment is finite. Let \(m_1=\int\rho_k\,d\mu\). Haar measure splits into odd arguments (mass \(1/2\)), even arguments not divisible by \(2^k\) (mass \(1/2-2^{-k}\)), and arguments divisible by \(2^k\) (mass \(2^{-k}\)). The values on the first two sets are one and one half. On the third they obey \(\rho_k(a)=1/2+B\rho_k(a/2^k)\). Haar invariance after conditional division gives
\[
m_1=\frac34+\frac14m_1,
\qquad\text{hence }m_1=1.
\]
For \(k=3\), the second moment \(m_2\) is finite by step 4. Expanding the square on those same three sets gives
\[
m_2=\frac78+2^{k-4}m_2.
\]
Setting \(k=3\) yields \(m_2=7/4\), hence the variance \(7/4-1=3/4\). For every odd \(k\ge5\), step 4 gives \(2\ge k/(k-2)\), so \(m_2=+\infty\). This proves all assertions.

## Verification

The standalone program `verify.py`, executable with `python3 verify.py` and using only the Python standard library, independently enumerates ordered pairs and residue counts modulo \(2^n\) for odd exponents \(k\in\{3,5,7,9\}\) and every \(1\le n\le9\). It compares all counts to the symbolic recurrence, checks odd-unit permutation, and tests normalized density stabilization against the closed form at \(180\) additional parameter pairs. The program also performs exact rational arithmetic for the cubic moment and variance. Its checked totals are \(36\) exponent/modulus settings, \(4088\) residue counts, \(1{,}398{,}096\) ordered input pairs, and \(180\) stabilization comparisons; all passed. This finite computation checks the formulas on those ranges; the infinite claims follow from the proof above, not exhaustive computation.

## Relationship to prior work

Arias, Borja and Anaya (2023, *Journal of Integer Sequences*, Article 23.8.1, primary MSC2020 \(11\mathrm{A}07\)) study the number of residue **classes with at least one representation** by diagonal sums of powers, including two-variable power sums; their Theorem 18 and Section 4 treat prime-power moduli. That image-cardinality statistic does not determine the fiber multiplicities \(R_{k,n}(r)\), their limiting distribution, or their moments. Broughan (2003/2004, *Journal of Integer Sequences*, Article 03.4.6) treats cube representability, modular obstructions and global integer representations, likewise without this dyadic fiber-density moment law. General finite-field estimates for the number of points on diagonal equations concern other rings or coarse estimates rather than this explicit characteristic-two valuation distribution.

The primary incremental contribution is a complete quantitative refinement of residue representability: the exact finite-ring fiber counts and the sharp integrability/variance transition. The bijection of odd power maps on the unit group is elementary and is not claimed as new. Related general results on local zeta functions and polynomial push-forward measures could potentially encompass qualitative aspects; no such source was established to imply these exact statements in the inspected literature.

## Limitations

The result is restricted to two summands, coefficient one, odd exponent \(k\ge3\), and powers of the prime two. It does not address even exponents, odd prime powers, or unrestricted global sums of like powers. The moment theorem describes limiting local representation densities, not the number of integral solutions to a fixed global Diophantine equation. No independent external mathematical validation has been performed, and unindexed overlap remains possible.

## References

1. F. Arias, J. Borja and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1, published August 28, 2023. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
2. K. A. Broughan, *Characterizing the Sum of Two Cubes*, Journal of Integer Sequences **6** (2003), Article 03.4.6. https://cs.uwaterloo.ca/journals/JIS/VOL6/Broughan/broughan25.pdf
