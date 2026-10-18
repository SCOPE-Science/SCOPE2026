# Boundary thresholds and exponential saturation for two-bond weighted shifts

## Finding
For real \(a,b>1\), integer \(k\ge1\), and the unilateral weighted shift \(S_k(a,b)\) defined below, put \(r_k=w(S_k(a,b))\) and \(s=a^2+b^2-1\). There is an exact transition
\[
r_k>1\quad\Longleftrightarrow\quad b^2+\frac{k}{k+1}a^2>2.
\]
Otherwise \(r_k=1\). Moving the two neighboring exceptional weights one site away from the boundary cannot decrease numerical radius; it increases it strictly as soon as the destination radius exceeds \(1\). Moreover,
\[
r_k\nearrow r_\infty=\frac12\left(\sqrt{s}+\frac1{\sqrt{s}}\right),\qquad
\lim_{k\to\infty}s^{k+1/2}(r_\infty-r_k)=\frac{a^2(s-1)^2}{4s^2}>0.
\]
The equality regime in the transition is a spectral-edge resonance, not a square-summable eigenvector.

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb N;\mathbb C)\), with standard basis \((e_j)_{j\ge1}\). For integer \(k\ge1\), define \(S_k(a,b)e_j=w_je_{j+1}\), where \(w_k=a\), \(w_{k+1}=b\), and \(w_j=1\) otherwise. The exceptional weights \(a,b\) are fixed real numbers strictly larger than \(1\). The numerical radius is \(w(T)=\sup_{\|x\|_2=1}|\langle Tx,x\rangle|\). All limit statements hold with \(a,b\) fixed and \(k\to\infty\), not uniformly as either weight approaches \(1\). The orientation is significant: \(a\) is nearer the left boundary.

## Proof
**Step 1: spectral reduction.** Let \(J_k=S_k+S_k^*\), a self-adjoint Jacobi operator whose consecutive off-diagonal entries are \(w_j\). Diagonal phase conjugation makes every rotated Hermitian part of \(S_k\) unitarily equivalent to \(J_k/2\); the alternating-sign unitary makes \(J_k\) unitarily equivalent to \(-J_k\). Consequently \(r_k=\sup\sigma(J_k)/2\). The difference between \(J_k\) and the free half-line adjacency matrix (all weights \(1\)) has finite rank, so \(\sigma_{\mathrm{ess}}(J_k)=[-2,2]\). Thus \(r_k\ge1\); any strict inequality comes from an eigenvalue \(\lambda>2\).

**Step 2: the exact bound-state equation.** For \(\lambda>2\), put
\[
t=t(\lambda)=\frac{\lambda-\sqrt{\lambda^2-4}}2\in(0,1),\qquad \lambda=t+t^{-1}.
\]
Write \(p_0(\lambda)=1\), \(p_1(\lambda)=\lambda\), and \(p_{j+1}=\lambda p_j-p_{j-1}\). These are positive on \((2,\infty)\). The left Dirichlet recurrence for a putative eigenvector has \(x_j=p_{j-1}(\lambda)x_1\) for \(1\le j\le k\). Matching the first exceptional edge gives \(a x_{k+1}=p_k(\lambda)x_1\). The square-summable right tail has \(x_{k+2}=bt x_{k+1}\) and \(x_{k+2+m}=t^m x_{k+2}\) for \(m\ge0\). The equation at site \(k+1\) is equivalent to
\[
F_k(\lambda):=\lambda-a^2\frac{p_{k-1}(\lambda)}{p_k(\lambda)}-b^2t(\lambda)=0.\tag{1}
\]
Conversely, a solution of (1) yields the displayed nonzero positive \(\ell^2\)-eigenvector. The ratio of Dirichlet polynomials is
\[
\frac{p_{k-1}(\lambda)}{p_k(\lambda)}
=t\frac{1-t^{2k}}{1-t^{2k+2}},
\]
so the exact equation can also be written
\[
F_k(\lambda)=\lambda-(a^2+b^2)t+
\frac{a^2t^{2k+1}(1-t^2)}{1-t^{2k+2}}.\tag{2}
\]

**Step 3: threshold and location monotonicity.** For fixed \(\lambda>2\), the ratio \(p_{k-1}/p_k\) is the last diagonal resolvent entry of the \(k\)-vertex free path. It is strictly decreasing in \(\lambda\) because differentiating the resolvent gives the negative of a positive quadratic form; \(t(\lambda)\) is also strictly decreasing. Therefore \(F_k(\lambda)\) strictly increases from its finite edge value to \(+\infty\). At \(\lambda\downarrow2\), the elementary limits \(p_j(2)=j+1\) and \(t(2)=1\) give
\[
F_k(2^+)=2-\frac{k}{k+1}a^2-b^2.
\]
There is exactly one eigenvalue above \(2\) if and only if this quantity is negative, proving the transition. If it is zero, the associated right-tail solution has \(t=1\), hence is not square summable and there is no eigenvalue above the essential spectrum. The ratio \(p_{k-1}/p_k\) increases strictly with \(k\) at fixed \(\lambda>2\): its recurrence \(q_{k+1}=1/(\lambda-q_k)\), started at \(q_1=1/\lambda\), converges monotonically upward to \(t\). Hence \(F_{k+1}(\lambda)<F_k(\lambda)\). The root at the new location is strictly larger whenever it is above \(2\); the possible initial equality interval occurs only at the essential edge. This proves the monotonicity assertion, including the transition case.

**Step 4: limit and exact leading correction.** Let \(s=a^2+b^2-1>1\). On compact subintervals of \((2,\infty)\), the exponentially small last term in (2), together with its derivative, tends uniformly to zero. Therefore \(F_k\) converges to \(G(\lambda)=\lambda-(s+1)t(\lambda)\), whose unique zero above \(2\) has \(t_*=s^{-1/2}\) and
\[
\lambda_*=t_*+t_*^{-1}=\sqrt{s}+\frac1{\sqrt{s}}.
\]
The roots \(\lambda_k=2r_k\) eventually exist, are strictly increasing, and are trapped between any sufficiently close test points on opposite sides of \(\lambda_*\). Thus \(\lambda_k\to\lambda_*\). Equation (2) yields
\[
F_k(\lambda_*)=\frac{a^2s^{-(k+1/2)}(1-s^{-1})}{1-s^{-(k+1)}}.
\]
Also \(t'(\lambda_*)=-1/(s-1)\), and hence
\[
G'(\lambda_*)=\frac{2s}{s-1}.
\]
Applying the mean-value theorem between \(\lambda_k\) and \(\lambda_*\), together with locally uniform convergence of \(F_k'\), gives
\[
\lim_{k\to\infty}s^{k+1/2}(\lambda_*-\lambda_k)
=\frac{a^2(s-1)^2}{2s^2}.
\]
Dividing by \(2\) proves the asserted numerical-radius correction. This argument establishes an infinite-index limit rather than extrapolating a finite computation.

## Verification
The standalone standard-library program `verify.py` checks the Dirichlet-polynomial/decaying-tail identity with exact rational arithmetic at 216 parameter instances. It also checks the transition and monotonicity formulas and compares the asymptotic coefficient against numerically bracketed roots. A separately constructed exact example has \(k=1\), \(a=b=5/3\), \(t=1/2\), \(\lambda=5/2\), hence numerical radius \(5/4\); substitution makes (1) identically zero. The program provides consistency checks only. The all-dimension result and infinite limit follow from the analytic proof above, not from finite enumeration.

## Relationship to prior work
Chien, Nakazato, Undrakh, and Vandanjav's 2015 work on determinantal polynomials (DOI `10.1080/03081087.2014.1003528`, online January 21, 2015) treats numerical radii of weighted shifts through algebraic characteristic tools. Undrakh, Nakazato, Vandanjav, and Chien's 2015 paper (DOI `10.13001/1081-3810.2821`, especially Theorems 3.1–3.3 and examples after them) gives a finite-perturbation spectral criterion and general polynomial relation, including basic boundary special cases. It does not state the two-bond location-dependent edge threshold, the monotone boundary response, or its precise exponential leading coefficient. The present result is a refined consequence of the shared Jacobi recurrence, not an independent rediscovery of the characteristic polynomial. Vandanjav and Undrakh's 2014 article considers finite matrices with adjacent enhanced weights, not the present half-line two-bond bound-state phase diagram. Classic finite-rank Jacobi theory provides the general spectral framework; possible derivation from another unexamined general source is an acknowledged originality risk.

## Limitations
The two exceptional bonds must be adjacent, positive, and strictly heavier than the remaining bonds. The exponential coefficient is for fixed parameters as the exceptional pair moves away from the boundary; no uniform weak-defect assertion is made. No formula is claimed for arbitrary perturbation patterns, nonadjacent defects, or complex weights. The unavailable full text of the 2015 determinantal-polynomial article, and the possibility of a general Jacobi result already implying the precise boundary expansion, remain bibliographic limitations.

## References
1. M.-T. Chien, H. Nakazato, B. Undrakh, and A. Vandanjav, *Determinantal polynomials of a weighted shift operator*, Linear and Multilinear Algebra 64 (2016), 2–13, DOI: `10.1080/03081087.2014.1003528`; first online January 21, 2015.
2. B. Undrakh, H. Nakazato, A. Vandanjav, and M.-T. Chien, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra 30 (2015), 944–963, DOI: `10.13001/1081-3810.2821`.
3. A. Vandanjav and B. Undrakh, *On the numerical range of some weighted shift matrices and operators*, Linear Algebra and Its Applications 449 (2014), 76–88, DOI: `10.1016/j.laa.2014.02.018`.
4. M.-T. Chien and H.-A. Sheu, *The numerical radii of weighted shift matrices and operators*, Operators and Matrices 7 (2013), 197–204, DOI: `10.7153/oam-07-11`.
