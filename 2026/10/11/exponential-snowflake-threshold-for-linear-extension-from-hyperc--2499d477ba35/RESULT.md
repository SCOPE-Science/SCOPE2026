# Exponential snowflake threshold for linear extension from hypercube vertices

## Finding

For each integer \(d\ge2\), let \(A_d=\{-1,1\}^d\subset\mathbb R^d\) and \(X_d=A_d\cup\{0\}\). Give \(X_d\) the snowflake metric \(\rho_\alpha(x,y)=\|x-y\|_2^\alpha\), with \(0<\alpha\le1\). Let \(\Lambda_d(\alpha)\) be the least Lipschitz-seminorm operator norm of any real-linear simultaneous extension \(E:\operatorname{Lip}(A_d;\mathbb R)\to\operatorname{Lip}(X_d;\mathbb R)\) satisfying \((Ef)|_{A_d}=f\). The unique optimal invariant extension assigns the arithmetic mean of the \(2^d\) vertex values to the origin, and its norm gives

\[
\Lambda_d(\alpha)=\max\left\{1,F_d(\alpha)\right\},\qquad
F_d(\alpha)=2^{-d}\sum_{k=1}^{d}\binom dk\left(2\sqrt{\frac{k}{d}}\right)^\alpha.
\]

There is a unique \(\alpha_d\in(0,1)\) such that \(F_d(\alpha_d)=1\). Consequently \(\Lambda_d(\alpha)=1\) precisely for \(0<\alpha\le\alpha_d\), and the contraction threshold has the two-term high-dimensional expansion

\[
\boxed{\;2^d\alpha_d=\frac{2}{\log2}+\frac{1}{(\log2)^2\,d}+O(d^{-2})\;}
\quad(d\to\infty).
\]

In particular, \(\alpha_d\sim 2^{1-d}/\log2\); the admissible exponents are exponentially small in cube dimension. Without snowflaking,

\[
\Lambda_d(1)=\sqrt2\left(1-\frac{1}{8d}+O(d^{-2})\right),
\]

so the optimal Lipschitz norm tends to \(\sqrt2\) for ordinary Euclidean distances. All error terms are for integers \(d\to\infty\), with absolute implicit constants.

## Assumptions and scope

We study **real-valued** Lipschitz functions and **real-linear** simultaneous extension operators. For a finite metric space \(Y\), the Lipschitz seminorm is

\[
[f]_{\mathrm{Lip}(Y)}=\max_{x\ne y\in Y}\frac{|f(x)-f(y)|}{\rho_\alpha(x,y)}.
\]

Boundedness in these seminorms forces an extension to preserve constants. Every \(E\) is determined by its linear functional for the one missing point, \((Ef)(0)\). For \(d\ge2\), all vertex-to-origin distances are \(d^{\alpha/2}\); two vertices differing in exactly \(k\) coordinates are \((2\sqrt k)^\alpha\) apart. The group of signed coordinate permutations fixes the origin and acts transitively on vertices. The parameter \(\alpha=0\) is used only as a **right-hand limit**, not as a metric exponent. The case \(d=1\) is elementary and excluded from the transition theorem: \(\Lambda_1(\alpha)=1\) throughout \(0<\alpha\le1\).

## Proof

**1. Optimality of the vertex mean.** Write \((Ef)(0)=\sum_{v\in A_d}c_v f(v)\). Preservation of constants yields \(\sum_v c_v=1\). Conjugating \(E\) by a signed coordinate permutation preserves its extension property and operator norm. Average all such conjugates. Convexity of the operator norm gives an invariant extension whose norm does not exceed \(\|E\|\). Transitivity forces every coefficient of its central functional to be \(2^{-d}\). Thus the uniform-mean operator attains the infimum over all, including signed-coefficient, real-linear extensions.

Fix \(v\in A_d\). If \([f]_{\mathrm{Lip}(A_d)}\le1\), then

\[
\left|2^{-d}\sum_{u\in A_d}f(u)-f(v)\right|
\le2^{-d}\sum_{u\in A_d}\|u-v\|_2^\alpha.
\]

Equality is attained by the admissible distance function \(f(u)=\rho_\alpha(u,v)\), since distance to a fixed point is one-Lipschitz in every metric space. Dividing by \(\rho_\alpha(0,v)=d^{\alpha/2}\), and observing that the input seminorm is unchanged on pairs of vertices, gives \(\Lambda_d(\alpha)=\max\{1,F_d(\alpha)\}\). Exactly \(\binom dk\) vertices differ from \(v\) in \(k\) coordinates, proving the displayed binomial sum. This is a global operator-norm identity, not just a calculation for the mean extension.

**2. Unique contractivity transition.** Put \(K_d\sim\operatorname{Bin}(d,1/2)\) and \(R_d=2\sqrt{K_d/d}\). For \(\alpha>0\), take \(R_d^\alpha=0\) when \(K_d=0\). Then \(F_d(\alpha)=\mathbb E R_d^\alpha\). Its right-hand limit at zero is \(1-2^{-d}<1\). Because the positive summand for \(K_d=d\) has \(\log R_d=\log2\ne0\), the finite sum has \(F_d''(\alpha)>0\) for every real \(\alpha\), after restricting to \(K_d\ge1\). At \(\alpha=1\), the inequality \(\sqrt t\ge t\) for \(0\le t\le1\) gives

\[
F_d(1)=2\mathbb E\sqrt{K_d/d}\ge2\mathbb E(K_d/d)=1.
\]

The inequality is strict for \(d\ge2\), because \(\mathbb P(0<K_d<d)>0\). Continuity and strict convexity therefore imply a unique root \(\alpha_d\in(0,1)\) of \(F_d(\alpha)=1\); indeed, at any crossing from the initial value below one, the secant and hence derivative are positive, so a second crossing is impossible. This proves the exact contractivity classification.

**3. Logarithmic binomial moment.** Let \(\varepsilon_d=2^{-d}\), and define the finite right derivative

\[
\mu_d=F_d'(0+)=2^{-d}\sum_{k=1}^d\binom dk\log\left(2\sqrt{k/d}\right).
\]

Set \(Z_d=(2K_d-d)/d\). On \(K_d\ge1\),

\[
\log R_d=\tfrac12\log2+\tfrac12\log(1+Z_d).
\]

One has \(\mathbb E Z_d=\mathbb E Z_d^3=0\), \(\mathbb E Z_d^2=1/d\), and \(\mathbb E Z_d^4=3/d^2-2/d^3\), by the symmetry and elementary binomial moments. Restrict to \(|Z_d|\le1/2\) and Taylor-expand

\[
\log(1+z)=z-\tfrac12z^2+\tfrac13z^3+O(z^4).
\]

The complementary binomial tail has probability at most \(2e^{-d/8}\) (Hoeffding's elementary binomial bound); on \(1\le K_d\le d\), the absolute logarithm is \(O(\log d)\). Deleting the event \(K_d=0\) affects bounded polynomial moments by \(O(2^{-d})\). Hence

\[
\boxed{\mu_d=\tfrac12\log2-\tfrac{1}{4d}+O(d^{-2}).}
\]

In particular \(\mu_d\ge\frac14\log2>0\) for all sufficiently large \(d\).

**4. Solving the exponentially small crossing.** For \(0\le t\le1\), the finite-sum second derivative satisfies

\[
0<F_d''(t)=\mathbb E\bigl[R_d^t(\log R_d)^2\mathbf1_{K_d\ge1}\bigr]
=O((\log d)^2),
\]

uniformly in \(t\), since \(2/\sqrt d\le R_d\le2\) on \(K_d\ge1\). Convexity gives \(F_d(\alpha)\ge1-\varepsilon_d+\mu_d\alpha\), and at the crossing this implies \(0<\alpha_d\le\varepsilon_d/\mu_d=O(2^{-d})\). Taylor's formula at zero then gives

\[
0=F_d(\alpha_d)-1=-\varepsilon_d+\mu_d\alpha_d
+O(\alpha_d^2(\log d)^2),
\]

so

\[
2^d\alpha_d=\frac1{\mu_d}+O(2^{-d}(\log d)^2)
=\frac{2}{\log2}+\frac{1}{(\log2)^2d}+O(d^{-2}).
\]

The coefficient of \(d^{-1}\) follows by expanding the reciprocal of \(\tfrac12\log2-\tfrac1{4d}+O(d^{-2})\).

**5. Ordinary Euclidean metric.** Using the same centered binomial variable,

\[
F_d(1)=\sqrt2\,\mathbb E\sqrt{1+Z_d}.
\]

On \(|Z_d|\le1/2\), Taylor's formula gives \(\sqrt{1+z}=1+z/2-z^2/8+z^3/16+O(z^4)\). The tail is exponentially small and \(\mathbb E Z_d=\mathbb E Z_d^3=0\), so \(F_d(1)=\sqrt2(1-1/(8d)+O(d^{-2}))\). Since \(F_d(1)>1\) for \(d\ge2\), this is also \(\Lambda_d(1)\).

## Verification

Run the self-contained Python standard-library program \(`verify_cube_extension.py`\) from the directory containing this file:

`python3 verify_cube_extension.py`

A replay returned `VERIFY_OK distance_witness_pairs=86360 scalar_checks=73`, with threshold approximations \(\alpha_2=0.611516173\), \(\alpha_3=0.352841879\), and \(\alpha_4=0.191981864\). The program checks all ordered distinct vertex pairs in dimensions one through seven, for four nonzero snowflake exponents, verifying that distance-to-vertex functions saturate the averaging bound. It also brackets the unique crossing for dimensions two through eighteen and checks the two-vertex and square boundary identities. These finite tests do not establish existence, uniqueness or asymptotics for arbitrary dimension; those follow from the proof above.

## Relationship to prior work

Ambrosio and Puglisi (initial public version 2016) developed random projections and their equivalence with weak-star continuous simultaneous linear Lipschitz extensions. The uniform probability measure on the cube vertices is an instance of their mechanism, but the cited article gives neither the exact cube-center seminorm nor the transition exponent or its two-term exponential expansion. Brudnyi and Brudnyi (2004, 2006) establish existence and bounds for broad metric-space families; their cube/lattice discussions do not calculate the present sharp one-added-point constant. The present exact cube-center threshold and its exponential two-term expansion are not consequences of the general existence bounds alone.

## Limitations

The finding concerns scalar real functions on the finite vertex set of a **Euclidean** hypercube, a single added center, and \(0<\alpha\le1\). It is not a theorem about extension to the full solid cube, arbitrary subsets or added points, vector-valued maps, or arbitrary norms on the ambient \(\mathbb R^d\). The asymptotic \(O(d^{-2})\) applies only as \(d\to\infty\); the exact implicit finite-dimensional norm is the binomial sum. Finite computational checks are corroborative rather than infinite-dimensional certificates.

## References

1. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, first publicly posted 2 September 2016; arXiv:1609.01450v1 (6 September 2016), Sections 1–2, especially Theorems 2.14–2.15. https://arxiv.org/abs/1609.01450 ; https://cvgmt.sns.it/paper/3155/ . The preprint lists primary classifications 26A16 and 47B38.
2. A. Brudnyi and Yu. Brudnyi, *Metric spaces with linear extensions preserving Lipschitz condition*, arXiv:math/0404304 (first posted 17 April 2004), Sections 1–2 and 10. https://arxiv.org/abs/math/0404304 .
3. A. Brudnyi and Yu. Brudnyi, *Extension of Lipschitz functions defined on metric subspaces of homogeneous type*, arXiv:math/0609535 (19 September 2006), Theorem 1.2. https://arxiv.org/abs/math/0609535 .
