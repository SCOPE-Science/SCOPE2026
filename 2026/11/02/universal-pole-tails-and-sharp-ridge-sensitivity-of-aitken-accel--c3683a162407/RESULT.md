# Universal pole tails and sharp ridge sensitivity of Aitken-accelerated Gaussian trace means

## Finding
Let \(A\) be any nonzero real symmetric positive-semidefinite matrix and let \(g_1,\dots,g_4\) be independent standard Gaussian vectors. Put \(X_j=g_j^{\mathsf T}Ag_j\), \(\mu=\operatorname{tr} A\), and take the nested Gaussian trace means with cumulative probe budgets one, two, and four:
\[
M_1=X_1,\qquad M_2=(X_1+X_2)/2,\qquad M_4=(X_1+X_2+X_3+X_4)/4.
\]
Their Aitken \(\Delta^2\) transform is almost surely defined and equals
\[
T=M_1-\frac{(M_2-M_1)^2}{M_4-2M_2+M_1}
 = X_1-\frac{(X_2-X_1)^2}{X_1-3X_2+X_3+X_4}.
\]
Write \(f\) for the density of one \(X_j\), \(g=f*f\), and for \(r=2,4\) define the finite strictly positive constants
\[
J_r(A)=\int_0^\infty\!\int_0^{3y}(y-x)^r f(x)f(y)g(3y-x)\,dx\,dy.
\]
Then the *sharp two-sided pole-tail law* and absolute-moment threshold are
\[
\lim_{t\to\infty}t\,\Pr\{|T-\mu|>t\}=2J_2(A)>0,
\qquad \mathbb E|T-\mu|^q<\infty\ \Longleftrightarrow\ 0<q<1.
\]
For the smoothly denominator-regularized estimator, with any \(\delta>0\),
\[
T_\delta=X_1-\frac{(X_2-X_1)^2H}{H^2+\delta^2},
\qquad H=X_1-3X_2+X_3+X_4,
\]
the sharp small-ridge mean-squared-error law is
\[
\lim_{\delta\downarrow0}\delta\,\mathbb E[(T_\delta-\mu)^2]
   =\frac\pi2J_4(A)>0.
\]
For the smallest isotropic example with exponential Gaussian probe energies, \(A=I_2\), these become fully explicit:
\[
\Pr\{|T-2|>t\}\sim\frac{27}{128t},\qquad
\mathbb E[(T_\delta-2)^2]\sim\frac{243\pi}{512\delta}.
\]
These statements describe the Aitken transform of *nested Gaussian Monte Carlo means*; they do not describe a deterministic probing sequence.

## Assumptions and scope
The matrix dimension is any positive integer; \(A\) is fixed, real, symmetric, positive semidefinite and nonzero. Every Gaussian probe is independent with covariance identity, and the same first probes are reused when sample means are enlarged from one to two and four samples. No floating-point roundoff or stochastic stopping is assumed. All results concern one exactly specified extrapolated estimate. The ridge parameter \(\delta\) has the units of the trace estimate. Powers \(q\) are arbitrary positive reals.

## Proof
**1. Distribution and pole geometry.** If \(A\) has positive eigenvalues \(\lambda_1,\ldots,\lambda_k\), then \(X_j\) has the law of \(\sum_{i=1}^k\lambda_iG_i^2\). It has a strictly positive continuous density \(f\) on \((0,\infty)\). Standard gamma convolution, or scaling the simplex integral for the sum of independent \(\Gamma(1/2,2\lambda_i)\) variables, shows that \(f(x)\) is bounded by \(C x^{k/2-1}e^{-cx}\) for suitable positive constants \(C,c\), with the same kind of bound for \(g=f*f\), now having power \(k-1\). In particular, \(g\) is bounded on the positive half-line and the integrals \(J_2,J_4\) are finite. They are strictly positive because \(f\) and \(g\) are positive, and the integration region contains points with \(x\ne y\).

Direct substitution of the three means yields the displayed formula for \(T\). Conditional on \((X_1,X_2)=(x,y)\), put \(B=(y-x)^2\), \(c=3y-x\), and \(S=X_3+X_4\). The correction is \(B/(S-c)\), where \(S\) has density \(g\). Since \(S\) is continuous, the denominator vanishes with probability zero. For fixed \(x,y\) with \(B>0\) and \(c>0\), the event \(|x-\mu-B/(S-c)|>t\) probes the density in an interval of total length asymptotic to \(2B/t\) around \(S=c\). Therefore
\[
\lim_{t\to\infty}t\Pr\{|T-\mu|>t\mid X_1=x,X_2=y\}
=2B\,g(3y-x)\,\mathbf1_{\{3y>x\}}.
\]
For \(|x-\mu|\le t/2\), the event forces \(|S-c|<2B/t\); boundedness of \(g\) dominates \(t\) times its conditional probability by \(4B\|g\|_\infty\). The complementary \(x\)-tail has exponentially decaying probability, so integrating and passing to the limit is justified by the finite second moments of \(X_j\). This gives \(2J_2(A)\). Tail integration, \(\mathbb E|Z|^q=q\int_0^\infty t^{q-1}\Pr\{|Z|>t\}\,dt\), gives the claimed exact \(q=1\) moment boundary.

**2. Ridge law.** With \(H=S-c\), the squared correction in \(T_\delta\) is \(B^2H^2/(H^2+\delta^2)^2\). The rescaled kernel \(\delta H^2/(H^2+\delta^2)^2\) has total integral \(\pi/2\) and converges weakly to \((\pi/2)\) times a unit point mass at zero. Conditional integration against \(g(c+H)\), using boundedness of \(g\) and integrability of \(B^2\), gives
\[
\lim_{\delta\downarrow0}\delta\,\mathbb E\left[
\frac{B^2H^2}{(H^2+\delta^2)^2}\right]=\frac\pi2J_4(A).
\]
The \(X_1-\mu\) squared term disappears after multiplication by \(\delta\), and its cross term does too by Cauchy--Schwarz, since the correction's second moment is \(O(1/\delta)\). This proves the ridge limit.

**3. Exact two-dimensional constants.** For \(A=I_2\), one probe energy is chi-square with two degrees of freedom, hence \(f(x)=\lambda e^{-\lambda x}\), \(g(s)=\lambda^2s e^{-\lambda s}\) with \(\lambda=1/2\). Writing \(x=yu\),
\[
J_r=\lambda^4\int_0^\infty y^{r+2}e^{-4\lambda y}\,dy
 \int_0^3(1-u)^r(3-u)\,du.
\]
The two finite polynomial integrals are exactly \(9/4\) for \(r=2\) and \(27/10\) for \(r=4\). Since the first integral is \((r+2)!/(4\lambda)^{r+3}\),
\[
J_2=\frac{27}{512\lambda}=\frac{27}{256},\qquad
J_4=\frac{243}{2048\lambda^3}=\frac{243}{256}.
\]
Inserting these constants into parts 1 and 2 proves the explicit \(27/128\) tail coefficient and \(243\pi/512\) ridge-error coefficient.

## Verification
Execute `python3 verify.py` using only the Python standard library. The verifier reconstructs the nested-means identity, evaluates both polynomial integrals and gamma integrals in exact rational arithmetic, and checks the numerical large-threshold tail and small-ridge scaling on independently sampled exponential Gaussian probe energies using a fixed pseudorandom seed. The latter experiments are finite corroboration only; the preceding argument supplies the infinite-distribution proof.

## Relationship to prior work
Kalantzis, Kollias, Ubaru and Salonidis (ICASSP 2023) introduced Aitken \(\Delta^2\) acceleration of **deterministic hierarchical probing** trace estimates and compared that scheme with an unaccelerated randomized trace baseline. The Aitken identity and susceptibility to nearly equal first differences are classical; the paper does not state this stochastic-moment theorem, and this finding must not be interpreted as refuting its deterministic algorithm. Avron--Toledo's randomized trace-estimation analysis concerns the unextrapolated quadratic-form mean. Fika's 2018 chapter studies extrapolation approaches to inverse-trace approximation and mentions a stochastic route in its abstract; its full text was unavailable in the checked sources, so possible specialized prior coverage remains a stated publication-priority risk. The contribution assessed here is the general Gaussian-probe pole law, its exact absolute-moment threshold, its sharp smooth-ridge asymptotic, and the two-dimensional closed constants in a naturally nested doubling-budget scheme.

## Limitations
No claim is made that a particular deterministic probing method is unstable, or that every form of stochastic sequence acceleration has these tails. The theorem assumes independent Gaussian quadratic-form probes of a fixed nonzero PSD matrix and the particular nested budget schedule \(1,2,4\). It does not cover Rademacher probing or correlated/adaptively selected probes, and the ridge limit is not a globally optimal choice of \(\delta\). The result establishes an exact law for one finite-batch transform, not its large-batch consistency or practical wall-clock performance. Independent publication-priority assessment remains outstanding.

## References
1. V. Kalantzis, G. Kollias, S. Ubaru and T. Salonidis, *Accelerating Matrix Trace Estimation by Aitken's \(\Delta^2\) Process*, ICASSP 2023, DOI 10.1109/ICASSP49357.2023.10095081; author open-access text: https://vkalantzi.github.io/papers/icassp12023.pdf (public conference date 2023-06-04).
2. H. Avron and S. Toledo, *Randomized Algorithms for Estimating the Trace of an Implicit Symmetric Positive Semi-Definite Matrix*, J. ACM 58 (2011), DOI 10.1145/1944345.1944349.
3. P. Fika, *Extrapolation Methods for Estimating the Trace of the Matrix Inverse*, in *Modern Discrete Mathematics and Analysis* (2018), DOI 10.1007/978-3-319-74325-7_7; abstract and bibliographic description consulted, full text not verified.
4. D. Buoso, A. Karapiperi and S. Pozza, *Generalizations of Aitken's Process for a Certain Class of Sequences*, Applied Numerical Mathematics 90 (2015), 38--54, DOI 10.1016/j.apnum.2014.12.003.
