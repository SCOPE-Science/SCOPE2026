# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof separates the open exceptional range from the endpoint.

For \(-1<\gamma<0\), with \(u=\mathbf1_Q\) and \(Q=(0,1)^N\), the level-set measure is exactly
\[
\int_{|h|<\lambda^{-1/(1+\gamma)}}
|h|^{\gamma-N}|Q\triangle(Q-h)|\,dh.
\]
The translation bound \(|Q\triangle(Q-h)|\lesssim\min\{|h|,1\}\) yields the radial integrals
\[
\int_0^R r^\gamma\,dr
\quad(R\le1),
\]
and
\[
\int_0^1r^\gamma\,dr+
\int_1^Rr^{\gamma-1}\,dr
\quad(R>1).
\]
The first has exactly the scaling \(R^{1+\gamma}\), which cancels \(\lambda\), and the second is uniformly bounded because \(\gamma<0\). Thus the cube indicator has finite BSVY quasi-seminorm but is not Sobolev.

At \(\gamma=-1\), the same jump cannot work: on a cone of small translations transverse to a cube face, the symmetric difference is comparable to \(|h|\), while the kernel is \(|h|^{-N-1}\). After polar integration the lower bound is \(\int_0^\varepsilon dr/r\), so the endpoint quasi-seminorm is infinite.

For the endpoint replacement, the compactly supported function
\[
v(x)=F(x)-F(x-2)
\]
built from the middle-third Cantor distribution function has the singular derivative \(Dv=\mu_C-\tau_2\mu_C\), hence is in \(BV\setminus W^{1,1}\). The two estimates used in the weak-level calculation are standard and have matching exponents:
\[
|v(x+h)-v(x)|\lesssim h^\alpha,
\qquad
|(C\cup(C+2))_h|\lesssim h^{1-\alpha},
\quad
\alpha=\frac{\log2}{\log3}.
\]
Therefore
\[
m_\lambda(h)\lesssim
h^{1-\alpha}
\mathbf1_{h\gtrsim\lambda^{1/\alpha}},
\]
and the endpoint integral satisfies
\[
\lambda\int m_\lambda(h)h^{-2}\,dh
\lesssim
\lambda\int_{c\lambda^{1/\alpha}}^1h^{-1-\alpha}\,dh+O(\lambda)
\lesssim1.
\]
The large-translation tail is integrable because \(v\) is compactly supported. This proves finite \(\dot{BV}_1(-1)\) quasi-seminorm.

For the higher-dimensional lift \(V(x_1,x')=v(x_1)\psi(x')\), the derivative in the first coordinate retains a nonzero singular measure, so \(V\notin W^{1,1}\). The endpoint kernel reductions are exact:
\[
\int_{\mathbb R^{N-1}}(a^2+|z|^2)^{-(N+1)/2}\,dz=C_Na^{-2},
\]
\[
\int_{\mathbb R}(s^2+r^2)^{-(N+1)/2}\,ds=C_Nr^{-N}.
\]
After splitting the increment into its one-dimensional and transverse parts, these identities reduce the two level-set estimates respectively to the already established one-dimensional endpoint bound for \(v\) and the endpoint bound for a compactly supported Lipschitz function \(\psi\). No cancellation between the two parts is required.

The limiting cases were checked explicitly: the cube argument uses \(\gamma<0\) at large scales and breaks exactly at \(\gamma=-1\) at small scales; the Cantor proof remains finite exactly because the Hölder exponent and Minkowski-neighborhood exponent cancel in the weak integral.

## Originality

**PASS, to the best of our knowledge.**

The recent paper of Chen–Yang–Yuan–Zhang, arXiv:2609.19029v1, was inspected at its definitions, Theorem 1.2, Remark 1.3, Theorem 2.4, and the constructions used for non-normability. It proves that the homogeneous Hardy–Sobolev space is strictly contained separately in \(\dot W^{1,1}(\gamma)\) and \(\dot{BV}(\gamma)\), and it uses the natural inclusion
\[
\dot W_N^{1,1}(\gamma)\longrightarrow\dot{BV}_N(\gamma),
\]
but the inspected statements and proof do not assert that this inclusion is strict and do not provide a singular-BV witness for it.

The 2024 Brezis–Seeger–Van Schaftingen–Yung paper was checked around the exceptional negative range and its perspectives section. It poses the relation of the exceptional spaces to other familiar function spaces but no mutual strictness theorem between \(\dot W^{1,1}(\gamma)\) and \(\dot{BV}(\gamma)\) was located.

Picenni's 2024 work was checked as nearby literature on jump and Cantor contributions in nonlocal total-variation approximations; its main setting uses positive \(\gamma\) and does not cover this exceptional negative-range statement.

Searches were made for exact and synonymous formulations involving the BSVY spaces, strict \(W^{1,1}(\gamma)\)-to-\(BV(\gamma)\) inclusion, \(\gamma=-1\), Cantor functions/staircases, singular-continuous BV derivatives, and the source identifier arXiv:2609.19029. No equivalent or stronger theorem was located. The current SCOPE archive was also checked by source identifier, object, and synonymous terminology, with no overlap found immediately before publication.

No specifically identified inaccessible paper produced concrete evidence of prior coverage. Residual originality risk remains for two reasons. First, for \(-1<\gamma<0\) the cube witness is elementary once the mutual-inclusion question is isolated, so it could exist as an informal or differently phrased observation. Second, the closest paper on the exceptional range is extremely recent, so parallel work may not yet be indexed. The endpoint Cantor witness and the jump-to-Cantor transition are the more substantive part of the result.

## Value

**PASS.**

The result completes the basic mutual ordering of the two exceptional BSVY first-order spaces throughout the entire range \([-1,0)\). Combined with the recent strict Hardy–Sobolev embedding, it yields
\[
\dot H^{1,1}
\subsetneq
\dot W_N^{1,1}(\gamma)
\subsetneq
\dot{BV}_N(\gamma).
\]

The endpoint supplies an analytic mechanism rather than only a separation example. For \(-1<\gamma<0\), codimension-one jumps have finite weak difference-quotient size. At \(\gamma=-1\), the same singularity produces a logarithmic divergence, yet a singular-continuous Cantor derivative survives because its Hölder modulus and the Minkowski size of its support exactly compensate. This identifies a change in the kind of BV singularity compatible with the exceptional endpoint.

## Literature checked

- Y. Chen, D. Yang, W. Yuan, Y. Zhang, *On Two Questions by Brezis et al Concerning the Critical Difference Quotient Characterization of First-Order Sobolev Spaces*, arXiv:2609.19029v1 (2026), including the definitions, Theorem 1.2, Remark 1.3, Theorem 2.4, and the endpoint constructions.
- H. Brezis, A. Seeger, J. Van Schaftingen, P.-L. Yung, *Families of functionals representing Sobolev norms*, Analysis & PDE 17 (2024), 943–979, especially the exceptional-range discussion and perspectives.
- N. Picenni, *New estimates for a class of non-local approximations of the total variation*, J. Funct. Anal. 287 (2024); arXiv:2307.16471, as nearby BV jump/Cantor literature.
- Searches for strict mutual inclusion, endpoint Cantor witnesses, singular-continuous examples, and equivalent BSVY terminology.
- The current SCOPE archive by source identifier, mathematical object, and equivalent terminology.

## Scope of the claim

Novelty is claimed only for the strict inclusion
\[
\dot W_N^{1,1}(\gamma)\subsetneq\dot{BV}_N(\gamma),
\qquad -1\le\gamma<0,
\]
with the explicit open-range jump witness, the endpoint Cantor witness, and the associated jump-to-Cantor transition.

No novelty is claimed for the definitions of the BSVY spaces, the natural Sobolev-to-BV inclusion, the classical BV translation inequality, standard properties of the Cantor function, or the strict Hardy–Sobolev embeddings established in arXiv:2609.19029. No intrinsic characterization of \(\dot{BV}_N(-1)\) is claimed.
