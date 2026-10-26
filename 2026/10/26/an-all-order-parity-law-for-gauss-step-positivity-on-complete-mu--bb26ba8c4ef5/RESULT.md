# An all-order parity law for Gauss-step positivity on complete multipartite heat networks

## Finding

For **every** positive stage count \(s\), and on **every** finite connected unweighted complete multipartite graph \(K_{n_1,\ldots,n_r}\), the completed \(s\)-stage Gauss–Legendre Runge–Kutta step for combinatorial heat diffusion has strictly positive off-diagonal entries at each positive step size. Its entrywise nonnegativity for **every** step size is characterized exactly by
\[
\boxed{\;s\text{ even}\quad\text{or}\quad N=2,\qquad N=\sum_{i=1}^{r}n_i.\;}
\]
In particular, every even-stage Gauss method, at orders \(4,8,12,\ldots\), is strictly positivity preserving, mass preserving, and positive definite on this entire graph class for every positive step size. When \(s\) is odd and \(N\ge3\), all diagonal entries eventually become negative; the off-diagonal entries nevertheless remain strictly positive.

The conclusion applies to the *completed endpoint step*, not to intermediate Runge–Kutta stages.

## Assumptions and scope

Let \(r\ge2\), with integers \(n_i\ge1\), and let \(N=\sum_i n_i\ge2\). The graph is simple, undirected, unweighted, and has an edge precisely between vertices in different parts. Its combinatorial Laplacian is \(L=D-A\), and heat diffusion is \(y'=-Ly\). The step size is any real \(h\ge0\). The stage count \(s\ge1\) is an arbitrary integer, not bounded in advance. Entrywise positivity means positivity of **every matrix entry**, whereas nonnegativity allows zeros.

Define, for \(0\le k\le s\),
\[
a_{s,k}=\frac{s!(2s-k)!}{(2s)!(s-k)!k!},\qquad
Q_s(z)=\sum_{k=0}^s a_{s,k}z^k,\qquad
R_s(z)=\frac{Q_s(-z)}{Q_s(z)}.
\]
All coefficients are strictly positive, \(Q_s(z)>0\) on \(z\ge0\), and \(R_s(0)=1\). The stage-\(s\) Gauss stability function for a scalar decay equation is \(R_s\), so its matrix endpoint map is
\[
T_s(h)=Q_s(-hL)\,[Q_s(hL)]^{-1}=R_s(hL).
\]
The inverse exists since \(L\) is symmetric positive semidefinite and \(Q_s\) has positive coefficients. In matrix formulas below, \(J_m\) denotes the \(m\times m\) all-ones matrix and \(J_N\) has size \(N\).

## Proof

**1. A scalar divided-difference lemma, uniform in stage count.** Separate the even and odd coefficients as
\[
E_s(x)=\sum_{2j\le s}a_{s,2j}x^j,
\qquad O_s(x)=\sum_{2j+1\le s}a_{s,2j+1}x^j.
\]
Then \(Q_s(\pm z)=E_s(z^2)\pm zO_s(z^2)\). Consequently, for \(z>0\),
\[
g_s(z):=\frac{1-R_s(z)}{z}
=\frac{2O_s(z^2)}{E_s(z^2)+zO_s(z^2)}
=\frac{2}{z+E_s(z^2)/O_s(z^2)}.
\]
We prove \(g_s\) strictly decreases on \((0,\infty)\), for **every** \(s\ge1\). For each index with \(2j+1\le s\), the ratio of adjacent even and odd coefficients is
\[
\frac{a_{s,2j}}{a_{s,2j+1}}
=\frac{(2j+1)(2s-2j)}{s-2j}
=2(2j+1)\frac{s-j}{s-2j}.
\]
This ratio strictly increases with \(j\): both positive factors strictly increase over the admissible integers. If \(s\) is even, the last even coefficient has no paired odd coefficient, and we extend the ratio there by \(+\infty\). Write \(e_j\) and \(o_j\) for the coefficients of \(E_s\) and \(O_s\), padding a missing terminal odd coefficient with zero. For any \(i>j\), this increasing-ratio property gives \(e_i o_j-e_j o_i\ge0\). Direct multiplication yields
\[
E_s'(x)O_s(x)-E_s(x)O_s'(x)
=\sum_{i>j}(i-j)(e_i o_j-e_j o_i)x^{i+j-1}\ge0\quad(x>0).
\]
Thus \(E_s/O_s\) is nondecreasing, and the additional strictly increasing term \(z\) in the denominator of \(g_s\) proves the strict decrease. The case \(s=1\), where \(E_s/O_s\) is constant, is included. In addition,
\[
1-R_s(z)=\frac{2zO_s(z^2)}{Q_s(z)}>0,
\qquad
1+R_s(z)=\frac{2E_s(z^2)}{Q_s(z)}>0
\]
for every \(z>0\). In particular, \(-1<R_s(z)<1\).

**2. Exact multipartite Laplacian projectors.** Let \(H\) be block diagonal with blocks \(J_{n_i}/n_i\), let \(P_0=J_N/N\), let \(P_N=H-P_0\), and let \(F_i\) be the block-supported matrix \(I_{n_i}-J_{n_i}/n_i\) in part \(i\), zero elsewhere. These are mutually orthogonal projections summing to the identity, and
\[
L=NP_N+\sum_{i=1}^{r}(N-n_i)F_i.
\]
Indeed, constant vectors on each part with total sum zero have eigenvalue \(N\), zero-sum vectors within part \(i\) have eigenvalue \(N-n_i\), and global constants have eigenvalue zero. The decomposition is valid even when a part has one vertex (then \(F_i=0\)). Functional calculus gives
\[
T_s(h)=P_0+R_s(Nh)P_N+\sum_i R_s((N-n_i)h)F_i.
\]

**3. Every off-diagonal entry is strictly positive.** If distinct vertices \(u\) and \(v\) lie in different parts, the preceding identity gives
\[
(T_s(h))_{uv}=\frac{1-R_s(Nh)}{N}=h\,g_s(Nh)>0.
\]
For distinct vertices in the same part \(i\), put \(q_i=N-n_i>0\). The entry is
\[
\begin{aligned}
(T_s(h))_{uv}
&=\frac{1-R_s(Nh)}N+\frac{R_s(Nh)-R_s(q_i h)}{n_i}\\
&=\frac{q_i h}{n_i}\,[g_s(q_i h)-g_s(Nh)]>0,
\end{aligned}
\]
since \(0<q_i<N\) and \(g_s\) is strictly decreasing. All these claims hold for every \(s\ge1\) and every \(h>0\), independently of the signs of \(R_s\) at individual eigenvalues.

**4. Even-stage positivity.** The polynomial has the exact integral representation
\[
Q_s(z)=\frac1{(2s)!}\int_0^\infty e^{-t}t^s(t+z)^s\,dt.
\]
Expanding the binomial and integrating termwise gives the coefficients \(a_{s,k}\) above. When \(s\) is even and \(z\ge0\), the integrand for \(Q_s(-z)\) is nonnegative and positive except on a null set; hence \(Q_s(-z)>0\). Therefore \(R_s(z)>0\) on \(z\ge0\). For any vertex \(u\) in part \(i\), its diagonal entry equals the same-part off-diagonal expression (viewed algebraically even when \(n_i=1\)) plus \(R_s(q_i h)>0\). Every diagonal entry is strictly positive. Because \(T_s(h)\) is a real symmetric function of \(L\), and \(R_s\) is strictly positive on the spectrum, it is also positive definite. Finally \(L\mathbf1=0\) implies \(T_s(h)\mathbf1=\mathbf1\); symmetry gives column sums one. Thus the matrix is strictly positive and doubly stochastic for every \(h>0\). At \(h=0\), it equals \(I\).

**5. Odd-stage obstruction and the two-vertex exception.** For odd \(s\), the leading coefficients of \(Q_s(-z)\) and \(Q_s(z)\) have opposite sign, so \(R_s(z)\to-1\) as \(z\to+\infty\). On a connected graph the nonzero eigenspace projectors sum to \(I-P_0\), giving
\[
\lim_{h\to\infty}T_s(h)=P_0-(I-P_0)=\frac{2}{N}J_N-I.
\]
For \(N\ge3\), every diagonal limit is \(2/N-1<0\); hence each diagonal entry is negative for all sufficiently large finite \(h\), proving failure of unconditional nonnegativity. If \(N=2\), the only permitted graph is \(K_2\), and
\[
T_s(h)=\frac12\begin{pmatrix}1+R_s(2h)&1-R_s(2h)\\1-R_s(2h)&1+R_s(2h)\end{pmatrix}.
\]
The inequalities \(-1<R_s(2h)<1\) from Step 1 make every entry strictly positive at all finite \(h>0\), even for odd \(s\). This proves both directions of the classification.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic (SymPy matrices with rational entries). It checked all stage counts from \(1\) through \(40\) for the coefficient-ratio identities, and independently reconstructed the completed Padé matrix in \(231\) rational test cases: \(11\) multipartite patterns, \(7\) stage counts and \(3\) time steps. It checked the spectral entry formulas, row sums, and \(5{,}352\) strict-positivity assertions. Five odd-stage large-step obstructions were checked separately. The script yielded the exact recorded output in `verification_output.txt`. Those finite tests are not the proof of the all-stage, all-graph theorem: the proof is Steps 1–5 above.

Reproduce using `python verify.py` with Python 3 and SymPy installed; no network service or external dataset is used. The script and recorded output are included in this package.

## Relationship to prior work

Strong-stability-preserving theory explains why high-order Runge–Kutta methods cannot be positivity preserving for *every* positive differential equation under unrestricted step sizes. The present result instead gives a sharply delimited, highly symmetric *linear graph* class for which infinitely many high-order Gauss endpoint steps are positive. Bresten et al. (2013) study explicit multistep Runge–Kutta SSP bounds, not this all-stage implicit graph classification. Nüßlein, Ranocha and Ketcheson (2020) enforce positivity by adaptive Runge–Kutta weights, rather than retaining unmodified Gauss weights. Blanes, Iserles and Macnamara (2021) discuss graph-Laplacian positivity and explicitly identify positivity of diagonal Padé approximants as a challenge. Banjai and Ferrari (2024) give the all-stage Gauss stability-function formula and parity at infinity in the context of convolution quadrature, without the multipartite entrywise classification.

Earlier specialized calculations treat the two-stage and three-stage methods separately on this graph class, as well as other graph classes. They supply examples and finite-stage boundaries but not the present universal strict off-diagonal lemma and complete classification across every integer stage count. The new statement does **not** claim those fixed-stage cases as independent discoveries. Comparisons against available indexed research descriptions and full primary texts did not reveal a result implying the all-stage statement, though absence in search results cannot prove novelty.

## Limitations

All claims concern one *completed endpoint* Gauss step on an **unweighted simple complete multipartite combinatorial Laplacian**. Intermediate Runge–Kutta stages may have negative entries. No claim is made for arbitrary weighted graphs, general Metzler generators, nonlinear equations, or all symmetric graph Laplacians. For odd stage counts with at least three vertices, the theorem establishes eventual diagonal negativity, **not** a unique finite positivity threshold or monotonicity of every diagonal for all step sizes. For even stages, \(R_s(z)\to1\) as \(z\to\infty\), so large steps make the update approach the identity rather than correctly resolving fast-decaying modes; positivity does not imply stiff-regime accuracy or \(L\)-stability. The statement is a mathematical self-reviewed finding, not independently audited. Literature coverage could be incomplete, especially specialized historical rational-matrix positivity results.

## References

1. C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D. I. Ketcheson, and A. Németh, *Strong Stability Preserving Multistep Runge–Kutta Methods*, arXiv:1307.8058v1, first submitted 30 July 2013. https://arxiv.org/abs/1307.8058
2. S. Nüßlein, H. Ranocha, and D. I. Ketcheson, *Positivity-Preserving Adaptive Runge–Kutta Methods*, arXiv:2005.06268, 2020. https://arxiv.org/abs/2005.06268
3. S. Blanes, A. Iserles, and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242, 2021. https://arxiv.org/abs/2102.08242
4. L. Banjai and M. Ferrari, *Runge–Kutta convolution quadrature based on Gauss methods*, Numerische Mathematik **156** (2024), 1719–1750. https://doi.org/10.1007/s00211-024-01429-4
