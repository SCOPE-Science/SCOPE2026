# Sparsity forces strong-PV structure for every real parameter
## Finding
For every real number \(a\), let \(D(a)\) be the \(a\)-convex hull of \(\{0,1\}\). Then \(D(a)\) has no limit points if and only if \(a\) is a strong PV number.

Equivalently, if \(D(a)\) is sparse, then \(a\) is an algebraic integer and every algebraic conjugate of \(a\) distinct from \(a\) lies in \((0,1)\). In particular, a sparse real parameter is automatically totally real. Conversely, every real strong PV number has uniformly discrete \(D(a)\), hence is sparse.

This removes the total-reality hypothesis from the 2026 proof of Pinch's conjecture and establishes the real-parameter case of the strong-PV discreteness characterization formulated by Fenner, Green, and Homer.
## Assumptions and scope
The parameter \(a\) is any real number. The set \(D(a)\) is generated from \(\{0,1\}\) by the binary operation \(x,y\mapsto ax+(1-a)y\). A parameter is called sparse when \(D(a)\) has no limit points.

A real number \(a\) is called a strong PV number when it is an algebraic integer and every algebraic conjugate distinct from \(a\) lies in \((0,1)\). This is the real specialization of the strong-PV definition used by Fenner, Green, and Homer.
## Proof
Assume first that \(D(a)\) is sparse. A theorem of Pinch, restated as Theorem 8.1 in the extended treatment by Fenner, Green, and Homer, says that a real parameter with discrete \(D(a)\) is an algebraic integer. Since having no limit points implies discreteness, \(a\) is an algebraic integer.

If \(a\) is an integer, it has no nontrivial algebraic conjugates, so it is strong PV. Hence suppose that \(a\) is not an integer. Campbell's Lemma 4, quoting Pinch's Proposition 10, says that if some \(P\in D(X)\) satisfies \(0<P(a)<1\), then \(a\) is not sparse. Taking \(P(X)=X\) shows that a sparse noninteger parameter cannot lie in \((0,1)\). Because it is not an integer, it follows that \(a\notin[0,1]\).

Suppose for contradiction that \(a\) has a nontrivial conjugate \(a^{\ast}\notin(0,1)\). If \(a^{\ast}\) is nonreal, then automatically \(a^{\ast}\notin[0,1]\). If \(a^{\ast}\) is real, then it cannot equal \(0\) or \(1\): otherwise the irreducible minimal polynomial of \(a\) would be divisible by \(X\) or \(X-1\), forcing \(a=0\) or \(a=1\). Thus again \(a^{\ast}\notin[0,1]\). This is the only point where Campbell's published proof invokes total reality: there it uses total reality to infer that \(a^{\ast}\) is real before reaching the same conclusion.

Set \(K=[0,1]\cup\{a\}\). Campbell's Lemma 5 gives \(d(K)<1\), where \(d(K)\) is the transfinite diameter. We claim that the union \(J_0(K,\mathbb Z)\) of complete conjugacy classes of algebraic integers contained in \(K\) is exactly \(\{0,1\}\). Certainly \(0\) and \(1\) belong. Conversely, let \(\alpha\in J_0(K,\mathbb Z)\). If one conjugate of \(\alpha\) were \(a\), irreducibility would make the conjugacy classes of \(\alpha\) and \(a\) equal, forcing the class of \(\alpha\) to contain \(a^{\ast}\notin K\), a contradiction. Hence all conjugates \(\beta_1,\ldots,\beta_d\) of \(\alpha\) lie in \([0,1]\). If one is zero, irreducibility gives \(\alpha=0\). Otherwise their product is a positive integer at most \(1\), so it equals \(1\); since every factor lies in \((0,1]\), every factor equals \(1\), and \(\alpha=1\). Thus \(J_0(K,\mathbb Z)=\{0,1\}\).

Campbell's Lemma 6 now gives an integer polynomial \(Q\) with \(Q(0)=Q(1)=0\) and \(0<Q(x)<1\) for every \(x\in K\setminus\{0,1\}\). In particular, \(0<Q(x)<1\) on \((0,1)\), so Campbell's Lemma 3 yields \(Q\in D(X)\). Also \(0<Q(a)<1\), and Campbell's Lemma 4 then contradicts sparsity. Therefore no such \(a^{\ast}\) exists. Every nontrivial conjugate of \(a\) lies in \((0,1)\), so \(a\) is strong PV and is automatically totally real.

For the converse, Fenner, Green, and Homer prove that for every strong PV number \(a\), the generated set \(Q_a(S)\) is uniformly discrete for every finite \(S\subseteq\mathbb Q(a)\). Taking \(S=\{0,1\}\) identifies \(Q_a(S)=D(a)\); uniform discreteness implies that \(D(a)\) has no limit points.
## Verification
The proof is deductive and uses no finite experiment as a substitute for an infinite argument. The critical published inputs were checked in the full text of Campbell's arXiv version: the definitions of \(D(a)\) and sparsity, Lemmas 3--6, and Theorem 2 with its complete proof. In Theorem 2, the total-reality hypothesis is used explicitly only to assert that the chosen bad conjugate is real; all subsequent objects are built from the real parameter \(a\), not from the bad conjugate. Replacing that single step by the real/nonreal dichotomy above leaves every later hypothesis unchanged.

The strong-PV definition, the sufficient uniform-discreteness theorem, and the conjectured converse were checked in the open-access full text of Fenner, Green, and Homer. Their text also restates Pinch's real-parameter algebraic-integrality theorem as Theorem 8.1.
## Relationship to prior work
Campbell proves the necessity statement under the additional assumption that \(a\) is totally real. The present argument removes that assumption: a nonreal bad conjugate is even easier to exclude from the real compact set \([0,1]\cup\{a\}\), after which Campbell's argument applies verbatim at the level of hypotheses.

Fenner, Green, and Homer define strong PV numbers, prove that strong PV parameters give uniformly discrete generated sets, and formulate the converse as Conjecture 11.1 for complex parameters. They separately record the real quadratic converse from Pinch. The result here supplies the missing necessity for every real parameter, not only for the totally real or quadratic subfamilies.

Targeted searches of the published-findings database for the total-reality removal, automatic total reality, strong-PV equivalence, and nonreal-conjugate formulation returned no covering result. The closest returned records concern unrelated algebraic or analytic topics and do not imply the present statement.
## Limitations
The proof is restricted to real parameters \(a\). It does not resolve the genuinely complex part of the strong-PV discreteness conjecture. The 1985 Pinch paper was not available in full text during this verification; the specific Pinch statements used here were checked through their explicit restatements and citations in the full texts of Campbell and Fenner--Green--Homer. No claim is made about complex parameters beyond the cited sufficient theorem.
## References
1. John M. Campbell, *Pinch's conjecture on \(a\)-convexity*, arXiv:2609.30771v1, first public 2026-09-25. Primary MSC 11R04.
2. Stephen Fenner, Frederic Green, and Steven Homer, *Fixed-Parameter Extrapolation and Aperiodic Order*, Discrete & Computational Geometry 76 (2026), 1--74, DOI 10.1007/s00454-025-00816-4.
3. R. G. E. Pinch, *\(a\)-convexity*, Mathematical Proceedings of the Cambridge Philosophical Society 97 (1985), 63--68, DOI 10.1017/S0305004100062587.
