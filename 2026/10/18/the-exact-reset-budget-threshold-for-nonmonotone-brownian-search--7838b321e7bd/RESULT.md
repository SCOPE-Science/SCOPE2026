# The exact reset-budget threshold for nonmonotone Brownian search termination

## Finding
Consider one-dimensional Brownian search for an absorbing boundary at zero, with independent Poisson resets to the starting position and a finite allowance of reset events. The expected time to **either** hit the boundary or exhaust that allowance is strictly decreasing in the resetting rate when at most 20 resets are allowed, but is nonmonotone when at least 21 resets are allowed. The transition is universal: it is independent of the diffusion coefficient and the initial target distance.

Precisely, write \(D>0\) for the Brownian diffusivity (generator \(D\partial_{xx}\)), \(a>0\) for the starting and resetting position, \(r>0\) for the Poisson resetting rate, and \(\mu\geq0\) for an integer reset allowance. The process is killed upon reaching zero **or** upon the \((\mu+1)\)-st resetting alarm, whichever occurs first. Let \(T_\mu(r)\) be its mean killing time. Then
\[
\boxed{\quad T_\mu'(r)<0\ \text{for all }r>0\ \Longleftrightarrow\ 0\leq\mu\leq20.\quad}
\]
For every \(\mu\geq21\), \(T_\mu'(r)>0\) at \(r=(D/a^2)(\log7)^2\), while \(T_\mu'(r)<0\) for sufficiently small and sufficiently large positive \(r\). Thus it has at least one interior local minimum and one interior local maximum. No assertion of uniqueness of these extrema is needed or made.

## Assumptions and scope
The motion between alarms is ordinary Brownian diffusion on \([0,\infty)\) with absorption at zero. Reset alarms form an independent homogeneous Poisson process; the particle is returned instantaneously to \(a\) until the allowance is exhausted. The mean includes **both** successful absorption and termination by the reset budget. It is not the mean hitting time conditional on successful absorption. Parameters \(D,a,r\) are strictly positive and \(\mu\) is an arbitrary nonnegative integer.

Set \(n=\mu+1\), \(z=a\sqrt{r/D}\), and \(q=1-e^{-z}\). The exact formula is
\[
T_\mu(r)=\frac1r\sum_{j=1}^{n}q^j
=\frac{a^2}{D}\,\frac{S_n(q)}{z^2},\qquad S_n(q)=\sum_{j=1}^n q^j.
\]
This formula is already obtainable from standard resetting renewal theory and appears in an equivalent form in Bressloff's equation (5.37). The new result is the sharp integer boundary \(\mu=21\) for global monotonicity, with a complete exact inequality certificate.

## Proof
**1. Renewal identity.** If \(\tau\) is the Brownian first-hitting time of zero without resetting, its Laplace transform is \(\mathbb E[e^{-r\tau}]=e^{-z}\). The probability that a Poisson alarm precedes absorption during an attempt is \(q=1-e^{-z}\). Each attempt has mean duration \(\mathbb E[\min(\tau,E_r)]=q/r\), where \(E_r\) is an independent rate-\(r\) exponential time. Summing the durations of at most \(n\) attempts gives \(T_\mu(r)=r^{-1}\sum_{j=1}^nq^j\).

**2. Reduction to one critical integer.** Define
\[
H_n(z)=z(1-q)\frac{S_n'(q)}{S_n(q)}.
\]
Then \(z\,\partial_z\log (S_n(q)/z^2)=H_n(z)-2\). For fixed \(0<q<1\), the quantity \(qS_n'(q)/S_n(q)\) is the mean of \(j\) under weights proportional to \(q^j\), \(j=1,\ldots,n\). Appending the strictly larger value \(n+1\) increases this mean. Hence \(H_n(z)\) increases strictly with \(n\) for every \(z>0\). Also \(H_n(z)\to1\) as \(z\downarrow0\) and \(H_n(z)\to0\) as \(z\to\infty\), for each finite \(n\). Thus it suffices to prove \(H_{21}(z)<2\) everywhere and \(H_{22}(z)>2\) somewhere.

**3. Exact global bound for 21 attempts.** Put \(y=\tanh(z/2)\in(0,1)\), so that \(q=2y/(1+y)\) and \(z=2\sum_{j\ge0}y^{2j+1}/(2j+1)\). Write
\[
B(y)=y+\frac{y^3}{3}+\frac{y^5}{5}+\frac{y^7}{7},\qquad
U(y)=2\left(B(y)+\frac{y^9}{9(1-y^2)}\right).
\]
The exact series gives \(z<U(y)\) for \(0<y<1\). Define the integer-coefficient polynomials
\[
Q(y)=\sum_{j=1}^{21}(2y)^j(1+y)^{21-j},\quad
M(y)=\sum_{j=1}^{21}j(2y)^{j-1}(1+y)^{21-j}.
\]
Direct substitution yields \(H_{21}(z)=z(1-y)M(y)/Q(y)\). The inequality \(U(y)(1-y)M(y)<2Q(y)\) is equivalent to positivity of
\[
P(y)=(1-y^2)\bigl(Q(y)-(1-y)M(y)B(y)\bigr)
       -\frac{y^9}{9}(1-y)M(y).
\]
Exact rational polynomial division gives \(P(y)=y(1-y)F(y)\), where \(F\) has degree 28, \(F(0)=1\), and \(F(1)=183500800/3\). On each of the four intervals \([0,1/4]\), \([1/4,1/2]\), \([1/2,3/4]\), and \([3/4,1]\), the 29 Bernstein coefficients of \(F\) of degree 28 are **all strictly positive**. The exact smallest coefficient on these intervals, respectively, is
\[
1,\quad
\frac{98838903696272268379}{756604737398243328},\quad
\frac{286415793320830451119}{630503947831869440},\quad
\frac{231505758399776864059}{180143985094819840}.
\]
Every Bernstein basis function is nonnegative and their sum is one, so these rational inequalities prove \(F(y)>0\) throughout \([0,1]\). The accompanying standalone script reconstructs \(F\) algebraically and checks all 116 rational Bernstein coefficients, rather than relying on a plot or floating-point root search. Consequently \(H_{21}(z)<2\) at every finite positive \(z\), and by monotonicity in \(n\), \(H_n(z)<2\) for every \(n\le21\).

**4. Exact witness for 22 attempts.** Set \(y=3/4\), hence \(q=6/7\) and \(z=\log7\). Truncating the positive series after five terms gives the rigorous lower bound
\[
\log7>2\sum_{j=0}^4\frac{(3/4)^{2j+1}}{2j+1}
=\frac{8858481}{4587520}.
\]
At \(q=6/7\), exact rational arithmetic shows
\[
\frac{8858481}{4587520}(1-q)S_{22}'(q)-2S_{22}(q)
=\frac{641665092531749639153799}{17936382256795429334548480}>0.
\]
Thus \(H_{22}(\log7)>2\), and the strict increase in \(n\) gives the same for all \(n\ge22\). Since \(r\mapsto z\) is strictly increasing, this proves the derivative-sign classification. The negative derivative near both endpoints forces at least one interior local minimum and one interior local maximum whenever \(n\ge22\).

## Verification
Run `python verify.py` from the same directory as this file. The script requires Python 3.10 or later and SymPy 1.10 or later. It constructs the two exact polynomials for \(n=21\), verifies the factorization \(P=y(1-y)F\), checks all Bernstein coefficients using rational arithmetic on four explicitly stated intervals, and independently confirms the 22-attempt witness fraction. A separate numerical derivative cross-check tests the dimensionless mean against the differentiated formula at several values, but **all universal inequalities are certified by exact rational algebra and positive-series bounds**. The script was executed successfully on the packaged source.

## Relationship to prior work
Bressloff, *Truncated stochastically switching processes* (arXiv:2310.20502v1, 31 October 2023), analyzes the exact same Brownian half-line budget-exhaustion model. Section V.B, especially equation (5.37) and Figure 4, provides the full mean as a function of the resetting rate and observes qualitatively that smaller allowances give monotone decay whereas larger allowances yield an intermediate local minimum. It does **not** identify the smallest integer allowance at which monotonicity fails or supply a global finite-integer sign certificate. The renewal identity and exact mean are therefore prior work; the sharp threshold theorem and its finite algebraic proof are the contribution assessed here. General frequent-reset asymptotics in Linn and Lawley, *First-passage times under frequent stochastic resetting* (2023), do not address a fixed finite allowance, and do not determine this integer threshold.

## Limitations
The theorem concerns the **unconditional** duration to either outcome, not absorption-conditioned times or optimal probability of absorption. Nonmonotonicity means the derivative takes both signs; uniqueness, precise positions, or heights of local extrema are not proved. The integer 21 applies to one-dimensional Brownian half-line search with memoryless alarms, instant return to the same location, and exhaustion at the first disallowed alarm. It should not be transferred to other search processes or resource accounting rules without separate analysis. The exact-mean input is published; the new global parameter ordering and Bernstein certificate have not undergone independent audit.

## References
1. P. C. Bressloff, *Truncated stochastically switching processes*, arXiv:2310.20502v1 (31 October 2023), especially section V.B, equation (5.37), and Figure 4. https://arxiv.org/abs/2310.20502
2. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, Physical Review E 108, 024114 (2023). https://doi.org/10.1103/PhysRevE.108.024114
