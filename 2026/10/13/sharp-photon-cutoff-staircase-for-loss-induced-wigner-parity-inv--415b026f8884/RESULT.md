# Sharp photon-cutoff staircase for loss-induced Wigner parity inversion

## Finding
Fix an integer \(K\ge 2\), put \(m=\lfloor K/2\rfloor\), and define
\[
r_m=(2m)^{-1/(2m-1)},\qquad
B_K=-\frac{2m-1}{2m\pi}(2m)^{-1/(2m-1)}.
\]
Among all one-mode density operators \(\rho\) supported on Fock levels \(0,\dots,K\) with \(W_\rho(0)\ge0\), and all transmissivities \(\eta\in[0,1]\) of the quantum-limited pure-loss channel \(\mathcal L_\eta\), the exact minimum of the output Wigner function at the phase-space origin is
\[
\boxed{\min_{\rho,\,0\le\eta\le1} W_{\mathcal L_\eta(\rho)}(0)=B_K.}
\]
Equality occurs exactly at \(\eta=(1+r_m)/2\), when the only nonzero photon-number probabilities are \(\langle1|\rho|1\rangle=\langle2m|\rho|2m\rangle=1/2\). Coherences between these two Fock levels are unrestricted subject to positivity. The minimum has the exact two-step staircase \(B_{2m}=B_{2m+1}\), with \(B_{2m+2}<B_{2m}\), and \(\lim_{m\to\infty}B_{2m}=-1/\pi\).

## Assumptions and scope
Use the single-mode Wigner normalization \(W_\rho(0)=\frac2\pi\operatorname{Tr}(\rho\,(-1)^{\hat n})\), where \(\hat n\) is the photon number operator. The state \(\rho\) is any positive trace-one density operator with \(\rho=P_K\rho P_K\) for \(P_K=\sum_{j=0}^K|j\rangle\langle j|\); it need not be diagonal. Only nonnegativity of the **initial value at the origin** is imposed, not nonnegativity of the entire initial Wigner function. The attenuation is the standard vacuum-environment beamsplitter channel of intensity transmissivity \(\eta\). The optimization ranges over both preparations and transmissivities.

## Proof
Let \(p_j=\langle j|\rho|j\rangle\). The pure-loss channel has Kraus operators with matrix elements
\[
A_\ell|j\rangle=\begin{cases}\sqrt{\binom j\ell}\,\eta^{(j-\ell)/2}(1-\eta)^{\ell/2}|j-\ell\rangle,&\ell\le j,\\0,&\ell>j.\end{cases}
\]
Its output photon-number diagonal is the binomial thinning of \((p_j)\). The binomial theorem therefore yields the exact parity identity
\[
W_{\mathcal L_\eta(\rho)}(0)=\frac2\pi\sum_{j=0}^K p_j(1-2\eta)^j.
\]
In particular, off-diagonal input coherences do not contribute to this observable. For \(0\le\eta\le1/2\) every summand is nonnegative, while for \(\eta=1\) the output equals the constrained nonnegative initial value. Thus any strictly negative optimum uses \(1/2<\eta<1\).

Write \(r=2\eta-1\in(0,1)\) and \(w=\sum_{j\ \mathrm{odd}}p_j\). The input condition \(W_\rho(0)\ge0\) gives \(0\le w\le1/2\). Since every even \(j\le K\) obeys \(j\le2m\) and every odd \(j\ge1\), the inequalities \(r^j\ge r^{2m}\) on even indices and \(r^j\le r\) on odd indices give
\[
\sum_{j=0}^Kp_j(-r)^j
=\sum_{j\ \mathrm{even}}p_jr^j-\sum_{j\ \mathrm{odd}}p_jr^j
\ge(1-w)r^{2m}-wr
\ge\frac12(r^{2m}-r).
\]
Both inequalities are sharp simultaneously, for every \(r\in(0,1)\), precisely when \(w=1/2\), all even population occupies level \(2m\), and all odd population occupies level \(1\). Hence
\[
W_{\mathcal L_\eta(\rho)}(0)\ge\frac{r^{2m}-r}{\pi}.
\]
The function \(f_m(r)=r^{2m}-r\) is strictly convex on \((0,1)\), has \(f_m(0)=f_m(1)=0\), and has its unique global minimum at the root \(2mr^{2m-1}=1\), namely \(r=r_m\). Since \(r_m^{2m}=r_m/(2m)\), its minimum is \(-(2m-1)r_m/(2m)\). This gives \(B_K\), its attaining transmissivity, and all possible equality cases. Positivity allows every off-diagonal coherence between levels \(1\) and \(2m\) with modulus at most \(1/2\), and forces all other rows/columns to vanish because their diagonal entries are zero.

For \(m\ge1\), \(0<r<1\) gives \(r^{2m+2}-r<r^{2m}-r\), so their optimized minima satisfy \(B_{2m+2}<B_{2m}\). Dependence only on \(m=\lfloor K/2\rfloor\) gives \(B_{2m}=B_{2m+1}\). Finally \(r_m\to1\) as \(m\to\infty\), which implies \(B_{2m}\to-1/\pi\). This completes the proof.

## Verification
The self-contained standard-library Python program `verify_parity.py` checks binomial loss against a direct Kraus reconstruction for 5,600 randomly prepared pure-state/transmissivity pairs across cutoffs \(2\le K\le11\). It also checks exact equality examples, cutoff plateaus, strict staircase ordering, and a two-Fock-level radial example. Run it as `python3 verify_parity.py`. The analytic inequalities and convex minimization above are the proof for every cutoff, not consequences of the finite computations. At \(K=2\) or \(K=3\), the exact bound is \(-1/(4\pi)\), reached at \(\eta=3/4\) by equal population in levels \(1\) and \(2\).

## Relationship to prior work
Kenfack and Życzkowski study integrated Wigner negativity and Fock states, rather than this loss-and-cutoff optimization. Genoni and coauthors derive the same underlying binomial photon-loss model for an individual Fock input and analyze a quantum non-Gaussianity witness. Walschaers surveys Wigner negativity and Fock-state phase-space representations. These established ingredients are used here, while the objective, arbitrary-input origin-positivity constraint, sharp all-cutoff optimum and optimizer classification are different. Results about squeezing to protect Wigner negativity under transmission address another optimization objective. No claim is made that the underlying parity or binomial thinning formulas are new.

## Limitations
The constraint concerns only the origin value. The state achieving the bound may already have negative Wigner values away from the origin; passive loss does not create Wigner negativity from an everywhere nonnegative input Wigner distribution. The theorem is not a bound on the total integrated Wigner negativity, on the minimum over all phase-space points, or on a thermal or amplifying channel. Some nearby work on lossy, Fock-based Wigner negativity was available only in abstract form; equivalent formulations elsewhere remain a priority risk. The proof is elementary once its constrained physical observable is isolated, and independent priority validation has not been performed.

## References
1. A. Kenfack and K. Życzkowski, “Negativity of the Wigner function as an indicator of nonclassicality,” arXiv:quant-ph/0406015v1 (public 2004-06-02), https://arxiv.org/html/quant-ph/0406015v1 .
2. M. G. Genoni, M. L. Palma, T. Tufarelli, S. Olivares, M. S. Kim, and M. G. A. Paris, “Detecting quantum non-Gaussianity via the Wigner function,” arXiv:1304.3340, https://arxiv.org/html/1304.3340v2 .
3. M. Walschaers, “Non-Gaussian Quantum States and Where to Find Them,” arXiv:2104.12596, https://arxiv.org/html/2104.12596v3 .
4. R. Filip, “Gaussian quantum adaptation of non-Gaussian states for a lossy channel,” Physical Review A 87, 042308 (2013), https://doi.org/10.1103/PhysRevA.87.042308 (abstract examined; full text not available during comparison).
