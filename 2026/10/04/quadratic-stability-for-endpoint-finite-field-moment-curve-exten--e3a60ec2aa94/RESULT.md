# Quadratic stability for endpoint finite-field moment-curve extension
## Finding
Let \(d\ge 2\), let \(q=p^n\) with prime \(p>d\), and let
\[\Gamma=\{(t,t^2,\ldots,t^d):t\in\mathbb F_q\}\subset\mathbb F_q^d.\]
Let \(\sigma\) be normalized counting measure on \(\Gamma\). For a probability vector \(\theta\) on a \(q\)-point set, let \(T=(T_1,\ldots,T_d)\) be i.i.d. with law \(\theta\), and let \(M(T)\) be the number of distinct rearrangements of the sample. Put
\[F_d(\theta)=\mathbb E_\theta[M(T)],\qquad u=(1/q,\ldots,1/q),\qquad A=F_d(u).\]
Then
\[A-F_d(\theta)\ge \frac{d(d-1)}2\|\theta-u\|_2^2\tag{1}\]
for every probability vector \(\theta\). For \(d=2\), equality holds in (1) for every \(\theta\).

Using the exact reduction of arXiv:2609.29882v1, (1) gives the Fourier-extension remainder: every nonzero \(f:\Gamma\to\mathbb C\) satisfies
\[A\|f\|_{L^2(\sigma)}^{2d}-\|(f\sigma)^\vee\|_{L^{2d}(\mathbb F_q^d)}^{2d}\ge \frac{d(d-1)}{2q}\|f\|_{L^2(\sigma)}^{2d-4}\big\||f|^2-\|f\|_{L^2(\sigma)}^2\big\|_{L^2(\sigma)}^2.\tag{2}\]
Thus the sharp endpoint deficit quantitatively controls failure of constant modulus. No optimality of the coefficient in (1) or (2) is asserted when \(d>2\).

## Assumptions and scope
The field has order \(q=p^n\) and characteristic \(p>d\), exactly as in the endpoint moment-curve theorem used below. The \(L^2(\sigma)\) norm is with normalized counting measure on \(\Gamma\), while the target \(L^{2d}(\mathbb F_q^d)\) norm uses counting measure. The probabilistic inequality (1) itself needs only a finite alphabet of size \(q\); the field enters only in transferring it to (2).

The claim concerns amplitude stability. At this endpoint, the source identity makes the extension norm depend only on \(|f|\), so no phase rigidity is claimed or needed.

## Proof
Fix two letters \(a,b\) and write \(m=\theta_a+\theta_b\). Let \(\theta'\) be obtained by replacing \(\theta_a,\theta_b\) by their average. If \(m=0\), then \(\theta_a=\theta_b=0\) and the desired local estimate is trivial. Assume \(m>0\), put \(\rho=\theta_a/m\), merge \(a,b\) into one symbol, and let \(S\) be its multiplicity in the projected sample.

The exact factorization in arXiv:2609.29882v1 gives
\[F_d(\theta')-F_d(\theta)=\mathbb E\!\left[M(\widetilde T)\big(H_S(1/2)-H_S(\rho)\big)\right],\tag{3}\]
where
\[H_s(\rho)=\sum_{j=0}^{\lfloor s/2\rfloor}\binom{s}{2j}\binom{2j}{j}\big(\rho(1-\rho)\big)^j.\tag{4}\]
All terms of (4) beyond the constant term have nonnegative coefficients. Retaining only \(j=1\), whose coefficient is \(s(s-1)\), yields
\[H_s(1/2)-H_s(\rho)\ge s(s-1)\left(\frac14-\rho(1-\rho)\right)=s(s-1)(\rho-1/2)^2.\tag{5}\]
Since \(M(\widetilde T)\ge1\) and \(S\sim\operatorname{Bin}(d,m)\), equations (3)--(5) imply
\[F_d(\theta')-F_d(\theta)\ge (\rho-1/2)^2\mathbb E[S(S-1)]=\frac{d(d-1)}4(\theta_a-\theta_b)^2.\tag{6}\]

Now repeatedly choose a maximum and a minimum coordinate and average that pair. For
\[V(\theta)=\|\theta-u\|_2^2,\]
one such averaging changes \(V\) by
\[V(\theta)-V(\theta')=\frac12(\theta_a-\theta_b)^2.\tag{7}\]
The sum of the squared max--min gaps is finite by (7), so those gaps tend to zero. The coordinate mean remains \(1/q\), hence the iterates converge to \(u\). Since \(F_d\) is a polynomial, it is continuous. Summing (6) and using (7) therefore gives
\[A-F_d(\theta)\ge \frac{d(d-1)}4\sum_k(\theta_{a_k}-\theta_{b_k})^2=\frac{d(d-1)}2V(\theta),\]
which proves (1). For \(d=2\), the exact identity \(F_2(\theta)=2-\sum_j\theta_j^2\) gives equality in (1).

For (2), put \(N=\|f\|_{L^2(\sigma)}^2\) and, for \(f\ne0\), define
\[\theta_t=\frac{|f(\gamma(t))|^2}{qN}.\]
The source's exact fiber identity is
\[\|(f\sigma)^\vee\|_{2d}^{2d}=N^dF_d(\theta).\tag{8}\]
Moreover,
\[\|\theta-u\|_2^2=\frac1{qN^2}\big\||f|^2-N\big\|_{L^2(\sigma)}^2.\tag{9}\]
Multiplying (1) by \(N^d\) and substituting (8)--(9) proves (2). The zero function satisfies the endpoint inequality trivially and is excluded only to avoid the normalization in (9).

## Verification
The proof above is symbolic and valid for all stated \(d,q\). A standalone exact-rational checker independently enumerates the rearrangement expectation for \(2\le q\le4\), \(2\le d\le5\), and a deterministic collection of boundary, sparse, uniform, and nonuniform rational probability vectors. It checks both the one-step estimate (6) and the global remainder (1), and checks exact equality for every tested case with \(d=2\). The replay output is `VERIFY_OK global_cases=68 pair_cases=236`.

The finite checks are sanity checks only; they are not used to justify the infinite theorem. The critical proof inputs are the source identities (3), (4), and (8), together with the elementary factorial moment \(\mathbb E[S(S-1)]=d(d-1)m^2\) and the exact variance drop (7).

## Relationship to prior work
Biswas, Carneiro, Flock, Madrid, Oliveira e Silva, Stovall, and Tautges prove that \(F_d\) is uniquely maximized by the uniform distribution and identify this with the sharp endpoint extension inequality. Their two-point proof gives the exact formula (3) and the nonnegative-coefficient expansion (4), but uses them to establish monotonicity and strictness, not the metric remainder (1). Their Remark 14 also notes that qualitative Schur concavity follows from Peskir's multinomial-transfer argument based on Rinott.

Gonçalves subsequently proves a stronger component-wise majorization statement for permutation matches and recovers the uniform-maximizer theorem as a corollary. Its statement and proof provide a broader qualitative comparison but do not state a quadratic distance-to-uniform remainder. The present estimate extracts the first nonconstant coefficient of (4) and telescopes the resulting local gain against the exact Euclidean variance drop.

The closest prior published-finding database matches found under searches for finite-field moment-curve stability and quantitative Schur concavity concern different objects, including weighted extension for real monomial curves and a variance-stability bound for a product-profile scale. Neither contains or implies (1) or (2).

## Limitations
For \(d>2\), the coefficient \(d(d-1)/2\) is a certified universal coefficient, not claimed to be best possible. The argument measures squared-amplitude nonuniformity only and gives no phase information. It relies on the endpoint identity special to the finite-field moment curve and does not transfer automatically to Euclidean restriction or to other finite-field surfaces.

A residual literature risk remains that an equivalent strong-Schur-concavity remainder for this exact multinomial functional appears under different notation in older majorization literature. The inspected Peskir theorem establishes qualitative Schur concavity through Rinott's transfer theorem; targeted searches did not locate the quadratic remainder stated here.

## References
1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1, 24 September 2026.
2. F. Gonçalves, *A component-wise inequality for permutation matches*, arXiv:2609.31979v1, 25 September 2026.
3. G. Peskir, *Best constants in Kahane--Khintchine inequalities for complex Steinhaus functions*, Proc. Amer. Math. Soc. 123 (1995), 3101--3111.
4. Y. Rinott, *Multivariate majorization and rearrangement inequalities with some applications to probability and statistics*, Israel J. Math. 15 (1973), 60--77.
