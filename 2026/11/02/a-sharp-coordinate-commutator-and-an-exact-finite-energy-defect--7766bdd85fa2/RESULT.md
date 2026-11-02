# A sharp coordinate commutator and an exact finite-energy defect for the Fock bisector cone

## Finding

Let \(\mathcal F^2(\mathbb C^2)\) denote the entire-function subspace of Gaussian \(L^2\) with measure \(\pi^{-2}e^{-|z_1|^2-|z_2|^2}\,dA(z_1)dA(z_2)\). Let \(P\) be its orthogonal projection and let \(T=P\mathbf1_E|_{\mathcal F^2}\), where
\[
E=\{(z_1,z_2)\in\mathbb C^2:|z_1|>|z_2|\}.
\]
Define \(M_1 f=z_1f\) with its natural closed multiplication domain, and \(C=[M_1,T]=M_1T-TM_1\) on that domain. Then \(C\) extends uniquely to a bounded, noncompact operator and
\[
\boxed{\|C\|=\|C\|_{\mathrm{ess}}=\frac1{2\sqrt\pi}.}
\]
The operator norm is not attained by any unit vector. For the total-degree projection \(P_N\) onto polynomials of degree at most \(N\), every integer \(N\ge0\) satisfies the exact finite-energy identity
\[
\boxed{\operatorname{tr}\big(P_NT(I-T)P_N\big)
=\frac{(N+1)(2N+3)}6\frac{\binom{2N+2}{N+1}}{4^{N+1}}.}
\]
In particular, the normalized defect has the sharp growth law
\[
\lim_{N\to\infty}\frac{\operatorname{tr}(P_NT(I-T)P_N)}{N^{3/2}}=\frac1{3\sqrt\pi}.
\]
Both identities concern the same discontinuous, dilation-invariant two-coordinate Fock cone and quantify different manifestations of its spectral boundary layer.

## Assumptions and scope

All operator norms and traces are in the complex Hilbert space \(\mathcal F^2(\mathbb C^2)\). The monomials
\[
e_{n,m}(z)=\frac{z_1^nz_2^m}{\sqrt{n!m!}},\qquad n,m\in\mathbb N_0,
\]
form an orthonormal basis. The projection \(P_N\) has finite rank \((N+1)(N+2)/2\). The essential norm means distance to compact operators. Commutators involving \(M_1\) are initially defined on \(\operatorname{Dom}(M_1)\) and subsequently interpreted through their unique bounded extension. The cone boundary has Gaussian measure zero, so strict versus nonstrict inequality in \(E\) makes no difference.

## Proof

**1. Exact diagonalization.** Rotational invariance in both coordinates makes \(T\) diagonal. If \(X,Y\) are independent unit-rate gamma variables with respective integer shapes \(n+1,m+1\), Gaussian polar integration gives
\[
Te_{n,m}=\lambda_{n,m}e_{n,m},\qquad
\lambda_{n,m}=\Pr(X>Y).
\]
The ratio \(X/(X+Y)\) has the beta distribution with parameters \((n+1,m+1)\). Integrating its integer-parameter density, or using the beta-binomial identity, gives for \(k=n+m+1\)
\[
\lambda_{n,m}=2^{-k}\sum_{j=0}^n\binom{k}{j}.
\]
In particular \(0<\lambda_{n,m}<1\) and \(\lambda_{n,m}+\lambda_{m,n}=1\).

**2. The coordinate commutator.** The natural domain of \(M_1\) consists precisely of the coefficient arrays for which \(\sum_{n,m}(n+1)|c_{n,m}|^2<\infty\). Bounded diagonal multiplication by \(\lambda_{n,m}\) preserves this domain. Since \(M_1e_{n,m}=\sqrt{n+1}\,e_{n+1,m}\), a binomial recursion yields
\[
Ce_{n,m}=-w_{n,m}e_{n+1,m},\qquad
w_{n,m}=\frac{\sqrt{n+1}}{2^{n+m+2}}
\binom{n+m+1}{n+1}.
\]
Images of distinct basis vectors under this weighted shift are orthogonal. Thus \(\|C\|=\sup_{n,m}w_{n,m}\), provided the supremum is finite.

Put \(a=n+1\ge1\) and \(k=n+m+1\ge a\). For fixed \(a\), the ratio of the consecutive binomial probability masses is
\[
\frac{\binom{k+1}{a}2^{-(k+1)}}{\binom{k}{a}2^{-k}}
=\frac{k+1}{2(k+1-a)}.
\]
It is greater than one for \(k+1<2a\), equal to one for \(k+1=2a\), and smaller afterward. Hence the largest weight for each \(a\) is attained at \(k=2a-1\) and \(k=2a\), with common value
\[
\frac{\sqrt a}{2}\frac{\binom{2a}{a}}{4^a}.
\]
Set \(b_a=4^{-a}\binom{2a}{a}\). The sequence \(\sqrt a\,b_a\) is strictly increasing because
\[
\frac{\sqrt{a+1}\,b_{a+1}}{\sqrt a\,b_a}
=\frac{2a+1}{2\sqrt{a(a+1)}}>1.
\]
By the central-binomial Stirling formula it tends to \(1/\sqrt\pi\). Thus every individual weight is strictly less than \(1/(2\sqrt\pi)\), while weights at \((n,m)=(a-1,a-1)\) approach that number. The weighted shift is bounded, has the claimed sharp norm, and has no maximizing unit vector: in \(\|Cf\|^2=\sum_{n,m}w_{n,m}^2|c_{n,m}|^2\), every coefficient weight is strictly below the squared norm.

The basis vectors \(e_{a-1,a-1}\) converge weakly to zero while their images under \(C\) have norms tending to \(1/(2\sqrt\pi)\). Every compact operator sends such an orthonormal sequence to a norm-null sequence; consequently \(\|C\|_{\mathrm{ess}}\ge1/(2\sqrt\pi)\). The reverse inequality follows from the operator norm. This proves the commutator part.

**3. Exact finite-energy nonprojection defect.** For a fixed shell \(n+m=s\), write \(k=s+1\) and let \(B,B'\) be independent \(\mathrm{Binomial}(k,1/2)\) variables. Writing \(F(j)=\Pr(B\le j)\), the shell's defect equals
\[
\sum_{n=0}^s\lambda_{n,s-n}(1-\lambda_{n,s-n})
=\sum_{n=0}^s F(n)(1-F(n))
=\frac12\mathbb E|B-B'|.
\]
The last equality counts the integer thresholds lying strictly between the two independent binomial values. In distribution, \(2(B-B')\) is a simple symmetric random walk of length \(2k\). The standard random-walk binomial sum (obtainable by telescoping adjacent probabilities) gives
\[
\mathbb E|S_{2k}|=2k\frac{\binom{2k}{k}}{4^k}.
\]
It follows that each shell contributes exactly
\[
\frac{k}{2}\frac{\binom{2k}{k}}{4^k}.
\]
Write again \(b_k=4^{-k}\binom{2k}{k}\), for which \(b_{k+1}/b_k=(2k+1)/(2k+2)\). Induction, using that ratio, proves
\[
\sum_{k=1}^{M}k b_k=\frac{M(2M+1)}3b_M.
\]
Summing the shells with \(M=N+1\) yields the displayed exact trace formula. Finally \(b_M\sim(\pi M)^{-1/2}\) proves the sharp \(N^{3/2}\) coefficient. As an accompanying exact normalization, symmetry of the eigenvalues gives
\[
\operatorname{tr}(P_NTP_N)=\frac{(N+1)(N+2)}4.
\]
All assertions concern every stated integer; no finite enumeration is substituted for the arguments above.

## Verification

The accompanying self-contained Python script `checker.py` uses exact rational arithmetic for the beta-binomial identity, the commutator weights, the individual-shell trace identity, and the closed finite-cutoff trace. It also tests finite maximizers and the predicted leading coefficient. It passed 3,073 supplementary assertions. The sharp infinite norm, nonattainment, essential norm, and asymptotic coefficient are established by the analytic proof above, not by extrapolating numerical checks.

## Relationship to prior work

Dewage and Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols* (arXiv:2107.01465, first posted 3 July 2021), prove general diagonalization and gamma-integral eigenvalue formulas for bounded quasi-radial symbols, including this cone's symmetry class. Their Theorem 2.12 and Corollary 2.16 supply the integral starting point, not the sharp norm for the unbounded-coordinate commutator or the exact finite-energy defect formula. Hagger's *Essential Commutants and Characterizations of the Toeplitz Algebra* (arXiv:2002.02344) concerns commutation modulo compact operators with bounded vanishing-oscillation symbols; it does not imply a norm for multiplication by the unbounded coordinate. Dong's 2020 paper addresses finite-rank commutators of monomial-type Toeplitz operators, a different operation and symbol class. Historical priority for the two sharp formulas is not independently certified.

## Limitations

The theorem is for the unweighted analytic Gaussian Fock space in precisely two complex dimensions and the symmetric cone \(|z_1|>|z_2|\). It does not classify unequal cone slopes, additional coordinate blocks, or arbitrary discontinuous Toeplitz symbols. The exact constant depends on the Gaussian normalization. A separate finite-size equality cannot be assumed to hold after changing the energy cutoff. The accessible account of Dong's related commutator paper was its abstract, not its full text. No independent mathematical audit has been performed.

## References

1. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465v1 (3 July 2021), especially Theorem 2.12 and Corollary 2.16; full HTML: https://arxiv.org/html/2107.01465v3 .
2. R. Hagger, *Essential Commutants and Characterizations of the Toeplitz Algebra*, arXiv:2002.02344 (6 February 2020), https://arxiv.org/abs/2002.02344 .
3. X.-T. Dong, *Commutators and Semi-Commutators of Toeplitz Operators on the Fock Space*, Indian Journal of Pure and Applied Mathematics 51 (2020), 195–215, DOI:10.1007/s13226-020-0395-7 (abstract consulted).
