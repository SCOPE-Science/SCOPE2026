# Poisson-binomial vacancy law for heterogeneous group coupon drawings

## Finding
For every integer \(n\geq1\) and every finite sequence of integers \(0\leq s_1,\ldots,s_m\leq n\), draw independent uniformly random \(s_\ell\)-element subsets \(S_\ell\subseteq[n]\), where \(m\geq0\), and put
\[
U=\bigl|[n]\setminus\bigcup_{\ell=1}^{m}S_\ell\bigr|.
\]
Then the probability-generating polynomial \(F(z)=\mathbb E[z^U]\) has only real nonpositive zeros. Consequently, for some \(\theta_1,\ldots,\theta_n\in[0,1]\),
\[
U\ \stackrel{\mathrm d}=\ \sum_{i=1}^n B_i,
\qquad B_i\ \text{independent Bernoulli}(\theta_i).
\]
The multivariate distribution of the vector of *unseen-type indicators* is strongly Rayleigh and, in particular, negatively associated; this is a conclusion about the joint vector rather than a claim that its coordinates are independent. The assertion holds with arbitrary packet sizes varying between rounds, including zero-size and full-size rounds.

The complete finite-sample probability-generating polynomial is
\[
F(z)=\sum_{j=0}^n\binom nj(z-1)^j
\prod_{\ell=1}^m\frac{\binom{n-j}{s_\ell}}{\binom n{s_\ell}},
\]
where \(\binom ab=0\) when \(b>a\), and an empty product equals one. Its roots yield the Bernoulli parameters explicitly.

## Assumptions and scope
The ground set \([n]\) contains \(n\) distinguishable coupon types. In round \(\ell\), exactly \(s_\ell\) *distinct* types are drawn, each subset of that size having equal probability; rounds are independent. No limiting regime or restriction on the number of rounds is assumed. The assertion concerns the total number of types never drawn, not the vector of numbers of repetitions of individual coupons. The Bernoulli parameters need not be distinct and may be zero or one.

## Proof
**1. Exact factorial moments.** For each fixed \(j\)-subset \(J\subseteq[n]\), the probability that all its types remain unseen is
\[
\mathbb P(J\text{ unseen})=\prod_{\ell=1}^{m}
\frac{\binom{n-j}{s_\ell}}{\binom n{s_\ell}}.
\]
The identity \(z^U=\sum_{j=0}^U\binom Uj(z-1)^j\), followed by summation over the \(\binom nj\) choices for \(J\), proves the displayed formula for \(F\).

**2. Hypergeometric packet update.** Consider any exchangeable random unseen subset \(A\subseteq[n]\) and let \(F(z)=\mathbb E[z^{|A|}]\). Independently choose a uniform \(t\)-subset \(B\) of \([n]\), where \(0\leq t\leq n\). The updated unseen set is \(A\cap B\). Conditional on \(|A|=k\),
\[
\mathbb E[z^{|A\cap B|}\mid |A|=k]
=\frac{[w^t](1+zw)^k(1+w)^{n-k}}{\binom nt}.
\]
Hence the updated probability-generating polynomial is exactly
\[
T_tF(z)=\frac{[w^t](1+w)^n F\!\left(\frac{1+zw}{1+w}\right)}{\binom nt}.
\]
Here \([w^t]\) denotes the coefficient of \(w^t\); the apparent rational substitution cancels for every polynomial \(F\) of degree at most \(n\).

**3. Root preservation.** Assume \(F\) has only nonpositive real zeros. Factor it as
\[
F(z)=c\prod_{i=1}^{d}(z+a_i),\qquad
c>0,\quad a_i\geq0,\quad 0\leq d\leq n.
\]
Then
\[
G(z,w)=(1+w)^nF\!\left(\frac{1+zw}{1+w}\right)
=c(1+w)^{n-d}\prod_{i=1}^{d}
\bigl(1+a_i+(z+a_i)w\bigr).
\]
For \(\operatorname{Im}z>0\) and \(\operatorname{Im}w<0\), none of these factors can vanish. Indeed, the zero equation for a nonconstant factor is \(z=-a_i-(1+a_i)/w\), whose imaginary part is *negative* whenever \(\operatorname{Im}w<0\). Also \(1+w\ne0\) on this lower half-plane. Fixing such a \(z\), every zero of the polynomial \(w\mapsto G(z,w)\) lies in the closed upper half-plane. By the Gauss–Lucas theorem the same is true of every derivative \(\partial_w^tG(z,w)\) with \(0\leq t\leq n\). In particular, \(\partial_w^tG(z,w)\ne0\) when \(\operatorname{Im}z>0\) and \(\operatorname{Im}w<0\). Let \(w\) tend to zero within the lower half-plane. Hurwitz's theorem applied as a function of \(z\) shows that \(\partial_w^tG(z,0)\) is either zero-free in the upper half-plane or is identically zero. The second alternative is excluded because
\[
G(1,w)=(1+w)^nF(1)=(1+w)^n,
\qquad [w^t]G(1,w)=\binom nt>0.
\]
Thus \(T_tF\) has no zero in the upper half-plane. Since it is a real polynomial, all its zeros are real; since its coefficients are probabilities, no real zero can be positive. Hence \(T_tF\) has only nonpositive real zeros.

**4. Induction and distributional representation.** Before any drawing, the unseen set is \([n]\) and \(F_0(z)=z^n\). In round \(\ell\), intersect with the complement of the drawn set, a uniform subset of cardinality \(t_\ell=n-s_\ell\). Step 3 inductively proves the real-zero assertion for every finite drawing sequence. As \(F(1)=1\), its factorization gives
\[
F(z)=\prod_{i=1}^{d}\left(\frac{a_i}{1+a_i}
+\frac{z}{1+a_i}\right)
=\prod_{i=1}^{n}(1-\theta_i+\theta_i z),
\]
where \(\theta_i=(1+a_i)^{-1}\) for \(i\leq d\) and the remaining parameters are zero. This is the probability-generating polynomial of a sum of independent Bernoulli random variables. This establishes equality *in law*, not independence of the physical unseen indicators.

**5. Strong Rayleigh consequence.** The unseen subset is exchangeable because every drawing distribution is invariant under permutations of the ground set. Its multiaffine generating polynomial is the polarization of \(F\):
\[
H(z_1,\ldots,z_n)=\sum_{k=0}^n
\frac{\mathbb P(U=k)}{\binom nk}
\sum_{\substack{J\subseteq[n]\\|J|=k}}\prod_{j\in J}z_j.
\]
Polarization of a univariate real-stable polynomial is multivariate stable (equivalently, apply the exchangeable characterization in Borcea–Brändén–Liggett, Theorem 3.8). Therefore \(H\) is real stable, and the unseen-indicator law is strongly Rayleigh. Its negative association and ultra log concavity of its rank sequence follow by the standard implications established in that work. This applies also when \(F\) has deterministic factors.

## Verification
Run `python verify.py` with Python 3 and SymPy. The exact verifier constructs the hypergeometric law using rational arithmetic for every \(1\leq n\leq8\) and every sorted packet-size sequence of length at most three. It performs 710 rational distribution/real-root checks (exact Sturm root counts of squarefree factors), 5,144 exact factorial-moment checks, and eight independently enumerated underlying-subset cases. All pass. The example with \(n=5\) and two rounds of size two gives
\[
F(z)=\frac{z(z^2+6z+3)}{10},\qquad
\operatorname{roots}(F)=\{0,-3-\sqrt6,-3+\sqrt6\}.
\]
The verifier is supplementary: the analytic induction above proves the statement for unbounded \(n\) and arbitrary finite \(m\).

## Relationship to prior work
Betken and Thäle (2022, arXiv:2202.07485; published 2023) investigate *the same number of unseen types* for independent fixed-size uniform group drawings, proving quantitative Gaussian and Poisson approximation in asymptotic regimes. Their inspected work does not give a finite-sample Poisson-binomial representation or arbitrary varying packet sizes. Borcea, Brändén, and Liggett (2009, arXiv:0707.2340) supply the strongly Rayleigh and stable-polynomial framework, including polarization and negative-dependence consequences. Tang and Tang (2023, DOI:10.1214/22-STS852) review the classical equivalence between real-rooted probability-generating polynomials and Poisson-binomial laws. These general characterizations do not by themselves establish the group-drawing root-preserving transition proved here.

## Limitations
The group sizes may vary, but conditional uniformity within each round and independence between rounds are essential hypotheses; arbitrary weighted or dependent packets are not covered. The result identifies existence of Bernoulli parameters through roots rather than closed elementary expressions for all parameters. No claim of a new general stable-polynomial preservation theorem is made beyond the specific transition. The mathematical proof is finite-dimensional but uniform over every admissible dimension and finite drawing sequence. Earlier equivalent results in differently named occupancy or negative-dependence literature remain a possible bibliographic risk; independent priority assessment has not been performed.

## References
1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485 (first posted 2022-02-15); *Journal of Applied Probability*, DOI:10.1017/jpr.2023.6.
2. J. Borcea, P. Brändén and T. M. Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340; *Journal of the American Mathematical Society* 22 (2009), 521–567.
3. W. Tang and F. Tang, *The Poisson Binomial Distribution—Old & New*, *Statistical Science* 38 (2023), 108–119, DOI:10.1214/22-STS852.
4. P. Brändén and J. Jonasson, *Negative dependence in sampling*, *Scandinavian Journal of Statistics* 39 (2012), 830–838, DOI:10.1111/j.1467-9469.2011.00766.x (comparison based on abstract and publicly indexed theorem statement; full text not retrieved).
