# Parity-separated metastable energy spectra of Möbius and periodic Ising ladders

## Finding
For every integer \(n\ge3\), let \(M_{2n}\) be the Möbius ladder obtained from the cycle on \(2n\) vertices by joining antipodal pairs, and let \(P_n=C_n\square K_2\) be the circular two-leg ladder. For the antiferromagnetic Ising Hamiltonian \(H_G(\sigma)=J\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v\), with \(J>0\), call a configuration *blocked* when no single spin flip strictly lowers \(H_G\). Define \(K_G(\sigma)=\#\{\{u,v\}\in E(G):\sigma_u=\sigma_v\}\), and the complete blocked-state energy polynomial \(Z_G(z)=\sum_{\sigma\ \mathrm{blocked}} z^{K_G(\sigma)}\).

Set \(C_n(w)=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n}{n-j}\binom{n-j}{j}w^j\). The exact two-boundary classification is
\[
 Z_{P_n}(z)=C_n(z^2)+(-1)^nC_n(-z^2)+(1+(-1)^n)z^n,\qquad
 Z_{M_{2n}}(z)=C_n(z^2)-(-1)^nC_n(-z^2)+(1+(-1)^n)z^n.
\]
For odd \(n\), the energy supports are strictly disjoint: the possible numbers of aligned edges are \(2\pmod4\) in \(P_n\) and \(0\pmod4\) in \(M_{2n}\). For even \(n\), the two supports intersect in at most the single value \(K=n\), because the respective regular families have opposite congruences modulo four and only the two exceptional configurations contribute an opposite-sector term \(2z^n\). Consequently, if \(\mu_n^P,\mu_n^M\) are the normalized distributions of \(K\) on uniformly sampled blocked configurations, then \(\|\mu_n^P-\mu_n^M\|_{\mathrm{TV}}=1\) for odd \(n\), while for even \(n\), \(\|\mu_n^P-\mu_n^M\|_{\mathrm{TV}}\ge1-2/\min(Z_{P_n}(1),Z_{M_{2n}}(1))\). In particular the distance tends to one exponentially quickly.

Despite this near-disjoint energy support, both models have exactly the same limiting blocked-state entropy per spin, \(\frac12\log\varphi\), and the same limiting number of aligned bonds per rung, \(1-1/\sqrt5\), where \(\varphi=(1+\sqrt5)/2\). The asymptotic variance of aligned bonds divided by \(n\) is \(4\sqrt5/25\) in both models. The two unweighted counts are \(Z_{P_n}(1)=L_n+1+(-1)^n+2\cos(2\pi n/3)\) and \(Z_{M_{2n}}(1)=L_n+1+(-1)^n-2\cos(2\pi n/3)\), where \(L_n=\varphi^n+(1-\varphi)^n\) is the Lucas number.

## Assumptions and scope
The graphs are simple and cubic for \(n\ge3\). Their vertices are individually labeled and the global spin reversal is counted as a distinct configuration. The antiferromagnetic exchange \(J\) is spatially uniform and strictly positive; there are no external fields. A tie in spin-flip energy counts as blocked, but in these cubic graphs a flip cannot have zero energy change. The polynomial variable \(z\) is formal (or any positive real evaluation). There are exactly \(3n\) edges, and the physical energy is \(H_G=J(2K_G-3n)\). The probability statements concern the *uniform measure on all blocked configurations*, not a claim about dynamical basin sizes.

## Proof
**Local criterion.** If a vertex has \(a\) equally oriented neighbors among its three neighbors, flipping it changes the energy by \(\Delta H=2J(3-2a)\). Hence \(\Delta H>0\) exactly when \(a\le1\). Thus a configuration is blocked if and only if its aligned-edge subgraph is a matching. The criterion is independent of \(J\).

**Common transfer operator.** Order the rung states as the four pairs \((\pm1,\pm1)\). A transfer state is an ordered pair \((a,b)\) of consecutive rung states, hence one of \(16\) possibilities. Define \(T(z)_{(a,b),(b',c)}=0\) unless \(b=b'\). If \(b=b'\), retain the transition exactly when both vertices of rung \(b\) have at most one equal neighbor among their preceding leg neighbor in \(a\), following leg neighbor in \(c\), and vertical rung partner in \(b\). For retained transitions set
\[
T(z)_{(a,b),(b,c)}=z^{\mathbf1_{b_0=c_0}+\mathbf1_{b_1=c_1}+\mathbf1_{b_0=b_1}}.
\]
Every vertical bond and every forward leg bond is then counted precisely once. Let \(Q\) swap the two rows simultaneously in both rung states of an ordered pair: \(Q(a,b)=(\bar a,\bar b)\), with \(\bar a=(a_1,a_0)\). The uniform interaction makes \(TQ=QT\). Tracing an \(n\)-step transfer loop counts \(P_n\) configurations, whereas tracing after a row-exchange closure counts precisely the twisted cycles of \(M_{2n}\):
\[
 Z_{P_n}(z)=\operatorname{tr}(T(z)^n),\qquad Z_{M_{2n}}(z)=\operatorname{tr}(T(z)^nQ).
\]
The transfer correspondence remains valid at \(n=3\), where the cyclic legs are triangles and no edges are repeated.

**Finite symbolic calculation.** The involution \(Q\) has symmetric and antisymmetric invariant subspaces of dimensions \(10\) and \(6\). Form bases from the row-swap orbits, with vectors \(e_i+e_{Qi}\) and \(e_i-e_{Qi}\), respectively, taking one basis vector per orbit (and retaining fixed-point basis vectors only in the symmetric sector). Substitution into the displayed \(16\)-state definition, followed by ordinary finite row reduction, gives the exact polynomial identities
\[
 \det(tI-T|_{Q=+1})=t^6(t^2-z^2)(t^2-t-z^2),\qquad
 \det(tI-T|_{Q=-1})=t^4(t^2+t+z^2).
\]
This is an identity of integer polynomials in \(t,z\), not a numerical extrapolation. The included standalone code constructs the explicitly defined matrices and repeats both symbolic factorizations exactly.

**All-size trace formula.** The two nonzero eigenvalues of the first quadratic sum to one and have product \(-z^2\), so the sum of their \(n\)th powers is \(C_n(z^2)\): it equals two at index zero, one at index one, and obeys \(R_n=R_{n-1}+z^2R_{n-2}\). The two roots of the second quadratic sum to minus one and have product \(z^2\); their power sum is \((-1)^nC_n(-z^2)\). The remaining nonzero eigenvalues in the symmetric sector are \(z\) and \(-z\). Taking the sum and difference of the two sector traces proves both displayed energy polynomials for all \(n\ge3\), including possible non-diagonalizable values of \(z\), since traces of matrix powers are always sums of eigenvalue powers with algebraic multiplicities.

**Parity and separation.** In \(C_n(z^2)\pm C_n(-z^2)\), the coefficients with odd or even index \(j\), respectively, cancel. Thus the regular energy supports belong to complementary residue classes modulo four, with at most the shared monomial \(2z^n\) at even \(n\). For odd \(n\), no exceptional monomial appears and the supports are disjoint. For even \(n\), exactly one graph gets \(2z^n\) outside its regular residue class, so their common energy mass is at most \(2\) raw configurations in that graph; normalization gives the total-variation lower bound.

**Thermodynamic formulas.** The dominant eigenvalue of the transfer operator for every real \(z>0\) is \(\lambda(z)=(1+\sqrt{1+4z^2})/2\). All other contributing eigenvalues have strictly smaller modulus, uniformly on a sufficiently small complex neighborhood of \(z=1\). Therefore \(\log Z_G(z)=n\log\lambda(z)+O(1)\) with exponentially small relative correction for both graph families, locally analytically around one. It follows by evaluating and differentiating \(z\partial_z\log Z_G\) at \(z=1\) that \(n^{-1}\mathbb E K\to1-1/\sqrt5\) and \(n^{-1}\operatorname{Var}K\to4\sqrt5/25\). Since \(\lambda(1)=\varphi\), division by the \(2n\) spins gives entropy \(\frac12\log\varphi\). At \(z=1\), \((-1)^nC_n(-1)=2\cos(2\pi n/3)\), proving the unweighted formulas and their exponential growth.

## Verification
The supplied `verify.py` constructs \(T\) and \(Q\) from the independent local criteria and verifies the two invariant-sector characteristic polynomials *symbolically* over \(\mathbb Z[z,t]\). It independently enumerates all \(2^{2n}\) labeled spin assignments for each \(3\le n\le9\) on both graphs, checks stability directly from their adjacency lists, counts aligned edges directly, and matches the resulting energy polynomials to both transfer traces and the two closed forms. Execution succeeded. The finite enumeration is a diagnostic; the identity for all \(n\) follows from the symbolic determinant and trace argument above.

## Relationship to prior work
Spirin, Krapivsky and Redner (2001) study freezing and local spin-flip metastability in homogeneous ferromagnetic lattices; their full introduction/model discussion motivated the local-energy question but neither the antiferromagnetic Möbius topology nor its energy-resolved polynomial appears in those portions. Kalinin and Berloff (2022) analyze the same Möbius-ladder antiferromagnetic graph as a benchmark for global Ising minimization. Their full discussion supplies the ground-state energy and degeneracy (including \(2n\) ground states at even \(n\)), which is **prior work** and is recovered here as the lowest-degree coefficient; it does not imply the complete blocked-state generating polynomials or energy-support separation. Masui, Southern and Jacobs (1989) study recursive metastable-state enumeration on random spin-glass and ferromagnetic strips; only the abstract was accessible, so possible stronger coverage in their full text remains a bibliographic risk. The ordinary periodic ladder at even \(n\) is bipartite, so its antiferromagnetic blocked-state polynomial is gauge-equivalent to an existing ferromagnetic periodic-ladder classification; that portion is a baseline and is **not** claimed as independently new. The general locally maximal-cut/defect-matching reformulation is standard. The new contribution asserted here is the complete *Möbius-twisted* energy polynomial and its all-size comparison with the ordinary closure, especially the asymptotic separation of the two energy distributions; the periodic-even baseline alone does not imply a twisted-sector trace.

## Limitations
No rate of actual zero-temperature Glauber convergence, dynamical basin probability, activation barrier, or finite-temperature equilibrium theorem is claimed. The exact results require uniform antiferromagnetic interactions and the specified cubic graph families. Full-text inspection of one potentially relevant older metastability paper was unavailable; equivalence to an overlooked result is a residual originality risk. External independent validation has not been performed.

## References
1. V. Spirin, P. L. Krapivsky and S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037v1, first publicly posted 2001-05-02, https://arxiv.org/abs/cond-mat/0105037.
2. K. P. Kalinin and N. G. Berloff, *Computational complexity continuum within Ising formulation of NP problems*, Communications Physics **5** (2022), 20, DOI:10.1038/s42005-021-00792-0, https://www.nature.com/articles/s42005-021-00792-0.
3. S. Masui, B. W. Southern and A. E. Jacobs, *Metastable states of Ising spin glasses and random ferromagnets*, Physical Review B **39** (1989), 6925–6933, DOI:10.1103/PhysRevB.39.6925; abstract checked, full text not inspected.
