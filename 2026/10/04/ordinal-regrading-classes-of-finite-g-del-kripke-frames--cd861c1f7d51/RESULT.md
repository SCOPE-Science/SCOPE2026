# Ordinal regrading classes of finite Gödel Kripke frames
## Finding

Fix \(m\ge 1\) and the labelled world set
\[
W=\{0,\ldots,m-1\}.
\]
A fuzzy Gödel Kripke frame is \(F=(W,R)\) with
\[
R:W\times W\to[0,1].
\]
Two such frames on the same labelled world set are **regrading-equivalent** when
\[
R'=h\circ R
\]
for some strictly increasing homeomorphism \(h:[0,1]\to[0,1]\). Such a homeomorphism necessarily fixes \(0\) and \(1\).

For the standard Gödel modal language with propositional variables, \(\bot\), \(\wedge\), \(\vee\), \(\to\), \(\Box\), and \(\Diamond\), but no named intermediate truth constants, regrading-equivalent finite frames validate exactly the same formulas.

Moreover, every \(m\)-world frame has a unique canonical representative of its regrading class: if its distinct interior accessibility values are
\[
0<r_1<\cdots<r_k<1,
\]
replace each \(r_i\) by
\[
\frac{i}{k+1},
\]
while leaving \(0\) and \(1\) fixed.

Let \(N=m^2\), and let
\[
F_s=\sum_{k=0}^s k!\,S(s,k)
\]
be the \(s\)-th ordered Bell number, with \(S(s,k)\) the Stirling number of the second kind. The exact number of labelled regrading classes is
\[
T_N=\sum_{s=0}^N \binom Ns 2^{N-s}F_s.
\]
Thus the continuum of real-valued accessibility matrices on \(m\) labelled worlds collapses, for frame-validity purposes, to at most \(T_{m^2}\) canonical ordinal types. The first relevant values are
\[
T_1=3,\qquad T_4=299,\qquad T_9=28{,}349{,}043.
\]

The count is an exact count of regrading classes, not a claim that all those classes induce pairwise different modal logics.

## Assumptions and scope

The semantics is the fuzzy Gödel Kripke semantics used by Ferrari, Fiorentini, Giardini, and Rodriguez. For a model \(M=(W,R,e)\),
\[
e(w,\Box\alpha)=\inf_{v\in W}\bigl(R(w,v)\to e(v,\alpha)\bigr),
\]
and
\[
e(w,\Diamond\alpha)=\sup_{v\in W}\min\bigl(R(w,v),e(v,\alpha)\bigr),
\]
where Gödel implication is
\[
a\to b=
\begin{cases}
1,&a\le b,\\
b,&a>b.
\end{cases}
\]
Because \(W\) is finite, the infimum and supremum are minima and maxima, and every finite Gödel model is witnessed.

Frame validity means truth value \(1\) at every world under every valuation of propositional variables into \([0,1]\). The theorem uses the ordinary object language of \(\mathbf{GW}\), which has no named rational truth constants. Adding constants for specific intermediate values would generally destroy regrading invariance.

The exact census is for a fixed labelled world set. Quotienting also by permutations of worlds would give a smaller orbit count and is not treated here.

## Proof

Let \(h:[0,1]\to[0,1]\) be a strictly increasing homeomorphism. Since it is an order automorphism fixing the endpoints, for all \(a,b\in[0,1]\),
\[
h(\min(a,b))=\min(h(a),h(b)),
\qquad
h(\max(a,b))=\max(h(a),h(b)).
\]
It also preserves Gödel implication:
\[
h(a\to b)=h(a)\to h(b).
\]
Indeed, if \(a\le b\), both sides equal \(1\); if \(a>b\), both sides equal \(h(b)\).

Given a model \(M=(W,R,e)\), define its regrading
\[
M^h=(W,h\circ R,h\circ e),
\]
where on propositional variables
\[
e^h(w,p)=h(e(w,p)).
\]
We prove by structural induction that for every formula \(\varphi\) and every \(w\in W\),
\[
e^h(w,\varphi)=h(e(w,\varphi)).
\]
The atomic, \(\bot\), and propositional-connective cases follow from the preceding algebraic identities. For \(\Box\), finiteness of \(W\) gives
\[
\begin{aligned}
e^h(w,\Box\varphi)
&=\min_{v\in W}\bigl(h(R(w,v))\to h(e(v,\varphi))\bigr)\\
&=\min_{v\in W}h\bigl(R(w,v)\to e(v,\varphi)\bigr)\\
&=h\!\left(\min_{v\in W}\bigl(R(w,v)\to e(v,\varphi)\bigr)\right)\\
&=h(e(w,\Box\varphi)).
\end{aligned}
\]
The \(\Diamond\) case is identical with \(\max\) and \(\min\).

Because \(h(1)=1\), a formula has value \(1\) at a world in \(M\) exactly when it has value \(1\) at the corresponding world in \(M^h\). The transformation \(e\mapsto h\circ e\) is a bijection between valuations on \(F\) and valuations on \(F^h\), with inverse induced by \(h^{-1}\). Hence \(F\) and \(F^h\) have exactly the same frame-valid formulas.

Now fix a finite frame \(F\). Its finitely many distinct accessibility values form
\[
\{0,1\}\cup\{r_1<\cdots<r_k\},
\]
after omitting endpoints not actually attained by \(R\). Mapping \(r_i\) to \(i/(k+1)\) and fixing \(0,1\) extends piecewise linearly to an increasing homeomorphism of \([0,1]\). This yields the canonical representative. Uniqueness is immediate: the equality pattern, strict order among interior levels, and endpoint membership determine the canonical matrix entry by entry.

It remains to count the classes. There are \(N=m^2\) labelled matrix entries. Choose \(s\) entries that receive interior values: \(\binom Ns\) choices. Each of the other \(N-s\) entries independently receives endpoint \(0\) or \(1\): \(2^{N-s}\) choices. The \(s\) interior entries are partitioned into an ordered list of nonempty equality blocks, one block for each distinct interior level. The number of such ordered set partitions is
\[
F_s=\sum_{k=0}^s k!\,S(s,k).
\]
Multiplying and summing over \(s\) gives
\[
T_N=\sum_{s=0}^N\binom Ns2^{N-s}F_s.
\]
Every endpoint-anchored weak order is realized by its canonical equally spaced matrix, so this count is exact.

## Verification

The proof is exact and does not rely on finite experimentation.

The bundled checker performs two independent finite consistency tests. First, for \(N\le4\) labelled accessibility entries it enumerates raw tuples over a sufficiently long finite chain, rank-compresses each tuple while retaining the distinguished endpoints, and verifies that the number of canonical signatures equals the closed formula \(T_N\). It obtains
\[
3,\ 11,\ 51,\ 299
\]
for \(N=1,2,3,4\).

Second, it exhaustively checks the semantic commutation identity on small finite Gödel models and a generated family of modal formulas: strictly increasing regradings preserve \(\wedge,\vee,\to,\Box,\Diamond\) evaluation exactly after applying the same regrading to the valuation.

These computations corroborate the proof but are not used to justify the general theorem.

## Relationship to prior work

Ferrari, Fiorentini, Giardini, and Rodriguez define the fuzzy Gödel Kripke semantics used here, with both accessibility and propositional valuations taking values in \([0,1]\), and introduce the witnessed logic \(\mathbf{GW}\). They prove a finite model property and show that failed proof search yields a finite discrete countermodel. In their complexity analysis they also observe that only finitely many accessibility and atomic values are needed for a formula-specific countermodel and replace them by a finite rational set.

That result is close in spirit but has a different quantifier structure from the present statement. It asserts existence of a suitably finite-valued countermodel for each nonvalid formula. The present theorem fixes an arbitrary finite fuzzy frame first, transports **every valuation and every formula** through a common order regrading, obtains a canonical representative of the entire frame, and counts the resulting regrading classes exactly. It therefore gives a frame-level quotient rather than a formula-specific countermodel construction.

The earlier standard Gödel-modal papers of Caicedo and Rodriguez establish the underlying fuzzy Kripke semantics and completeness results. Searches in those sources and in the recent \(\mathbf{GW}\) paper did not locate the endpoint-anchored weak-order classification or the exact ordered-Bell census.

## Limitations

Regrading equivalence is sufficient for equality of frame-validity logics, not necessary: distinct regrading classes can still validate the same formulas. Accordingly, \(T_{m^2}\) is an exact orbit count and an upper bound on the number of frame logics, not an exact count of distinct logics.

The result uses finiteness of \(W\). For infinite frames, a general increasing homeomorphism still preserves existing infima and suprema because it is an order homeomorphism of the compact chain, but the canonical finite-level reduction and the finite census no longer apply.

The theorem is sensitive to the language. Named intermediate truth constants would pin numerical levels and invalidate arbitrary regrading.

## References

[1] Mauro Ferrari, Camillo Fiorentini, Paolo Giardini, and Ricardo Oscar Rodriguez, “A Gödel Modal Logic Over Witnessed Models,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 355–373. arXiv:2606.31906. DOI:10.4204/EPTCS.447.20.

[2] Xavier Caicedo and Ricardo O. Rodriguez, “Standard Gödel Modal Logics,” *Studia Logica* 94 (2010), 189–214. DOI:10.1007/s11225-010-9230-1.

[3] Xavier Caicedo and Ricardo O. Rodriguez, “Bi-modal Gödel logic over \([0,1]\)-valued Kripke frames,” *Journal of Logic and Computation* 25 (2015), 37–55. DOI:10.1093/logcom/exs014.
