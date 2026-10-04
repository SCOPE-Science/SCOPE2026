# Sharp operator-span capacity of two-sparse multi-window Gabor systems

## Finding
Let \(N\ge 2\), write \(\mathbb Z_N=\mathbb Z/N\mathbb Z\), and let \(T_a,M_b\) be the standard translation and modulation operators on \(\mathbb C^N\). For \(s\) unit vectors \(g_1,\ldots,g_s\), consider all rank-one projectors
\[
P_{r,a,b}=(M_bT_ag_r)(M_bT_ag_r)^*,\qquad 1\le r\le s,\quad a,b\in\mathbb Z_N.
\]
Assume every window has exactly two nonzero coordinates. Then
\[
\max_{g_1,\ldots,g_s}\dim_{\mathbb C}\operatorname{{span}}\{{P_{r,a,b}\}}
=N\min\{{N,1+2s\}}.
\]
In particular, the projectors span \(M_N(\mathbb C)\) if and only if a suitable choice of exactly two-sparse windows exists with \(s\ge\lfloor N/2\rfloor\). Thus the exact minimum sparse-window budget for quantum injectivity is \(\lfloor N/2\rfloor\).

## Assumptions and scope
The ambient group is the cyclic group \(\mathbb Z_N\), the Gabor orbit is full in both translation and modulation, and the operator span is the complex linear span of the associated rank-one projectors. A window is exactly two-sparse when its support has cardinality two. Quantum injectivity here means that the rank-one projectors span the full matrix algebra, equivalently that measurements against them distinguish all matrices and hence all quantum states. No claim is made for partial time-frequency lattices, higher support sizes, or noncyclic groups.

## Proof
Put \(W_{a,b}=M_bT_a\). The Weyl matrices \(\{{W_{a,b}:a,b\in\mathbb Z_N\}}\) form an orthogonal basis of \(M_N(\mathbb C)\). If \(P_g=gg^*\), expand \(P_g\) in this Weyl basis. The coefficient of \(W_{a,b}\) is, up to a fixed nonzero normalization and conjugation, the ambiguity coefficient
\[
A_g(a,b)=\langle g,M_bT_ag\rangle.
\]
Conjugation by another Weyl operator multiplies \(W_{a,b}\) by a character of \(\mathbb Z_N^2\). Taking the two-dimensional discrete Fourier transform of the orbit \(\{{W_{x,y}P_gW_{x,y}^*\}}\) therefore isolates each Weyl component separately. For several windows this gives the exact identity
\[
\dim_{\mathbb C}\operatorname{{span}}\{{P_{r,a,b}\}}
=\#\Bigl\{(a,b):A_{g_r}(a,b)\ne0\text{{ for at least one }}r\Bigr\}.
\]

Now let one window have support \(\{u,v\}\), and put \(d=v-u\ne0\). The supports of \(g\) and \(T_ag\) intersect only when
\[
a\in\{0,d,-d\}.
\]
Hence its ambiguity function can be nonzero on at most three translation rows, or only two rows when \(d=N/2\) is self-inverse. For \(s\) windows, the union of possible nonzero translation rows therefore has size at most \(1+2s\), and of course at most \(N\). Each row contains \(N\) modulation coordinates, so
\[
\dim_{\mathbb C}\operatorname{{span}}\{{P_{r,a,b}\}}
\le N\min\{N,1+2s\}.
\]

It remains to attain the bound. For every non-antipodal difference \(d\), use
\[
g_d=\frac{e_0+2e_d}{\sqrt5}.
\]
With \(\omega=e^{2\pi i/N}\), its zero-translation ambiguity values have the form
\[
A_{g_d}(0,b)=\frac{1+4\omega^{bd}}5,
\]
which never vanish because the two summands have unequal moduli. On each of the translation rows \(a=d\) and \(a=-d\), the overlap consists of a single coordinate, so every modulation coefficient is nonzero. Thus distinct unoriented non-antipodal differences contribute two new complete translation rows apiece.

For odd \(N\), there are exactly \((N-1)/2\) such difference classes, so taking any \(s\) of them realizes \(N(1+2s)\) until full rank is reached. For even \(N\), there are \(N/2-1\) non-antipodal classes. After using them, add the antipodal window
\[
g_{N/2}=\frac{e_0+2e^{i\pi/4}e_{N/2}}{\sqrt5}.
\]
For \(a=N/2\), its ambiguity coefficient is proportional to
\[
2e^{i\pi/4}+(-1)^b2e^{-i\pi/4},
\]
which is nonzero for both parities of \(b\). Its zero-translation row is also nonzero because \(1+4(-1)^b\ne0\). Therefore the antipodal row supplies the final missing translation row, giving full dimension \(N^2\). Additional two-sparse windows cannot enlarge the matrix algebra, so the formula holds for every \(s\ge1\).

Finally, full dimension requires \(1+2s\ge N\), hence \(s\ge\lceil(N-1)/2\rceil=\lfloor N/2\rfloor\), and the constructions above attain this bound.

## Verification
The bundled program `artifacts/verify.py` independently evaluates the ambiguity functions of the displayed windows for all \(2\le N\le20\) and every tested window budget through the injective threshold. It also directly forms all Gabor rank-one projectors and numerically checks their matrix-span ranks for \(2\le N\le10\). Finally, for \(2\le N\le9\), it exhausts all collections of support pairs and verifies the sharp maximum number \(\min\{N,1+2s\}\) of translation rows. The replay prints `VERIFY_OK ambiguity_cases=119 projector_rank_cases=34 exhaustive_support_N=2..9`.

The finite replay is only a consistency check. The theorem for arbitrary \(N\) and \(s\) is the analytic Weyl-decomposition and difference-row argument above.

## Relationship to prior work
Goldberger, Kang, and Okoudjou characterize a single full Gabor POVM by the nonvanishing of all ambiguity coefficients and compute the rank of its projector Gramian from the number of nonzero ambiguity coefficients. Their paper also records the possible ranks for a single two-sparse window. It does not state a multi-window sparse capacity law or optimize the joint operator span over a fixed number of sparse windows.

Han, Hu, Liu, and Wang study quantum injectivity of full multi-window Gabor frames and give a necessary and sufficient condition in terms of simultaneous zeros of the window ambiguity functions. The readable abstract and later literature describing their result establish that framework, but the inspected lawful open-access sources did not provide the full article text. The present result goes beyond the yes/no injectivity criterion by determining the exact maximum operator-span dimension at every two-sparse window budget and by giving sharp extremizers.

Salanevich studies multi-window Gabor phase retrieval and explicitly summarizes the Han--Hu--Liu--Wang simultaneous-nonvanishing criterion while pursuing reduced phaseless measurement counts. That work concerns pure-state phase retrieval rather than the exact matrix-span capacity of full Gabor orbits with two-sparse windows.

## Limitations
The result is specific to exactly two-sparse windows and full cyclic Gabor orbits. The optimal capacity for support size three or larger is not determined here. The full text of the 2022 Han--Hu--Liu--Wang article was not available through the lawful open-access sources inspected, so there remains a residual priority risk that one of its examples contains a related sparse special case; its abstract and later summaries do not state the rank-capacity theorem above. No independent audit has been performed.

## References
1. A. Goldberger, S. Kang, K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509, first posted 2021-06-02; later published in *Linear and Multilinear Algebra*, DOI 10.1080/03081087.2021.1998308.
2. D. Han, Q. Hu, R. Liu, H. Wang, *Quantum injectivity of multi-window Gabor frames in finite dimensions*, *Annals of Functional Analysis* 13 (2022), article 59, DOI 10.1007/s43034-022-00208-2; first online 2022-08-05.
3. P. Salanevich, *Injectivity of Multi-window Gabor Phase Retrieval*, arXiv:2307.00834, first posted 2023-07-03.
