# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness — PASS

The argument uses the exact one-sided level-set identity recalled in the
direct source. Integrating that identity by layer cake gives
\[
\|M_\pm f\|_p^p
=
p'\int f(M_\pm f)^{p-1}.
\]
Truncation by \(\min(f,m)\mathbf1_{[-m,m]}\) and monotone convergence make
this identity valid for every nonnegative \(f\in L^p\).

For a normalized centered near-extremizer with deficit
\(\delta=p'-\|M_{\mathrm c}f\|_p\), the chain
\[
M_{\mathrm c}f\le (M_-f+M_+f)/2,\qquad
\|M_\pm f\|_p\le p'
\]
forces both one-sided norms to lie in \([p'-2\delta,p']\).
After normalizing \(M_\pm f\), the exact identity says that its dual pairing
with \(f\) is \(1-O_p(\delta)\). The standard \(L^p\) modulus of convexity has
power type \(\max\{2,p\}\), so both normalized one-sided maximal functions
are \(O_p(\delta^{1/\max\{2,p\}})\)-close to \(f\). Rescaling gives the two
one-sided near-eigenfunction estimates.

The centered estimate follows from the pointwise ordering
\(0\le M_{\mathrm c}f\le (M_-f+M_+f)/2\) and
\[
(A-B)^p\le A^p-B^p\qquad(0\le B\le A).
\]
This gives an \(O_p(\delta^{1/p})\) gap from the arithmetic mean, which is
never worse than the uniform-convexity rate needed in the theorem.

For exact equality, the one-sided relation \(M_+f=p'f\), combined with the
rising-sun level identity, forces the distribution function to be a pure
\(t^{-p}\) tail. Such a tail has a logarithmically divergent \(p\)-moment,
so no nonzero \(L^p\) extremizer exists.

The dyadic-radii extension uses only
\(M_{\mathrm{dyad}}\le M_{\mathrm c}\), the exact norm \(p'\) from Madrid,
and the same pointwise power-difference inequality. The strong
noncompactness statement is valid because translations and normalized
dilations preserve the centered norm, while the centered maximal map is
Lipschitz on \(L^p\).

## Originality — PASS, to the best of our knowledge

The direct source, arXiv:2609.12440, was inspected at its main theorem and
upper-bound proof. It proves the previously unknown exact centered norm
\(p'\), produces smooth compactly supported extremizing sequences, and
proves the same norm for centered dyadic radii. Searches in the source found
no statement about norm attainment, extremizers, or quantitative
near-eigenfunction rigidity.

Searches combining centered Hardy--Littlewood maximal operators with
"extremizer", "nonattainment", "extremizing sequence", "near extremizer",
"eigenfunction", and "stability" did not locate the theorem above. The
older paper of Colzani and Pérez Lázaro explicitly concerns eigenfunctions
and nonattainment for the one-dimensional uncentered maximal operator,
whose sharp constant is different. Its abstract and bibliographic record
were inspected, but its full text was not independently rechecked in this
review. Grafakos--Montgomery-Smith concerns the sharp uncentered norm.

The main residual originality risk is that the centered exact norm is very
recent, so a contemporaneous note exploiting the same equality chain may
not yet be indexed. Also, general quantitative Hölder/uniform-convexity
stability principles are classical; originality is claimed only for their
application to the newly sharp centered maximal inequality and the resulting
simultaneous one-sided/centered rigidity. No inaccessible source was found
that gives concrete evidence of equivalent centered coverage.

## Value — PASS

The direct source establishes a sharp constant and an explicit family of
extremizing sequences, but sharpness alone does not describe the equality
or near-equality regime. The present result settles nonattainment and gives
a quantitative structural statement applying to every near-extremizer:
both one-sided maximal functions and the centered maximal function must
collapse onto the same approximate eigenprofile \(p'|f|\).

This identifies a necessary mechanism behind all extremizing sequences,
including Madrid's multiscale examples, and immediately explains why
strong compactness modulo the natural affine symmetries is impossible. The
same mechanism persists for the sparse geometric family of centered radii
that already has the full sharp norm.

## Limitations

- The power \(1/\max\{2,p\}\) is not claimed optimal.
- No spatial or multiscale classification of all extremizing sequences is
  obtained.
- The compactness statement is not a full concentration-compactness theorem.
- The result is one-dimensional.
- The dyadic-radii operator is the centered radii-restricted operator in the
  direct source, not the usual dyadic-grid maximal operator.
- The full text of the 2010 uncentered eigenfunction paper was not
  independently rechecked.
- A contemporaneous unindexed refinement of the 2026 source may exist.
- Cross-model review has not been performed.
