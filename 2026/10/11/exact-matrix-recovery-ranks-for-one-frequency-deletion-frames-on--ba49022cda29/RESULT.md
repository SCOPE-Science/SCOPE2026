# Exact matrix-recovery ranks for one-frequency deletion frames on finite abelian groups

## Finding
Let \(G\) be any finite abelian group of order \(N\ge4\), let \(\Gamma=\widehat G\) be its character group, written additively, and let \(\mathcal H_0\subset\mathbb C^G\) be the zero-mean signals. For each nontrivial character \(\ell\in\Gamma\setminus\{0\}\), let \(P_\ell\) remove exactly its Fourier coefficient. The complex span of the rank-one intensity measurement operators arising from all pointwise values of \(P_\ell f\), \(\ell\ne0\), has **exact** dimension
\[
\boxed{R(G)=(N-1)^2-\sum_{\substack{\delta\in\Gamma\setminus\{0\}\\\operatorname{ord}(\delta)\text{ even}}}\left(\frac N{\operatorname{ord}(\delta)}-1\right).}
\]
For each even-order \(\delta\), the corresponding invisible Fourier-matrix band has precisely one independent complex null direction for each coset of \(\langle\delta\rangle\) other than the subgroup itself; there are no other invisible directions.

Consequently the family recovers **all complex matrices** on \(\mathcal H_0\) exactly when \(N\) is odd. Furthermore, for all finite abelian groups with \(N\ge2\), the magnitudes \(\{|P_\ell f(x)|:x\in G,\ \ell\ne0\}\) recover every \(f\in\mathcal H_0\) up to one global unimodular factor **if and only if \(N\) is odd and \(N\ge5\)**. The exceptional smaller orders have matrix ranks \(R(G)=0\) for \(N=2\) and \(R(G)=2\) for \(N=3\).

The rank depends on the group structure, not just its cardinality. For the three abelian groups of order eight,
\[
R(\mathbb Z_8)=44,\qquad R(\mathbb Z_4\times\mathbb Z_2)=36,\qquad R(\mathbb Z_2^3)=28.
\]

## Assumptions and scope
A character \(\gamma\) takes values in the unit circle. With Fourier normalization
\[
\widehat f(\gamma)=\sum_{x\in G}f(x)\overline{\gamma(x)},\qquad
f(x)=\frac1N\sum_{\gamma\in\Gamma}\widehat f(\gamma)\gamma(x),
\]
zero mean is equivalent to \(\widehat f(0)=0\). In the Fourier coordinate space \(V=\mathbb C^{\Gamma\setminus\{0\}}\) of dimension \(N-1\), define measurement vectors \(v_{\ell,x}\in V\) by
\[
v_{\ell,x}(\gamma)=\begin{cases}\overline{\gamma(x)},&\gamma\ne\ell,\\0,&\gamma=\ell.\end{cases}
\]
Then \(N^2|P_\ell f(x)|^2=\langle \widehat f\widehat f^*v_{\ell,x},v_{\ell,x}\rangle\), with the usual Hermitian inner-product convention; equivalently this is \(v_{\ell,x}^*(\widehat f\widehat f^*)v_{\ell,x}\). The rank \(R(G)\) is the complex dimension of \(\operatorname{span}\{v_{\ell,x}v_{\ell,x}^*:\ell\ne0,x\in G\}\), or the real dimension of the same span inside the Hermitian matrices. It is independent of Fourier normalization.

The statement covers **all** finite abelian groups (including noncyclic, composite, odd, and even orders) and **all** nonzero-frequency deletion masks, one at a time. It does not require the original signal to have nonzero Fourier coefficients at every character.

## Proof
Put \(K=\Gamma\), and regard a general complex matrix \(X=(X_{a,b})_{a,b\ne0}\) as an element of \(M_{N-1}(\mathbb C)\). The linear measurement map is
\[
\mathcal M(X)_{\ell,x}=v_{\ell,x}^*Xv_{\ell,x}
=\sum_{a,b\in K\setminus\{0,\ell\}}X_{a,b}(a-b)(x).
\]
By character orthogonality, taking the Fourier coefficient in \(x\) at \(\delta\in K\) is an invertible change of output coordinates and yields
\[
T_\delta^\ell=\sum_{\substack{a,b\ne0,\ell\\a-b=\delta}}X_{a,b}.
\]
Thus different difference bands \(\delta\) decouple exactly, without approximation.

For \(\delta=0\), put \(S_0=\sum_{a\ne0}X_{a,a}\). We have \(T_0^\ell=S_0-X_{\ell,\ell}\). When \(N\ge4\), summing over the \(N-1\) allowed deletions gives
\[
S_0=\frac1{N-2}\sum_{\ell\ne0}T_0^\ell,
\]
so every diagonal entry is recoverable and this band has no kernel.

Fix \(\delta\ne0\). Extend the band entries to functions on \(K\) by
\[
x_j=\begin{cases}X_{j,j-\delta},&j\ne0,\delta,\\0,&j=0\text{ or }j=\delta.\end{cases}
\qquad S_\delta=\sum_{j\in K}x_j.
\]
Exactly two deletions remove each genuine off-diagonal matrix entry: its row frequency and its column frequency. Consequently
\[
T_\delta^\ell=S_\delta-x_\ell-x_{\ell+\delta},\qquad
S_\delta=\frac1{N-3}\sum_{\ell\ne0}T_\delta^\ell
\]
(the denominator is nonzero because \(N\ge4\)). The data therefore determine \(b_\ell=S_\delta-T_\delta^\ell=x_\ell+x_{\ell+\delta}\) for all \(\ell\ne0\), and \(b_0=x_0+x_\delta=0\) is known in advance.

Let \(r=\operatorname{ord}(\delta)\). The cycles of translation by \(\delta\) are exactly the \(N/r\) cosets of \(\langle\delta\rangle\), each of length \(r\). A vector is in the kernel of this band exactly when
\[
x_{j+\delta}=-x_j\quad(j\in K),\qquad x_0=x_\delta=0.
\]
If \(r\) is odd, iterating once around any cycle gives \(x_j=-x_j\), hence every entry vanishes. If \(r\) is even, an alternating value is free on each cycle. The cycle through zero is forced to vanish, whereas each of the remaining \(N/r-1\) cycles contributes exactly one free complex scalar. Such alternating cycles have zero sum, so they satisfy the independently recovered \(S_\delta=0\) constraint as well. Thus **the kernel dimension in band \(\delta\)** is exactly \(N/r-1\) for even \(r\), and zero for odd \(r\). Distinct bands have disjoint sets of matrix coordinates, so adding these dimensions gives the boxed formula.

The measurement operators are Hermitian. Their rank over \(\mathbb C\) equals the real span dimension in the Hermitian subspace: taking adjoints of any complex linear dependence separates its real and imaginary parts into real linear dependences. Hence the computed complex rank is also the full Hermitian tomography rank. When every nonzero element of \(K\) has odd order (equivalently, \(N\) odd), the matrix map is injective; the explicit odd-cycle inverse is
\[
x_j=\frac12\sum_{t=0}^{r-1}(-1)^t b_{j+t\delta},\qquad r\text{ odd}.
\]
In particular, all rank-one Gram matrices \(\widehat f\widehat f^*\) are recovered, which recovers \(f\) up to a global phase.

If \(N\ge4\) is even, \(K\) contains an element \(\delta\) of order two. Choose \(u\notin\{0,\delta\}\), so \(u\) and \(v=u+\delta\) are both nonzero. Take Fourier coefficient vectors supported at \(u,v\) with respective coefficients \((1,i)\) and \((1,-i)\). After deleting \(u\) or \(v\), one unimodular character survives; after any other deletion the two terms interfere with relative character \(\delta(x)\in\{1,-1\}\), and their intensities remain equal. The two coefficient vectors are not unimodular scalar multiples, so phase retrieval fails. For \(N=3\), any deletion leaves one of the two nonzero characters, revealing only its modulus; the two relative phases cannot be distinguished. For \(N=2\), deleting the sole nonzero coefficient leaves the zero signal regardless of its magnitude. This proves the phase-retrieval classification and the small-order ranks.

For \(N=8\), summing over element orders gives nullities \(5\), \(13\), and \(21\) for the three groups displayed in the finding, and subtracting these from \(7^2=49\) yields their ranks.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library, rational Gaussian elimination, and group arithmetic on tuples of residues. Run `python3 verify.py` in the directory containing this document; the program prints each tested group's exact rank/nullity and ends with `VERIFY_OK groups= 20`.

The checker constructs the actual linear Fourier-band observation matrices whose \((\ell,(a,b))\) entry equals \(1\) precisely when the pair \((a,b)\) survives deletion of \(\ell\). It computes their ranks over \(\mathbb Q\), checks the predicted dimensions for twenty cyclic and noncyclic groups, constructs and tests explicit alternating kernel vectors for every even-order band, and checks odd-order inverse reconstruction from twenty deterministic rank-one test vectors per odd group. All arithmetic is exact. The finite suite is not a proof for untested groups; the algebraic proof above gives the universal theorem.

## Relationship to prior work
Bartusel, Führ and Oussa, *Phase retrieval for affine groups over prime fields* (arXiv:2109.07123, first public version 2021-09-15), establish the underlying frequency-deletion phase-retrieval phenomenon for prime cyclic groups in Remark 6.11 and ask whether it persists for general cyclic groups. The publicly available result *Frequency-deletion phase retrieval on cyclic groups: exact odd-order classification* resolves that cyclic **phase-retrieval** question for all orders, but explicitly does not classify noncyclic abelian groups; its theorem does not state the operator-span dimensions or even-order nullspaces. The present result retains that earlier cyclic phase-retrieval conclusion as prior coverage. Its distinct contribution is the all-abelian **exact tomography rank law**, an explicit basis of its missing matrix directions, and its order-dependent structure effects, including the order-eight trichotomy.

Führ and Oussa, *Phase retrieval for nilpotent groups* (arXiv:2201.08654), study phase retrieval for irreducible representation orbits rather than this fixed deterministic family of Fourier-deletion projectors. Likewise, the published result *Sharp operator-span capacity of two-sparse multi-window Gabor systems* concerns time-frequency Weyl orbits and sparse-window budgets, not deletion frames. Neither supplies this operator's element-order nullity formula.

## Limitations
There is no noise-stability constant or condition-number calculation here; the result concerns exact linear matrix recovery and exact noiseless rank-one phase retrieval. It does not determine the smallest subset of deletion labels or sample sites sufficient for injectivity. The known odd-cyclic phase-retrieval case is **not** claimed as new. An equivalent operator-rank formula under different terminology may have escaped indexing; independent mathematical review remains necessary.

## References
1. D. Bartusel, H. Führ, V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123v1 (2021-09-15), Remark 6.11 and Theorems 6.5–6.6.
2. *Frequency-deletion phase retrieval on cyclic groups: exact odd-order classification*, publicly indexed published-finding corpus result, `2026/10/4/SCOPE-frequency-deletion-phase-retrieval-on-cyclic-groups-exact-odd-or--36702d91730c`, complete published `RESULT.md`.
3. H. Führ, V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654v1 (2022-01-21), especially the setting of the finite-group phase-retrieval results.
4. *Sharp operator-span capacity of two-sparse multi-window Gabor systems*, publicly indexed published-finding corpus result, `2026/10/4/SCOPE-sharp-operator-span-capacity-of-two-sparse-multi-window-gabor-sy--b553eeb756ed`, published `RESULT.md`.
