# Dimension-free linear rigidity of nonnegative critically sampled cyclic Gabor windows

## Finding

Let integers \(p\ge 2\), \(q\ge1\), and \(N=pq\) be arbitrary. For a nonnegative real unit vector \(g\in\mathbb C^N\), form the critical-density finite Gabor family
\[
\mathcal G(g)=\{M_{pb}T_{qa}g:0\le a<p,\ 0\le b<q\}.
\]
Write \(S_g\) for its frame operator, and \(\delta=\|S_g-I_N\|_{\mathrm{op}}\). Let \(\mathcal T_{p,q}\) be the class of nonnegative flat transversal windows: for every residue \(u\in\{0,\ldots,q-1\}\), exactly one coordinate of the form \(u+qt\), \(0\le t<p\), equals \(1/\sqrt q\), with all other coordinates zero.

The complete frame spectrum, with multiplicity, is
\[
\operatorname{spec}(S_g)=\bigcup_{u=0}^{q-1}\bigcup_{j=0}^{p-1}
\left\{q\left|\sum_{t=0}^{p-1}g[u+qt]e^{-2\pi ijt/p}\right|^2\right\}.
\]
Consequently \(S_g=I_N\) if and only if \(g\in\mathcal T_{p,q}\). More strongly, for every such \(g\) with \(\delta\le1/10\),
\[
\boxed{\operatorname{dist}_{\ell^2}(g,\mathcal T_{p,q})\le\frac43\delta.}
\]
The constant is independent of both dimensions. The *linear order* in \(\delta\) cannot be replaced by any uniform \(o(\delta)\) estimate: explicit nonnegative two-tap windows have distance-to-defect ratio tending to \(1/2\). No optimality of the displayed constant \(4/3\) is asserted.

## Assumptions and scope

Use counting-measure \(\ell^2\) on the cyclic group \(\mathbb Z_N\), with inner product \(\langle f,h\rangle=\sum_{k=0}^{N-1}f[k]\overline{h[k]}\). Define cyclic translation \((T_af)[k]=f[k-a]\) and modulation \((M_bf)[k]=e^{2\pi ibk/N}f[k]\). The set of \(pq=N\) atoms uses translations by multiples of \(q\) and modulations by multiples of \(p\). No coprimality of \(p,q\) is assumed. All inequalities are with the unnormalized synthesis/frame operator \(S_g f=\sum_{a,b}\langle f,M_{pb}T_{qa}g\rangle M_{pb}T_{qa}g\). Nonnegativity and normalization \(\|g\|_2=1\) are essential to the rigidity assertion; the spectral identity itself holds for arbitrary complex \(g\).

## Proof

**Step 1: complete spectral decomposition.** Write each coordinate uniquely as \(k=u+qt\) with \(0\le u<q\), \(0\le t<p\). Fixing \(u\), let \(h_u[t]=g[u+qt]\), a cyclic vector of length \(p\). On this residue fiber, the atom \(M_{pb}T_{qa}g\) equals \(e^{2\pi ibu/q}\) times the cyclic translate \(h_u[t-a]\). Summing over \(b\) eliminates all interactions between different residues, because \(\sum_{b=0}^{q-1}e^{2\pi ib(u-v)/q}=q\mathbf1_{u=v}\). The restriction of the frame operator to the \(u\)-fiber is therefore the circulant
\[
q\sum_{a=0}^{p-1}|T_a h_u\rangle\langle T_a h_u|.
\]
The \(p\)-point discrete Fourier basis diagonalizes it, with eigenvalues \(q|\sum_t h_u[t]e^{-2\pi ijt/p}|^2\). Taking the orthogonal sum over residues gives the stated full spectrum.

**Step 2: a nonnegative fiber inequality.** Set \(a_t=\sqrt q\,g[u+qt]\ge0\). Since every eigenvalue differs from \(1\) by at most \(\delta\), the discrete Fourier coefficients \(F_j=\sum_t a_te^{-2\pi ijt/p}\) obey
\[
1-\delta\le |F_j|^2\le1+\delta\qquad(0\le j<p).
\]
Put \(Z=\sum_ta_t=F_0\), \(Q=\sum_ta_t^2=p^{-1}\sum_j|F_j|^2\), and \(m=\max_ta_t\). Then \(Z^2,Q\in[1-\delta,1+\delta]\). As \(Q\le mZ\),
\[
m\ge\frac{1-\delta}{\sqrt{1+\delta}}\ge\frac67\qquad(0\le\delta\le1/10),
\]
where \(\sqrt{11/10}<21/20\). Choose an index \(t_*\) at which \(m\) occurs and define \(r=\sum_{t\ne t_*}a_t\) and \(R^2=\sum_{t\ne t_*}a_t^2\). By nonnegativity,
\[
2mr\le Z^2-Q=2\sum_{s<t}a_sa_t\le2\delta.
\]
Hence \(r\le7\delta/6\) and \(R^2\le r^2\le49\delta^2/36\). Moreover \(m^2=Q-R^2\), so
\[
|m-1|=\frac{|m^2-1|}{m+1}
\le\frac{\delta+49\delta^2/36}{13/7}
\le\frac{2863}{4680}\delta<\frac58\delta.
\]
The squared distance from the fiber \((a_t)\) to the unit basis vector at \(t_*\) is bounded by
\[
(m-1)^2+R^2\le\left(\frac{25}{64}+\frac{49}{36}\right)\delta^2
=\frac{1009}{576}\delta^2<\frac{16}{9}\delta^2.
\]
Rescaling each fiber by \(1/\sqrt q\) and independently selecting its index \(t_*\) yields a member of \(\mathcal T_{p,q}\). Summing the \(q\) fiber errors proves the claimed \(4\delta/3\) bound.

**Step 3: exact equality.** If \(\delta=0\), Step 2 gives \(r=0\) and \(m=1\) in each rescaled fiber, exactly a single unit spike per fiber, so \(g\in\mathcal T_{p,q}\). Conversely, a transversal has, in each fiber, Fourier coefficients of modulus \(1\), and the spectrum from Step 1 equals \(1\) throughout. Thus \(S_g=I_N\) exactly for the stated class.

**Step 4: optimal order.** Fix \(p=2\) and any \(q\ge1\). For \(0<t<1/\sqrt2\) let each rescaled fiber consist of the entries \(\sqrt{1-t^2}\) and \(t\). The corresponding nonnegative global window is normalized. The two eigenvalues on each fiber are
\[
\bigl(\sqrt{1-t^2}+t\bigr)^2\quad\text{and}\quad
\bigl(\sqrt{1-t^2}-t\bigr)^2,
\]
so \(\delta=2t\sqrt{1-t^2}\). The nearest flat transversal chooses the larger of the two taps in every fiber, giving
\[
\operatorname{dist}_{\ell^2}(g,\mathcal T_{2,q})
=\sqrt{2-2\sqrt{1-t^2}}.
\]
Their ratio tends to \(1/2\) as \(t\downarrow0\), ruling out a dimension-uniform sublinear error estimate. This does not prove the coefficient \(4/3\) optimal.

## Verification

The accompanying `CHECK.py` independently constructs the finite Gabor synthesis/Gram matrices and compares their numerical eigenvalues with the Fourier-fiber spectrum across several dimensions. It also tests exact transversals, small nonnegative perturbations and the linear-order witness. With NumPy installed, run `python CHECK.py`; its deterministic output is `CHECK_OK 576`. These finite tests corroborate formulas but do not establish the universal theorem, whose proof is above. No external theorem prover or independent audit was used.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez (arXiv:2605.16139, initially public 15 May 2026) obtain block equivalences and diagonal structures for finite Gabor frame operators. Their matrix decompositions motivate the choice of subgroup lattice here. The present claim is an inverse, dimension-free quantitative conclusion **under positivity**, not merely another diagonalization: a near-identity frame operator forces the window to be near a discrete flat transversal, with optimal linear *order*.

Nicola (arXiv:2305.02738) classifies maximally localized Gabor orthonormal bases in locally compact abelian groups; its extremal constructions are relevant to the exact-flat case, but the inspected arguments do not yield this finite, uniform, near-orthonormal stability inequality. Salanevich and Strachan (arXiv:2509.01325) analyze robustness of finite Gabor frames under noise and erasures; their principal results study frame bounds of random and other designs, rather than a positive-window inverse structural estimate. Liehr (arXiv:2605.29984) classifies compactly supported orthonormal Gabor systems on the real line, not the stated finite quantitative problem. The exact-flat characterization is not presented as a standalone originality claim; the quantitative inverse rigidity and sharp exponent are the asserted contribution.

## Limitations

The theorem is for nonnegative *real* windows and the specified rectangular critical lattice. It does not extend automatically to signed or complex windows, different lattices, redundant Gabor systems, or noisy frame-operator observations other than the operator norm. The coefficient \(4/3\) is sufficient, not claimed best. The proof supplies no stability statement once \(\delta>1/10\). Similar inequalities may exist in unindexed or more general frame-stability literature, and independent mathematical validation remains outstanding.

## References

1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139 (first posted 2026-05-15), https://arxiv.org/abs/2605.16139.
2. F. Nicola, *Maximally localized Gabor orthonormal bases on locally compact Abelian groups*, arXiv:2305.02738, https://arxiv.org/abs/2305.02738.
3. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325, https://arxiv.org/abs/2509.01325.
4. L. Liehr, *Compactly supported Gabor orthonormal bases*, arXiv:2605.29984, https://arxiv.org/abs/2605.29984.
