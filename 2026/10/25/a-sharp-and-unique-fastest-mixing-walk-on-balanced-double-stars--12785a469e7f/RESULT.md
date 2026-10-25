# A sharp and unique fastest-mixing walk on balanced double stars

## Finding
For every integer \(k\ge1\), consider the balanced double-star tree \(D_k\) with two adjacent hubs and \(k\) pendant leaves at each hub. Among **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices whose off-diagonal entries vanish outside this tree, there is a **unique** fastest-mixing matrix (minimizing the second-largest eigenvalue modulus, SLEM).

Put \(D=1+k(3+2\sqrt2)\). Its minimal SLEM is
\[
\mu_k^*=1-\frac{2}{D}.
\]
Every pendant edge has transition probability \(a_*=(2+\sqrt2)/D\), and the edge joining the hubs has transition probability \(b_*=[1+k(1+\sqrt2)]/D\). Every hub self-loop is zero, and every pendant-leaf self-loop is \(1-a_*\). No asymmetric assignment of individual edge probabilities can tie the optimum.

For \(k=1\), this specializes to the familiar optimal four-vertex path. For \(k\ge2\), it strictly improves both uniform maximum-degree weights and the equal-stationary-distribution Metropolis weights. If \(\gamma_k^{\mathrm{heur}}\) denotes the latter chain's SLEM gap, then
\[
\gamma_k^{\mathrm{heur}}=
\frac{k+3-\sqrt{(k+3)^2-8}}{2(k+1)},
\quad
\lim_{k\to\infty}\frac1k\frac{1-\mu_k^*}{\gamma_k^{\mathrm{heur}}}=3-2\sqrt2.
\]
Thus the best achievable gap is of order \(1/k\), while these standard chains have gap of order \(1/k^2\).

## Assumptions and scope
All graphs are finite and undirected. The two hub vertices, \(u\) and \(v\), are connected, and each has precisely \(k\) private degree-one neighbors. A feasible transition matrix \(P\) is real, symmetric, nonnegative entrywise, satisfies \(P\mathbf1=\mathbf1\), and has zero off-diagonal entries on nonedges. Nonnegative self-loops are allowed at all vertices. Feasibility does not require positive weights or irreducibility. Eigenvalues of \(P\) are ordered \(1=\lambda_1(P)\ge\lambda_2(P)\ge\cdots\), counting multiplicities, and \(\mu(P)=\max_{i\ge2}|\lambda_i(P)|\). This is an exact **discrete-time** Markov optimization, not an unconstrained signed consensus update or a continuous-time total-rate-budget optimization.

## Proof
**1. A graph-wide sharp certificate without assuming symmetry of the weights.** Write \(L=I-P\). Let \(A\) and \(C\) be the sums of the \(k\) pendant transition probabilities incident to \(u\) and \(v\), respectively, and let \(b=P_{uv}\). Stochasticity and nonnegative diagonal entries give \(A+b\le1\) and \(C+b\le1\).

Set \(t=1+\sqrt2\) and define a vector \(x\) which has value \(+t\) on all leaves incident to \(u\), value \(+1\) at \(u\), value \(-1\) at \(v\), and value \(-t\) on all leaves incident to \(v\). Then \(\mathbf1^\top x=0\),
\[
\|x\|^2=2(1+kt^2)=2D,
\quad x^\top Lx=2(A+C)+4b\le4.
\]
By Courant–Fischer, the algebraic connectivity \(\alpha=\lambda_2(L)\) satisfies \(\alpha\le2/D\). The second-largest eigenvalue of \(P\) is \(1-\alpha\), so for every feasible matrix, including a reducible one,
\[
\mu(P)\ge1-\alpha\ge1-2/D.
\]
Note that \(D>2\), so this is a positive bound.

**2. Construct a saturating stochastic chain.** Assign \(a=(2+\sqrt2)/D\) to every pendant edge and \(b=[1+k(1+\sqrt2)]/D\) to the central bridge. Direct arithmetic gives \(ka+b=1\), and both weights are strictly positive. Hub diagonal entries are therefore zero, and leaf diagonal entries are \(1-a\ge0\). The vector above satisfies \(Lx=(2/D)x\), as follows from the two scalar identities
\[
a(t-1)=\frac{2t}{D},\qquad k a(1-t)+2b=\frac2D.
\]
These identities and the construction prove equality in the lower-bound certificate.

**3. Show the negative spectrum cannot spoil SLEM optimality.** For a balanced double star with identical pendant weight \(a>0\) and central bridge weight \(b>0\), the full Laplacian eigenvalue multiset is
\[
0,\quad a\ (\text{multiplicity }2k-2),\quad (k+1)a,
\quad\eta_-,\quad\eta_+,
\]
where \(\eta_-<\eta_+\) are the roots of
\[
q(z)=z^2-[(k+1)a+2b]z+2ab.
\]
The symmetric hub/leaf constant subspace contributes \(0,(k+1)a\); antisymmetric hub/leaf constants give the displayed quadratic; and the within-leaf sum-zero spaces give eigenvalue \(a\). The inequalities \(0<\eta_-<a\) and \((k+1)a<\eta_+\) follow by evaluating \(q(0)=2ab>0\), \(q(a)=-ka^2<0\), and \(q((k+1)a)=-2kab<0\). They also hold for \(k=1\), when the multiplicity \(2k-2\) is zero.

For the constructed chain, \(\eta_-=2/D\), since \(x\) is the antisymmetric eigenvector and \(2/D<a\). Since \(ka+b=1\), the sum \(\eta_++\eta_-=(k+1)a+2b=1+a+b\le2\). Hence \(\eta_+\le2-\eta_-\), so the negative Markov eigenvalue cannot be more extreme than the positive nontrivial eigenvalue. It follows that \(\mu(P_*)=1-\eta_-=1-2/D\), attaining the universal lower bound.

**4. Prove uniqueness even among nonuniform matrices.** If any feasible \(P\) attains \(\mu(P)=1-2/D\), then the inequalities in step 1 are both equalities: its algebraic connectivity is \(2/D\) and \(x^\top Lx=4\). Thus both hub row-sum inequalities are equalities, meaning both hub self-loops vanish. Equality in the smallest Rayleigh quotient on \(\mathbf1^\perp\) additionally gives \(Lx=(2/D)x\). At each individual leaf, the corresponding equation forces its edge weight to be \([2/D]t/(t-1)=(2+\sqrt2)/D\). The hub constraint then forces the bridge weight to equal \(1-ka=b_*\). Every diagonal entry is determined by row stochasticity, proving global uniqueness.

**5. Compare with the heuristics.** Since both endpoints of every edge include a hub of degree \(k+1\), the maximum-degree and uniform-stationary Metropolis rules both give \(a=b=1/(k+1)\). The antisymmetric quadratic above gives the exact SLEM gap displayed in Finding. Their equality to the optimal chain at \(k=1\) and strict inferiority at every \(k\ge2\) follow from uniqueness and the fact that \(a_*=1/(k+1)\) holds exactly at \(k=1\). The asymptotic gap ratio follows by rationalizing the quadratic root. No asymptotic approximation is needed for the finite-\(k\) theorem.

## Verification
A standalone reproducible script `verify.py` checks the radical and eigenvector identities exactly using SymPy for all integers \(1\le k\le12\), constructs the full transition matrix and independently diagonalizes it numerically using NumPy, checks the Metropolis eigenvalue formula, and tests 2,000 additional random feasible matrices with individually different edge weights. The exact global result is proved in steps 1–4; finite tests only detect implementation or algebra slips. Reproduce using Python 3 with the versions in `requirements.txt` and run `python verify.py`. Observed output:

`VERIFY_OK: exact radical identities for 12 graph orders; 2000 fully nonuniform feasible competitors; stochasticity, 2k+2 eigenvalue comparisons and Metropolis asymptotic comparison`

## Relationship to prior work
Boyd, Diaconis, and Xiao (2004) formalized fastest mixing of nonnegative symmetric stochastic matrices as a semidefinite program; the current result gives a closed-form global solution for one entire diameter-three tree family and a direct equality/uniqueness certificate. Boyd, Diaconis, Sun, and Xiao (2006) solved paths, including the special case \(k=1\) here. Boyd, Diaconis, Parrilo, and Xiao (arXiv:0709.0955) analyze two **cliques** joined by a bridge and a complete binary tree. Their two-clique family has extra internal edges among the leaves; although its spectral block becomes relevant when those internal probabilities are forced to zero, its optimized full-clique solution uses positive internal weights, so it does not yield the present constrained optimum. Sun et al. (2006) solve a continuous-time total-rate-budget problem, not the present discrete-time vertexwise stochastic constraints. Jafarizadeh (arXiv:1003.3543) studies two star networks *sharing one center*, rather than distinct hubs joined by a bridge. These connections do not constitute a proof of historical novelty: a specialized unpublished or unindexed exact double-star formula remains a residual risk.

## Limitations
The claim concerns **balanced** double stars, symmetric nonnegative stochastic matrices, and uniform stationary distribution. It does not optimize nonreversible chains, arbitrary consensus matrices with negative entries, or unbalanced double stars. It makes no claim that the simple bound extends to other graph families. The archived 2003 technical-report version of the 2004 foundational article has a month-dated record but no independently verified public-release day in the examined evidence; 2004-10-29 is the earliest public exact date verified for a source directly used here.

## References
1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI:10.1137/S0036144503423264; publicly released electronically 2004-10-29. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007-09-06), subsequently SIAM J. Optim. 20 (2009), 792–819. Full text: https://arxiv.org/pdf/0709.0955.
3. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
4. S. Boyd, P. Diaconis, J. Sun, L. Xiao, *Fastest Mixing Markov Chain on a Path*, American Mathematical Monthly 113 (2006), 70–74. https://www.web.stanford.edu/~boyd/papers/fmmc_path.html.
5. S. Jafarizadeh, *Fastest Distributed Consensus Problem on Fusion of Two Star Networks*, arXiv:1003.3543 (2010). https://arxiv.org/pdf/1003.3543.
