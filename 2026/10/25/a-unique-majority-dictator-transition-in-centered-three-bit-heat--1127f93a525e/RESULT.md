# A unique majority–dictator transition in centered three-bit heat norms

## Finding

The operator norm of independent-coordinate continuous-time heat flow on three fair bits, **restricted to zero-mean real or complex functions**, has an exact two-branch formula and a unique positive-time change of norming Boolean function whenever the slowest flip rate is simple.

Let \(0<r_1\le r_2\le r_3\), let \(s_i(t)=e^{-2r_i t}\), and use the uniform probability measure on \(X=\{-1,1\}^3\). For the semigroup specified below,
\[
\left\|H_t\big|_{L^\infty_0(X)}\right\|_{\infty\to\infty}
=\max\left\{s_1(t),\,\frac{s_1(t)+s_2(t)+s_3(t)-s_1(t)s_2(t)s_3(t)}2\right\},\qquad t\ge0.
\]
Here \(L^\infty_0(X)=\{f:\sum_{x\in X}f(x)=0\}\), and the norm is induced by the pointwise supremum norm. The two branches are attained by the slow-coordinate dictator \(D(x)=x_1\) and the three-input majority \(M(x)=\operatorname{sgn}(x_1+x_2+x_3)\), respectively.

If \(r_1<r_2\), the majority branch strictly dominates for \(0<t<t_*\) and the dictator branch strictly dominates for \(t>t_*\), where the **unique** \(t_*>0\) is specified by
\[
s_1(t_*)\bigl(1+s_2(t_*)s_3(t_*)\bigr)=s_2(t_*)+s_3(t_*).
\]
Both branches agree at the transition, but their derivatives are different; the operator norm is continuous and is not differentiable at \(t_*\). The two Boolean extremizers are mutually incompatible, so no fixed input norms the entire semigroup at all positive times when the smallest rate is simple. If \(r_1=r_2\), majority strictly dominates for every \(t>0\) and gives one time-independent norming input. At \(t=0\), the norm is one.

For every fixed positive rate triple,
\[
\left\|H_t\big|_{L^\infty_0(X)}\right\|_{\infty\to\infty}
=1-2(r_1r_2+r_1r_3+r_2r_3)t^2+O_{r_1,r_2,r_3}(t^3)
\quad(t\downarrow0).
\]
In the simple-slowest-rate case, the large-time branch is exactly \(e^{-2r_1t}\) for **all** \(t\ge t_*\), not merely asymptotically.

## Assumptions and scope

Let \(\tau_i f(x_1,x_2,x_3)=f(x_1,\ldots,-x_i,\ldots,x_3)\). Set \(L=\sum_{i=1}^3r_i(I-\tau_i)\) and \(H_t=e^{-tL}\). Each coordinate is independently flipped with probability \(q_i(t)=(1-e^{-2r_it})/2\), giving a positive unital, uniform-measure-preserving Markov semigroup. No factor of two is hidden in the generator: the coordinate eigenvalue on \(x_i\) is \(2r_i\). The theorem holds for every \(r_i>0\) with the indicated ordering, all \(t\ge0\), and real or complex-valued functions. It concerns the restriction of \(H_t\) to the mean-zero subspace, not the full operator (whose supremum norm is always one).

## Proof

**1. The sharp finite-dimensional endpoint reduction.** Translation invariance makes all output-row norming problems equivalent. At \(x=(1,1,1)\), the transition probabilities for signs \(y=(y_1,y_2,y_3)\) are
\[
p_t(y)=\prod_{i=1}^3\frac{1+s_i(t)y_i}{2}.
\]
For real \(f\), maximize \(\sum_yp_t(y)f(y)\) under \(|f(y)|\le1\) and \(\sum_yf(y)=0\). Every extreme point of this seven-dimensional polytope has four entries \(+1\) and four entries \(-1\): at most one coordinate could be strictly between its bounds, but the other seven signs have odd sum and the zero-sum constraint forces the last entry to be a sign as well. Rearrangement therefore chooses the four largest probabilities. For complex \(f\), rotate the output to the nonnegative real axis and apply the same argument to \(\operatorname{Re}f\); hence exactly the same norm formula applies. Strict separation at the fourth-fifth probability threshold makes the maximizing sign vector unique up to a unimodular scalar for a fixed evaluation row.

**2. Only two sign configurations compete.** For \(t>0\), define \(a_i(t)=\log[(1+s_i(t))/(1-s_i(t))]=\log\coth(r_it)\). Then \(a_1\ge a_2\ge a_3>0\) and \(\log[p_t(y)/p_t(-y)]=\sum_i a_i y_i\). Among each antipodal pair exactly the more likely vertex belongs to the top four, except at an equality. If \(a_1<a_2+a_3\), the top four signs have positive coordinate sum and the optimizing function is \(M\). If \(a_1>a_2+a_3\), the top four all satisfy \(y_1=1\), and the optimizing function is \(D\). At equality both choices tie. The degree-one/degree-three identity
\[
M(y)=\frac{y_1+y_2+y_3-y_1y_2y_3}{2}
\]
shows that the majority value is \((s_1+s_2+s_3-s_1s_2s_3)/2\); the dictator value is \(s_1\). Their sign comparison is equivalent to the sign of \(a_2+a_3-a_1\), also obtained from the addition formula for \(\tanh\). This proves the exact two-branch formula.

**3. Strict one-crossing lemma.** Write \(h(u)=\log\coth u\) for \(u>0\). Since \(h'(u)=-2/\sinh(2u)\), set
\[
J(u)=\frac{h(u)\sinh(2u)}{2u}
=\int_0^\infty\frac{\sinh(2u)}{u\sinh(2u+2v)}\,dv.
\]
For each fixed \(v\ge0\), the logarithmic derivative of this integrand with respect to \(u\) is
\[
2\coth(2u)-2\coth(2u+2v)-\frac1u
\le\frac4{e^{4u}-1}-\frac1u<0.
\]
The bound follows from \(\coth(2u+2v)\ge1\) and \(e^{4u}-1>4u\). Consequently \(J\) is strictly decreasing and \(G(u)=-uh'(u)/h(u)=1/J(u)\) is strictly increasing. For any \(r<s\),
\[
\frac d{dt}\log\frac{h(rt)}{h(st)}
=\frac{G(st)-G(rt)}t>0.
\]
Therefore when \(r_1<r_2\), each ratio \(a_2/a_1\) and \(a_3/a_1\) is strictly decreasing (the latter also because \(r_3\ge r_2>r_1\)). Their sum decreases continuously from \(2\) as \(t\downarrow0\), since \(h(rt)=\log[1/(rt)]+o(1)\), to \(0\) as \(t\to\infty\), since \(h(rt)\sim2e^{-2rt}\). Hence exactly one \(t_*>0\) solves \(a_2+a_3=a_1\), equivalently the displayed multiplier equation. The crossing is transverse because the ratio sum has strictly negative derivative there. Thus the two analytic norm branches meet with unequal derivatives and their maximum has a genuine nondifferentiable point. If \(r_1=r_2\), then \(a_1=a_2<a_2+a_3\) for every finite positive time; no crossing occurs.

**4. Extremizer rigidity and expansions.** Away from the transition the rearrangement threshold is strict and the rowwise maximizer is uniquely the corresponding translated majority or dictator up to phase. Translation of an input changes only its signed argument and preserves essential-coordinate count; no majority truth table can also be a one-coordinate dictator, so no function norms the full positive-time family when \(r_1<r_2\). A fixed majority norms it when \(r_1=r_2\). Taylor-expanding \(e^{-2r_it}\) in the majority expression gives \(1-2\sum_{i<j}r_ir_jt^2+O(t^3)\), proving the claimed onset. Once the dictator branch wins it equals \(e^{-2r_1t}\) identically.

## Verification

The standalone script `checker.py` uses exact rational arithmetic to compare the closed formula with direct maximization over all \(\binom84=70\) balanced sign patterns for \(343\) independently selected rational multiplier triples, checks an exact branch tie, independently constructs heat rows for several continuous-time rate triples, and checks the quadratic short-time coefficient. It reports **371 passed grouped cases**. These finite computations are diagnostics only: steps 1–4 give the proof for arbitrary positive real rates and all times. An illustrative distinct-rate triple \((r_1,r_2,r_3)=(1,2,3)\) has \(t_*\approx0.19112254291987044\), numerically consistent with its defining equation.

## Relationship to prior work

The fair-bit noise operator, Walsh diagonalization, and majority Fourier polynomial are standard ingredients; their appearance alone is not proposed as new. Polyanskiy's 2013 hypercontractivity work studies spherical Hamming averages and familiar Bernoulli noise \(L^p\)-estimates, not the restricted centered endpoint norm or rate-dependent norming function. O'Donnell's 2014 Boolean Fourier text develops majority and noise stability, including homogeneous noise, but does not in the inspected material derive the present anisotropic three-coordinate centered operator-norm profile. Mori's 2016 three-input majority theorem studies a nonlocal-box bias-amplification objective rather than this endpoint Markov norm. The present contribution is the **complete fixed-rate semigroup profile and proof of a unique finite-time majority-to-dictator switch with an analytic cusp**; the optimal-four-atom rearrangement itself is classical.

## Limitations

The theorem is restricted to three independent fair binary coordinates, their centered supremum-norm function space, and strictly positive constant flip rates. It does not establish analogous single-transition behavior in dimensions four or greater, for nonproduct kernels, or under nonuniform stationary measures. The finite checker is not an infinite-parameter certificate. Equivalence to an unindexed classical optimal-voting or statistical-decision theorem is a remaining historical originality risk. No independent scientific audit is claimed.

## References

1. Y. Polyanskiy, *Hypercontractivity of spherical averages in Hamming space*, arXiv:1309.3014 (first public preprint 2013-09-12), https://arxiv.org/abs/1309.3014.
2. R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), ISBN 9781107038325; accessible revised author's text https://arxiv.org/abs/2105.10386.
3. R. Mori, *Three-input majority function as the unique optimal function for the bias amplification using nonlocal boxes*, arXiv:1604.05663 (first public preprint 2016-04-18), https://arxiv.org/abs/1604.05663.
