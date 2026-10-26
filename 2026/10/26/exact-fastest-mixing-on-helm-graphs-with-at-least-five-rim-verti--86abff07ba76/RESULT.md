# Exact fastest mixing on helm graphs with at least five rim vertices

## Finding
For every integer \(n\geq5\), let \(H_n\) be the **helm graph** consisting of one hub, an \(n\)-cycle of rim vertices, one hub--rim edge to each rim vertex, and one private pendant leaf at each rim vertex. Among all symmetric, entrywise nonnegative stochastic matrices \(P\) whose off-diagonal support is contained in \(H_n\), minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-J/(2n+1)\|_2\), with \(J\) the all-ones matrix.

Set
\[
 c=\cos(2\pi/n),\quad \delta=\sqrt{1-c},\quad t=1+\delta,\quad p=1/n,
\]
\[
 \rho=\frac{t[1-c(1-p)]}{\delta(1+t^2)},\qquad
 q=\frac{1-p-\rho}{2},\qquad
 M=\frac{c(1-p)+t^2}{1+t^2}.
\]
Then the **global optimum is exactly** \(\mu^*(H_n)=M\). An optimizing chain gives probability \(p\) to each hub--rim edge, \(q\) to each rim-cycle edge, and \(\rho\) to each rim--leaf edge. The hub and every rim vertex have zero holding probability, and each leaf holds with probability \(1-\rho\). In particular \(0<\rho<1/2\) and \(q>0\). This optimizer is the **unique** transition assignment invariant under the dihedral symmetries of the rim; uniqueness among unrestricted assignments is not asserted.

The exact gap \(1-M\) has the asymptotic behavior
\[
 1-\mu^*(H_n)=\frac{1}{2n}+\frac{\pi^2-\pi/\sqrt2}{n^2}+O(n^{-3}),
 \qquad \lim_{n\to\infty}\rho=\frac{1}{2\sqrt2\pi}.
\]
In comparison, uniform maximum-degree weighting of every allowed edge by \(1/n\) has gap \((3-\sqrt5)/(2n)+O(n^{-2})\), so the optimal-to-maximum-degree spectral-gap ratio tends to \((3+\sqrt5)/4\), approximately \(1.3090\).

## Assumptions and scope
The number of rim vertices is any integer \(n\ge5\); the total number of vertices is \(2n+1\). Self-loops are permitted, but off-diagonal transitions only follow graph edges. Matrices are symmetric and row-stochastic, ensuring the uniform stationary distribution. Zero transition probability on an allowed edge is permitted. The objective is the **two-sided** spectral modulus, not just the second-largest eigenvalue. No claim is made for the smaller helm graphs with three or four rim vertices, nor for nonsymmetric chains or a nonuniform prescribed stationary distribution.

## Proof
**1. Symmetry and spectral blocks.** The objective is the operator norm of \(P-J/(2n+1)\), hence convex and invariant under conjugation by any automorphism. Averaging an arbitrary feasible matrix over the dihedral group does not increase the objective. Every invariant feasible matrix has three edge probabilities \(p,q,r\), with
\[
 0\le p\le1/n,\quad q,r\ge0,\quad p+2q+r\le1.
\]
The hub, rim and leaf holding probabilities are \(1-np\), \(1-p-2q-r\), and \(1-r\). Discrete Fourier decomposition around the rim yields the symmetric radial block
\[
 B_0=\begin{pmatrix}
 1-np&\sqrt n\,p&0\\
 \sqrt n\,p&1-p-r&r\\
 0&r&1-r
 \end{pmatrix}
\]
containing eigenvalue \(1\), and for \(k=1,\dots,n-1\), blocks
\[
 B_k=\begin{pmatrix}
 1-p-r-2q(1-\cos(2\pi k/n))&r\\
 r&1-r
 \end{pmatrix}.
\]
The nontrivial eigenvalues are the two remaining radial eigenvalues and all the eigenvalues of the \(B_k\).

**2. A global lower bound.** Put \(c=\cos(2\pi/n)>0\). For any feasible \(p,q,r\), the first diagonal entry of \(B_1\) is at least \(c(1-p-r)\), using \(2q\le1-p-r\). Since \(p\le1/n\), and \(c>0\), its largest eigenvalue is at least that of
\[
 A(r)=\begin{pmatrix}c(1-1/n-r)&r\\r&1-r\end{pmatrix}.
\]
With \(\delta^2=1-c\) and \(t=1+\delta\), the positive vector \(v=(1,t)^T\) satisfies
\[
 v^T\begin{pmatrix}-c&1\\1&-1\end{pmatrix}v=-c+2t-t^2=0.
\]
Consequently its Rayleigh quotient in \(A(r)\) is independent of \(r\), and equals \(M=[c(1-1/n)+t^2]/(1+t^2)\). Thus every feasible matrix has \(\mu(P)\ge M\).

**3. Feasible construction and eigenvalue equality.** Choose \(p=1/n\), \(r=\rho=t[1-c(1-p)]/[\delta(1+t^2)]\), and \(q=(1-p-r)/2\). Direct multiplication gives \(A(\rho)v=Mv\). As \(\rho>0\) and \(v>0\), this is the larger eigenvalue of \(A(\rho)\).

We show \(0<\rho<1/2\), proving feasibility. Writing \(\delta=\sqrt2\sin(\pi/n)\), the formula and \(2+2\delta+\delta^2\ge2(1+\delta)\) yield
\[
 \rho\le\frac\delta2+\frac{p(1-\delta^2)}{2\delta}\le\frac\delta2+\frac{p}{2\delta}.
\]
For \(n\ge7\), the elementary bounds \(2/n\le\sin(\pi/n)\le\pi/n\) and \(\pi^2<10\) give
\[
 \rho\le\frac{\sqrt{20}}{2n}+\frac{1}{4\sqrt2}
 \le\frac{\sqrt{20}}{14}+\frac{1}{4\sqrt2}<\frac12.
\]
For \(n=6\), \(\delta=1/\sqrt2\) gives \(\rho\le\sqrt2/3<1/2\). For \(n=5\), \(\delta=\sqrt{(5-\sqrt5)/4}\in(4/5,5/6)\), so the sharper preceding bound gives \(\rho<5/12+9/200<1/2\). Since \(p\le1/5\), \(q=(1-p-\rho)/2>0\).

**4. All other eigenvalues fit the lower bound.** First we show \(M\ge1-p\). The difference is
\[
 M-(1-p)=\frac{p(1+\delta)^2-(1-p)\delta^2}{1+(1+\delta)^2}.
\]
Since \(\delta\le\sqrt{20}/n\), it suffices that \((1+n/(2\sqrt5))^2\ge n-1\). The difference is the everywhere-positive quadratic \(n^2/20+(1/\sqrt5-1)n+2\), whose discriminant is negative. Hence \(M\ge1-p\).

For the constructed chain, \(2q=1-p-\rho\), so \(B_k\) has upper-left entry \((1-p-\rho)\cos(2\pi k/n)\). Thus every \(B_k\) is bounded below in positive-semidefinite order by
\[
 B_{-}=\begin{pmatrix}-(1-p-\rho)&\rho\\\rho&1-\rho\end{pmatrix},
\]
and bounded above in its largest eigenvalue by \(B_1=A(\rho)\), because \(-1\le\cos(2\pi k/n)\le c\). The matrix
\[
 B_-+(1-p)I=\begin{pmatrix}\rho&\rho\\\rho&2-p-\rho\end{pmatrix}
\]
is positive semidefinite: its determinant is \(\rho(2-p-2\rho)>0\). Therefore every nonzero Fourier eigenvalue belongs to \([-(1-p),M]\subseteq[-M,M]\).

Since \(p=1/n\), the radial block has eigenvalues \(1,\lambda_+,\lambda_-\), where \(\lambda_+>0>\lambda_-\) are the roots of
\[
 f(z)=z^2-(1-p-2\rho)z-p(1-\rho).
\]
Both \(f(1-\rho)\) and \(f(-p-\rho)\) equal \(\rho(1-\rho)>0\), whereas \(f(0)<0\). Hence \(\lambda_+<1-\rho\le M\) and \(\lambda_->-(p+\rho)\). Since \(p+\rho<1/5+1/2<1-p\le M\), the radial eigenvalues also lie in \([-M,M]\). Thus the constructed matrix has \(\mu(P)=M\), attaining the global lower bound.

**5. Uniqueness within the invariant class and asymptotics.** Equality in the Rayleigh lower-bound chain requires \(p=1/n\) and \(q=(1-p-r)/2\), since \(c>0\) and the extremal Rayleigh vector has strictly positive coordinates. Equality of the top Rayleigh quotient then requires \(v\) to be an eigenvector, and its first coordinate fixes \(r=\rho\). The invariant optimizer is therefore unique. Finally \(\delta=\sqrt2\pi/n+O(n^{-3})\) and the exact identity \(1-M=[\delta^2+pc]/[1+(1+\delta)^2]\) give the stated gap expansion and pendant-weight limit. For maximum-degree weighting \(p=q=r=1/n\), the \(k=1\) Fourier block has eigenvalues \(1-(3\mp\sqrt5)/(2n)+O(n^{-2})\); its larger eigenvalue determines the asymptotic SLEM, giving the claimed comparison.

## Verification
Execute `python verify.py` with Python 3, NumPy and SymPy. It checks exact symbolic eigenvector and Rayleigh identities, rigorous trig-boundary constants, forty full graph eigenspectra, eight hundred feasible symmetric competitors and four asymptotic samples. The computed outcome was `VERIFY_OK symbolic_eigen_lemmas 6; trig_boundaries 5; dense_graphs 40; feasible_comparisons 800; asymptotic_samples 4`. The universal claim follows from the preceding argument, not from the finite computations.

## Relationship to prior work
Boyd, Diaconis and Xiao introduce the FMMC semidefinite objective. Boyd, Diaconis, Parrilo and Xiao develop the automorphism and Fourier reduction, and explicitly solve the **wheel** graph (hub plus cycle, without pendant leaves). The displayed proof uses that methodology, but the helm graph has an additional leaf orbit and a genuinely different three-block spectral calculation. Jafarizadeh studies clique lifts and several branched families in a more general reversible setting; its displayed result classes are not the same wheel-with-a-leaf-at-each-rim construction. No inspected primary statement gives the present closed formula or optimal invariant rim/leaf weights. Absence from the inspected texts is not a proof that no equivalent result exists.

## Limitations
The claim concerns \(n\ge5\), symmetric stochastic kernels and spectral modulus, not mixing time constants in other metrics. Global uniqueness beyond invariant kernels is not proved. The leading-order comparison with maximum-degree weighting does not assert domination over every other heuristic at every finite size. A search of primary literature and available mathematical records cannot exclude overlooked equivalent theorems; independent mathematical validation has not been performed.

## References
1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first publicly posted 2007-09-06. https://arxiv.org/html/0709.0955v1
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks (2020), DOI:10.1109/TSIPN.2020.2964211. https://www.researchgate.net/publication/338414306_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_Subgraphs
4. E. W. Weisstein, *Helm Graph*, MathWorld, https://mathworld.wolfram.com/HelmGraph.html
