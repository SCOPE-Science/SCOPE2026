# Sharp witness spectrum of infinite Gödel modal frames

## Finding

Let \(W\ne\varnothing\), let \(R:W\times W\to[0,1]\), fix \(w\in W\), and write \(r_v=R(w,v)\). For an arbitrary function \(f:W\to[0,1]\), use the Gödel residual \(a\Rightarrow b=1\) when \(a\le b\), and \(a\Rightarrow b=b\) otherwise. Define
\[
B_w(f)=\inf_{v\in W}(r_v\Rightarrow f(v)),\qquad
D_w(f)=\sup_{v\in W}\min\{r_v,f(v)\}.
\]
An extremum is **witnessed** when one of the displayed terms equals it. These are the usual box and diamond evaluation clauses, without assuming that \(R\) is crisp.

**Theorem (sharp witness spectrum).** For each \(\delta\in[0,1]\), let \(\mathcal V_\delta\) be all functions from \(W\) to \(\{0\}\cup[\delta,1]\). Then the following hold.

1. The value \(B_w(f)\) is witnessed for **every** \(f\in\mathcal V_\delta\) if and only if \(\{v:r_v>\delta\}\) is finite. In particular, every unrestricted box input has a witness exactly when \(\{v:r_v>0\}\) is finite.
2. The value \(D_w(f)\) is witnessed for **every** function \(f:W\to[0,1]\) if and only if, for each \(\varepsilon>0\), the set \(\{v:r_v\ge\varepsilon\}\) is finite. Equivalently, robust diamond witnessing holds precisely when the row \(r\) vanishes at infinity in the finite-superlevel sense. It is also equivalent to robust box witnessing on \(\mathcal V_\delta\) for **every** \(\delta>0\).
3. Every finite-image input \(f\) has a witnessed box. Every finite-image input has a witnessed diamond if and only if **every nonempty subset** of the positive values \(\{r_v:r_v>0\}\) has a greatest element. Binary-valued inputs already test this last condition.
4. As \(\delta\) varies in \([0,1]\), the set of parameters for which every \(f\in\mathcal V_\delta\) has a witnessed box is exactly an upper interval containing \(1\). Conversely, every such interval occurs on a countable fuzzy frame: these are \([c,1]\), \(0\le c\le1\), and \((c,1]\), \(0\le c<1\).

Thus, in the **whole-world term-attainment convention defined above**, a fixed fuzzy frame \(W,R\) has attained box and diamond extrema for every propositional valuation, at every world and modal formula, precisely when each row has finitely many positive weights. Every valuation has attained diamond extrema precisely when each row has finite superlevel sets at all positive thresholds. Both frame characterizations hold for arbitrary modal nesting because the scalar extremum criteria apply to every formula-value function. Some alternative witnessed-model conventions additionally require a strictly positive-weight successor; the current theorem specifically concerns attainment of the displayed terms, so it does not assert equivalence to that stronger convention on zero-successor rows.

## Assumptions and scope

No countability, continuity, reflexivity, transitivity, or seriality assumption is imposed on the frame. We use ordinary classical set theory with the choice of a countably infinite subset from any infinite set (automatic for countable frames). The world set is nonempty. We compute modal extrema over **all** worlds, including worlds with zero accessibility weight: such worlds contribute \(1\) to the box terms and \(0\) to the diamond terms. Thus an empty positive successor set still has witnessed extrema in this convention, although a positive successor is not required as the witness in that degenerate case.

Items 1 and 3 concern scalar inputs to one modal operation. The restriction in item 1 that every positive input degree is at least \(\delta\) is not presumed to be preserved by nested modal formulas; only the unrestricted frame consequences following item 4 assert witnessing at arbitrary modal depth.

## Proof

**Box at a positive-degree cutoff.** Fix \(\delta\in[0,1]\). Suppose \(S_\delta=\{v:r_v>\delta\}\) is finite. Let \(f\in\mathcal V_\delta\). If some \(v\) has \(r_v>0\) and \(f(v)=0\), its box term is \(0\) and witnesses the infimum. Otherwise, at every world with \(r_v\le\delta\), either \(r_v=0\) or \(f(v)\ge\delta\ge r_v\); the box term is \(1\). All terms below \(1\) are therefore confined to the finite set \(S_\delta\). Their infimum is a minimum (or all terms equal \(1\)), proving witnessing.

Conversely, suppose \(S_\delta\) is infinite, and choose distinct \(v_k\in S_\delta\) for \(k\ge1\). Set
\[
f(v_k)=\delta+\min\!\left\{\frac{r_{v_k}-\delta}{2},\frac1{k+1}\right\},\qquad f(v)=1\quad(v\notin\{v_k:k\ge1\}).
\]
For each \(k\), \(\delta<f(v_k)<r_{v_k}\), so its residual is \(f(v_k)\), strictly above \(\delta\). Every other residual equals \(1\). Yet \(f(v_k)\to\delta\), and hence \(B_w(f)=\delta\) is not attained. This includes \(\delta=0\); for \(\delta=1\) the hypothesized infinite superlevel set is impossible. Item 1 follows.

**Unrestricted diamond.** Suppose all positive superlevels of \(r\) are finite. Given \(f\), let \(s=D_w(f)\). If \(s=0\), every term is zero and any world witnesses it. If \(s>0\), only finitely many worlds satisfy \(r_v\ge s/2\), while all other terms are at most \(s/2<s\). Thus the supremum is the maximum of finitely many terms and is attained. Conversely, if \(\{v:r_v\ge\varepsilon\}\) is infinite for some \(\varepsilon>0\), choose distinct \(v_k\) there and put \(f(v_k)=\varepsilon k/(k+1)\), with \(f=0\) elsewhere. The diamond terms are \(\varepsilon k/(k+1)\) on the sequence and zero elsewhere. Their supremum \(\varepsilon\) is not attained. This proves item 2's main equivalence. Moreover, finite \(\{r_v\ge\varepsilon\}\) at all \(\varepsilon>0\) implies finite \(\{r_v>\delta\}\) at every \(\delta>0\); the reverse implication follows by taking \(\delta=\varepsilon/2\). Together with item 1, this proves the claimed intersection identity.

**Finite palettes.** For finite-image \(f\), each box residual lies in \(\{1\}\cup f(W)\), a finite set, so its infimum occurs among the terms. For the diamond, first assume every nonempty subset of positive \(r\)-values has a greatest element. Partition \(W\) into the finitely many nonempty level sets of \(f\). On a level \(f(v)=a\), the supremum of \(\min\{r_v,a\}\) is attained: this is immediate if \(a=0\) or all \(r_v=0\), and otherwise follows by taking a largest positive \(r_v\) on that level. The largest among these finitely many witnessed levelwise maxima witnesses the full diamond. Conversely, if a nonempty subset \(T\subseteq\{r_v:r_v>0\}\) lacks a greatest element, choose the binary input \(f(v)=1\) exactly when \(r_v\in T\), and zero otherwise. Then \(D_w(f)=\sup T>0\) is not attained. This proves item 3.

**Complete cutoff spectrum.** By item 1, robust box witnessing holds at \(\delta\) exactly when the strict superlevel above \(\delta\) is finite. This property is upward closed, and holds at \(1\). Every upward subset of the interval \([0,1]\) that contains \(1\) is of the claimed closed-left or open-left form. To realize \((c,1]\), for \(0\le c<1\), take one distinguished row with positive entries \(r_{v_k}=c+(1-c)/(k+1)\) for \(k\ge1\). It has infinitely many entries strictly above \(c\), but only finitely many strictly above any \(\delta>c\). To realize \([c,1]\) for \(0<c\le1\), instead take \(r_{v_k}=ck/(k+1)\), whose terms are strictly below \(c\) and converge upward to \(c\). For \([0,1]\), take a finitely supported row. Other rows may be identically zero. This proves item 4.

**Frame conclusions and strict boundary.** Apply items 1 and 2 separately at every source world. If a row fails its condition, the nonattainment witness above is the valuation of a single atom, so no modal-nesting qualification can repair necessity. Conversely, the scalar condition applies to the value function of every formula, yielding witnesses at each modal occurrence. The row \(r_{v_k}=1/(k+1)\) has all positive superlevels finite but infinitely many positive entries: all valuations witness every diamond at the source world, yet the box input \(f(v_k)=1/(k+1)^2\), \(f=1\) elsewhere, has unwitnessed infimum \(0\). Finally \(r_{v_k}=1/2+1/(2(k+1))\) has reverse-well-ordered positive range, so all finite-image diamonds are witnessed, but it fails unrestricted diamond witnessing because infinitely many weights exceed \(1/2\). These explicit separations complete the classification.

## Verification

The standalone `checker.py` uses exact rational arithmetic to verify both modal evaluation definitions over all rows and valuations from a four-degree palette through length three, and the stated rational finite-prefix identities for the boundary examples at lengths \(4,8,16,32\). Replay with `python3 checker.py`; expected terminal line is `EXACT_PREFIX_CHECKS_OK: enumerations n<=3; illustrative prefixes 4,8,16,32`. Finite prefixes **do not prove** infinite nonattainment; the limiting arguments above supply those proofs. All calculations are independent of outside data and need only Python's standard library.

## Relationship to prior work

Caicedo and Rodriguez (2009) establish the original arbitrary fuzzy Gödel-Kripke infimum/supremum semantics and completeness of its modal fragments. Ferrari, Fiorentini, Giardini and Rodriguez (2026) introduce the fully witnessed fuzzy Gödel modal semantics and develop a refutation calculus and finite-model property. Vidal and Rodriguez (2026) separately establish completeness and distinctions among full, diamond-only and partial witnessing conditions. The present result asks a different **frame-uniform** question: for which fixed accessibility rows is the witnessing property guaranteed under **every valuation**? The row-finiteness, positive-superlevel, palette, and cutoff classifications are not stated in the inspected relevant portions of those papers.

Bílková, Frittella and Kozhemiachenko (2022) prove finite-branching definability for a distinct bi-Gödel/paraconsistent language, with a fuzzy-frame side condition for a related theorem; that result neither identifies the all-valuation diamond superlevel condition nor the sharp guarded-box spectrum here. Earlier fuzzy-description-logic work supplies the conceptual distinction between witnessed and unwitnessed quantifier extrema, but does not establish these frame-wide equivalences. These comparisons are limited to inspected material; a differently formulated result in older fuzzy-relation literature could subsume part of the elementary extremum analysis.

## Limitations

The theorem classifies witness attainment, not logical validity, axiomatizability, decision complexity, or any finite-model bound. The cutoff clause is only for one scalar box operation applied to \(\mathcal V_\delta\); without further assumptions there is **no claim** that nested formula values stay within \(\mathcal V_\delta\). The finite-palette characterization is likewise about individual scalar inputs, not full nested finite-valued modal models. There is no assertion of independent verification or exhaustive bibliographic novelty. The stronger full-valuation frame statements do apply to arbitrarily nested formulas, for the reason proved above.

## References

1. X. Caicedo and R. O. Rodriguez, *A Godel Modal Logic*, arXiv:0903.2767, first posted 2009-03-16, https://arxiv.org/abs/0903.2767.
2. M. Ferrari, C. Fiorentini, P. Giardini and R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, arXiv:2606.31906, first posted 2026-06-30, https://arxiv.org/abs/2606.31906.
3. A. Vidal and R. O. Rodriguez, *Axiomatizing logics of finite Gödel-Kripke models*, arXiv:2605.15810, first posted 2026-05-15, https://arxiv.org/abs/2605.15810.
4. M. Bílková, S. Frittella and D. Kozhemiachenko, *Paraconsistent Gödel Modal Logic*, IJCAR 2022, DOI 10.1007/978-3-031-10769-6_26, https://link.springer.com/chapter/10.1007/978-3-031-10769-6_26.
5. M. Ferrari, C. Fiorentini and R. O. Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models*, TABLEAUX 2025, DOI 10.1007/978-3-032-06085-3_8.
