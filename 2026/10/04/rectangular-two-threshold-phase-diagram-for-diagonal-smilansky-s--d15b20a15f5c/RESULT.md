# Rectangular two-threshold phase diagram for diagonal Smilansky–Solomyak contact interactions
## Finding
For the general contact-interaction Hamiltonian \(H_{\alpha,\beta,\gamma}\) of Exner and Lipovský, set \(\gamma=0\) and assume \(\alpha,\beta>0\). The two Jacobi transition parameters reduce, as an unordered pair, to
\[
\{\mu_1,\mu_2\}=
\left\{\frac{\sqrt2}{\alpha},\frac{\beta}{2\sqrt2}\right\}.
\]
Therefore
\[
\sigma_{\mathrm{ac}}(H_{\alpha,\beta,0})=
\begin{cases}
[1/2,\infty),&0<\alpha<\sqrt2,\ \beta>2\sqrt2,\\
[0,\infty),&\alpha\le\sqrt2,\ \beta\ge2\sqrt2\ \text{and}\ (\alpha=\sqrt2\ \text{or}\ \beta=2\sqrt2),\\
\mathbb R,&\alpha>\sqrt2\ \text{or}\ \beta<2\sqrt2.
\end{cases}
\]
For almost every \(E<0\), the absolutely continuous multiplicity is
\[
\mathbf 1_{\{\alpha>\sqrt2\}}+\mathbf 1_{\{\beta<2\sqrt2\}},
\]
and for almost every \(0<E<1/2\) it is
\[
\mathbf 1_{\{\alpha\ge\sqrt2\}}+\mathbf 1_{\{\beta\le2\sqrt2\}}.
\]
The two independent critical lines meet at \((\sqrt2,2\sqrt2)\). The locus \(\alpha\beta=4\) only exchanges the channel labels.

From the subcritical rectangle \(0<\alpha<\sqrt2\), \(\beta>2\sqrt2\),
\[
N_-\!\left(\frac12,H_{\alpha,\beta,0}\right)
\sim
\frac{1}{4\,2^{1/4}\sqrt{\sqrt2-\alpha}}
+
\frac{2^{1/4}}{4\sqrt{\beta-2\sqrt2}}
\]
as \((\alpha,\beta)\to(\sqrt2,2\sqrt2)\), with no restriction on the relative approach rates.

## Assumptions and scope
The claim concerns the Hamiltonian and normalization of arXiv:2207.03713v1, with \(\gamma=0\) and positive diagonal parameters \(\alpha,\beta\). The paper notes the simultaneous sign symmetry \((\alpha,\beta)\mapsto(-\alpha,-\beta)\); only the positive quadrant is stated here to keep the channel parameters positive and to apply its Theorem 6.2 exactly as written.

The eigenvalue count is \(N_-(1/2,H)\), so eigenvalues are counted with multiplicity. The asymptotic statement concerns the two-parameter limit from the open subcritical rectangle only.

## Proof
Equations (4.6a)–(4.6b) of arXiv:2207.03713v1 give, for \(\beta>0\),
\[
\mu_1=\frac{2\sqrt2\,\beta}{4+\alpha\beta+|\gamma|^2-\sqrt{(\alpha\beta+|\gamma|^2-4)^2+16|\gamma|^2}},
\]
\[
\mu_2=\frac{2\sqrt2\,\beta}{4+\alpha\beta+|\gamma|^2+\sqrt{(\alpha\beta+|\gamma|^2-4)^2+16|\gamma|^2}}.
\]
At \(\gamma=0\), the square root is \(|\alpha\beta-4|\). If \(\alpha\beta\le4\), direct substitution gives
\[
\mu_1=\frac{\sqrt2}{\alpha},\qquad
\mu_2=\frac{\beta}{2\sqrt2}.
\]
If \(\alpha\beta\ge4\), the same two values occur in the opposite order. This proves the unordered-pair identity and also shows that \(\alpha\beta=4\) is only a channel-label exchange.

Theorem 6.2 of the same paper states that one Jacobi channel contributes absolutely continuous spectrum \(\mathbb R\) when \(0<\mu<1\), contributes \([0,\infty)\) when \(\mu=1\), and contributes no absolutely continuous spectrum when \(\mu>1\). Theorem 6.3 adds the free branch \([1/2,\infty)\) and adds channel multiplicities. Since
\[
\frac{\sqrt2}{\alpha}\lessgtr1\quad\Longleftrightarrow\quad \alpha\gtrless\sqrt2,
\qquad
\frac{\beta}{2\sqrt2}\lessgtr1\quad\Longleftrightarrow\quad \beta\lessgtr2\sqrt2,
\]
the stated rectangular phase diagram and the two sub-threshold multiplicity formulas follow.

Inside the open subcritical rectangle both channel parameters exceed one. Theorem 7.2 gives
\[
\left|
N_-\!\left(\frac12,H_{\alpha,\beta,0}\right)
-
N_+\!\left(\frac{\sqrt2}{\alpha},J_0\right)
-
N_+\!\left(\frac{\beta}{2\sqrt2},J_0\right)
\right|\le2.
\]
The Jacobi asymptotic used in the proof of Theorem 7.3 is
\[
N_+(\mu,J_0)\sim\frac{1}{4\sqrt2\,\sqrt{\mu-1}}
\qquad(\mu\downarrow1).
\]
Writing \(\delta_\alpha=\sqrt2-\alpha\) and \(\delta_\beta=\beta-2\sqrt2\),
\[
\frac{\sqrt2}{\alpha}-1=\frac{\delta_\alpha}{\alpha},
\qquad
\frac{\beta}{2\sqrt2}-1=\frac{\delta_\beta}{2\sqrt2}.
\]
Hence the two channel contributions are respectively
\[
\frac{1}{4\,2^{1/4}\sqrt{\delta_\alpha}}(1+o(1)),
\qquad
\frac{2^{1/4}}{4\sqrt{\delta_\beta}}(1+o(1)).
\]
Their sum diverges for every approach to the corner from the open rectangle, so the bounded error in Theorem 7.2 is negligible and the displayed two-scale asymptotic follows without a constraint on the relative rates.

## Verification
The proof uses only exact algebra plus Theorems 6.2, 6.3, 7.2 and the Jacobi asymptotic explicitly invoked in Theorem 7.3 of the primary source. A standalone script, `verify.py`, checks the channel factorization numerically over representative parameter values and checks the two asymptotic conversion constants. The numerical checks are corroborative; the proof above is analytic.

## Relationship to prior work
The primary source, arXiv:2207.03713v1, treats the full four-real-parameter contact interaction, gives the two effective Jacobi parameters, states the general spectral transition through \(\mu_j=1\), and proves eigenvalue-count asymptotics near criticality. In the inspected text it separately identifies the pure \(\delta\) and pure \(\delta'\) axes and discusses the degenerate locus \(\gamma=0,\alpha\beta=4\), but it does not state the unordered diagonal factorization, the resulting rectangular two-parameter phase diagram, or the unrestricted two-scale bicritical corner law.

Naboko and Solomyak, arXiv:math/0504190, establish the \(\delta\)-model threshold \(\alpha=\sqrt2\). Exner and Lipovský, arXiv:1801.08304, establish the \(\delta'\)-model threshold \(\beta=2\sqrt2\). Those one-parameter results are the two coordinate thresholds recovered simultaneously here; neither treats the two-parameter diagonal contact slice.

## Limitations
This result does not classify the full \(\gamma\ne0\) phase geometry. It is a structural classification of the natural no-mixing slice \(\gamma=0\). It also does not sharpen the bounded comparison error in Theorem 7.2; that error is only shown to be asymptotically negligible at the bicritical corner.

A residual literature risk is that the diagonal factorization may have been recorded informally or under point-interaction parity terminology outside the indexed and inspected sources.

## References
1. P. Exner and J. Lipovský, *Spectral transition model with the general contact interaction*, arXiv:2207.03713v1 (2022); later published in *From Complex Analysis to Operator Theory: A Panorama*.
2. S. N. Naboko and M. Solomyak, *On the absolutely continuous spectrum in a model of an irreversible quantum graph*, arXiv:math/0504190; Proc. Lond. Math. Soc. 92 (2006), 251–272.
3. P. Exner and J. Lipovský, *Smilansky-Solomyak model with a \(\delta'\)-interaction*, arXiv:1801.08304; Phys. Lett. A 382 (2018), 1207–1213.
