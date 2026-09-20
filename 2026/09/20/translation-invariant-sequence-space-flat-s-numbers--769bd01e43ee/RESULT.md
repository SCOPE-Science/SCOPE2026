# Flat s-number profile for translation-invariant operators on sequence spaces

## Result

Let \(G\) be an infinite discrete group. Let
\[
X=\ell_p(G)\quad (1\le p<\infty),\qquad\text{or}\qquad X=c_0(G),
\]
and let \(L_g\) denote left translation,
\[
(L_gx)(h)=x(g^{-1}h).
\]
Suppose \(T\in\mathcal B(X)\) commutes with every left translation:
\[
TL_g=L_gT\qquad(g\in G).
\]
Then, for every \(n\ge1\),
\[
\boxed{a_n(T)=b_n(T)=c_n(T)=d_n(T)=\|T\|.}
\]
Here
\[
\begin{aligned}
a_n(T)&=\inf_{\operatorname{rank}R<n}\|T-R\|,\\
b_n(T)&=\sup_{\dim E=n}\ \inf_{\substack{x\in E\\ \|x\|=1}}\|Tx\|,\\
c_n(T)&=\inf_{\operatorname{codim}M<n}\|T|_M\|,\\
d_n(T)&=\inf_{\dim N<n}\|Q_NT\|,
\end{aligned}
\]
where \(Q_N:X\to X/N\) is the quotient map.

Moreover,
\[
\boxed{
\operatorname{dist}(T,\mathcal K(X))
=\operatorname{dist}(T,\mathcal{FSS}(X))
=\operatorname{dist}(T,\mathcal{SS}(X))
=\|T\|.
}
\]
Consequently, within this translation-invariant class,
\[
T\text{ compact}\iff T\text{ finitely strictly singular}
\iff T\text{ strictly singular}\iff T=0.
\]

The quantitative mechanism is stronger. For every \(\varepsilon>0\) and every
nonzero \(T\), there is a **1-complemented** subspace \(E\subset X\), isometric
to \(\ell_p\) when \(X=\ell_p(G)\) and to \(c_0\) when \(X=c_0(G)\), such that
\[
\boxed{\|Tx\|\ge(\|T\|-\varepsilon)\|x\|\qquad(x\in E).}
\]
Thus nonzero translation-invariant operators do not merely fail to be compact:
they almost attain their full norm while being bounded below on an explicitly
complemented classical sequence subspace.

## Proof

Fix \(\varepsilon>0\). Finitely supported vectors are dense in \(X\), so choose
a finitely supported unit vector \(u\) such that, with \(y=Tu\),
\[
\|y\|>\|T\|-\varepsilon/4.
\]
Write \(A=\operatorname{supp}u\). Choose positive numbers \(\delta_k\downarrow0\)
and finite sets \(F_k\subset G\) such that
\[
\|y-y\mathbf 1_{F_k}\|\le\delta_k.
\]
The sequence \((\delta_k)\) is chosen so that its relevant error norm is smaller
than \(\varepsilon/4\): use \(\sup_k\delta_k\) for \(p=1\), its \(\ell_q\)-norm
for \(1<p<\infty\), where \(q=p/(p-1)\), and its \(\ell_1\)-norm for \(c_0\).

Inductively choose \(g_k\in G\) so that the finite sets
\[
g_kA\quad\text{are pairwise disjoint},\qquad
g_kF_k\quad\text{are pairwise disjoint}.
\]
At each stage only finitely many group elements are forbidden, while \(G\) is
infinite. Put
\[
u_k=L_{g_k}u,\qquad y_k=Tu_k=L_{g_k}y,
\qquad v_k=y_k\mathbf 1_{g_kF_k}.
\]
Then the \(u_k\) have pairwise disjoint supports, the \(v_k\) have pairwise
disjoint supports, and
\[
\|y_k-v_k\|\le\delta_k,
\qquad
\|v_k\|\ge\|y\|-\delta_k.
\]
Hence, for every finitely supported scalar sequence \((a_k)\), disjointness gives
\[
\left\|\sum_k a_kv_k\right\|
\ge (\|y\|-\sup_k\delta_k)\|(a_k)\|,
\]
where the scalar norm is \(\ell_p\) or \(c_0\), as appropriate. Also
\[
\left\|\sum_k a_k(y_k-v_k)\right\|
\le\sum_k |a_k|\delta_k.
\]
For \(p=1\) this is bounded by
\(\sup_k\delta_k\,\|(a_k)\|_1\); for \(1<p<\infty\), Hölder gives
\(\|(\delta_k)\|_q\|(a_k)\|_p\); and for \(c_0\) it is bounded by
\(\sum_k\delta_k\,\|(a_k)\|_\infty\). With the preceding choices,
\[
\left\|T\sum_k a_ku_k\right\|
\ge(\|T\|-\varepsilon)\left\|\sum_k a_ku_k\right\|.
\]
Thus \(E=\overline{\operatorname{span}}\{u_k\}\) is the required lower-bound
subspace.

The complementability assertion is explicit. Choose a norm-one functional
\(\varphi\) on the finite-dimensional coordinate space supported on \(A\) with
\(\varphi(u)=1\), translate it to functionals \(\varphi_k\) supported on
\(g_kA\), and define
\[
Px=\sum_k\varphi_k(x\mathbf 1_{g_kA})u_k.
\]
For \(\ell_p\), disjointness gives \(\|Px\|_p\le\|x\|_p\). For \(c_0\), the
coefficients tend to zero because the supports \(g_kA\) are disjoint and
\(x\in c_0(G)\), and again \(\|Px\|_\infty\le\|x\|_\infty\). Since \(P|_E=I_E\),
\(P\) is a norm-one projection onto \(E\).

Now let \(S\in\mathcal{SS}(X)\). Since \(E\) is infinite-dimensional,
\(S|_E\) is not bounded below. Hence for every \(\eta>0\) there is a unit
\(x\in E\) with \(\|Sx\|<\eta\), and therefore
\[
\|T-S\|\ge\|(T-S)x\|\ge\|Tx\|-\|Sx\|
>\|T\|-\varepsilon-\eta.
\]
Letting \(\varepsilon,\eta\downarrow0\) gives
\(\operatorname{dist}(T,\mathcal{SS})=\|T\|\). Since
\[
\mathcal K(X)\subset\mathcal{FSS}(X)\subset\mathcal{SS}(X)
\]
and the zero operator belongs to all three ideals, all three distance formulas
follow.

The approximation-number identity follows immediately because every rank
\(<n\) operator is compact. The Bernstein identity follows by taking arbitrary
\(n\)-dimensional subspaces of \(E\). For the Gelfand numbers, if
\(\operatorname{codim}M<n\), then \(E\cap M\) is infinite-dimensional; hence
\(\|T|_M\|\ge\|T\|-\varepsilon\). Letting \(\varepsilon\downarrow0\) yields
\(c_n(T)=\|T\|\).

For the Kolmogorov numbers, fix a finite-dimensional \(N\subset X\) and
\(\eta,\delta>0\). Finite-dimensional compactness of the unit sphere gives a
finite \(H\subset G\) such that
\[
\|z\mathbf1_{G\setminus H}\|\le\delta\|z\|
\qquad(z\in N).
\]
Choose finite \(F\subset G\) with
\(\|y-y\mathbf1_F\|\le\eta\), and choose \(g\in G\) with \(gF\cap H=\varnothing\).
For \(d=\|L_gy-z\|\), \(z\in N\), restriction to \(gF\) gives
\[
d\ge\|y\mathbf1_F\|-\delta\|z\|.
\]
Since \(\|z\|\le\|y\|+d\),
\[
(1+\delta)d\ge\|y\mathbf1_F\|-\delta\|y\|.
\]
Letting \(\eta,\delta\downarrow0\) shows
\(\|Q_NT\|\ge\|y\|\). Taking the infimum over all
\(\dim N<n\), then choosing \(u\) increasingly norming, gives
\(d_n(T)=\|T\|\).

## Literature context and originality boundary

Crombez and Govaerts studied compact convolution operators between \(L_p(G)\)
spaces in 1978, and in 1980 studied compactness, weak compactness and strict
singularity for convolution-type maps from \(\ell_1\) to \(\ell_\infty\). Finol
(1986) studied strict singularity and translation-invariant operators between
Orlicz sequence spaces, particularly in cross-space settings.

The closest modern result located is Karlovych--Shargorodsky (2024). They prove
that, under mild target-space conditions, translation-invariant operators between
translation-invariant Banach sequence spaces on \(\mathbb Z^d\) are maximally
noncompact: their operator norm equals their Hausdorff measure of noncompactness.
Their result therefore already covers the essential-norm/maximal-noncompactness
phenomenon in a substantially broader \(\mathbb Z^d\) setting. **No novelty is
claimed here for essential-norm equality or maximal noncompactness by itself.**

The present contribution is the stronger same-space statement, for
\(\ell_p(G)\) and \(c_0(G)\) over arbitrary infinite discrete groups, that all
four finite-index numbers \(a_n,b_n,c_n,d_n\) are exactly flat at \(\|T\|\),
together with the exact distances to the compact, finitely strictly singular and
strictly singular ideals and the explicit 1-complemented almost-norming witness.
To the best of our knowledge, this combined quantitative statement was not located
in the literature checked.

Edmunds--Lang (2025) emphasize that maximal noncompactness and ordinary
approximation-type quantities do not by themselves capture the finer structure
measured by Bernstein numbers and strict singularity; this is precisely the extra
boundary resolved here for the translation-invariant sequence-space class.

## Limitations

The result is restricted to same-space operators on \(\ell_p(G)\),
\(1\le p<\infty\), and \(c_0(G)\). It does not cover \(\ell_\infty(G)\), where
finite-support density fails, nor does it classify cross-space translation-invariant
operators. It does not assume or assert that every such operator is convolution by
an \(\ell_1\) kernel.

Originality is to the best of our knowledge. The full text of the 2024
Karlovych--Shargorodsky article could not be exhaustively inspected in the available
source trail, although its bibliographic abstract clearly establishes the
maximal-noncompactness theorem described above. Consequently, an equivalent
stronger formulation inside that paper remains a material residual risk. Older
multiplier monographs and Fredholm/local-spectral treatments of translation-invariant
operators are an additional residual source of equivalent reformulations.

## References

1. G. Crombez and W. Govaerts, *Compact convolution operators between
   \(L_p(G)\)-spaces*, Colloquium Mathematicum 39 (1978), 325--329.
   https://doi.org/10.4064/cm-39-2-325-329
2. G. Crombez and W. Govaerts, *Towards a Classification of Convolution-Type
   Operators From l1 to linfinity*, Canadian Mathematical Bulletin 23 (1980),
   413--419. https://doi.org/10.4153/CMB-1980-060-4
3. C. E. Finol, *On dilation functions and some applications*, Publicationes
   Mathematicae Debrecen 33 (1986), 307--322.
   https://doi.org/10.5486/PMD.1986.33.3-4.15
4. O. Karlovych and E. Shargorodsky, *Discrete Riesz transforms on
   rearrangement-invariant Banach sequence spaces and maximally noncompact
   operators*, Pure and Applied Functional Analysis 9 (2024), 195--210.
   https://kclpure.kcl.ac.uk/portal/en/publications/discrete-riesz-transforms-on-rearrangement-invariant-banach-seque/
5. D. E. Edmunds and J. Lang, *Notes on Non-Compact Maps and the Importance of
   Bernstein Numbers*, arXiv:2503.19600 (2025).
   https://arxiv.org/abs/2503.19600
