# A zero-dimensional continuous limit law for reciprocal divisor sums over finite polynomial rings

## Finding

Fix a prime power \(q\ge 2\). For any monic \(F\in\mathbb F_q[T]\), define its reciprocal-divisor sum
\[
A(F)=\sum_{D\mid F,\ D\text{ monic}}q^{-\deg D}.
\]
Let \(F_n\) be uniformly distributed over the \(q^n\) monic polynomials of degree \(n\). **As \(n\to\infty\), \(A(F_n)\) converges in distribution to a random variable \(Z_q\) whose law has no atoms and assigns probability one to a Borel subset of the real line of Hausdorff dimension zero.** Consequently its limiting law is purely singular continuous: it is not a discrete law, and is singular with respect to Lebesgue measure. This is a statement about a full-measure carrier; it does **not** claim that the topological support has dimension zero.

More explicitly, for each monic irreducible polynomial \(P\), choose an independent integer-valued random variable \(V_P\ge0\) with
\[
\Pr(V_P=k)=(1-q^{-\deg P})q^{-k\deg P},\qquad k\ge0.
\]
Then
\[
Z_q=\prod_{P\text{ monic irreducible}}
\left(\sum_{j=0}^{V_P}q^{-j\deg P}\right)
\]
converges to a finite, strictly positive random variable almost surely. Its first two moments are exactly
\[
\mathbb E Z_q=\frac{1}{1-q^{-1}},\qquad
\mathbb E Z_q^2=\frac{1-q^{-3}}{(1-q^{-1})^2(1-q^{-2})},
\]
so its variance is \(\big[q^2(1-q^{-1})(1-q^{-2})\big]^{-1}>0\).

## Assumptions and scope

The field size \(q\) is fixed as the polynomial degree \(n\) tends to infinity. Divisors and irreducibles are monic, and the constant divisor is counted. The normalized polynomial absolute value is \(|F|=q^{\deg F}\) for nonzero \(F\). The random variables \(V_P\) are independent across distinct monic irreducibles. The theorem applies uniformly in characteristic, including characteristic two; it does not describe a simultaneous \(q,n\to\infty\) limit. No claim is made about Hausdorff dimension of the *topological support* of the law.

Write \(\pi_q(d)\) for the number of monic irreducibles of degree \(d\). Unique factorization gives
\[
\pi_q(d)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}
=\frac{q^d}{d}+O_q(q^{d/2}/d),\qquad
\pi_q(d)\le \frac{q^d}{d}.
\]
The error estimate follows directly by bounding the proper divisors; it is not a hypothesis.

## Proof

**1. Limiting product and convergence.** Let \(p_P=q^{-\deg P}\) and set
\[
Y_n=\log A(F_n),\quad
Y=\sum_P\log\Big(\sum_{j=0}^{V_P}p_P^j\Big).
\]
All terms in the last sum are nonnegative and satisfy
\[
0\le\log\Big(\sum_{j=0}^{V_P}p_P^j\Big)
\le \frac{p_P}{1-p_P}\,\mathbf1_{V_P\ge1}.
\]
As \(\Pr(V_P\ge1)=p_P\), the expectation of the sum is bounded by
\[
\sum_{d\ge1}\pi_q(d)\frac{q^{-2d}}{1-q^{-d}}<\infty.
\]
Thus \(Y<\infty\) almost surely and \(Z_q=e^Y\in[1,\infty)\) is well-defined.

For each fixed cutoff \(D\), the valuations of the finitely many monic irreducibles of degrees at most \(D\) in \(F_n\) converge jointly to \((V_P)_{\deg P\le D}\): for any finite exponents, the probability that the corresponding product divides \(F_n\) is exactly the reciprocal norm of that product once \(n\) is large enough. Inclusion and exclusion recover all joint geometric probabilities. Let \(Y_{n,D}\) and \(Y_D\) denote the corresponding truncated logarithms. Since a monic irreducible \(P\) of degree at most \(n\) divides the uniform \(F_n\) with probability \(p_P\), for every \(D,n\)
\[
\mathbb E(Y_n-Y_{n,D})\le
\sum_{d>D}\pi_q(d)\frac{q^{-2d}}{1-q^{-d}}
=O_q(q^{-D}/(D+1)).
\]
The same estimate holds for \(\mathbb E(Y-Y_D)\). Fixed-cutoff convergence and these uniform tail bounds imply \(Y_n\Rightarrow Y\), hence \(A(F_n)=e^{Y_n}\Rightarrow Z_q\).

**2. Absence of atoms.** The following splitting uses only \(p_P\le 1/2\). Independently for each \(P\), choose \(B_P\) Bernoulli with success probability \(2p_P\), \(C_P\) fair Bernoulli, and \(W_P\ge1\) with \(\Pr(W_P=k)=(1-p_P)p_P^{k-1}\). Set \(V_P=B_PC_PW_P\). Then \(\Pr(V_P=k)=(1-p_P)p_P^k\) for \(k\ge1\) and \(\Pr(V_P=0)=1-p_P\), as required.

Condition on all \((B_P,W_P)\) with \(\deg P\le D\). The truncated logarithm is a sum of
\[
M_D=\sum_{\deg P\le D}B_P
\]
independent fair Bernoulli variables, each multiplied by a strictly positive real weight \(\log\sum_{j=0}^{W_P}p_P^j\). For a prescribed real sum, the corresponding subsets form an antichain in the Boolean lattice: a proper inclusion would strictly increase the sum. Sperner's theorem therefore gives the conditional point-mass bound
\[
\sup_t\Pr(Y_D=t\mid(B_P,W_P)_{\deg P\le D})
\le 2^{-M_D}\binom{M_D}{\lfloor M_D/2\rfloor}
\le \frac{C}{\sqrt{M_D+1}}.
\]
The prime-polynomial count above yields
\[
\mathbb E M_D=2\sum_{d\le D}\pi_q(d)q^{-d}
=2\log D+O_q(1),\quad
\operatorname{Var}M_D\le \mathbb E M_D.
\]
Hence \(M_D\to\infty\) in probability, and \(\sup_t\Pr(Y_D=t)\to0\). The infinite tail \(Y-Y_D\) is independent of \(Y_D\), so for any fixed \(t\),
\[
\Pr(Y=t)\le \sup_s\Pr(Y_D=s)\longrightarrow0.
\]
Thus \(Y\), and therefore \(Z_q=e^Y\), has no atoms.

**3. Zero-dimensional full-measure carrier.** Define \(K_D=\sum_{\deg P\le D}V_P\). For fixed \(0<t<\log q\), geometric generating functions give
\[
\log\mathbb E e^{tK_D}
=\sum_{d\le D}\pi_q(d)
\log\frac{1-q^{-d}}{1-e^tq^{-d}}
=(e^t-1)\log D+O_{q,t}(1).
\]
Here the contribution of quadratic and higher powers of \(q^{-d}\) is summable. Chernoff's inequality therefore permits a constant \(L=L(q)>0\) for which
\[
\Pr(K_D>L\log D)=O_q(D^{-3}),\qquad D\ge2.
\]
Whenever \(K_D\le L\log D\), the value of \(Y_D\) depends only on the numbers \(c_{d,r}\) of irreducibles of each degree \(1\le d\le D\) having exponent \(1\le r\le\lfloor L\log D\rfloor\). All such counts are nonnegative integers with \(\sum_{d,r}r c_{d,r}\le L\log D\). There are therefore at most
\[
N_D\le \exp(C_q(\log D)^2)
\]
possible values of \(Y_D\) in this event: one may choose at most \(L\log D\) nonzero entries among \(O(D\log D)\) possible index pairs, with each value at most \(L\log D\).

From Step 1 and Markov's inequality,
\[
\Pr(Y-Y_D>q^{-D/2})=O_q(q^{-D/2}/(D+1)).
\]
Both failure probabilities are summable over \(D\). By the first Borel–Cantelli lemma, with probability one, for all sufficiently large \(D\), the value \(Y\) belongs to a union of at most \(N_D\) intervals of length \(2q^{-D/2}\), centered at the possible values of \(Y_D\) satisfying \(K_D\le L\log D\). Let \(E\) be the Borel set of points that belong to all these unions for all sufficiently large \(D\); then \(\Pr(Y\in E)=1\). For every \(s>0\),
\[
\mathcal H^s(E)\le\liminf_{D\to\infty}
N_D(2q^{-D/2})^s=0.
\]
Thus \(\dim_{\mathrm H} E=0\). The exponential map is Lipschitz on each bounded interval, so \(e^E\) is a countable union of sets of Hausdorff dimension zero. It is a Borel set of dimension zero carrying the entire distribution of \(Z_q\). As Lebesgue measure vanishes on any such set, the atomless law of \(Z_q\) is singular continuous.

**4. Moments.** Independence, monotone convergence, and the local geometric distribution give
\[
\mathbb EZ_q=\prod_P(1-p_P^2)^{-1}
=\frac1{1-q^{-1}},
\]
using \(\prod_P(1-z^{\deg P})^{-1}=(1-qz)^{-1}\). For the second moment the exact single-prime identity is
\[
\mathbb E\left(\sum_{j=0}^{V_P}p_P^j\right)^2
=\frac{1-p_P^4}{(1-p_P^2)^2(1-p_P^3)}.
\]
Taking the product yields
\[
\mathbb E Z_q^2
=\frac{\zeta_q(2)^2\zeta_q(3)}{\zeta_q(4)}
=\frac{1-q^{-3}}{(1-q^{-1})^2(1-q^{-2})}.
\]
Subtracting the square of the mean gives the stated positive variance. Each product converges by the explicit zeta identity.

## Verification

All infinite assertions follow from the proofs above, not from finite experiments. The separately supplied `verify.py` uses exact rational arithmetic and direct polynomial division to check all monic polynomials over \(\mathbb F_2\) through degree eight and over \(\mathbb F_3\) through degree five. It compares exact first and second empirical moments with the generating-function identities
\[
\sum_{n\ge0}\sum_{F\in\mathcal M_n} A(F)u^n
=\frac1{(1-qu)(1-u)},
\]
\[
\sum_{n\ge0}\sum_{F\in\mathcal M_n} A(F)^2u^n
=\frac{1-u^2/q}{(1-qu)(1-u)^2(1-u/q)}.
\]
The program completed with `VERIFY_OK`. Exhaustive finite-degree examples cannot establish weak convergence, atomlessness, or dimension zero.

## Relationship to prior work

Afifurrahman, *Statistics of divisor functions over function fields* (arXiv:2610.11240v1, October 8, 2026; primary MSC 11T55), studies restricted divisor-function moments and shifted correlations. It is the recent impetus for studying finer limiting statistics of naturally weighted polynomial divisor functions; its theorems do not assert the present singular-continuity and Hausdorff-dimension classification.

Darbar and Mukhopadhyay, *Correlation of multiplicative functions over function fields* (arXiv:1905.09303), Theorem 4 and Section 3, and the published expanded treatment *Correlation of multiplicative functions over \(\mathbb F_q[x]\): A pretentious approach* (Mathematika, DOI 10.1112/mtk.12227), Theorem 6, establish broad existence criteria for limiting laws of additive functions. Such a theorem may already give the weak-convergence component here by applying it to \(\log A\). **The claim of originality is restricted to the concrete, jointly proved fact that this specific normalized divisor-sum law is non-atomic yet concentrated on a zero-dimensional set, with the displayed moment formulas; mere existence of a weak limit is not claimed new.** Those sources do not provide the particular Sperner argument or the subexponential degree-histogram covering conclusion.

The classical theory of infinite convolutions and arithmetic distribution laws supplies general context, including the Jessen–Wintner pure-type principle; pure-type assertions alone do not determine dimension zero or eliminate atoms for this arithmetic law.

## Limitations

The theorem is a fixed-\(q\), large-degree result; no quantitative rate of weak convergence or density regularity on a subset is claimed. It concerns the distribution's full-measure Hausdorff-zero carrier, not necessarily its closed topological support. The independent geometric local model, the exact polynomial prime-count formula, and Sperner's theorem are invoked with proofs of the applications; the computations check only finitely many degrees over two prime fields. Although targeted literature comparisons found no statement subsuming the geometric classification, a differently phrased general theorem about infinite convolutions could in principle cover it, so external literature verification remains warranted. No external independent audit has been performed.

## References

1. M. Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first public October 8, 2026), https://arxiv.org/abs/2610.11240.
2. P. Darbar and A. Mukhopadhyay, *Correlation of multiplicative functions over function fields*, arXiv:1905.09303 (2019), https://arxiv.org/abs/1905.09303.
3. P. Darbar and A. Mukhopadhyay, *Correlation of multiplicative functions over \(\mathbb F_q[x]\): A pretentious approach*, Mathematika 70 (2024), e12227, https://doi.org/10.1112/mtk.12227.
4. E. Sperner, *Ein Satz über Untermengen einer endlichen Menge*, Math. Z. 27 (1928), 544–548 (antichain bound).
5. B. Jessen and A. Wintner, *Distribution functions and the Riemann zeta function*, Trans. Amer. Math. Soc. 38 (1935), 48–88 (infinite-convolution context).
