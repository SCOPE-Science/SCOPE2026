# Sharp three-regime conductance allocation for two cliques joined by a partial matching

## Finding

Let \(G_{k,m}\) be two copies of \(K_{k+m}\) connected by \(k\) disjoint corresponding gateway-to-gateway links, where \(k\ge2\) and \(m\ge1\). Let \(\Lambda_{k,m}(B)\) be the greatest possible second Laplacian eigenvalue when all allowed edge conductances are nonnegative and have sum \(B>0\). Set
\[
 r=\frac{k}{m},\qquad s_k=1+\sqrt{\frac{k}{2(k+1)}},\qquad
 t_*=\begin{cases}
 3/2,&r\le 3/2,\\
 r,&3/2<r<s_k,\\
 s_k,&r\ge s_k.
 \end{cases}
\]
Then the exact answer is
\[
 \boxed{\Lambda_{k,m}(B)=\frac{B}{C_{k,m}}},\qquad
 C_{k,m}=\frac{k+m}{2}+2mt_*+\frac{m}{2(t_*-1)}
 +(k-1)\max\left\{0,1-\frac{mt_*}{k}\right\}.
\]
Equivalently, the three cost regimes are
\[
 C_{k,m}=\begin{cases}
 (k+9m)/2,&r\le3/2,\\
 (k+m)/2+2k+m^2/[2(k-m)],&3/2<r<s_k,\\
 3k/2-1+m\bigl(3/2+1/k+\sqrt{2(k+1)/k}\bigr),&r\ge s_k.
 \end{cases}
\]
All formulas agree on common boundaries. Thus the optimal mixing rate is an exact rational/radical function of the two community sizes and the budget.

There is a unique optimizer invariant under exchanging the two cliques, simultaneously permuting their \(k\) matched gateways, and independently permuting each set of \(m\) nongateways. Its rates are given in the table below, multiplied by \(B/C_{k,m}\):

| Edge class | Rate when the spectral gap is normalized to one |
| --- | --- |
| Gateway–gateway edges within either clique | \(a_*=\max\{0,1-mt_*/k\}/k\) |
| Gateway–nongateway edges within either clique | \(c_*=t_*/k\) |
| Matched interclique gateway links | \(b_*=((k+m)t_*-k)/[2k(t_*-1)]\) |
| Nongateway–nongateway edges within either clique | \(d_*=0\) |

**Support classification for all (not necessarily symmetric) optimizers:** every optimum has zero rates on *every* nongateway–nongateway edge. If \(r\le s_k\), every optimum also has zero rates on *every* gateway–gateway intracluster edge. If \(r>s_k\), the total intracluster gateway–gateway conductance is positive in every optimum. These assertions remain true for \(m=1\), where the first edge class is empty.

## Assumptions and scope

The undirected weighted Laplacian is \(L=\sum_{\{i,j\}\in E}w_{ij}(e_i-e_j)(e_i-e_j)^\top\), with edge weights \(w_{ij}\ge0\). Its eigenvalues are in ascending order; the objective is \(\lambda_2(L)\) without stochastic row-normalization or a discrete-time holding-probability constraint. Every allowed clique edge and every one of the \(k\) bridge edges may independently be set to zero. The objective is homogeneous in \(B\); normalization to \(\lambda_2(L)=1\) reduces the problem to minimal total conductance. This is a *partial* matching, so \(m\ge1\), and \(k\ge2\) is essential to the transverse gateway constraint used below. No claim is made for \(m=0\), \(k=1\), unequal clique sizes, or fixed intracluster rates.

## Proof

**1. Symmetry reduction without loss of global optimality.** For \(z\perp\mathbf1\),
\[
 \lambda_2(L)=\min_{\|z\|=1,\ z\perp\mathbf1}\sum_{\{i,j\}\in E}w_{ij}(z_i-z_j)^2
\]
is a concave function of the conductances. Average any feasible allocation under the indicated graph automorphisms. The cost remains \(B\), while concavity and unitary invariance show that the spectral gap cannot decrease. Consequently, a symmetric maximizer exists and the unrestricted global optimum equals the symmetric optimum.

Assign common rates \(a\), \(b\), \(c\), and \(d\) to the four edge classes in the finding. The total weight is
\[
 W=k(k-1)a+kb+2kmc+m(m-1)d.
\]
Gateway transversals within each clique have eigenvalue \(ka+mc\) in the symmetric-across-layers sector and \(ka+mc+2b\) in the antisymmetric sector, each with multiplicity \(k-1\). Nongateway transversals have eigenvalue \(kc+md\), multiplicity \(2(m-1)\), absent when \(m=1\). In the two constant-on-each-orbit sectors, the symmetric-across-layers nonzero eigenvalue is \((k+m)c\); the antisymmetric-across-layers restriction acts on gateway and nongateway constants by
\[
 Q=\begin{pmatrix}mc+2b&-mc\\-kc&kc\end{pmatrix}.
\]
Although written in a nonorthonormal orbit-constant basis, this matrix is similar to a symmetric positive-semidefinite matrix using multiplicities \(k,m\). Its eigenvalues \(q_-\le q_+\) are therefore real. These blocks exhaust all \(2(k+m)\) eigenvalues, together with the zero mode.

**2. Exact normalized gap constraints.** The condition \(\lambda_2(L)\ge1\) forces \(kc>1\), because the smaller eigenvalue of \(Q\) is strictly below its \(kc\) diagonal value when \(c>0\); if \(c=0\), the graph is disconnected. For \(t=kc>1\), positivity of \(Q-I\) in its symmetric representation is equivalent to
\[
 \det(Q-I)=1-(k+m)c+2b(kc-1)\ge0,
\]
or
\[
 b\ge\frac{(k+m)t-k}{2k(t-1)}.
\]
Indeed, the lower diagonal entry of \(Q-I\) is \(t-1>0\), so its determinant condition also ensures the other principal minor is nonnegative. The remaining potentially restrictive transverse block requires
\[
 ka+mc\ge1,
 \qquad\text{equivalently}\qquad
 a\ge\frac1k\max\left\{0,1-\frac{mt}{k}\right\}.
\]
All other eigenvalues are automatically at least one: \((k+m)c>1\), \(kc+md\ge t>1\), and the extra gateway transverse eigenvalue exceeds \(ka+mc\). Thus the displayed inequalities are both necessary and sufficient for normalized gap at least one.

**3. One-dimensional exact minimization.** At fixed \(t>1\) the cheapest feasible \(b\) and \(a\) attain those lower bounds; \(d=0\) is optimal whenever its edge class exists. Substitution in \(W\) yields
\[
 F_{k,m}(t)=\frac{k+m}{2}+2mt+\frac{m}{2(t-1)}
 +(k-1)\max\left\{0,1-\frac{mt}{k}\right\}.
\]
It is strictly convex: away from its kink its second derivative is \(m/(t-1)^3>0\), and the maximum of the two affine terms is convex. On \(t\ge r=k/m\), the derivative vanishes only at \(t=3/2\). On \(1<t\le r\), the derivative vanishes only at \(t=s_k\). Comparing these stationary points with the boundary \(t=r\) gives exactly the displayed three regimes for \(t_*\) and hence \(C_{k,m}=\min_{t>1}F_{k,m}(t)\). Uniqueness of \(t_*\), and the strict positivity of each feasible rate's contribution to \(W\), give uniqueness of the symmetry-invariant minimizing allocation. Homogeneity then yields \(\Lambda_{k,m}(B)=B/C_{k,m}\).

**4. Support statements for arbitrary optimizers.** Average any unrestricted optimizer across the graph automorphisms. Its average is the unique invariant optimum just constructed. Every conductance is nonnegative. An orbit-average rate of zero is possible only if every edge of that orbit had zero rate before averaging. Hence nongateway–nongateway edges always vanish, and gateway–gateway edges always vanish if \(r\le s_k\). If \(r>s_k\), the unique invariant optimizer has strictly positive gateway–gateway rate; therefore the original optimizer must have positive conductance on at least one edge of that orbit. This does **not** assert uniqueness of arbitrary nonsymmetric optimizers.

## Verification

A companion script, `verify_spectral.py`, assembles each full weighted Laplacian, checks the two equivalent cost formulas and the complete eigenspectrum, and checks finite perturbations around the analytic minimizing scalar. For integers \(2\le k\le13\) and \(1\le m\le13\), the symmetric normalized optimum has spectral gap numerically equal to one and total weight equal to \(C_{k,m}\) within the specified numerical tolerance. Reproducibility: run `python verify_spectral.py` in an environment with Python and NumPy. This finite numerical check is supplementary; the proof above covers every admissible integer pair and positive budget.

For example, \(k=8\), \(m=5\) gives \(r=8/5\) and lies in the intermediate regime; \(k=2\), \(m=1\) lies in the final regime with strictly positive gateway–gateway conductance.

## Relationship to prior work

The continuous-time fastest-mixing process with a linear transition-rate budget is the convex optimization framework of Sun, Boyd, Xiao, and Diaconis (2006). Göring, Helmberg, and Wappler (2005) independently study maximizing weighted algebraic connectivity and its geometric SDP dual. Symmetry reductions for discrete-time fastest-mixing chains are developed by Boyd, Diaconis, Parrilo, and Xiao (2009). The interconnected-layer literature, including Shakeri and coauthors (2015), optimizes interlayer connectivity for prescribed intralayer networks; that restriction does not encompass reallocating an entire combined budget from clique edges into matching bridges. The new claim here is the explicit all-parameter partial-matching classification, including its three cost regimes and its universal zero-rate edge classes, not the general convex formulation or symmetry technique.

## Limitations

The characterization assumes equal clique orders and a disjoint matching of gateways. It permits zero conductances, so the weighted optimum may discard existing graph edges. Uniqueness is asserted only in the automorphism-invariant class; the support restrictions stated above apply to every optimum. Literature comparison can miss specialized treatments of this precise family, especially inaccessible full texts on unions of cliques. No separate independent review is claimed.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. Public article date: 2006-11-02.
2. F. Göring, C. Helmberg, M. Wappler, “Embedded in the Shadow of the Separator,” public preprint (2005). https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf.
3. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM Journal on Optimization* 20 (2009), 792–819. DOI: 10.1137/070689413.
4. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, C. Scoglio, “Maximizing Algebraic Connectivity in Interconnected Networks,” 2015 preprint, arXiv:1510.06792.
5. M. Allison, B. Shader, “Fastest Mixing Markov Chain Problem for the Union of Two Cliques,” *Linear and Multilinear Algebra* 59 (2011), 801–823. DOI: 10.1080/03081087.2010.538690; distinct discrete-time problem and graph union, full text not examined.
