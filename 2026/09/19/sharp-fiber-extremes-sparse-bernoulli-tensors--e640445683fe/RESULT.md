# Sharp fiber-extreme barriers for sparse Bernoulli tensor norms

## Statement

Let \(k\ge2\) be fixed and let \(T\in\{0,1\}^{n\times\cdots\times n}\) be an order-\(k\) tensor with independent \(\operatorname{Bernoulli}(p_n)\) entries. Put \(d_n=np_n\) and \(W=T-\mathbb ET\). For a one-dimensional fiber \(F\), let \(D_F\) be its number of ones. Define
\[
D_n^{\max}=\max_F D_F,\qquad L_n^{\max}=\max_F\|W_F\|_2,
\]
where the maximum is over all \(k n^{k-1}\) fibers. The injective norm satisfies \(\|W\|\ge L_n^{\max}\).

Write
\[
h(x)=x\log x-x+1,\qquad x\ge1.
\]

### Logarithmic sparsity

Assume \(d_n/\log n\to c\in(0,\infty)\), and let \(x_{k,c}>1\) be the unique solution
\[
c h(x_{k,c})=k-1.
\]
Then
\[
\boxed{\frac{D_n^{\max}}{d_n}\xrightarrow{\mathbb P}x_{k,c}},\qquad
\boxed{\frac{L_n^{\max}}{\sqrt{d_n}}\xrightarrow{\mathbb P}\sqrt{x_{k,c}}}.
\]
Consequently, for every \(\varepsilon>0\),
\[
\boxed{\mathbb P\!\left\{\frac{\|W\|}{\sqrt{d_n}}\ge\sqrt{x_{k,c}}-\varepsilon\right\}\to1.}
\]
For example, \(k=3,c=2\) gives \(x_{3,2}=e\), hence a compulsory fiber constant \(\sqrt e\).

### Second-order localization

Assume now \(d_n=c\log n\) exactly and put \(x_*=x_{k,c}\). Define
\[
b_n=x_*c\log n-\frac{\log\log n}{2\log x_*}.
\]
Then
\[
\boxed{D_n^{\max}=b_n+O_{\mathbb P}(1)},\qquad
\boxed{(L_n^{\max})^2=b_n+O_{\mathbb P}(1)}.
\]
For the \(n^{k-1}\) mutually independent fibers in any one fixed mode, let \(M_n^{(1)}\) be the maximum degree and define
\[
A_{k,c}=\frac{\sqrt{x_*}}{(x_*-1)\sqrt{2\pi c}}.
\]
If integers \(m_n\) satisfy \(m_n-b_n\to z\), then
\[
\boxed{\mathbb P\{M_n^{(1)}<m_n\}\to
\exp\!\left(-A_{k,c}x_*^{-z}\right).}
\]
Thus the natural second-order object is a lattice extreme profile rather than a single continuously normalized Gumbel law.

### Polynomial-tail obstruction

For fixed \(C>1\), if \(c h(C^2)>k-1\), then
\[
\boxed{\mathbb P\{L_n^{\max}>C\sqrt{d_n}\}
=n^{k-1-c h(C^2)+o(1)}.}
\]
If \(c h(C^2)<k-1\), this probability tends to one. Hence for \(r>0\), if \(x_{k,c,r}>1\) solves
\[
c h(x_{k,c,r})=k-1+r,
\]
then any fixed \(C\) for which
\[
\mathbb P\{\|W\|>C\sqrt{d_n}\}\le n^{-r}
\]
holds throughout \(d_n=c\log n\) must satisfy
\[
\boxed{C\ge\sqrt{x_{k,c,r}}=
\sqrt{h^{-1}\!\left(\frac{k-1+r}{c}\right)}.}
\]
For \(k=3,c=2,r=2\), this gives \(x_{3,2,2}=3.591121476668\ldots\) and \(C\ge1.895025455414\ldots\).

### Sublogarithmic refinement

Assume \(1\le d_n=o(\log n)\), and let \(x_n>1\) solve
\[
d_n h(x_n)=(k-1)\log n.
\]
Then \(x_n\to\infty\) and
\[
\boxed{\frac{D_n^{\max}}{d_nx_n}\xrightarrow{\mathbb P}1},\qquad
\boxed{L_n^{\max}=(1+o_{\mathbb P}(1))\sqrt{d_nx_n}}.
\]
Therefore
\[
\boxed{\frac{\|W\|}{\sqrt{d_n}}\ge(1-o_{\mathbb P}(1))\sqrt{x_n}\to\infty.}
\]
Writing \(a_n=(k-1)\log n/d_n\), one has the exact representation
\[
\boxed{x_n=\frac{a_n-1}{W_0((a_n-1)/e)}}
\]
whenever \(a_n>1\).

## Proof

For every fiber,
\[
\|W_F\|_2^2=D_F(1-p_n)^2+(n-D_F)p_n^2
=(1-2p_n)D_F+d_np_n.
\]
The tensor injective norm dominates each fiber norm by fixing the other \(k-1\) arguments at coordinate vectors. In a fixed mode the \(n^{k-1}\) fibers partition the entries, so their degrees are independent \(\operatorname{Bin}(n,p_n)\); all modes together contribute only the fixed factor \(k\).

If \(d_n\asymp\log n\), then for fixed \(x>1\) and \(D\sim\operatorname{Bin}(n,p_n)\), Chernoff's bound plus a one-mass Stirling lower bound gives
\[
\log\mathbb P\{D\ge x d_n\}=-d_nh(x)+o(d_n).
\]
Thus, when \(d_n/\log n\to c\),
\[
q_n(x):=\mathbb P\{D\ge x d_n\}=n^{-c h(x)+o(1)}.
\]
If \(c h(x)<k-1\), the maximum among one fixed mode's \(n^{k-1}\) independent fibers exceeds \(xd_n\) with probability tending to one. If \(c h(x)>k-1\), the all-mode union bound and the one-mode lower bound give
\[
\mathbb P\{D_n^{\max}\ge xd_n\}=n^{k-1-c h(x)+o(1)}.
\]
This proves the first-order threshold and the polynomial-tail exponent, and the centered-fiber statements follow from the exact fiber identity and \(p_n\to0\).

For the second-order term, take \(d_n=c\log n\) and \(m/d_n\to x>1\). Since \(m=O(\log n)\), the binomial mass is relatively Poisson:
\[
\mathbb P\{D=m\}=(1+o(1))e^{-d_n}\frac{d_n^m}{m!}.
\]
The successive upper-tail mass ratios tend to \(1/x\), so Stirling's formula gives
\[
\mathbb P\{D\ge m\}\sim
\frac{\sqrt{x}}{(x-1)\sqrt{2\pi d_n}}
\exp\{-d_nh(m/d_n)\}.
\]
For
\[
m_n=x_*d_n-\frac{\log\log n}{2\log x_*}+z_n,
\]
Taylor expansion yields
\[
d_nh(m_n/d_n)=(k-1)\log n-\frac12\log\log n+z_n\log x_*+o(1).
\]
Hence
\[
n^{k-1}\mathbb P\{D\ge m_n\}\to A_{k,c}x_*^{-z}
\]
when \(z_n\to z\), and independence gives the displayed one-mode lattice law. A one-mode lower bound and all-mode union upper bound give \(D_n^{\max}=b_n+O_{\mathbb P}(1)\). The fiber identity changes the squared centered norm by \(o(1)\) on this degree scale.

Finally, in the sublogarithmic regime define \(x_n\) by \(h(x_n)=(k-1)\log n/d_n\). Since \(x_n\to\infty\) and \(h(x)\sim x\log x\), for fixed \(\varepsilon\in(0,1)\),
\[
\frac{h((1\pm\varepsilon)x_n)}{h(x_n)}\to1\pm\varepsilon.
\]
The same one-mass lower bound and Chernoff upper bound then separate the lower and upper thresholds by powers of \(n\), proving \(D_n^{\max}/(d_nx_n)\to1\). Solving \(x(\log x-1)=a_n-1\) gives the Lambert-\(W\) expression.

## Context and originality boundary

Zhou and Zhu's 2026 preprint proves an order-optimal log-free upper bound \(\|T-\mathbb ET\|\le C_{k,r,c}\sqrt{np}\) with failure probability at most \(n^{-r}\) for \(np\ge c\log n\). It notes the fiber obstruction, proves the \(\sqrt d\) scale from a fixed fiber at logarithmic sparsity, and states that the maximum fiber norm is \(\omega(\sqrt d)\) when \(1\le d=o(\log n)\). Its maximum-degree lemma uses the same rate \(h(\kappa)\) with a sufficient constant containing slack. The preprint does not state the exact equation \(c h(x)=k-1\), the \(-\log\log n/(2\log x)\) localization, or the explicit necessary \(n^{-r}\) constant barrier above.

The scalar extreme-value ingredients are classical and are not claimed as new. Anderson, Coles and Hüsler (1997) study maxima of Poisson-like triangular arrays, and Bollobás (1982) studies degree extremes in logarithmic random-graph regimes. No novelty claim is made for the scalar maximum law or the \(k=2\) row/column specialization. The claim is restricted to the tensor-specific consequences for the new sparse-tensor concentration theorem: the explicit \((k,c)\) fiber constant, second-order localization, polynomial-tail obstruction, necessary dependence on \((k,c,r)\), and quantitative sublogarithmic refinement.

To the best of our knowledge, searches by the source paper, maximum fiber degree, fiber norm, logarithmic sparsity, the rate \(x\log x-x+1\), and equivalent spectral-norm lower-bound formulations did not locate these tensor-specific statements. The full Anderson--Coles--Hüsler (1997) article was not directly inspected; its abstract and bibliographic record were inspected, leaving residual originality uncertainty for the scalar component.

## Limitations

- Homogeneous independent Bernoulli entries only.
- The exact second-order center is stated for \(d_n=c\log n\); perturbations on the \(\log\log n\) scale must be tracked explicitly.
- The exact lattice law is for one fixed mode. Across all modes, overlapping fibers justify only \(O_{\mathbb P}(1)\) localization here.
- The result is a lower obstruction and does not determine the full limiting constant of the tensor injective norm.
- Classical discrete-extreme theory may subsume the scalar maximum calculation.

## Verification

`artifacts/verify_fiber_extremes.py` evaluates exact binomial tails and compares the one-mode maximum distribution with the second-order lattice profile. `artifacts/verification.txt` contains its deterministic output.

## References

1. Zhixin Zhou and Yizhe Zhu, *Sharp spectral norm concentration of sparse random tensors*, arXiv:2609.20520v1 (2026). https://arxiv.org/abs/2609.20520
2. Zhixin Zhou and Yizhe Zhu, *Sparse random tensors: Concentration, regularization and applications*, Electronic Journal of Statistics 15(1), 2483--2516 (2021). https://doi.org/10.1214/21-EJS1838
3. C. W. Anderson, S. G. Coles and J. Hüsler, *Maxima of Poisson-like variables and related triangular arrays*, Annals of Applied Probability 7, 953--971 (1997). https://doi.org/10.1214/aoap/1043862420
4. Béla Bollobás, *Vertices of given degree in a random graph*, Journal of Graph Theory 6, 147--155 (1982). https://doi.org/10.1002/jgt.3190060209
