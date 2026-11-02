# Exact multisink capture law on balanced block-design incidence networks

## Finding

Let a nontrivial balanced incomplete block design have \(v\) points and \(b\) blocks, with every block containing \(k\) points, every point lying in \(\rho\) blocks, and every pair of points lying together in \(\lambda\) blocks. Assume \(2\le k<v\), \(\lambda\ge1\), and let \(\delta=\rho-\lambda>0\). On its bipartite point-block incidence graph, choose any set \(S\) of \(t\) distinct point-side absorbing vertices, with \(3\le t\le v-1\); write \(s=v-t\).

For uniform positive coherent hopping and arbitrary strictly positive site-dependent absorption rates, the eventual capture probability from a point vertex \(x\) is

\[
\eta(x)=\begin{cases}1,&x\in S,\\ 1/s,&x\notin S.\end{cases}
\]

For a block vertex \(L\), put \(u_L=|L\setminus S|\), the number of unabsorbing points incident to that block. The exact probability is

\[
\boxed{\eta(L)=\frac vb-\frac{u_L(s-u_L)}{s(\rho-\lambda)}.}
\]

The minimal adjacency-invariant capturing subspace has dimension \(2(t+1)\), so the maximally mixed initial state on all \(v+b\) vertices has capture efficiency

\[
\boxed{\eta_{\mathrm{mixed}}=\frac{2(t+1)}{v+b}.}
\]

These laws do not depend on which absorbing points were selected except through the local intersection number \(u_L\), and do not depend on the magnitudes of the positive absorption rates. In a nonsymmetric design, \(b>v\), **no block vertex can be captured with certainty**, because \(\eta(L)\le v/b<1\). In a symmetric design, \(b=v\), a block vertex has certain capture exactly when \(u_L=0\) or \(u_L=s\).

A geometric distinction occurs even when the average is fixed. In the Fano plane, with any three marked points, the mixed capture efficiency is \(4/7\). If the points are collinear, the seven block vertices have capture values \(1\) once and \(1/2\) six times. If they are noncollinear, the block vertices have capture values \(5/8\) four times and \(1/2\) three times, with no perfectly captured block. The four unmarked point vertices always have probability \(1/4\).

## Assumptions and scope

The design is a finite \(2\)-\((v,k,\lambda)\) incidence structure, allowing the standard block-design interpretation with \(b\) labeled blocks. Its replication number is \(\rho=\lambda(v-1)/(k-1)\), and the usual incidence counting relation is \(bk=v\rho\). Write \(B\in\{0,1\}^{v\times b}\) for the point-by-block incidence matrix. The Hilbert space is \(\mathbb C^v\oplus\mathbb C^b\), with real symmetric hopping adjacency

\[
A=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}.
\]

For any real \(J>0\) and every choice of \(\gamma_x>0\) on \(x\in S\), the non-Hermitian effective Hamiltonian is

\[
H_{\mathrm{eff}}=JA-\frac{i}{2}\sum_{x\in S}\gamma_x|x\rangle\langle x|.
\]

For each basis state \(|z\rangle\), define eventual absorption by \(\eta(z)=1-\lim_{T\to\infty}\|e^{-iTH_{\mathrm{eff}}}|z\rangle\|^2\). A maximally mixed initial state is \(I_{v+b}/(v+b)\). These definitions concern one coherent excitation, without environmental dephasing or other loss channels.

## Proof

**1. Incidence algebra and active subspace.** Counting the common blocks containing one or two points gives the exact matrix identity

\[
BB^{\mathsf T}=(\rho-\lambda)I_v+\lambda\mathbf1_v\mathbf1_v^{\mathsf T}=\delta I_v+\lambda\mathbf1_v\mathbf1_v^{\mathsf T}.
\]

Since \(\delta>0\), \(B\) has full row rank. For \(S\) as above, define \(W=\operatorname{span}\{\mathbf1_v,e_x:x\in S\}\). The vectors are independent, so \(\dim W=t+1\). As \(t\ge1\), the adjacency orbit of any selected \(e_x\) contains \(\mathbf1_v\), because \(BB^{\mathsf T}e_x=\delta e_x+\lambda\mathbf1_v\) and \(\lambda>0\). Repeated applications of \(A\) therefore generate precisely

\[
\mathcal K=(W\oplus0)\oplus(0\oplus B^{\mathsf T}W).
\]

Indeed \(A(W\oplus0)\subseteq0\oplus B^{\mathsf T}W\) and \(A(0\oplus B^{\mathsf T}W)\subseteq W\oplus0\), by the incidence identity. The full row rank of \(B\) shows \(\dim B^{\mathsf T}W=t+1\). Thus \(\dim\mathcal K=2(t+1)\).

**2. Capture is orthogonal projection.** The orthogonal complement \(\mathcal K^\perp\) is invariant under \(A\), and every absorbing coordinate vanishes on it. Evolution there is unitary. On \(\mathcal K\) the generator \(-iH_{\mathrm{eff}}\) is dissipative. If it had an eigenvector with nonnegative real generator eigenvalue, taking the real part of its norm identity would force all marked coordinates to vanish. The eigenvector would then be an eigenvector of \(A\) orthogonal to every \(e_x\), \(x\in S\), hence to every \(A^j e_x\); this contradicts its membership in \(\mathcal K\). Thus every eigenvalue on \(\mathcal K\) has strictly negative real part, and the restricted evolution decays to zero. For any initial state \(\psi\), eventual capture is exactly \(\|P_{\mathcal K}\psi\|^2\).

**3. Point probabilities.** The point-side part of \(P_{\mathcal K}\) is \(P_W\). The orthogonal complement \(W^\perp\) consists of vectors supported on the \(s\) unmarked points and summing to zero. Consequently \(P_W\) fixes every marked coordinate and acts on the unmarked coordinates by averaging. Its diagonal is \(1\) at marked points and \(1/s\) elsewhere.

**4. Block probabilities.** Since \(B\) has row rank \(v\), the block space splits orthogonally into \(\ker B\), \(B^{\mathsf T}W^\perp\), and \(B^{\mathsf T}W\). Orthogonality of the two latter spaces follows from the incidence identity: for \(w\in W\), \(z\in W^\perp\),

\[
\langle B^{\mathsf T}w,B^{\mathsf T}z\rangle=w^{\mathsf T}(\delta I+\lambda\mathbf1\mathbf1^{\mathsf T})z=0.
\]

Also \(\|B^{\mathsf T}z\|^2=\delta\|z\|^2\) for \(z\in W^\perp\). Let \(c_L=Be_L\) be a block's incidence indicator. Its orthogonal projection onto \(W^\perp\) is the centered indicator of the \(u_L\) unmarked points in \(L\), and therefore

\[
\bigl\|P_{W^\perp}c_L\bigr\|^2=\frac{u_L(s-u_L)}s.
\]

It follows that the projection of \(e_L\) onto \(B^{\mathsf T}W^\perp\) has squared norm \(u_L(s-u_L)/(s\delta)\). The projection onto the full row space \(\operatorname{im}B^{\mathsf T}\) has constant squared norm \(v/b\) on every block basis vector. To see this directly, since \(BB^{\mathsf T}\) has eigenvalues \(\rho k\) on constants and \(\delta\) on their orthogonal complement,

\[
\begin{aligned}
\langle e_L,P_{\operatorname{im}B^{\mathsf T}}e_L\rangle
&=c_L^{\mathsf T}(BB^{\mathsf T})^{-1}c_L\\
&=\frac{k^2}{v\rho k}+\frac{k-k^2/v}{\delta}=\frac vb,
\end{aligned}
\]

where the last identity uses \(bk=v\rho\) and \(\lambda(v-1)=\rho(k-1)\). Subtracting the \(W^\perp\) contribution from this row-space leverage gives the asserted block formula.

**5. Mixed state and perfect capture.** Since the full projector has rank \(2(t+1)\), its trace divided by \(v+b\) gives \(\eta_{\mathrm{mixed}}\). Fisher's inequality gives \(b\ge v\). For \(b>v\), the nonnegative variance correction makes every block probability strictly below one. For \(b=v\), equality occurs if and only if \(u_L(s-u_L)=0\), namely \(u_L\in\{0,s\}\). This proves all claims.

## Verification

The accompanying `proof/verify_general.py` checks the design identities, the invariant-subspace closure, exact rational projection diagonals, independently computed numerical QR projectors and non-Hermitian dissipative time evolution. Seven nonisomorphic or parameter-distinct design examples are exercised, including symmetric projective designs and nonsymmetric affine and triple-system designs. The recorded run checked **244 subsets** of at least three absorbing points, **6,936 site capture probabilities**, **150 exact symbolic projector cases**, and **20 direct dissipative survival cases**; maximum numerical projector error was \(1.110\times10^{-15}\). The exact infinite-family statement is proved above, not inferred from testing.

Reproduce from the package root using `python -m pip install -r proof/requirements.txt` and then `python proof/verify_general.py`. Expected output is embedded in `proof/verification_general_output.txt`. The implementation checks finite representatives; no exhaustive census of all block designs is claimed.

## Relationship to prior work

Novo, Chakraborty, Mohseni, Neven and Omar (arXiv:1412.7209; first public version 2014-12-22) developed invariant-subspace reduction for continuous-time quantum search and transport, including single-site trapping; the Krylov and transport principles used above are not new. Razzoli, Paris and Bordone (arXiv:2011.13794) analyze site-specific efficiency and related spectral methods for a single trap, rather than the present multi-point design classification.

Lugão and Portugal (arXiv:2310.14141, first public 2023-10-22) explicitly give the adjacency eigenprojectors of symmetric designs and analyze **multiple marked vertices** for Hermitian spatial search. This is the closest design-specific antecedent. Their calculation concerns optimal search time and coherent marked-state success, not irreversible capture; it does not give the nonsymmetric incidence-design point/block absorption law, the \(2(t+1)\) bright dimension, or the block-side \(v/b\) perfect-capture obstruction. In particular, the spectral decomposition of symmetric designs is known and is not claimed as original. Previously investigated two-absorber finite-plane cases are not the novelty claim; the present classification assumes at least three point absorbers and includes every balanced \(2\)-design, with or without \(b=v\).

## Limitations

The absorbers occupy only the point part and number at least three and at most one fewer than all points. Absorption rates must be strictly positive, and coherent hopping must be uniform. The model excludes traps on the block part, dephasing, discrete-time or coined walks, finite-time capture rates, and non-balanced incidence structures. The result is a self-review, not an independent audit; exact historical priority remains subject to specialized literature beyond the inspected sources.

## References

1. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (2014). https://arxiv.org/abs/1412.7209
2. P. H. G. Lugão and R. Portugal, *Quantum search by continuous-time quantum walk on t-designs*, arXiv:2310.14141 (2023). https://arxiv.org/abs/2310.14141
3. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794 (2020). https://arxiv.org/abs/2011.13794
