# The stiff-sweep spectral law and a path–star mixing reversal for edgewise midpoint diffusion on trees

## Finding

For any finite tree with positive edge rates and any once-per-sweep edge ordering, an edgewise Crank–Nicolson discretization of graph diffusion is strictly mixing at every finite positive step size, yet its subdominant spectral radius returns to one as the step size grows without bound. The leading large-step deficit is an explicit Fourier minimum on a limiting permutation cycle. For equal-rate paths and stars on \(n\ge4\) vertices, the star mixes faster for all sufficiently small steps, but the path mixes faster for all sufficiently large steps. At least one crossover therefore occurs.

Fix a tree \(T=(V,E)\) with \(n\ge2\), labeled vertices \(V=\{1,\ldots,n\}\), rates \(a_e>0\), and a fixed ordering \(e_1,\ldots,e_{n-1}\). For edge \(e=\{u,v\}\), write \(v_e=\mathbf e_u-\mathbf e_v\), \(Q_e=-a_ev_ev_e^\top\), and
\[
 C_e(h)=(I-\tfrac h2Q_e)^{-1}(I+\tfrac h2Q_e)
       =I-\frac{h a_e}{1+h a_e}v_ev_e^\top,\qquad h>0.
\]
Define the complete sweep \(M_h=C_{e_{n-1}}(h)\cdots C_{e_1}(h)\), and let \(\rho_\perp(M_h)\) be its spectral radius on \(\mathbf1^\perp\). Then \(\rho_\perp(M_h)<1\) for every \(h>0\), but \(\lim_{h\to\infty}\rho_\perp(M_h)=1\).

For an explicit coefficient, let \(S_e=I-v_ev_e^\top\), the transposition matrix exchanging endpoints of \(e\). Put \(K_j=S_{e_{j-1}}\cdots S_{e_1}\), with \(K_1=I\), and \(w_j=K_j^{-1}v_{e_j}\). The product \(P=S_{e_{n-1}}\cdots S_{e_1}\) is a single \(n\)-cycle. Choose any cyclic enumeration \(c_0,\ldots,c_{n-1}\) satisfying \(P\mathbf e_{c_\ell}=\mathbf e_{c_{\ell+1\pmod n}}\). If the endpoints of \(w_j\) appear \(d_j\in\{1,\ldots,n-1\}\) positions apart in that cycle, then
\[
 \rho_\perp(M_h)=1-\frac{\Gamma_T}{h}+O_T(h^{-2}),\qquad
 \Gamma_T=\min_{1\le k\le n-1}\frac4n\sum_{j=1}^{n-1}
 \frac{\sin^2(\pi k d_j/n)}{a_{e_j}}>0.
\]
Here the error term is for each fixed tree, rates and ordering; it is not uniform over growing families of trees.

For a unit-rate path ordered consecutively along the path, and a unit-rate star ordered consecutively through its leaves, respectively,
\[
\Gamma_{\mathrm{path}}=2,\qquad
\Gamma_{\mathrm{star}}=\frac{4(n-1)}n\sin^2(\pi/n).
\]
With common edge rate \(a\), divide both coefficients by \(a\). For each fixed \(n\ge4\), \(\Gamma_{\mathrm{star}}<\Gamma_{\mathrm{path}}\), whereas the small-step expansions are
\[
 \rho_\perp(M_h^{\mathrm{path}})=1-2a(1-\cos(\pi/n))h+O_n(h^2),\quad
 \rho_\perp(M_h^{\mathrm{star}})=1-ah+O_n(h^2).
\]
The inequalities of the mixing factors reverse between sufficiently small and sufficiently large steps.

## Assumptions and scope

The graph is a simple connected tree; every edge has a finite strictly positive rate; all edge updates use the same positive step size; and each tree edge is applied exactly once per sweep in a fixed order. The iteration is on vectors in \(\mathbb R^n\). Mixing speed refers to the spectral radius of the **complete-sweep** map on the zero-sum subspace, not to one-edge updates, a one-step singular norm, or the random-gossip expectation. The equal-rate path and star conclusions hold for any common positive rate with the stated natural ascending orders; known tree-edge order spectral invariance can extend the spectral comparison to other permutations of the same edges.

## Proof

**1. Finite-step mixing and the cycle limit.** On the two coordinates incident to \(e\), \(C_e(h)\) has diagonal weight \((1+h a_e)^{-1}\) and off-diagonal weight \(h a_e/(1+h a_e)\), with the unchanged coordinates acting as the identity. Thus each update is symmetric, stochastic and nonnegative, with positive diagonal and positive weight on its edge. Every original tree edge has both directions represented by positive entries in the sweep product: select its off-diagonal transition at that edge and diagonal transitions elsewhere. Consequently \(M_h\) is doubly stochastic, irreducible, and aperiodic, and its only eigenvalue of unit modulus is its simple eigenvalue one. The restriction to \(\mathbf1^\perp\) is therefore strictly spectrally contractive.

As \(h\to\infty\), \(C_e(h)\to S_e\), so \(M_h\to P\). Initially every vertex forms its own permutation cycle. Adding the edges of a tree in their prescribed order always joins two distinct forest components, so left-multiplication by the corresponding transposition merges two distinct permutation cycles. After \(n-1\) joins, \(P\) is one \(n\)-cycle. Its remaining eigenvalues have unit modulus, proving the return of \(\rho_\perp\) to one.

**2. Large-step expansion.** Write \(\varepsilon_j=(1+h a_{e_j})^{-1}\). Since \(S_{e_j}^2=I\), \(S_{e_j}v_{e_j}=-v_{e_j}\), and \(v_{e_j}^\top v_{e_j}=2\), there is the exact factorization
\[
 C_{e_j}(h)=S_{e_j}\bigl(I-\varepsilon_j v_{e_j}v_{e_j}^\top\bigr).
\]
Conjugating the factors into a frame fixed by their limiting permutations gives
\[
 P^{-1}M_h=I-\frac1h H+O_T(h^{-2}),\qquad
 H=\sum_{j=1}^{n-1}a_{e_j}^{-1}w_jw_j^\top.
\]
Because the eigenvalues of the single cycle \(P\) are simple, standard finite-dimensional first-order eigenvalue perturbation applies separately to every cycle Fourier vector \(u_k\). For mode \(k\ne0\), its eigenvalue has the form
\[
 \lambda_k(M_h)=\zeta_k\bigl(1-h^{-1}u_k^*Hu_k+O_T(h^{-2})\bigr),
 \qquad |\zeta_k|=1.
\]
The entries of \(u_k\) are \(n^{-1/2}\) times the phases \(e^{2\pi i k\ell/n}\). Thus \(|w_j^\top u_k|^2=4n^{-1}\sin^2(\pi k d_j/n)\), yielding the stated formula by maximizing \(|\lambda_k(M_h)|\) over finitely many nonconstant modes.

Every attenuation coefficient is strictly positive. Indeed, define \(T_j=K_j^{-1}S_{e_j}K_j=I-w_jw_j^\top\). The telescoping product \(T_1\cdots T_{n-1}=P\). If \(u_k^*Hu_k=0\), positivity of every summand forces \(w_j^\top u_k=0\) for all \(j\), and hence each \(T_j\) fixes \(u_k\). Then \(P u_k=u_k\), impossible for a nonconstant Fourier mode of an \(n\)-cycle.

**3. Two graph families.** On the consecutively ordered path \((1,2),(2,3),\ldots,(n-1,n)\), the transformed incidence vectors \(w_j\) connect vertex \(1\) to each of \(2,\ldots,n\), while the limiting permutation cycles through the path vertices in reverse order after the first. The transformed chord distances cover all integers \(1,\ldots,n-1\), so \(\sum_{d=1}^{n-1}\sin^2(\pi kd/n)=n/2\) for \(k\ne0\), giving \(\Gamma_{\mathrm{path}}=2/a\). On the consecutively ordered star \((1,2),(1,3),\ldots,(1,n)\), the transformed vectors connect consecutive vertices of the limiting \(n\)-cycle, giving \(\Gamma_{\mathrm{star}}=4(n-1)\sin^2(\pi/n)/(na)\); the minimizing nonconstant modes are \(k=1,n-1\).

Finally \(M_h=I-hL_T+O_T(h^2)\), where \(L_T=\sum_e a_ev_ev_e^\top\) is the graph Laplacian. Its algebraic connectivities are \(2a(1-\cos(\pi/n))\) for the path and \(a\) for the star. For \(n\ge4\), \(2(1-\cos(\pi/n))<1\) while \(4(n-1)\sin^2(\pi/n)/n<2\). The two strict spectral-radius inequalities therefore reverse at the endpoints, and continuity forces at least one intermediate crossover. No uniqueness of that crossover is asserted.

## Verification

The accompanying `verify.py` implements the individual edge matrices and complete products, checks exact rational stochasticity on paths and stars, checks the Fourier attenuation formula on both families and randomly generated weighted trees with reordered edges, and verifies the first matrix derivative symbolically for small trees. Running `python verify.py` with Python 3, NumPy and SymPy prints `VERIFY_OK 1198`. The finite calculations are not substituted for the cycle-merging and perturbation proofs of the assertions for every tree and every positive rate.

## Relationship to prior work

Spiteri and Wei study fractional-step Runge–Kutta products and their scalar / simultaneously diagonalizable linear stability framework; the present edge Laplacians on nontrivial trees do not commute. Yu, Anderson, Mou, Liu, He and Morse analyze deterministic periodic gossip on trees, prove edge-order spectral invariance, and explicitly allow common local averaging weights beyond one half (their Remark 3). Their path/star examples and topology comparisons concern the periodic gossip setting, not the parameter-asymptotic loss of contraction for the edgewise midpoint/Cayley updates as the common step tends to infinity. Edge-order invariance, periodic gossiping and tree-path/star benchmark choices are prior art, not claimed contributions. Chen, Belabbas and Liu study a wider class of gossip updates but do not supply the Fourier coefficient for the stiff permutation limit. The specific all-tree limiting-cycle Fourier law and the small-/large-step reversal are the assessed claims.

## Limitations

The big-O estimates are for fixed finite graphs, rates and orderings. The theorem does not cover arbitrary graphs with cycles, repeated/missing edge updates, time-varying schedules, nondiagonal/nonreversible generators, nonlinear dynamics, or a uniform-in-dimension asymptotic. Spectral-radius convergence describes asymptotic sweep mixing, not necessarily the Euclidean amplification of a single nonnormal sweep. The crossover's existence, not its number, exact position or uniqueness, is proved. No claim of independence from all existing operator-splitting or gossip literature is made.

## References

1. R. J. Spiteri and S. Wei, *Fractional-Step Runge–Kutta Methods: Representation and Linear Stability Analysis*, arXiv:2205.06365, first posted 2022-05-12. https://arxiv.org/abs/2205.06365
2. C. Yu, B. D. O. Anderson, S. Mou, J. Liu, F. He and A. S. Morse, *Distributed Averaging Using Periodic Gossiping*, IEEE Transactions on Automatic Control (2017), DOI:10.1109/TAC.2017.2688278.
3. X. Chen, M.-A. Belabbas and J. Liu, *Gossip over Holonomic Graphs*, arXiv:2102.08853, first posted 2021-02-17. https://arxiv.org/abs/2102.08853
