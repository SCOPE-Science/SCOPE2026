# A sharp atomic-to-Bernoulli phase diagram for randomized incremental proximal steps

## Finding
For a scalar strongly convex objective split into two absolute-value regularizers, a fixed-step randomized incremental proximal method has a unique stationary distribution of **exactly one of three mutually exclusive types**: a symmetric pair of atoms, an infinite countable atomic measure, or a nonatomic Bernoulli convolution. Both transition surfaces are explicit and sharp; the middle regime features finite-word exact resetting despite a nontrivial contraction between resets.

More precisely, given the assumptions below, set \(s=c/(1+r)\) and \(b=c/(1-r)\), so \(0<s<b\). The invariant distribution \(\pi\) satisfies

\[
\begin{array}{c|c}
\text{Condition}&\text{exact invariant-measure type}\\
0<a\le s&\frac12(\delta_{-a}+\delta_a)\\
s<a<b&\text{purely atomic, countably infinitely many atoms}\\
a\ge b&\text{nonatomic Bernoulli convolution}.
\end{array}
\]

In the middle regime a run of \(N\) identical update signs forces an exact reset to the associated endpoint, with the *least* uniform reset length
\[
N=\min\left\{n\ge1:r^n\le\frac{b-a}{b+a}\right\}.
\]
For \(a\ge b\), \(\pi\) has variance \(c^2/(1-r^2)\); its support is an interval when \(r\ge1/2\) and a Cantor set of Hausdorff dimension \(\log 2/(-\log r)\) otherwise. The Bernoulli-convolution support and dimension formulas are classical; the contribution assessed here is the complete threshold classification for this proximal iteration.

## Assumptions and scope
Let \(\mu,\lambda,a>0\), \(0<\tau\mu<1\), and
\[
f(x)=\frac{\mu}{2}x^2,\quad g_+(x)=\lambda|x-a|,\quad g_-(x)=\lambda|x+a|,\quad h=f+g_++g_-.
\]
Because \(|x-a|+|x+a|=2\max(a,|x|)\), the unique minimizer of \(h\) is \(0\). The exact-arithmetic randomized incremental proximal iteration with two independently and uniformly selected regularizer components is
\[
X_{n+1}=\operatorname{prox}_{2\tau g_{\varepsilon_n}}\big(X_n-\tau f'(X_n)\big),\qquad \mathbb P(\varepsilon_n=\pm1)=1/2,
\]
where the \(\varepsilon_n\) are independent and \(X_0\in I=[-a,a]\). We use \(g_{+1}=g_+\), \(g_{-1}=g_-\), and \(\operatorname{prox}_{\gamma\phi}(z)=\arg\min_y\{\gamma\phi(y)+|y-z|^2/2\}\). Write
\[
r=1-\tau\mu\in(0,1),\quad c=2\tau\lambda,\quad s=\frac{c}{1+r},\quad b=\frac{c}{1-r}=\frac{2\lambda}{\mu}.
\]
The two update maps, restricted to the invariant interval \(I\), are
\[
T_+(x)=\min(a,rx+c),\qquad T_-(x)=\max(-a,rx-c).
\]
All distributional claims refer to the unique invariant probability of this Markov chain on \(I\), without a claim of almost-sure convergence of the individual forward sample paths.

## Proof
**1. Exact proximal maps and unique invariant law.** The scalar optimality condition for the proximal subproblem with center \(d\) is \(0\in y-z+c\partial|y-d|\). Its solution equals \(z+c\) below \(d-c\), \(d\) between \(d-c\) and \(d+c\), and \(z-c\) above \(d+c\). Since \(rx\in[-ra,ra]\) for \(x\in I\), the displayed clipped formulas follow (with \(d=\pm a\)). Both maps preserve \(I\) and are \(r\)-Lipschitz. Coupling two chains with the same sign sequence gives \(|X_n-Y_n|\le r^n|X_0-Y_0|\). The induced Markov map is therefore a strict contraction in the complete \(W_1\) space of probabilities on compact \(I\): it has a unique invariant law and \(W_1(\mathcal L(X_n),\pi)\le 2a r^n\) for every deterministic \(X_0\in I\).

**2. Two atoms.** For every \(x\in I\), \(T_+(x)=a\) exactly when \(c-ra\ge a\), or \(a\le c/(1+r)=s\). By symmetry the same condition makes \(T_-(x)=-a\) for all \(x\in I\). Thus one update creates independent fair endpoint selection and the invariant law is the displayed two-atom measure.

**3. Infinite countable atoms.** Suppose \(s<a<b\). Iterating plus updates from the left endpoint gives
\[
T_+^n(-a)=\min\big(a,\,b-r^n(b+a)\big).
\]
The formula follows inductively from monotone clipping of the affine contraction with unconstrained fixed point \(b>a\). Hence a block of \(N\) plus signs, with the least \(N\) in the finding, maps the *entire* interval to \(a\); a minus block similarly maps it to \(-a\). In a two-sided independent sign sequence, almost surely at least one constant-sign block of length \(N\) lies at a finite time in the past, because disjoint length-\(N\) windows have independent probability \(2^{1-N}>0\) of being monochromatic. Every composition after the most recent such block acts on the known reset endpoint and therefore produces one of countably many finite-word values. The backward contractive construction produces the unique stationary law, so it is purely atomic. A plus block of length \(N\) produces mass at \(a\) of at least \(2^{-N}\) (and analogously at \(-a\)).

To prove there are infinitely many *distinct* atoms, let \(G=T_+\circ T_-\). For each \(x\in[s,a]\), the lower map does not clip, and the upper map also does not clip after it; a direct substitution gives
\[
G(x)=s+r^2(x-s).
\]
Consequently \(G^j(a)=s+r^{2j}(a-s)\) are pairwise distinct for integers \(j\ge0\), since \(s<a\). Each is an atom: stationarity and the positive probability of the specified finite sign word propagate positive mass from the atom \(a\). There are exactly countably infinitely many atoms.

**4. Nonatomic branch.** If \(a\ge b\), then \(rx+c\le a\) and \(rx-c\ge-a\) for all \(x\in I\), so the caps are inactive. The invariant distribution is
\[
X\stackrel d= c\sum_{j=0}^{\infty}r^j\varepsilon_j,
\]
with fair independent signs; absolute convergence and stationary invariance are immediate. The law is supported on \([-b,b]\). For a self-contained no-atoms argument, assume some atom exists and choose one of maximum mass \(M>0\); a maximum exists since a probability has only finitely many atoms larger than any fixed positive threshold. From stationarity, an atom of mass \(M\) at \(x\) would require *both* its two affine preimages, \((x-c)/r\) and \((x+c)/r\), to carry mass \(M\). Repeated first preimages have the form \(b+(x-b)/r^n\); when \(x<b\) they eventually exit the support \([-b,b]\), contradiction. For \(x=b\), the second preimage exceeds \(b\), also a contradiction. Thus there are no atoms.

The support is the invariant attractor of the two affine maps \(x\mapsto rx\pm c\). Their images of \([-b,b]\) overlap or touch precisely at \(r\ge1/2\), yielding that full interval; otherwise they are disjoint and give the standard two-copy Cantor set, of Hausdorff dimension \(\log2/(-\log r)\) by the open-set condition. Independence gives \(\mathbb EX=0\) and \(\operatorname{Var}(X)=c^2\sum_{j\ge0}r^{2j}=c^2/(1-r^2)\).

**5. Sharpness and design meaning.** Since \(r\in(0,1)\), \(s<b\), all three regimes are nonempty and the endpoint equalities belong exactly to the indicated cases. The atom-to-diffuse threshold is \(a=b=2\lambda/\mu\), independent of \(\tau\). For a fixed objective with \(a<b\), the two-atom regime begins at the admissible stepsize \(\tau=2a/(2\lambda+a\mu)\); below it the law is countably atomic. No finite forward-path enumeration is used to prove measure type.

## Verification
The accompanying standalone standard-library Python script `verify_clipped_ripm.py` performs 131,832 rational-algebra and seeded finite-sample assertions. The checks independently implement the proximal optimality cases, verify clipped-map identities for rational parameters, test the exact minimal reset word and the distinct alternating-word orbit, and check finite Bernoulli-convolution moments. The measure classification and infinite quantifiers are established by the proof above, not by these finite tests.

## Relationship to prior work
Vaidyan, Friedlander and Alacaoglu (2026), Section 4, establish last-iterate expected-objective rates for the randomized incremental proximal method with horizon-dependent stepsizes; they do not classify its constant-step invariant law. The method predates that paper, as recognized there and in Bertsekas's incremental proximal survey. Hermer, Luke and Sturm (2023), especially Section 4 and Proposition 4.1, give general distributional convergence for stochastic forward–backward random-function iterations; that theory supports the general framework but does not specify the two sharp clipping surfaces, the intermediate infinitely atomic regime, or its exact uniform reset length. Hutchinson's theory covers affine contraction invariant measures and the Bernoulli branch; the Cantor/interval dichotomy is not claimed as new. The assessment concerns the complete proximal-specialization classification, not existence of invariant measures or Bernoulli-convolution fundamentals.

## Limitations
This is a one-dimensional, two-component, symmetric, exact-arithmetic, iid uniformly sampled, fixed-step result with \(0<\tau\mu<1\). It makes no claim of smooth stationary densities in the overlapping Bernoulli-convolution regime, no bound on floating-point resets, no analogous transition for arbitrary nonsymmetric components, and no almost-sure convergence of individual stationary sample paths. The literature comparison is not proof of exhaustive bibliographic novelty; an earlier specialist classification of clipped random affine maps could imply the result.

## References
1. K. K. T. Vaidyan, M. P. Friedlander and A. Alacaoglu, *Convergence Rate of the Last Iterate of Stochastic Proximal Algorithms*, arXiv:2602.05489v1 (first public 2026-02-05), Section 4. https://arxiv.org/pdf/2602.05489
2. D. P. Bertsekas, *Incremental Gradient, Subgradient, and Proximal Methods for Convex Optimization: A Survey*, arXiv:1507.01030v2, Sections 3–4. https://arxiv.org/pdf/1507.01030
3. N. Hermer, D. R. Luke and A. Sturm, *Nonexpansive Markov Operators and Random Function Iterations for Stochastic Fixed Point Problems*, arXiv:2205.15897v2 (2023), Sections 2 and 4. https://arxiv.org/pdf/2205.15897
4. J. E. Hutchinson, *Fractals and Self Similarity*, Indiana University Mathematics Journal 30 (1981), 713–747, doi:10.1512/iumj.1981.30.30055.
