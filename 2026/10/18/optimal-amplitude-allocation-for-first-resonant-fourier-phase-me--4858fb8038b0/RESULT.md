# Optimal amplitude allocation for first resonant Fourier-phase measurements
## Finding
Let \(n_0<n_1<n_2\) be distinct integers, \(g=\gcd(n_1-n_0,n_2-n_0)\), \(A=(n_1-n_0)/g\), and \(B=(n_2-n_0)/g\). Thus \(0<A<B\) and \(\gcd(A,B)=1\). For nonzero complex coefficients \(c_0,c_1,c_2\), put
\[
P_\theta(x)=c_0e^{2\pi in_0x}+c_1e^{i\theta/B}e^{2\pi in_1x}+c_2e^{2\pi in_2x},\qquad S=\sum_{j=0}^2|c_j|^2,
\]
and \(m_r(\theta)=S^{-r}\int_0^1|P_\theta(x)|^{2r}\,dx\) for integers \(r\ge1\).

All \(m_r\) with \(r<B\) are phase-independent. The first phase-sensitive moment has the exact form
\[
m_B(\theta)=D(c)+R(c)\cos(\theta-\phi),\qquad
\phi=\arg\bigl(\overline{c_1}^{\,B}c_0^{B-A}c_2^A\bigr),
\]
where \(D(c)\) is explicitly defined below and
\[
R(c)=\frac{2\binom BA|c_0|^{B-A}|c_1|^B|c_2|^A}{S^B}.
\]
Its **sharp, unconditional amplitude-allocation law** is
\[
\boxed{R(c)\le R_{A,B}^*:=\frac{2\binom BA}{2^B}\sqrt{\frac{(B-A)^{B-A}A^A}{B^B}}.}
\]
Equality holds exactly when
\[
\boxed{|c_0|^2:|c_1|^2:|c_2|^2=(B-A):B:A,}
\]
with arbitrary coefficient phases and overall nonzero scale. Thus the largest possible phase-to-phase moment range is exactly \(2R_{A,B}^*\), and it is **strictly larger** than the range for equal-magnitude coefficients.

With the three coefficient magnitudes known, the two controlled quadrature measurements determine the single intrinsic relative phase exactly:
\[
\bigl(m_B(0)-D(c)\bigr)+i\bigl(m_B(\pi/2)-D(c)\bigr)=R(c)e^{i\phi}.
\]
Consequently, the local Euclidean inverse condition number for recovering \(\phi\) from these two centered measurements is exactly \(1/R(c)\); its minimum over nonzero coefficients is \(1/R_{A,B}^*\), attained precisely by the same amplitude ratio. An additive Euclidean measurement perturbation of norm \(\delta<R(c)\) yields angular error at most \(\arcsin(\delta/R(c))\) for the argument estimator, with the bound geometrically sharp.

Furthermore \(R_{A,B}^*\le 2^{1-B/2}\) for every permitted pair; on the coprime balanced sequence \(B=2j+1\), \(A=j\),
\[
R_{j,2j+1}^*\sim2\sqrt{\frac{2}{\pi(2j+1)}}\,2^{-(2j+1)/2}\qquad(j\to\infty).
\]
Thus the optimal first-resonance phase sensitivity is exponentially small in the primitive outer frequency gap even after arbitrary amplitude reallocation.

## Assumptions and scope
Frequencies are integers, and the trigonometric moments use normalized Lebesgue measure on the unit circle. All three coefficients must be nonzero for phase recovery. The modulation \(e^{i\theta/B}\) is an explicitly *controlled change to the middle coefficient*, not a change in the unknown phase parameter. The coefficient magnitudes are assumed known in the two-measurement inversion statement, as is the normalized frequency triple. No noise distribution is assumed: the error bound is deterministic for Euclidean errors in the centered quadrature pair.

Only the first phase-sensitive **even** Fourier moment and its two controlled phase probes are optimized. No general noisy blind phase-retrieval theorem is asserted. Moment normalization uses \(S=\|P_\theta\|_2^2\), which does not depend on \(\theta\).

## Proof
By translation and division of frequencies by their common gap, phase collisions can be computed on \(\{0,A,B\}\). In \(P_\theta^r\), multinomial triples \(u=(u_0,u_1,u_2)\) with \(u_0+u_1+u_2=r\) occur at Fourier frequency \(Au_1+Bu_2\). Two such triples have the same frequency precisely when their difference is an integer multiple of \((-(B-A),B,-A)\), since \(\gcd(A,B)=1\). Every nonzero multiple has total positive multiplicity at least \(B\). Consequently there are no collisions for \(r<B\).

For \(r=B\) there is exactly one unordered colliding pair, namely \((0,B,0)\) and \((B-A,0,A)\); the corresponding multinomial coefficients are \(1\) and \(\binom BA\). Parseval for \(P_\theta^B\) therefore gives the displayed cosine, with
\[
D(c)=S^{-B}\sum_{u_0+u_1+u_2=B}\binom{B}{u_0,u_1,u_2}^{\!2}\prod_{j=0}^2|c_j|^{2u_j}.
\]
All terms of this baseline depend only on magnitudes. The single off-diagonal cross term is
\[
2S^{-B}\binom BA\operatorname{Re}\bigl(c_1^B\overline{c_0}^{\,B-A}\overline{c_2}^{\,A}e^{i\theta}\bigr),
\]
which proves both its phase and its amplitude exactly, because the displayed complex product has argument \(-\phi\).

Set \(x_j=|c_j|^2/S\). Then \(x_j>0\), \(\sum_jx_j=1\), and
\[
R(c)=2\binom BA x_0^{(B-A)/2}x_1^{B/2}x_2^{A/2}.
\]
The logarithm of the product is strictly concave on the positive simplex. Its Lagrange equations give the unique maximizer
\[
x_0=\frac{B-A}{2B},\quad x_1=\frac12,\quad x_2=\frac A{2B}.
\]
At any boundary point the product vanishes, so this is the global maximum. Substitution yields \(R_{A,B}^*\). The equality ratio is not \(1:1:1\), so equal-magnitude coefficients have strictly smaller phase contrast.

The quadrature identity follows by taking \(\theta=0\) and \(\theta=\pi/2\) in the same cosine. For a nonzero measurement vector of radius \(R(c)\), the derivative of its argument has Euclidean operator norm \(1/R(c)\). A perturbation of length less than \(R(c)\) makes at most the tangent angle \(\arcsin(\delta/R(c))\), which is attained by a tangent perturbation. This proves the stated inverse condition number and finite-error bound, and its sharp optimization follows from the amplitude maximum.

For the universal exponential bound, write \(t=A/B\). The binomial probability \(\binom BA t^A(1-t)^{B-A}\) is at most one, and \(\binom BA\le 2^B\). Therefore
\[
\frac{R_{A,B}^*}{2}=2^{-B}\sqrt{\binom BA\left(\binom BA t^A(1-t)^{B-A}\right)}\le2^{-B/2}.
\]
On \(B=2j+1\), \(A=j\), Stirling's formula gives \(\binom B A\sim 2^B\sqrt{2/(\pi B)}\) and \(t^A(1-t)^{B-A}\sim2^{-B}\), implying the asserted asymptotic. Since \(\gcd(j,2j+1)=1\), this family satisfies the primitive frequency hypothesis.

## Verification
Run the included standalone standard-library verifier by `python3 verify_first_resonance.py`. It independently enumerates multinomial Fourier collisions for every primitive pair \(0<A<B\le14\), for every moment order up to its first resonance; it checks a unique first collision, the exact cross coefficient, Gaussian-integer phase witnesses, and rational squares of the optimal cosine radii. It reports `VERIFY_OK collision_cases=614 B_max=14 exact_first_response_and_allocation`. The infinite-frequency, all-coefficient proof is the symbolic argument above; finite checks are corroborative rather than a substitute for it.

## Relationship to prior work
Pan, You, Wang, Zhou, and Chen (2026) resolve Mockenhaupt's three-term Hardy–Littlewood majorant conjecture for the special support \(\{0,1,N\}\) at non-even exponents, using resonance estimates; their result does not give the present three-amplitude first-even-moment optimization. The published result *Even phase moments recover the normalized geometry of a three-frequency spectrum* (2026) gives the all-even-moment resonance formula and the first response for **unimodular** coefficients, and expressly leaves non-unimodular magnitude optimization untreated. Its frequency-collision mechanism is prior work and is not claimed here. The new content is the sharp arbitrary-amplitude phase sensitivity, full optimizer rigidity, two-probe inverse stability, and exponential sensitivity law.

Ling, Geng, Li, and Wang (2026) determine average Nikolskii norm ratios for Gaussian random trigonometric polynomials. Their stochastic averaged objective neither implies the present extremal phase-contrast functional nor its optimizers. General phase-retrieval surveys concern different measurement families. The claim is elementary in ingredients and carefully restricted to the two-probe, three-frequency problem.

## Limitations
The magnitudes must be known to compute the centered baseline for inversion; this is not ordinary blind Fourier phase retrieval from a lone magnitude spectrum. Higher moments beyond the first resonance, zero coefficients, arbitrary numbers of frequencies, and noisy statistical estimators are not classified. An equivalent optimization may exist in specialized older phase-sensing literature under different terminology; no independence or comprehensive bibliographic uniqueness is asserted. The sharp angular bound refers to the argument estimator for deterministic Euclidean perturbations, not an optimal estimator under unspecified noise models.

## References
1. Guancheng Pan, Chengsong You, Hengyu Wang, Junwei Zhou, Yongchao Chen, *Mockenhaupt's Three-Term Hardy-Littlewood Majorant Conjecture*, arXiv:2609.09740v1, first posted 2026-09-09. Primary MSC 42A05.
2. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, publicly available result 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79/RESULT.md (full result and limitations inspected).
3. Yun Ling, Jiaxin Geng, Jiansong Li, Heping Wang, *Average Nikolskii factors for random trigonometric polynomials*, Journal of Inequalities and Applications 2026, article 78, published 2026-04-27, DOI:10.1186/s13660-026-03484-x.
4. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409v1 (2010).
