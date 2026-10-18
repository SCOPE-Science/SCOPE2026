# Exact equality sets and agreement frequencies of classical implication-only formulas

## Finding

Fix an integer \(k\ge 2\). Let \(\mathcal I_k\) consist of classical propositional formulas built from the positive letters \(p_1,\ldots,p_k\) using **only** material implication \(\to\), with no constants or other connectives. For \(\varphi,\psi\in\mathcal I_k\) put
\[
E(\varphi,\psi)=\{a\in\{0,1\}^k:\varphi(a)=\psi(a)\}.
\]

**Exact solution-set theorem.** A set \(E\subseteq\{0,1\}^k\) equals \(E(\varphi,\psi)\) for such formulas if and only if there exist two distinct indices \(i,j\) such that
\[
\{a:a_i=a_j=1\}\subseteq E.
\]
For \(k=1\), the only equality sets are \(\{1\}\) and \(\{0,1\}\).

**Exact equational probability spectrum.** Under the uniform distribution on assignments and allowing every positive arity, the full spectrum is
\[
\boxed{\left\{\frac{m}{2^k}: k\ge2,\ 2^{k-2}\le m\le 2^k,\ m\in\mathbb Z\right\}}
=\left\{r\in\mathbb Z[1/2]:\frac14\le r\le1\right\}.
\]
In particular, every implication-only equation holds on at least one-quarter of the assignments, this bound is attained, and **every dyadic agreement frequency above the bound** occurs. The same spectrum holds for the four two-element binary operations grouped in the previously unresolved row of Cardó's 2026 table: material implication, its converse, and their Boolean-dual operations.

## Assumptions and scope

The truth values are exactly \(0,1\), and \(a\to b\) has its classical truth table \(\neg a\lor b\). An equation is a pair of formulas, and its solution set is computed over a specified finite vocabulary. A displayed formula may omit a designated letter; unused letters can always be inserted without changing its Boolean function using \((q\to q)\to\varphi\). Accordingly, the displayed spectrum also applies when arity means the number of variables syntactically occurring in the equation. There are no nullary symbols. Syntactic formula size is unrestricted.

The result classifies the solution sets of **single equations**, not arbitrary conjunctions of equations and not the distribution obtained by choosing a random formula tree. The principal classification is in classical propositional logic (MSC2020 03B05); the binary-algebraic spectrum is an equivalent formulation.

## Proof

**Lemma 1 (forced-one coordinate).** Every implication-only formula \(\theta\) has an index \(i\) for which \(a_i=1\) implies \(\theta(a)=1\), uniformly over all other coordinates. Induct on the formula: a positive letter forces itself; for \(\alpha\to\beta\), a forced-one coordinate of the consequent \(\beta\) also forces \(\alpha\to\beta\) to one. Thus for any equation \(\varphi\approx\psi\), choose forced-one indices \(i,j\) for the two terms. If \(i\ne j\), the entire codimension-two face on which both coordinates are one is a solution set. If \(i=j\), equality holds on the larger codimension-one face \(a_i=1\); since \(k\ge2\), choose any \(j\ne i\) to obtain the required codimension-two face.

**Lemma 2 (converse expressibility).** If a Boolean function \(f\colon\{0,1\}^k\to\{0,1\}\) equals one whenever \(a_i=1\), then \(f\) is expressible in the implication-only language. Indeed, write \(f(a)=a_i\lor g(a_{\ne i})\) for an arbitrary Boolean function \(g\) of the remaining coordinates. For a formula \(G\) denoting \(g\) in the temporary Boolean language with \(0,1,\neg,\land,\lor\), recursively construct an implication-only formula \(T_i(G)\) denoting \(p_i\lor g\):
\[
\begin{aligned}
T_i(0)&=p_i,&T_i(1)&=(p_i\to p_i),\\
T_i(p_h)&=((p_h\to p_i)\to p_i)&\quad(h\ne i),\\
T_i(\neg G)&=(T_i(G)\to p_i),\\
T_i(G\lor H)&=((T_i(G)\to T_i(H))\to T_i(H)),\\
T_i(G\land H)&=((T_i(G)\to(T_i(H)\to p_i))\to p_i).
\end{aligned}
\]
All identities follow by considering \(a_i=0\) and \(a_i=1\); in the former case \(p_i\) functions as the temporary false constant, while in the latter every displayed term evaluates to one. Every finite Boolean function \(g\) has a Boolean expression \(G\), so this is an explicit existence construction using no new primitive symbols.

**Lemma 3 (all supersets of a positive codimension-two face).** Let \(E\) contain the face \(a_i=a_j=1\), with \(i\ne j\). Define Boolean functions \(f,g\) pointwise, with their values depending on any other coordinates as follows. At \((a_i,a_j)=(1,1)\), set both values to one. At \((1,0)\), set \(f=1\) and \(g=\mathbf1_E\). At \((0,1)\), set \(g=1\) and \(f=\mathbf1_E\). At \((0,0)\), set \(g=1\) and \(f=\mathbf1_E\). Thus \(f=1\) wherever \(a_i=1\), \(g=1\) wherever \(a_j=1\), and \(f=g\) exactly on \(E\). Lemma 2 provides formulas denoting them. This proves the equality-set classification.

**Spectrum and boundary.** By Lemma 1 every equality set for \(k\ge2\) has at least \(2^{k-2}\) assignments, hence its probability is at least \(1/4\). By Lemma 3, for every integer \(m\) between \(2^{k-2}\) and \(2^k\), select any \(m\)-element set containing a fixed codimension-two face: it is an equality set. The one-variable case has only the two term functions \(p_1\) and \(p_1\to p_1\), yielding agreement rates \(1/2\) and \(1\), already in the displayed spectrum. Every equation in finitely many variables therefore gives, and every fraction in the displayed set attains, precisely an allowed dyadic rate. The lower endpoint is witnessed by \(p_1\approx(p_1\to p_2)\), satisfied exactly on the assignment \((1,1)\). No smaller rate is possible.

**Other binary operations.** Conjugating the material-implication operation on \(\{0,1\}\) by swapping \(0\) and \(1\) yields \(\neg x\land y\); reversing inputs gives the other two operations. Isomorphic and anti-isomorphic groupoids have identical term-equation probability spectra (a direct bijection of term equations, possibly reversing binary-operand order). Thus all four operations in the previously unknown table row have this same spectrum.

## Verification

The included standalone Python checker enumerates, independently from the abstract proofs, (i) the clone generated by implication from projections; (ii) the Boolean functions that have a forced-one coordinate; (iii) all equality sets of pairs of term functions; and (iv) all subsets containing a positive codimension-two face. It compares the two descriptions exhaustively for \(k=1,2,3\).

Run `python3 implication_spectrum_verify.py`. Expected terminal line: `IMPLICATION_SPECTRUM_VERIFY_OK`. The observed closure sizes were \(2,6,38\) term functions, respectively, and the equality-set counts were \(2,8,112\). The attained numerator ranges were respectively \(1\) through \(2\), \(1\) through \(4\), and \(2\) through \(8\). These exhaustive finite checks corroborate the proof; the theorem for all arities rests on Lemmas 1–3, not on extrapolation from the tests.

## Relationship to prior work

Cardó [1], Section 4, Table 1, marks the equational probabilistic spectrum of exactly these four two-element groupoids **unknown**. The present result fills that explicit classification gap. The older work of Fournier, Gardy, Genitrini, and Gittenberger [2] already characterizes the individual Boolean functions expressible by implication-only formulas as those of shape \(p_i\lor g\); that characterization is prior art, not claimed as new. The present contribution is the complete **pairwise equality-set classification**, including the sharp all-arity probability spectrum. The argument supplies the combinatorial bridge from the known term-function class to the previously unrecorded equation-solution invariant.

The companion study [3] classifies groupoids with **minimal** spectra and does not supply this four-operation nonminimal spectrum. No broader previously identified result was found that states this equality-set family or its exact spectrum, though an equivalent result in older or unindexed literature remains possible.

## Limitations

The claim concerns uniform assignments, positive variables, binary material implication alone, and single equations. It does not cover intuitionistic implication, many-valued implication, biased product measures, random formula-tree sampling, or the succinctness of formulas realizing a specified equality set. The link to the previously unknown table is a new consequence of known Boolean clone structure; no priority is claimed for that structure itself. Historical-priority uncertainty remains, and no independent mathematical audit has been performed.

## References

[1] Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (first public 2026-04-09), Section 4, Table 1. https://arxiv.org/abs/2604.08446

[2] Hervé Fournier, Danièle Gardy, Antoine Genitrini, Bernhard Gittenberger, *The fraction of large random trees representing a given Boolean function in implicational logic*, *Random Structures & Algorithms* **40** (2012), 317–349, DOI:10.1002/rsa.20379; accessible author manuscript: https://danielegardy.github.io/SourcesPubli/implication.pdf

[3] Carles Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487 (2026). https://arxiv.org/abs/2603.19487
