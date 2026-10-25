# Arithmetic dark-state selection and exact leaf survival on three-arm quantum spiders

## Finding

Let \(T(L_1,L_2,L_3)\) be the tree consisting of a central vertex \(o\) and three otherwise disjoint simple paths of lengths \(L_1,L_2,L_3\), each a positive integer. A path length counts edges from \(o\) to its terminal leaf. Give every edge unit hopping, let \(H\) be the real symmetric adjacency matrix, and impose a single irreversible loss of strength \(\gamma>0\) at \(o\):
\[
K=H-i\gamma|o\rangle\langle o|.
\]
Start the quantum walker at the terminal leaf \(u_1\) of the first arm. Its asymptotic survival is the limit
\[
S=\lim_{t\to\infty}\|e^{-itK}|u_1\rangle\|^2.
\]
Put \(p=L_1+1\), \(q=L_2+1\), \(r=L_3+1\), and abbreviate
\[
g_{12}=\gcd(p,q),\quad g_{13}=\gcd(p,r),\quad g_{23}=\gcd(q,r),\quad g_{123}=\gcd(p,q,r),
\]
with \(h(g)=g\) for integers \(g\ge2\) and \(h(1)=0\). Then
\[
\boxed{S=\frac{h(g_{12})}{p+q}+\frac{h(g_{13})}{p+r}
+h(g_{123})\left(\frac{q+r}{pq+pr+qr}-\frac1{p+q}-\frac1{p+r}\right).}
\]
The formula is independent of \(\gamma>0\). The total dimension of the nondecaying (trap-invisible) subspace is
\[
\boxed{\dim\mathcal D=g_{12}+g_{13}+g_{23}-g_{123}-2.}
\]
Consequently the leaf on arm \(1\) is completely absorbed if and only if
\[
\boxed{\gcd(p,q)=\gcd(p,r)=1.}
\]
The corresponding formulas for leaves of arms \(2\) and \(3\) follow by permuting the denominators.

For instance, lengths \((1,2,3)\) give \(S=1/3\) and \(\dim\mathcal D=1\); lengths \((3,5,7)\) give \(S=17/39\) and \(\dim\mathcal D=4\). Lengths \((4,5,11)\) have \(\dim\mathcal D=5\) yet \(S=0\) for an excitation at the first leaf: protected states exist, but none overlaps that source.

## Assumptions and scope

Every arm has at least one edge, all hopping amplitudes are identical and real, the hub alone is absorbing, and the loss strength is fixed and strictly positive. The Hilbert space has dimension \(1+L_1+L_2+L_3\). The result concerns the single-particle adjacency Hamiltonian and the infinite-time norm remaining inside this finite non-Hermitian system, not a graph-Laplacian Hamiltonian, finite-time absorption kinetics, or simultaneous parameter limits. The initial state for the explicit survival formula is a normalized delta state at an outer leaf.

## Proof

**1. The nondecaying spectral subspace.** Let \(\mathcal D\) be the span of eigenvectors \(v\) of \(H\) satisfying \(\langle o|v\rangle=0\). It is invariant and reducing for \(H\). The loss projector annihilates it, so \(K\) acts on \(\mathcal D\) as the Hermitian matrix \(H\), and \(\mathcal D^\perp\) is also invariant. If \(Kv=zv\) for a nonzero vector, taking imaginary parts of \(\langle v|Kv\rangle=z\|v\|^2\) gives
\[
\operatorname{Im}z\,\|v\|^2=-\gamma|\langle o|v\rangle|^2.
\]
Thus an eigenvalue on the real axis has an eigenvector in \(\mathcal D\). The contractivity of \(e^{-itK}\), or equivalently its finite-dimensional dissipative spectral decomposition, excludes nontrivial Jordan blocks on the real axis. All eigenvalues of the restriction to \(\mathcal D^\perp\) have strictly negative imaginary part. Therefore
\[
S=\|P_{\mathcal D}|u_1\rangle\|^2.
\]
This argument proves existence of the limit for every allowed arm length and every \(\gamma>0\).

**2. Dirichlet modes of individual arms.** A vector with hub amplitude zero restricts on arm \(i\) to a Dirichlet eigenvector of the path on \(L_i\) vertices. Writing \(d_i=L_i+1\), this path has simple eigenvalues and normalized mode amplitudes
\[
\lambda_{i,k}=2\cos\frac{\pi k}{d_i},\qquad
v_{i,k}(x)=\sqrt{\frac2{d_i}}\sin\frac{\pi kx}{d_i},\qquad
1\le k\le d_i-1,\quad1\le x\le L_i.
\]
Here \(x=1\) is adjacent to the hub and \(x=L_i\) is the terminal leaf. Since cosine is strictly monotone over \((0,\pi)\), common eigenvalues correspond exactly to common reduced fractions \(k/d_i\).

Fix one common spectral angle \(\theta\in(0,\pi)\), and let \(I\subseteq\{1,2,3\}\) be the set of arms supporting that angle. A vector at this energy and with zero hub coordinate has amplitudes \(c_i v_{i,\theta}\) on participating arms. The eigenvalue equation at the hub becomes
\[
\sum_{i\in I}c_i\sqrt{\frac2{d_i}}\sin\theta=0.
\]
All coefficients in this one equation are nonzero. Consequently the dark eigenspace at this energy has dimension \(|I|-1\) for \(|I|\ge2\), and is absent for \(|I|=1\).

**3. Dark-state dimension.** Two Dirichlet paths with denominators \(d_i,d_j\) share precisely \(\gcd(d_i,d_j)-1\) eigenvalues: their common fractions are \(s/g\), \(1\le s<g=\gcd(d_i,d_j)\). The three paths share \(g_{123}-1\) eigenvalues. For \(|I|=1,2,3\), the identity \(|I|-1=\binom{|I|}{2}-\binom{|I|}{3}\) holds. Summing over distinct energies gives
\[
\dim\mathcal D=(g_{12}-1)+(g_{13}-1)+(g_{23}-1)-(g_{123}-1),
\]
which is the asserted dimension formula.

**4. Projection of a terminal leaf.** At one common angle containing arm \(1\), the normalized first-arm Dirichlet vector has squared terminal amplitude
\[
|v_{1,\theta}(L_1)|^2=\frac2p\sin^2\theta.
\]
Within the direct sum of the participating one-dimensional arm modes, the orthogonal complement to the dark modes is the line whose coefficient vector has entries \(\sqrt{2/d_i}\sin\theta\). The dark fraction of squared weight originating on arm \(1\) is therefore
\[
F(I)=1-\frac{1/p}{\sum_{i\in I}1/d_i}.
\]
It equals \(p/(p+q)\) when \(I=\{1,2\}\), \(p/(p+r)\) when \(I=\{1,3\}\), and \(p(q+r)/(pq+pr+qr)\) when \(I=\{1,2,3\}\).

For any integer \(g\ge2\), the elementary root-of-unity identity gives
\[
\sum_{s=1}^{g-1}\sin^2\frac{\pi s}{g}=\frac g2;
\]
for \(g=1\), the sum is empty and zero. Hence the total weight of the modes shared by the first and second arms, if counted as double-arm modes, is \(h(g_{12})/(p+q)\), and similarly for the first and third arms. Frequencies common to all three arms have been counted with the two double-arm fractions; replace those two fractions by the correct three-arm fraction, with the same weighted trigonometric sum \(h(g_{123})/2\). This gives exactly the displayed formula for \(S\).

Every shared angle involving arm \(1\) contributes a strictly positive amount, since \(\sin\theta\ne0\) and \(F(I)>0\) for \(|I|\ge2\). Such an angle exists exactly when \(g_{12}>1\) or \(g_{13}>1\). This proves the complete-absorption equivalence. The initial leaf and the chosen absorber do not enter the dissipative argument except through their stated positions, completing the proof.

## Verification

The standalone program `verify_spider.py`, run with Python 3, NumPy and SymPy, constructs the full adjacency matrix independently of the number-theoretic formula. It groups Hermitian eigenspaces and projects onto their trap-orthogonal portions. It passed \(492\) parameter triples with \(1\le L_i\le8\) and total arm length at most \(20\), comparing both survival and dark-space dimension. The largest survival discrepancy was approximately \(1.443\times10^{-15}\).

It also passed \(24\) exact-integer hub-Krylov-rank comparisons and \(21\) checks of the real-eigenvalue count of the non-Hermitian absorbing Hamiltonian at three positive absorption strengths. The proof above, not these finite checks, establishes the claim for all positive arm lengths. The files `verify_spider.py` and `requirements.txt` specify a standalone reproducible check.

## Relationship to prior work

Adjacency-driven continuous-time walks on homogeneous trees appear in Konno (2006), whose analysis concerns unitary walks and tree asymptotics, not this lossy unequal-arm geometry. Yalouz and Pouthier (2018) study a star with a central trap and equal-length branches; their abstract makes this a particularly relevant prior comparison. Their accessible 2022 follow-on studies a symmetric number of branches, each of the same length, with peripheral energy defects, and its full model equations make the equal-arm assumption explicit. The full text of the 2018 work was not available for inspection; this is a material residual priority uncertainty, not evidence of absence.

Razzoli, Paris and Bordone (2021) provide a general spectral transport-efficiency method and apply it to several other graph families. Their general projection principle is consistent with Step 1, but the specific arithmetic classification of unequal-arm spider resonances and its exact leaf weights require the additional path-spectrum and gcd calculation in Steps 2–4. The equal-arm case \(p=q=r\), which yields \(S=2/3\), is not claimed as a separately new result.

## Limitations

This is a precise finite-tree, single-excitation, long-time statement. It does not calculate the absorption-time distribution or its mean, cover arbitrary weighted edges or multiple traps, or show stability against geometric disorder, on-site disorder or dephasing. Survival at noncoprime arm lengths can be destroyed by small generic hopping perturbations, but no quantitative perturbation bound is claimed. The 2018 equal-arm trapping article was compared only through its accessible abstract, leaving an explicit historical-priority risk. Other, unlocated spectral-controllability literature may subsume aspects of the formula; exhaustive historical originality is not asserted.

## References

1. N. Konno, “Continuous-Time Quantum Walks on Trees in Quantum Probability Theory,” arXiv:quant-ph/0602213 (first posted 26 February 2006), https://arxiv.org/abs/quant-ph/0602213.
2. S. Yalouz and V. Pouthier, “Continuous-time quantum walk on an extended star graph: Trapping and superradiance transition,” *Physical Review E* **97**, 022304 (2018), https://doi.org/10.1103/PhysRevE.97.022304.
3. S. Yalouz and V. Pouthier, “The extended star graph as a light-harvesting-complex prototype: excitonic absorption speedup by peripheral energy defect tuning,” arXiv:2210.17524 (2022), https://arxiv.org/abs/2210.17524.
4. L. Razzoli, M. G. A. Paris, and P. Bordone, “Transport Efficiency of Continuous-Time Quantum Walks on Graphs,” *Entropy* **23**, 85 (2021), https://doi.org/10.3390/e23010085.
