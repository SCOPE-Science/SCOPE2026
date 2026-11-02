# An exact extinction dichotomy for uniformly sampled one-agent S5 announcements

## Finding

Fix an integer \(k\geq0\), let \(T=\{0,1\}^k\), and put \(m=|T|=2^k\). Consider announcement-free epistemic formulas over the \(k\) propositional letters, Boolean connectives (including constants \(\top,\bot\)), and one S5 knowledge operator \(K\), identified when equivalent on **all** S5 models. Repeatedly announce the same formula by ordinary truthful public announcement (deleting non-satisfying worlds, not deleting arrows into them). We allow the resulting model to be empty.

Every semantic formula class corresponds bijectively to a map \(F:2^T\to2^T\) satisfying \(F(S)\subseteq S\) for all \(S\subseteq T\). The map records the set of atomic valuation types surviving an announcement in an equivalence class whose present type support is \(S\). Every such map is realized by a formula of modal depth at most one. Therefore the number of distinct semantic announcement classes is
\[
A_m=2^{m2^{m-1}}.
\]

Sample one of these \(A_m\) semantic classes uniformly. For **every specified nonempty initial type support** \(S\subseteq T\), the probability that repeating the sampled announcement eventually removes every world of that S5 class is exactly
\[
\Pr(F^{\circ n}(S)=\varnothing\text{ for some }n)=\frac12.
\]
By contrast, the probability that the sampled formula eventually empties **every** S5 model, equivalently every nonempty type support, is
\[
P_m=\prod_{j=1}^{m}(1-2^{-j})^{\binom mj}
     =\frac{\prod_{j=1}^{m}(2^j-1)^{\binom mj}}{2^{m2^{m-1}}}.
\]
This probability has the logarithmic asymptotic
\[
\log P_m=-\left(\frac32\right)^m-\frac12\left(\frac54\right)^m
      +O\!\left(\left(\frac98\right)^m\right)\quad(m\to\infty).
\]
In particular, a typical semantic formula has a one-half chance of extinguishing any *fixed* class, whereas formulas guaranteed to extinguish *all* classes are extraordinarily rare as the vocabulary grows.

More exactly, if \(Z\) is the number of nonempty supports that remain unchanged after one announcement, then its probability-generating function is
\[
\mathbb E[z^Z]=\prod_{j=1}^m\bigl(1+(z-1)2^{-j}\bigr)^{\binom mj},
\]
and \(\mathbb E Z=(3/2)^m-1\), \(\operatorname{Var}(Z)=(3/2)^m-(5/4)^m\). Eventual universal extinction is exactly the event \(Z=0\). For \(k=2\) (so \(m=4\)), there are \(2^{32}=4{,}294{,}967{,}296\) distinct formula classes and exactly \(26{,}254{,}935\) universally extinguishing classes.

## Assumptions and scope

An S5 model is \((W,R,V)\) with nonempty \(W\), an equivalence relation \(R\), and Boolean valuations of exactly \(k\) fixed propositional letters. Models may be infinite, and distinct worlds may have the same atomic type. For each equivalence class \(C\), its *support* \(S(C)\subseteq T\) is the nonempty set of types realized by worlds in \(C\). The semantic classes of formulas are equivalence classes **over all such models**, not by formula length or syntax. Their uniform distribution is defined by the finite set of semantic classes, rather than a distribution on formula strings or models. Ordinary public announcement deletes worlds failing the formula and restricts \(R\) and \(V\) to the survivors. Iteration always reevaluates the **same** announcement-free formula in the current submodel. After extinction the empty support is terminal by convention.

The assertion of probability \(1/2\) concerns any one specified equivalence class and its initial type support; it does **not** assert the same probability for simultaneous extinction of several distinct classes in a fixed multi-class model. Universal extinction quantifies over all possible S5 models.

## Proof

**Support invariance and realization.** Let \(\tau_t\) be the conjunction of the corresponding positive or negative literals for \(t\in T\). A structural induction on a formula shows that its truth at a world depends only on the pair \((t,S)\), where \(t\) is the world's atomic type and \(S\) is the support of its S5 equivalence class. The induction step for \(K\psi\) holds because every world in the class sees precisely that class, so \(K\psi\) is true iff \(\psi\) is true for every type in \(S\). In particular the multiplicity of any type is irrelevant.

Conversely, for each \(S\subseteq T\) define
\[
\chi_S=\bigwedge_{t\in S}\neg K\neg\tau_t\ \wedge\
        \bigwedge_{t\notin S}K\neg\tau_t.
\]
At any world of a nonempty S5 class, \(\chi_S\) holds exactly when the class support is \(S\). Given any map \(F\) with \(F(S)\subseteq S\), set
\[
\varphi_F=\bigvee_{S\subseteq T}
 \left(\chi_S\wedge\bigvee_{t\in F(S)}\tau_t\right),
\]
with empty disjunction interpreted as false. This modal-depth-one formula holds at a world of type \(t\) in support \(S\) exactly if \(t\in F(S)\). It therefore deletes exactly the other types. Every \((S,t)\) with \(t\in S\) is witnessed by a finite S5 model with one world per type in \(S\), proving that two distinct maps correspond to distinct semantic formula classes. Since \(F(\varnothing)=\varnothing\), there are \(\prod_{S\subseteq T}2^{|S|}=2^{m2^{m-1}}\) such maps.

**Iteration and fixed supports.** Repeating \(\varphi_F\) on a class with initial support \(S\) produces \(S,F(S),F^{\circ2}(S),\ldots\), because an announcement either retains every world of a given type or none of them. Since \(F(U)\subseteq U\), each strict change removes at least one type; an orbit stabilizes within at most \(|S|\) strict changes. A nonempty fixed support \(U\) provides a model that cannot be extinguished, and conversely a nonempty terminal support of any orbit must be fixed. Thus universal extinction is equivalent to \(F(U)\ne U\) for every nonempty \(U\subseteq T\).

**Uniform semantics and the fixed-support census.** Sampling a map \(F\) uniformly from the finite Cartesian product of all choices \(F(U)\subseteq U\) makes the values \(F(U)\) independent and uniformly distributed over \(2^U\). Hence the indicator of \(F(U)=U\) is Bernoulli with parameter \(2^{-|U|}\), independently over nonempty \(U\). Their sum is \(Z\), giving its generating function, expectation and variance. The event \(Z=0\) has probability \(\prod_{U\ne\varnothing}(1-2^{-|U|})=P_m\), and the number of maps with this property is \(\prod_{j=1}^m(2^j-1)^{\binom mj}\).

**The one-half law.** Fix nonempty \(S\) with \(|S|=n\), and write \(e_n\) for the probability, under a uniformly sampled \(F\), that its orbit from \(S\) eventually reaches the empty support. This depends only on \(n\). Set \(e_0=1\). The value \(F(S)\) is uniform over the \(2^n\) subsets of \(S\). If \(F(S)=S\), extinction fails. If \(F(S)=U\subsetneq S\), the independent choices of \(F\) on all subsets of \(U\) have the original uniform distribution, so the conditional extinction probability is \(e_{|U|}\). Therefore
\[
 e_n=2^{-n}\sum_{U\subsetneq S}e_{|U|}.
\]
Induction using \(e_j=1/2\) for \(1\le j<n\) gives
\[
 e_n=2^{-n}\left(1+\frac12(2^n-2)\right)=\frac12,
\]
for every \(n\ge1\), including the base case.

**Asymptotic rarity.** Expanding \(\log(1-x)\), interchanging a finite outer sum and an absolutely convergent positive series, and using the binomial theorem yield
\[
\log P_m=-\sum_{r\ge1}\frac{(1+2^{-r})^m-1}{r}.
\]
The terms \(r=1,2\) give the two displayed leading exponentials. For \(r\ge3\), convexity of \((1+x)^m-1\), vanishing at \(x=0\), implies
\[
(1+2^{-r})^m-1\le 2^{3-r}\bigl((9/8)^m-1\bigr).
\]
The remaining sum is therefore at most a constant times \((9/8)^m\). Constants from the first two terms are absorbed into the stated error. This proves the asymptotic for every integer sequence \(m\to\infty\), in particular the vocabulary sizes \(m=2^k\).

## Verification

Run `python3 checker.py` from the directory containing this result. The standalone program enumerates every anti-extensive map for \(m=1,2,3\), checks the extinction probability for every nonempty initial support, checks the universal-extinction census, and verifies maximal-length chains as a secondary consistency check. It separately evaluates the characteristic modal-depth-one support tests for sampled maps to confirm realization. Exact results are: \(m=1\): \(2\) maps, \(1\) universally extinguishing; \(m=2\): \(16\) maps, \(3\) universally extinguishing; \(m=3\): \(4096\) maps, \(189\) universally extinguishing. The program emits `ALL_CHECKS_OK`. The general assertions rest on the symbolic proof, not on these finite tests.

## Relationship to prior work

The semantics of truthful public announcements and the qualitative connection between informative and eventually self-refuting single-agent S5 formulas are established in Holliday and Icard (2010), especially Proposition 5.7 and Corollary 5.8. Yamada (2026a) analyzes the logical relationships of eventual and strong eventual notions, chiefly in believed-public-announcement semantics; Yamada (2026b) characterizes unknowability and unbelievability in S5. The known general S5 support normal form and previously established bounds on finite-vocabulary stabilization provide the qualitative background, not a claimed novelty. The distinct question here is the **uniform measure on semantic formula classes**, its exact fixed-support distribution and universal-extinction census, and the one-half fixed-support extinction law. No theorem of the cited primary sources inspected establishes these quantitative assertions. See the separate review for the remaining historical-priority risk.

## Limitations

The uniform random object is a **semantic equivalence class**, not a randomly generated formula string, syntactic tree, valuation or frame. The modal-depth-one representation may have enormous size. This result is limited to one agent with S5 accessibility, finitely many Boolean propositional letters, and repetition of one announcement-free formula with world-deletion semantics. The one-half law concerns a specified single S5 equivalence class. Neither the quantitative theorem nor its proof extends automatically to multi-agent epistemic frames, non-equivalence accessibility, or arrow-deletion believed announcements. The formula-counting normal form is classical in spirit; the exact random-announcement laws are the claims assessed here for originality.

## References

1. Eiji Yamada, *Eventual and Strong Eventual Notions in Public Announcements* (2026), first submitted 2026-09-21, arXiv:2609.24006, https://arxiv.org/abs/2609.24006.
2. Eiji Yamada, *The Sources of Unknowability and Self-refutation in Epistemic and Dynamic Epistemic Logic* (2026), arXiv:2609.21317, https://arxiv.org/abs/2609.21317.
3. Wesley H. Holliday and Thomas F. Icard III, *Moorean Phenomena in Epistemic Logic*, Advances in Modal Logic 8 (2010), pp. 178–199, especially Proposition 5.7 and Corollary 5.8, https://philosophy.berkeley.edu/file/805/Moore.pdf.
