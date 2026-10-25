# A sharp four-row binomid test for eventually periodic second-order recurrences

## Finding

For an integer sequence \(f=(f_n)_{n\ge1}\) without zero entries, put
\[
 {n\brack k}_f=\frac{f_{n-k+1}\cdots f_n}{f_1\cdots f_k}
 \qquad(0\le k\le n),
\]
where empty products are \(1\). Call \(f\) *binomid* if these numbers are integers for every \(n,k\). Suppose \(f\) is eventually periodic **as a sequence of exact integers** and obeys some homogeneous second-order recurrence with integer coefficients for all \(n\ge1\):
\[
 f_{n+2}=P f_{n+1}-Q f_n,\qquad P,Q\in\mathbb Z.
\]
Then the following four properties are equivalent:

1. \(f\) is binomid.
2. Just \({2\brack1}_f=f_2/f_1\) and \({4\brack2}_f=f_3f_4/(f_1f_2)\) are integers.
3. \(f_m\mid f_n\) for every pair of positive integers \(m\mid n\).
4. \(f\) is binomid at every level (its complete generalized-binomial pyramid is integral).

More precisely, these properties hold exactly for the following six forms (an initial segment followed by \(^\infty\) denotes infinite repetition):
\[
\begin{array}{ll}
\mathrm I&(a,b)^\infty,\\
\mathrm {II}&(a,b,-a,-b)^\infty,\\
\mathrm {III}&(a,a,-2a)^\infty,\\
\mathrm {IV}&(a,-a,-2a,-a,a,2a)^\infty,\\
\mathrm V&(a,b,b,b,\ldots),\\
\mathrm {VI}&(a,b,-b,b,-b,\ldots).
\end{array}
\]
Here \(a,b\) are nonzero integers, and \(a\mid b\) is required in families I, II, V and VI. The expressions can overlap; this is a union classification, not a claim of disjointness.

Every periodic sequence in this list also satisfies the *strong* divisibility identity
\[
 \gcd(|f_m|,|f_n|)=|f_{\gcd(m,n)}|.
\]
The four-row cutoff is sharp: the period-three sequence \((1,2,-3)^\infty\), obeying \(f_{n+2}=-f_{n+1}-f_n\), has integral generalized-binomial rows through \(n=3\) but \({4\brack2}_f=-3/2\). Neither of the two tested entries can be omitted: \((2,3)^\infty\) has \({4\brack2}_f=1\) but \({2\brack1}_f=3/2\).

## Assumptions and scope

Indices start at \(n=1\); eventual periodicity means there are positive integers \(N,L\) for which \(f_{n+L}=f_n\) as integers for all \(n\ge N\), not merely modulo a modulus. Zeros are excluded so every generalized binomial coefficient is defined. Negative terms are allowed. The recurrence coefficients need not be primitive and \(Q=0\) is allowed. No hypothesis about \(f_0\) is made. Divisibility is signed integer divisibility, and the displayed GCD uses nonnegative absolute values. The first public motivating manuscript appeared on 2023-02-04 [1].

## Proof

**1. Exhaust all possible exact eventual-periodic shapes.** Let \(E\) be the forward shift on rational sequences, \((Ef)_n=f_{n+1}\). The recurrence gives \((E^2-PE+Q)f=0\); eventual periodicity gives \(E^N(E^L-1)f=0\). Hence the monic minimal annihilating polynomial of \(f\) over \(\mathbb Q\) divides both polynomials and has degree at most two. Since \(E^L-1\) is squarefree in characteristic zero, its nonzero-root factors cannot repeat. Since the minimal polynomial has rational coefficients, the only possible cyclotomic irreducible factors of degree at most two are \(E-1\), \(E+1\), \(E^2+1\), \(E^2+E+1\), and \(E^2-E+1\). The two linear factors can occur together as \(E^2-1\). The only possibility containing a zero root, compatible with every \(f_n\ne0\), is \(E(E-1)\) or \(E(E+1)\); an annihilator \(E\) or \(E^2\) would force zero terms.

Writing \(a=f_1\), \(b=f_2\), we therefore obtain precisely the six unconstrained shapes
\[
 (a,b)^\infty,\quad (a,b,-a,-b)^\infty,\quad
 (a,b,-a-b)^\infty,\quad
 (a,b,b-a,-a,-b,a-b)^\infty,
\]
\[
 (a,b,b,b,\ldots),\quad (a,b,-b,b,-b,\ldots).
\]
Linear minimal-polynomial cases are already included. The cyclotomic factors listed above are exhaustive because \(\varphi(d)\le2\) precisely for \(d=1,2,3,4,6\).

**2. Apply the two finite tests.** Since \({2\brack1}_f=b/a\), the first test means \(a\mid b\). For the first two periodic shapes, \({4\brack2}_f=1\). For the last two transient shapes it is respectively \(b/a\) and \(-b/a\). For the period-three and period-six shapes it is respectively \(-(a+b)/b\) and \(-(b-a)/b\). Thus, in either of these two cases, once \(a\mid b\), the second test requires \(b\mid a\). Consequently \(b=\pm a\). For the period-three shape \(b=-a\) would make \(f_3=0\), and for the period-six shape \(b=a\) would make \(f_3=0\); both are forbidden. The remaining choices give exactly families III and IV. This proves that property 2 forces exactly the six stated families. Necessity of the tests from property 1 is immediate.

**3. Infinite divisibility and strong divisibility.** In families I and II, \(|f_n|=|a|\) for odd \(n\) and \(|f_n|=|b|\) for even \(n\). Write \(|b|=|a|t\) with \(t\in\mathbb Z_{\ge1}\). For any positive \(m,n\), both are even precisely when \(\gcd(m,n)\) is even; hence \(\gcd(|f_m|,|f_n|)=|f_{\gcd(m,n)}|\). In families III and IV, \(|f_n|=|a|2^{\mathbf1_{3\mid n}}\), and the same argument with divisibility by three proves the strong GCD identity. In families V and VI the absolute values are the divisor-chain \((|a|,|b|,|b|,\ldots)\), with \(|a|\mid|b|\). Thus all six families are divisibility sequences. Moreover, the periodic four are GCD sequences, and the transient two are divisor-chains (also with signs).

The established results that every GCD sequence is a divisor-product and that GCD and divisor-chain sequences are binomid at every level [1, Sections 2--4] apply to their absolute-value sequences. Replacing any entries by their negatives changes any generalized-binomial coefficient, and every iterated one, only by a sign. Thus all six families are binomid at every level. This proves property 2 implies properties 3 and 4; property 4 implies property 1.

Finally, property 3 forces \(f_1=a\mid f_2=b\) and \(f_2=b\mid f_4\) since \(2\mid4\). On the six unconstrained shapes, those two divisibilities imply exactly the restrictions derived in Step 2: in particular \(f_4=\pm a\) for period three and six, while \(f_4=\pm b\) in all other shapes. Thus property 3 also implies property 2, completing the equivalence.

**4. Sharpness.** For \(f=(1,2,-3)^\infty\), the only nontrivial coefficients through row three are \(2,-3,-3\), all integers; nevertheless \({4\brack2}_f=-3/2\). For \(g=(2,3)^\infty\), \({4\brack2}_g=1\) but \({2\brack1}_g=3/2\). Therefore both indicated tests are essential and row four is the earliest row at which universal recognition can be achieved.

## Verification

The self-contained Python 3 program `check.py` enumerates 984 nonzero parameter instances from all six unconstrained shapes and tests equivalence of the two-entry criterion with all generalized-binomial coefficients through row 24. It separately checks all six accepted families through row 30 for several positive and negative scales, verifies strong divisibility for the periodic families, and checks the two sharpness witnesses. The computation passed, but the infinite assertions are established by the proof above, not by finite enumeration. Run with `python3 check.py`; only Python's standard library is used.

## Relationship to prior work

Shapiro [1, Open Questions 29(1)] asks whether second-order binomid recurrence sequences must be divisible. His paper proves that second-order Lucas sequences initialized at zero are binomid at every level, and that GCD and divisor-chain sequences have this stronger property, but it does not provide the two-entry criterion for exactly eventually periodic second-order recurrences. Horák and Skula [2] classify second-order **strong divisibility** sequences; several sequences in the list above overlap their known cases, but a classification assuming strong divisibility does not establish that the much weaker two binomid integrality tests force it in the periodic subclass, nor cover the weakly divisible transient families with \(|b|>|a|\). The new assertion is the exact finite recognition equivalence on the entire eventually periodic subclass, including sharpness, not a claim that the underlying strong-divisibility examples were unknown.

## Limitations

The result makes no assertion about non-eventually-periodic recurrence sequences, which remain central to Shapiro's question. It is a classification of a natural bounded/dynamical subclass, not a solution of the unrestricted second-order binomid problem. The application of [1] to higher binomid-pyramid levels is a cited mathematical theorem rather than a standalone reproof here. Possible earlier implicit formulations of the finite test remain a literature-priority risk.

## References

[1] D. B. Shapiro, *Divisibility Properties for Integer Sequences*, Integers **23** (2023), A57; first public arXiv submission 4 February 2023, arXiv:2302.02243, https://arxiv.org/abs/2302.02243 ; journal PDF https://math.colgate.edu/~integers/x57/x57.pdf . In particular Definition 1, Lemma 5, Theorems 15 and 20, and Open Questions 29.

[2] P. Horák and L. Skula, *A Characterization of the Second-Order Strong Divisibility Sequences*, Fibonacci Quarterly **23** (1985), 126–132, https://www.fq.math.ca/Scanned/23-2/horak.pdf ; especially Section 4, Theorem 4.1 and Corollary 4.2.

[3] A. Bauval, *Suites récurrentes linéaires d'ordre 2 à divisibilité forte*, arXiv:1606.01594 (2016), https://arxiv.org/abs/1606.01594 (related strong-divisibility classification; abstract consulted).
