# Exact speed-resonance reaction laws for two quantum walkers on a star

## Finding

Let \(L\ge3\) be an integer. Two distinguishable single-particle quantum walkers hop on the star \(K_{1,L}\) with nonzero positive hopping amplitudes \(a\) and \(b\). Reaction irreversibly removes a pair at any coincidence vertex, with independent strictly positive reaction rates. If \(\mathcal B\) is the subspace visible to reaction, then

\[
\dim\mathcal B=\begin{cases}3L+1,&a=b,\\5L,&a\ne b.\end{cases}
\]

For a localized initial configuration \(|x,y\rangle\), the eventual reaction probability \(C(x,y)\) has exactly three site classes:

\[
\begin{array}{c|cc}
\text{initial sites}&a=b&a\ne b\\\hline
x=y&1&1\\
\text{one hub, one leaf}&1/2&1\\
\text{two different leaves}&1/(L-1)&(2L-1)/(L(L-1)).
\end{array}
\]

The dark-space dimensions are, respectively, \(L^2-L\) and \(L^2-3L+1\). In particular, any unequal positive hopping strengths lead to certain eventual reaction when exactly one walker starts at the hub; equal strengths leave half of that initial norm permanently protected. All statements hold for any positive, site-dependent reaction rates.

## Assumptions and scope

The one-particle vertex basis is \(\{|c\rangle,|1\rangle,\ldots,|L\rangle\}\), where \(c\) is the hub. Define the star adjacency operator by \(A|c\rangle=\sum_{i=1}^L|i\rangle\) and \(A|i\rangle=|c\rangle\). On the ordered, distinguishable two-particle Hilbert space \(\mathscr H=\mathbb C^{L+1}\otimes\mathbb C^{L+1}\), set

\[
H=aA\otimes I+bI\otimes A,\qquad
K=\tfrac12\sum_{v\in\{c,1,\ldots,L\}}\gamma_v|v,v\rangle\langle v,v|,
\]

with \(a,b,\gamma_v>0\). The non-Hermitian no-reaction evolution is \(\psi(t)=\exp[(-iH-K)t]\psi(0)\). Define \(C(\psi)=1-\lim_{t\to\infty}\|\psi(t)\|^2\) for a normalized pure initial state; by linearity the same definition extends to density matrices. No exchange symmetry, external dephasing, disorder, finite-time cutoff or interaction other than the loss is assumed. The theorem is about the \(t\to\infty\) limit, not a uniform-in-time estimate.

## Proof

**1. The asymptotic reaction projector.** For any finite Hermitian \(H\) and nonnegative \(K\), differentiation gives \(d\|\psi(t)\|^2/dt=-2\langle\psi(t),K\psi(t)\rangle\le0\). An eigenvector of \(-iH-K\) with purely imaginary eigenvalue must lie in \(\ker K\), by taking its real quadratic form, and hence is an eigenvector of \(H\). The semigroup is contractive, so a nontrivial Jordan block on the imaginary axis is impossible. The maximal nondecaying invariant subspace is therefore

\[
\mathcal D=\bigoplus_{\lambda\in\operatorname{spec}(H)}
\big(\operatorname{ran}P_\lambda\cap\ker K\big),
\]

where \(P_\lambda\) are orthogonal spectral projections. Its orthogonal complement \(\mathcal B\) is exactly the span of \(P_\lambda|v,v\rangle\) over all vertices \(v\) and distinct eigenvalues \(\lambda\). Thus \(C(\psi)=\langle\psi,\Pi_\mathcal B\psi\rangle\), and changing the positive \(\gamma_v\) cannot change any answer.

**2. Single-star decomposition.** Let \(|s\rangle=L^{-1/2}\sum_{i=1}^L|i\rangle\), \(B=\operatorname{span}\{|c\rangle,|s\rangle\}\), and \(W=\{\sum_i z_i|i\rangle:\sum_i z_i=0\}\), of dimension \(L-1\). The normalized vectors \(|\pm\rangle=(|c\rangle\pm|s\rangle)/\sqrt2\) have one-body energies \(\pm\sqrt L\), while \(A|_W=0\). In the two-walker decomposition \((B\oplus W)\otimes(B\oplus W)\), the energies on \(B\otimes B\) are \(\sqrt L(\pm a\pm b)\), on \(B\otimes W\) they are \(\pm a\sqrt L\), on \(W\otimes B\) they are \(\pm b\sqrt L\), and on \(W\otimes W\) they are zero.

**3. Coincidence images on the leaf-zero sector.** Write \(w_i=|i\rangle-|s\rangle/\sqrt L\in W\). The zero-energy detector vectors in \(W\otimes W\) are \(d_i=w_i\otimes w_i\), with Gram matrix

\[
G_{ij}=\langle d_i,d_j\rangle=(\delta_{ij}-1/L)^2
=\frac{L-2}{L}\,\delta_{ij}+\frac1{L^2}.
\]

Its eigenvalues are \((L-1)/L\) on the all-ones direction and \((L-2)/L\) on its orthogonal complement, both positive since \(L\ge3\). Therefore precisely \(L\) directions in \(W\otimes W\) are detector-visible. For distinct leaves \(i\ne j\), put \(u_k=\langle d_k,w_i\otimes w_j\rangle=(\delta_{ki}-1/L)(\delta_{kj}-1/L)\). Direct calculation gives \(\sum_k u_k=-1/L\) and \(\|u\|^2=(2L-3)/L^3\), so the squared norm of the visible projection of \(w_i\otimes w_j\) is

\[
u^\top G^{-1}u=\frac{2L-1}{L^2(L-1)}.
\]

**4. Unequal hopping.** If \(a\ne b\), all four \(B\otimes B\) eigenvectors are individually visible, each of the four energy-sign sectors in \((B\otimes W)\oplus(W\otimes B)\) contributes \(L-1\) bright directions, and \(W\otimes W\) contributes \(L\). The total is \(4+4(L-1)+L=5L\). Exceptional coincidences at the positive ratios \(a/b=2\) or \(b/a=2\) do not reduce the rank: the images of \(B\otimes B\) in coincidence coordinates are constant over the leaves (with a possible hub entry), whereas the images of \(B\otimes W\) or \(W\otimes B\) are leaf-zero-sum vectors, so their images are orthogonal and ranks add. For a hub–leaf input, all of its \(B\otimes B\) and \(B\otimes W\) components are visible, giving \(C(c,i)=1\). For distinct leaves, the \(B\otimes B\), mixed, and \(W\otimes W\) contributions are respectively \(1/L^2\), \(2(L-1)/L^2\), and the quantity in step 3; their sum is \((2L-1)/(L(L-1))\).

**5. Equal hopping.** If \(a=b\), at energies \(\pm2a\sqrt L\) one bright direction remains in \(B\otimes B\) for each sign. The zero-energy \(B\otimes B\) eigenspace contains one visible vector \((|c,c\rangle-|s,s\rangle)/\sqrt2\) and one invisible antisymmetric vector \((|c,s\rangle-|s,c\rangle)/\sqrt2\). The detector at \((c,c)\) isolates that visible zero-energy \(B\otimes B\) direction, and the leaf detectors additionally generate all \(L\) bright \(W\otimes W\) directions. Each of the two energies \(\pm a\sqrt L\) combines \(B\otimes W\) and \(W\otimes B\): only their symmetric combinations are detector-visible, giving \(L-1\) directions per sign. The rank is consequently \(2+(1+L)+2(L-1)=3L+1\).

For a hub–leaf input, the \(B\otimes B\) and mixed contributions to capture are \(1/(2L)\) and \((L-1)/(2L)\), yielding \(1/2\). For distinct leaf inputs, the contributions are \(1/L^2\), \((L-2)/L^2\), and \((2L-1)/(L^2(L-1))\) from step 3, totaling \(1/(L-1)\). A coincident initial configuration lies directly in \(\mathcal B\), so its capture probability is one in both regimes. Subtracting the calculated ranks from \((L+1)^2\) gives the stated dark-space dimensions. This proves all cases.

## Verification

Run `python verify.py` with NumPy and SciPy as stated in `requirements.txt`. The standalone checker reconstructs the Hamiltonian and absorbing spectral projections independently by Hermitian diagonalization and singular-value decomposition, comparing dimensions, sitewise values and projector idempotence for \(3\le L\le7\), five hopping pairs per size including the ratios \(1:2\) and \(2:1\). It independently checks selected survival probabilities by evolving the non-Hermitian Hamiltonian with nonuniform positive loss rates. On the supplied package the checker reports `VERIFY_OK spectral_cases=25 sitewise_probabilities=950 projector_idempotence=25 loss_dynamics=12`. Numerical sampling and long but finite evolution do not establish the infinite-family theorem; the foregoing algebra is the proof.

## Relationship to prior work

Štefaňák, Kiss, Jex and Mohring study the meeting problem for coined discrete-time quantum walks on the infinite line, including distinguishability and quantum statistics; their meeting probability is evaluated at a specified time rather than by an irreversible complete coincidence sink on a finite star. Razzoli, Paris and Bordone develop the spectral/Krylov approach to irreversible transport and explicitly examine complete bipartite graphs including stars, but for one walker with one trapping vertex rather than two walkers with all coincidence configurations trapped. Qiang and collaborators experimentally demonstrate coherent multiparticle walks including a two-particle four-vertex star; they analyze unitary quantum correlations and search, not the present two-rate long-time reacting subspace. These works supply the physical and methodological setting; their general spectral framework does not itself tabulate the claim's evaluated star-specific formulas. A stronger or differently phrased unlocated result could nevertheless imply the formulas.

## Limitations

Distinguishable, noninteracting walkers and a complete set of diagonal reaction sites are essential hypotheses; no assertion is made for indistinguishable particles, missing reaction sites, graph perturbations, nonlinear interactions, or nonpositive rates. The discontinuity concerns limits of infinite-time capture and does not imply discontinuity at any finite time. Numerical verifier tolerances are solely corroborative. Publication priority requires independent examination of a broader literature than the sources specifically inspected here.

## References

1. M. Štefaňák, T. Kiss, I. Jex and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985v1, first posted 14 May 2007. https://arxiv.org/html/0705.1985v1
2. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794, first posted 27 November 2020; *Entropy* 23 (2021), 85. https://arxiv.org/html/2011.13794v2
3. X. Qiang et al., *Implementing graph-theoretic quantum algorithms on a silicon photonic quantum walk processor*, *Science Advances* 7 (2021), eabb8375, doi:10.1126/sciadv.abb8375. https://pmc.ncbi.nlm.nih.gov/articles/PMC7909884/
