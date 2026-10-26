# A two-clock empirical-law dichotomy for geometric-delay Bernoulli shifts

## Finding
Fix an integer \(b\geq2\) and \(0<p<1\). Let \(X=\{0,1\}^{\mathbb Z}\), \(\sigma:X\to X\) be the left shift \((\sigma\omega)_j=\omega_{j+1}\), and let \(\mathbb P_p\) be the two-sided independent Bernoulli law with \(\mathbb P_p(\omega_j=1)=p\). Starting at \(y_0=\omega\), define the *homogeneous geometric-delay trajectory*
\[
y_{n+1}=\sigma\bigl(y_{\lfloor n/b\rfloor}\bigr),\qquad n\geq0,
\]
and its binary observation \(a_n=(y_n)_0\). Write \(C_N=N^{-1}\sum_{n=0}^{N-1}a_n\) and \(T_k=(b^k-1)/(b-1)\) for \(k\geq0\).

For \(\mathbb P_p\)-almost every initial \(\omega\), simultaneously:

1. **All-time averages:** the set of limits along subsequences of \((C_N)_{N\geq1}\) is exactly \([0,1]\), even though the ordinary undelayed orbit has \(\lim_{k\to\infty}k^{-1}\sum_{j=0}^{k-1}\omega_j=p\).
2. **Completed-plateau averages:** the accumulation set of \((C_{T_k})_{k\geq1}\) is exactly
   \[
   K_b=\left\{(b-1)\sum_{r=1}^{\infty}b^{-r}\varepsilon_r:\varepsilon_r\in\{0,1\}\right\}.
   \]
   Thus \(K_2=[0,1]\), whereas for \(b\geq3\), \(K_b\) is a two-branch Cantor set with Hausdorff dimension \(\log 2/\log b\).
3. **Empirical law at geometric times:** the probability measures \(k^{-1}\sum_{j=1}^k\delta_{C_{T_j}}\) converge weakly to the explicit self-similar law
   \[
   \nu_{b,p}=\operatorname{Law}\left((b-1)\sum_{r=1}^{\infty}b^{-r}\xi_r\right),
   \qquad \xi_r\ \text{independent Bernoulli}(p).
   \]
   Its mean and variance are exactly \(p\) and \(p(1-p)(b-1)/(b+1)\). It has Hausdorff dimension \(H(p)/\log b\), where \(H(p)=-p\log p-(1-p)\log(1-p)\); for \(b=2,p=1/2\) it is Lebesgue measure on \([0,1]\), while it is singular with respect to Lebesgue measure whenever \(b\geq3\) or \(p\ne1/2\).

In particular, when \(b\geq3\), sampling at consecutive geometric plateau endpoints has a Cantor accumulation set, whereas sampling the same ordinary time averages at every integer time has the entire interval \([0,1]\) as its accumulation set.

## Assumptions and scope
The state space is the full **two-sided binary shift** with independent coordinate law; the observation is its coordinate-zero cylinder function. The delay is the exact integer rule \(h(n)=\lfloor n/b\rfloor\); the homogeneous weight is one. No assertion is made for general observables, non-Bernoulli laws, arbitrary delay functions, or nonhomogeneous delayed updates. All almost-sure statements refer to the single initial law \(\mathbb P_p\) and hold jointly for fixed \(b,p\).

## Proof
**Exact plateaus.** For \(k\geq0\), \(T_{k+1}=bT_k+1\) and \(T_{k+1}-T_k=b^k\). Induction using
\[
T_{k-1}\leq\left\lfloor\frac{n-1}{b}\right\rfloor<T_k\quad (T_k\leq n<T_{k+1})
\]
shows that \(y_n=\sigma^k\omega\) on the entire integer interval \([T_k,T_{k+1})\). Hence \(a_n=\omega_k\) there. In particular, for each \(j\geq1\),
\[
B_j:=C_{T_j}=\frac{\sum_{i=0}^{j-1}b^i\omega_i}{\sum_{i=0}^{j-1}b^i}
=\frac{(b-1)\sum_{r=1}^{j}b^{-r}\omega_{j-r}}{1-b^{-j}}.
\tag{1}
\]

**A stationary backward transform.** On the two-sided shift set
\[
\Psi(\eta)=(b-1)\sum_{r=1}^{\infty}b^{-r}\eta_{-r}.
\]
The series converges uniformly, so \(\Psi:X\to[0,1]\) is continuous. Let \(S_j=(b-1)\sum_{r=1}^{j}b^{-r}\omega_{j-r}\). Then \(0\leq S_j\leq1-b^{-j}\), \(B_j=S_j/(1-b^{-j})\), and \(0\leq\Psi(\sigma^j\omega)-S_j\leq b^{-j}\). Both \(B_j-S_j\) and \(\Psi(\sigma^j\omega)-S_j\) lie in \([0,b^{-j}]\). Thus
\[
\left|B_j-\Psi(\sigma^j\omega)\right|\leq b^{-j}.\tag{2}
\]

**Endpoint empirical law.** The Bernoulli shift is ergodic. For every continuous test function \(g:[0,1]\to\mathbb R\), Birkhoff's theorem applied to \(g\circ\Psi\) gives
\[
\lim_{k\to\infty}\frac1k\sum_{j=1}^{k}g(\Psi(\sigma^j\omega))
=\mathbb E_p[g(\Psi)]
\]
for almost every \(\omega\). Uniform continuity of \(g\) and (2) permit replacement by \(B_j\). A countable dense family of continuous tests yields weak convergence on a common full-measure set. Independence of the negative coordinates identifies the push-forward distribution as \(\nu_{b,p}\). Geometric summation gives its mean and variance.

**Endpoint accumulation set.** Every \(\Psi(\sigma^j\omega)\) belongs to compact \(K_b\), so (2) puts every endpoint accumulation point there. Conversely, almost every Bernoulli word contains every finite binary block arbitrarily far to the right, by ergodicity (or disjoint-block Borel–Cantelli). Each finite suffix of a prescribed backward digit sequence therefore occurs along infinitely many \(\sigma^j\omega\). Continuity of \(\Psi\), followed by (2), shows every element of \(K_b\) is an endpoint accumulation point.

**All-time accumulation set.** Almost every Bernoulli word contains arbitrarily long runs of zeroes and arbitrarily long runs of ones. If the \(m\) digits just before endpoint \(j\) are all one, (1) gives \(B_j\geq1-b^{-m}\); if they are all zero, (1) gives \(B_j\leq b^{-m}/(1-b^{-j})\). Consequently \(\limsup_j B_j=1\) and \(\liminf_j B_j=0\). All \(C_N\) lie in \([0,1]\), and the exact recursion
\[
C_{N+1}-C_N=\frac{a_N-C_N}{N+1},\qquad |C_{N+1}-C_N|\leq\frac1{N+1},
\]
means that a sequence attaining arbitrarily low and high levels, but with vanishing jumps, must have every intermediate level as a subsequential limit. Thus the full Cesàro accumulation set is exactly \([0,1]\). By the strong law, the undelayed digit mean is \(p\).

**Support and dimension.** The compact set \(K_b\) is invariant under the two similarities \(S_0(t)=t/b\) and \(S_1(t)=(b-1+t)/b\). For \(b=2\) their intervals tile \([0,1]\); for \(b\geq3\) they are separated by an open gap. The open-set condition holds for every integer \(b\geq2\), including the endpoint-touching binary case. Standard cylinder covering and mass-distribution bounds yield \(\dim_H K_b=\log2/\log b\) for \(b\geq3\) and the exact Bernoulli self-similar measure dimension \(\dim_H\nu_{b,p}=H(p)/\log b\). (The latter dimension is defined as the infimum of Hausdorff dimensions of Borel sets of full measure.) For \(b=2,p=1/2\), independent fair binary digits give Lebesgue distribution; otherwise \(H(p)<\log2\) when \(p\ne1/2\), or \(\log2<\log b\) when \(b\geq3\), proving singularity.

## Verification
Run \`python3 check.py\` from the same directory as this document. The deterministic program checks the actual delayed index recursion, plateau endpoints, finite backward-discount bounds, and exact first and second moment identities in rational arithmetic. Expected output is recorded in \`checker_output.txt\`. These finite checks are supplementary; the infinite almost-sure conclusions follow from the displayed proof, ergodicity, recurrence of words, and standard separated self-similar measure dimension estimates.

## Relationship to prior work
Gade and Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos* (arXiv:2610.21635, first submitted 2026-10-15), give the proportional-delay composition and plateau structure for scalar logistic and tent maps and explicitly note that delayed time averages need not agree with undelayed averages. The present statement instead classifies the complete *almost-sure accumulation sets and endpoint occupation law* of the homogeneous delay applied to a Bernoulli symbolic shift. The plateau recursion is a shared starting point, not a novel lemma. Classical Bernoulli measures and their dimensions are also prior background; the new identified relationship is their exact almost-sure emergence as the logarithmic-clock sampling law, together with the contrasting full-time accumulation interval.

Jones and Wierdl's work on convergence and divergence of general ergodic averages provides broader context, but the accessible abstract does not specify this delay or its endpoint law. Kempton and Persson study Bernoulli convolutions and one-dimensional maps, rather than this induced nonautonomous delayed trajectory. Broader weighted-ergodic or historic-behavior theorems could entail the accumulation assertion; priority for those general implications has not been independently established.

## Limitations
The theorem addresses almost-everywhere limits for fixed positive Bernoulli bias, not every deterministic symbolic sequence or nonlinear logistic-state observations. The self-similar measure dimensions use the classical open-set-condition theorem; only the delayed sampling mechanism and limit-law deductions are reconstructed directly here. The result concerns **empirical measures of scalar Cesàro averages at plateau endpoints**, not invariant distributions of the delayed state sequence or claims of mixing for the delayed nonautonomous dynamics.

## References
1. P. M. Gade and S. Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos*, arXiv:2610.21635 (first public submission 2026-10-15), https://arxiv.org/abs/2610.21635; full-text accessible rendering https://www.paperpeel.com/paper/2610.21635, especially Sections 2–4.
2. R. L. Jones and M. Wierdl, *Convergence and divergence of ergodic averages*, Ergodic Theory and Dynamical Systems (2008), https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/convergence-and-divergence-of-ergodic-averages/D4FB21EB33BECD29AEAB07834BDA6951 (abstract inspected).
3. T. Kempton and T. Persson, *Bernoulli convolutions and 1D dynamics*, Nonlinearity 28 (2015), 3921–3934, https://research-repository.st-andrews.ac.uk/handle/10023/9629 (repository record and abstract inspected).
4. J. E. Hutchinson, *Fractals and self-similarity*, Indiana University Mathematics Journal 30 (1981), 713–747 (standard self-similar measure dimension theorem).
