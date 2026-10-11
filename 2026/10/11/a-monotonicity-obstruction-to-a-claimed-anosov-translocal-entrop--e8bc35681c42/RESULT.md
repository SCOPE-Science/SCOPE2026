# A monotonicity obstruction to a claimed Anosov translocal-entropy formula
## Finding
Biś and Bruin define upper translocal entropy by counting orbit segments that start inside an exponentially shrinking ball \(B(z,e^{-\omega n})\). Their Definition 2.1 therefore has an immediate monotonicity property: if \(\omega_2>\omega_1\), then
\[
B(z,e^{-\omega_2 n})\subseteq B(z,e^{-\omega_1 n})
\]
for every \(n\), so the corresponding separated-set count cannot increase. Hence both upper and lower translocal entropy are nonincreasing functions of \(\omega\).

Immediately after Theorem 2.2, the paper states for a bounded-distortion toral automorphism or Anosov map the formula
\[
R(\omega)=h_{\mathrm{top}}(f)-\sum_{\chi_i\ge\omega}(\chi_i-\omega),
\]
where \(\chi_i\) denotes the positive rate entering the displayed threshold and summand. This right-hand side has the opposite monotonicity: between thresholds its derivative is the number of active rates, and across a threshold it is continuous. Thus \(R\) is nondecreasing, and it is strictly increasing on every interval on which at least one positive rate remains active.

The contradiction is already exact on the classical cat map induced by
\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Its expanding eigenvalue is \(\Lambda=(3+\sqrt5)/2\), and write \(\chi=\log\Lambda\). The affine toral formula proved in Theorem 2.2 gives
\[
h_\omega(z)=(\chi-\omega)_+.
\]
Since \(h_{\mathrm{top}}(F_A)=\chi\), the claimed post-theorem extension gives, under the rate interpretation compatible with Theorem 2.2,
\[
R(\omega)=\min\{\omega,\chi\}.
\]
In particular it gives \(R(0)=0\) although Theorem 2.2 gives \(h_0(z)=\chi\), and it gives \(R(\omega)=\chi\) for \(\omega\ge\chi\) although Theorem 2.2 gives \(h_\omega(z)=0\). Therefore the bounded-distortion Anosov/toral formula stated after Theorem 2.2 is false as written.

## Assumptions and scope
The argument uses exactly the definition and notation of the source, with one notational normalization. The paper's post-theorem sentence refers to an “upper Lyapunov exponent” inside a logarithm; to compare it with the preceding affine theorem, this note writes \(\chi_i\) for the positive logarithmic expansion rates that enter the threshold and summand. The counterexample is independent of any finer convention because the cat map belongs simultaneously to the affine class covered by Theorem 2.2 and to the broader toral/Anosov class named in the disputed sentence.

No claim is made about the correct formula for a general non-affine Anosov map. The affine formula of Theorem 2.2 is used as a verified premise and is not challenged.

## Proof
Fix \(z\) and two localization rates \(0\le\omega_1<\omega_2\). For every \(n\),
\[
e^{-\omega_2 n}\le e^{-\omega_1 n},
\]
so every orbit segment counted from the smaller initial ball for \(\omega_2\) is also admissible for \(\omega_1\). Therefore, for every separation scale \(\varepsilon>0\), the maximal separated-set cardinalities satisfy
\[
N(n,\varepsilon,\omega_2,z)\le N(n,\varepsilon,\omega_1,z).
\]
Taking \(n^{-1}\log\), then the required limsup or liminf, and finally the limit as \(\varepsilon\downarrow0\), preserves the inequality. Thus translocal entropy is nonincreasing in \(\omega\).

Now fix finitely many positive rates \(\chi_i\). On any open interval containing no threshold \(\chi_i\), the active index set \(\{i:\chi_i\ge\omega\}\) is constant and
\[
R(\omega)=h_{\mathrm{top}}(f)-\sum_{\chi_i\ge\omega}\chi_i+\omega\,\#\{i:\chi_i\ge\omega\}.
\]
Hence \(R\) has nonnegative slope there, strictly positive whenever the active set is nonempty. At a threshold \(\omega=\chi_j\), the disappearing summand \(\chi_j-\omega\) is zero, so \(R\) is continuous. Therefore \(R\) is nondecreasing globally.

For the cat matrix \(A\), the characteristic polynomial is \(t^2-3t+1\), so the eigenvalues are \(\Lambda=(3+\sqrt5)/2\) and \(\Lambda^{-1}\). The source's Theorem 2.2 therefore gives
\[
h_\omega(z)=
\begin{cases}
\chi-\omega,&0\le\omega\le\chi,\\
0,&\omega\ge\chi,
\end{cases}
\qquad \chi=\log\Lambda.
\]
The same affine toral automorphism has topological entropy \(\chi\). Substitution into the disputed post-theorem formula yields
\[
R(\omega)=
\begin{cases}
\omega,&0\le\omega\le\chi,\\
\chi,&\omega\ge\chi.
\end{cases}
\]
The two functions disagree at both endpoints and have opposite monotonicity on \((0,\chi)\). Since this single map satisfies the hypotheses named by the claimed extension, it is a counterexample to that statement as written.

## Verification
The source was checked at Definition 2.1, Theorem 2.2, and the paragraph immediately following that theorem. The author-hosted preprint dated 2025-12-09 and the journal version state the same affine theorem and the same subsequent bounded-distortion extension. The monotonicity argument uses only set inclusion in the defining shrinking balls. The cat-map calculation is exact algebra: the eigenvalues are the roots of \(t^2-3t+1\), and no numerical approximation is used.

The proof establishes only a contradiction to the displayed general extension. It does not infer a replacement theorem from the counterexample, and it does not use a finite experiment to support an infinite assertion.

## Relationship to prior work
The motivating paper proves an exact affine toral formula in Theorem 2.2 and then asserts a different-looking formula for bounded-distortion toral automorphisms or Anosov maps. The present finding compares those two statements on an object lying in both classes and combines that comparison with the monotonicity forced by Definition 2.1.

Targeted searches for the title, DOI, translocal entropy, bounded distortion, Anosov formulations, Lyapunov formulations, cat-map specializations, corrections, errata, and equivalent monotonicity objections did not locate a published correction or an implication-equivalent result. The closest retrieved entropy and Lyapunov records concern different invariants and do not cover this contradiction.

## Limitations
The conclusion is deliberately narrow: the post-Theorem-2.2 bounded-distortion formula is false as written. The argument does not determine whether a sign, complement, normalization, or larger reformulation gives the intended general theorem. It also does not challenge the affine formula proved in Theorem 2.2.

A later or unindexed author correction may exist even though targeted searches did not surface one. The first-public-date evidence used here is the date printed on the author-hosted preprint; the journal publication occurred later in December 2025.

## References
A. Biś and H. Bruin, “On some aspects of local thermodynamical formalism,” DOI: 10.1007/s12346-025-01431-7. Author-hosted preprint dated 2025-12-09: https://www.mat.univie.ac.at/~bruin/papers/BB.pdf.
