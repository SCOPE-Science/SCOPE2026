# Exact two-particle entanglement spectra on complete bipartite graphs

## Finding

Consider the indistinguishable-particle Grover walk on a finite complete bipartite graph, in the precise arc-Hilbert-space convention introduced by Kubota, Matsubara and Segawa [1]. For **every** pair of integers \(m,n\geq1\), either exchange sign, either initial edge, and every integer time \(t\geq0\), the complete particle-reduced entanglement spectrum is a duplicated tensor power of a single Bernoulli pair.

Set \(N=mn\),
\[
q=\frac{2\sqrt{(m-1)(n-1)}}{mn},\qquad
A=\frac{1+\sqrt{1-4q^2}}2,\qquad B=1-A,
\]
and set \(k_t=0,1,2,1\) as \(t\equiv0,1,2,3\pmod4\), respectively. The nonzero eigenvalues of the one-particle reduced density operator, with multiplicities, are exactly the positive entries of
\[
\left\{\frac12\prod_{j=1}^{k_t}c_{\epsilon_j}:
(\epsilon_1,\ldots,\epsilon_{k_t})\in\{0,1\}^{k_t}\right\},
\quad\text{each entry appearing twice},\qquad(c_0,c_1)=(A,B).
\]
The empty product is one; zero eigenvalues of the displayed multiset are removed. In particular the bosonic and fermionic states have **identical full reduced spectra**, not just identical entropies.

For every real \(\alpha>0\), \(\alpha\neq1\), the Rényi entropy is
\[
S_\alpha(t)=\log2+\frac{k_t}{1-\alpha}\log(A^\alpha+B^\alpha),
\]
where a vanishing Bernoulli component contributes zero. At \(\alpha=1\),
\[
S_1(t)=\log2+k_t[-A\log A-B\log B].
\]
The entanglement rank never exceeds eight, **independently of graph size**, and equals eight precisely at times \(t\equiv2\pmod4\) when \(m,n\geq2\). The universal von Neumann entropy ceiling is \(\log8\), attained precisely for \(K_{2,2}\) at times \(t\equiv2\pmod4\). If either part has size one, the spectrum is always \((1/2,1/2)\). As both part sizes diverge, \(S_1(t)\to\log2\) uniformly in \(t\); for balanced \(m=n=r\), the maximum time entropy satisfies
\[
\max_t S_1(t)=\log2+\frac{16\log r}{r^2}+O(r^{-2}).
\]

## Assumptions and scope

The graph is \(G=K_{m,n}\), with parts \(X=\{x_1,\ldots,x_m\}\) and \(Y=\{y_1,\ldots,y_n\}\). Its directed arcs are \(\mathcal A(G)\), and the one-particle Hilbert space is \(\mathcal H=\mathbb C^{\mathcal A(G)}\), of dimension \(2mn\). The two-particle walk is the ordinary arc-reversal Grover walk on the Kronecker-product graph \(G\otimes G\), transferred to \(\mathcal H\otimes\mathcal H\) by the canonical arc-tensor bijection [1, Section 3]. It is **not** the product of two independent single-particle Grover walks. The initial state associated with the edge \(a=(x_1,y_1)\) is
\[
\psi_0^{\sigma}=\frac{|a\rangle\otimes|a^{-1}\rangle+\sigma|a^{-1}\rangle\otimes|a\rangle}{\sqrt2},\quad\sigma\in\{+1,-1\}.
\]
All edges are equivalent by graph automorphism. Let \(\psi_t^\sigma=U^t\psi_0^\sigma\), and let \(\rho_t=\operatorname{Tr}_2|\psi_t^\sigma\rangle\langle\psi_t^\sigma|\), with the **particle-label partial trace** used in [1]. Entropy is in natural logarithms. No claim is made about a distinct operational identical-particle entanglement measure or a noisy/different quantum walk.

## Proof

**1. Four-step reduction.** In \(G\otimes G\), the connected component joining \(X\times Y\) to \(Y\times X\) is the balanced complete bipartite graph \(K_{N,N}\), even when \(m\neq n\). Both terms of the initial state belong to its directed-arc Hilbert space. On \(K_{N,N}\), the arc-reversal Grover operator maps an incoming amplitude row at each endpoint to its reflection about the uniform vector. After two steps the amplitude array transforms by two reflections \(R=2J_N/N-I_N\). Because \(R^2=I_N\), the walk has \(U^4=I\) on this component, including the degenerate \(N=1\) case. Consequently only times \(0,1,2,3\) need consideration.

**2. Exact amplitude blocks.** Order particle-one arcs by \(X\to Y\), then \(Y\to X\), with particle-two arcs in the same order. Identify an arc \(y_j\to x_i\) with index \((i,j)\). In \(\mathbb R^N=\mathbb R^m\otimes\mathbb R^n\), use standard basis vectors \(e_x,e_y\), all-ones vectors \(\mathbf1_x,\mathbf1_y\), and abbreviate
\[
e=e_x\otimes e_y,\quad u=\mathbf1_x\otimes\mathbf1_y,\quad p=e_x\otimes\mathbf1_y,\quad v=\mathbf1_x\otimes e_y.
\]
The complete amplitude matrix is block off-diagonal,
\[
\Psi_t=\begin{pmatrix}0&B_t\\\sigma B_t^T&0\end{pmatrix}.
\]
Applying the Grover scattering rule
\[
U\bigl(|s,t\rangle\otimes|u,v\rangle\bigr)
=\frac{2}{\deg(t)\deg(v)}\sum_{t'\sim t,\,v'\sim v}
|t,t'\rangle\otimes|v,v'\rangle
-|t,s\rangle\otimes|v,u\rangle
\]
to the initial arcs yields the following **four exact matrices**, where juxtaposition denotes a column-row outer product:
\[
\begin{aligned}
\sqrt2 B_0 &=ee^T,\\
\sqrt2 B_1 &=\sigma(2pv^T/N-ee^T),\\
\sqrt2 B_2 &=ee^T+4uu^T/N^2-2(pv^T+vp^T)/N,\\
\sqrt2 B_3 &=\sigma(2vp^T/N-ee^T).
\end{aligned}
\]
These formulas also follow by evaluating the two-reflection propagation in Step 1, and are checked directly by the independent full-arc transition construction in the accompanying verifier. In particular the even-time block has no exchange-sign dependence.

**3. Singular-value reduction.** Define the unit vector
\[
z=e_x\otimes e_y-\frac2N\mathbf1_x\otimes\mathbf1_y.
\]
Indeed, \(\langle z,z\rangle=1-4/N+4/N=1\). Regard \(z\) as the \(m\times n\) coefficient matrix
\[
D=e_xe_y^T-\frac2N\mathbf1_x\mathbf1_y^T.
\]
It has rank at most two. Its squared singular values are \(A,B\): their sum is \(\|D\|_F^2=1\), and their product is the squared exterior-product area
\[
\Bigl(\frac2N\Bigr)^2\|e_x\wedge\mathbf1_x\|^2\|e_y\wedge\mathbf1_y\|^2
=\frac{4(m-1)(n-1)}{N^2}=q^2.
\]
The formula includes rank-one cases by continuity or direct calculation.

The two odd-time blocks \(B_1,B_3\) each restrict, after deleting zero rows and columns and possibly transposing, to \(-\sigma D/\sqrt2\); hence their nonzero squared singular values are \(A/2,B/2\).

For time two use the partial transpose \(\Gamma_Y\) with respect to the \(\mathbb C^n\) coordinate in \(\mathbb C^m\otimes\mathbb C^n\). The displayed matrices give the **exact identity**
\[
\sqrt2 B_2=(|z\rangle\langle z|)^{\Gamma_Y}.
\]
Writing the Schmidt decomposition \(z=\sqrt A|00\rangle+\sqrt B|11\rangle\), its partial-transposed projector has eigenvalues \(A,B,+\sqrt{AB},-\sqrt{AB}\), and otherwise zero. Therefore the squared singular values of \(B_2\) are \(A^2/2,B^2/2,AB/2,AB/2\).

Finally \(\rho_t=\Psi_t\Psi_t^*=\operatorname{diag}(B_tB_t^*,B_t^TB_t)\). The two blocks have exactly the same nonzero spectrum, so every singular-value square occurs **twice**. This proves the whole claimed multiplicity-resolved tensor-power spectrum, for both signs, all graph sizes and all integer times.

**4. Entropies and sharpness.** Summing \(\alpha\)-powers of these eigenvalues gives \(\operatorname{Tr}(\rho_t^\alpha)=2^{1-\alpha}(A^\alpha+B^\alpha)^{k_t}\) and hence the Rényi formulas, including the continuous \(\alpha\to1\) limit. For any integer \(r\ge1\), the elementary estimate \((r-1)/r^2\le1/4\) has equality only at \(r=2\); hence \(q\le1/2\), with equality exactly when \(m=n=2\). Binary entropy is maximized only by \(A=B=1/2\), and \(k_t\le2\). This gives the exact \(\log8\) bound and its equality cases. If \(m=1\) or \(n=1\), then \(B=0\). For both dimensions large, \(q\to0\), hence \(B\to0\). For \(m=n=r\), \(B=4/r^2+O(r^{-3})\), and expanding binary entropy yields the claimed \(\log r/r^2\) law.

## Verification

The reproducibility file `verify.py` constructs the complete two-particle Grover transition directly from the **original graph's directed arcs**, independent of the closed-form block matrices; it does not assume the spectrum formula. On eleven graph sizes, both exchange signs and all four time residues (plus the four-step return), it checks the explicit amplitude blocks, reduced-density eigenvalues and their multiplicities, normalization, exchange symmetry and period four. Run `python3 verify.py` after installing `numpy` as specified in `requirements.txt`. The tested implementation returned `VERIFY_OK 572 matrix identities 11 graph sizes`. These finite tests are corroboration, not a substitute for the exact proof above.

## Relationship to prior work

Kubota–Matsubara–Segawa [1] **define** this two-particle Grover model, prove swap compatibility, derive balanced complete-bipartite amplitudes (their Section 4), and classify saturation of the *ambient Hilbert-space bound* on \(K_{r,r}\): it occurs precisely for \(r=1,2\), with an appropriate time congruence for \(r=2\). Those statements are not new here. In particular, some balanced-case entropy values can be derived directly from their existing state formula. The present theorem instead gives the **entire reduced spectrum for every unbalanced \(K_{m,n}\)**, exact all-index Rényi entropies, the dimension-free rank-eight and entropy-\(\log8\) bounds, and the partial-transpose tensorization that explains those bounds. The universal constant bound is more informative for large graphs than the ambient \(\log(2mn)\) inequality. The latter paper does not state these general rectangular spectral laws.

No equivalent or stronger complete rectangular-spectrum theorem was identified in targeted mathematical-literature and published-record searches, but absence from the searches is not a proof of publication priority. The exact Bernoulli spectrum is ultimately an implication of explicit Grover scattering, and an earlier implicit or unindexed derivation remains possible.

## Limitations

This is a statement about a specific exchange-symmetric initial edge pair, finite complete bipartite graphs, the particle-label reduced density matrix, discrete nonnegative integer time and the Grover walk on the **Kronecker product graph**. Other initial states, interacting coins, imperfect graph edges, other graph families, operational particle-entanglement measures and continuous-time walks are not included. The finite verification covers only eleven small graphs. No claim of independent external audit, publication priority, or experimental implementability is made.

## References

[1] S. Kubota, H. Matsubara, and E. Segawa, *Entanglement entropy in two-particle Grover walks on graphs*, arXiv:2607.09066 (first posted 2026-07-10), especially Sections 2–5, Lemmas 4.1–4.4 and Theorem 4.5. https://arxiv.org/abs/2607.09066 .
