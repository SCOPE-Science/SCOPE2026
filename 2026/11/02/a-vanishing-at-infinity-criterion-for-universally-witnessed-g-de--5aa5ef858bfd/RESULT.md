# A vanishing-at-infinity criterion for universally witnessed Gödel possibility

## Finding

Consider any nonempty set of worlds \(W\), any fuzzy accessibility relation \(R:W\times W\to[0,1]\), and ordinary Gödel-modal evaluations with arbitrary real truth degrees. The following is a **pointwise frame characterization**: at any world \(w\), every possibility formula \(\Diamond\varphi\) is witnessed there, under every valuation (including formulas containing nested necessity and possibility), **if and only if** each positive superlevel set \(\{v\in W:R(w,v)\ge\varepsilon\}\) is finite for every \(\varepsilon>0\).

This condition allows infinitely many positive-weight successors. It is equivalent to continuity of the local max-min possibility operator on the product cube, and to its uniform approximability by finite-successor operators. For every finite \(F\subseteq W\), the **exact** worst-case truncation error is

\[
\sup_{x\in[0,1]^W}\left[D_w(x)-D_{w,F}(x)\right]
=\sup_{v\notin F}R(w,v),
\]

where \(D_w(x)=\sup_{v\in W}\min\{R(w,v),x_v\}\) and \(D_{w,F}\) restricts this supremum to \(F\) (with the empty supremum equal to zero). This formula gives both a sharp finite-approximation certificate and a necessary-and-sufficient condition for arbitrarily accurate *uniform* finite approximation. In contrast, **every necessity formula is witnessed at \(w\) under every valuation if and only if \(w\) has only finitely many positive-weight successors**. Consequently the two notions coincide for crisp accessibility but differ strictly for fuzzy accessibility.

## Assumptions and scope

The carrier \(W\) is an arbitrary nonempty set, finite, countably infinite, or larger. No reflexivity, seriality, transitivity, or symmetry is assumed. The accessibility values \(R(w,v)\) and propositional truth values lie in the whole real interval \([0,1]\), independently. Gödel implication is \(a\Rightarrow b=1\) for \(a\le b\) and \(a\Rightarrow b=b\) otherwise. The modal clauses are

\[
 e(w,\Box\varphi)=\inf_{v\in W}(R(w,v)\Rightarrow e(v,\varphi)),
 \qquad e(w,\Diamond\varphi)=\sup_{v\in W}\min(R(w,v),e(v,\varphi)).
\]

A modal occurrence is *witnessed at \(w\)* precisely when its displayed infimum or supremum is attained by some \(v\in W\) in the corresponding weighted term. The condition on \(\Diamond\) (respectively \(\Box\)) below quantifies over **every valuation and every formula**, not merely over one chosen model; zero-weight successors are permitted as vacuous extremizers when the modal value is an endpoint. A world with no positive successors satisfies both conditions.

For fixed \(w\), write \(r_v=R(w,v)\), \(X=[0,1]^W\) with the product topology, and \(C_\varepsilon=\{v:r_v\ge\varepsilon\}\). The main equivalence concerns the following five statements:

1. Every \(C_\varepsilon\) is finite for \(\varepsilon>0\).
2. For each valuation and each formula \(\varphi\), the value of \(\Diamond\varphi\) at \(w\) is a maximum of the weighted successor terms.
3. For every \(x\in X\), \(D_w(x)\) attains its supremum at some coordinate.
4. The map \(D_w:X\to[0,1]\) is continuous for the product topology.
5. For every \(\eta>0\), some finite \(F\subseteq W\) satisfies \(\sup_{x\in X}|D_w(x)-D_{w,F}(x)|<\eta\).

The second assertion includes formulas with both modalities nested arbitrarily deeply. The assertion about \(\Box\) characterizes universal infimum attainment separately. These are structural/operational properties of a **fixed frame**, not completeness, decidability, or definability claims for an axiomatic logic.

## Proof

**Finite cut sets imply attainment.** Suppose each \(C_\varepsilon\) is finite, and let \(x\in X\). If \(s=D_w(x)=0\), each weighted term is zero and a coordinate attains the supremum because \(W\ne\varnothing\). If \(s>0\), take \(\varepsilon=s/2\). A coordinate whose weighted term exceeds \(s/2\) must lie in the finite set \(C_{s/2}\). Thus all terms outside this finite set are at most \(s/2\), while the supremum exceeds \(s/2\). The supremum therefore equals the maximum over that finite set. This proves statement 1 implies statement 3.

**Failure of a finite cut set produces a nonattained supremum.** If \(C_\varepsilon\) is infinite for some \(\varepsilon>0\), choose pairwise distinct \(v_n\in C_\varepsilon\), \(n\ge1\). Put \(x_{v_n}=(\varepsilon/2)\,n/(n+1)\) and set all other coordinates to zero. As \(r_{v_n}\ge\varepsilon\), the corresponding weighted terms are \((\varepsilon/2)n/(n+1)\), strictly increasing toward \(\varepsilon/2\), which no term attains. Therefore statement 3 implies statement 1. Since any \(x\in X\) can be realized as the values of one propositional variable under a suitable valuation, statement 2 implies statement 3. Conversely, any formula and valuation produce a vector \(x_v=e(v,\varphi)\in X\); hence statement 3 implies statement 2. This proves equivalence of the first three statements.

**Exact uniform truncation error.** For a finite set \(F\), write \(A=D_{w,F}(x)\), \(B=\sup_{v\notin F}\min(r_v,x_v)\) and \(t=\sup_{v\notin F}r_v\). Then \(D_w(x)=\max(A,B)\) and \(0\le D_w(x)-A\le t\). Take \(x_v=0\) on \(F\) and \(x_v=1\) outside \(F\). This yields \(A=0\) and \(D_w(x)=t\); equality follows. Therefore statement 1 implies statement 5 by choosing \(F=C_{\eta/2}\), and statement 5 implies statement 1 by the exact identity: if some \(C_\varepsilon\) is infinite, then every finite \(F\) leaves a tail of weight at least \(\varepsilon\).

Each finite-coordinate truncation is continuous in the product topology (minima and finite maxima are continuous). Uniform convergence proves statement 5 implies statement 4. Conversely, if some \(C_\varepsilon\) is infinite, then \(D_w\) is discontinuous at the all-zero vector: every basic product neighborhood of zero constrains only finitely many coordinates; choosing an unconstrained coordinate in \(C_\varepsilon\) and setting it to one produces a vector in that neighborhood with \(D_w(x)\ge\varepsilon\). Thus statement 4 implies statement 1. All five statements are equivalent.

**Necessity is stricter.** Suppose the set \(S_w=\{v:R(w,v)>0\}\) is finite. Terms at zero-weight successors in the necessity infimum are always one, so the infimum is attained among finitely many terms (or equals one everywhere if \(S_w\) is empty). Conversely, if \(S_w\) is infinite, choose distinct \(v_n\in S_w\). Assign a propositional variable the values \(p(v_n)=\frac12\min\{R(w,v_n),1/n\}>0\), and \(p(v)=1\) at all other worlds. At \(v_n\), the Gödel residuum is exactly \(p(v_n)\) because \(p(v_n)<R(w,v_n)\); elsewhere it is one. The infimum equals zero but is never attained. Therefore universal necessity witnessing at \(w\) is equivalent to finite positive support.

**Strict separation and sharp error.** Let \(W=\{o\}\cup\{v_n:n\ge1\}\), with \(R(o,v_n)=1/n\) and all other weights zero. At every world, every positive \(\varepsilon\)-cut is finite, so all possibility formulas in every model on this frame have witnesses. Yet at \(o\), the necessity construction above gives an unwitnessed \(\Box p\). The finite truncation retaining the first \(k\) edges of the row at \(o\) has exact worst-case error \(1/(k+1)\) (including \(k=0\)). With crisp weights \(R\in\{0,1\}\), finite positive cuts and finite positive support are the same property, so this separation requires genuinely fuzzy weights.

For completeness, finite positive cuts imply countable positive support: \(S_w=\bigcup_{m\ge1}C_{1/m}\), a countable union of finite sets. No assumption of countability of \(W\) was used in the theorem.

## Verification

The standard-library script `checker.py` exhaustively checks the sharp truncation identity for all weight and valuation vectors of lengths one through four over \(\{0,1/3,2/3,1\}\), and all finite truncation subsets. It tests 4,680 weight/subset configurations and, within each, every possible valuation vector. It also checks the finite stages of the decaying-edge example and the explicit monotone sequences used for nonattainment. Run `python3 checker.py`; the expected message begins `ALL_CHECKS_OK`.

These finite checks do not establish any assertion about infinite carriers. The proof above handles arbitrary \(W\), including uncountable sets. Continuity is with respect to the **product** topology, not the supremum-norm topology. The quantitative identity gives **uniform absolute** error over all valuation vectors, not a relative error bound.

## Relationship to prior work

Caicedo and Rodríguez (2011/2015) establish the Gödel-modal weighted semantics. Ferrari, Fiorentini and Rodríguez (2025) analyze witnessed *crisp* models, and Ferrari, Fiorentini, Giardini and Rodríguez (2026) develop calculi for witnessed *fuzzy* models. Vidal and Rodríguez (2026) study completeness under partial witnessing, including possibility-only witnessing. These sources supply the central semantic concepts and are not recast here as new. Bílková, Frittella and Kozhemiachenko (2022) already define finite branching within an enriched Gödel modal setting, and discuss the relation between finite branching and witnessed behavior; finite branching itself is therefore **not** a claimed novelty.

The present claim instead gives a frame-by-frame equivalence for **universal possibility-only witnessing under every valuation**, an exact product-topology continuity characterization, the optimal weighted finite-truncation error, and a strict contrast with universal necessity witnessing. It does not assert that possibility witnessing or finite branching was previously unknown. Sup-min fuzzy relational composition and the general principle of uniform finite-coordinate approximation are established background; the specific joint fixed-frame characterization is the candidate contribution. No full historical priority claim is made.

## Limitations

The theorem requires the standard real Gödel scale, its min-based possibility clause, unrestricted independent valuations, and the product topology. It does not automatically extend to an arbitrary t-norm or restricted atomic truth-value set. The result characterizes universal frame properties; it does not classify the witnessed models generated by a *single* valuation, prove any new completeness or finite model property theorem, or provide an algorithm for arbitrary noncomputable infinite rows. The explicit first-order/finite-model logical consequences of related literature are not reasserted here.

An unlocated earlier theorem in fuzzy relational equation theory, Sugeno/possibility integration, or general lattice aggregation could imply these identities under different terminology. The exact truncation formula is elementary once the operator is isolated; its value rests on the complete coupled modal/functional characterization and sharp computability boundary, not technical complexity.

## References

1. A. Vidal and R. O. Rodríguez, *Axiomatizing logics of finite Gödel-Kripke models*, first arXiv posting May 15, 2026, https://arxiv.org/abs/2605.15810 .
2. M. Ferrari, C. Fiorentini, P. Giardini and R. O. Rodríguez, *A Gödel Modal Logic Over Witnessed Models*, first arXiv posting June 30, 2026, https://arxiv.org/abs/2606.31906 .
3. X. Caicedo and R. O. Rodríguez, *Bi-modal Gödel logic over [0,1]-valued Kripke frames*, first arXiv posting October 11, 2011, https://arxiv.org/abs/1110.2407 .
4. M. Bílková, S. Frittella and D. Kozhemiachenko, *Paraconsistent Gödel Modal Logic* (2022), https://doi.org/10.1007/978-3-031-10769-6_26 .
5. M. Ferrari, C. Fiorentini and R. O. Rodríguez, *A Gödel Modal Logic over Witnessed Crisp Models* (2025), https://doi.org/10.1007/978-3-032-06085-3_8 .
6. E. Bartl and R. Bělohlávek, *Sup-t-norm and inf-residuum are a single type of relational equations* (2011), https://doi.org/10.1080/03081079.2011.571438 (relevant general operator background; abstract reviewed, full text not inspected).
