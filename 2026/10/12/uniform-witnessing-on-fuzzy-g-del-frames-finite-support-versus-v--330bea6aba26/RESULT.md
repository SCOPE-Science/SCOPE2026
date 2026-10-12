# Uniform witnessing on fuzzy Gödel frames: finite support versus vanishing tails
## Finding

Let \(W\) be any nonempty set, and let \(R:W\times W\to[0,1]\) be a fuzzy accessibility relation. For \(w\in W\) define its positive support and positive level sets by
\[
S_w=\{u\in W:R(w,u)>0\},\qquad
S_w(\varepsilon)=\{u\in W:R(w,u)\ge\varepsilon\}\quad(\varepsilon>0).
\]
Call a frame **uniformly box-witnessed** if, for every valuation and every formula, each necessity infimum is attained at an actual world. Define **uniformly diamond-witnessed** analogously for each possibility supremum. Then:

1. The frame is uniformly box-witnessed **if and only if** \(S_w\) is finite for every \(w\in W\).
2. The frame is uniformly diamond-witnessed **if and only if** \(S_w(\varepsilon)\) is finite for every \(w\in W\) and every real \(\varepsilon>0\). Equivalently, each row of \(R\) belongs to \(c_0(W)\) for the discrete index set.
3. The frame makes *every* Gödel model on it witnessed for both modalities if and only if every \(S_w\) is finite.

The second condition is strictly weaker than the first. For example, on \(W=\mathbb N\), the relation \(R(w,n)=1/(n+1)\) for every \(w,n\in W\) has infinite positive support at every world but has finite positive level sets. Thus every diamond value is witnessed under every valuation while box witnessing fails for some valuation.

## Assumptions and scope

We work in ordinary set theory with choice, with a countable propositional language containing at least one atom \(p\). Each atomic valuation is an arbitrary map \(W\to[0,1]\), extended recursively by the standard Gödel operations. In particular,
\[
a\mathbin{\to_{\mathrm G}}b=\begin{cases}1,&a\le b,\\b,&a>b,\end{cases}\qquad
 e(w,\Box\varphi)=\inf_{u\in W}(R(w,u)\to_{\mathrm G}e(u,\varphi)),
\]
\[
e(w,\Diamond\varphi)=\sup_{u\in W}\min\{R(w,u),e(u,\varphi)\}.
\]
A **witness** is any \(u\in W\) attaining the displayed infimum or supremum, including a world of weight zero when the relevant extremum is respectively \(1\) or \(0\). This is the fuzzy-model convention of Ferrari--Fiorentini--Giardini--Rodriguez (2026); it differs from a convention requiring positive-weight successor witnesses even at zero-accessibility worlds. We quantify over **all** assignments of atoms, worlds, and modal formulas. No transitivity, seriality, continuity, or finiteness of \(W\) is assumed. The necessity counterexample below uses a countably infinite subset of an infinite set, available in the ambient set theory.

## Proof

**1. Sufficiency for the box.** Fix \(w\), an arbitrary truth-value function \(v:W\to[0,1]\), and suppose \(S_w\) finite. When \(R(w,u)=0\), the Gödel implication \(R(w,u)\to_{\mathrm G}v(u)\) is \(1\). If \(S_w\ne\varnothing\), the infimum over all \(W\) is the minimum of finitely many implication values on \(S_w\) together with possible copies of \(1\), hence is attained. If \(S_w=\varnothing\), every implication value is \(1\), attained anywhere because \(W\ne\varnothing\). Substituting \(v(u)=e(u,\varphi)\) proves the modal assertion for any valuation and any \(\varphi\).

**2. Necessity for the box.** Suppose \(S_w\) infinite. Choose distinct \(u_1,u_2,\ldots\in S_w\). Set one atom's values to
\[
e(u_j,p)=\min\{R(w,u_j)/2,\ 1/(j+1)\}>0\quad(j\ge1),
\]
and set \(e(u,p)=1\) at every other world. At \(u_j\), its accessibility value strictly exceeds \(e(u_j,p)\), so
\[
R(w,u_j)\to_{\mathrm G}e(u_j,p)=e(u_j,p)>0,
\]
with values tending to \(0\). Outside the chosen sequence the implication equals \(1\). Consequently \(e(w,\Box p)=0\), but no world attains zero. Thus universal box witnessing fails already at modal depth one.

**3. Sufficiency for the diamond.** Suppose all positive level sets \(S_w(\varepsilon)\) are finite. For an arbitrary \(v\), let
\[
s=\sup_{u\in W}\min\{R(w,u),v(u)\}.
\]
If \(s=0\), every term is zero and any world witnesses the supremum. If \(s>0\), terms outside the finite set \(S_w(s/2)\) are less than \(s/2\), while the definition of \(s\) ensures some terms exceed \(s/2\). Therefore the supremum agrees with the maximum over this nonempty finite level set and is attained. Again put \(v(u)=e(u,\varphi)\) for any formula.

**4. Necessity for the diamond.** If some \(S_w(\varepsilon)\) is infinite for \(\varepsilon>0\), choose distinct \(u_1,u_2,\ldots\) therein and a real \(c\) with \(0<c<\min\{\varepsilon,1\}\). Put
\[
e(u_j,p)=c\bigl(1-1/(j+1)\bigr),\quad e(u,p)=0\ \text{elsewhere}.
\]
Since \(R(w,u_j)\ge\varepsilon>c\), the corresponding diamond terms equal the displayed values, all strictly below \(c\) and converging upward to \(c\). All remaining diamond terms are zero. Hence \(e(w,\Diamond p)=c\), but no term attains \(c\). This proves the converse.

Finally, finite support implies finite level sets, so combining parts 1--4 gives the joint characterization. For strictness take \(R(w,n)=1/(n+1)\) on \(\mathbb N\); then each positive level set is finite but the positive support is infinite. In particular \(e(n,p)=1/(2(n+1))\) witnesses the box failure by the construction in part 2. \(\square\)

## Verification

The self-contained `verify.py` uses exact rational arithmetic. Running `python3 verify.py` checks all 4,368 combinations of row and atom values on nonempty finite rows of sizes one through three over the four-element truth-value grid, and tests twelve finite prefixes of the two infinite counterexample sequences. All checks passed. The mathematical proof above, not the finite enumeration, establishes the infinite and unrestricted-valuation statements. No computational certificate beyond these checks is needed.

## Relationship to prior work

Ferrari, Fiorentini, Giardini, and Rodriguez (2026) define witnessed fuzzy Gödel models, exhibit a non-witnessed infinite crisp example, and establish proof-search and finite-model results for the class of witnessed models. The present result **does not** claim that notion or their exhibited counterexample; it gives an exact framewise necessary-and-sufficient criterion when witnessing must hold **for every valuation**, separately for the two modal operators. In particular, the positive-level-set characterization identifies infinite fuzzy frames where possibility is universally witnessed even though necessity is not.

The earlier paper *A Gödel Modal Logic over Witnessed Crisp Models* (2025) studies crisp-frame, model-dependent witnesses. *Paraconsistent Gödel Modal Logic* (2022) discusses finitely branching frames and a modal definability criterion (Theorem 2); this already covers important finite-branching and non-attainment phenomena. Neither compared result states the separate \(c_0\)-row criterion for universal diamond witnessing with unrestricted fuzzy accessibility. The older work substantially motivates the box half; the sharper operator-selective separation is the principal point here.

## Limitations

The result concerns the standard Gödel residuum and minimum-based diamond over \([0,1]\). It is not a theorem about arbitrary t-norms, restricted classes of valuations, nonstandard successor-only conventions at zero-weight rows, or axiom systems. Necessity uses standard choice to enumerate infinitely many positive successors. Prior literature on modal frame definability and compactness might contain a reformulation not found in the inspected sources; independence and originality are not externally certified.

## References

1. Mauro Ferrari, Camillo Fiorentini, Paolo Giardini, and Ricardo Oscar Rodriguez, *A Gödel Modal Logic Over Witnessed Models* (first publicly available 2026-06-30), arXiv:2606.31906, DOI:10.4204/EPTCS.447.20. https://arxiv.org/abs/2606.31906
2. Mauro Ferrari, Camillo Fiorentini, and Ricardo Oscar Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models* (2025), DOI:10.1007/978-3-032-06085-3_8. https://link.springer.com/chapter/10.1007/978-3-032-06085-3_8
3. Marta Bílková, Sabine Frittella, and Daniil Kozhemiachenko, *Paraconsistent Gödel Modal Logic* (2022), DOI:10.1007/978-3-031-10769-6_26, especially Section 3, Theorem 2. https://link.springer.com/chapter/10.1007/978-3-031-10769-6_26
