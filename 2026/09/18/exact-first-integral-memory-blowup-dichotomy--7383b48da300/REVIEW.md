# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The source F2 equation reduces exactly to

\[
\dot u=(1-v)^{-1},\qquad \dot v=\alpha u-\beta v.
\]

On either side of the singular line \(v=1\), the substitution \(w=(1-v)^{-1}\) gives

\[
\dot u=w,\qquad \dot w=(\alpha u-\beta)w^2+\beta w.
\]

Dividing the second equation by the first is legitimate because finite \(v\ne1\) implies \(w\ne0\). The resulting linear equation in \(w(u)\) has the displayed exact integrating factor. Direct differentiation of the proposed first integral gives zero identically.

The sign argument is global: for \(w_0>0\), the bracket \(Q(u)\) is bounded below by a strictly positive constant for all \(u\ge u_0\); for \(w_0<0\), it is bounded above by a strictly negative constant for all \(u\le u_0\). Hence the sign of \(w\) cannot change, the solution is monotone toward the corresponding infinite end, and the remaining time is dominated by a Gaussian tail. This proves finite-time positive blow-up below \(v=1\) and finite-time negative blow-up above it. At \(v_0=1\), the original right-hand side is undefined.

The refined asymptotics follow from the exact trajectory formula and the standard Gaussian-tail expansion. Re-expansion was checked for sign, shift, and coefficient consistency. In particular differentiating the leading term \(\sqrt{2/\alpha}\sqrt{\log(1/(T-t))}\) gives the stated leading derivative coefficient \(1/\sqrt{2\alpha}\).

The verification artifact was executed. It returns `symbolic_dHdt = 0` and numerically checks both signs for \(\alpha=\beta=1\).

## Adversarial checks

The main possible escape for the source theorem would be an implicit hypothesis \(v(0)<1\). The theorem statement itself quantifies over every positive bounded history, while the proof later says it is "focusing on the range" \(0\le v(t)<1\) before defining \(w\). The introductory assumptions only state \(v(0)>0\), not \(v(0)<1\). Constant positive histories show that all three cases \(v_0<1\), \(v_0=1\), and \(v_0>1\) occur under the stated history class.

For \(\alpha=\beta=1\), the admissible constant history \(\phi\equiv2\) gives \((u_0,v_0)=(2,2)\), so the equation is initially nonsingular but lies on the negative branch. The history \(\phi\equiv1\) gives \(v_0=1\), where the right-hand side is singular immediately. Thus the issue is not a boundary artifact that requires exotic data.

If the model is interpreted as constrained to nonnegative \(u\), the supercritical trajectory crosses \(u=0\) before the negative singularity and exits the biological state space. That convention still invalidates the universal positive-blow-up statement; it does not restore it.

## Originality

PASS, to the best of our knowledge.

The full arXiv v1 text was inspected, including the theorem statement, the F2 linear-chain reduction, the restriction to \(0\le v<1\), and the asymptotic proof. Searches using the exact title and arXiv identifier together with `first integral`, `initial memory`, `correction`, `counterexample`, `logarithmic blow-up`, and equivalent source-specific equation forms did not locate a public correction, comment, or derivation of this trichotomy and exact first integral.

General results about the linear-chain trick, planar integrating factors, Gaussian-tail inversion, and blow-up analysis are established mathematics and are excluded from the originality claim. The novelty claim is only the source-specific correction and completion: identifying the missing \(v(0)<1\) hypothesis in arXiv:2609.15470v1, classifying the omitted \(v(0)>1\) regime exactly, and sharpening the source's unspecified F2 blow-up constants and next terms.

The source is very recent, so an unindexed author revision or discussion is the main residual originality risk. No inaccessible paper emerged from the search as a particularly plausible source of the same source-specific correction.

## Value

PASS.

The source presents Theorem 2 as a universal statement for positive bounded histories and uses it to motivate memory-induced blow-up. The initial-memory split changes that statement qualitatively: one open half-plane blows up positively, the other blows down negatively, and the separating line is singular. The exact first integral also makes the leading amplitudes universal and isolates how the forgetting rate and initial history enter only at lower order. This is a substantive correction and refinement of the source's main F2 result rather than a parameter variant.

## Scope and limitations

The result applies only to F2 with the single exponential kernel. It does not settle F1 or F3 and does not assert that negative populations are physically meaningful. It is a mathematical classification of the real-valued model wherever the vector field is defined.
