# Decidable limiting endpoints for depth-one counting modal queries on random graphs

## Finding

**Theorem (depth-one convergence, exact finite census, and effective endpoint test).** Fix a finite set of \(k\geq 0\) propositional letters and let \(\varphi\) be any fixed formula of modal depth at most one in counting modal logic \(K^{\#}\). This includes arbitrary Boolean connectives, integer linear combinations of successor counts, and current-state truth indicators, provided no successor count is nested inside another successor count.

Choose a rational edge probability \(0<\lambda<1\) and a positive rational probability distribution \((\nu_s)_{s\in\{0,1\}^k}\) on complete propositional types. On \(n\geq1\) labelled worlds, include every ordered edge independently with probability \(\lambda\), including loops, and independently assign to every world a type with distribution \(\nu\). Evaluate \(\varphi\) at world \(1\), and denote its truth probability by \(\mu_n(\varphi)\). Then:

1. For every \(n\geq1\), the probability \(\mu_n(\varphi)\) is given **exactly** by the explicit root-row multinomial sum in the proof.
2. The limit \(\lim_{n\to\infty}\mu_n(\varphi)\) **always exists**. It is an effectively constructed finite sum of Gaussian probabilities of rational polyhedral cones, with positive-definite covariance \(\Sigma\) below.
3. Whether this limit equals \(0\) or \(1\) is **decidable** by finitely many rational strict-linear-feasibility tests; both endpoints may be tested separately.
4. Already for two independent fair letters and fair edges, the single depth-one formula
   \[
   \vartheta:=\bigl(2\,\#p\geq\#\top\bigr)\land\bigl(4\,\#(p\land q)\geq\#\top\bigr)
   \]
   has the **irrational** limiting probability
   \[
   \lim_{n\to\infty}\mu_n(\vartheta)
   =\frac14+\frac{1}{2\pi}\arcsin\!\left(\frac1{\sqrt3}\right)
   =0.347956638007652\ldots .
   \]

For the original uniform model of all directed labelled, loop-permitting graphs with fair propositional labels, take \(\lambda=1/2\) and \(\nu_s=2^{-k}\). Thus the theorem supplies a complete depth-one convergence result for that graph-counting model. No convergence assertion is made for formulas of modal depth two or greater.

## Assumptions and scope

The syntax is \(\varphi ::=p\mid\neg\varphi\mid\varphi\lor\varphi\mid(\xi\geq0)\), and \(\xi ::=c\mid 1_{\varphi}\mid\#\varphi\mid\xi+\xi\mid c\xi\), where \(c\in\mathbb Z\). The expression \(\#\chi\) counts successors of the current world satisfying \(\chi\), including the current world if the relation has a loop. The modal depth counts nested occurrences of \(\#\); indicators alone do not increase depth. The integer arithmetic convention includes abbreviations for subtraction and conjunction.

Set \(S=\{0,1\}^k\) and \(q_0=|S|=2^k\), and write \(p_s=\lambda\nu_s\). For a nonroot world \(j\geq2\), let \(Y_j=s\) if \((1,j)\) is an edge and world \(j\) has type \(s\), and \(Y_j=\star\) otherwise. Then \(\Pr(Y_j=s)=p_s\), \(\Pr(Y_j=\star)=1-\lambda\), and these variables are independent. Let \(M_s=\#\{j\geq2:Y_j=s\}\). The vector \(M=(M_s)_{s\in S}\) has a \((q_0+1)\)-category multinomial distribution with total \(n-1\). Root type \(T\) and loop indicator \(L\) are independent of \(M\), with laws \(\nu\) and \(\operatorname{Bernoulli}(\lambda)\).

For each Boolean (modal-depth-zero) formula \(\chi\), its successor count is exactly
\[
\#\chi=\sum_{s\in S}\boldsymbol1_{\chi(s)}M_s+L\boldsymbol1_{\chi(T)}.
\]
Consequently any depth-one formula can be evaluated by a finite Boolean-arithmetic predicate \(B_\varphi(T,L,M)\in\{0,1\}\). This predicate is constructive from syntax; it does not require the rest of the adjacency matrix.

## Proof

**Step 1: exact finite-size formula.** For \(m=(m_s)_{s\in S}\in\mathbb N^S\) put \(|m|=\sum_sm_s\) and \(z=n-1-|m|\). When \(z\geq0\), its multinomial weight is
\[
w_n(m)=\frac{(n-1)!}{z!\prod_{s\in S}m_s!}(1-\lambda)^z\prod_{s\in S}p_s^{m_s}.
\]
Therefore, for every integer \(n\geq1\),
\[
\boxed{\mu_n(\varphi)=\sum_{t\in S}\nu_t\sum_{\ell=0}^1\lambda^\ell(1-\lambda)^{1-\ell}
\sum_{m\in\mathbb N^S:\,|m|\leq n-1}w_n(m)B_\varphi(t,\ell,m).}
\]
This is finite and exact. With fair edges and fair labels, the total count of satisfying pointed labelled graphs is \(2^{n^2+kn}\mu_n(\varphi)\); all summands yield this integer because the formula depends only on root outgoing edges and world types.

**Step 2: finite sign-cell reduction.** Fix root type \(t\) and loop value \(\ell\). Every \(\#\chi\) present in a depth-one formula has Boolean \(\chi\), so it is affine-linear in \(M\). The remaining current-world indicators \(1_\psi\) take values in \(\{0,1\}\), even when \(\psi\) has modal depth one. Enumerate their finitely many truth-value assignments, replace each by its chosen constant, and conjoin the corresponding consistency tests; equivalently, eliminate indicators recursively by the two-case identity that replaces an indicator with its truth condition and with its negation. Since the syntax tree is finite, this terminates. Thus \(B_\varphi(t,\ell,M)\) is a Boolean combination of finitely many integer-affine comparisons
\[
a\cdot M+b(t,\ell)\geq0,\qquad a\in\mathbb Z^{q_0},\quad b(t,\ell)\in\mathbb Z.
\]
A comparison produced from a linear combination of counts has loop contribution \(\ell a_t\) (the same coefficient function evaluated at the root type), plus a bounded constant from numerical constants and indicators. Zero-coefficient comparisons are therefore resolved using the corresponding constant value in each branch; their truth is independent of \(n\). This remains true when the Boolean case-splitting is nested.

**Step 3: all probabilities converge.** Define
\[
\pi=(p_s)_{s\in S},\qquad
Z_n=\frac{M-(n-1)\pi}{\sqrt{n-1}},\qquad
\Sigma=\operatorname{diag}(\pi)-\pi\pi^{\mathsf T}.
\]
For \(n\geq2\), the multivariate central limit theorem gives \(Z_n\Rightarrow Z\sim N(0,\Sigma)\). The covariance is positive definite: for every nonzero vector \(u\),
\[
u^{\mathsf T}\Sigma u
=\lambda\sum_s\nu_su_s^2-\lambda^2\left(\sum_s\nu_su_s\right)^2
\geq\lambda(1-\lambda)\sum_s\nu_su_s^2>0,
\]
by Cauchy–Schwarz and \(0<\lambda<1\), \(\nu_s>0\). This bound is strictly positive for every nonzero \(u\).

For each comparison from Step 2, let its drift be \(d=a\cdot\pi\). The law of large numbers makes its truth eventually certain when \(d>0\), and its falsity eventually certain when \(d<0\). If \(d=0\) and \(a\neq0\), divide the comparison by \(\sqrt{n-1}\); its truth converges to the event \(a\cdot Z>0\), since \(a\cdot Z\) has strictly positive variance and the bounded offset disappears. Convergence holds jointly for the finite family of balanced nonzero comparisons: their Gaussian zero hyperplanes have probability zero, and the finite union of boundaries is null. Finally, comparisons with \(a=0\) are constants after the preceding case splits. Any Boolean combination of these finitely many events has a limiting probability. Average over finitely many \((t,\ell)\). This proves existence of \(\mu_\infty(\varphi)\) and constructs its finite Gaussian-cone expression. The limiting formula may be represented by a separate Boolean sign condition for each root type and loop choice.

**Step 4: deciding the endpoints.** Because \(\lambda\), \(\nu\), and each \(a\) are rational, the zero/nonzero drift trichotomy is exact arithmetic. Enumerate all sign choices \(\epsilon_i\in\{-1,1\}\) for the finitely many nonzero zero-drift coefficient vectors \(a_i\). A sign cell
\[
\mathcal C_\epsilon=\{z:\epsilon_i(a_i\cdot z)>0\text{ for every }i\}
\]
is nonempty precisely when the rational linear constraints \(\epsilon_i(a_i\cdot z)\geq1\) are feasible (rescale any strictly feasible point by a sufficiently large positive scalar). Rational linear-programming feasibility decides this. Every nonempty sign cell is open and has positive Gaussian measure because \(\Sigma\) is positive definite. Each branch's limiting Boolean truth is constant on a sign cell. The limiting probability is zero precisely when no root-type/loop branch of positive probability has a true feasible sign cell; it is one precisely when no root-type/loop branch of positive probability has a false feasible sign cell. Therefore both endpoint questions are decidable. For fixed rational parameters the Gaussian integral over each required finite union of cells can also be approximated effectively, without claiming that all such values have elementary closed forms.

**Step 5: an explicit irrational limit.** In the fair two-letter model, for a nonroot world let \(E,P,Q\) be independent fair bits for its incoming edge, its truth of \(p\), and its truth of \(q\). Its contributions to \(A_n=2\#p-\#\top\) and \(B_n=4\#(p\land q)-\#\top\) are \(X=E(2P-1)\) and \(Y=E(4PQ-1)\). They have mean zero and
\[
\operatorname{Var}(X)=\frac12,\qquad
\operatorname{Var}(Y)=\frac32,\qquad
\operatorname{Cov}(X,Y)=\frac12,
\qquad\rho=\frac1{\sqrt3}.
\]
The root loop contributes only a bounded term. A bivariate central limit theorem and the Gaussian orthant identity therefore give
\[
\lim_{n\to\infty}\Pr(A_n\geq0,B_n\geq0)
=\frac14+\frac{\arcsin(\rho)}{2\pi}.
\]
To prove irrationality, put \(\alpha=\arcsin(1/\sqrt3)\). If \(\alpha/\pi\) were rational, \(e^{2i\alpha}\) would be a root of unity, so \(2\cos(2\alpha)=e^{2i\alpha}+e^{-2i\alpha}\) would be an algebraic integer. But \(2\cos(2\alpha)=2/3\), not an integer, whereas a rational algebraic integer must be integral. Hence \(\alpha/\pi\), and therefore \(1/4+\alpha/(2\pi)\), are irrational.

## Verification

The standalone file `checker.py` implements direct finite-model semantics, an independently weighted multinomial root-row enumeration, full-adjacency enumeration for small sizes, and exact rational moment calculations. Run it with `python checker.py`; it requires only the Python standard library. The recorded result was `ALL_CHECKS_OK`.

For each of three depth-one example formulas (including one with nested current-state indicators), complete root-row enumeration agreed with the exact multinomial sum for \(n=1,2,3,4,5\). For the irrational-limit witness, enumeration of **all** directed adjacency matrices and two-letter valuations also agreed for \(n=1,2,3\). The verified row-satisfying counts for \(\vartheta\) at \(n=1,\ldots,5\) are \(5,31,221,1727,13940\), out of \(8^n\) equally likely row-and-label assignments. Exact moment verification gave the stated covariance matrix and numerical limiting constant. Finite computation is not substituted for the central limit theorem or the irrationality proof.

## Relationship to prior work

Ghosh and Schwarzentruber (2026), *On Counting Graphs for Modal Logic with Counting* (arXiv:2610.26187v1, first publicly submitted 19 October 2026), formulate the same labelled pointed graph-counting model and the \(K^{\#}\) language. Their Section 6 analyzes limits for branching-tree models, with a multivariate central limit approach and Gaussian orthant identities; their Section 7 explicitly lists convergence on general graphs as an open direction. Their Appendix A works out one graph formula, \(\#p\geq\#q\). Their stated tree nonconvergence example has modal depth two. The depth-one **convergence part alone can also be recovered** from their Theorem 28: mark each potential root successor by an independent edge-indicator proposition and translate every root count into a count of marked children; handle the single possible root self-loop by conditioning. Thus convergence by itself is **not** asserted to be independent of their stronger tree theorem. The additional claim here is the **complete rational feasibility decision procedure for limiting endpoint membership** for the entire depth-one graph fragment (including nested current-state indicators), with an explicit full-rank categorical covariance and an exact irrational graph instance. Neither the central limit theorem nor Sheppard's Gaussian identity is claimed as new.

Nunn and Schwarzentruber (2023) introduce modal counting syntax and graph-neural interpretations. Nunn, Sälzer, Schwarzentruber and Troquard (2024) develop aggregate-combine graph-neural logic and satisfiability. Adam-Day, Benedikt, Ceylan and Finkelshtein (2024) study asymptotically constant architectures under restrictions different from balanced integer successor-count comparisons. The inspected accessible primary texts do not imply the complete depth-one graph result.

## Limitations

The depth-one restriction is essential to this argument: nested successor counts sample correlated remote neighborhoods and cannot be reduced to one independent multinomial row. The claim does not solve general \(K^{\#}\) graph convergence or identify the computational complexity of the complete unrestricted convergence problem. Strictly positive type masses and nondegenerate edge probability ensure full-rank Gaussian covariance; degenerate parameter cases require separate handling. Parameters are rational for the exact endpoint decision procedure. The theorem applies to labelled directed graphs with loops; other random-graph ensembles require a fresh dependence analysis. General earlier theorems for linear threshold properties of independent categorical observations could encompass the Gaussian component under other terminology; independent literature review remains valuable.

## References

1. A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1 (19 October 2026), Sections 3, 4, 6, 7 and Appendix A. https://arxiv.org/html/2610.26187v1
2. P. Nunn and F. Schwarzentruber, *A Modal Logic for Explaining some Graph Neural Networks*, arXiv:2307.05150 (2023). https://arxiv.org/abs/2307.05150
3. P. Nunn, M. Sälzer, F. Schwarzentruber and N. Troquard, *A Logic for Reasoning about Aggregate-Combine Graph Neural Networks*, arXiv:2405.00205 (2024). https://arxiv.org/html/2405.00205v2
4. S. Adam-Day, M. Benedikt, İ. İ. Ceylan and B. Finkelshtein, *Almost Surely Asymptotically Constant Graph Neural Networks*, arXiv:2403.03880 (2024). https://arxiv.org/html/2403.03880v3
5. Standard multivariate central limit theorem, Portmanteau theorem, Gaussian orthant identity, and algebraic-integrality criterion for roots of unity (classical tools; no novelty claimed for these ingredients).
