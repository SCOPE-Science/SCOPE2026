# Quenched Hausdorff spectra of regular and historic rotation in a three-branch random circle map

## Finding

For the two piecewise-affine degree-one circle lifts in Example 3.1 of Li–Lloyd–Romaña, not only is every rotation-average cluster interval attained: its entire realizing set has an exact Hausdorff dimension. Fix \(0<p<1\) and any environment \(\omega\in\{+,-\}^{\mathbb N}\) with asymptotic \(+\)-frequency \(p\). Define
\[
\mathcal P_p(t)=p\log(1+2e^t)+(1-p)\log(1+2e^{-t}),\qquad
D_p(r)=\frac{1}{\log3}\inf_{t\in\mathbb R}(\mathcal P_p(t)-tr).
\]
For every nonempty closed interval \([a,b]\subseteq[p-1,p]\), the set \(E_\omega([a,b])\) of initial circle points whose lift-displacement averages have *exactly* \([a,b]\) as their accumulation set satisfies
\[
\boxed{\dim_H E_\omega([a,b])=\min\{D_p(a),D_p(b)\}.}
\]
The assertion holds simultaneously for all intervals for each fixed frequency-regular environment, so it holds almost surely under Bernoulli forcing. In particular the regular level set \(E_\omega([r,r])\) has dimension \(D_p(r)\). At the extremal rotations,
\[
D_p(p)=\frac{p\log2}{\log3},\qquad
D_p(p-1)=\frac{(1-p)\log2}{\log3}.
\]
Consequently the set realizing the entire historic accumulation interval \([p-1,p]\) has dimension \(\min\{p,1-p\}\log2/\log3>0\). The spectrum has maximum one at \(r=(4p-2)/3\).

## Assumptions and scope

Work on \([0,1)\) modulo integers. The lifts are
\[
F_+(x)=\begin{cases}3x&0\le x<2/3,\\4-3x&2/3\le x<1,\end{cases}
\qquad
F_-(x)=\begin{cases}-3x&0\le x<1/3,\\3x-2&1/3\le x<1,\end{cases}
\]
and \(F_\pm(x+k)=F_\pm(x)+k\) for every integer \(k\). Fix an arbitrary deterministic one-sided environment \(\omega\) such that
\[\lim_{n\to\infty}\frac1n\#\{0\le j<n:\omega_j=+\}=p,\quad 0<p<1.\]
Put \(F_\omega^{(n)}=F_{\omega_{n-1}}\circ\cdots\circ F_{\omega_0}\) and \(A_n(\omega,x)=(F_\omega^{(n)}(x)-x)/n\). Let \(E_\omega([a,b])\) be the set of \(x\in[0,1)\) with \(\operatorname{Clust}_{n\to\infty}\{A_n(\omega,x)\}=[a,b]\). Hausdorff dimension refers to the ordinary Euclidean metric on the circle. No random sample-specific rate of frequency convergence is assumed.

## Proof

**1. Full-branch coding and additive displacement.** Divide \([0,1)\) into thirds \(I_j=[j/3,(j+1)/3)\), \(j=0,1,2\). Both maps have one full affine branch of slope absolute value \(3\) on each \(I_j\). The integer displacements of these branches, apart from the countable set of preimages of partition endpoints, are
\[
(\kappa_+(0),\kappa_+(1),\kappa_+(2))=(0,1,1),\qquad
(\kappa_-(0),\kappa_-(1),\kappa_-(2))=(-1,-1,0).
\]
Every finite branch word labels a distinct interval of length \(3^{-n}\), and every infinite itinerary has a unique coded point (up to the usual countable boundary ambiguities). Writing \(j_i\) for its branch symbols and \(u_i=F_\omega^{(i)}(x)\bmod1\), one has
\[
F_\omega^{(n)}(x)-x=\sum_{i=0}^{n-1}\kappa_{\omega_i}(j_i)+u_n-u_0.
\]
Thus the cluster sets of the original averages agree with those of the bounded-increment integer sums. Partition-boundary itineraries form a countable exceptional set; their inclusion or exclusion does not change the dimensions below, which are strictly positive when \(0<p<1\).

**2. Sharp upper bound.** Fix \(r\in[p-1,p]\), a real \(t\), and \(\epsilon>0\). For any \(n\), the number \(N_n(r,\epsilon)\) of branch words satisfying
\[
\left|\sum_{i<n}\kappa_{\omega_i}(j_i)-nr\right|\le n\epsilon
\]
obeys the exponential counting estimate
\[
N_n(r,\epsilon)\le\exp\!\left(-tnr+n|t|\epsilon+\sum_{i<n}\log Z_{\omega_i}(t)\right),
\quad Z_+(t)=1+2e^t,\quad Z_-(t)=1+2e^{-t}.
\]
Since the environment has limiting \(+\)-frequency \(p\), \(n^{-1}\sum_{i<n}\log Z_{\omega_i}(t)\to\mathcal P_p(t)\). The points with \(r\) among their cluster values lie, for every \(\epsilon>0\), in the limsup of these length-\(3^{-n}\) cylinder covers. For every finite \(t\), their Hausdorff dimension is therefore at most \((\mathcal P_p(t)-tr+|t|\epsilon)/\log3\). First let \(\epsilon\downarrow0\) and then infimize over finite \(t\), including limiting \(t\to\pm\infty\) for endpoint \(r\). Thus this dimension is at most \(D_p(r)\). Membership in \(E_\omega([a,b])\) forces both endpoints to be cluster values, giving
\[\dim_H E_\omega([a,b])\le\min\{D_p(a),D_p(b)\}.\]

**3. Entropy-optimal Bernoulli digit measures.** The pressure \(\mathcal P_p\) is strictly convex, and its derivative maps \(\mathbb R\) bijectively onto \((p-1,p)\). For each interior \(r\), let \(t_r\) solve \(\mathcal P_p'(t_r)=r\), and choose at a sign \(\xi\) the independent digit distribution
\[
q_{\xi,r}(j)=\frac{e^{t_r\kappa_\xi(j)}}{Z_\xi(t_r)}.
\]
At \(r=p\), use equal probabilities on digits \(1,2\) for \(+\) and digit \(2\) with probability one for \(-\). At \(r=p-1\), use digit \(0\) surely for \(+\) and equal probabilities on digits \(0,1\) for \(-\). Write \(m_{\xi,r}\) and \(h_{\xi,r}\) for their mean digit displacement and Shannon entropy. Direct substitution gives
\[
p\,m_{+,r}+(1-p)m_{-,r}=r,\qquad
p\,h_{+,r}+(1-p)h_{-,r}=\log3\,D_p(r).
\]
These identities also hold at the endpoints by their limiting distributions. The endpoint entropies reduce to \(p\log2\) and \((1-p)\log2\), respectively.

**4. One measure realizing the entire historic interval.** When \(a=b=r\), apply the distribution \(q_{\omega_i,r}\) at every time \(i\). The independent bounded-variable strong law gives displacement average \(r\) and per-symbol negative log cylinder mass \(\log3\,D_p(r)\), almost surely under the corresponding digit product measure. The deterministic environment-frequency assumption suffices for convergence of the expectations.

When \(a<b\), choose an integer switching schedule \(N_1<N_2<\cdots\) with \(N_{k+1}/N_k\to\infty\), for example \(N_k=2^{2^k}\), and apply the digit laws targeting \(a,b,a,b,\ldots\) on successive time blocks. Within each block, digit coordinates remain independent. The bounded-variable strong law applies to centered displacements and centered negative log probabilities. The environment-frequency error \(e(n)=\#\{i<n:\omega_i=+\}-pn=o(n)\) has total contribution \(o(n)\), uniformly for prefixes crossing these superexponentially separated blocks: each completed block contributes the difference of two \(e\)-values, the sum of preceding boundary errors is \(o(n)\), and the current partial block contributes at most \(|e(n)|+|e(N_k)|=o(n)\). Therefore the drift averages remain asymptotically in \([a,b]\), while at alternating block endpoints they tend to \(a\) and \(b\). As increments of scalar Cesàro averages vanish, their exact accumulation set is the entire interval \([a,b]\).

Likewise, at every sufficiently large prefix, the expected accumulated Shannon entropy is at least
\[
n\log3\min\{D_p(a),D_p(b)\}-o(n).
\]
For almost every coded point under this digit product measure,
\[
\liminf_{n\to\infty}\frac{-\log\mu(I_n(x))}{n\log3}\ge\min\{D_p(a),D_p(b)\},
\]
where \(I_n(x)\) is its length-\(3^{-n}\) cylinder. To turn this into an ordinary Hausdorff bound, fix any smaller exponent \(s\); a positive-measure set satisfies \(\mu(I_n(x))\le3^{-ns}\) uniformly for all sufficiently large \(n\). The restricted measure obeys the same bound on every level-\(n\) cylinder intersecting this set. Any real interval of length at most \(3^{-n}\) meets at most two (at worst three if endpoint conventions are included) level-\(n\) triadic intervals, yielding a uniform Frostman \(s\)-bound. Therefore \(\dim_H E_\omega([a,b])\ge s\), and letting \(s\) increase to the displayed minimum gives the required lower bound.

**5. Endpoint and maximum values.** The limiting entropy-optimal distributions in step 3 give \(D_p(p)=p\log2/\log3\), \(D_p(p-1)=(1-p)\log2/\log3\). Since \(\mathcal P_p(0)=\log3\) and \(\mathcal P_p'(0)=(4p-2)/3\), the strictly concave spectrum attains value one at that rotation. This finishes the simultaneous all-interval classification.

## Verification

The accompanying standalone `verify_rotation_spectrum.py` checks every one of the \(3^n\) digit itineraries for all \(2^n\) environments of lengths \(1\le n\le5\), and three further length-seven environments. It reconstructs exact rational points by inverse branches, directly applies the piecewise lifts, compares every step's integer displacement with the asserted cocycle, and independently counts rotation sums using polynomial convolution. There are 15,891 finite-word checks. It also checks the pressure-spectrum endpoint identities and normalization for three parameter choices. Run using `python3 verify_rotation_spectrum.py`; the expected output begins with `VERIFY_OK`.

The general Hausdorff-dimension statement follows from the cylinder-counting argument and the inhomogeneous product-measure construction, not from those finite checks.

## Relationship to prior work

Li, Lloyd, and Romaña (2026, arXiv:2606.16498v1), Example 3.1 and Example 4.1, establish the Bernoulli rotation interval \([p-1,p]\), full three-branch coding and random topological entropy \(\log3\); their Theorem 2.2 and Corollary 2.1 establish existence of individual orbits with prescribed historic cluster intervals. Those results do not give the Hausdorff dimension of the sets of such initial conditions. The present result is an exact quantitative refinement for that particular example, not a general theorem for arbitrary random circle endomorphisms.

Barreira, Li, and Valls (2012) study the residuality of prescribed-average accumulation sets in autonomous full shifts; residuality does not determine the quenched Hausdorff spectrum. Liu and Liu (2024/2026) study irregular sets for a uniquely ergodic base with Anosov invertible fibers, and their full fiber-entropy result does not apply to the one-sided Bernoulli base and noninvertible three-branch circle model. General deterministic multifractal formalism motivates the Legendre transform; it is not claimed as new. The nonstationary environment and simultaneous exact historic dimensions are the particular computations proved here.

## Limitations

The theorem requires a fixed environment with limiting \(+\)-frequency strictly between zero and one and this specific uniform-slope three-branch family. It does not assert the same formulas for general nonuniform expanding random maps, Bernoulli environments without a frequency limit, or arbitrary cocycles. The proof computes Hausdorff dimensions, not packing dimensions, Lebesgue measures, or exact Hausdorff measures. General conditional multifractal and saturation literature could conceivably contain an equivalent specialization; no exhaustive priority or independent external validation is claimed.

## References

1. Z. Li, S. Lloyd, S. Romaña, *Rotation Sets and Topological Entropy for Random Circle Endomorphisms*, arXiv:2606.16498v1 (first posted 2026-06-15), especially Examples 3.1 and 4.1 and Theorem 2.2.
2. L. Barreira, J. Li, C. Valls, *Full shifts and irregular sets*, São Paulo J. Math. Sci. 6 (2012), 135–143, DOI:10.11606/issn.2316-9028.v6i2p135-143.
3. N. Liu, X. Liu, *Irregular sets for a class of skew product transformations*, arXiv:2404.12562v1; Discrete Contin. Dyn. Syst. 51 (2026), 128–160, DOI:10.3934/dcds.2026025.
4. A. Käenmäki, H. W. J. Reeve, *Multifractal analysis of Birkhoff averages for typical infinitely generated self-affine sets*, J. Fractal Geom. 1 (2014), 83–152, DOI:10.4171/JFG/3 (general background; different self-affine setting).
