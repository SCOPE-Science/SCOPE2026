# Pathwise stabilization and independent Gaussian–geometric limits for biased cycle coverage

## Finding
Fix a clockwise probability \(p\in(1/2,1)\), put \(q=1-p\), \(d=p-q\) and \(r=q/p\). Use one sequence of independent increments \((\xi_t)_{t\ge1}\), each equal to \(+1\) with probability \(p\) and \(-1\) with probability \(q\), to couple nearest-neighbour walks on every cycle \(C_n\), \(n\ge3\). Write \(S_t=\sum_{i=1}^t\xi_i\), \(S_0=0\), and let \(T_n\) and \(L_n\in\{1,\ldots,n-1\}\) be the first full-vertex-cover time and the final new vertex (labelled clockwise from the starting vertex \(0\)) on \(C_n\). Set \(J=-\inf_{t\ge0}S_t\), and \(H_b=\inf\{t\ge0:S_t=b\}\) for integers \(b\ge0\).

**Pathwise stabilization.** With probability one there exists a finite random integer \(N\) such that, simultaneously for **every** \(n\ge N\),
\[
 n-1-L_n=J,\qquad T_n=H_{n-1-J}.
\]
The terminal deficit has the nondegenerate geometric law \(\Pr(J=j)=(1-r)r^j\), \(j=0,1,\ldots\). In particular, across increasing cycle sizes under this coupling the deficit is eventually **exactly the same random integer**, rather than merely converging in distribution.

**Joint fluctuation law.** As \(n\to\infty\),
\[
 \left(\frac{T_n-n/d}{\sqrt{(4pq/d^3)n}},\ n-1-L_n\right)
 \Longrightarrow (Z,J),
\]
where \(Z\) is standard normal and **independent** of \(J\). The almost-sure identity and joint independence are included in the single assessed claim; the classical marginal geometric last-vertex law and ordinary random-walk first-passage CLT alone are not claimed as new.

## Assumptions and scope
The walk is discrete-time, nearest-neighbour, clockwise-biased with a fixed probability \(1/2<p<1\), and every cycle starts at vertex \(0\). The coupling across \(n\) uses the **same** increments, not independent experiments for different cycles. The global infimum \(\inf_{t\ge0}S_t\) is an attained finite integer almost surely because \(S_t/t\to d>0\) almost surely. Finite-size last-vertex laws are known from the source paper and are not the assessed contribution. Reversing clockwise/counterclockwise gives the analogous statement for \(0<p<1/2\) after relabelling, but the displayed formula is written only for \(p>1/2\).

## Proof
**1. Lift the cover time to a growing range.** Let \(M_t=\max_{0\le s\le t}S_s\), \(m_t=\min_{0\le s\le t}S_s\). Because all steps are \(\pm1\), the set of lifted positions visited through time \(t\) is the entire integer interval \([m_t,M_t]\cap\mathbb Z\). Its reduction modulo \(n\) covers the cycle exactly when \(M_t-m_t\ge n-1\). The span increases at most one per step. Consequently
\[
 T_n=\inf\{t:M_t-m_t=n-1\},\qquad L_n\equiv S_{T_n}\pmod n.
\]
At \(T_n\), the lifted walker is necessarily at the **new** minimum or maximum.

**2. Stabilization after the last global-minimum epoch.** The strong law makes \(m_\infty=\inf_{t\ge0}S_t=-J\) finite and attained; let \(\tau\) be any finite time by which it has first been attained. Define \(K=M_\tau\), finite almost surely. For all \(n>K+J+2\), the range before and at \(\tau\) is smaller than \(n-1\). Thereafter the running minimum is fixed at \(-J\). The next time its range reaches \(n-1\) is the first visit to the new maximum \(n-1-J\), which is \(H_{n-1-J}>\tau\). Thus \(T_n=H_{n-1-J}\), and its final new residue is \(n-1-J\) (which is between \(1\) and \(n-1\) for all sufficiently large \(n\)). This establishes both pathwise identities simultaneously for every sufficiently large \(n\).

**3. Global minimum distribution.** For every integer \(j\ge0\), the classical two-barrier ruin formula, sending the right barrier to infinity, gives \(\Pr(H_{-j}<\infty)=r^j\). Equivalently \(\Pr(J\ge j)=r^j\), hence \(\Pr(J=j)=(1-r)r^j\).

**4. Passage-time moments and Gaussian limit.** By the strong Markov property and spatial homogeneity, \(H_b=\sum_{i=1}^b D_i\) for \(b\ge1\), where \((D_i)\) are i.i.d. copies of \(H_1\). The drift and centered-square martingales yield
\[
 \mathbb ED_1=\frac1d,\qquad \operatorname{Var}(D_1)=\frac{4pq}{d^3}.
\]
These identities also follow by differentiating the first-passage generating function \(\mathbb E[z^{D_1}]=(1-\sqrt{1-4pqz^2})/(2qz)\). Since \(d>0\), \(D_1\) has exponential tails (the generating function is finite on an interval strictly past \(z=1\)). The i.i.d. CLT therefore gives
\[
 \frac{H_n-n/d}{\sqrt{(4pq/d^3)n}}\Longrightarrow N(0,1).
\]
For each fixed integer \(K_0\), on \(\{J\le K_0\}\) and for \(n>K_0+1\), monotonicity of hitting times gives \(0\le H_n-H_{n-1-J}\le H_n-H_{n-K_0-1}\). The upper bound has the law of a sum of \(K_0+1\) copies of \(D_1\), uniformly in \(n\). Since \(J\) is tight, \(H_n-H_{n-1-J}=O_{\Pr}(1)\). The pathwise identity from Step 2 implies \(T_n-H_n=O_{\Pr}(1)\), and so the same Gaussian limit holds for \(T_n\).

**5. Asymptotic independence.** Let \(\mathcal F_m=\sigma(\xi_1,\ldots,\xi_m)\) and \(J_m=-\min_{0\le t\le m}S_t\). For fixed \(m\) and any \(n>m\), the walk cannot reach level \(n\) before time \(m\). By the strong Markov property at time \(m\), conditionally on \(\mathcal F_m\), \(H_n=m+H'_{n-S_m}\), where the future hitting time is generated by independent increments. Since \(S_m\) is fixed under this conditioning, the ordinary i.i.d. first-passage CLT shows that the normalized \(H_n\) tends to a standard normal *independently of* \(\mathcal F_m\), and hence independently of \(J_m\). As \(m\to\infty\), \(J_m\to J\) almost surely, while the bounded test-function error in replacing \(J\) by \(J_m\) vanishes by bounded convergence. Consequently the joint limit of normalized \(H_n\) and \(J\) has the product normal–geometric law. Replacing \(H_n\) by \(T_n\) changes the first coordinate by a term tending to zero in probability, and replacing \(J\) by \(n-1-L_n\) changes the second only on an event whose probability tends to zero. This proves the stated joint convergence.

## Verification
The standalone `verify.py` performs exact-fraction dynamic programming of first-discovery directions on small biased cycles and checks the known finite geometric last-vertex formula. It also checks the range-cover correspondence exhaustively across all short increment sequences and directly replays the eventual pathwise identity on seeded long trajectories. Run `python3 verify.py` from this directory. The recorded test run passed **26,859 assertions**. These finite checks verify definitions and algebra; the infinite pathwise assertion, limiting independence, and CLT follow from the analytical steps above rather than enumeration.

## Relationship to prior work
Idnani and Salem (2026, arXiv:2610.15115v1, Sections 3–4) establish interval-expansion representations and the *finite-cycle marginal law* of the final vertex, including its geometric concentration with fixed bias. The present finding does **not** claim that known geometric marginal. Instead it establishes the coupled, eventual **sample-path equality across all sufficiently large cycles** and the independent joint Gaussian–geometric limit of the final location and cover time. The source discusses cover-time distributions and large-ring terminal concentration as open directions, but does not provide this joint limit or coupling. The range/hitting-time reduction uses classical first-passage theory; see Feller and the Aldous–Fill cover-time treatment. Lovász and Winkler (1993) treat the uniform-last-vertex characterization and do not, from the accessible abstract, settle the present biased joint law. A 2021 mathematical discussion of unbiased cycle conditional cover times addresses a different zero-drift problem. These distinctions are statements of what was materially inspected, not a claim that all older literature has been exhaustively excluded.

## Limitations
The result assumes a **fixed, strictly positive drift**; it does not control the critical regime \(p\downarrow1/2\) jointly with increasing cycle size. It does not provide a finite-\(n\) rate of convergence in total variation, nor a local central limit theorem, nor the full cover-time distribution. The eventual coupling is with the same infinite increment sequence across cycles; independent cycle samples would not exhibit pathwise stabilization. Normal and geometric components are independent only **in the limiting joint law**, not for finite \(n\). Historical priority for differently phrased biased range-cover limits remains a residual risk.

## References
- K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115v1, first publicly posted 2026-10-10, https://arxiv.org/abs/2610.15115 .
- L. Lovász and P. Winkler, *A note on the last new vertex visited by a random walk*, Journal of Graph Theory 17 (1993), 593–596, https://doi.org/10.1002/jgt.3190170505 .
- D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6 (2002 manuscript), https://www.stat.berkeley.edu/~aldous/RWG/book.html .
- W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. I, gambler's ruin and random-walk first-passage chapters.
