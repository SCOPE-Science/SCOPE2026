# Exact coherent stationary state and Lindblad limit of an energy-space quantum walk

## Finding

Let \(\mathcal H=\ell^2(\mathbb N_0)\), with right unilateral shift \(S_+|n\rangle=|n+1\rangle\), left shift \(S_-=S_+^\dagger\), and ground projector \(P_0=|0\rangle\langle0|\). Fix rates \(0<a<b\), coherence parameter \(0\le\mu\le1\), and step \(0<h\le(a+b)^{-1}\). Define the collision-assisted energy-walk channel (the channel of [1], Eq. (39)) by
\[
\begin{aligned}
\Phi_h(\rho)={}&ahS_+\rho S_+^\dagger+bhS_-\rho S_-^\dagger
+[1-(a+b)h]\rho+bhP_0\rho P_0\\
&+\mu h\sqrt{ab}(S_+\rho P_0+P_0\rho S_-).
\end{aligned}
\]
Put \(q=a/b\in(0,1)\). Then **for every admissible \(h\)** the unique normal stationary density operator of \(\Phi_h\) is
\[
\boxed{\quad\langle n|\rho_*|m\rangle=(1-q)q^{(n+m)/2}\mu^{|n-m|},\qquad n,m\ge0.\quad}
\]
Here \(\mu^0=1\), including at \(\mu=0\). Its diagonal is the geometric Gibbs occupation distribution, and its exact purity is
\[
\boxed{\quad\operatorname{Tr}(\rho_*^2)=\frac{1-q}{1+q}\frac{1+q\mu^2}{1-q\mu^2}.\quad}
\]
Thus purity increases strictly with \(\mu\in[0,1]\), from the diagonal Gibbs value \((1-q)/(1+q)\) to unity. At \(\mu=1\), \(\rho_*=|\psi_0\rangle\langle\psi_0|\), where
\[|\psi_0\rangle=\sqrt{1-q}\sum_{n\ge0}q^{n/2}|n\rangle.\]
For \(0\le\mu<1\), it is a Poisson-kernel phase diffusion of that pure state:
\[
\rho_*=\int_0^{2\pi}\frac{1-\mu^2}{1-2\mu\cos\theta+\mu^2}
|\psi_\theta\rangle\langle\psi_\theta|\frac{d\theta}{2\pi},\qquad
|\psi_\theta\rangle=\sqrt{1-q}\sum_{n\ge0}q^{n/2}e^{in\theta}|n\rangle.
\]
In addition, the entire weak-step family is an **exact uniformization of one bounded Lindblad generator**:
\[
\boxed{\quad\Phi_h=I+h\mathcal L,\quad
\mathcal L(\rho)=\sum_{j=1}^3\left(J_j\rho J_j^\dagger-\tfrac12\{J_j^\dagger J_j,\rho\}\right),\quad}
\]
where
\[
J_1=\sqrt aS_++\mu\sqrt bP_0,\qquad
J_2=\sqrt{b(1-\mu^2)}P_0,\qquad J_3=\sqrt b S_-.
\]
In particular, \(e^{t\mathcal L}\) is a completely positive trace-preserving semigroup with the same unique normal stationary solution of \(\mathcal L(\rho)=0\). Write \(K=\|\mathcal L\|_{1\to1}\le2(a+b)\). For every \(T>0\) and admissible \(h\),
\[
\boxed{\quad\sup_{0\le t\le T}\|\Phi_h^{\lfloor t/h\rfloor}-e^{t\mathcal L}\|_{1\to1}
\le hK+\frac{T}{2}hK^2e^{hK}.\quad}
\]
The operator norms are induced by the trace norm on trace-class operators.

## Assumptions and scope

The system has the infinite nonnegative energy ladder, constant positive upward/downward rates with strict downward bias, and the precise boundary-coherence channel written above. The statement covers all coherence endpoints, including the fully incoherent \(\mu=0\) and pure-state \(\mu=1\) cases. A *normal stationary density operator* means a positive trace-class operator of unit trace fixed by the map. A stationary solution for \(\mathcal L\) is a trace-class density matrix annihilated by the generator. The theorem does not assert ergodic convergence of all initial states or embedding of each fixed \(\Phi_h\) as \(e^{h\widetilde{\mathcal L}}\).

## Proof

**1. Complete positivity and the continuous-time generator.** The unilateral shift obeys \(S_-S_+=I\), \(S_+S_-=I-P_0\), \(S_-P_0=P_0S_+=0\). Consequently the three bounded operators displayed above satisfy
\[\sum_{j=1}^3J_j^\dagger J_j=(a+b)I.\]
Expanding their gain terms gives precisely the two shift terms, the boundary term, and the two cross terms in \(\Phi_h\), with \(\Phi_h=I+h\mathcal L\). Since \(h(a+b)\le1\), the latter is the Kraus channel with operators \(\sqrt hJ_1,\sqrt hJ_2,\sqrt hJ_3,\sqrt{1-(a+b)h}I\). In particular it is completely positive and trace-preserving. Because \(\mathcal L\) is bounded and in GKSL form, \(e^{t\mathcal L}\) is a norm-continuous quantum Markov semigroup. More directly, \(e^{t\mathcal L}=e^{-(a+b)t}\sum_{k\ge0}\frac{[(a+b)t]^k}{k!}\mathcal P^k\), where the channel \(\mathcal P(\rho)=(a+b)^{-1}\sum_jJ_j\rho J_j^\dagger\), proving complete positivity and trace preservation for every \(t\ge0\).

**2. Diagonal uniqueness.** For any stationary density matrix, its diagonal \(d_n=\langle n|\rho|n\rangle\) obeys a classical birth-death balance: \(bd_1=ad_0\), and \(bd_{n+1}-(a+b)d_n+ad_{n-1}=0\) for all \(n\ge1\). Summability and normalization force \(d_n=(1-q)q^n\). This is independent of \(\mu\) and \(h\).

**3. Off-diagonal uniqueness.** For each offset \(r\ge1\), set \(c_n^{(r)}=\langle n+r|\rho|n\rangle\) for \(n\ge0\). At \(n\ge1\), stationarity gives
\[bc_{n+1}^{(r)}-(a+b)c_n^{(r)}+ac_{n-1}^{(r)}=0.\]
Its two characteristic roots are \(1\) and \(q\). Positivity and the fixed diagonal imply \(|c_n^{(r)}|^2\le d_{n+r}d_n\to0\) as \(n\to\infty\). Thus \(c_n^{(r)}=B_rq^n\), and the boundary \(n=0\) equation reads
\[bc_1^{(r)}-(a+b)c_0^{(r)}+\mu\sqrt{ab}\,c_0^{(r-1)}=0.\]
Here \(c_0^{(0)}=d_0=1-q\). Substituting \(c_1^{(r)}=qc_0^{(r)}\) yields the forced recursion \(c_0^{(r)}=\mu\sqrt q\,c_0^{(r-1)}\). Therefore
\[c_n^{(r)}=(1-q)q^{n+r/2}\mu^r\quad(r\ge1,n\ge0).\]
Hermiticity gives the corresponding lower-triangular entries. Every normal fixed density matrix must therefore have precisely the matrix stated in the finding. The same recurrence characterizes \(\ker\mathcal L\) because \(\Phi_h-I=h\mathcal L\) with \(h>0\).

**4. Existence and positivity.** For \(0\le\mu<1\), the displayed Poisson kernel is a positive normalized probability density on the unit circle whose \(r\)-th Fourier coefficient is \(\mu^{|r|}\); the integral of rank-one normalized projectors therefore has the stated entries. This provides a positive trace-one trace-class operator. At \(\mu=1\), the formula is the pure rank-one projector written above. Substitution in the diagonal and off-diagonal stationary recurrences verifies \(\mathcal L(\rho_*)=0\) entrywise. Since the generator is bounded on trace class, these matrix identities imply operator equality. Thus a unique stationary density matrix exists in both the discrete and continuous dynamics.

**5. Purity.** Absolute summability follows from \(q<1\) and \(\mu\le1\). Grouping the squared entries by \(r=|n-m|\) gives
\[
\operatorname{Tr}(\rho_*^2)=(1-q)^2\sum_{n,m\ge0}q^{n+m}\mu^{2|n-m|}
=\frac{(1-q)^2}{1-q^2}\left(1+2\sum_{r\ge1}(q\mu^2)^r\right),
\]
which simplifies to the advertised formula. This expression is strictly increasing in \(\mu\) on \([0,1]\) for every \(q\in(0,1)\) (with vanishing derivative only at the endpoint \(\mu=0\)).

**6. Uniform semigroup approximation.** On the trace class, \(\mathcal J(\rho)=\sum_jJ_j\rho J_j^\dagger\) has \(\|\mathcal J\|_{1\to1}=a+b\), because its normalized version is a channel; hence \(K=\|\mathcal J-(a+b)I\|\le2(a+b)\). The one-step remainder is bounded by \(\|e^{h\mathcal L}-(I+h\mathcal L)\|\le \tfrac12 h^2K^2e^{hK}\). Telescope the difference of \(\lfloor t/h\rfloor\) powers using that \(I+h\mathcal L\) and \(e^{h\mathcal L}\) are both trace-norm contractions; the accumulated error is at most \(ThK^2e^{hK}/2\). The unmatched terminal time is shorter than \(h\), and integration of the bounded generator contributes at most \(hK\). This proves the uniform estimate.

## Verification

Run `python verify.py` with NumPy installed. Five finite sections were checked for \((q,\mu)=(0.25,0),(0.25,0.5),(0.25,1),(0.4,0.7),(0.7,0.3)\), testing interior stationary equations, positivity and purity truncations; an additional rational calculation gives purity \(21/31\) at \(q=2/5,\mu=3/4\). Finite sections omit their artificial top boundary from stationary residual checks. These computational checks do not prove infinite-ladder statements; the proof above does.

## Relationship to prior work

Santos and Angelo [1], Eq. (39), introduce the exact discrete collision map, identify the decoupled geometric stationary populations, and derive perturbative coherence estimates (Sec. IV.4). Their Introduction and Conclusion explicitly leave the existence of an appropriate continuous-time limit unresolved; they do not provide the full all-parameter stationary density matrix or an exact purity law. The present finding derives these additional facts for their fixed constant-rate channel, without changing its jump model. Buecher [2] studies invariant states of more general quantum birth-death chains through existence conditions rather than this special model's closed stationary solution. Loebens [3] develops continuous-time open quantum walks and spectral methods for position processes with internal coin degrees of freedom; that setting does not supply the boundary-coherent stationary operator here. The underlying Poisson kernel and the standard Euler-to-semigroup bound are classical tools, not separately claimed as new.

## Limitations

Strict \(a<b\) is necessary here for the stated trace-one geometric fixed point; the critical and upward-biased regimes are excluded. Neither global trace-norm convergence from arbitrary initial states nor a sharp mixing-time estimate is proved. The approximation is for the explicitly chosen weak-step family, not a claim that a fixed non-infinitesimal collision channel has a Lindblad logarithm or arises from a Davies detailed-balance bath. The explicit stationary formula is specialized to constant rates and a single boundary-coherence parameter. Priority beyond the inspected literature remains unverified by independent assessment.

## References

[1] A. Spak dos Santos and R. M. Angelo, *Energy-space quantum walks: Thermalization without state convergence*, arXiv:2605.15339v1, submitted 14 May 2026, especially Sec. IV and Eq. (39). https://arxiv.org/html/2605.15339v1

[2] D. Buecher, *Invariant states of quantum birth and death chains*, arXiv:1408.6162, 2014, especially Introduction and Theorem 7. https://arxiv.org/abs/1408.6162

[3] N. Loebens, *Continuous-time open quantum walks in one dimension: matrix-valued orthogonal polynomials and Lindblad generators*, arXiv:2311.16366, 2023, especially Introduction and Sec. 3. https://arxiv.org/abs/2311.16366
