# Sharp spectral relaxation at the admissibility boundary of a Dicke-state open quantum walk

## Finding

Consider the ring transition matrix associated with the Dicke-state preparation construction of Linck and Bernardes, at the joint-size admissibility boundary described below. Let \(H_N=\sum_{j=1}^N j^{-1}\), and let \(\Delta_N\) be its **absolute spectral gap**, meaning one minus the maximum modulus of all nonstationary eigenvalues. As the number \(N\) of ring vertices (and register qubits) tends to infinity,
\[
\boxed{\Delta_N=\frac{\pi^4}{3(N+1)H_N^3}-\frac{\pi^8}{90(N+1)H_N^5}+O\!\left(\frac1{N H_N^6}\right).}
\]
This is a genuine two-term asymptotic for the **exact** spectral gap, not an approximation based on assuming that every jump probability is small. In particular \(\Delta_N\sim\pi^4/[3N(\log N)^3]\), even though the largest jump probability tends to one and equals one for odd \(N\). The ring's mean time \(T_N\) for one full lap satisfies \(T_N=(N+1)H_N/2\), so
\[
\frac{\Delta_N^{-1}}{T_N}\sim\frac{6}{\pi^4}H_N^2.
\]
Thus the relaxation scale is a diverging squared-logarithmic factor longer than a complete average circulation. These assertions concern the ring's position distribution and do not imply a preparation-fidelity theorem for unmeasured coherent degrees of freedom.

## Assumptions and scope

Fix any elementary jump parameter \(p\in(0,1]\). For each integer \(N\ge3\), take the admissibility-boundary normalization \(A_N=(N+1)\sqrt p/2\). On sites \(k\in\{0,\ldots,N-1\}\), define
\[
p_{N,k}=\frac{p(k+1)(N-k)}{A_N^2}=\frac{4(k+1)(N-k)}{(N+1)^2},\qquad q_{N,k}=1-p_{N,k}.
\]
The row-stochastic transition matrix \(T_N\) has entries \((T_N)_{k,k}=q_{N,k}\) and \((T_N)_{k,k+1\bmod N}=p_{N,k}\), with all other entries zero. The rates are positive and at most one. The matrix is irreducible and aperiodic (some diagonal entries are strictly positive). It has simple eigenvalue one. Let
\[
\Delta_N=1-\max\{|\lambda|:\lambda\in\operatorname{spec}(T_N),\ \lambda\ne1\},
\qquad S_j(N)=\sum_{k=0}^{N-1}p_{N,k}^{-j}.
\]
All limits below are along integers \(N\to\infty\). The parameter \(p\) cancels identically from this boundary family. The primary mathematical subject is quantum mechanics on a graph, MSC2020 81Q35.

## Proof

**1. Exact cyclic characteristic equation.** The eigenvalue equation along successive ring sites gives
\[
\prod_{k=0}^{N-1}(\lambda-q_{N,k})=\prod_{k=0}^{N-1}p_{N,k}.
\]
With \(\delta=1-\lambda\), it becomes \(\prod_k(1-\delta/p_{N,k})=1\). Near \(\delta=0\) choose the logarithms analytic at zero. The nonstationary winding-one branch solves
\[
F_N(\delta):=\sum_k\log(1-\delta/p_{N,k})=2\pi i.
\]

**2. Moment scales and existence of the winding-one pair.** The partial-fraction identity
\[
\frac1{p_{N,k}}=\frac{N+1}{4}\left(\frac1{k+1}+\frac1{N-k}\right)
\]
gives, with \(H_N^{(2)}=\sum_{j=1}^Nj^{-2}\),
\[
S_1=\frac{N+1}{2}H_N,\qquad
S_2=\frac{(N+1)^2}{8}H_N^{(2)}+\frac{N+1}{4}H_N.
\]
For every fixed integer \(j\ge2\), \(S_j=O(N^j)\), and specifically
\[
S_4=\frac{(N+1)^4}{128}\zeta(4)+O(N^3).
\]
Also \(p_{N,\min}=4N/(N+1)^2\). On a disk of radius proportional to \(1/(NH_N)\), the quantities \(|\delta|/p_{N,k}\) are uniformly \(O(1/H_N)\). Consequently
\[
F_N(\delta)=-\sum_{j\ge1}\frac{S_j\delta^j}{j}
\]
converges there. Comparison with \(-S_1\delta-2\pi i\), on a small circle centered at \(-2\pi i/S_1\) with radius a sufficiently large constant times \(1/(NH_N^3)\), gives exactly one solution by Rouché's theorem for sufficiently large \(N\). Its complex conjugate corresponds to the opposite winding.

Set \(t=2\pi/S_1\), \(a=S_2/(2S_1)\), \(b=S_3/(3S_1)\) and \(c=S_4/(4S_1)\). Analytic inversion of \(\delta+a\delta^2+b\delta^3+c\delta^4+\cdots=-it\) yields
\[
\delta=-it+a t^2+i(2a^2-b)t^3+(-5a^3+5ab-c)t^4
+O\!\left(\frac1{NH_N^6}\right).
\]
Here \(a=O(N/H_N)\), \(b=O(N^2/H_N)\), and \(c=O(N^3/H_N)\). Expanding \(\operatorname{Re}\log(1-\delta)\) through fourth order, and bounding the higher inverse-series terms with \(S_j=O(N^j)\), gives
\[
-\log|1-\delta|=\frac{2\pi^2(S_2-S_1)}{S_1^3}
-\frac{4\pi^4S_4}{S_1^5}
+O\!\left(\frac1{NH_N^6}\right).
\]
The omitted fourth-order combinations (such as the \(S_2S_3\) term) are \(O(1/(NH_N^6))\), and the first nonzero sixth-order contribution is smaller. Since \(-\log|1-\delta|=O(1/(NH_N^3))\), replacing minus log modulus by \(1-|1-\delta|\) changes the result only by \(O(1/(N^2H_N^6))\).

**3. The winding-one eigenvalues really determine the gap.** Write \(q_k=q_{N,k}\), and put \(q_{\max}=1-4N/(N+1)^2\). For \(r\in(q_{\max},1)\) near one and \(0\le\theta\le\pi\), set
\[
U(r,\theta)=\sum_k\log\frac{|re^{i\theta}-q_k|}{p_{N,k}}.
\]
At fixed \(r\), \(U\) strictly increases with \(\theta\in(0,\pi)\): differentiation of each squared modulus gives \(2rq_k\sin\theta\ge0\), and some \(q_k>0\). Further \(U(r,0)<0\) and \(U(r,\pi)>0\) for all sufficiently large \(N\) and all \(r\) between the winding-one root's modulus and one. Thus \(U=0\) defines a unique \(\theta(r)\) in this interval. Because \(\partial_rU>0\) when \(r>q_{\max}\), \(\theta(r)\) increases strictly as \(r\) decreases.

Along this modulus-one-product curve define
\[
V(r)=\sum_k\arg(re^{i\theta(r)}-q_k),
\]
using arguments in \((0,\pi)\). The elementary derivative formulas
\[
\partial_\theta\arg(re^{i\theta}-q)=\frac{r(r-q\cos\theta)}{|re^{i\theta}-q|^2}>0,
\quad
\partial_r\arg(re^{i\theta}-q)=\frac{-q\sin\theta}{|re^{i\theta}-q|^2}\le0
\]
show that \(V(r)\) increases strictly as \(r\) decreases, starting at zero as \(r\uparrow1\). At the constructed eigenvalue \(V=2\pi\), since it is the winding-one solution. No larger modulus below one can therefore satisfy the eigenvalue requirement \(V\in2\pi\mathbb Z\); complex conjugation handles the lower half-plane. This proves that the winding-one conjugate pair is the subdominant spectral pair for all sufficiently large \(N\).

**4. Sharp expansion and observable timescale.** Since \(\zeta(2)=\pi^2/6\), \(\zeta(4)=\pi^4/90\), inserting the exact \(S_1,S_2\) and asymptotic \(S_4\) into step 2 gives
\[
\Delta_N=\frac{\pi^4}{3(N+1)H_N^3}
-\frac{\pi^8}{90(N+1)H_N^5}
+O\!\left(\frac1{NH_N^6}\right).
\]
The time to circulate once is the sum of independent geometric mean holds, \(T_N=S_1=(N+1)H_N/2\), proving the scale separation in the finding. As one operational consequence, for the worst starting site, the total-variation mixing time at any fixed \(0<\varepsilon<1/2\) obeys
\[
t_{\mathrm{mix}}(\varepsilon)\ge
\frac{\log(1/(2\varepsilon))}{-\log(1-\Delta_N)}.
\]
Indeed a right eigenfunction of eigenvalue modulus \(1-\Delta_N\) can be normalized to sup norm one and has stationary mean zero, so some starting point retains expectation of modulus \((1-\Delta_N)^t\); this is bounded above by twice the total-variation distance. The bound gives a rigorous \(\Omega(N(\log N)^3)\) worst-start relaxation obstruction.

## Verification

Run `python3 verify.py` from this directory (standard library only). The program uses exact fractions to check the moment identities and the positivity of transition probabilities for \(2\le N\le40\), then locates the winding-one complex root numerically and checks its characteristic-log residual for \(N=20,50,100,200,500\). These finite tests reproduce the coefficient scales but do not replace the analytic root ordering, asymptotic estimates, or infinite-\(N\) proof. All analytical constants and error classes are determined in the proof.

## Relationship to prior work

Linck and Bernardes, *State Preparation Protocols for Entangled States via Open Quantum Walks* (arXiv:2608.07695v1, publicly submitted 2026-08-07), derive this ring's stationary law, circulation time, exact characteristic equation (their Eq. 47), and a **second-order approximate** gap formula (their Eqs. 48–52), emphasizing a regime where all jump probabilities are small. Their finite-size plots hold the control normalization fixed and are subject to an upper admissible register size. The present result instead takes the physically permitted joint-size boundary \(A_N=(N+1)\sqrt p/2\), where the maximum jump probability is of order one. It rigorously identifies which exact complex eigenpair controls the absolute spectral gap, supplies the explicit negative \(H_N^{-5}\) correction absent from the second-order approximation, and quantifies the squared-logarithmic separation between one-lap and relaxation times. The leading coefficient is consistent with their formula when formally evaluated along this boundary; it is **not** claimed as a novel coefficient on its own.

General spectral facts about irreducible stochastic matrices, analytic inversion, and total-variation duality are classical background. The result does not claim a new general theory of cyclic Markov chains or an improvement to arbitrary state-preparation protocols.

## Limitations

The spectral-gap identity and two-term asymptotic are proved for the specific ring at the displayed admissibility boundary, not for arbitrary varying rate profiles or every normalization trajectory. The lower bound concerns worst-start position mixing; nonnormality means the spectral gap alone does not give a matching uniform upper mixing bound, nor does position mixing alone certify arbitrary internal-state preparation fidelities. The displayed asymptotic error is not a finite-\(N\) certified numerical error bar. The originality comparison is limited to the inspected primary paper, related abstracts, relevant available records, and targeted literature searches; unindexed or inaccessible stronger results remain possible. Independent audit has not been performed.

## References

1. P. Linck and N. K. Bernardes, *State Preparation Protocols for Entangled States via Open Quantum Walks*, arXiv:2608.07695v1 (2026-08-07), https://arxiv.org/html/2608.07695 . In particular §§ IV.2–IV.3 and Eqs. (40), (47)–(52).
2. P. Linck and N. K. Bernardes, *Thermodynamics of linear open quantum walks*, arXiv:2601.22064v1 (2026-01-29), https://arxiv.org/abs/2601.22064 . Background for the distinct linear-walk framework.
3. S. Attal, F. Petruccione, C. Sabot, and I. Sinayskiy, *Open Quantum Random Walks*, arXiv:1402.3253 (2014), https://arxiv.org/abs/1402.3253 . General open-quantum-walk framework.
