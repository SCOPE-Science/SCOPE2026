# Parity-sharp fastest mixing on Möbius ladders

## Finding

For every integer \(n\ge4\), let the Möbius ladder \(M_{2n}\) have vertex set \(\mathbb Z/(2n)\mathbb Z\), cycle edges \(\{i,i+1\}\), and antipodal matching edges \(\{i,i+n\}\), with indices taken modulo \(2n\). Among **all** symmetric nonnegative row-stochastic matrices supported on these edges and the diagonal, the minimum second-largest eigenvalue modulus (SLEM) has the following exact answer.

Put
\[
 u_n=1-\cos(\pi/n),\quad v_n=1-\cos(2\pi/n),\qquad
 w_n=\begin{cases}2,&n\text{ odd},\\2-u_n,&n\text{ even},\end{cases}
 \qquad d_n=2v_n+w_n-u_n.
\]
There is a dihedrally invariant fastest-mixing matrix with probability \(a_n=1/d_n\) on each cycle edge and \(b_n=(v_n-u_n)/d_n\) on each antipodal edge, and holding probability \((v_n+w_n-2)/d_n\) at every vertex. Its globally minimal SLEM is
\[
\boxed{\mu_n^*=\frac{w_n-u_n}{2v_n+w_n-u_n}.}
\]
This is the **unique** optimizer among matrices invariant under rotations and reflections. No claim of uniqueness among arbitrary non-invariant optimizers is made. The positive edge probabilities and holding probabilities are well-defined for every \(n\ge4\).

The standard maximum-degree and uniform-stationary Metropolis choices both assign probability \(1/3\) to all three edges at each vertex. If \(n\) is odd, this chain is bipartite and has SLEM \(1\), while the optimized SLEM is strictly below \(1\). If \(n\) is even, the standard chain has
\[
\mu_n^{\rm heur}=1-\frac{2u_n}{3},\qquad
\frac{1-\mu_n^*}{1-\mu_n^{\rm heur}}
=\frac{3v_n}{2u_n(1+v_n-u_n)}\longrightarrow 6
\quad(n\to\infty\text{ through even integers}).
\]
For either parity, the optimal gap satisfies \(1-\mu_n^*\sim 2\pi^2/n^2\).

## Assumptions and scope

The feasible matrix \(P\) is real, symmetric, entrywise nonnegative and row-stochastic; \(P_{ij}=0\) off the diagonal unless the distinct vertices \(i,j\) form an edge of \(M_{2n}\). Holding probabilities are allowed. Every individual edge probability may be different. The objective is the spectral norm \(\mu(P)=\|P-J/(2n)\|_2\), with \(J\) the all-ones matrix. This equals the largest modulus of a nonstationary eigenvalue, including when the eigenvalue \(1\) has multiplicity greater than one. The theorem concerns discrete-time, uniform-stationary, reversible Markov chains, not nonreversible chains, arbitrary stationary masses, or mixing-time objectives other than SLEM. The case \(n=3\) is an already-known edge-transitive complete-bipartite case and is not asserted as new.

## Proof

**1. Global symmetry reduction.** Rotations and reflections of \(\mathbb Z/(2n)\mathbb Z\) preserve the graph. For every admissible \(P\), averaging conjugates of \(P\) under this finite dihedral group preserves feasibility and cannot increase \(\mu(P)=\|P-J/(2n)\|_2\), by convexity and conjugation invariance of the spectral norm. The averaged chain has the form
\[
 P(a,b)=(1-2a-b)I+a(S+S^{-1})+bS^n,
 \qquad a,b\ge0,\quad 2a+b\le1,
\]
where \(S\) denotes cyclic shift on \(2n\) coordinates. Thus minimizing over \(a,b\) yields the unrestricted global optimum (but does not establish unrestricted uniqueness).

**2. Exact spectral constraints.** The Fourier characters of the cycle diagonalize \(P(a,b)\); its eigenvalues, with \(j=0,\ldots,2n-1\), are
\[
 \lambda_j(a,b)=1-2a\bigl(1-\cos(\pi j/n)\bigr)
 -b\bigl(1-(-1)^j\bigr).
\]
The stationary eigenvalue is \(\lambda_0=1\). Write \(u=u_n\), \(v=v_n\), \(w=w_n\), \(d=d_n\). The two upper-mode constraints and one lower-mode constraint read
\[
 \mu\ge\lambda_1=1-2ua-2b,\quad
 \mu\ge\lambda_2=1-2va,\quad
 \mu\ge-\lambda_{j_-}=-1+2wa+2b,
\]
where \(j_-=n\) for odd \(n\) and \(j_-=n-1\) for even \(n\). (For even \(n\), the same lower eigenvalue also occurs at \(j=n+1\).)

**3. Sharp universal dual bound.** Multiply the first, second, and third inequalities by \(v/d\), \((w-u)/d\), and \(v/d\), respectively. They are strictly positive and sum to \(1\). Coefficients of both \(a\) and \(b\) cancel exactly, leaving
\[
 \mu(P(a,b))\ge\frac{w-u}{d}.
\]
The candidate \(a_*=1/d\), \(b_*=(v-u)/d\) makes the three constraints equalities: \(\lambda_1=\lambda_2=-\lambda_{j_-}=(w-u)/d\). Since \(v>u>0\) and \(w>u\), every dual multiplier is positive; equality in the weighted bound forces all three mode inequalities to be equalities. Solving the three linear equalities uniquely yields \(a_*,b_*\). This proves uniqueness among dihedrally invariant optimizers.

**4. Feasibility and control of all other modes.** Since \(v>u>0\), both edge probabilities are positive. Their holding probability is \(r_*=(v+w-2)/d\), equal to \(v/d>0\) for odd \(n\), and \((v-u)/d>0\) for even \(n\). The odd Fourier modes have \(s_j=1-\cos(\pi j/n)\) in \([u,w]\); their eigenvalues decrease linearly from \(\mu_*\) to \(-\mu_*\), so all satisfy the SLEM bound. Even nonstationary Fourier modes have \(s_j\) in \([v,z]\), where \(z=2-u\) for odd \(n\) and \(z=2\) for even \(n\). Their eigenvalues decrease from \(\mu_*\). The remaining lower endpoint obeys
\[
 \lambda_{\mathrm{even,min}}+\mu_*=
 \begin{cases}2v/d>0,&n\text{ odd},\\2(v-2u)/d>0,&n\text{ even}.
 \end{cases}
\]
In the even case, \(v=4u-2u^2\) and \(0<u<1\), whence \(v-2u=2u(1-u)>0\). Consequently every nonstationary eigenvalue lies in \([-\mu_*,\mu_*]\), and the dual lower bound is attained. The preceding reduction makes the value optimal over all possibly nonuniform admissible matrices.

**5. Comparison and asymptotics.** For the equal-probability chain \(a=b=1/3\), odd \(n\) has \(\lambda_n=-1\). For even \(n\), the extreme odd Fourier mode is \(-1+2u/3\), and all other nonstationary Fourier modes have modulus at most \(1-2u/3\). The even-mode upper extreme is \(1-2v/3\), and \(v>u\) gives the claimed heuristic SLEM. Finally \(u=\pi^2/(2n^2)+O(n^{-4})\) and \(v=2\pi^2/n^2+O(n^{-4})\), proving both the optimal-gap asymptotic and sixfold even-parity spectral-gap ratio.

## Verification

Run `python verify.py` with NumPy and SciPy installed (specific dependencies appear in `requirements.txt`). The program checks 98 successive graph sizes, compares 30 full dense spectra with their Fourier descriptions and independent two-variable linear programs, checks the dual inequality against 980 deterministic feasible chains, verifies 78 parity-sensitive heuristic spectra, and checks exact small cases and the asymptotic ratio. Its output is recorded in `verification_output.txt`. These numerical tests corroborate the fully quantified proof above; none are used as a substitute for the inequalities for all \(n\ge4\).

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduced the global symmetric fastest-mixing Markov-chain convex program, including the same SLEM normalization. Boyd, Diaconis, Parrilo and Xiao (2009) established symmetry averaging and Fourier/orbit reductions and explicitly solved cycles, hypercubes, a Cartesian torus mesh, complete bipartite graphs and wheels. Their edge-transitive formula covers the degenerate \(n=3\) Möbius ladder (isomorphic to \(K_{3,3}\)), not the graph family \(n\ge4\) with its two edge types. Their Cartesian-product formulas concern different graphs: the prism \(C_n\square K_2\) has the opposite bipartiteness parity to \(M_{2n}\), and therefore is not the latter graph. The relevant accessible full-text example and theorem sections do not state the present all-size parity-dependent optimum or its dual certificate. The 2005 symmetry-analysis paper develops orbit and eigenvalue tools, not this network-specific classification. The present result is an explicit solution using, but not reproducing, those general methods.

## Limitations

This is a self-review, not independently audited, mathematical result. Novelty is assessed from searched mathematical records and inspected accessible primary texts, not exhaustively certified. The two-edge-type invariant optimum is unique, but uniqueness of arbitrary optimal matrices is not established. SLEM is a spectral convergence surrogate and is not identical to optimizing total-variation mixing time at every time scale. The 2003 technical-report existence is documented in archival bibliographic listings but its precise day of initial public release was not verified; the date in metadata is the earliest source-day verified for the underlying published framework (the 2004 electronically released article). No claim is made about other graph families, nonuniform equilibrium masses, or nonreversible chains.

## References

1. S. Boyd, P. Diaconis, L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46(4) (2004), 667–689, doi:10.1137/S0036144503423264; publicly released electronically 2004-10-29; freely accessible author manuscript: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, “Symmetry Analysis of Reversible Markov Chains,” *Internet Mathematics* 2(1) (2005), 31–71, doi:10.1080/15427951.2005.10129100; freely accessible author preprint: https://web.stanford.edu/~boyd/papers/pdf/symmetry_analysis.pdf.
3. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM Journal on Optimization* 20(2) (2009), 792–819, doi:10.1137/070689413, arXiv:0709.0955v1 (2007-09-06); freely accessible paper: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
