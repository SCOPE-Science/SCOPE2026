# Strong-loss mirror reciprocity and logarithmic boundary escape in a graded dissipative quantum walk

## Finding
Consider the two-sublattice finite open chain specified below, with arbitrary positive loss weights \(w_1,\ldots,w_N\), initially occupied only at an \(A\)-sublattice site \(S\). For each \(j\), the total probability of eventual escape through the lossy \(B_j\) site has a strong-loss limit \(\pi_j\). The limit is positive, sums to one, and obeys the **exact weighted mirror law**
\[
w_j\pi_j=w_{N+1-j}\pi_{N+1-j},\qquad 1\le j\le N.
\]
It is independent of the initial-site choice and hopping ratio at the level of this *pairwise identity*, although the individual probabilities depend on both. In particular, for the linear loss gradient \(w_j=j\), the far-left to far-right escape-probability ratio tends to exactly \(N\), at every fixed chain size.

The full limit is explicit. Put \(q_k=\pi k/(N+1)\) and
\[
F_{j,k}=t_1^2\sin^2(jq_k)+t_2^2\sin^2(q_k)\cos^2(jq_k),\qquad
D_k=\sum_{\ell=1}^N\frac{F_{\ell,k}}{w_\ell}.
\]
For all integers \(N\ge2\), \(1\le S,j\le N\), positive real \(t_1,t_2,w_1,\ldots,w_N\),
\[
\boxed{\pi_j=\frac{2}{N+1}\sum_{k=1}^N\sin^2(Sq_k)\frac{F_{j,k}/w_j}{D_k}.}
\]

There is also a sharp, sequential large-system law for linear weights and excitation at the rightmost \(A\) site. After first taking the strong-loss limit at each fixed \(N\),
\[
\boxed{\lim_{N\to\infty}(\log N)\pi_1
=C(t_1,t_2)=\frac4\pi\int_0^\pi
\frac{\sin^4 q\,[t_1^2+t_2^2\cos^2q]}{t_1^2+t_2^2\sin^2q}\,dq.}
\]
Consequently \(\pi_1\sim C(t_1,t_2)/\log N\) and \(\pi_N\sim C(t_1,t_2)/(N\log N)\) in that sequential limit. For the source-paper coupling values \(t_1=0.3\), \(t_2=0.5\), the coefficient is approximately \(0.737503087043\).

## Assumptions and scope
The Hilbert space is \(\mathbb C^N_A\oplus\mathbb C^N_B\), with open boundary conditions (all amplitudes at cell indices \(0\) and \(N+1\) vanish). Fix \(N\ge2\), \(1\le S\le N\), \(t_1,t_2>0\), and \(w_j>0\). Let \(D=\operatorname{diag}(w_1,\ldots,w_N)\). Define the Hermitian \(N\)-by-\(N\) matrix \(A\) and real symmetric matrix \(W\) by
\[
A_{j,j-1}=\frac{i t_2}{2},\quad A_{j,j+1}=-\frac{i t_2}{2},\qquad
W_{j,j}=t_1,\quad W_{j,j\pm1}=\frac{t_2}{2},
\]
whenever the indicated indices lie in the chain; all other entries are zero. In particular \(A^*=A\), \(W^*=W\). At loss scale \(\Gamma>0\), the non-self-adjoint no-jump Hamiltonian is
\[
H_\Gamma=\begin{pmatrix} A&W\\ W&-A-i\Gamma D\end{pmatrix}.
\]
This is exactly the open-chain two-sublattice model of Yuce and Ramezani (2022), with site-dependent loss \(\gamma_j=\Gamma w_j\) and their hopping convention. Set \(\psi(0)=(e_S,0)\), \(\psi(t)=e^{-itH_\Gamma}\psi(0)\), and
\[
P_j(\Gamma)=2\Gamma w_j\int_0^\infty|\psi_{B_j}(t)|^2\,dt.
\]
The \(P_j\) are site-resolved eventual loss probabilities. Theorem statements are for **fixed finite \(N\)** before taking \(\Gamma\to\infty\); the subsequent \(N\to\infty\) statement uses \(w_j=j\) and \(S=N\) after that first limit. There is no assertion about an arbitrary joint scaling of \(N\) and \(\Gamma\), full Lindbladian mixing, or unconditional arrival-time distributions.

## Proof
**1. Strict loss and decay at finite strength.** The dissipative identity gives
\[
\frac{d}{dt}\|\psi(t)\|^2=-2\Gamma\sum_{j=1}^Nw_j|\psi_{B_j}(t)|^2.
\]
If \(H_\Gamma\) had an eigenvector with a real eigenvalue, its \(B\)-component would vanish. Its \(A\)-component would then be an eigenvector of \(A\) annihilated by \(W\). But \(A\) has the simple eigenpairs
\[
\epsilon_k=t_2\cos q_k,\qquad
u_k(j)=i^j\sqrt{\frac{2}{N+1}}\sin(jq_k),\qquad k=1,\ldots,N.
\]
A direct calculation, including the open endpoints, yields
\[
(Wu_k)(j)=i^j\sqrt{\frac{2}{N+1}}
\big[t_1\sin(jq_k)+i t_2\sin q_k\cos(jq_k)\big].
\]
In particular the component at \(j=1\) is nonzero since \(t_1>0\) and \(\sin q_k>0\). Therefore all eigenvalues of \(H_\Gamma\) have strictly negative imaginary parts. The finite-dimensional propagator decays, so the integral exists and \(\sum_jP_j(\Gamma)=1\).

**2. Large-loss eigenmode reduction.** Write \(Q=WD^{-1}W\) and \(r_k=\langleu_k,Qu_k\rangle\). Every \(r_k>0\). Eliminating the fast \(B\) component via the Schur complement gives the slow effective matrix
\[
A-\frac{i}{\Gamma}Q+O(\Gamma^{-2}).
\]
Because the \(\epsilon_k\) are simple, the \(N\) slow eigenvalues and their \(B\)-amplitudes satisfy
\[
E_k(\Gamma)=\epsilon_k-\frac{i r_k}{\Gamma}+O(\Gamma^{-2}),\qquad
u_{k,B}(\Gamma)=-\frac{i}{\Gamma}D^{-1}Wu_k+O(\Gamma^{-2}).
\]
All remaining modes are fast, damped on a time scale of order \(\Gamma^{-1}\); an initially pure \(A\) state has fast-mode amplitude of order \(\Gamma^{-1}\). In the time integral defining \(P_j\), distinct slow frequencies have nonzero fixed gaps \(|\epsilon_k-\epsilon_\ell|\), so their off-diagonal oscillatory integrals contribute \(o(1)\), while the diagonal integrals have leading factor \(\Gamma/(2r_k)\). Thus
\[
\lim_{\Gamma\to\infty}P_j(\Gamma)
=\sum_{k=1}^N|u_k(S)|^2\frac{|(Wu_k)(j)|^2}{w_jr_k}.
\]
The finite matrix setting, spectral separation, and strictly positive \(r_k\) justify termwise limits; no numerical extrapolation is used as an infinite-size proof. Substituting the expressions in step 1, and cancelling the common \(2/(N+1)\) factor in the channel rates, gives the announced finite sum. Positivity and \(\sum_j\pi_j=1\) follow by construction.

**3. Weighted mirror reciprocity.** For integer \(k\), the identities
\[
\sin((N+1-j)q_k)=(-1)^{k+1}\sin(jq_k),\quad
\cos((N+1-j)q_k)=(-1)^k\cos(jq_k)
\]
imply \(F_{N+1-j,k}=F_{j,k}\). Multiplying the finite sum for \(\pi_j\) by \(w_j\) therefore gives exactly the same sum as multiplying \(\pi_{N+1-j}\) by \(w_{N+1-j}\). The conclusion is valid for each individual source \(S\), without averaging over injection sites or assuming the loss profile is symmetric.

**4. Sharp logarithmic law.** Now choose \(w_j=j\), \(S=N\), and abbreviate \(a=t_1^2\), \(b=t_2^2\), \(H_N=\sum_{j=1}^N j^{-1}\). Since \(\sin^2(Nq_k)=\sin^2q_k\),
\[
\pi_1=\frac{2}{N+1}\sum_{k=1}^N\sin^2q_k\,
\frac{F_{1,k}}{\sum_{j=1}^N F_{j,k}/j}.
\]
For \(q\) bounded away from \(0\) and \(\pi\), Dirichlet summation of \(\sum_{j=1}^N\cos(2jq)/j\) implies, uniformly on any compact interior subinterval,
\[
\frac{1}{H_N}\sum_{j=1}^N\frac{a\sin^2(jq)+b\sin^2q\cos^2(jq)}{j}
\longrightarrow\frac{a+b\sin^2q}{2}.
\]
To handle the endpoint modes without silently interchanging an unbounded limit, observe the **uniform inequality** for every integer \(j\):
\[
a\sin^2(jq)+b\sin^2q\cos^2(jq)
\ge\min(a,b)\sin^2q.
\]
Also \(F_{1,k}\le(a+b)\sin^2q_k\). Hence the summands in \(H_N\pi_1\), after extracting the normalized discrete sine weight, are bounded by \((a+b)/\min(a,b)\), independently of \(N,k\). The Riemann-sum limit and endpoint truncation are therefore justified. It yields the displayed integral for \(\lim H_N\pi_1\). Since \(H_N/\log N\to1\), the logarithmic assertion follows. Finally, the mirror identity for \(w_1=1\), \(w_N=N\) gives \(\pi_N=\pi_1/N\) exactly at every finite \(N\).

## Verification
An accompanying Python program constructs the physical \(2N\)-dimensional non-Hermitian Hamiltonian, solves its continuous Lyapunov equation for integrated finite-loss probabilities, and independently reconstructs the strong-loss formula both from the Hermitian eigenvectors and the trigonometric expression. It checks normalized probabilities, arbitrary positive nonsymmetric loss profiles, weighted mirror identities, and the linear-gradient endpoint ratio. It also performs numerical quadrature for the logarithmic coefficient and calculates increasing-chain examples. Example results are \(\pi_1\log N\approx0.6728613\) at \(N=60\), \(0.6818480\) at \(N=120\), and \(0.6991543\) at \(N=1200\), approaching the integral value \(0.7375030870\). These finite tests are corroboration only; the proof above supplies the all-parameter and asymptotic arguments. Run `python verify_loss.py` with NumPy and SciPy installed.

## Relationship to prior work
Wang, Liu, and Zhang (2020, arXiv:2011.07441) introduced and numerically investigated the same class of lossy bipartite walk with **uniform** dissipation, including counterintuitive edge escape. Yuce and Ramezani (2022, arXiv:2212.02879, Eq. (1), Figs. 2 and 5) studied the **graded** profile \(\gamma_j=\Gamma j\), finding numerically that increasing loss can produce a pronounced edge peak even without conventional skin localization. Their paper does not state the general strong-loss channel decomposition, weighted mirror identity for arbitrary profiles, or logarithmic sequential size law. Hu, Xue, Song, and Wang (2023, arXiv:2306.08676) obtained a Green-function formula and dynamical/steady-state correspondence, concentrating on **uniform** loss and bulk-edge power-law scaling; its quoted general resolvent identity does not supply the evaluated graded-loss high-absorption limits here. The mode elimination itself uses standard finite-dimensional perturbation theory; the claim is the explicit channel law and the consequences of the lattice symmetry, not a new general Zeno approximation theorem.

## Limitations
The \(\Gamma\to\infty\) limit must precede the \(N\to\infty\) limit; the proof gives no uniform error bound in growing \(N\). Neither the finite-loss peak maximum nor the full space-time escape distribution is classified. Finite-matrix checks do not replace the asymptotic argument. The literature comparison supports self-review, not independent priority certification; related general adiabatic-elimination theorems may contain ingredients of the method without stating the specialized weighted reciprocity and coefficient.

## References
1. C. Yuce and H. Ramezani, *Non-Hermitian edge burst without skin localizations*, arXiv:2212.02879v1 (first public 2022-12-06), *Physical Review B* **107**, L140302 (2023). https://arxiv.org/abs/2212.02879
2. L. Wang, Q. Liu, and Y. Zhang, *Quantum dynamics on a lossy non-Hermitian lattice*, arXiv:2011.07441 (2020), *Chinese Physics B* **30**, 020506 (2021). https://arxiv.org/abs/2011.07441
3. Y.-M. Hu, W.-T. Xue, F. Song, and Z. Wang, *Steady-state edge burst: From free-particle systems to interaction-induced phenomena*, arXiv:2306.08676 (2023), *Physical Review B* **108**, 235422 (2023). https://arxiv.org/abs/2306.08676
4. W.-T. Xue, Y.-M. Hu, F. Song, and Z. Wang, *Non-Hermitian edge burst*, arXiv:2109.14628 (2021), *Physical Review Letters* **128**, 120401 (2022). https://arxiv.org/abs/2109.14628
