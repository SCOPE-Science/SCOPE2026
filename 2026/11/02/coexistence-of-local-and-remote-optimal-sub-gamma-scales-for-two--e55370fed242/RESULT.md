# Coexistence of local and remote optimal sub-gamma scales for two-point Poisson jumps

## Finding
Let \(N\sim\operatorname{Poisson}(\lambda)\), with \(\lambda>0\), and let \(J_i\) be independent, also independent of \(N\), with \(\Pr(J_i=5)=p\) and \(\Pr(J_i=1)=1-p\). Define the centered compound-Poisson variable \(X_p=\sum_{i=1}^{N}J_i-\lambda(1+4p)\) and fix the variance proxy at its true variance \(V_p=\lambda(1+24p)\). Its optimal right-sided sub-gamma scale is
\[
 c_*(p)=\inf\left\{c>0:\log\mathbb E e^{tX_p}\le\frac{V_pt^2}{2(1-ct)}\ \text{for all }0\le t<1/c\right\}.
\]
Set \(m_p=(1+124p)/[3(1+24p)]\), its third-cumulant lower bound. **There exists \(p_*\in(0,10^{-4})\)** such that (i) \(c_*(p)=m_p\) for every sufficiently small \(p\ge0\); (ii) \(c_*(10^{-4})>m_{10^{-4}}\), even though the variational objective is strictly decreasing immediately to the right of zero for all \(0\le p\le10^{-4}\); and (iii) \(c_*(p_*)=m_{p_*}\), with its global variational supremum attained both at the limiting argument \(t=0\) and at some strictly positive finite \(t_*>0\). Thus the globally optimal argument jumps from a locally stable endpoint to a separated interior maximizer along parameters immediately above \(p_*\). No uniqueness or numerical value for \(p_*\) is asserted.

## Assumptions and scope
The intensity \(\lambda\) is arbitrary and positive; \(p\) ranges only over \([0,10^{-4}]\). The bound is right-sided, the quadratic proxy is \(V_p\) rather than a freely enlarged variance proxy, and the jump values are exactly one and five. All jump MGFs are entire. Define
\[
M_p(t)=\frac{2\{(1-p)(e^t-1-t)+p(e^{5t}-1-5t)\}}{(1+24p)t^2}\quad(t>0),\qquad M_p(0)=1,
\]
\[
\Phi_p(t)=\frac{1-M_p(t)^{-1}}t\quad(t>0),\qquad\Phi_p(0)=m_p.
\]
The exact optimal-scale variational formula from Chen (2026) is \(c_*(p)=\sup_{t\ge0}\Phi_p(t)\); it also follows by algebra from the sub-gamma inequality. The argument \(t=0\) means a limiting Taylor coefficient, not a positive Laplace argument.

## Proof
**1. Transform and origin expansion.** The compound-Poisson cumulant generating function is \(\lambda\{\mathbb E(e^{tJ})-1-t\mathbb E J\}=V_pt^2M_p(t)/2\). Its coefficients about zero satisfy
\[
M_p(t)=1+a_1(p)t+a_2(p)t^2+O(t^3),\quad a_1(p)=m_p,\quad a_2(p)=\frac{1+624p}{12(1+24p)}.
\]
It follows that
\[
\Phi'_p(0)=a_2(p)-a_1(p)^2=-\frac{16576p^2-952p+1}{36(1+24p)^2}<0
\]
throughout \(0\le p\le10^{-4}\): the numerator decreases throughout this interval and remains positive at its right endpoint, where its exact value is \(1414009/1562500\). Smoothness on this compact parameter interval gives a uniform \(\delta>0\) for which \(\Phi_p(t)<m_p\) whenever \(0<t\le\delta\). In particular the origin is always a strict local maximizer.

**2. Strict origin dominance at zero mixture.** For \(p=0\),
\[
M_0(t)=\sum_{n=0}^{\infty}\frac{2t^n}{(n+2)!}.
\]
For every integer \(n\ge0\), \(2/(n+2)!\le3^{-n}\), with equality only for \(n=0,1\). At \(n=2\) the inequality is strict; induction holds since successive coefficients have ratio \(1/(n+3)<1/3\) for \(n\ge1\). Thus \(M_0(t)<(1-t/3)^{-1}\) for \(0<t<3\), equivalently \(\Phi_0(t)<1/3\). For \(t\ge3\), positivity of \(M_0(t)>1\) gives \(\Phi_0(t)<1/t\le1/3\). Therefore \(c_*(0)=m_0=1/3\), with a strict gap at every positive argument.

**3. An exact distant witness despite negative slope.** Put \(q=1/10000\). The exact values are \(m_q=2531/7518<1/2\) and
\[
M_q(2)=\frac{9999(e^2-3)+(e^{10}-11)}{20048}.
\]
The elementary finite positive Taylor sums give \(e^2>7\) (through degree five) and \(e^{10}>22000\) (through degree twenty-one). Consequently
\[
M_q(2)>\frac{61985}{20048}=\frac{8855}{2864}>\frac{3759}{1228}=\frac{1}{1-2m_q}.
\]
Multiplying the strictly positive denominators proves the second comparison by integer arithmetic. Since \(2m_q<1\), the inequality is precisely \(\Phi_q(2)>m_q\). Hence \(c_*(q)>m_q\), while \(\Phi'_q(0)<0\). As \(\Phi_q(t)\to0\) as \(t\to\infty\), its global maximizer is strictly interior; at least one intervening local minimum also exists.

**4. Continuity and a coexistence parameter.** Since \(M_p(t)>1\) for \(t>0\), \(\Phi_p(t)<1/t\). Also \(m_p\ge1/3\) for \(p\ge0\). Thus every global maximizer lies in \([0,3]\), and
\[
G(p):=\max_{0\le t\le3}\Phi_p(t)-m_p=c_*(p)-m_p
\]
is nonnegative and continuous on \([0,q]\), since \(\Phi\) extends jointly continuously to the compact rectangle. The uniform negative slope from step 1 excludes maximizers on \((0,\delta]\). On the complementary compact interval \([\delta,3]\), step 2 shows \(\max\Phi_0(t)<m_0\). Joint continuity then yields some \(\varepsilon>0\) such that \(G(p)=0\) for \(0\le p\le\varepsilon\). Step 3 gives \(G(q)>0\).

Define \(p_*=\inf\{p\in(0,q]:G(p)>0\}\). Then \(0<p_*<q\) and \(G(p_*)=0\) by continuity (strict inequality at \(q\) also gives \(p_*<q\)). Take \(p_n\downarrow p_*\) with \(G(p_n)>0\), and select global maximizers \(t_n\). They lie in \([\delta,3]\); hence some subsequence tends to \(t_*\in[\delta,3]\). Continuity shows \(\Phi_{p_*}(t_*)=m_{p_*}=\Phi_{p_*}(0)\). The origin remains a strict local maximizer and \(t_*>0\) is a second global maximizer, proving coexistence and non-continuous optimizer selection along the positive-gap sequence.

## Verification
The standalone Python 3 checker `check.py` validates the exact rational negative-slope certificate, coefficient comparisons, finite Taylor bounds, and strict rational witness inequality; `check_output.txt` contains its actual output. For scale, direct floating-point evaluation gives \(\Phi_{1/10000}(2)\approx0.347894523632774\) and \(m_{1/10000}\approx0.336658685820697\). Neither finite Taylor tests nor floating point replace the analytic compactness argument, which proves existence of \(p_*\) without locating it numerically.

## Relationship to prior work
Chen (2026), Sections 3, 4 and 7.2, supplies the exact optimal-scale transform and the two-point example \(p=1/40\), for which an interior maximizer is established by a positive *local* obstruction. The present result concerns the sparse mixture \(p\le10^{-4}\): the origin is a strict **local** maximizer throughout, yet eventually loses *global* optimality and coexists at a boundary parameter with a remote optimal argument. This is not a restatement of the earlier interior example or the general M-class equivalence. Karp, Vishnyakova and Zhang (2025), Theorem 2.5, gives unimodality preservation for ratios under a unimodal coefficient-ratio hypothesis. The observed separated local minimum and maximum means that a universal unimodality conclusion is inapplicable in the sparse-mixture case; the theorem does not supply the demonstrated global coexistence parameter. Previous mathematical record searches did not reveal the same transition, but independent priority review is outstanding.

## Limitations
The threshold is established existentially in the open interval \((0,10^{-4})\); uniqueness, its exact numerical value, the full optimizer phase diagram, and all parameter values beyond this interval are not claimed. The argument assumes precisely the stated positive two-point jumps and variance-exact right-sided concentration. Numerical checks are finite and are not proof of all-parameter inequalities. No independent mathematical audit has been performed.

## References
1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public 2026-09-02), Sections 3, 4, 7.2. https://arxiv.org/html/2610.00032v1
2. D. Karp, A. Vishnyakova and Y. Zhang, *Unimodality preservation by ratios of functional series and integral transforms*, arXiv:2408.01755v2 (2025), Theorem 2.5. https://arxiv.org/html/2408.01755v2
3. B. Klar and A. Müller, *Characterizations of classes of lifetime distributions generalizing the NBUE class*, Journal of Applied Probability 40 (2003), 20–32 (M-class background, as cited and defined in Chen 2026).
