# An exact prime-square root law and sharp stabilization degree for random monic polynomials

## Finding

Fix any prime \(p\) and integer \(d\geq0\). Choose the coefficients of the monic polynomial
\[
f(X)=X^d+\sum_{j=0}^{d-1}a_j X^j\in(\mathbb Z/p^2\mathbb Z)[X]
\]
independently and uniformly modulo \(p^2\). Let \(R_{p,d}\) be the number of distinct residue classes \(x\bmod p^2\) with \(f(x)=0\). Define
\[
B_p(z)=1-p^{-1}-z+p^{-1}z^p.
\]
Then, for every \(p\) and \(d\), the **entire probability generating function** is
\[
\boxed{G_{p,d}(z):=\mathbb E[z^{R_{p,d}}]
=p^{-d}[u^d]\frac{\big(1+(z-1)u+B_p(z)u^2\big)^p}{1-pu}.}
\tag{1}
\]
In particular, the distribution is independent of \(d\) for all \(d\geq 2p\), and this threshold is **sharp**: more precisely,
\[
\boxed{G_{p,2p}(z)-G_{p,2p-1}(z)=p^{-2p}B_p(z)^p\ne0.}
\tag{2}
\]
For every \(d\geq2\), its first two moments have no degree dependence:
\[
\boxed{\mathbb E R_{p,d}=1,\quad
\operatorname{Var}(R_{p,d})=2(1-p^{-1}),\quad
\mathbb E R_{p,d}^2=3-2p^{-1}.}
\tag{3}
\]
For \(d=0\), \(R_{p,0}=0\); for \(d=1\), \(R_{p,1}=1\) surely.

A further consequence illustrates why the second moment matters: for every fixed \(d\geq2\), as primes \(p\to\infty\), the distribution of \(R_{p,d}\) converges to the fixed-point count of a uniform random permutation of \(d\) labels, whose second moment is \(2\), whereas \(\mathbb E R_{p,d}^2\to3\). Rare fibers of \(p\) singular lifts account for this failure of second-moment convergence.

## Assumptions and scope

The sample space has exactly \(p^{2d}\) monic coefficient vectors over \(\mathbb Z/p^2\mathbb Z\), with the leading coefficient fixed to \(1\). Roots are **residue classes modulo \(p^2\)**, not roots over \(\mathbb Q_p\) or \(\mathbb Z_p\). No assumption on \(p\), including the prime \(2\), or on the relative sizes of \(p\) and \(d\) is imposed. The formal coefficient extraction \([u^d]\) is in the power-series ring \(\mathbb Q[z][[u]]\).

## Proof

**Step 1: conditional lifting.** Write the reduction of \(f\) modulo \(p\) as \(\bar f\in\mathbb F_p[X]\). Let \(s(\bar f)\) be the number of distinct simple roots, and let \(m(\bar f)\) be the number of distinct roots of multiplicity at least two, in \(\mathbb F_p\). The unique lift of a simple root gives exactly one root modulo \(p^2\), by the linear Taylor congruence
\[
f(\alpha+pt)\equiv f(\alpha)+ptf'(\alpha)\pmod{p^2}.
\]
For a repeated root \(\alpha\) of \(\bar f\), the same congruence shows that either all \(p\) classes \(\alpha+pt\) are roots or none are. Writing a coefficient lift in the form \(f=f_0+ph\), with \(\deg h<d\) uniformly random over \(\mathbb F_p\), the condition for all \(p\) classes to be roots is one affine equation \(h(\alpha)=c_\alpha\). These conditions for distinct repeated roots are independent because
\[
m(\bar f)\leq \lfloor d/2\rfloor\leq d,
\]
and evaluation at that many distinct field elements is surjective (Vandermonde interpolation for \(\deg h<d\)). Hence, conditionally on \(\bar f\), the repeated roots contribute independent Bernoulli choices with success probability \(1/p\), each success adding \(p\) roots. Thus
\[
\mathbb E\big[z^{R_{p,d}}\mid\bar f\big]
=z^{s(\bar f)}\left(1-p^{-1}+p^{-1}z^p\right)^{m(\bar f)}.
\tag{4}
\]
For \(d=0\) there are no roots and this formula also holds, with both counts zero.

**Step 2: count reductions of every degree simultaneously.** A monic polynomial over \(\mathbb F_p\) factors uniquely into monic irreducibles. For each of the \(p\) linear irreducibles, its multiplicity \(0\), \(1\), or \(\geq2\) contributes respective weights \(1\), \(z\), or \(H_p(z)=1-p^{-1}+p^{-1}z^p\). Its degree-enumerating series is
\[
1+zu+H_p(z)(u^2+u^3+\cdots)
=\frac{1+(z-1)u+(H_p(z)-z)u^2}{1-u}.
\tag{5}
\]
The unweighted Euler product over **all** monic irreducibles equals \(\sum_{d\geq0}p^du^d=(1-pu)^{-1}\); the product for linear factors alone is \((1-u)^{-p}\). Consequently the Euler product over irreducibles of degree at least two equals \((1-u)^p/(1-pu)\). Multiplying it by the \(p\) modified linear-factor series in (5), and averaging over the \(p^d\) reductions of degree \(d\), gives exactly (1) because \(H_p(z)-z=B_p(z)\).

**Step 3: exact stabilization boundary.** Write
\[
A_p(u,z)=\big(1+(z-1)u+B_p(z)u^2\big)^p
=\sum_{j=0}^{2p}b_{p,j}(z)u^j.
\]
Equation (1) becomes \(G_{p,d}(z)=\sum_{j=0}^{\min(d,2p)}p^{-j}b_{p,j}(z)\). Therefore it is constant for all \(d\geq2p\); subtracting adjacent degrees at the last boundary gives
\[
G_{p,2p}(z)-G_{p,2p-1}(z)
=p^{-2p}b_{p,2p}(z)=p^{-2p}B_p(z)^p.
\]
The polynomial \(B_p\) is not zero (its coefficient of \(z\) is \(-1\)), establishing (2) and the minimal stabilization degree.

**Step 4: moments.** At \(z=1\), both \(B_p(1)\) and \(B_p'(1)\) vanish and \(B_p''(1)=p-1\). Differentiating (1) at \(z=1\) gives, for \(d\geq1\),
\[
G'_{p,d}(1)=p^{-d}[u^d]\frac{pu}{1-pu}=1.
\]
Differentiating twice yields, for \(d\geq2\),
\[
G''_{p,d}(1)=p^{-d}[u^d]\frac{2p(p-1)u^2}{1-pu}
=2(1-p^{-1}).
\]
Since \(G''(1)=\mathbb E[R(R-1)]\), (3) follows. The cases \(d=0,1\) are immediate.

**Step 5: limiting distribution and moment defect.** Let \(T_{p,d}\) count the roots of \(\bar f\) in \(\mathbb F_p\). A uniformly random monic polynomial of degree \(d\geq2\) over \(\mathbb F_p\) is nonsquarefree with probability \(1/p\), by the elementary squarefree polynomial count \(p^d-p^{d-1}\). On the complementary event every root lifts once, so \(R_{p,d}=T_{p,d}\). Hence their laws differ in total variation by at most \(1/p\). For \(0\leq k\leq d\), evaluation at distinct field elements imposes \(k\) independent constraints on the \(d\) free coefficients, so
\[
\mathbb E[(T_{p,d})_k]=(p)_k/p^k\longrightarrow1
\qquad(p\to\infty),
\]
while all factorial moments of order \(k>d\) vanish. These are precisely the factorial moments of the fixed-point count of a uniform random permutation of \(d\) elements; bounded support of \(T_{p,d}\) makes the limiting law unique. For \(d\geq2\), that law has mean \(1\) and second factorial moment \(1\), hence second moment \(2\). Formula (3) gives \(\mathbb E R_{p,d}^2\to3\), proving the assertion.

## Verification

Run `python3 verify_root_p2_monic.py` using only Python's standard library. The verifier independently exhausts all monic coefficient vectors over twelve small prime-square rings and further instances, compares the distribution against the rational generating function, checks the conditional singular-root law by separate enumeration of reductions, checks the sharp \(2p\) stabilization boundary, and verifies both moments. Its execution output is

`VERIFY_OK exhaustive_cases=17 conditional_cases=5 stability_primes=6`

All finite enumerations are checks of finite instances, not substitutes for the uniform all-prime proof above. Exact rational arithmetic is used throughout.

## Relationship to prior work

Simhi's 2026 study of squarefree values of random polynomials uses the local counts \(\rho_g(p^2)\), analyzes simple and singular lifts in §3.1, and bounds their moments in Lemma 3.4 and Appendix A. It does not state (1), (2), or an exact law for the **monic** fixed-degree ensemble. The present result gives a complete all-degree formula and a sharp stabilization index for that natural local model.

Jain, Moon, and Wu study finite-field root-count generating functions and, in §5, ask for their prime-power-ring analogues, along with conjectural stabilization. Their explicit prime-power question concerns **all** polynomials of degree at most \(d\), so (1) is a monic univariate analogue, **not** a claimed solution of that more general question. Leont'ev's earlier result concerns roots over finite fields, not modulo prime squares. Bhargava, Cremona, Fisher, and Gajović compute distributions of **actual** \(p\)-adic zeros, a different random variable from finite-level congruence roots. An earlier finite-degree quadratic calculation for nonzero unrestricted coefficient vectors does not imply this all-degree monic distribution.

## Limitations

The theorem is restricted to **univariate monic** polynomials modulo the **square** of a prime. It does not handle unrestricted leading coefficients, multivariable root counts, prime powers of exponent \(\geq3\), or actual \(p\)-adic roots. The limiting-law comparison is for fixed degree as \(p\to\infty\) and is not uniform in growing degree. A priority search cannot exclude unindexed or implicit earlier derivations of (1).

## References

1. O. Simhi, *Squarefree values of random polynomials are Gaussian mixtures*, arXiv:2610.29911 (first public 2026-10-21), §§3.1 and A.1. https://arxiv.org/abs/2610.29911
2. R. Jain, H.-B. Moon, P. Wu, *Distribution of the number of zeros of polynomials over a finite field*, arXiv:2308.14580 (first public 2023-08-28), §§3,5. https://arxiv.org/abs/2308.14580
3. V. K. Leont'ev, *Roots of Random Polynomials over a Finite Field*, Mathematical Notes 80 (2006), 300–304. https://doi.org/10.1007/s11006-006-0139-y
4. M. Bhargava, J. Cremona, T. Fisher, S. Gajović, *The density of polynomials of degree n over Zp having exactly r roots in Qp*, Proc. London Math. Soc. 124 (2022), 713–736. https://doi.org/10.1112/plms.12438
