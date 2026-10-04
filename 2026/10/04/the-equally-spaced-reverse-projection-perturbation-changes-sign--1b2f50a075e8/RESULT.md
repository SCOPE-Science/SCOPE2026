# The equally spaced reverse-projection perturbation changes sign exactly in dimension nine
## Finding
For every integer \(n\ge 2\), define the centered equally spaced vector
\[
b_j=j-\frac{n+1}{2},\qquad 1\le j\le n,
\]
and, for sufficiently small \(\varepsilon\ge0\),
\[
a_\varepsilon=(-1,\varepsilon b_1,\ldots,\varepsilon b_n,1)\in\mathbb R^{n+2},\qquad
F_\varepsilon=\{\mathbf 1,a_\varepsilon\}^{\perp},\qquad
\lambda=\frac1{n+2}\mathbf1.
\]
Let \(C_{n+2}=[-1/2,1/2]^{n+2}\), and normalize the section/projection product by
\[
\Gamma_n(\varepsilon)=\frac{n!}{n+1}\,V_{F_\varepsilon}\!\left((\lambda+F_\varepsilon)\cap\Delta_{n+1}\right)V_{F_\varepsilon}\!\left(P_{F_\varepsilon}C_{n+2}\right).
\]
Then \(\Gamma_n(0)=1\) and
\[
\Gamma_n'(0+)=n\left(\frac{n-1}{12}-A_{n-1}\right),
\]
where
\[
A_d=\frac{2}{(d+1)!}\sum_{k=0}^{\lfloor d/2\rfloor}(-1)^k\binom dk\left(\frac d2-k\right)^{d+1}
=\mathbb E\left|U_1+\cdots+U_d\right|
\]
for independent \(U_i\sim\mathrm{Unif}[-1/2,1/2]\). The sign is exact:
\[
\Gamma_n'(0+)<0\quad(2\le n\le8),\qquad
\Gamma_n'(0+)>0\quad(n\ge9).
\]
Hence dimension nine is the exact first-order threshold for the direct equally spaced splitting used in the recent reverse-projection counterexample mechanism.

## Assumptions and scope
The statement concerns only this one-parameter family of codimension-two simplex sections and the associated projected cube. The restriction on \(\varepsilon\) is local; it is enough to take \(0\le\varepsilon<2/(n-1)\), which keeps all middle coordinates strictly between the two outer coordinates when \(\varepsilon>0\). The source's Proposition 4.2 identifies \(\Gamma_n>1\) with a strict violation of its simplex-section product threshold, and its Proposition 4.1 turns such a violation into a reverse-projection counterexample.

The conclusion for dimensions \(4\) through \(8\) is deliberately only a first-order obstruction for this direct arithmetic path. It neither proves the conjectured reverse-projection upper bound there nor excludes a different path, a nonlocal crossing, or a higher-order effect.

## Proof
Put \(D(a)=\sum_{i<j}|a_i-a_j|\). The source proves, for \(m=n+2\),
\[
V_{F_a}\!\left((\lambda+F_a)\cap\Delta_{n+1}\right)V_{F_a}(P_{F_a}C_{n+2})=\frac{D(a)f_a(0)}{(n+1)!}.
\]
For \(a_0=(-1,0,\ldots,0,1)\), one has \(D(a_0)=2(n+1)\). Parametrize a point of \(\Delta_{n+1}\) by the total middle mass \(w\), a normalized middle point \(p\in\Delta_{n-1}\), and the difference parameter of the two outer coordinates. The same calculation as in the source's Lemma 4.3 gives
\[
f_{a_\varepsilon}(0)=\frac{n+1}{2}\,I_n(\varepsilon),\qquad
I_n(\varepsilon)=\int_{\Delta_{n-1}}\left(1+\varepsilon|L_n(p)|\right)^{-n}d\bar p,
\]
where
\[
L_n(p)=\sum_{j=1}^n b_jp_j.
\]
Therefore
\[
\Gamma_n(\varepsilon)=\frac{D(a_\varepsilon)}{D(a_0)}I_n(\varepsilon).
\]
Because the middle coordinates remain between the two outer coordinates, all outer-middle contributions to \(D\) stay fixed, and
\[
D(a_\varepsilon)=D(a_0)+\varepsilon D(b).
\]
For the centered arithmetic progression,
\[
D(b)=\sum_{i<j}(b_j-b_i)=2\sum_{j=1}^n b_j^2.
\]
Uniform-simplex second moments give
\[
\mathbb E_{\Delta_{n-1}}L_n^2=\frac{\sum_j b_j^2}{n(n+1)},
\]
so
\[
\frac{D(b)}{D(a_0)}=n\,\mathbb E L_n^2.
\]
Differentiating the integral at the origin yields
\[
I_n'(0+)=-n\,\mathbb E|L_n|,
\]
and hence
\[
\Gamma_n'(0+)=n\left(\mathbb E L_n^2-\mathbb E|L_n|\right).
\]

To identify these moments, write a uniform point of \(\Delta_{n-1}\) as the successive gaps of ordered \(0\le x_1\le\cdots\le x_{n-1}\le1\). A telescoping sum gives
\[
L_n=\frac{n-1}{2}-\sum_{i=1}^{n-1}x_i.
\]
Both \(|L_n|\) and \(L_n^2\) are symmetric in the \(x_i\), so integrating over the ordered chamber is the same as integrating over the full cube. Thus \(L_n\) has, for these two moments, the same law as \(-S_d\), where \(d=n-1\) and
\[
S_d=U_1+\cdots+U_d,\qquad U_i\sim\mathrm{Unif}[-1/2,1/2].
\]
In particular,
\[
\mathbb E S_d^2=\frac d{12}.
\]
For \(X_d=S_d+d/2\), the Irwin--Hall density is the standard truncated-power density. Integrating \(2(d/2-X_d)_+\) gives the finite exact sum
\[
A_d=\mathbb E|S_d|=\frac{2}{(d+1)!}\sum_{k=0}^{\lfloor d/2\rfloor}(-1)^k\binom dk\left(\frac d2-k\right)^{d+1}.
\]
This proves the derivative formula.

For \(d=1,\ldots,12\), exact rational evaluation gives the derivative values, with \(n=d+1\):
\[
-\frac13,-\frac12,-\frac58,-\frac23,-\frac{239}{384},-\frac{29}{60},-\frac{5629}{23040},\frac{25}{252},\frac{1137217}{2064384},\frac{40417}{36288},\frac{3326800613}{1857945600},\frac{3683129}{1425600}.
\]
The sign first becomes positive at \(d=8\), equivalently \(n=9\). For every \(d\ge13\), Cauchy--Schwarz gives
\[
A_d\le\sqrt{\mathbb E S_d^2}=\sqrt{d/12}<d/12,
\]
so positivity persists for all larger dimensions. This completes the classification.

## Verification
The analytic proof reduces the only finite sign check to exact rational arithmetic for \(1\le d\le12\); dimensions \(d\ge13\) are covered uniformly by Cauchy--Schwarz. The accompanying `verify_threshold.py` evaluates the closed formula using Python's exact `Fraction` arithmetic, independently recomputes \(D(b)=2\sum b_j^2\), and checks the expected sign boundary. Its successful output is `VERIFY_OK`.

No floating-point computation is needed for the theorem. The checker is a reproducibility aid, not a substitute for the all-dimensional proof.

## Relationship to prior work
Feng, Hu, Liu, and Xu derive the exact section/projection product formula, introduce the nine-middle-coordinate vector \((-1,\varepsilon(-4,-3,\ldots,4),1)\), and prove that its first variation is positive. They then lift the resulting nine-dimensional counterexample to every higher dimension by adjoining zero coordinates. Their paper explicitly leaves dimensions \(4\) through \(8\) unresolved.

The present finding asks a different, mechanism-level question: what happens if the same direct equally spaced split is made with exactly \(n\) middle coordinates in every dimension? The answer is a complete sign classification. The source proves the positive \(n=9\) case and a separate lifting theorem; it does not state the direct all-dimensional derivative formula, the negative signs for \(n\le8\), or the exact first-order threshold.

A published-finding search for reverse projection, simplex sections, arithmetic-progression perturbations, and the Irwin--Hall formulation returned no statement implying this direct-path classification. The closest returned simplex-section result concerns stability of minimal central sections of a regular simplex, a different extremal functional and a different family of sections.

## Limitations
The derivative sign is local. For \(2\le n\le8\), a negative derivative only says this path initially moves below the threshold; it does not preclude a later crossing at finite \(\varepsilon\). The result also says nothing about other perturbation directions. Accordingly, it does not resolve the open reverse-projection problem in dimensions \(4\) through \(8\).

The literature comparison is strongest against the lead paper because its full construction and proof were inspected. Searches cannot exclude an independently stated equivalent result under remote terminology, so a small residual novelty risk remains.

## References
Y. Feng, S. Hu, W. Liu, and L. Xu, *On the Reverse Projection Inequality*, MathSciDoc:2608.23002, first public 2026-08-21; Zenodo DOI 10.5281/zenodo.22037130. Relevant portions: Proposition 4.2, Lemmas 4.3--4.4, Proposition 4.5, and the subsequent lifting argument.
