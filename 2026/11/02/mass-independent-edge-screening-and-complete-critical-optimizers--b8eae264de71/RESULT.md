# Mass-independent edge screening and complete critical optimizers for priced reversible cycles

## Finding

The edge price at which an entire optional closing edge is optimally discarded is **exactly**
\[
q_c=\left(\sum_{i=1}^{n-1}\sqrt{p_i}\right)^2,
\]
independent of all positive vertex masses. Above this cutoff the unique optimum is a completely explicit weighted path. Below it every optimum retains the closing edge. At equality, the **complete unrestricted optimal set** is a nontrivial, explicitly computable closed line segment, not merely a symmetric subfamily.

The theorem specifies all designs at or above the cutoff. It does **not** solve the exact optimal value for every price below the cutoff.

## Assumptions and scope

Take any integer \(n\ge3\). Vertices \(1,\ldots,n\) have arbitrary masses \(m_i>0\), with \(M=\operatorname{diag}(m_1,\ldots,m_n)\). The graph has path edges \(\{i,i+1\}\) of independently selectable conductances \(w_i\ge0\), with fixed positive prices \(p_i\), and one closing edge \(\{1,n\}\), of independently selectable conductance \(t\ge0\) at positive price \(q\). The budget is \(B>0\):
\[
\sum_{i=1}^{n-1}p_iw_i+qt\le B.
\]
The graph Laplacian is \(L(w,t)=\sum_iw_i(e_i-e_{i+1})(e_i-e_{i+1})^\mathsf{T}+t(e_1-e_n)(e_1-e_n)^\mathsf{T}\). The objective is the smallest positive generalized eigenvalue of \(Lu=\lambda Mu\), equivalently the relaxation rate of the reversible continuous-time chain with generator \(-M^{-1}L\). This normalization is important: no unmentioned row-stochastic constraint is imposed.

Define
\[
\ell_i=\sqrt{p_i},\quad z_1=0,\quad z_{i+1}=z_i+\ell_i,\quad S=z_n=\sum_{i=1}^{n-1}\ell_i,
\]
\[
\mu=\frac{\sum_i m_iz_i}{\sum_i m_i},\quad f_i=z_i-\mu,\quad V=\sum_i m_i f_i^2>0,
\]
\[
G_i=\sum_{j=1}^{i}m_j(\mu-z_j)>0,\quad \Lambda=\frac BV,\quad w_i^0=\frac{\Lambda G_i}{\ell_i},\quad q_c=S^2.
\]
All sums over path edges run from \(1\) to \(n-1\); all vertex sums run from \(1\) to \(n\). Strict positivity of \(G_i\) follows because the mass-weighted mean of a strict initial segment of the strictly increasing sequence \(z_i\) is smaller than the mean of all vertices.

**Theorem.** For \(q>q_c\), the unique global optimal conductances are \((w_1^0,\ldots,w_{n-1}^0,t=0)\) and the optimal gap is \(\Lambda\). For \(0<q<q_c\), the optimal gap is strictly greater than \(\Lambda\), and **every** optimal conductance vector has \(t>0\). For \(q=q_c\), the optimal gap is \(\Lambda\) and **every and only** optimal conductance vector is
\[
w_i(t)=w_i^0-\frac{tS}{\ell_i},\qquad 0\le t\le t_*.
\]
Here the fully specified, positive endpoint \(t_*\) is calculated as follows. Let
\[
E=\left\{g\in\mathbb R^n:\sum_i m_i g_i=0,\quad\sum_i m_if_ig_i=0\right\}.
\]
For \(g\in E\setminus\{0\}\), define
\[
A(g)=\sum_{i=1}^{n-1}w_i^0(g_{i+1}-g_i)^2-\Lambda\sum_i m_ig_i^2,
\]
\[
R(g)=S\sum_{i=1}^{n-1}\frac{(g_{i+1}-g_i)^2}{\ell_i}-(g_n-g_1)^2.
\]
Then \(A(g)>0\) and \(R(g)>0\) and
\[
t_{\mathrm{edge}}=\min_i\frac{w_i^0\ell_i}{S},\qquad
 t_{\mathrm{spectral}}=\min_{g\in E\setminus\{0\}}\frac{A(g)}{R(g)},\qquad
 t_*=\min\{t_{\mathrm{edge}},t_{\mathrm{spectral}}\}>0.
\]
This is a finite-dimensional generalized eigenvalue minimum on an \((n-2)\)-dimensional space; the minimum is attained. The theorem makes no assertion that every ordinary edge stays positive below the closing-edge price threshold.

## Proof

**1. Sharp path comparison and its uniqueness.** For an arbitrary real vector \(g\), let \(\bar g=\sum_im_ig_i/\sum_im_i\) and \(\delta_i=g_{i+1}-g_i\). The weighted variance identity gives
\[
\sum_i m_i(g_i-\bar g)^2
 =\frac{1}{\sum_i m_i}\sum_{a<b}m_am_b\left(\sum_{i=a}^{b-1}\delta_i\right)^2.
\]
Weighted Cauchy–Schwarz bounds each inner square by \((z_b-z_a)\sum_{i=a}^{b-1}\delta_i^2/\ell_i\). After interchanging finite sums, its coefficient at edge \(i\) is
\[
\frac1{\sum_jm_j}\sum_{a\le i<b}m_am_b(z_b-z_a)
=G_i.
\]
Consequently,
\[
\sum_i m_i(g_i-\bar g)^2\le\sum_{i=1}^{n-1}\frac{G_i}{\ell_i}\delta_i^2.
\tag{1}
\]
Equality holds if and only if \(\delta_i/\ell_i\) is constant across all path edges: equality in the positive-weight term for the pair \((a,b)=(1,n)\) already forces this. Thus the only equality vectors in (1) are \(g_i=c+dz_i\). Equation (1) implies that the generalized spectral gap of \(L(w^0,0)\) is at least \(\Lambda\), while the test vector \(f\) attains equality, so it is exactly \(\Lambda\) and its generalized Fiedler eigenspace is one-dimensional. The path budget is \(\sum_i p_iw_i^0=\Lambda\sum_i\ell_iG_i=\Lambda V=B\); the equality \(\sum_i\ell_iG_i=V\) follows either from the same variance identity with \(g=z\) or by finite summation by parts.

For any conductance allocation with \(t=0\), the Rayleigh quotient at \(f\) is at most \(B/V=\Lambda\). Equality forces \(f\) to be a generalized eigenvector, since the attained minimum Rayleigh quotient is \(\Lambda\). At vertex 1 this fixes \(w_1\ell_1=\Lambda G_1\); recursively the interior vertex equations fix every \(w_i\ell_i=\Lambda G_i\). Hence the path optimizer is unique.

**2. A universal closing-edge inequality and the strict regimes.** The same fixed test vector \(f\) has edge increments \(\ell_i\) and closing-edge increment of magnitude \(S\). Therefore for every budget-feasible cycle allocation,
\[
\lambda_2(L(w,t),M)\le\frac{\sum_i\ell_i^2w_i+S^2t}{V}
\le\frac{B-(q-S^2)t}{V}.
\tag{2}
\]
For \(q>S^2\), (2) and the feasible path witness force \(t=0\) for every optimum; path uniqueness completes this case. For \(q=S^2\), (2) still proves the optimal gap is at most \(\Lambda\), which the path attains.

For \(q<S^2\), consider \(t=\varepsilon>0\) and \(w_i=(1-q\varepsilon/B)w_i^0\) for sufficiently small \(\varepsilon\). This preserves nonnegativity and costs exactly \(B\). Because the path Fiedler eigenvalue is simple, its first derivative along this differentiable perturbation is
\[
\left.\frac{d}{d\varepsilon}\lambda_2\right|_{\varepsilon=0+}
=-\frac qB\Lambda+\frac{S^2}{V}=
\frac{S^2-q}{V}>0.
\]
The spectral gap is therefore strictly larger than \(\Lambda\) for some positive \(\varepsilon\). As every closing-edge-deleted design has gap at most \(\Lambda\), all global optima below the cutoff have \(t>0\). Existence follows from compactness of the budget simplex and continuity of the eigenvalue.

**3. Every critical optimum is on the same affine line.** Now take \(q=S^2\), and let an allocation be optimal. Equality in (2) implies budget saturation and that \(f\) is a generalized eigenvector with eigenvalue \(\Lambda\). At vertex 1,
\(w_1\ell_1+tS=w_1^0\ell_1\). Comparing the interior vertex equations with those of the reference path yields \(w_i\ell_i+tS=w_i^0\ell_i\) for every \(i\). Hence, necessarily,
\[
w_i=w_i^0-tS/\ell_i.
\tag{3}
\]
Conversely, every nonnegative vector (3) uses exactly budget \(B\), makes \(f\) an eigenvector of eigenvalue \(\Lambda\), and is optimal precisely when no generalized eigenvalue in the orthogonal complement of both the constants and \(f\) falls below \(\Lambda\).

**4. Explicit endpoint of the complete critical face.** Nonnegative edge weights in (3) require \(0\le t\le t_{\mathrm{edge}}\). For any test vector \(g\), the quadratic difference from the reference path is
\[
g^{\mathsf T}\big(L(w(t),t)-L(w^0,0)\big)g
=t\left[(g_n-g_1)^2-S\sum_i\delta_i^2/\ell_i\right]=-tR(g).
\]
The weighted Cauchy–Schwarz inequality gives \(R(g)\ge0\), with equality exactly for affine functions of the path coordinate \(z\). On \(E\), no nonzero affine function is possible, hence \(R>0\). Equation (1) also gives \(A>0\) on \(E\). Since \(L(w(t),t)f=\Lambda Mf\), the quadratic form \(L(w(t),t)-\Lambda M\) restricted to mean-zero vectors decomposes without cross terms into the zero direction \(f\) and the form \(A-tR\) on \(E\). This is nonnegative exactly when \(t\le\inf_{g\in E\setminus\{0\}}A(g)/R(g)\). Both forms are positive definite on the finite-dimensional space \(E\), making that infimum an attained positive generalized eigenvalue. Combining with the edge constraint gives precisely \(0\le t\le t_*\), including all boundary cases. Every such design has gap exactly \(\Lambda\), completing the characterization.

## Verification

Run `python3 verify.py` with Python 3, NumPy and SciPy installed. The standalone script checks 400 different integer-price and integer-mass cases by exact rational arithmetic (2,000 assertions), including the path eigenvector, budget identities and critical-line eigenvector equations; it also checks 8,190 floating-point assertions across heterogeneous models and performs 24 constrained numerical optimizations below the price threshold. It reconstructs the critical endpoint as a generalized eigenvalue on \(E\). These finite experiments do not prove the arbitrary-real-parameter theorem; the proof above does.

As a simple check, for \(n=5\), all masses and ordinary prices equal one, the threshold is \(q_c=16\), the reference path has conductances \((2,3,3,2)\) when \(B=10\), and the critical family is \((2-4t,3-4t,3-4t,2-4t;t)\), truncated at the independently computed generalized-eigenvalue cutoff \(t_*\approx0.34188611699\). In particular, mere nonnegativity of the four path conductances would incorrectly allow \(t\le1/2\); the spectral cutoff is indispensable.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006), *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, develop the semidefinite and geometric dual framework, give the arbitrary-edge-price **path** solution (Result 5), solve the homogeneous cycle, and prove a bound on the general cycle eigenspace dimension (Result 6). Their §6 formulates prescribed-stationarity reversible processes. Those foundational ingredients and the path computation are prior results, **not claimed as new**. The present result specifies the mass-independent sharp price transition for a heterogeneously priced cycle and gives the **whole unrestricted optimal face at critical price**, including its independent spectral endpoint. The earlier framework permits an implicit optimization treatment; it does not state this complete all-parameter classification.

Gerencsér, Hendrickx and Van Dooren, *Spectral gap of Markov chains on a cycle*, study the eigenvalue-modulus objective for **discrete-time doubly stochastic** cycles, without this continuous-time independent-edge-cost and prescribed-mass design problem. Neither that work nor the inspected Sun et al. sections yielded an equivalent complete critical-face statement. The possibility of a less visible earlier equivalence remains.

## Limitations

The theorem concerns undirected cycles, positive masses, positive linear conductance prices, arbitrary nonnegative individual conductances, and a continuous-time generalized Laplacian spectral gap. It gives the exact optimum for prices at or above the threshold and a strict edge-retention characterization below it, **not** an explicit below-threshold optimum. It does not address arbitrary chords, multiple optional links, discrete-time fastest mixing, nonlinear prices, or nonreversible generators. Scientific originality remains subject to independent literature and expert examination.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis (2006), *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48(4), 681–699. DOI: https://doi.org/10.1137/S0036144504443821 ; full author PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf . Published electronically 2006-11-02.
2. B. Gerencsér, J. Hendrickx, P. Van Dooren, *Spectral gap of Markov chains on a cycle*, https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf .
