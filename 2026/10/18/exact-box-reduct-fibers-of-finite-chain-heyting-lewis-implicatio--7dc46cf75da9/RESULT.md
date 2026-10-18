# Exact box-reduct fibers of finite-chain Heyting–Lewis implication

## Finding

**Theorem (box-reduct reconstruction fibers).** Fix an integer \(n\geq1\). Let \(G_n=\{c_0<c_1<\cdots<c_n\}\) be the fixed \((n+1)\)-element Gödel (Heyting) chain. A **Heyting–Lewis expansion** is a binary connective \(\Rightarrow\) satisfying the four weak-Heyting identities specified below; its **box reduct** is \(\Box a=c_n\Rightarrow a\). All expansions are considered on this *fixed labelled chain*, without quotienting by isomorphism.

1. Each expansion is uniquely specified by arbitrary adjacent-edge values \(d_k=c_k\Rightarrow c_{k-1}\in G_n\), for \(1\leq k\leq n\), through
\[
 c_a\Rightarrow c_b=
 \begin{cases}
 c_n,&a\leq b,\\
 \bigwedge_{k=b+1}^{a}d_k,&a>b.
 \end{cases}
\]
 Thus there are \((n+1)^n\) binary expansions.
2. Exactly \(\binom{2n}{n}\) distinct box reducts occur: precisely all order-preserving unary operators \(\Box:G_n\to G_n\) with \(\Box c_n=c_n\) (equivalently, all normal meet-preserving unary operators on the chain).
3. Fix such a box reduct, and put \(b_i=\Box c_i\) for \(0\leq i<n\); then \(b_0\leq\cdots\leq b_{n-1}\). Its exact number of distinct compatible strict implications is
\[
 \boxed{\quad
  |\operatorname{Fib}(\Box)|=
  \prod_{\substack{0\leq i<n-1\\b_i=b_{i+1}}}
  |[b_i,c_n]|.\quad}
\]
 In the ordinal labeling \(b_i=c_{s_i}\), the factor is \(n-s_i+1\). Empty products equal one.
4. Exactly \(2^n\) of the \(\binom{2n}{n}\) box reducts uniquely determine their strict implication. Equivalently, every equality plateau in the sequence \(b_0,\ldots,b_{n-1}\) must occur at the top \(c_n\). Consequently, only \(2^n\) of all \((n+1)^n\) expansions have a singleton box fiber. The largest fiber has size \((n+1)^{n-1}\); for \(n\geq2\) it is uniquely attained by the box that sends every \(c_i\) below top to bottom \(c_0\).

The theorem concerns reconstruction *among possible finite-chain expansions*, not syntactic term-definability of strict implication from box.

## Assumptions and scope

The fixed Heyting chain has \(n+1\) elements with lattice meet \(\wedge=\min\), join \(\vee=\max\), and its uniquely determined ordinary Heyting arrow. The independent additional binary connective \(\Rightarrow\) is required to satisfy, for all \(x,y,z\in G_n\),
\[
\begin{aligned}
(x\Rightarrow y)\wedge(x\Rightarrow z)&=x\Rightarrow(y\wedge z),\\
(x\Rightarrow z)\wedge(y\Rightarrow z)&=(x\vee y)\Rightarrow z,\\
(x\Rightarrow y)\wedge(y\Rightarrow z)&\leq x\Rightarrow z,\\
x\Rightarrow x&=c_n.
\end{aligned}
\]
These are the weak-Heyting axioms defining the strict connective in Heyting–Lewis algebras. No idempotence, reflexivity of a relational accessibility relation, or compatibility equation with the ordinary Heyting arrow is imposed beyond these four identities. For \(n=1\), the theorem includes the degenerate one-edge case.

## Proof

**Step 1: Edge normal form.** The first identity implies monotonicity of \(x\Rightarrow y\) in its consequent, and the second implies antitonicity in its antecedent. The fourth identity then gives \(c_a\Rightarrow c_b=c_n\) whenever \(a\leq b\). For \(a>b\), monotonicities yield
\[
 c_a\Rightarrow c_b\leq c_k\Rightarrow c_{k-1}=d_k
 \quad(b<k\leq a).
\]
Therefore the long-arrow value is at most the meet of its adjacent-edge values. Iterating the third identity along the adjacent chain gives the reverse inequality; hence the displayed edge formula is necessary.

Conversely, choose arbitrary \(d_1,\dots,d_n\in G_n\) and define the arrow by that formula. It is antitone in its first input and isotone in its second; on a chain these two statements imply the first two weak-Heyting identities. The diagonal identity holds by convention. For transitivity, whenever \(a>c\), the interval of edge indices \((c,a]\) is contained in the union \((b,a]\cup(c,b]\), omitting empty intervals. Thus the meet of the two short-arrow values is at most the meet over \((c,a]\); if \(a\leq c\), the required upper bound is the top element. This establishes the third identity. Distinct adjacent-edge vectors give distinct arrows because \(d_k=c_k\Rightarrow c_{k-1}\). The count follows.

**Step 2: Box and its fibers.** For every \(0\leq i<n\), the edge normal form gives
\[
 b_i=\Box c_i=\bigwedge_{k=i+1}^{n}d_k,\qquad
 b_{n-1}=d_n.
\]
Consequently \(b_0\leq\cdots\leq b_{n-1}\). Conversely, any weakly increasing \(n\)-tuple of values in \(G_n\) is realized by taking \(d_{i+1}=b_i\). This is a bijection between box reducts and multisets of \(n\) values chosen from \(n+1\) ordered values, giving \(\binom{2n}{n}\).

Recover the edges backwards. At the final edge \(d_n=b_{n-1}\) is forced. For \(1\leq k<n\),
\[
 b_{k-1}=d_k\wedge b_k.
\]
If \(b_{k-1}<b_k\), only \(d_k=b_{k-1}\) works. If \(b_{k-1}=b_k\), the edge \(d_k\) can be any value at least \(b_k\); there are exactly \(|[b_k,c_n]|\) such values. All choices at different positions are independent, proving the product formula.

**Step 3: Unique recovery and maximal ambiguity.** A fiber has cardinality one exactly when every repeated successive box value equals \(c_n\). Such a box sequence consists of a strictly increasing list of some subset of \(\{c_0,\ldots,c_{n-1}\}\), followed by enough \(c_n\)'s to reach length \(n\). Each subset is unique and admissible, giving \(2^n\) singleton fibers. There are \(n-1\) possible free-edge factors, each at most \(n+1\); equality throughout occurs precisely when all box values are \(c_0\), for \(n\geq2\). For \(n=1\), every fiber has size one. QED.

## Verification

The accompanying standard-library Python program `verify.py` independently checks all four weak-Heyting identities on every edge-parameter operation for \(1\leq n\leq5\), reconstructs each box fiber, and checks its closed product formula, the central-binomial count, the \(2^n\) singleton count and maximal fiber. It separately brute-forces all \(3^9\) possible binary operation tables on the three-element chain against the axioms; exactly nine survive, coinciding with the edge-parametrized operations. The finite checks do not substitute for the proof for all \(n\).

## Relationship to prior work

De Groot, Litak and Pattinson's Heyting–Lewis semantics identifies the four weak-Heyting identities for constructive strict implication and explicitly notes that the full strict connective is in general not definable from its unary box. The present theorem studies a distinct finite inverse problem: the number and complete fiber profile of *all* strict arrows inducing each chosen box on a fixed Gödel chain. Alizadeh and Joharizadeh previously give a general algorithm for enumerating weak Heyting structures on finite distributive lattices; the elementary total count is not advanced here as independently new. The claimed additional content is the exact box-forgetful fiber formula and complete uniqueness/maximal-ambiguity classification. Celani studies varieties of \(n\)-linear weak Heyting algebras, without an identified instance of this exact forgetful-map classification.

## Limitations

The formulas are for a fixed finite chain and arbitrary weak-Heyting strict arrows; they do not classify additional axioms for specialized Heyting–Lewis logics or establish syntactic definability. An older enumeration of finite weak Heyting algebras could conceivably contain an equivalent unary-reduct refinement; its full manuscript was inaccessible in the source access used for this comparison. Independent mathematical and originality validation have not been performed.

## References

1. J. de Groot, T. Litak and D. Pattinson, *Gödel–McKinsey–Tarski and (not quite) Blok–Esakia for Heyting–Lewis Implication*, arXiv:2105.01873 (first publicly available 2021-05-05; revised 2026). Sections on axioms, algebras and strict-implication frames. https://arxiv.org/abs/2105.01873
2. M. Alizadeh and N. Joharizadeh, *Counting weak Heyting algebras on finite distributive lattices*, Logic Journal of the IGPL 23 (2015), 247–258, doi:10.1093/jigpal/jzu033 (abstract and indexing accessible; complete paper not inspected).
3. S. A. Celani, *n-linear weakly Heyting algebras*, Mathematical Logic Quarterly 52 (2006), 404–416, doi:10.1002/malq.200510041 (abstract accessible).
