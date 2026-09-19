# Amplitude-free universal completeness for irrational-rotation quasicrystals

## Result

Let \(\alpha\in\mathbb R\setminus\mathbb Q\) and \(\beta\in\mathbb R\setminus\{0\}\) satisfy the nonresonance condition
\[
\alpha+\beta^{-1}\notin\mathbb Q.
\]
Define the centered irrational-rotation perturbation
\[
\lambda_n=n+\beta\left(\{n\alpha\}-\frac12\right),\qquad n\in\mathbb Z,
\]
and
\[
\Lambda_{\alpha,\beta}=\{\lambda_n:n\in\mathbb Z\}.
\]
Then \(\Lambda_{\alpha,\beta}\) is uniformly discrete, has uniform density one, and has the following universal uniqueness property:

> For every measurable \(S\subset\mathbb R\) with \(|S|<1\), if \(f\in L^1(S)\) and
> \[
> \int_{\mathbb R}f(t)e^{2\pi i\lambda t}\,dt=0\qquad(\lambda\in\Lambda_{\alpha,\beta}),
> \]
> then \(f=0\) almost everywhere.

Consequently, for every \(1\le p<\infty\), the exponential system
\[
E(\Lambda_{\alpha,\beta})=\{e^{2\pi i\lambda x}:\lambda\in\Lambda_{\alpha,\beta}\}
\]
is complete in \(L^p(S)\) for every measurable \(S\subset\mathbb R\) of measure less than one.

The directly relevant result of Bertolini--Florit-Simon--Liehr--Taylor, *Universal completeness of exponentials* (arXiv:2609.20805), proves this construction under a small-amplitude hypothesis. Its one-dimensional main theorem assumes rational \(\beta\) with \(0<|\beta|<1/2\), while its higher-dimensional formulation, specialized to one dimension, allows real \(\beta\) with the same nonresonance condition but still requires \(|\beta|<1/2\). The theorem above removes the amplitude restriction completely in dimension one.

In particular, for every irrational \(\alpha\) and every nonzero rational \(\beta\), the conclusion holds with no restriction on \(|\beta|\). More generally, for fixed irrational \(\alpha\), it holds for every nonzero real \(\beta\) outside the countable resonant set
\[
\left\{\frac1{q-\alpha}:q\in\mathbb Q\right\}.
\]

## Uniform discreteness without a small-amplitude hypothesis

Put \(a_d=\{d\alpha\}\) for \(d\ge1\). If \(m\in\mathbb Z\), then
\[
\{(m+d)\alpha\}-\{m\alpha\}\in\{a_d,a_d-1\}.
\]
Hence every difference \(\lambda_{m+d}-\lambda_m\) is one of
\[
A_d=d+\beta a_d,
\qquad
B_d=d-\beta(1-a_d).
\]
Neither number can vanish. Indeed,
\[
A_d=0\implies
\alpha+\beta^{-1}=\frac{\lfloor d\alpha\rfloor}{d}\in\mathbb Q,
\]
while
\[
B_d=0\implies
\alpha+\beta^{-1}=\frac{\lfloor d\alpha\rfloor+1}{d}\in\mathbb Q.
\]
Both contradict nonresonance.

Moreover,
\[
|A_d|,|B_d|\ge d-|\beta|.
\]
Thus all \(d>|\beta|+1\) give a gap greater than one, while only finitely many positive \(d\) remain. Since their corresponding \(A_d,B_d\) are nonzero, their absolute values have a positive minimum. This proves uniform discreteness.

Also
\[
|\lambda_n-n|\le\frac{|\beta|}{2}.
\]
Because the indexing is injective, bounded displacement gives, uniformly in \(x\),
\[
\#\bigl(\Lambda_{\alpha,\beta}\cap[x,x+R]\bigr)=R+O_\beta(1).
\]
Hence \(D(\Lambda_{\alpha,\beta})=1\). No order-preserving assumption on \(n\mapsto\lambda_n\) is needed.

## The Fourier identity is amplitude-free

Let \(f\in L^1(S)\) satisfy the vanishing conditions. As in arXiv:2609.20805, decompose \(f\) into its unit-interval pieces \(f_j\), \(j\in\mathbb Z\), so that
\[
\sum_j\|f_j\|_1=\|f\|_1,
\qquad
\sum_j|\{f_j\ne0\}|\le |S|<1.
\]
The proof uses the Fourier expansion
\[
e^{2\pi i a(y-1/2)}
=
\sum_{\ell\in\mathbb Z}
\frac{\sin(\pi a)}{\pi(a-\ell)}e^{2\pi i\ell y},
\qquad 0<y<1.
\]
The crucial absolute-convergence estimate for the differenced coefficients is
\[
\sum_{\ell\in\mathbb Z}
\left|
\frac{\sin(\pi a)}{\pi}
\left(\frac1{a-\ell+k}-\frac1{a-\ell}\right)
\right|
\le C_k,
\]
and it holds uniformly for every real \(a\). Therefore the Fourier-identity part of the argument applies to arbitrary fixed real \(\beta\), with no smallness assumption.

For almost every \(x\in[0,1)\), introduce the meromorphic series
\[
M_z(x)=\sum_{j,\ell\in\mathbb Z}r_{\ell,j}
\left(\frac1{z-p_{\ell,j}}+\frac1{p_{\ell,j}}\right),
\]
where
\[
p_{\ell,j}=\ell-\beta(\{x-\ell\alpha\}+j),
\]
\[
r_{\ell,j}=
\frac{\sin\!\bigl(\pi\beta(\{x-\ell\alpha\}+j)\bigr)}{\pi}
 f_j(\{x-\ell\alpha\}).
\]
The Fourier identity gives
\[
M_k(x)=0\qquad(k\in\mathbb Z).
\]
It remains to check that the meromorphic-function argument survives when \(|\beta|\) is arbitrary. Within this meromorphic stage, the small-amplitude hypothesis is used through bounded-distance and exceptional-set estimates; both admit finite-amplitude replacements. Uniform discreteness, handled separately above, is supplied by nonresonance.

## Poles: bounded displacement replaces the \(1/2\) bound

For fixed \((j,\ell)\), the condition
\[
\beta(\{x-\ell\alpha\}+j)\in\mathbb Z
\]
has only finitely many solutions \(x\in[0,1)\), because its left-hand side ranges through a bounded interval. After discarding the countable union of these finite exceptional sets, every nonzero residue corresponds to a genuine pole and no pole lies in \(\mathbb Z\).

Set
\[
q_{\ell,j}=\ell-\lfloor\beta j\rfloor\in\mathbb Z.
\]
Then
\[
p_{\ell,j}-q_{\ell,j}
=
\lfloor\beta j\rfloor-\beta j
-
\beta\{x-\ell\alpha\},
\]
so
\[
|p_{\ell,j}-q_{\ell,j}|\le 1+|\beta|.
\]
Consequently
\[
1+p_{\ell,j}^2\asymp_\beta 1+q_{\ell,j}^2.
\]
The reparametrization \((j,\ell)\leftrightarrow(j,q)\),
\[
\ell=\lfloor\beta j\rfloor+q,
\]
is still a bijection. Since \(|r_{\ell,j}|\le |f_j(\{x-\ell\alpha\})|/\pi\), Fubini therefore gives
\[
\sum_{j,\ell}
\frac{|r_{\ell,j}|}{1+p_{\ell,j}^2}<\infty
\]
for almost every \(x\), exactly as in the small-amplitude proof, with constants now allowed to depend on \(\beta\).

The poles are also pairwise distinct. If
\[
p_{\ell,j}=p_{\ell',j'},
\]
then, with \(d=\ell-\ell'\), the difference of the two fractional parts differs from \(-d\alpha\) by an integer. Hence
\[
d(\alpha+\beta^{-1})\in\mathbb Z.
\]
Nonresonance forces \(d=0\), and then \(j=j'\).

Thus the pole set is real, simple and locally finite.

## Pole density is unchanged

For \(\ell=\lfloor\beta j\rfloor+q\), the pole \(p_{\ell,j}\) lies within the fixed distance \(1+|\beta|\) of the integer \(q\). The number of poles associated with a fixed \(q\) is
\[
\varphi(\{x-q\alpha\}),
\]
where
\[
\varphi(t)=
\sum_{j\in\mathbb Z}
\mathbf 1_{\{f_j\ne0\}}
\bigl(\{t-\lfloor\beta j\rfloor\alpha\}\bigr).
\]
This function is integrable and
\[
\int_0^1\varphi(t)\,dt
=
\sum_j|\{f_j\ne0\}|
\le |S|.
\]
The pointwise ergodic theorem for the irrational rotation by \(\alpha\) therefore yields
\[
\limsup_{R\to\infty}
\frac{\#\{\text{poles of }M_z(x):|z|\le R\}}{2R}
\le |S|<1
\]
for almost every \(x\). Replacing a fixed displacement bound \(3/2\) by \(1+|\beta|\) changes only an \(O_\beta(1)\) boundary count and hence does not affect this normalized density.

On the other hand, all integers are zeros of \(M_z(x)\), so if the meromorphic function is not identically zero then its zeros have lower density at least one. The weighted pole summability above gives the same logarithmic circular-mean growth estimate as in the source proof,
\[
\int_0^{2\pi}\log|M_{Re^{i\theta}}(x)|\,d\theta=O_x(\log R).
\]
Jensen's formula then forces the lower density of zeros not to exceed the upper density of poles. This contradicts
\[
1\le D_-(\text{zeros})
\le D_+(\text{poles})
\le |S|<1.
\]
Therefore \(M_z(x)\equiv0\) for almost every \(x\), so all \(f_j(x)\) vanish and hence \(f=0\) almost everywhere.

The \(L^p\)-completeness statement follows by Hahn--Banach, since every dual annihilator on a finite-measure set lies in \(L^1(S)\).

## Relation to prior literature and originality

The strongest directly relevant statement located is Section 6 of Bertolini--Florit-Simon--Liehr--Taylor (arXiv:2609.20805): in dimension one it permits real \(\beta\) under the same arithmetic nonresonance condition, but retains \(|\beta|<1/2\). Their detailed one-dimensional proof uses the smallness assumption to bound how far the auxiliary poles lie from integers and to say that a certain integer-valued exceptional condition occurs at most once; the argument above shows that only a finite bound is required in both places.

Earlier work of Matei--Meyer and Grepstad--Lev studies simple quasicrystals as stable or universal sampling sets for compact spectra and related bounded-remainder-set problems. Olevskii--Ulanovskii established universal sampling/completeness phenomena by different constructions. None of the located statements gives the amplitude-free arbitrary-measurable-spectrum theorem for this explicit irrational-rotation family.

Searches using arXiv:2609.20805, the formula \(n+\beta(\{n\alpha\}-1/2)\), the nonresonance condition \(\alpha+1/\beta\notin\mathbb Q\), and combinations of “universal completeness”, “simple quasicrystal”, “irrational rotation”, and “arbitrary amplitude” located no equivalent result or follow-up removing the smallness hypothesis. To the best of our knowledge, the amplitude-free one-dimensional theorem above is new. The source preprint is very recent, so an unindexed contemporaneous observation remains a residual originality risk.

## Limitations

The result is one-dimensional. It does not remove the small-norm hypothesis from the higher-dimensional theorem, treat the resonant parameters \(\alpha+1/\beta\in\mathbb Q\), address the critical case \(|S|=1\), or provide stable sampling/frame bounds. The separation constant is positive for each fixed nonresonant \((\alpha,\beta)\), but no uniform quantitative lower bound over large parameter classes is claimed. No independent validation or proof-assistant formalization of the amplitude-free extension is asserted.

## References

1. S. Bertolini, E. Florit-Simon, L. Liehr, and M. A. Taylor, *Universal completeness of exponentials*, arXiv:2609.20805 (2026), https://arxiv.org/abs/2609.20805.
2. A. Olevskii and A. Ulanovskii, *Universal sampling and interpolation of band-limited signals*, Geom. Funct. Anal. 18 (2008), 1029--1052, https://doi.org/10.1007/s00039-008-0674-7.
3. B. Matei and Y. Meyer, *Quasicrystals are sets of stable sampling*, C. R. Math. Acad. Sci. Paris 346 (2008), 1235--1238, https://doi.org/10.1016/j.crma.2008.10.006.
4. S. Grepstad and N. Lev, *Universal sampling, quasicrystals and bounded remainder sets*, C. R. Math. Acad. Sci. Paris 352 (2014), 633--638.
