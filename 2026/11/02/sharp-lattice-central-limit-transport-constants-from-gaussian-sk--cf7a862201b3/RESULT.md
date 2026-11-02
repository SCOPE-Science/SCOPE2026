# Sharp lattice central-limit transport constants from Gaussian skewness and uniform quantization

## Finding
For the standardized sum of any iid nondegenerate finite-support lattice distribution with maximal span \(d\), standard deviation \(\sigma\), and skewness \(\gamma\), the complete fixed-order asymptotic transport spectrum is
\[
\lim_{n\to\infty} n^{r/2}W_r(P_n,G)^r
=\mathbb E\left|\frac{\gamma}{6}(Z^2-1)+U\right|^r,
\qquad 1\le r<\infty,
\]
where \(G=N(0,1)\), \(Z\sim G\), \(U\sim\mathrm{Unif}[-d/(2\sigma),d/(2\sigma)]\), and \(Z,U\) are independent. Consequently,
\[
\lim_{n\to\infty}nW_2(P_n,G)^2
=\frac{d^2}{12\sigma^2}+\frac{\gamma^2}{18}.
\]
Thus the leading quadratic transport cost is the sum of an arithmetic lattice quantization contribution and a smooth skewness contribution, without a mixed term. For symmetric summands the leading \(W_r\) constant is \(d/[2\sigma(r+1)^{1/r}]\). 

## Assumptions and scope
Fix a nonconstant real random variable \(X\) taking finitely many values contained in \(a+d\mathbb Z\) for a real \(a\) and maximal lattice span \(d>0\) (the integer differences of its supported lattice indices have greatest common divisor one). Let \(X_i\) be iid copies. Write \(\mu=\mathbb EX\), \(\sigma^2=\operatorname{Var}X>0\), and \(\gamma=\mathbb E[(X-\mu)^3]/\sigma^3\). Set
\[
S_n=\frac{\sum_{i=1}^nX_i-n\mu}{\sigma\sqrt n},
\quad P_n=\mathcal L(S_n),\quad G=N(0,1),\quad c=d/\sigma.
\]
We use \(W_r(P,Q)^r=\inf\mathbb E|V-W|^r\), where the infimum is over couplings with laws \(P,Q\). All limits are for fixed \(1\le r<\infty\). Finite support supplies every required moment and the maximal-span lattice Edgeworth expansion. No assumption of symmetry is imposed.

## Proof
**1. Continuity-corrected lattice normal approximation.** Put \(h_n=c/\sqrt n\). Central support values of \(S_n\) lie on \(b_n+h_n\mathbb Z\), with \(b_n=(na-n\mu)/(\sigma\sqrt n)\). Since the integer support differences generate \(\mathbb Z\), the standard lattice local central limit theorem ensures all lattice sites in each fixed compact interval eventually have positive masses. Denote the standard Gaussian CDF and density by \(\Phi,\phi\). For \(x\) at a central support site, the continuity-corrected first-order lattice Edgeworth expansion, as in Kolassa–McCullagh (1990), is uniformly
\[
F_n(x)=\Phi(x+h_n/2)
+\frac{\gamma}{6\sqrt n}\bigl[1-(x+h_n/2)^2\bigr]\phi(x+h_n/2)
+o(n^{-1/2}). \tag{1}
\]
The Sheppard corrections to cumulants start at order \(n^{-1}\), so (1) is the ordinary first-order skewness term at the half-step location. This is an invoked classical input, not an independently claimed new lattice-Edgeworth theorem.

Define \(A(z)=\gamma(1-z^2)/6\). Taking the inverse Gaussian CDF on any compact interval (where \(\phi\) is bounded below), (1) gives the boundaries of Gaussian-quantile cells:
\[
q_{n,k}:=\Phi^{-1}\bigl(F_n(b_n+kh_n)\bigr)
=b_n+(k+1/2)h_n+\frac{A(b_n+kh_n)}{\sqrt n}+o(h_n),\tag{2}
\]
uniformly in central indices \(k\).

**2. Quantile coupling and deterministic oscillations.** Let \(Z\) be standard normal, and define \(Q_n(z)=F_n^{-1}(\Phi(z))\) using the left-continuous generalized inverse. The coupling \((Q_n(Z),Z)\) is optimal simultaneously for all powers \(r\ge1\) by one-dimensional monotone transport. On a fixed compact \([-R,R]\), consider the shifted nearest-lattice map
\[
T_n(z)=b_n+h_n\left\lfloor
\frac{z-A(z)/\sqrt n-b_n}{h_n}+\frac12
\right\rfloor.
\]
Its cell boundaries differ from the true boundaries (2) by \(o(h_n)\), uniformly over central cells, because \(A\) is continuously differentiable and the boundaries shift by \(O(h_n)\) from unperturbed midpoints. There are \(O_R(h_n^{-1})\) such cells, so the Gaussian measure of their symmetric differences tends to zero. On \([-R,R]\), the rescaled errors \(\sqrt n(Q_n(z)-z)\) and \(\sqrt n(T_n(z)-z)\) remain uniformly bounded. It follows that for each fixed \(r\),
\[
\int_{-R}^R \big|\sqrt n(Q_n(z)-z)\big|^r\phi(z)\,dz
-\int_{-R}^R \big|\sqrt n(T_n(z)-z)\big|^r\phi(z)\,dz\longrightarrow0.\tag{3}
\]
Write \(\psi(v)=\lfloor v+1/2\rfloor-v\), which is periodic of period one and is uniformly distributed on \([-1/2,1/2]\) when its argument is uniform modulo one. Direct subtraction yields
\[
\sqrt n(T_n(z)-z)=-A(z)+c\,\psi\left(\frac{z-b_n}{h_n}-\frac{A(z)}c\right).\tag{4}
\]
For fixed \(R\), a periodic averaging lemma applies to the continuous amplitude \(A\), the smooth Gaussian weight, and the fast phase with derivative \(h_n^{-1}-A'(z)/c\). Partition \([-R,R]\) into short intervals on which amplitudes vary arbitrarily little, then average over complete periods; the leftover fragments have vanishing measure. Hence (4) has the limiting \(r\)-moment over that compact interval
\[
\int_{-R}^R\phi(z)\int_{-1/2}^{1/2}
|-A(z)+cv|^r\,dv\,dz.\tag{5}
\]
The sign of \(v\) is immaterial because the uniform distribution is symmetric. The phase also asymptotically decouples from \(Z\); indeed (5) is valid with arbitrary bounded continuous functions of \(z\), and yields weak convergence of the rescaled quantile-coupling error to \(\gamma(Z^2-1)/6+U\), with independent \(U\sim\mathrm{Unif}[-c/2,c/2]\).

**3. Tail control and power transport limit.** Choose any \(s>r\). Bobkov's general transport Berry–Esseen bound (Theorem 1.1 of Bobkov, 2018), applicable since the summands have all moments, gives \(W_s(P_n,G)=O(n^{-1/2})\). Monotone transport is simultaneously optimal for \(W_s\), so
\[
\sup_n\mathbb E\big|\sqrt n(Q_n(Z)-Z)\big|^s<\infty.
\]
Hölder's inequality now bounds the \(r\)-moment on \(\{|Z|>R\}\) by a constant times \(\Pr(|Z|>R)^{1-r/s}\), uniformly in \(n\). The limit in (5) has finite moments of every fixed order. Letting \(R\to\infty\) in (3)–(5) establishes
\[
\lim_n n^{r/2}W_r(P_n,G)^r
=\mathbb E|\gamma(Z^2-1)/6+U|^r.
\]
The \(r=2\) identity follows from independence, \(\mathbb E(Z^2-1)^2=2\), \(\mathbb EU=0\), and \(\mathbb EU^2=c^2/12\). For \(\gamma=0\), \(\mathbb E|U|^r=c^r/[2^r(r+1)]\).

## Verification
The accompanying `verify.py` evaluates the exact monotone-transport quadratic cost of centered, unit-variance binomial sums by Gaussian cell integrals. Its comparisons at four probabilities and three growing sample sizes approach the predicted constants. A separate exact symbolic integration confirms \(\mathbb E|\gamma(Z^2-1)/6+U|^2=c^2/12+\gamma^2/18\). Run `python verify.py` with Python, NumPy, SciPy and SymPy. The output in `verification_output.txt` records 21 passing assertions. These finite checks are corroboration, not evidence for an infinite asymptotic. The rigorous steps are (1), quantile-cell inversion, periodic averaging, and the higher-order transport-moment tail bound.

As a concrete family, if \(X\sim\mathrm{Bernoulli}(p)\), \(0<p<1\), then \(d=1\), \(\sigma^2=p(1-p)\), \(\gamma=(1-2p)/\sqrt{p(1-p)}\), so
\[
\lim_n nW_2(P_n,G)^2=
\frac1{12p(1-p)}+\frac{(1-2p)^2}{18p(1-p)}.
\]

## Relationship to prior work
Hafouta–Leppänen (2026, arXiv:2610.30352v1, first posted 2026-10-21) develop optimal-order \(W_2\) CLT bounds for weakly dependent sequences; these give rates, not the fixed-order sharp constants for arithmetic iid laws. Bobkov (2018) proves order-optimal \(W_r\) Berry–Esseen bounds that remain valid for lattice distributions and a sharp Edgeworth transport limit under a nonlattice Cramér condition; the latter hypothesis fails on the present maximal-span lattice. Kolassa–McCullagh (1990) supply lattice continuity-corrected Edgeworth expansions but do not state this optimal-transport constant. An established symmetric-lattice first-Wasserstein constant \(c/4\) appears in classical optimal-transport exposition and is a covered special case; the present finding is the explicit joint skewness–quantization law across all fixed orders. The stated structural combination was not found in inspected primary material or targeted mathematical research-record searches, but non-detection is not a uniqueness or priority certificate.

## Limitations
The proof assumes a fixed nondegenerate iid **finite-support**, **maximal-span lattice** law. The formula need not hold unchanged for nonlattice laws, triangular arrays, dependent inputs, or transport orders growing with sample size. A separate historical treatment of sharp arithmetic transport CLT constants may imply parts of this statement. Independent mathematical and priority validation have not been performed.

## References
- Y. Hafouta and J. Leppänen, *Optimal CLT error bounds in the second order Wasserstein metric via Stein's method for weakly dependent sequences*, arXiv:2610.30352v1 (posted 2026-10-21), https://arxiv.org/html/2610.30352v1 .
- S. G. Bobkov, *Berry–Esseen bounds and Edgeworth expansions in the central limit theorem for transport distances*, Probability Theory and Related Fields 170 (2018), 229–262, DOI:10.1007/s00440-017-0756-2; author preprint https://www-users.cse.umn.edu/~bobko001/preprints/CLT.for.W_p.7_After.revision.correction.pdf .
- J. E. Kolassa and P. McCullagh, *Edgeworth Series for Lattice Distributions*, Annals of Statistics 18 (1990), 981–985, DOI:10.1214/aos/1176347637 .
- F. Ouimet, *An improvement of Tusnády's inequality in the bulk*, arXiv:2010.15917v3 (the fair-binomial quantile setting).
