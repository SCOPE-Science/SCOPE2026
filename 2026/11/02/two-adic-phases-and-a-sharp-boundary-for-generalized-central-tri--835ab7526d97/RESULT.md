# Two-adic phases and a sharp boundary for generalized central trinomial coefficients

## Finding

For nonzero integers \(b,c\), define the generalized central trinomial coefficient
\[
T_n(b,c)=[X^n](X^2+bX+c)^n
=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n}{2k}\binom{2k}{k}b^{n-2k}c^k.
\]
Let \(B=\nu_2(b)\), \(C=\nu_2(c)\), and write \(n=2m+e\) with \(m\geq0\) and \(e\in\{0,1\}\). Write \(s_2(m)\) for the number of ones in the binary expansion of \(m\).

**Noncritical phase theorem.** For every nonnegative integer \(n\):
\[
\nu_2(T_n(b,c))=
\begin{cases}
nB,&C\geq 2B,\\
mC+eB+s_2(m),&C\leq2B-2.
\end{cases}
\]
In the second phase put
\[
D_{2m+e}(b,c)=(2m+1)^e\binom{2m}{m}b^e c^m.
\]
The quotient \(T_{2m+e}(b,c)/D_{2m+e}(b,c)\) is a two-adic unit, and it obeys the sharper congruence
\[
\frac{T_{2m+e}(b,c)}{D_{2m+e}(b,c)}
\equiv 1+\frac{m^2b^2}{2c}\pmod4\quad\text{in }\mathbb Z_2.
\]
The rational correction on the right lies in \(\mathbb Z_2\), since \(2B-C\geq2\).

**Sharp intervening boundary.** The only remaining valuation relation is \(C=2B-1\), necessarily \(B\geq1\). For every \(B\geq1\) and every \(r\geq1\), there are nonzero integers \(b,c\) with \(\nu_2(b)=B\), \(\nu_2(c)=2B-1\), and \(\nu_2(T_2(b,c))=2B+r\). There are also such coefficients with \(T_2(b,c)=0\). Thus no valuation formula depending only on \((n,B,C)\) can cover that boundary.

**Primitive-coefficient census.** If \(\gcd(b,c)=1\) and \(b,c\neq0\), then an odd \(b\) makes every \(T_n(b,c)\) odd. If \(b\) is even (and therefore \(c\) is odd), the valuation is \(s_2(m)+eB\) at \(n=2m+e\). Consequently, for every \(r\geq1\), every integer \(j\), and even \(b\) coprime to \(c\),
\[
\#\{0\leq n<2^r:\nu_2(T_n(b,c))=j\}
=\binom{r-1}{j}+\binom{r-1}{j-B},
\]
with an out-of-range binomial coefficient interpreted as zero.

## Assumptions and scope

The parameters \(b,c\) are nonzero integers; the index \(n\) is any nonnegative integer. The valuation is normalized by \(\nu_2(2)=1\), and \(\nu_2(0)=+\infty\). The first two cases cover all parameter valuations except the stated critical boundary. The mod-four quotient is interpreted in the two-adic integers, including inverses of odd denominators; this is not a claim of ordinary integer divisibility by the displayed normalization.

## Proof

**Phase \(C\geq2B\).** Divide the binomial sum by \(b^n\). Then \(c/b^2\in\mathbb Z_2\), giving
\[
\frac{T_n(b,c)}{b^n}=1+\sum_{k=1}^{\lfloor n/2\rfloor}
\binom n{2k}\binom{2k}k\left(\frac c{b^2}\right)^k.
\]
For every \(k\geq1\), the central binomial coefficient \(\binom{2k}{k}\) is even. Therefore the displayed quotient is congruent to one modulo two. It is a two-adic unit, so \(\nu_2(T_n)=nB\). This argument includes \(n=0\).

**Phase \(C\leq2B-2\).** Write \(n=2m+e\), change the summation index from \(k\) to \(j=m-k\), and divide by the nonzero baseline \(D_{2m+e}\). Direct factorial cancellation yields the exact rational identity
\[
\frac{T_{2m+e}(b,c)}{D_{2m+e}(b,c)}
=\sum_{j=0}^{m}
\frac{\bigl(m(m-1)\cdots(m-j+1)\bigr)^2}{(2j+e)!}
\left(\frac{b^2}{c}\right)^j,
\]
where the empty product for \(j=0\) is one. Put \(\delta=2B-C\geq2\). Legendre's factorial formula gives, for each \(j\geq1\) and either \(e=0\) or \(e=1\),
\[
\nu_2((2j+e)!)=2j-s_2(j).
\]
The \(j\)-th summand of the normalized expansion therefore has valuation at least
\[
j\delta-(2j-s_2(j))=j(\delta-2)+s_2(j)\geq1.
\]
Thus the normalized sum is one modulo two. Meanwhile
\[
\nu_2(D_{2m+e})=eB+mC+\nu_2\binom{2m}{m}
=eB+mC+s_2(m),
\]
where the last equality follows from Legendre's formula. This proves the valuation identity.

To sharpen the unit congruence modulo four, observe that when \(j\geq2\) the falling factorial \(m(m-1)\cdots(m-j+1)\) is even, so that term's valuation is at least \(2+s_2(j)\geq3\). The sole possible correction modulo four comes from \(j=1\), namely \(m^2b^2/(2c)\) for \(e=0\) or \(m^2b^2/(6c)\) for \(e=1\). Their difference, \(m^2b^2/(3c)\), belongs to \(4\mathbb Z_2\), since \(\nu_2(b^2/c)=\delta\geq2\). This proves the stated mod-four formula.

**Critical line.** Take arbitrary \(B\geq1\), any odd \(u,v\), and set \(b=2^B u\), \(c=2^{2B-1}v\). Then
\[
T_2(b,c)=b^2+2c=2^{2B}(u^2+v).
\]
For \(u=3\), choosing \(v=2^r-9\), which is odd for \(r\geq1\), gives the finite valuation \(2B+r\). Choosing \(v=-9\) gives a zero term. Both choices have the same specified coefficient valuations. The valuation-only classification is therefore impossible on this boundary.

**Census.** Coprimality forces either \(B=0\) or \(B\geq1,C=0\); the two phases above then give the claimed formulas. As \(n\) runs over \([0,2^r)\), each \(m\in[0,2^{r-1})\) occurs exactly once for each \(e=0,1\). Exactly \(\binom{r-1}{k}\) such \(m\) have \(s_2(m)=k\). Summing the two parity contributions proves the histogram identity.

## Verification

Run `python3 verify.py` with Python 3 and its standard library. The checker independently generates coefficients from the algebraic generating-function recurrence, compares selected coefficients with direct multinomial sums, checks the proposed valuations and the mod-four two-adic-unit formula, verifies critical-boundary witnesses, and tests dyadic valuation histograms. A completed run reported:

```
VERIFY_OK coefficient_pairs= 1944 valuation_indices= 157464 unit_mod4_checks= 59292 direct_multinomial_checks= 3920 critical_witnesses= 72 dyadic_histograms= 60
```

The unrestricted claims are proved by the preceding identities; finite checks cannot establish them independently.

## Relationship to prior work

Noe (2006), particularly Section 8 and Theorem 8.1, defines the same generalized coefficients and proves their parity law; his Theorem 8.5 treats prime divisibility. These results are stronger as to general prime-divisibility coverage, but do not provide the coefficient-dependent exact two-adic valuation, normalized mod-four correction, or sharp intervening boundary stated here. Sun (2010), Section 1 and its displayed specialization \(T_n(2,1)=\binom{2n}{n}\), already covers the central-binomial special case; it is not claimed as new. His main theorems treat different congruence sums and odd-prime phenomena. Wang and Sun (2019), especially Theorems 1.1 and 1.2, similarly establish weighted sums modulo squares of odd primes, not per-index two-adic valuations for arbitrary coefficients. Alekseyev, Amdeberhan, Shallit and Vukusic (2025), Theorem 3, establish exact valuations of Legendre polynomials \(P_n(r)\) for rational \(r\) divisible by the chosen prime in the valuation sense. Through \(T_n(b,c)=d^{n/2}P_n(b/\sqrt d)\), \(d=b^2-4c\), their result implies the valuation part of the second phase for those parameters having nonzero rational-square \(d\) and \(\nu_2(b/\sqrt d)\geq1\). This genuine prior-covered subclass is excluded from the individual novelty claim; their stated theorem does not cover arbitrary nonsquare discriminants, the entire borderline regime, or the normalized mod-four correction. The standard central-binomial identity \(\nu_2\binom{2m}{m}=s_2(m)\) also predates this statement. The contribution claimed here is the joint noncritical coefficient-valuation phase diagram, its first unit correction, the critical-boundary counterfamily, and the resulting primitive-coefficient census, not those component identities.

## Limitations

No complete formula is asserted on the critical line \(C=2B-1\); the degree-two witnesses prove only that valuation data alone cannot determine its behavior. Coefficients \(b=0\) or \(c=0\) are excluded from the theorem, although directly calculable. No odd-prime analogue is supplied. The literature comparison is necessarily nonexhaustive; an earlier equivalent specialization or broader two-adic result may exist. No independent mathematical audit has been performed.

## References

1. Tony D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, Journal of Integer Sequences **9** (2006), Article 06.2.7, especially Sections 1, 2, 8 and Table 1. https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.pdf
2. Zhi-Wei Sun, *Congruences Involving Generalized Central Trinomial Coefficients*, arXiv:1008.3887 (first public version 2010-08-23), especially Section 1, definitions and specialization, and Sections 2–5. https://arxiv.org/abs/1008.3887
3. Chen Wang and Zhi-Wei Sun, *Some Parametric Congruences Involving Generalized Central Trinomial Coefficients*, arXiv:1910.06850 (first public version 2019-10-15), particularly Theorems 1.1 and 1.2. https://arxiv.org/abs/1910.06850
4. Max A. Alekseyev, Tewodros Amdeberhan, Jeffrey Shallit and Ingrid Vukusic, *On the p-adic valuations of values of Legendre polynomials*, arXiv:2505.08935 (2025), particularly Theorem 3. https://www.math.tulane.edu/~tamdeberhan/Legendre_polynomials.pdf
5. Kummer's theorem and Legendre's factorial valuation formula, standard classical identities, cited for the binary digit valuation of central binomial coefficients.
