# Exact price-optimal continuous-time mixing on transitive one-leaf coronas and rigid cyclic sunlets

## Finding

Let \(H\) be a connected, finite, simple, vertex- and edge-transitive \(d\)-regular graph with \(m\ge3\) vertices, \(d\ge2\), and first positive eigenvalue \(\lambda=\lambda_2(L_H)>0\). Form its *one-leaf corona* by adjoining a private degree-one vertex to each vertex of \(H\). Every base edge has unit-price coefficient \(P>0\), every pendant edge has unit-price coefficient \(Q>0\), and one can choose each symmetric transition rate independently, subject to aggregate expenditure at most \(B>0\).

Define
\[
c=\frac{dP}{2\lambda},\qquad D=2c+Q+2\sqrt{cQ},\qquad t_*=\frac{B}{mD}.
\]
The **largest possible spectral gap**, \(\lambda_2\) of the weighted corona Laplacian, is exactly \(t_*\). It is attained at constant rates within each of the two edge classes:
\[
a_* = \frac{t_*}{\lambda}\left(2+\sqrt{\frac Qc}\right)
\quad\text{on each base edge},\qquad
b_* = t_*\left(1+\sqrt{\frac cQ}\right)
\quad\text{on each pendant edge}.
\]
This solution is the sole optimal allocation among allocations constant on the two classes. All permissible rates, however, were optimized independently; no symmetry constraint was imposed to obtain the upper bound.

When \(H=C_n\), \(n\ge3\), this optimizer is **unique even over all independent nonuniform edge rates**. Put
\[
\lambda_n=4\sin^2\!\left(\frac\pi n\right),\qquad c_n=\frac P{\lambda_n}.
\]
The two edge classes consume exactly equal total expenditure if and only if \(Q=2c_n\). At fixed \(B,P,Q>0\), as \(n\to\infty\),
\[
t_*\sim\frac{2\pi^2B}{Pn^3},\qquad
a_*\sim\frac{B}{Pn},\qquad
b_*\sim\frac{\pi B}{n^2\sqrt{PQ}}.
\]
Thus rim and leaf investments have genuinely different length scales in a growing cycle.

## Assumptions and scope

All edge rates are arbitrary real numbers in \([0,\infty)\), independently selected. The weighted Laplacian is \(L(w)=\sum_{e=\{i,j\}}w_e(e_i-e_j)(e_i-e_j)^{\mathsf T}\); its negative generates the *continuous-time symmetric* Markov process. The stationary distribution of any connected positive-rate realization is uniform on the \(2m\) vertices. Exactly \(md/2\) base edges and \(m\) pendant edges occur. The constraint is
\[
P\sum_{e\in E(H)}w_e+Q\sum_{i=1}^m v_i\le B.
\]
The quantity optimized is \(\lambda_2(L(w))\), not the discrete-time second-largest eigenvalue modulus, a nonuniform-mass spectral gap, or a fixed-base-layer interconnection-only problem. Vertex- and edge-transitivity are essential for the general formula; the all-nonuniform uniqueness statement is separately proved for cyclic bases only.

## Proof

**1. Reduction from every nonuniform allocation to two rates.** On the mean-zero subspace,
\[
\lambda_2(L(w))=\min_{\substack{x\perp\mathbf1\\\|x\|_2=1}}
\sum_e w_e(x_i-x_j)^2.
\]
This is a concave, positive-homogeneous function of the independent edge rates. Average any feasible allocation under the automorphism group of \(H\), extended to its private leaves. The group is transitive on base edges and also on pendant edges; the average therefore has common base-edge rate \(a\) and pendant-edge rate \(b\). The price and budget are invariant under this averaging, and concavity ensures that it cannot reduce the gap. Hence a globally optimal two-rate allocation exists, whether or not all global optimizers have this form. The budget must be saturated at an optimum with positive gap, by homogeneity.

**2. Full two-rate spectral factorization.** In core/leaf order, the weighted Laplacian is
\[
L(a,b)=\begin{pmatrix}aL_H+bI&-bI\\-bI&bI\end{pmatrix}.
\]
For every base-Laplacian eigenvalue \(\eta\), the corresponding two eigenvalues are
\[
\mu_{\pm}(a\eta,b)=\frac{a\eta+2b\pm\sqrt{a^2\eta^2+4b^2}}2.
\]
At \(\eta=0\) they are \(0,2b\). For every \(\eta>0\), \(0<\mu_-(a\eta,b)<b\), and \(\mu_-(z,b)\) is strictly increasing in \(z>0\). Consequently
\[
\lambda_2(L(a,b))=\mu_-(\lambda a,b).
\]
In particular, for a proposed \(t>0\), the inequality \(\lambda_2(L(a,b))\ge t\) is equivalent to
\[
b>t,\qquad \lambda a\ge\frac{t(2b-t)}{b-t}.
\]
The equivalence follows by evaluating the characteristic polynomial of the positive two-by-two block at \(t\), together with \(t<b\).

**3. Exact budget optimization and uniqueness in the symmetric class.** Write \(u=b/t>1\). At target gap \(t\), the least admissible base rate is
\[
a=\frac t\lambda\left(2+\frac1{u-1}\right).
\]
Since \(H\) has \(md/2\) edges, the necessary and sufficient price bound is
\[
B\ge mt\left[c\left(2+\frac1{u-1}\right)+Qu\right].
\]
The bracket has strictly positive second derivative \(2c/(u-1)^3\) and diverges at both ends of \((1,\infty)\). Its unique minimizer is \(u_*=1+\sqrt{c/Q}\), with exact minimum \(D=2c+Q+2\sqrt{cQ}\). It follows that \(t\le B/(mD)\) for every original nonuniform allocation, by Step 1. Choosing \(b=b_*\) and \(a=a_*\) realizes equality and exhausts the budget. Strict convexity of the scalar bracket plus strict monotonicity of the spectral mode proves uniqueness **within** the two-rate family.

**4. Rigidity for cyclic bases (no imposed symmetry).** Let the base be \(C_n\), \(n\ge3\), and let \(w_i\) and \(v_i\) denote independently variable rim and spoke rates, respectively, with indices taken modulo \(n\). Suppose their weighted corona has optimal gap \(t_*\). Averaging over cyclic rotations gives the unique symmetric optimum from Step 3, so necessarily
\[
\sum_i w_i=na_*,\qquad \sum_i v_i=nb_*.
\]
Put \(\theta=2\pi/n\), and choose \(\alpha=1\) and \(\beta=b_*/(b_*-t_*)>1\). For each \(i\), construct the two real vectors
\[
f^c_i=(\alpha\cos(i\theta),\,\beta\cos(i\theta)),\qquad
f^s_i=(\alpha\sin(i\theta),\,\beta\sin(i\theta)),
\]
where the two coordinates refer to the core and attached leaf. These vectors are nonzero, orthogonal to the constant vector, and are eigenvectors of the *symmetric optimum* with eigenvalue \(t_*\). The sums over these two vectors of the squared differences across any rim edge and across any spoke edge are, respectively, the constants \(\alpha^2\lambda_n\) and \((\beta-\alpha)^2\). Therefore the sum of their Rayleigh energies for **any** optimal nonuniform allocation depends only on the two edge-class totals above, and equals
\[
\sum_{\nu\in\{c,s\}}(f^\nu)^{\mathsf T}L(w,v)f^\nu
=t_*\sum_{\nu\in\{c,s\}}\|f^\nu\|_2^2.
\]
Each separate Rayleigh quotient is at least \(t_*\), so equality of their sum forces both vectors to lie in the \(t_*\)-eigenspace of the actual, possibly nonuniform Laplacian. At each leaf the two eigenvector equations read
\[
v_i(\beta-\alpha)\cos(i\theta)=t_*\beta\cos(i\theta),\qquad
v_i(\beta-\alpha)\sin(i\theta)=t_*\beta\sin(i\theta).
\]
Since cosine and sine never vanish together, every \(v_i=b_*\). Combining the cosine and sine core equations as one complex equation and subtracting the known pendant term yields
\[
w_i(1-e^{i\theta})+w_{i-1}(1-e^{-i\theta})=\lambda_n a_*.
\]
Its imaginary part is \(\sin\theta\,(w_{i-1}-w_i)=0\). For \(n\ge3\), \(\sin\theta\ne0\); thus all rim weights agree, and their sum fixes \(w_i=a_*\). This proves unrestricted uniqueness, including when the first nonzero base eigenvalue has multiplicity two (as it does on cycles).

**5. Expenditure crossover and cycle limit.** At the optimum, core expenditure is \(mt_*(2c+\sqrt{cQ})\), while pendant expenditure is \(mt_*(Q+\sqrt{cQ})\). Hence equality holds exactly at \(Q=2c\). For a cycle \(d=2\), so \(c=P/\lambda_n\). Since \(\lambda_n=4\pi^2n^{-2}+O(n^{-4})\), we have \(c_n=Pn^2/(4\pi^2)+O(1)\); substitution into the explicit formulas yields the three stated leading asymptotics.

## Verification

A standalone standard-library Python checker, `verify.py`, independently constructs finite weighted Laplacians, computes their eigenvalues with a Jacobi algorithm, compares the proposed optimum against randomized nonuniform edge allocations, and checks budget identities. It also verifies exact rational parameter identities and the three cycle asymptotic constants. The executed checker returned `PASS: 1549 exact and independent spectral/budget checks`. These finite checks supplement, but do not replace, the all-parameter variational and spectral proof above.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) establish the general continuous-time maximum-\(\lambda_2\) problem, a semidefinite formulation, and examples including bare paths and cycles. Their general framework is the methodological foundation; the corona-specific price optimum, all-nonuniform cyclic rigidity, and distinct rim/leaf asymptotics are not stated in the inspected treatment. Boyd, Diaconis, Parrilo, and Xiao (2007) develop automorphism reductions for a **discrete-time SLEM** objective, which is not the objective optimized here. Shakeri and coauthors (2015) optimize interlayer links with fixed underlying network layers; both the base and pendant conductances are decision variables in the present theorem. Suzuki (2013) studies the spectrum of a periodic infinite graph with pendants, while Liu–Shao (2022) develop weighted corona spectral identities, not the priced continuous-time optimization classification.

## Limitations

The proof does not claim that an arbitrary nonuniform optimizer on every transitive base must be symmetric; unrestricted uniqueness is established here only for cycles. The objective is the spectral relaxation rate of a continuous-time reversible symmetric process with uniform equilibrium, not discrete-time SLEM, worst-case hitting time, optimal control energy, or a nonuniform stationary distribution. A proof of a general optimization theorem is not by itself proof of publication priority. Related optimization and corona-spectral literature may contain equivalences not found in the inspected sources. Independent external mathematical validation has not been performed.

## References

- Jun Sun, Stephen Boyd, Lin Xiao, and Persi Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
- Stephen Boyd, Persi Diaconis, and Lin Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
- Stephen Boyd, Persi Diaconis, Pablo A. Parrilo, and Lin Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (2007). https://arxiv.org/abs/0709.0955
- Heman Shakeri, Nathan Albin, Faryad Darabi Sahneh, Pietro Poggi-Corradini, and Caterina Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785 (2015). https://arxiv.org/abs/1510.06785
- Akito Suzuki, *Spectrum of the Laplacian on a Covering Graph with Pendant Edges I: The One-Dimensional Lattice and Beyond*, arXiv:1304.4315 (2013). https://arxiv.org/abs/1304.4315
- Liu and Shao, *Two Kinds of Laplacian Spectra and Degree Kirchhoff Index of the Weighted Corona Networks*, 2022, DOI: 10.1155/2022/6884839. https://doi.org/10.1155/2022/6884839
