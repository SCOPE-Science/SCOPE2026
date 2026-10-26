# Exact spectral-gap allocation for a clique with two leaves at distinct vertices

## Finding

For every integer \(k\ge1\), start with a clique of order \(k+2\). Mark distinct clique vertices \(A\) and \(B\), name the other vertices \(C_1,\ldots,C_k\), and attach leaves \(X\) to \(A\) and \(Y\) to \(B\). This connected graph has \(N=k+4\) vertices. Arbitrary nonnegative symmetric conductances are allowed on the existing edges, with total conductance exactly \(B>0\). Let \(L\) be the unnormalized weighted graph Laplacian and \(\lambda_2(L)\) its second-smallest eigenvalue.

Let \(u=u_k\in(0,1)\) be the unique solution of
\[
 u\sqrt{k(k+2)}=(k+4+4u)\sqrt{1-u^2}.
\]
Set \(H=k+4+4u\) and
\[
 V_k=2+\frac1u+\frac{4(1+u)^2+4k(1+u)+k(k-1)/2}{H}.
\]
Then the **exact optimum over every conductance vector**, including nonsymmetric allocations, is
\[
 \boxed{\max\lambda_2(L)=\Lambda_k(B)=\frac{B}{V_k}.}
\]
In particular, an optimal allocation is
\[
 \begin{aligned}
 w_{AB}&=\frac{4\Lambda_k(B)(1+u)^2}{H},\\
 w_{AC_i}=w_{BC_i}&=\frac{2\Lambda_k(B)(1+u)}{H},\\
 w_{C_iC_j}&=\frac{\Lambda_k(B)}{H}\quad(i\ne j),\\
 w_{AX}=w_{BY}&=\Lambda_k(B)\left(1+\frac1{2u}\right).
 \end{aligned}
\]
The third edge class is empty for \(k=1\). Every existing edge in the displayed allocation has strictly positive conductance. Its second Laplacian eigenvalue has multiplicity exactly \(k+1\). Moreover,
\[
 V_k=\frac{k}{2}+\frac72+2\sqrt2+o(1),\qquad
 \Lambda_k(B)\sim\frac{2B}{k}\quad(k\to\infty;\ B\text{ fixed}).
\]

## Assumptions and scope

All vertices carry unit mass. Conductances may be zero, but must be nonnegative and sum to \(B\); the objective uses the **unnormalized** Laplacian, not the normalized Laplacian or the discrete-time second-largest eigenvalue modulus. The family begins at \(k=1\) (a triangle with leaves attached at different clique vertices). No restriction to automorphism-invariant competitors is imposed. The displayed optimizer is exhibited, but uniqueness of the full optimizer set is not claimed.

## Proof

**1. Root and elementary identities.** Put \(N=k+4\), \(s=\tfrac12\sqrt{(k+2)/k}\), and \(t=\sqrt{1-u^2}\). The defining equation is equivalent to
\[
 \frac{ks-2t}{N}=\frac{t}{2u}.
\]
Writing \(t\in(0,1)\) and \(u=\sqrt{1-t^2}\), the left side minus the right side is strictly decreasing, starts positive at \(t=0\), and tends to minus infinity as \(t\uparrow1\), since its derivative is \(-2/N-1/[2(1-t^2)^{3/2}]\). Thus the root is unique. Let \(\mu=(2t-ks)/N\); then \(\mu=-t/(2u)<0\). Another rearrangement gives \(\mu/s=-k/H\), where \(H=N+4u\).

**2. Feasible Euclidean upper-bound configuration.** Choose vectors \(z_1,\dots,z_k\) with sum zero and with all pairwise squared distances one and individual squared norm \((k-1)/(2k)\). For \(k=1\), take \(z_1=0\); for \(k\ge2\), use a centered regular simplex. In mutually orthogonal coordinate spaces, define
\[
 \begin{aligned}
 q_A&=(1/2,0,0),& q_B&=(-1/2,0,0),\\
 q_{C_i}&=(0,-s,z_i),&q_X&=(1/2+u,t,0),\\
 &&q_Y&=(-1/2-u,t,0).
 \end{aligned}
\]
Every graph edge has squared Euclidean length exactly one: the \(AB\) edge by its first coordinate, each \(AC_i\) and \(BC_i\) edge from \(1/4+s^2+(k-1)/(2k)=1\), the \(C_iC_j\) edges from the regular simplex, and each pendant edge from \(u^2+t^2=1\). The mean configuration has only its second coordinate nonzero, equal to \(\mu\). Let \(Q\) contain these point coordinates as rows and \(Q_c\) their centered versions. Define \(V=\mathrm{tr}(Q_c^TQ_c)>0\). For any admissible weighted Laplacian, the Rayleigh principle yields
\[
 \lambda_2(L)V\le\mathrm{tr}(Q^TLQ)
 =\sum_{ij\in E}w_{ij}\|q_i-q_j\|^2=B.
\]
Thus \(\lambda_2(L)\le B/V\) globally, without any symmetry restriction.

**3. Exact saturation.** First set \(\lambda>0\) arbitrarily, and define weights by the displayed formulas with \(\Lambda_k(B)\) replaced by \(\lambda\). Direct substitution using \(\mu/s=-k/H\) and \(\mu=-t/(2u)\) gives
\[
 LQ=\lambda Q_c.
\]
For a check by invariant subspaces: in the antisymmetric coordinate, \(2w_{AB}+kw_{AC_i}=2\lambda(1+u)\) and \(w_{AX}u=\lambda(1/2+u)\). In the symmetric coordinate, \(2w_{AC_i}=\lambda(1+\mu/s)\) and \(w_{AX}t=\lambda(t-\mu)\). The missing distinguished-vertex equations follow by the zero row sums and the symmetry between those vertices. Finally the centered simplex modes have eigenvalue \(2w_{AC_i}+kw_{C_iC_j}=\lambda\). Therefore the stated coordinate columns span a \((k+1)\)-dimensional eigen-subspace with eigenvalue \(\lambda\).

The remaining nonzero eigenvalues are strictly larger. Indeed, the antisymmetric two-dimensional block has trace \(2w_{AB}+kw_{AC_i}+2w_{AX}>2\lambda\), and one eigenvalue \(\lambda\), so its other eigenvalue exceeds \(\lambda\). The symmetric three-dimensional block has eigenvalues \(0,\lambda\), and a third equal to \((k+2)w_{AC_i}+2w_{AX}-\lambda>\lambda\), because \(w_{AX}=\lambda(1+1/(2u))>\lambda\). For \(k>1\), the \(k-1\) peripheral-difference modes all have eigenvalue \(\lambda\). Consequently \(\lambda_2(L)=\lambda\), with exact multiplicity \(k+1\).

Because every allowed edge in the trial embedding has squared length one, the identity \(LQ=\lambda Q_c\) gives \(\sum_{ij}w_{ij}=\lambda V\). Summing the displayed conductances yields \(\sum_{ij}w_{ij}=\lambda V_k\), hence \(V=V_k\). Choosing \(\lambda=B/V_k\) gives total budget \(B\), attains the universal bound, and proves global optimality. All displayed weights are strictly positive since \(0<u<1\) and \(H>0\).

**4. Asymptotics.** The root equation in \(t\) and \(s=\tfrac12+O(1/k)\) implies \(t/u\to1\), so \(t,u\to1/\sqrt2\). Directly from the configuration, \(V_k=3k/4+3+2u-(2t-ks)^2/(k+4)\), which expands to the asymptotic expression in the finding.

## Verification

The included `VERIFY.py` performs independent numerical matrix assembly, root finding, all relevant eigenvalue checks, full-budget checks, and independent simplex edge-length checks for 33 graph sizes: each integer from \(1\) through \(30\), plus \(40\), \(60\), and \(100\). It requires Python, NumPy, and SciPy and prints `VERIFY_OK` when its assertions pass. The infinite-family result rests on the preceding analytic certificate, not on this finite replay.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) formulate the continuous-time budgeted spectral-gap problem and its maximum-variance dual, and solve several general graph examples. The present finding obtains an explicit family-specific scalar root, every optimal edge class in an attaining allocation, and Fiedler multiplicities for a complete core with two pendant leaves incident to **different** core vertices. The general SDP prescription by itself does not state these formulas. Jafarizadeh's later clique-lift and lollipop discussion addresses a discrete-time reversible-chain SLEM objective and different attachment structures; it does not imply the present continuous-time, total-rate-budget formula. This is a statement of inspected coverage, not a proof of exhaustive literature novelty.

## Limitations

The claimed optimum concerns undirected, unit-mass continuous-time chains and a fixed graph topology; it does not cover nonuniform vertex masses, directed rates, discrete-time stochasticity constraints, or three or more pendant leaves. Unrestricted uniqueness of the optimizer is not claimed. The root is defined implicitly by a one-dimensional equation, not by an elementary radical; it is unique and numerically evaluable. Earlier obscure case-specific spectral design work may remain unlocated.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, doi:10.1137/S0036144504443821 (public online 2006-11-02). Open author-hosted full text: https://stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421v1 (2025-01-05), https://arxiv.org/abs/2501.02421. Different discrete-time objective and graph constructions.
