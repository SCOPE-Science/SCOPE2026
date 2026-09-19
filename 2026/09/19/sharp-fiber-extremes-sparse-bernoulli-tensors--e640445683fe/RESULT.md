# Sharp fiber-extreme barriers for sparse Bernoulli tensor norms

## Statement

Let \(k\ge 2\) be fixed. For each \(n\), let
\[
T=(T_{i_1,\ldots,i_k})\in\{0,1\}^{n\times\cdots\times n}
\]
have independent \(\operatorname{Bernoulli}(p_n)\) entries, put \(d_n=np_n\), and write
\[
W=T-\mathbb ET.
\]
A one-dimensional fiber is obtained by fixing \(k-1\) indices and varying the remaining one. Let
\[
D_n^{\max}=\max_F\sum_{\mathbf i\in F}T_{\mathbf i}
\]
be the largest uncentered fiber degree over all \(k n^{k-1}\) fibers, and let
\[
L_n^{\max}=\max_F\|W_F\|_2
\]
be the largest centered fiber Euclidean norm. The injective norm satisfies
\[
\|W\|\ge L_n^{\max}.
\]

Define the Poisson large-deviation rate
\[
h(x)=x\log x-x+1,\qquad x\ge1.
\]

### 1. Exact first-order profile at logarithmic sparsity

Assume
\[
\frac{d_n}{\log n}\longrightarrow c\in(0,\infty).
\]
Let \(x_{k,c}>1\) be the unique solution
\[
c\,h(x_{k,c})=k-1.
\]
Then
\[
\boxed{\frac{D_n^{\max}}{d_n}\xrightarrow{\mathbb P}x_{k,c}}
\]
and, since \(p_n\to0\),
\[
\boxed{\frac{L_n^{\max}}{\sqrt{d_n}}\xrightarrow{\mathbb P}\sqrt{x_{k,c}}}.
\]
Consequently, for every \(\varepsilon>0\),
\[
\boxed{
\mathbb P\!\left\{\frac{\|W\|}{\sqrt{d_n}}\ge \sqrt{x_{k,c}}-\varepsilon\right\}
\longrightarrow 1.
}
\]

Thus the logarithmic-sparsity threshold has a nontrivial constant inflation coming purely from the \(n^{k-1}\) fiber extremes. For example, when \(k=3\) and \(c=2\),
\[
h(x_{3,2})=1,
\]
so \(x_{3,2}=e\) and
\[
L_n^{\max}/\sqrt{d_n}\to\sqrt e.
\]

### 2. Second-order localization and the lattice extreme profile

Assume for this part that
\[
d_n=c\log n
\]
exactly, up to the harmless choice \(p_n=d_n/n\). Put \(x_*=x_{k,c}\) and
\[
b_n=x_*c\log n-\frac{\log\log n}{2\log x_*}.
\]
Then
\[
\boxed{D_n^{\max}=b_n+O_{\mathbb P}(1)}
\]
and
\[
\boxed{(L_n^{\max})^2=b_n+O_{\mathbb P}(1).}
\]

More precisely, restrict to the \(n^{k-1}\) mutually independent fibers in any one fixed mode, and let \(M_n^{(1)}\) be their maximum degree. Define
\[
A_{k,c}=
\frac{\sqrt{x_*}}{(x_*-1)\sqrt{2\pi c}}.
\]
For any integer sequence \(m_n\) such that
\[
z_n:=m_n-b_n\longrightarrow z\in\mathbb R,
\]
one has the lattice extreme profile
\[
\boxed{
\mathbb P\{M_n^{(1)}<m_n\}
\longrightarrow
\exp\!\left(-A_{k,c}x_*^{-z}\right).
}
\]
The absence of a single continuously normalized Gumbel limit is the usual lattice effect for discrete extremes; the displayed formula gives the subsequential profile at the natural \(O(1)\) scale.

### 3. Sharp polynomial-tail fiber obstruction

For any fixed \(C>1\) with
\[
c\,h(C^2)>k-1,
\]
the full collection of fibers satisfies
\[
\boxed{
\mathbb P\{L_n^{\max}>C\sqrt{d_n}\}
=
n^{\,k-1-c h(C^2)+o(1)}.
}
\]
If \(c\,h(C^2)<k-1\), that probability tends to one.

Therefore, for a fixed target exponent \(r>0\), define \(x_{k,c,r}>1\) by
\[
c\,h(x_{k,c,r})=k-1+r.
\]
Any fixed constant \(C\) for which a spectral-norm estimate of the form
\[
\mathbb P\{\|W\|>C\sqrt{d_n}\}\le n^{-r}
\]
holds throughout the boundary regime \(d_n=c\log n\) must satisfy
\[
\boxed{
C\ge \sqrt{x_{k,c,r}}
=
\sqrt{h^{-1}\!\left(\frac{k-1+r}{c}\right)}.
}
\]
This gives an explicit necessary dependence of a polynomial-tail spectral-norm constant on tensor order, sparsity constant, and requested tail exponent.

For \(k=3,c=2,r=2\),
\[
x_{3,2,2}=3.591121476668\ldots,\qquad
C\ge1.895025455414\ldots.
\]

### 4. Sublogarithmic refinement

Assume
\[
1\le d_n=o(\log n).
\]
Let \(x_n>1\) be the solution
\[
d_n h(x_n)=(k-1)\log n.
\]
Then \(x_n\to\infty\) and
\[
\boxed{
\frac{D_n^{\max}}{d_nx_n}\xrightarrow{\mathbb P}1,
\qquad
L_n^{\max}=(1+o_{\mathbb P}(1))\sqrt{d_nx_n}.
}
\]
Hence
\[
\boxed{
\frac{\|W\|}{\sqrt{d_n}}
\ge(1-o_{\mathbb P}(1))\sqrt{x_n}\longrightarrow\infty.
}
\]
When \((k-1)\log n/d_n>1\), the solution has the exact Lambert-\(W\) representation
\[
x_n=
\frac{a_n-1}{W_0((a_n-1)/e)},
\qquad
a_n=\frac{(k-1)\log n}{d_n}.
\]
This refines the previously stated qualitative \(\omega(\sqrt d)\) fiber obstruction below logarithmic sparsity.

## Proof

### Fiber identity

Fix a fiber \(F\), and let \(D_F\) be its number of ones. Exactly \(D_F\) centered entries equal \(1-p_n\), while the other \(n-D_F\) entries equal \(-p_n\). Thus
\[
\|W_F\|_2^2
=D_F(1-p_n)^2+(n-D_F)p_n^2
=(1-2p_n)D_F+d_np_n.
\]
The tensor injective norm dominates every fiber norm by fixing the other \(k-1\) test vectors to coordinate basis vectors.

### Binomial upper-tail exponent

For any fixed \(x>1\), if \(d_n\asymp\log n\), then \(p_n=d_n/n\to0\) and, for \(D\sim\operatorname{Bin}(n,p_n)\),
\[
\log\mathbb P\{D\ge xd_n\}
=-d_n h(x)+o(d_n).
\]
The upper bound is Chernoff. For the lower bound, take the single mass at \(m=\lceil xd_n\rceil\). Since \(m=O(\log n)=o(n)\), Stirling's formula gives
\[
\log\mathbb P\{D=m\}
=-d_n h(m/d_n)+O(\log d_n)+o(1),
\]
which has the same exponential rate.

There are \(n^{k-1}\) disjoint fibers in any fixed mode, hence their degrees are independent. Across all modes there are only \(kn^{k-1}\) fibers. Therefore, writing
\[
q_n(x)=\mathbb P\{D\ge xd_n\}
=n^{-c h(x)+o(1)},
\]
the lower bound from one fixed mode and the upper union bound over all modes yield
\[
\mathbb P\{D_n^{\max}\ge xd_n\}\to1
\quad\text{if }c h(x)<k-1,
\]
while, if \(c h(x)>k-1\),
\[
\mathbb P\{D_n^{\max}\ge xd_n\}
=n^{k-1-c h(x)+o(1)}.
\]
This proves the first-order maximum-degree statement and the polynomial-tail exponent. The centered-fiber conclusions follow from the exact fiber identity and \(p_n\to0\).

### Second-order tail

Now take \(d_n=c\log n\) and \(m/d_n\to x>1\). Because \(m=O(\log n)\), the binomial mass is asymptotically Poisson at this scale:
\[
\mathbb P\{\operatorname{Bin}(n,d_n/n)=m\}
=(1+o(1))e^{-d_n}\frac{d_n^m}{m!}.
\]
For \(m/d_n\to x>1\), the successive upper-tail mass ratios tend to \(1/x\), so
\[
\mathbb P\{D\ge m\}
\sim
\frac{x}{x-1}
e^{-d_n}\frac{d_n^m}{m!}
\sim
\frac{\sqrt{x}}{(x-1)\sqrt{2\pi d_n}}
\exp\{-d_n h(m/d_n)\}.
\]
Take
\[
m_n=x_*d_n-\frac{\log\log n}{2\log x_*}+z_n.
\]
Taylor expansion of the rate gives
\[
d_nh(m_n/d_n)
=(k-1)\log n
-\frac12\log\log n
+z_n\log x_*+o(1).
\]
Hence for one fixed mode,
\[
n^{k-1}\mathbb P\{D\ge m_n\}
\to
A_{k,c}x_*^{-z}
\]
whenever \(z_n\to z\). Independence then gives
\[
\mathbb P\{M_n^{(1)}<m_n\}
=
\left(1-\mathbb P\{D\ge m_n\}\right)^{n^{k-1}}
\to
e^{-A_{k,c}x_*^{-z}}.
\]
The lower bound from one mode and the upper bound over the \(k\) modes show that the full maximum differs from \(b_n\) by \(O_{\mathbb P}(1)\). The fiber identity changes the squared centered norm by \(o(1)\) on this \(O(\log n)\) degree scale.

### Sublogarithmic regime

Let
\[
a_n=\frac{(k-1)\log n}{d_n}\to\infty,
\qquad h(x_n)=a_n.
\]
For each fixed \(\varepsilon\in(0,1)\),
\[
\frac{h((1\pm\varepsilon)x_n)}{h(x_n)}
\longrightarrow 1\pm\varepsilon,
\]
because \(h(x)\sim x\log x\). The same one-mass lower bound and Chernoff upper bound, now at thresholds \(d_n(1\pm\varepsilon)x_n\), imply that among one mode's \(n^{k-1}\) independent fibers the lower threshold is exceeded with probability tending to one, while a union bound over all fibers makes the upper threshold vanish. Thus
\[
D_n^{\max}/(d_nx_n)\to1
\]
in probability. The remaining claims follow from the fiber identity. Solving
\[
x(\log x-1)=a_n-1
\]
gives the stated Lambert-\(W\) formula.

## Context and originality boundary

Zhou and Zhu's 2026 preprint proves the log-free upper bound
\[
\|T-\mathbb ET\|\le C_{k,r,c}\sqrt{np}
\]
with failure probability at most \(n^{-r}\) for \(np\ge c\log n\). It explicitly observes that the tensor norm dominates the maximum fiber norm, proves a fixed-fiber \(\sqrt d\) lower bound at logarithmic sparsity, and states that the maximum fiber norm is \(\omega(\sqrt d)\) when \(1\le d=o(\log n)\). Its Lemma 4.3 uses
\[
h(\kappa)=\kappa\log\kappa-\kappa+1
\]
inside a Chernoff/union-bound argument to obtain a nonsharp bounded-degree constant. The preprint does not state the exact \(x_{k,c}\) logarithmic-sparsity profile, the second-order \(-(\log\log n)/(2\log x_{k,c})\) localization, or the explicit necessary \(n^{-r}\) spectral-norm constant barrier above.

The scalar extreme-value ingredients are classical and are **not** claimed as new in isolation. Anderson, Coles and Hüsler (1997) study maxima of Poisson-like variables and triangular arrays, and older random-graph work such as Bollobás (1982) studies degree extremes in logarithmic regimes. The originality claim here is restricted to applying the sharp fiber-extreme profile to the independent-entry Bernoulli tensor injective norm, extracting the explicit lower constant and polynomial-tail barrier for the new Zhou--Zhu concentration theorem, and giving the corresponding sublogarithmic quantitative refinement.

To the best of our knowledge, searches by source paper, "maximum fiber degree", "fiber norm", logarithmic sparsity, the rate \(x\log x-x+1\), and equivalent spectral-norm lower-bound formulations did not locate these tensor-specific statements. The full text of Anderson--Coles--Hüsler (1997) was not directly inspected; its abstract and bibliographic record were inspected. It is therefore a residual originality risk for the scalar triangular-array extreme formulas, but not evidence that the tensor-norm translation has appeared previously.

## Limitations

- The tensor entries are homogeneous independent Bernoulli variables.
- The exact second-order profile is stated for \(d_n=c\log n\); a perturbation of \(d_n\) on the \(\log\log n\) scale shifts the center and must be tracked explicitly.
- The exact lattice limit is proved for the maximum over one fixed mode, whose fibers are independent. For the maximum over all modes, only \(O_{\mathbb P}(1)\) localization is asserted because fibers from different modes overlap.
- These are lower bounds and obstruction profiles. They do not identify the full limiting constant of \(\|T-\mathbb ET\|/\sqrt d\), which may exceed the maximum-fiber contribution.
- The scalar discrete-extreme mechanism has substantial classical prior art; novelty is claimed only for the tensor-specific consequences described above.

## Verification

`artifacts/verify_fiber_extremes.py` evaluates exact binomial tails using a stable probability-mass recurrence and compares the one-mode maximum distribution with the second-order lattice profile. `artifacts/verification.txt` contains its deterministic output.

## References

1. Zhixin Zhou and Yizhe Zhu, *Sharp spectral norm concentration of sparse random tensors*, arXiv:2609.20520v1 (2026). https://arxiv.org/abs/2609.20520
2. Zhixin Zhou and Yizhe Zhu, *Sparse random tensors: Concentration, regularization and applications*, Electronic Journal of Statistics 15(1), 2483--2516 (2021). https://doi.org/10.1214/21-EJS1838
3. C. W. Anderson, S. G. Coles and J. Hüsler, *Maxima of Poisson-like variables and related triangular arrays*, Annals of Applied Probability 7, 953--971 (1997). https://doi.org/10.1214/aoap/1043862420
4. Béla Bollobás, *Vertices of given degree in a random graph*, Journal of Graph Theory 6, 147--155 (1982). https://doi.org/10.1002/jgt.3190060209
