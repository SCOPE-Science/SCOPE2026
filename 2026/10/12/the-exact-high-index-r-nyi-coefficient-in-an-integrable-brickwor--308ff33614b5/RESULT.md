# The exact high-index Rényi coefficient in an integrable brickwork circuit

## Finding

For the integrable four-state permutation circuit defined below, the operator entanglement of a specified evolving one-site transition and the entanglement of its companion domain-wall state have **the same sharp logarithmic coefficient**. For every fixed real \(1<\alpha<\infty\), as integer \(t\to\infty\),

\[
\boxed{\quad S_\alpha(t)=\frac{\alpha-\frac12}{\alpha-1}\log t+O_\alpha(1).\quad}
\]

Equivalently, for the normalized squared Schmidt weights \(\{p_j(t)\}\),

\[
\boxed{\quad Z_\alpha(t):=\sum_jp_j(t)^\alpha=\Theta_\alpha(t^{1/2-\alpha}).\quad}
\]

In particular, the purity-order entropy satisfies \(S_2(t)=\tfrac32\log t+O(1)\). This resolves the finite-high-index coefficient left undetermined by the source's inequality (S51), without asserting a prefactor for the Rényi moments themselves.

## Assumptions and scope

Each lattice site has a sector bit and a color bit, so its Hilbert space is \(\mathbb C^2\otimes\mathbb C^2\). The two-site unitary is the permutation

\[
R|s,a;\tau,b\rangle=|\tau,a+(s+\tau)b;\ s,b\rangle,
\]

with all additions and products of bits taken modulo two. As in Pozsgay [1,2], one Floquet period comprises the even and odd brickwork layers, the spatial cut is between sites \(0\) and \(1\), and the infinite-volume limit is taken at fixed integer time \(t\) *before* the limit \(t\to\infty\). The first setting is the Hilbert–Schmidt normalized Heisenberg evolution of the one-site transition \(O_\times=|B,0\rangle\langle A,0|\) at site \(1\). Its normalized Hermitian combination \(O_H=(O_\times+O_\times^\dagger)/\sqrt2\) has the same Schmidt spectrum by the source's supplementary Section II C.

In the second setting, the initial domain-wall product state has left-side local state \(|+\rangle_{\mathrm{sec}}|0\rangle_{\mathrm{col}}\) and right-side local state \(|+\rangle_{\mathrm{sec}}|+\rangle_{\mathrm{col}}\); the evolution and spatial cut use the same brickwork permutation. All entropies use natural logarithms, and \(\alpha>1\) is fixed independently of \(t\). No claim is made for arbitrary input operators, other initial states, or noncommuting limits.

For either setting let \(M\) be the normalized coefficient matrix in orthonormal left/right count-resolving bases; thus \(\|M\|_2=1\), and \(Z_\alpha=\|M\|_{2\alpha}^{2\alpha}\), where the subscript indicates the Schatten norm. Let \(P_k^L,P_\ell^R\) be the orthogonal sector-count projectors from source [1], and set \(M_{k\ell}=P_k^LM P_\ell^R\). The source establishes the following exact *individual-block* flat squared singular values:

\[
\operatorname{spec}_{>0}(M_{k\ell}M_{k\ell}^\dagger)=
\{q_kr_\ell 2^{-g(\ell-k)}\}^{\times 2^{g(\ell-k)}}.
\]

For the operator \(q_k=2^{-(t-1)}\binom{t-1}{k}\), \(0\le k\le t-1\), and \(r_\ell=2^{-t}\binom t\ell\), \(0\le\ell\le t\). Its rank exponent is \(g(d)=d-1\) when \(d>0\), and \(g(d)=-d\) when \(d\le0\). For the domain wall, \(q_k=r_k=2^{-t}\binom tk\), \(0\le k\le t\), and \(g(d)=|d|\). We extend these probability masses by zero outside their ranges.

## Proof

**1. Group by count difference rather than by individual blocks.** For each integer \(d\), define \(M_d=\sum_k M_{k,k+d}\). Blocks within a fixed \(d\) occupy distinct left count spaces and distinct right count spaces, so \(M_d\) is their orthogonal direct sum (up to row/column permutations). Consequently, with \(p=2\alpha\), the source's flat block spectrum yields the *exact* identity

\[
\|M_d\|_{p}^{p}=2^{(1-\alpha)g(d)}\sum_k(q_kr_{k+d})^\alpha.
\tag{1}
\]

We do not claim that blocks with different \(d\) are mutually orthogonal in this sense; their coherence is controlled in Step 3.

**2. Uniform binomial overlap estimate.** For all sufficiently large \(t\), the standard central-binomial bound gives \(\max_kq_k\le C t^{-1/2}\) and \(\max_\ell r_\ell\le C t^{-1/2}\), with the same statement in both settings. Therefore \(\max_{k,\ell}q_kr_\ell\le C^2/t\), and, for every \(d\),

\[
\sum_kq_kr_{k+d}\le\max_\ell r_\ell\sum_kq_k\le C t^{-1/2}.
\]

For each fixed \(\alpha>1\), these imply

\[
\sum_k(q_kr_{k+d})^\alpha
\le (C^2/t)^{\alpha-1}\sum_kq_kr_{k+d}
\le C_\alpha t^{1/2-\alpha},
\tag{2}
\]

uniformly over all integer count differences \(d\).

**3. Schatten triangle controls coherent assembly.** By (1)–(2),

\[
\|M_d\|_{2\alpha}
\le C_\alpha t^{(1/2-\alpha)/(2\alpha)}
2^{-(\alpha-1)g(d)/(2\alpha)}.
\]

In both settings \(g(d)\ge |d|-1\), and so the numerical series \(\sum_{d\in\mathbb Z}2^{-(\alpha-1)g(d)/(2\alpha)}\) converges for every fixed \(\alpha>1\). Since \(2\alpha>1\), the Schatten norm obeys the triangle inequality. Hence

\[
\|M\|_{2\alpha}=\left\|\sum_d M_d\right\|_{2\alpha}
\le\sum_d\|M_d\|_{2\alpha}
\le C'_\alpha t^{(1/2-\alpha)/(2\alpha)},
\]

and therefore \(Z_\alpha(t)\le C''_\alpha t^{1/2-\alpha}\).

**4. Count-diagonal pinching gives a matching lower bound.** Let \(M_0=\sum_kP_k^LMP_k^R\). Count-phase averaging expresses this diagonal as

\[
M_0=\frac1{2\pi}\int_0^{2\pi}
\Bigl(\sum_ke^{ik\theta}P_k^L\Bigr)
M\Bigl(\sum_\ell e^{i\ell\theta}P_\ell^R\Bigr)^\dagger\,d\theta.
\]

Every left and right factor is unitary on the count-resolved support, so convexity and unitary invariance of the Schatten \(2\alpha\)-norm show \(\|M_0\|_{2\alpha}\le\|M\|_{2\alpha}\). Both rank-exponent functions satisfy \(g(0)=0\). By (1),

\[
Z_\alpha(t)\ge\|M_0\|_{2\alpha}^{2\alpha}
=\sum_k(q_kr_k)^\alpha.
\tag{3}
\]

For a fixed sufficiently large constant \(B\), at least \(c\sqrt t\) integers in \(|k-t/2|\le B\sqrt t\) have both \(q_k\ge c/\sqrt t\) and \(r_k\ge c/\sqrt t\), by Stirling's formula (equivalently the local central limit theorem). Their contribution to (3) is at least \(c_\alpha t^{1/2-\alpha}\).

Combining both bounds proves \(Z_\alpha(t)=\Theta_\alpha(t^{1/2-\alpha})\). Finally, \(S_\alpha=(1-\alpha)^{-1}\log Z_\alpha\) proves the displayed entropy law. The source's identity of normalized operator Schmidt spectra for \(O_\times\) and \(O_H\) transfers the result to the Hermitian operator.

## Verification

The standalone `verify.py` uses NumPy and *direct gate propagation*, not a stored spectrum or an assumed asymptotic identity. It builds normalized finite-time coefficient matrices for both settings at integer times \(1\) through \(4\), checks every nonempty count branch against its claimed flat singular spectrum, and independently tests diagonal pinching and Schatten-triangle moment inequalities at Rényi orders \(1.2,1.5,2,3\). On replay it reports `VERIFY_OK 94 flat count-sector spectra; diagonal pinching and Minkowski moments`. To reproduce: `python -m pip install -r requirements.txt` and `python verify.py` in a folder containing both package files. The infinity-time statement is proved analytically above; finite checks alone would not establish it.

## Relationship to prior work

Pozsgay's 2026 work [1,2], first publicly available in preliminary form on September 4, establishes the gate and domain-wall model, proves the flat spectra of count branches, and derives \(S_\alpha=\Theta(\log t)\) at each fixed \(\alpha>1\). Supplemental Eq. (S51) explicitly leaves its logarithmic coefficient unresolved. The present result uses the established branch spectra but introduces difference-diagonal Schatten-norm summation together with a matched count-diagonal pinching lower bound to determine the coefficient. We claim neither the four-state circuit construction nor the count-branch flatness, the square-root von Neumann law, or the original broad high-index order bounds. Pozsgay's separate Yang–Baxter classification [3] treats different gate classes and does not supply this coefficient. General operator-entanglement/simulability bounds [4] do not identify this exact count-sector coefficient.

## Limitations

The assertion is for fixed \(\alpha>1\), not uniform as \(\alpha\downarrow1\), and does not give a multiplicative constant or a limit for \(t^{\alpha-1/2}Z_\alpha(t)\). It also does not determine the full Schmidt spectrum, extend the result to arbitrary sources, or settle finite-size recurrence. The September 4 preliminary manuscript's file content was not retrievable during comparison; its public description states the qualitative logarithmic law, but an uninspected implicit derivation cannot be excluded. This residual priority risk warrants independent literature scrutiny.

## References

1. B. Pozsgay and I. Vona, *Square-root growth of operator entanglement in an integrable brickwork circuit*, preliminary public manuscript, Zenodo record 22306151, September 4, 2026, https://doi.org/10.5281/zenodo.22306151.
2. B. Pozsgay, *Square-root growth of operator entanglement in an integrable brickwork circuit*, arXiv:2609.39401, first posted September 30, 2026; supplementary Sections II and IV, especially (S22), (S38), (S51), https://arxiv.org/pdf/2609.39401.
3. B. Pozsgay, *On the growth of operator entanglement in brickwork circuits with Yang–Baxter gates*, arXiv:2609.05121, September 4, 2026, https://arxiv.org/abs/2609.05121.
4. N. Dowling, *Classical Simulability from Operator Entanglement Scaling*, arXiv:2603.05656, March 2026, https://arxiv.org/abs/2603.05656.
