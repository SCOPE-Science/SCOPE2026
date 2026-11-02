# Exact separation and interval-filling thresholds for three-sample random reshuffling

## Finding
Consider three scalar quadratic losses with centers \(-1,0,1\), trained by a fresh uniformly random permutation each epoch, with the component-gradient stepsize \(\eta=1-q\), \(0<q<1\). The epoch endpoints converge **in distribution**, from any deterministic initial value, to a unique stationary law \(\mu_q\) with compact support \(K_q\).

Let \(q_{\mathrm{sep}}\) be the unique root in \((0,1)\) of
\[
1-q-3q^3-q^4=0,
\]
and let \(q_{\mathrm{fill}}\) be the unique root in \((0,1)\) of
\[
1-q^2-2q^3=0.
\]
Then \(q_{\mathrm{sep}}\approx0.5162390097\) and \(q_{\mathrm{fill}}\approx0.6572981061\). These constants govern two distinct exact geometric conclusions:

1. The six closed, first-generation interval hulls are pairwise disjoint **if and only if** \(0<q<q_{\mathrm{sep}}\). In this range the stationary support is a strongly separated self-similar Cantor set, and both its Hausdorff dimension and the exact dimension of the stationary measure are
\[
\dim_{\mathrm H}K_q=\dim_{\mathrm H}\mu_q=\frac{\log 6}{-3\log q}.
\]
2. The stationary support is its **entire convex hull if and only if** \(q_{\mathrm{fill}}\le q<1\). In particular, in the intermediate range \(q_{\mathrm{sep}}\le q<q_{\mathrm{fill}}\), the first-generation interval hulls are not pairwise disjoint, but an explicit open gap remains in the stationary support. No dimension formula is asserted in this intermediate range.

For every \(0<q<q_{\mathrm{fill}}\), the explicit central hole is \((-g_q,g_q)\cap K_q=\varnothing\), where
\[
g_q=\frac{(1-q)^2q(1-q^2-2q^3)}{1-q^3}>0.
\]
The convex hull and the stationary moments are exactly
\[
\operatorname{conv}(K_q)=[-A_q,A_q],\qquad A_q=\frac{1-q^2}{1+q+q^2},
\]
\[
\int x\,d\mu_q(x)=0,\qquad \int x^2\,d\mu_q(x)=\frac{2(1-q)^3}{3(1+q^3)}.
\]
The variance identity is included to calibrate the geometry, not presented as a new general second-moment method.

## Assumptions and scope
There are exactly three component objectives \(f_c(x)=\frac12(x-c)^2\), indexed by \(c\in\{-1,0,1\}\). At every epoch the three centers are visited exactly once, in a uniformly random permutation independent of all earlier epochs, with no momentum or projection. Every component step uses the same constant \(\eta=1-q\), where \(0<q<1\). The state \(X_k\) means the endpoint after \(k\) complete epochs; the claim does not concern almost-sure convergence of the continuing noisy trajectory or the intermediate component iterates. The minimizer of the averaged objective is zero, but the fixed-stepsize stationary law need not collapse to zero.

## Proof
**Epoch reduction.** The component map is \(x\mapsto qx+(1-q)c\). For a permutation \((c_1,c_2,c_3)\) its composition is
\[
x\mapsto q^3x+(1-q)(q^2c_1+qc_2+c_3).
\]
Enumerating the six permutations of \((-1,0,1)\) produces precisely
\[
X_{k+1}=rX_k+tD_k,\quad r=q^3,\quad t=(1-q)^2,
\]
where the independent digits \(D_k\) are uniform on the sorted set
\[
\mathcal D_q=\{-1-q,-1,-q,q,1,1+q\}.
\]
Since \(0<r<1\), the affine Markov kernel contracts the one-dimensional Wasserstein distance by \(r\). It therefore has one stationary probability, the law of the absolutely convergent random series \(t\sum_{j\ge0}r^jD_j\), and the epoch-endpoint distributions converge to it. Its support is the unique nonempty compact fixed set of the six similarities \(\phi_d(x)=rx+td\), \(d\in\mathcal D_q\), because each digit has positive probability.

**Convex hull.** The extreme digits are \(\pm(1+q)\). Hence the smallest invariant closed interval is \(I_q=[-A_q,A_q]\) with
\[
A_q=\frac{t(1+q)}{1-r}=\frac{(1-q)^2(1+q)}{1-q^3}=\frac{1-q^2}{1+q+q^2}.
\]
The two constant-extreme digit strings attain its endpoints, so \(I_q=\operatorname{conv}K_q\). The ordered first-generation interval hulls \(\phi_d(I_q)\) each have length \(2rA_q\). Dividing an adjacent interval's center separation by \(t\), the five successive digit gaps are exactly \(q,1-q,2q,1-q,q\). Consequently neighboring hull intervals overlap or touch precisely when their normalized digit gap is at most
\[
T(q):=\frac{2rA_q}{t}=\frac{2q^3(1+q)}{1-q^3}.
\]
Nonneighbors cannot overlap without some neighboring pair overlapping.

**Disjointness threshold.** For \(0<q\le1/2\), the smallest digit gap is \(q\). Here \(q>T(q)\), because this inequality reduces to \(1-2q^2-3q^3>0\), a strictly decreasing polynomial that remains \(1/8>0\) at \(q=1/2\). For \(q>1/2\), the smallest gap is \(1-q\); its strict excess over \(T(q)\) is equivalent, after multiplication by the positive \(1-q^3\), to
\[
P(q):=1-q-3q^3-q^4>0.
\]
Since \(P'(q)=-1-9q^2-4q^3<0\), \(P(1/2)>0\), and \(P(1)<0\), exactly one threshold \(q_{\mathrm{sep}}\in(1/2,1)\) exists. Below it, the six compact image intervals are mutually disjoint, implying the strong separation condition for the support; the standard homogeneous self-similar dimension formula (six equal-probability maps of ratio \(q^3\)) gives the stated dimensions. At equality two neighboring image intervals touch; because both endpoint addresses belong to the support, their corresponding support pieces actually meet. Above equality this proof does **not** infer intersection of the underlying fractal pieces merely from overlap of their enclosing intervals.

**Interval-filling threshold.** The six image intervals fill \(I_q\) exactly when **every** adjacent normalized digit gap is at most \(T(q)\). The central gap \(2q\) is always present, so interval filling requires
\[
2q\le T(q)\quad\Longleftrightarrow\quad H(q):=1-q^2-2q^3\le0.
\]
The derivative \(H'(q)=-2q-6q^2<0\) for positive \(q\), while \(H(0)>0\) and \(H(1)<0\); thus there is a unique \(q_{\mathrm{fill}}\). Moreover \(H(1/3)>0\), so \(q_{\mathrm{fill}}>1/3\). For all \(q\ge q_{\mathrm{fill}}\), the central gap \(2q\) is the largest of the five because \(2q\ge1-q\). Therefore all adjacent image intervals touch or overlap, and \(\bigcup_d\phi_d(I_q)=I_q\). Uniqueness of the compact IFS attractor forces \(K_q=I_q\). Conversely if \(q<q_{\mathrm{fill}}\), the central two image intervals leave a nonempty open gap inside \(I_q\). Since \(K_q=\bigcup_d\phi_d(K_q)\subset\bigcup_d\phi_d(I_q)\), that gap is missing from \(K_q\), so \(K_q\ne I_q\). Finally \(q_{\mathrm{sep}}<q_{\mathrm{fill}}\): for example \(P(3/5)<0\) and \(H(3/5)>0\), while their zeros are unique.

**Moments.** Symmetry gives mean zero. Direct digit summation gives \(\mathbb E D^2=2(1+q+q^2)/3\). Taking the variance of \(X\stackrel d=rX+tD\), with independent \(X\) and \(D\), yields
\[
\mathbb E X^2=\frac{t^2\mathbb E D^2}{1-r^2}=\frac{2(1-q)^3}{3(1+q^3)}.
\]

## Verification
Run the portable Python exact-arithmetic checker `python3 verify.py`. It enumerates all six permutations for eight rational choices of \(q\), checks the digit gaps and convex-hull identities, checks both algebraic threshold criteria and exact second-moment identities, verifies 56 finite-epoch second-moment sums, and supplies rational sign brackets \(0.516<q_{\mathrm{sep}}<0.517\) and \(0.657<q_{\mathrm{fill}}<0.658\). The infinitely quantified transition statements follow from the analytical inequalities and monotonicity in the proof, not from the finite tests.

## Relationship to prior work
Chen and Zhang (2026) describe the independent-permutation RR-SGD algorithm and study final-iterate objective guarantees, but do not give an exact stationary-support phase diagram for this three-component model. Ying, Yuan, Vlaski and Sayed (2018) already analyze steady-state mean-square errors of constant-stepsize random reshuffling, including quadratic models; the variance calculation above does not claim priority over those analyses. Camuto and collaborators (2021) explicitly model stochastic optimization as a random iterated-function system and exhibit Cantor stationary supports for sampling with replacement. Accordingly, neither the IFS reduction nor the general observation of fractal stochastic-optimizer supports is claimed as new. The narrower contribution is the pair of exact three-permutation reshuffling thresholds, the intervening persistent central-gap regime, and the six-symbol dimension formula for the strongly separated parameter range. Standard self-similar-set theory supplies the dimension principle. These comparisons do not establish historical uniqueness across all specialized IFS literature.

## Limitations
This is a precisely specified one-dimensional, three-component symmetric quadratic benchmark with fresh independent epoch permutations and a fixed stepsize in \((0,1)\); arbitrary curvature, asymmetric component centers, different sample counts and other shuffling policies are outside the theorem. The disjointness boundary refers exactly to the **first-generation enclosing intervals**. Nothing is asserted about dimension, singularity or possible overlap of the underlying attractor pieces in \([q_{\mathrm{sep}},q_{\mathrm{fill}})\). Interval support does not imply an absolutely continuous stationary measure. Distributional convergence is not almost-sure convergence of forward sample paths. The proof does not imply a new generic convergence bound for RR-SGD.

## References
- Z. Chen and Z. Zhang, *Large-Step Last-Iterate Convergence of Random-Reshuffling Stochastic Gradient Descent*, arXiv:2610.19444, first submitted 2026-10-14. https://arxiv.org/abs/2610.19444
- B. Ying, K. Yuan, S. Vlaski and A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964, 2018. https://arxiv.org/abs/1803.07964
- A. Camuto, G. Deligiannidis, M. A. Erdogdu, M. Gürbüzbalaban, U. Şimşekli and L. Zhu, *Fractal Structure and Generalization Properties of Stochastic Optimization Algorithms*, arXiv:2106.04881, 2021. https://arxiv.org/abs/2106.04881
- J. E. Hutchinson, *Fractals and self-similarity*, Indiana University Mathematics Journal 30 (1981), 713–747; standard invariant-set and separation/dimension results.
