# Exact noise-coverage threshold and dark-state projection for rank-one bipartite quantum networks

## Finding
Let \(A\) and \(B\) be disjoint vertex classes of cardinalities \(a,b\ge2\). All edges between classes are present, but their complex hopping amplitudes are allowed to be nonuniform provided their coupling matrix factors as \(g u v^*\), where \(g\ne0\) and every component of \(u\in\mathbb C^a\) and \(v\in\mathbb C^b\) is nonzero. Put a positive local absorber at a fixed vertex \(w\in A\), and independent positive-rate site dephasers at an arbitrary set \(D\) disjoint from \(\{w\}\). Write \(F_A=A\setminus(D\cup\{w\})\), \(F_B=B\setminus D\), \(r=|F_A|\), and \(s=|F_B|\). Let \(u_F\) and \(v_F\) denote the coordinate restrictions of the coupling vectors.

Define the orthogonal projections
\[
Q_A=\begin{cases}I_{F_A}-|u_F\rangle\langle u_F|/\|u_F\|^2,&r>0,\\0,&r=0,\end{cases}
\qquad
Q_B=\begin{cases}I_{F_B}-|v_F\rangle\langle v_F|/\|v_F\|^2,&s>0,\\0,&s=0,\end{cases}
\]
where \(I_F\) denotes identity on the indicated coordinate subspace, extended by zero elsewhere. Put \(Q=Q_A\oplus Q_B\).

**Theorem.** For every initial density matrix \(\rho_0\), the unnormalized system density operator obeys
\[
\lim_{t\to\infty}\rho(t)=Q\rho_0Q,
\]
with exponential convergence at each fixed choice of nonzero couplings and positive absorption and dephasing rates. In particular,
\[
\dim\operatorname{Ran}Q=(r-1)_++(s-1)_+,
\qquad
P_{\mathrm{abs}}(\rho_0)=1-\operatorname{tr}(Q\rho_0).
\]
Here \((k-1)_+=\max(k-1,0)\) for integers \(k\ge0\). From a localized, undephased vertex \(x\in F_A\) the survival probability is \(1-|u_x|^2/\sum_{j\in F_A}|u_j|^2\); from \(y\in F_B\) it is \(1-|v_y|^2/\sum_{j\in F_B}|v_j|^2\). At the absorber or a dephased vertex the survival is zero. The formula remains valid when a free class is empty, with no localized sites in that class.

Full eventual absorption from *every* initial state occurs exactly when \(r\le1\) and \(s\le1\). Its **minimum local-dephaser budget** is \(a+b-3\), achieved in exactly \((a-1)b\) different placements: leave one nonabsorbing vertex of \(A\) and one vertex of \(B\) undephased. Thus asymmetric, arbitrarily small but positive site dephasing is sufficient at these placements; no smaller set is sufficient. For an initially maximally mixed state the surviving probability is \(((r-1)_++(s-1)_+)/(a+b)\).

## Assumptions and scope
Use the site basis of \(\mathbb C^a\oplus\mathbb C^b\). The Hermitian Hamiltonian and the trace-decreasing Lindblad generator are
\[
H=\begin{pmatrix}0&g u v^*\\\bar g v u^*&0\end{pmatrix},
\qquad
\mathcal L(\rho)=-i[H,\rho]-\frac\kappa2\{P_w,\rho\}
+\sum_{j\in D}\gamma_j\bigl(P_j\rho P_j-\tfrac12\{P_j,\rho\}\bigr),
\]
where \(P_j=|j\rangle\langle j|\), \(\kappa>0\), and all \(\gamma_j>0\). The evolution solves \(\dot\rho=\mathcal L(\rho)\), \(\rho(0)=\rho_0\). There is no additional uniform recombination, static diagonal disorder or unmonitored hopping. The model represents pure dephasing at specific sites and irreversible local loss at \(w\). The positive site-loss normalization means \(\dot {\operatorname{tr}\rho}=-\kappa\rho_{ww}\).

The factorization of *all* cross-class edge couplings is crucial: allowing a generic full-rank hopping matrix can remove the predicted dark states even without dephasing. The theorem does not assume identical couplings, real hopping phases, equal dephasing rates, or a particular initial pure state.

## Proof
**1. Invariant dark projection.** Every vector in \(\operatorname{Ran}Q_A\) is supported on \(F_A\) and orthogonal to \(u\), so \(H\) annihilates it. Likewise, every vector in \(\operatorname{Ran}Q_B\) is supported on \(F_B\) and orthogonal to \(v\), and is annihilated by \(H\). Both subspaces are orthogonal to \(w\) and each site in \(D\). Consequently \(HQ=QH=P_wQ=P_jQ=0\) for all \(j\in D\). The quantity \(Q\rho(t)Q\) is therefore exactly constant, equal to \(Q\rho_0Q\); the complementary block is invariant for the generator and cannot feed this protected block.

**2. Stationary positive operators have protected support.** Let \(\sigma\ge0\) satisfy \(\mathcal L(\sigma)=0\). Taking its trace yields \(\sigma_{ww}=0\), so positivity implies \(P_w\sigma=\sigma P_w=0\). Write \(S=\operatorname{Ran}\sigma\) and \(K=\ker\sigma\). For any \(z\in K\),
\[
0=\langle z,\mathcal L(\sigma)z\rangle
=\sum_{j\in D}\gamma_j\langle P_jz,\sigma P_jz\rangle.
\]
All summands are nonnegative, so \(P_jK\subset K\). As each \(P_j\) is self-adjoint, it also preserves \(S\); hence each dephasing dissipator has zero matrix block between \(K\) and \(S\). The absorption term does too. Evaluating the corresponding block of \(\mathcal L(\sigma)=0\) gives \(P_KH\sigma P_S=0\). Since \(\sigma\) is invertible on \(S\), we obtain \(HS\subset S\).

If \(P_jS\ne\{0\}\) for a dephasing site \(j\), the rank-one nature of \(P_j\), together with \(P_jS\subset S\), forces \(|j\rangle\in S\). This contradicts \(S\perp|w\rangle\) and \(HS\subset S\): when \(j\in B\),
\(\langle w,Hj\rangle=g u_w\overline{v_j}\ne0\); when \(j\in A\setminus\{w\}\),
\(\langle w,H^2j\rangle=|g|^2\|v\|^2u_w\overline{u_j}\ne0\).
Thus \(S\) is orthogonal to every dephased site.

The only nonzero eigenvalues of \(H\) are the two simple values \(\pm|g|\|u\|\|v\|\), with eigenvectors having a nonzero component at \(w\), because \(u_w\ne0\). An \(H\)-invariant subspace contained in \(\ker P_w\) cannot contain either nonzero-energy eigenvector. Hence \(HS=0\). The equations \(HS=0\), \(S\perp w\), and \(S\perp D\) say exactly that every vector in \(S\) belongs to \(\operatorname{Ran}Q\). Therefore **every positive stationary operator is supported on \(Q\)**.

**3. Long-time exhaustion of the complement.** For a positive initial matrix supported on \(R=I-Q\), \(\operatorname{tr}\rho(t)\) is nonincreasing. If its limit were positive, compactness of finite-dimensional positive matrices would yield a nonzero positive Cesàro accumulation point \(\sigma=\lim_{k\to\infty}T_k^{-1}\int_0^{T_k}\rho(t)\,dt\). Because
\(\mathcal L(\sigma)=\lim_{k\to\infty}(\rho(T_k)-\rho(0))/T_k=0\), the preceding step would put the support of \(\sigma\) inside \(Q\). But the evolved states remain supported on \(R\), a contradiction. Thus all population in \(R\) decays. By compactness of the density-matrix simplex and monotonicity of survival, a common time interval contracts the trace uniformly on positive matrices supported on \(R\); repetition gives exponential decay. For a general positive \(\rho_0\), positivity bounds its off-diagonal \(Q\)-\(R\) blocks by the geometric mean of the surviving block traces, so those coherences decay exponentially as well. Together with step 1 this proves the limiting density-matrix assertion.

**4. Dimensions and optimized placement.** In a free class of size \(r>0\), the one nonzero restriction \(u_F\) imposes exactly one independent linear constraint, leaving rank \(r-1\); similarly for \(s\). A class with no free vertices contributes zero. Thus the stated rank follows. Complete absorption for every initial state is equivalent to \(Q=0\), i.e. \(r,s\le1\). With the trap already occupying one vertex of \(A\), at least \(a-2\) other \(A\)-vertices and \(b-1\) \(B\)-vertices must be dephased. These placements have size \(a+b-3\), and selecting the two free vertices gives \((a-1)b\) choices. Evaluating the diagonal entries of \(Q_A,Q_B\) gives the sitewise probabilities. Taking the trace of \(Q/(a+b)\) gives the maximally mixed formula.

## Verification
The supplied `verify.py` independently constructs the full Lindblad superoperator on matrix units, checks its exact expected zero-eigenspace dimension numerically, and verifies that all other computed eigenvalues have strictly negative real part for \(168\) small systems and dephaser selections. It also compares four long-time density matrices with \(Q\rho_0Q\) using matrix exponentials. Replay with `python verify.py` after installing `requirements.txt`. The recorded output is `VERIFY_OK rank_one_bipartite_lindblad_cases=168 stationary_kernel=168 long_time_states=4`. These are finite corroborations, not proof of the uniform theorem; the proof above is analytic.

## Relationship to prior work
Novo, Chakraborty, Mohseni, Neven and Omar introduced exact invariant-subspace reduction for continuous-time graph quantum walks and studied complete bipartite graph search (preprint first posted 2014-12-22). Novo, Mohseni and Omar investigated dephasing-enhanced transport in trees and hypercubes (preprint first posted 2013-12-25). These establish physical and mathematical antecedents, not the evaluated selective-dephasing threshold for rank-one weighted complete bipartite couplings. Razzoli, Paris and Bordone evaluated coherent transport on complete bipartite graphs but explicitly excluded decoherence and coupling disorder. Le, Donati, Severini and Caruso studied noise-assisted destruction of dark states and other graph-control mechanisms, including all-site dephasing, without this arbitrary-site rank-one bipartite classification. The use of a stationary-support argument in the proof is standard finite-dimensional open-system theory; the claimed contribution is the evaluated coupling-weighted asymptotic projector, sitewise probabilities and optimal placement count.

## Limitations
Positive loss and dephasing strengths are essential to the stated long-time classification; setting a dephasing rate exactly to zero means removing that site from \(D\) and may cause a discontinuity in the infinite-time limit. No rate-uniform convergence constant is claimed as a dephasing strength tends to zero. The Hamiltonian has no independent site energies, diagonal interactions, nonfactorizable interclass coupling or general graph edges. The result says nothing about optimal finite-time collection or effects of global recombination. For example, replacing the rank-one \(2\times2\) cross-part hopping matrix by \(\begin{pmatrix}1&1\\1&2\end{pmatrix}\) removes the guaranteed one-dimensional dark subspace in the no-dephasing four-site case: its distinct singular directions both overlap with the absorbing first vertex. This is a boundary example, not an extension theorem. Potential equivalent specialized literature has not been exhaustively excluded; no independent review has been performed.

## References
1. L. Novo, M. Mohseni and Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, arXiv:1312.6989 (first public 2013-12-25), later *Scientific Reports* **6**, 18142 (2016), https://arxiv.org/abs/1312.6989.
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (first public 2014-12-22), later *Scientific Reports* **5**, 13304 (2015), https://arxiv.org/abs/1412.7209.
3. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794 (first public 2020-11-27), later *Entropy* **23**, 85 (2021), https://arxiv.org/abs/2011.13794.
4. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (first public 2017-07-24), later *Journal of Physics A* **51**, 365306 (2018), https://arxiv.org/abs/1707.07482.
