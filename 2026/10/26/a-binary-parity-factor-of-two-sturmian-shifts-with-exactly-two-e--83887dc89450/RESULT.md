# A binary parity factor of two Sturmian shifts with exactly two exceptional ambiguity orbits

## Finding
Let \(0<\alpha,\beta<1\) be such that \(1,\alpha,\beta\) are linearly independent over \(\mathbb Q\). Let \(X_\alpha,X_\beta\) be the bilateral Sturmian subshifts of slopes \(\alpha,\beta\). Define the one-block parity factor
\[
\Pi:X_\alpha\times X_\beta\longrightarrow Y_{\alpha,\beta},\qquad
\Pi(u,v)_n=u_n\oplus v_n\quad(n\in\mathbb Z),
\]
where \(\oplus\) is addition modulo two and \(Y_{\alpha,\beta}\) is the image subshift.

**Theorem.** The parity factor is one-to-one over every output except exactly two distinct shift orbits. Its fibres over each of these two orbits have cardinality two. Explicitly, write \(s_{\theta,x}^{\pm}\) for the two one-sided limiting Sturmian codings at the singular phase \(x=0\), with the \(+\) and \(-\) conventions described below. The exceptional orbits are those of
\[
W^{(0)}=s_{\alpha,0}^{-}\oplus s_{\beta,0}^{-}
           =s_{\alpha,0}^{+}\oplus s_{\beta,0}^{+},
\]
and
\[
W^{(1)}=s_{\alpha,0}^{-}\oplus s_{\beta,0}^{+}
           =s_{\alpha,0}^{+}\oplus s_{\beta,0}^{-}.
\]
They are different, and every two-element fibre is a shift of one of the displayed equalities.

Moreover, the **two one-sided Fourier averages of the binary output determine both rotation phases**. For \(w=\Pi(u,v)\), put \(W_n=(-1)^{w_n}\) and
\[
A_\theta(w)=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}W_n e^{-2\pi i n\theta}
\quad(\theta\in\{\alpha,\beta\}).
\]
These limits exist for every \(w\in Y_{\alpha,\beta}\). If \((x,y)\in\mathbb T^2\) are the underlying phases of \((u,v)\), then
\[
A_\alpha(w)=\frac{1-e^{2\pi i\alpha}}{\pi i}(1-2\beta)e^{2\pi i x},\qquad
A_\beta(w)=(1-2\alpha)\frac{1-e^{2\pi i\beta}}{\pi i}e^{2\pi i y}.
\]
Both prefactors are nonzero, so each phase is uniquely reconstructed by division. The resulting binary subshift is minimal and uniquely ergodic and is measure-theoretically isomorphic to translation by \((\alpha,\beta)\) on \(\mathbb T^2\) with Haar measure; its measure spectrum is simple and pure point, with eigenvalues \(e^{2\pi i(k\alpha+\ell\beta)}\) for \(k,\ell\in\mathbb Z\).

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/\mathbb Z\). For irrational \(\theta\in(0,1)\), ordinary mechanical codings are
\[
s_{\theta,x}(n)=\lfloor x+(n+1)\theta\rfloor-\lfloor x+n\theta\rfloor,
\quad n\in\mathbb Z.
\]
The subshift \(X_\theta\subset\{0,1\}^{\mathbb Z}\) is the shift-orbit closure of all these codings. At a singular phase \(x\equiv-j\theta\pmod1\), both limits obtained by approaching the phase from the two sides occur in this closure and disagree exactly at the two sites \(j-1,j\). At a nonsingular phase the coding is unique. The labels \(+\) and \(-\) refer to the two limits of the phase approaching zero from above or below, respectively. The theorem concerns the bilateral product with simultaneous shift, and relies on **joint rational independence**, not merely on the irrationality of each slope.

## Proof
**1. Sturmian phase fibres.** For each \(\theta\), the mechanical coding partitions the circle at \(0\) and \(1-\theta\). Along an irrational orbit these discontinuities can be encountered at only two consecutive observation times. If \(x+j\theta\equiv0\), the two phase limits differ only in positions \(j-1,j\), where the ordered pair is interchanged \(01\leftrightarrow10\). Otherwise they coincide. Every sequence in \(X_\theta\) arises from some phase and one of these choices, by compactness and the phase-interval construction. To see that the phase is intrinsic, set \(g_\theta(t)=1-2\mathbf1_{[1-\theta,1)}(t)\). For a coding of phase \(x\), the signs \((-1)^{s_{\theta,x}(n)}\) equal \(g_\theta(x+n\theta)\), except for at most two sites in a boundary convention. Uniform distribution of irrational rotations for bounded Riemann-integrable functions gives
\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}(-1)^{u_n}e^{-2\pi i n\theta}
=e^{2\pi i x}\,\widehat g_\theta(1),
\qquad
\widehat g_\theta(1)=\frac{1-e^{2\pi i\theta}}{\pi i}\ne0.
\]
Thus no two different circle phases can produce the same Sturmian sequence.

**2. Recovering both phases from parity.** For any \(u,v\) with phases \(x,y\), the parity signs satisfy \(W_n=(-1)^{u_n}(-1)^{v_n}\). Away from finitely many boundary indices they equal \(g_\alpha(x+n\alpha)g_\beta(y+n\beta)\). Kronecker equidistribution for the totally irrational torus rotation implies convergence of the two twisted averages. At frequency \(\alpha\), integration of the \(x\)-coordinate's first Fourier mode and the \(y\)-coordinate's constant mode gives
\[
A_\alpha=e^{2\pi i x}\widehat g_\alpha(1)\widehat g_\beta(0).
\]
The symmetric identity gives \(A_\beta\). Direct integration yields \(\widehat g_\theta(0)=1-2\theta\), and the formulas in the finding follow. As neither irrational slope equals \(1/2\), no prefactor vanishes. In particular equal outputs force equal phases in both input coordinates.

**3. Exhausting the fibres.** Fix the two phases reconstructed in step 2. Each input coordinate has one or two possible Sturmian labels. Changing the chosen label at a singular phase indexed by \(j\) flips precisely the binary positions \(j-1,j\). Therefore, two input pairs give the same parity sequence if and only if they differ in both coordinates and their singular indices are the same. This happens precisely at the phase pairs \((x,y)=(-j\alpha,-j\beta)\) modulo one. At each such phase pair, the four labeled pairs split into two parity-equivalence classes of size two. At \(j=0\) these are the two displayed classes; varying \(j\) shifts them. Their outputs differ at precisely the sites \(-1,0\) and hence are distinct. They cannot lie in the same shift orbit: a shift identifying them would have to return the recovered phase pair to itself, impossible for any nonzero shift by joint rational independence. All other output fibres are singletons.

**4. Dynamical consequences.** Every nonempty cylinder of each Sturmian subshift contains codings associated with an open interval of phases. The product rotation has dense orbits, so simultaneous shifts reach every pair of such cylinders. Thus the product shift and its parity factor are minimal. Any invariant probability on the product pushes forward under the phase map to invariant Haar measure of the uniquely ergodic torus translation. Outside the two countable singular-phase orbits of each coordinate, the phase coding is one-to-one; hence the pushforward determines a unique invariant measure. The product and its parity factor are uniquely ergodic. Since their phase and parity maps are one-to-one outside null sets, the binary factor is measure-isomorphic to Haar torus translation. The Fourier character basis of \(\mathbb T^2\) gives the asserted simple pure-point spectrum.

## Verification
The standalone `verify.py` checks the two exceptional XOR identities and their distinct cross-pair output on 101 exact-indexed sites. It also averages 30,000 symbols at the two fundamental frequencies for the rationally independent example \(\alpha=\sqrt2-1\), \(\beta=\sqrt3-1\), with phases \((0.19,0.37)\); the observed complex-phase errors are under \(0.006\). These finite computations illustrate the identities and Fourier recovery only; they are not used to infer uniqueness for arbitrarily long words or all slopes. The proof above supplies the unrestricted result.

## Relationship to prior work
Bédaride (arXiv:1205.5093, 2012) classifies complexity functions for torus translations coded by the three-letter cube-billiard partition. That coding, its complexity invariant, and the conclusions of its Theorem 3.1 are different from the two-letter checkerboard parity factor and its exact finite fibre classification here. Frid and Jamet (arXiv:1302.3722, 2013) count binary *single-circle* rotation words, and derive combinatorial identities for two Sturmian codings with a shared rotation slope; those identities do not imply phase reconstruction and exceptional-fibre classification for two rationally independent slopes. General finite-generator existence theorems alone provide neither the explicit two-frequency inversion nor the two exceptional orbits. The proof deliberately claims no new theorem about one-dimensional Sturmian complexity, general billiard complexity, or hidden Markov processes.

## Limitations
The theorem fixes and assumes known slopes \(\alpha,\beta\), and excludes rational dependence among \(1,\alpha,\beta\). It is an exact noiseless full-sequence theorem, not a finite-sample stability bound. A binary output may have two ordered Sturmian predecessors at the two specified output orbits, though its torus phase remains unique. Numerical finite-block complexity patterns are **not** asserted as infinite theorems. The work has not undergone independent expert review. Historical coverage of this particular parity factor in unindexed literature cannot be excluded.

## References
- N. Bédaride, *Classification of rotations on the torus* \(\mathbb T^2\), arXiv:1205.5093v1, first publicly posted 2012-05-23, https://arxiv.org/abs/1205.5093.
- A. Frid and D. Jamet, *The number of binary rotation words*, arXiv:1302.3722v1, first publicly posted 2013-02-15, https://arxiv.org/abs/1302.3722.
- J. Berstel and L. Vuillon, *Coding rotations on intervals*, Theoretical Computer Science 281 (2002), 99–107, DOI 10.1016/S0304-3975(02)00009-9 (related same-slope interval-coding literature).
