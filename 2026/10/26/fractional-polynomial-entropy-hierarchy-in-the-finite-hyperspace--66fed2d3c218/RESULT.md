# Fractional polynomial-entropy hierarchy in the finite hyperspaces of a pointwise periodic continuum

## Finding
For each real \(\alpha>1\), let \(A_\alpha=\{0\}\cup\{1/\lfloor j^\alpha\rfloor:j\in\mathbb N,\ j\ge1\}\). Define the compact connected rotating-disk space \(X_\alpha\) and pointwise periodic homeomorphism \(f_\alpha\) below. The exact induced polynomial entropies are
\[
h_{\mathrm{pol}}(F_n(f_\alpha))=\frac{n}{\alpha+1}\qquad(n\ge1),
\]
and
\[
h_{\mathrm{pol}}(\mathcal SF_n(f_\alpha))=\frac{n}{\alpha+1}\qquad(n\ge2).
\]
The induced homeomorphism on the full hyperspace \(2^{X_\alpha}\) of nonempty compact subsets has infinite polynomial entropy. Each finite-subset system is itself pointwise periodic and has zero ordinary topological entropy. This is an exact finite-to-infinite induced-complexity spectrum in a continuum with no nonperiodic points and no wandering points.

## Assumptions and scope
Write \(\overline{\mathbb D}=\{z\in\mathbb C:|z|\le1\}\) and identify \(X_\alpha=(A_\alpha\times\overline{\mathbb D})\cup([0,1]\times\{0\})\) with a subspace of \([0,1]\times\mathbb C\). On each horizontal disk set \(f_\alpha(a,z)=(a,e^{2\pi ia}z)\); on the central spine \(z=0\) this is the identity. The map is a homeomorphism of a compact connected metric space: the disks accumulate on the disk at height zero, and the axial spine joins them. Every height is rational; therefore each individual point has a finite orbit.

For \(n\ge1\), let \(F_n(X_\alpha)\) be all nonempty subsets with at most \(n\) points, with the Hausdorff metric, and let \(F_n(f_\alpha)(S)=f_\alpha(S)\). For \(n\ge2\), \(\mathcal SF_n(X_\alpha)=F_n(X_\alpha)/F_1(X_\alpha)\) collapses the entire closed singleton stratum to a single point. The induced map respects this quotient. Let \(2^{X_\alpha}\) be all nonempty compact subsets. Polynomial entropy uses the length-\(N\) Bowen metric \(d_N(x,y)=\max_{0\le t<N}d(f^t x,f^t y)\) and
\[
h_{\mathrm{pol}}(f)=\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}\frac{\log\operatorname{sep}(N,\varepsilon)}{\log N}.
\]
All assertions concern fixed \(\alpha>1\), with \(n\) an arbitrary fixed positive integer; no bound uniform in \(n\) or \(\alpha\) is claimed.

## Proof
**1. Height-packing law.** Put \(a_j=1/\lfloor j^\alpha\rfloor\). Since \(\alpha>1\), these heights become strictly decreasing and
\[
a_j-a_{j+1}\sim\alpha j^{-\alpha-1}.
\]
Indeed \(\lfloor(j+1)^\alpha\rfloor-\lfloor j^\alpha\rfloor\sim\alpha j^{\alpha-1}\), whereas the product of the two denominators is asymptotic to \(j^{2\alpha}\). Consequently, for each sufficiently large integer \(N\), one can select \(S_N\subset A_\alpha\cap(0,1/8)\) with \(\#S_N\ge c_\alpha N^{1/(\alpha+1)}\), with distinct heights separated by at least \(1/N\). For completeness, choose a fixed large \(j_0\) with \(a_{j_0}<1/8\) and all gap estimates valid, and include consecutive \(a_j\) for \(j_0\le j\le cN^{1/(\alpha+1)}\), with the constant \(c>0\) small enough that every neighboring gap exceeds \(1/N\). Conversely, the first \(O(N^{1/(\alpha+1)})\) heights form a finite net, while the remaining heights occupy an interval of length \(O(N^{-\alpha/(\alpha+1)})\), which costs only \(O(N^{1/(\alpha+1)})\) intervals of length \(1/N\). Hence, for every fixed \(c'>0\), the minimum number of \(c'/N\)-intervals covering \(A_\alpha\) is \(O_{\alpha,c'}(N^{1/(\alpha+1)})\).

**2. Upper bounds.** Fix \(\varepsilon>0\). Cover \(A_\alpha\) by intervals of length \(\varepsilon/(100N)\) with representatives in \(A_\alpha\); there are \(O_{\alpha,\varepsilon}(N^{1/(\alpha+1)})\) of them. On each representative disk choose an \(\varepsilon/10\)-net of \(\overline{\mathbb D}\), using the same planar coordinates for every disk; its size depends on \(\varepsilon\) but not on \(N\). The bound
\[
|e^{2\pi ita}-e^{2\pi itb}|\le2\pi t|a-b|
\]
shows that these choices give an \(O(\varepsilon)\)-spanning set in the length-\(N\) Bowen metric on the entire union of disks. The central spine is fixed and contributes only \(O_\varepsilon(1)\) additional centers. Thus the base system has \(O_{\alpha,\varepsilon}(N^{1/(\alpha+1)})\) Bowen spanning number. Taking ordered \(n\)-tuples and pushing them to the finite-subset quotient yields
\[
\operatorname{span}_{F_n}(N,\varepsilon)=O_{\alpha,\varepsilon,n}(N^{n/(\alpha+1)}).
\]
Indeed the map \((x_1,\ldots,x_n)\mapsto\{x_1,\ldots,x_n\}\) is 1-Lipschitz from the maximum product metric to the Hausdorff metric and equivariant. The singleton-collapse map is an equivariant continuous factor, so it cannot increase polynomial entropy. Therefore both claimed finite-layer entropies are at most \(n/(\alpha+1)\).

**3. Lower bound immune to point relabeling.** Fix \(n\ge1\) and distinct radii \(r_i=i/(n+1)\), \(1\le i\le n\). Let \(\Delta=1/(n+1)\). For each tuple \((a_1,\ldots,a_n)\in S_N^n\), form the unordered configuration
\[
C(a_1,\ldots,a_n)=\{(a_i,r_i):1\le i\le n\},
\]
where \(r_i\) is represented by the positive real point in its disk. There are \((\#S_N)^n\) distinct configurations. Suppose two tuples differ at coordinate \(i\). Their heights satisfy \(\delta=|a_i-b_i|\in[1/N,1/8]\). Let \(t=\lceil1/(4\delta)\rceil\). For all sufficiently large \(N\), \(t<N\) and \(t\delta\in[1/4,3/8]\). The same-radius \(i\)-th points, after time \(t\), have planar separation
\[
2r_i\sin(\pi t\delta)\ge\sqrt2r_i\ge\sqrt2\Delta.
\]
Every point having another radius \(r_j\) stays at distance at least \(\Delta\), independently of height, angle, or time. Thus the \(i\)-th point of the first configuration is at distance at least \(\Delta\) from **every** point of the second configuration at time \(t\). Their Hausdorff distance is at least \(\Delta\). This establishes an \((N,\Delta)\)-separated family of cardinality at least \(c_\alpha^nN^{n/(\alpha+1)}\), proving the matching lower bound for \(F_n\).

**4. Passing through singleton collapse.** For \(n\ge2\), every displayed configuration has points of two different radii separated by at least \(\Delta\) at all times; hence its Hausdorff distance from the closed singleton stratum is at least \(\Delta/2\). A compatible quotient metric is obtained by allowing the distance between two noncollapsed classes to be the minimum of their original Hausdorff distance and the sum of their distances to the collapsed stratum. Both quantities in that minimum are at least \(\Delta\) for distinct configurations at the separating time from Step 3. Thus the same family is separated in \(\mathcal SF_n\), and the lower bound survives collapse.

**5. Full hyperspace and ordinary entropy.** Each \(F_n(X_\alpha)\) is a compact invariant subspace of \(2^{X_\alpha}\). Monotonicity of polynomial entropy under restriction gives \(h_{\mathrm{pol}}(2^{f_\alpha})\ge n/(\alpha+1)\) for every \(n\), and therefore it is infinite. A finite configuration is periodic because its points have rational rotation heights; the common least common multiple of their periods fixes the set. The finite-layer polynomial entropy bound is finite, and therefore its ordinary topological entropy is zero. The same holds for the collapsed finite layers as their factors.

## Verification
The accompanying `checker.py` uses exact rational arithmetic on the height sets when \(\alpha=2\), checks the separation-time interval for many pairs, and numerically verifies the circle-chord and distinct-radius separation inequalities. Its observed success at finite parameters is not used to infer any asymptotic theorem. The analytic steps above establish the infinite-parameter bounds. Running `python3 checker.py` reproduces the attached `checker_output.txt`.

## Relationship to prior work
Đorić, Katić and Perić (2026), arXiv:2606.28283v1, introduce this pointwise periodic rotating-disk continuum, compute its base polynomial entropy as \(1/(\alpha+1)\), and establish the height packing estimates. The present theorem takes their specific example as an input and classifies every finite-subset layer and the full hyperspace; it does not claim the original base construction or packing lemma as new.

Đorić (2025 preprint; revised 2026), arXiv:2507.10126, proves the same **formal multiplicative expression** for the finite symmetric-product system and singleton-collapsed suspension under the hypothesis that the chain recurrent set is finite, and also gives a wandering-point lower bound. Those hypotheses do not apply: here every point is periodic and the entire infinite continuum is chain recurrent. The new argument uses labeled radial markers to prevent permutation cancellation in a system without wandering points. Đorić, Katić and Lasković (2023) give related lower bounds under a wandering-point assumption, which likewise fails here.

Naghmouchi (2025 preprint, revised 2026), arXiv:2512.08836, investigates qualitative dynamics and zero **topological** entropy of hyperspace maps of pointwise periodic homeomorphisms. This does not determine finite-level polynomial entropy or the infinite polynomial entropy of the full hyperspace. These distinctions are mathematical implication comparisons, not claims that unsearched literature cannot exist.

## Limitations
This is a classification for the specified rotating-disk continuum, not for all pointwise periodic systems. The full hyperspace is not asserted to be pointwise periodic, and no finite positive topological entropy is claimed. The asymptotic notation in the height-cover argument is for fixed \(\alpha>1\). The conclusion does not address arbitrary generalized suspension strata, measure-theoretic entropy of the full hyperspace, or quantitative constants uniform in \(n\). A comprehensive historical priority determination and independent proof validation have not been performed.

## References
1. Maša Đorić, Jelena Katić and Milan Perić, *A flexibility result for polynomial entropy of pointwise periodic homeomorphisms*, arXiv:2606.28283v1 (first public 2026-06-26), especially Example 12, Propositions 13 and 15, and Section 4.3. https://arxiv.org/abs/2606.28283
2. Maša Đorić, *Polynomial entropy on the n-fold symmetric product and its suspension*, arXiv:2507.10126v1 (2025), especially Theorem 9 of the 2026 revision; Glasnik Matematicki 61 (2026), 59–76. https://arxiv.org/abs/2507.10126
3. Issam Naghmouchi, *Dynamics on Hyperspace of Pointwise Periodic Homeomorphisms*, arXiv:2512.08836v1 (2025), especially the main zero-topological-entropy result. https://arxiv.org/abs/2512.08836
4. Maša Đorić, Jelena Katić and Bojana Lasković, *On polynomial entropy of induced maps on symmetric products*, Acta Math. Hungar. (2023). https://doi.org/10.1007/s10474-023-01386-8
