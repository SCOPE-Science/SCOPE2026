# Degree two uniquely maximizes conditional expected Wiener index in uniform Cayley trees

## Finding
For \(n\ge3\), let \(T_n\) be uniform on the \(n^{n-2}\) labelled trees on \(\{1,\ldots,n\}\), let \(W_n=\sum_{1\le u<v\le n}d_{T_n}(u,v)\), and distinguish vertex \(1\). Write \(m=n-1\), \(r=\deg_{T_n}(1)-1\in\{0,\ldots,m-1\}\), \(t=m-1-r\), and
\[ F_t=\sum_{j=0}^{t}\frac{(t)_j}{m^j},\qquad (t)_0=1,\qquad (t)_j=t(t-1)\cdots(t-j+1). \]
The exact conditional mean of the Wiener index is
\[
\boxed{\mathbb E[W_n\mid\deg_{T_n}(1)=r+1]
=mF_t+\binom m2\frac{(m+r-r^2)F_t+m(r-1)}{m-1}.}
\]
**Modal classification.** For every \(n\ge4\), the unique degree maximizing this expectation is \(2\). The conditional mean strictly decreases as the degree increases from \(2\) to \(n-1\), while its degree-one value is strictly smaller than its degree-two value. For \(n=3\), both possible degrees yield \(W_n=4\); for \(n=2\), \(W_n=1\) deterministically.

## Assumptions and scope
The tree is uniform among *unrooted labelled* Cayley trees; vertex \(1\) is a fixed label, not a random size-biased vertex. Distances are numbers of edges. The conditional degree event has positive probability for all \(0\le r\le m-1\), because the Prüfer formula gives
\[\Pr\{\deg(1)=r+1\}=\frac{\binom{m-1}{r}m^{m-1-r}}{(m+1)^{m-1}}.\]
The result covers all integer \(n\ge3\) and every admissible degree. There is no assertion about nonuniform random tree models or arbitrary finite trees.

## Proof
**1. Weighted marked-path identity.** Give vertex \(1\) weight \(z\) and all other vertices weight \(1\), and give a tree weight \(z^{\deg(1)-1}\). Prüfer enumeration gives the partition function
\[Z(z)=(m+z)^{m-1}.\]
More generally, for strictly positive vertex weights \(x_v\) with \(S=\sum_v x_v\), the total weight \(\sum_T\prod_v x_v^{\deg_T(v)-1}=S^{n-2}\). If a prescribed simple path with \(k\) edges has vertex set \(Q\), weighted forest contraction gives the probability that the path occurs as
\[
\frac{\left(\sum_{v\in Q}x_v\right)\prod_{v\in Q\setminus\{\text{two endpoints}\}}x_v}{S^k}.
\]
To see this, complete the fixed path to a spanning tree, contract its vertices to one supervertex, and sum over possible original attachment vertices at the supervertex; each attachment contributes its weight. The remaining weighted Cayley sum gives the power of \(S\). This counts each completion once and is valid also for a spanning path (the final power cancels). Thus the identity requires no independence assumption about paths.

**2. Exact weighted distance tails.** For any distinct \(u,v\ne1\), enumerate all ordered interior vertices of their unique path using the identity above. For \(1\le k\le m\), telescoping the exact probabilities of path lengths gives
\[
\Pr_z\{d(1,u)\ge k\}=\frac{(m-1)_{k-1}}{(m+z)^{k-1}}.
\]
For \(2\le k\le m\), splitting the paths from \(u\) to \(v\) according to whether their interior contains vertex \(1\) gives
\[
\Pr_z\{d(u,v)\ge k\}=\frac{(m-2)_{k-2}[m-k+(k-1)z]}{(m+z)^{k-1}}.
\]
For completeness, the corresponding exact path-length probabilities for \(k\ge1\) are respectively
\[
\frac{(m-1)_{k-1}(z+k)}{(m+z)^k}
\quad\text{and}\quad
\frac{(m-2)_{k-1}(k+1)+(k-1)(m-2)_{k-2}z(z+k)}{(m+z)^k}.
\]
The second expression is used for \(2\le k\le m\); at \(k=1\) its probability equals \(2/(m+z)\). Terms containing an out-of-range falling factorial vanish.

**3. Conditioning on degree.** The generating partition function \(Z(z)\) makes the coefficient ratio
\[\mathbb E[X\mid\deg(1)=r+1]=\frac{[z^r](Z(z)\mathbb E_zX)}{[z^r]Z(z)}\]
for any tree observable \(X\). Let \(P_n=\sum_{v\ne1}d(1,v)\) and \(Q_n=\sum_{2\le u<v\le n}d(u,v)\). Summing the distance tails, extracting the coefficients, and using \(\mathbb E[d]=\sum_{k\ge1}\Pr(d\ge k)\), one obtains
\[
\mathbb E[P_n\mid r]=mF_t,\qquad
\mathbb E[Q_n\mid r]=\binom m2 D_r,
\]
where
\[
D_r=\frac{(m+r-r^2)F_t+m(r-1)}{m-1}.
\]
One direct simplification uses \(J_t=\sum_{j=0}^{t}j(t)_j/m^j=m-(m-t)F_t\), obtained by shifting the index in the finite sum and using the falling-factorial recurrence. Since \(W_n=P_n+Q_n\), these identities give the displayed exact mean.

**4. Strict decrease from degree two.** For fixed \(m\), the recurrence \(F_t=1+(t/m)F_{t-1}\) gives for \(1\le r\le m-2\)
\[
(m-1)(D_{r+1}-D_r)
=(r-1)\left[r-\frac{m+r(r+1)}{m}F_{m-r-2}\right].
\]
Thus \(D_2=D_1\). If \(r\ge2\), the bracket is strictly negative. Indeed, define \(H_r=rm/[m+r(r+1)]\). Fix \(m\), start with \(r=m-2\): then \(F_0=1>H_{m-2}\). Descending induction on \(r\) uses
\[
F_{m-r-2}=1+\frac{m-r-2}{m}F_{m-r-3}
>1+\frac{m-r-2}{m}H_{r+1}>H_r,
\]
where the last inequality is the exact positive identity
\[
1+\frac{m-r-2}{m}H_{r+1}-H_r
=\frac{2m^2}{[m+r(r+1)][m+(r+1)(r+2)]}>0.
\]
Therefore \(D_{r+1}<D_r\) whenever \(r\ge2\). Meanwhile \(mF_{m-1-r}\) decreases strictly as \(r\) increases: the sums \(F_t\) increase strictly in integer \(t\ge0\), by comparison of falling-factorial terms. Hence the total conditional Wiener expectation decreases strictly between degrees \(2\) and \(3\), and at every subsequent degree, even though the nonroot part has one plateau.

**5. The degree-one-to-degree-two jump.** Set \(\overline W_m=\mathbb E W(T_m)\) for a uniform \(m\)-vertex labelled tree. Conditional on degree one, delete vertex \(1\): the remainder is uniform and its former attachment vertex is uniform, giving
\[\mu_0:=\mathbb E[W_n\mid\deg(1)=1]=m+\frac{m+2}{m}\overline W_m.\]
Conditional on degree two, suppress vertex \(1\): this bijects the conditioned trees with pairs consisting of a uniform \(m\)-vertex labelled tree and a uniformly chosen edge to subdivide. For each fixed \(m\)-vertex tree the sums of the extra nonroot distances and new-vertex-to-old-vertex distances over all its \(m-1\) edges equal respectively \(W(T_m)\) and \(2W(T_m)\). The second equality follows by summing \(\sum_v d(v,e)\) over edges and using \(\sum_v\sum_{w\ne v}d(v,w)=2W(T_m)\). Thus
\[\mu_1:=\mathbb E[W_n\mid\deg(1)=2]=\frac{m+2}{m-1}\overline W_m.\]
Every \(m\)-vertex tree has \(W(T_m)=\sum_e s_e(m-s_e)\ge(m-1)^2\), since each edge separates at least \(m-1\) pairs. Therefore, for \(m\ge3\),
\[
\mu_1-\mu_0=\frac{m+2}{m(m-1)}\overline W_m-m
\ge\frac{m-2}{m}>0.
\]
The strict first increase and all subsequent strict decreases prove the unique degree-two maximizer for every \(n\ge4\). At \(m=2\), direct enumeration gives the exceptional tie \(W_3=4\). \(\square\)

## Verification
Run \(\texttt{python3 verify.py}\) with a standard Python installation. The self-contained script uses integer Prüfer-code enumeration and rational arithmetic. It exhausts \(280392\) labelled trees at sizes \(2\) through \(8\), independently computes their Wiener and two distance components, and checks all conditional means and degree probabilities (\(28\) degree cells; \(112\) mean/count equalities). It also checks the mode on every nontrivial enumerated size and \(3003\) exact rational inequalities at larger finite parameter values. The infinite-size conclusion follows from the proof, not from these finite calculations.

## Relationship to prior work
Entringer, Meir, Moon and Székely (1994), sections 3–4, provide general aggregate Wiener generating functions and the unconditioned Cayley-tree mean, not the finite conditional-on-one-vertex-degree regression. Janson (2003), sections 2–7, studies marginal and joint asymptotic Wiener and root-path-length behavior for simply generated trees, but not the degree-resolved conditional mean or its degree-two maximizer. Berzunza Ojeda and Janson (2021 first arXiv version; journal 2022), sections 4–13, treat root modifications and distance profiles mainly via asymptotic convergence; their statements do not imply this finite regression without additional computation. Previous mixed-index formulas, including a covariance with the Zagreb degree-square sum, do not determine conditional means given one vertex's degree. Indeed, by exchangeability and the deterministic identity \(\sum_v\deg(v)=2(n-1)\), \(\operatorname{Cov}(W_n,\deg(1))=0\): the exact nonlinear regression reveals dependence that this covariance cannot detect.

## Limitations
The theorem is for uniform, unrooted, labelled Cayley trees with a fixed distinguished label. It establishes exact conditional expectations, not conditional distributions or stochastic ordering. Prior-work comparison is limited to the specifically inspected literature and available database results; a historical multivariate degree-marked Wiener generating function not located in the searches could express an equivalent regression. This manuscript has no independent audit.

## References
1. R. C. Entringer, A. Meir, J. W. Moon, L. A. Székely, “On the Wiener index of trees from certain families,” *Australasian Journal of Combinatorics* 10 (1994), 211–224. Full text: https://ajc.maths.uq.edu.au/pdf/10/ocr-ajc-v10-p211.pdf .
2. S. Janson, “The Wiener Index of Simply Generated Random Trees,” *Random Structures & Algorithms* 22 (2003), 337–358; first online 3 March 2003, https://doi.org/10.1002/rsa.10074 .
3. G. Berzunza Ojeda, S. Janson, “The distance profile of rooted and unrooted simply generated trees,” *Combinatorics, Probability and Computing* 31 (2022), 368–410; first arXiv release 1 September 2020, https://arxiv.org/abs/2009.00572 ; https://doi.org/10.1017/S0963548321000304 .
