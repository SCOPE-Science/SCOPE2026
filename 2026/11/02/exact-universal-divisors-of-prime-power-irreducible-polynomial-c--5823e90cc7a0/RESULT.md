# Exact universal divisors of prime-power irreducible-polynomial counts and Fermat-prime detection

## Finding
Let \(p\) be any prime and \(a\ge1\). Put \(n=p^a\), \(t=p^{a-1}\), and \(k=t(p-1)\). Let \(I_n(q)\) count monic irreducible polynomials of degree \(n\) over \(\mathbb F_q\), for prime powers \(q\), and define the **universal field-size divisor**
\[G_{p,a}=\gcd_{q\text{ a prime power}}I_n(q).\]
For each rational prime \(\ell\), set
\[h_\ell(k)=\begin{cases}
1,&\ell=2,\ k\text{ odd},\\
\nu_2(k)+2,&\ell=2,\ k\text{ even},\\
1+\nu_\ell(k),&\ell\text{ odd and }\ell-1\mid k,\\
0,&\ell\text{ odd and }\ell-1\nmid k.
\end{cases}\]
Then the complete prime factorization is determined by
\[\boxed{\nu_\ell(G_{p,a})=\min\{t,h_\ell(k)\}-a\mathbf1_{\ell=p}.}\]
The exponents are nonnegative, and no prime \(\ell>k+1\) occurs.

For degrees that are powers of two, the formula becomes \(G_{2,1}=1\), \(G_{2,2}=3\), and for each \(a\ge3\),
\[\boxed{G_{2,a}=2\prod_{\substack{j\ge0,\ 2^j\le a-1\\F_j=2^{2^j}+1\text{ prime}}}F_j.}\]
Thus a new odd prime factor appears exactly when the corresponding Fermat number is prime, and this sequence eventually stabilizes if and only if there are finitely many Fermat primes. This is an equivalence, not a resolution of the Fermat-prime question.

## Assumptions and scope
The degree is a positive prime power, while the finite-field cardinality ranges over **all** prime powers, including primes. The gcd is a positive integer and agrees with the fixed divisor over integer inputs of the prime-power necklace polynomial. The symbols \(\nu_\ell\) and \(\mathbf1_{\ell=p}\) mean the prime-adic valuation and the indicator of equality, respectively. Only ordinary finite fields are counted; no assertion concerns monic irreducibles with prescribed coefficients.

## Proof
**1. Exact counting reduction.** The classical Möbius-inversion formula for monic irreducibles (Bodin, Section 2, reflecting the classical formula) reads
\[I_n(q)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.\]
For \(n=p^a\) this is
\[p^aI_n(q)=q^{p^a}-q^{p^{a-1}}=q^t(q^k-1).\]
In particular \(I_n(q)\) is an integer. For each rational prime \(\ell\) it therefore suffices to determine the minimum \(\ell\)-valuation of the numerator among permitted \(q\), then subtract \(a\mathbf1_{\ell=p}\).

**2. Inputs divisible by \(\ell\).** If \(\ell\mid q\), then \(q^k-1\) is an \(\ell\)-adic unit, so
\[\nu_\ell(q^t(q^k-1))=t\nu_\ell(q)\ge t.\]
The permitted field size \(q=\ell\) attains equality.

**3. Unit inputs at odd \(\ell\).** If \(\ell-1\nmid k\), choose a generator of \(\mathbb F_\ell^\times\) whose \(k\)-th power is not \(1\). By Dirichlet's theorem, there is a rational prime \(q\) in that nonzero residue class; then \(\nu_\ell(q^k-1)=0\).
If \(\ell-1\mid k\), write \(k=(\ell-1)s\). Every unit \(q\) satisfies \(q^{\ell-1}\equiv1\pmod\ell\). The lifting-the-exponent identity gives
\[\nu_\ell(q^k-1)=\nu_\ell(q^{\ell-1}-1)+\nu_\ell(s)\ge1+\nu_\ell(k).\]
A primitive root \(g\) modulo \(\ell^2\) has \(\nu_\ell(g^{\ell-1}-1)=1\); Dirichlet's theorem supplies a prime field size \(q\equiv g\pmod{\ell^2}\). This attains the lower bound. Hence the minimum over unit prime-power field sizes equals the odd-prime branch of \(h_\ell(k)\).

**4. Unit inputs at \(\ell=2\).** If \(k\) is odd, taking a prime \(q\equiv3\pmod4\) gives \(\nu_2(q^k-1)=1\), the smallest possible value for odd \(q\). If \(k\) is even, the standard two-adic lifting formula yields
\[\nu_2(q^k-1)=\nu_2(q-1)+\nu_2(q+1)+\nu_2(k)-1\ge\nu_2(k)+2.\]
Taking a prime \(q\equiv3\pmod8\) makes \(\nu_2(q-1)=1\), \(\nu_2(q+1)=2\), so the lower bound is sharp. Consequently the unit-input minimum is exactly \(h_2(k)\).

**5. Global minimum and integrality.** Combining the divisible and unit cases gives
\[\min_{q\text{ prime power}}\nu_\ell(q^t(q^k-1))=\min\{t,h_\ell(k)\}.\]
Subtracting \(\nu_\ell(p^a)=a\mathbf1_{\ell=p}\) proves the formula. The exponents cannot be negative since the necklace count is always an integer; directly, \(t\ge a\), and for \(\ell=p\), the relevant unit branch is at least \(a\). If \(\ell>k+1\), the odd-prime residue group has order \(\ell-1>k\), so \(h_\ell(k)=0\); thus the displayed finite support is exact.

**6. Fermat-prime corollary.** Put \(p=2\), so \(t=k=2^{a-1}\). For \(a=1\) the exponent at \(2\) is \(0\); for \(a=2\) it is again \(0\); and for \(a\ge3\) it is \(1\). For an odd prime \(\ell\), the exponent is \(1\) exactly when \(\ell-1\mid2^{a-1}\). This says \(\ell=2^b+1\) is prime with \(1\le b\le a-1\). Primality forces \(b=2^j\): if \(b=2^ju\) with odd \(u>1\), then \(2^b+1\) has the proper factor \(2^{2^j}+1\). Hence precisely the Fermat primes contribute, proving the product formula and the eventual-stabilization equivalence.

## Verification
The accompanying \(\texttt{verify.py}\) independently generates prime powers up to \(70\) and computes the classical irreducible-polynomial counts by exact integer arithmetic. It compares their gcd with the formula for \(17\) prime/exponent pairs. This is finite corroboration; the universal proof uses unit-group structure, lifting-the-exponent, and Dirichlet's theorem, not extrapolation.

## Relationship to prior work
Bodin's 2009 article supplies the classical Möbius formula for \(I_n(q)\) and then studies several-variable counts; that formula alone does not state a gcd over variable field sizes. The general fixed-divisor theories of Peruginelli and the cited survey establish abstract valuation/finite-sampling mechanisms applicable to integer-valued polynomials; they do not give this explicit prime-power necklace formula or Fermat-prime detection in the material inspected. Hyde studies cyclotomic factors of necklace polynomials, a different factorization invariant; complete text of that relevant article was not accessible during this comparison. The result is therefore a special-family explicit classification with a genuine residual risk of earlier equivalent treatment.

## Limitations
No claim is made for arbitrary composite degrees, for all integer-valued counting sequences, or for the existence of infinitely many Fermat primes. General fixed-divisor frameworks may yield algorithms to evaluate individual cases; novelty here rests on the uniform closed prime-valuation formula and its Fermat-prime consequence. Equivalence to a result in unlocated specialist literature cannot be excluded. An independent audit has not been performed.

## References
- A. Bodin, *Generating series for irreducible polynomials over finite fields*, arXiv:0910.1680, first submitted 2009-10-09, especially Section 2 and the classical Möbius formula, https://arxiv.org/pdf/0910.1680.
- G. Peruginelli, *Primary decomposition of the ideal of polynomials whose fixed divisor is divisible by a prime power*, Journal of Algebra 398 (2014), pp. 456–467, https://pmc.ncbi.nlm.nih.gov/articles/PMC4986407/.
- D. Prasad, K. Rajkumar and A. Satyanarayana Reddy, *A Survey on Fixed Divisors*, arXiv:1709.08026, https://arxiv.org/pdf/1709.08026.
- T. Hyde, *Cyclotomic factors of necklace polynomials*, arXiv:1811.08601, https://arxiv.org/abs/1811.08601 (plausible related source; full text not inspected).
- Standard results used: Dirichlet's theorem on primes in arithmetic progressions, primitive roots modulo odd prime powers, and the lifting-the-exponent identities.
