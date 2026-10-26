# Sharp phase-ordering coefficients for periodically breathing dyadic holes

## Finding
Let \(q\ge2\) and \(a=(a_0,\ldots,a_{q-1})\) be a permutation of \(0,1,\ldots,q-1\). For \(m\ge1\), the doubling map \(T(x)=2x\bmod 1\) loses a point at time \(t\) if \(T^t(x)\in H_t=[0,2^{-(m+a_{t\bmod q})})\). Define its exponential Lebesgue escape rate by
\[
\gamma_m(a)=-\lim_{N\to\infty}\frac1N\log\operatorname{Leb}\{x\in[0,1):T^t(x)\notin H_t,\ 0\le t<N\}.
\]
Define the cyclic erosion profile and coefficient
\[
 b_s(a)=\min_{0\le k<q}\big(k+a_{(s+k)\bmod q}\big),\qquad
 C(a)=\frac1{2q}\sum_{s=0}^{q-1}2^{-b_s(a)}.
\]
Then for every fixed \(q,a\), as \(m\to\infty\) through the integers,
\[
 \gamma_m(a)=2^{-m}C(a)+O_{q,a}(m4^{-m}).
\]
Among all \(q!\) schedules, the **unique minimizer up to cyclic rotation** is the reverse staircase \((0,q-1,q-2,\ldots,1)\), with
\[
 C_{\min}(q)=\frac{1-2^{-q}}q.
\]
The exact maximum coefficient and number of maximizers up to cyclic rotation for \(2\le q\le8\) are:

| \(q\) | \(C_{\max}(q)\) | Maximizing cyclic schedules |
|---|---|---:|
| 2 | \(3/8\) | 1 |
| 3 | \(1/3\) | 1 |
| 4 | \(9/32\) | 4 |
| 5 | \(1/4\) | 10 |
| 6 | \(11/48\) | 12 |
| 7 | \(23/112\) | 144 |
| 8 | \(3/16\) | 864 |

Equivalently, if \(M_q=2qC_{\max}(q)\), then \(M_q=(q+5)/4\) for \(3\le q\le6\), but \(M_7=23/8<3\) and \(M_8=3<13/4\). Thus the initially linear extremal pattern stops at the first seven-phase case. At \(q=7\), a maximizing example is \((0,2,3,1,4,5,6)\), whereas the reverse staircase uniquely minimizes the coefficient.

## Assumptions and scope
The holes use the binary expansion outside the null set of dyadic rationals. The order \(a\) is fixed as \(m\to\infty\); no uniform claim is made when \(q\) grows with \(m\). Each permutation is identified modulo cyclic shifts because a shift merely changes the time origin. The escape rate is the infinite-time limit for each fixed finite \(m\), followed by the small-hole limit. This result concerns nested holes at the repelling fixed point \(0\), not arbitrary moving-hole locations.

## Proof
**1. Exact reduction to phase-dependent zero runs.** In binary coordinates \(T\) shifts the bit string left. Suppose a maximal zero run begins at time \(s\) after a \(1\), and has length \(\ell\). The hole at time \(s+k\) captures the orbit iff \(\ell\ge m+k+a_{(s+k)\bmod q}\). The minimum over \(k\ge0\) occurs among \(0\le k<q\), because adding an entire period adds \(q>0\). Therefore the run is safe exactly when \(\ell<m+b_{s\bmod q}\). This is a lossless conversion, not a rare-event approximation.

**2. Finite renewal matrix and its Perron singularity.** Under Lebesgue measure binary bits are independent fair bits. A complete run of \(\ell\) zeros followed by a \(1\) has probability \(2^{-(\ell+1)}\) and consumes \(\ell+1\) units of time. Write
\[
 K_m(z)_{s,t}=\sum_{\substack{0\le\ell<m+b_s\\t\equiv s+\ell+1\pmod q}}(z/2)^{\ell+1}.
\]
For sufficiently large \(m\), its nonnegative phase graph is primitive. Its row sum at \(z=1\) is \(1-2^{-(m+b_s)}\). Thus \(\rho(K_m(1))<1\), while \(\rho(K_m(z))\) grows strictly through \(1\) at a unique \(z=z_m>1\). Since the generating function for successive complete safe runs is \((I-K_m(z))^{-1}\), and initial/terminal partial runs contribute only positive polynomials of degree at most \(m+q-1\), the Perron singularity controls the finite-state survivor count: \(\gamma_m(a)=\log z_m\). The same equality follows directly by constructing the run-length finite automaton and eliminating its transient run-age states. Positive coefficients and the unit-length return prevent dominant cancellation.

**3. Controlled small-hole perturbation.** Let \(P\) cyclically increment the phase. Removing the run cap gives
\[
 K_\infty(z)=\sum_{\ell\ge0}(z/2)^{\ell+1}P^{\ell+1}=\frac z2 P(I-\tfrac z2P)^{-1}.
\]
For real \(z\) near \(1\), its simple Perron eigenvalue is \(z/(2-z)\), with normalized left eigenvector uniform and right eigenvector all ones. At \(z=1\), the omitted row mass is \(2^{-(m+b_s)}\). Standard finite-dimensional perturbation at this simple eigenvalue (the other eigenvalues remain separated for fixed \(q\)) gives
\[
 \rho(K_m(1))=1-\frac1q\sum_s2^{-(m+b_s)}+O_q(4^{-m}).
\]
Also \(\partial_z\rho(K_m(z))|_{z=1}=2+O_{q,a}(m2^{-m})\). The implicit root expansion yields
\[
 z_m-1=\frac{2^{-m}}{2q}\sum_s2^{-b_s}+O_{q,a}(m4^{-m}),
\]
whence the stated expansion for \(\log z_m\).

**4. All-period sharp minimum and uniqueness.** Since \(b_s\le a_s\),
\[
 \sum_s2^{-b_s}\ge\sum_s2^{-a_s}=\sum_{j=0}^{q-1}2^{-j}=2(1-2^{-q}).
\]
Equality holds exactly when \(b_s=a_s\) for every \(s\), equivalent to \(a_s\le1+a_{s+1}\) for each cyclic index. Starting at the unique maximum entry \(q-1\), the next \(q-1\) entries must decrease to \(0\), in steps of size at most one. Each step is therefore exactly minus one, forcing the reverse staircase. That schedule satisfies all required inequalities.

**5. Exhaustive sharp finite-period maxima.** Every cyclic class of permutations has exactly one representative with \(a_0=0\), leaving \((q-1)!\) representatives. For each such tuple the coefficient is an exact dyadic rational obtained by the stated length-\(q\) minimum and sum. The standalone `verify.py` independently computes the minimum by (i) scanning \(2q\) offsets and (ii) iterating the cyclic one-step min-plus recurrence to its fixed point; it asserts agreement, exhausts all \((q-1)!\) representatives for \(2\le q\le8\), computes maxima using Python rational arithmetic, and checks the exact maximizing counts. The output `VERIFY_OK` constitutes a reproducible finite exhaustive certificate for these finite-period claims. There is no numerical extrapolation of the finite maxima to larger \(q\).

## Verification
Execute `python verify.py` with Python 3; only the standard library is needed. The output checks all exact maxima and counts, including \(q=7\) and \(q=8\), and checks the general-minimum formula for each enumerated period. The infinite-\(m\) estimate and all-\(q\) minimum are proved analytically above, not inferred from the finite checker. Independent floating-point calculations of Perron roots for several three-phase schedules and \(m=6,9,12,15\) showed convergence to the stated coefficients; those calculations are corroborative only.

## Relationship to prior work
Livorati, Georgiou, Dettmann and Leonel introduced and numerically analyzed periodically varying holes for the doubling map and emphasized short-orbit overlap effects. Poo and Marcus studied the *same class of periodic maximum-run constraints* from coding theory, gave a canonical tight-vector reduction and general characteristic-matrix methods, and ordered the tight constraints through period four. Their construction makes the underlying exact capacities computable, so it is a powerful possible route to this asymptotic limit; no independence from that machinery is asserted. The present claim supplies an explicit rare-hole leading coefficient, a proof of its uniform-in-time renewal interpretation, the all-period extremal minimum with uniqueness, and exact ordering extrema/counts in the first subsequent periods five through eight. The 2011 periodic-finite-type formalism likewise gives general shift-capacity computations but does not in its inspected introductory/algorithmic material specify this optimized rare-hole coefficient. These structural reductions and optimization statements, not merely the existence of a finite adjacency matrix, are the asserted additions.

## Limitations
The finite extremal maxima are certified only for \(2\le q\le8\); no formula for the maximum for arbitrary \(q\) is claimed. For a fixed finite \(m\), schedules with the same leading coefficient may have different lower-order escape rates; the table is an asymptotic classification, not an exact finite-hole ordering. The general TMTR capacity theory could permit derivations of related claims not located in the inspected material; independent examination remains warranted. Full PDF text for one primary coding-theory source was not directly retrieved, but its complete multi-page HTML transcription, including definitions, tightness propositions, characteristic-equation discussion and capacity-ordering section, was inspected; mathematical equations lost in transcription are a residual originality limitation.

## References
1. A. L. P. Livorati, O. Georgiou, C. P. Dettmann and E. D. Leonel, “Escape through a time-dependent hole in the doubling map,” arXiv:1312.7030 (first publicly posted 2013-12-25); *Physical Review E* 89 (2014), 052913. https://arxiv.org/abs/1312.7030
2. T. L. Poo and B. H. Marcus, “Time-Varying Maximum Transition Run Constraints,” *IEEE Trans. Information Theory* 52 (2006), 4464–4480, DOI 10.1109/TIT.2006.881706.
3. M.-P. Béal, M. Crochemore, B. E. Moision and P. H. Siegel, “Periodic-Finite-Type Shift Spaces,” *IEEE Trans. Information Theory* 57 (2011), 3677–3691, DOI 10.1109/TIT.2011.2143910. https://cmrr-star.ucsd.edu/static/pubs/periodic_finite_type.pdf
4. A. Ferguson and M. Pollicott, “Escape rates for Gibbs measures,” arXiv:1009.0086 (2010). https://arxiv.org/abs/1009.0086
