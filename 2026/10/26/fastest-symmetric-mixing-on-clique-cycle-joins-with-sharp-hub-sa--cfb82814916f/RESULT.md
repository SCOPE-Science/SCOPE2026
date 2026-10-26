# Fastest symmetric mixing on clique-cycle joins with sharp hub saturation

## Finding

For every pair of integers \(r\ge2\) and \(n\ge4\), let \(G_{r,n}=K_r\vee C_n\) be the join of a clique of \(r\) hub vertices and a simple cycle of \(n\) peripheral vertices. Among all nonnegative symmetric stochastic transition matrices whose off-diagonal support is contained in \(G_{r,n}\), the minimum second-largest eigenvalue modulus (SLEM) has a closed form, as do all automorphism-invariant optimal matrices.

Define
\[
\ell_n=2(1-\cos(2\pi/n)),\qquad
u_n=2(1-\cos(2\pi\lfloor n/2\rfloor/n)),\qquad
q_n=\frac{\nu_n-\ell_n}{\nu_n+\ell_n}.
\]
Then \(0<q_n<1\). The unique optimal invariant probability on each hub-to-rim edge, the unique optimal invariant probability on each cycle edge, and the optimal SLEM are, respectively,
\[
 a_* = \min\left\{\frac1n,\frac{1+q_n}{n+r+r q_n}\right\},\qquad
 b_* = \frac{2(1-r a_*)}{\ell_n+\nu_n},\qquad
 \mu_* = q_n(1-r a_*).
\]
Every invariant optimal matrix has hub-clique edge probability \(c\) in precisely the closed interval
\[
\max\left\{0,\frac{1-n a_*-\mu_*}{r}\right\}
\ \le c\le\
\min\left\{\frac{1-n a_*}{r-1},\frac{1-n a_*+\mu_*}{r}\right\}.
\]
In particular, the spoke transition probability saturates the hub row budget, so that \(a_*=1/n\) and necessarily \(c=0\), exactly in the following regimes:
\[
\begin{cases}
n\ge 2r+2,&2\le r\le4,\\
n\ge 2r+1,&r\ge5.
\end{cases}
\]
Below these thresholds \(a_*<1/n\), and one optimal invariant chain has the strictly positive hub-clique probability \(c=(1-n a_*)/r\). There is no claim that all globally optimal matrices are invariant or unique.

## Assumptions and scope

The graph is finite, simple and unweighted, with \(r\ge2\) hub vertices forming a complete graph, a cycle on \(n\ge4\) vertices, and every hub joined to every cycle vertex. The transition matrix \(P\) is real, symmetric, entrywise nonnegative, stochastic (\(P\mathbf1=\mathbf1\)), and has zero off-diagonal entries at nonedges. Diagonal holding probabilities are allowed. The minimized objective is
\[
\mu(P)=\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{n+r}\right\|_2
=\max_{2\le j\le n+r}|\lambda_j(P)|.
\]
The eigenvalues are counted with multiplicity, with the unit stationary eigenvalue excluded. Graph-edge probabilities may be zero. The result is for the SLEM objective, not literal total-variation mixing time or a forced strictly-positive edge-support constraint.

## Proof

**1. Symmetry reduction without loss of global optimality.** Permute the \(r\) hubs and act dihedrally on the \(n\) rim vertices. The feasible set is convex and invariant under these permutations. The SLEM equals an operator norm after subtraction of the stationary projector and is convex. Hence the average of any globally optimal matrix under this group remains feasible and optimal. Thus a global optimum can be sought among three edge-orbit probabilities: \(a\) (each spoke), \(b\) (each rim edge), and \(c\) (each distinct hub pair). Their exact feasibility conditions are
\[
a,b,c\ge0,\qquad n a+(r-1)c\le1,\qquad r a+2b\le1.
\]
In particular, \(0\le a\le U=\min\{1/n,1/r\}\).

**2. Spectrum and reduction to one scalar.** Hub-contrast modes, the two class-constant modes, and nonconstant Fourier modes on the rim yield exactly the nonstationary eigenvalues
\[
1-na-rc\quad (r-1\text{ times}),\qquad
1-(n+r)a\quad (1\text{ time}),\qquad
1-r a-2b(1-\cos(2\pi j/n)),\quad 1\le j\le n-1.
\]
The cycle factors range between \(\ell_n\) and \(\nu_n\). Because \(1-ra\ge0\), the best possible maximum absolute rim eigenvalue at fixed \(a\) is
\[
\min_{b\ge0}\max\{|1-ra-\ell_n b|,|1-ra-\nu_n b|\}
=q_n(1-ra),
\]
with a unique minimizer \(b=2(1-ra)/(\ell_n+\nu_n)\). This choice is feasible: \(\ell_n+\nu_n>4\) for all \(n\ge4\). For even \(n\), \(\nu_n=4\); for odd \(n\), the sum is \(4+2(\cos(\pi/n)-\cos(2\pi/n))>4\).

At fixed \(a\), choose \(c=(1-na)/r\). This is feasible and sets the hub-contrast eigenvalue to zero. Therefore the unrestricted invariant optimization is exactly the one-variable minimization
\[
\min_{0\le a\le U}\max\{\,|1-(n+r)a|,\ q_n(1-ra)\,\}.
\]
The first term decreases to zero at \(a=1/(n+r)\), then increases; the second decreases strictly. Their unique post-zero intersection is \(a_0=(1+q_n)/(n+r+r q_n)\). Since \(a_0<1/r\), the minimizer is \(a_*=\min\{a_0,1/n\}\). At either kind of minimum, the rim bound is active, so \(b=b_*\) is necessary for every invariant optimum. The remaining hub mode has absolute value at most \(\mu_*\) precisely when \(|1-na_*-r c|\le\mu_*\), which combined with the hub-row budget gives the stated exact interval for \(c\).

**3. Exact integral saturation threshold.** The condition \(a_*=1/n\) is equivalent to
\[
q_n(n-r)\ge r.
\]
Writing \(s_n=\ell_n/\nu_n\), equivalently \(q_n=(1-s_n)/(1+s_n)\), this becomes
\[
n-2r\ge n s_n.
\]
The factor \(s_n\) is \(\sin^2(\pi/n)\) when \(n\) is even and \(4\sin^2(\pi/(2n))\) when \(n\) is odd. Thus \(0<s_n\le\pi^2/n^2\). If \(n\le2r\), saturation is impossible. If \(n\ge2r+2\), then \(n-2r\ge2>\pi^2/6\ge n s_n\) because \(n\ge6\). The only remaining possibility is \(n=2r+1\), for which saturation is equivalent to \(4n\sin^2(\pi/(2n))\le1\). For \(r\ge5\), \(n\ge11\) gives \(4n\sin^2(\pi/(2n))\le\pi^2/n<1\). For \(r=2,3,4\), i.e. \(n=5,7,9\), the strict reverse inequality follows from \(\sin t\ge t-t^3/6\) and the elementary bounds \(31/10<\pi<22/7\). For example, uniformly for these three \(n\),
\[
4n\sin^2(\pi/(2n))>
\frac{(31/10)^2}{n}\left(1-\frac{(11/(7n))^2}{6}\right)^2>1,
\]
where the last inequality can be verified directly at \(n=5,7,9\). This proves the stated thresholds with no integer equality cases at the boundary.

## Verification

The standalone program `verify.py` reconstructs each candidate matrix, checks stochasticity and eigenvalues, and compares its SLEM with an independently assembled linear program retaining every cycle Fourier mode. Running `python verify.py` with the versions specified in `requirements.txt` produced:

`VERIFY_OK phase_pairs=209 invariant_LP_comparisons=98 direct_full_spectra=50`

These are finite numerical cross-checks, not a substitute for the preceding proof. The infinite claim is established by exact spectral decomposition, elementary convexity, and trigonometric inequalities. The numerical program does not claim independent certification.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduced the symmetric fastest-mixing Markov-chain optimization and its convex semidefinite formulation. Boyd, Diaconis, Parrilo and Xiao (2009), Section 5.4.3, derive the *single-hub* wheel optimum \(K_1\vee C_n\), including Fourier block diagonalization and its optimal rim and spoke probabilities. Those statements and techniques are acknowledged, not claimed anew. The present conclusion treats \(r\ge2\) *mutually adjacent* hubs, which introduce an additional hub-contrast eigenmode and a distinct, sharp saturation boundary depending on \(r\). It does not follow by substituting \(r\) into the published single-hub wheel optimum: for example, \(K_2\vee C_4\) optimizes at \(a_*=1/5<1/4\), whereas the published single-hub wheel saturates its spoke budget. General SDP solvability does not by itself state the all-size closed form or the discrete transition. Targeted literature and mathematical-record searches found no dominating exact formula for these joins, but absence of a search hit is not a proof of novelty.

## Limitations

No uniqueness or classification is asserted for globally optimal *nonsymmetric* matrices; only the existence of a symmetric global optimizer and the complete set of invariant optimizers are proved. The result does not optimize nonuniform stationary laws, nonsymmetric chains, forced positive weights, continuous-time rates, or total-variation mixing time. Exact symbolic bounds prove the threshold, while numerical tests only sample finite parameter sets. Earlier related technical reports might contain variants under alternative graph names; independent external mathematical review has not been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: https://doi.org/10.1137/S0036144503423264 . Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, especially Section 5.4.3. arXiv version publicly dated 2007-09-06: https://arxiv.org/abs/0709.0955 . DOI: https://doi.org/10.1137/070689413 . Open full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf . An earlier technical-report listing has month-only evidence (May 2007).
