# Rational first-order limits for uniformly unlabelled coloured permutations

## Finding
Fix an integer \(q\geq2\). Let \(\mathcal U_{q,n}\) be the isomorphism classes of nonempty \(n\)-element structures with one bijective unary operation and an exhaustive disjoint partition into \(q\) named colours. Sample uniformly from \(\mathcal U_{q,n}\), **not** from labelled structures. Then for **every** first-order sentence \(\varphi\) in this signature there is a rational \(L_{q,\varphi}\in[0,1]\) and a constant \(\eta_{q,\varphi}<1\) such that
\[
\Pr_{\mathcal U_{q,n}}(\varphi)=L_{q,\varphi}+O_{q,\varphi}(\eta_{q,\varphi}^{n}).
\]
Moreover, for each fixed finite collection of directed cyclic colour words (necklaces) \(w\), the numbers of corresponding components converge jointly to independent geometric random variables with
\[
\Pr(M_w=j)=(1-q^{-|w|})q^{-j|w|}\quad(j=0,1,\ldots).
\]
In particular, if \(C\) is any one named colour, the first-order sentence asserting a fixed point of colour \(C\) has limit \(1/q\), exponentially fast. The contrasting one-colour case has an unlabelled first-order zero-one law, which is **previously known**; it is included only to locate the sharp colour boundary.

## Assumptions and scope
A structure has a finite universe \(V\), a bijection \(f:V\to V\), and named unary predicates \(P_1,\ldots,P_q\) partitioning \(V\). Isomorphisms preserve \(f\) and each named predicate separately. For \(n\geq1\), every isomorphism class has equal sampling mass; this differs from sampling a uniform labelled permutation and independent uniform vertex colours. First-order formulas may quantify over vertices and use arbitrarily nested terms \(f^j(x)\), but have fixed finite length and no order, counting or arithmetic predicates. The limiting result holds for every fixed \(q\geq2\) and every fixed sentence, with constants depending on that sentence.

A necklace is a \(q\)-letter word modulo **cyclic rotation** (not reflection), and its length is the cycle size. Let \(N_q(d)\) denote the number of necklaces of length \(d\), with no restriction to primitive words. Burnside's lemma gives
\[
N_q(d)=\frac1d\sum_{e\mid d}\phi(e)q^{d/e}.
\]
Write \(u_{q,n}=|\mathcal U_{q,n}|\), with \(u_{q,0}=1\) only for generating functions.

## Proof
**1. An isolated dominant pole.** Cycle decomposition identifies an isomorphism class with a multiset of coloured necklaces, hence its ordinary generating function is
\[
U_q(z)=\sum_{n\geq0}u_{q,n}z^n=\prod_{d\geq1}(1-z^d)^{-N_q(d)}.
\]
For \(q\geq2\), Burnside's expression implies \(N_q(d)=q^d/d+O(dq^{d/2})\). Expanding logarithms gives
\[
\log U_q(z)=-\log(1-qz)+B_q(z),
\]
where
\[
B_q(z)=\sum_{d\geq1}\left(N_q(d)-\frac{q^d}{d}\right)z^d
+\sum_{j\geq2}\frac1j\sum_{d\geq1}N_q(d)z^{dj}.
\]
Both series converge absolutely on every compact subdisk of \(|z|<q^{-1/2}\); the terms in the second series with \(j\geq2\) are controlled by \(q|z|^2<1\). Thus \(H_q(z)=\exp B_q(z)\) is analytic and nonzero there, and \(U_q(z)=H_q(z)/(1-qz)\). For any \(r\) with \(q^{-1}<r<q^{-1/2}\), coefficient extraction and Cauchy's estimate yield
\[
u_{q,n}=H_q(q^{-1})q^n+O_r(r^{-n}),\qquad H_q(q^{-1})>0.
\]
In particular, for every fixed integer \(s\geq0\), \(u_{q,n-s}/u_{q,n}=q^{-s}+O_s(\theta^n)\) for some \(\theta<1\).

**2. Exact component statistics.** For one fixed necklace \(w\) of length \(d\), replacing its factor by a prescribed multiplicity \(j\) yields
\[
\Pr_n(M_w=j)=\frac{u_{q,n-jd}-u_{q,n-(j+1)d}}{u_{q,n}},
\]
where counts at negative indices are zero. Step 1 yields the stated geometric limit; repeating the marking for any finite set of distinct necklaces establishes independence. More generally, for finitely many conditions of the form \(M_w=t_w\) or \(M_w\geq t_w\), the exact counting generating function is \(P(z)U_q(z)\), where \(P(z)\) is a finite product of factors \((1-z^{|w|})z^{t_w|w|}\) for exact conditions and \(z^{t_w|w|}\) for lower bounds. Its relative coefficient tends exponentially fast to the rational \(P(q^{-1})\). Finite unions of such events have rational limiting probabilities with exponential errors.

**3. Saturation of every long-cycle local type.** Fix integers \(R,T\geq1\), and a length \(L=2R+1\) colour word \(v\). Call a necklace *bad* if its cyclic word has fewer than \(T\) occurrences of \(v\). Let \(b_d\) count bad necklaces of length \(d\). Of the \(J=\lfloor d/L\rfloor\) disjoint blocks in a rooted linear representation of length \(d\), at most \(T-1\) can equal \(v\). Counting such words gives
\[
b_d\leq q^d\sum_{j=0}^{T-1}\binom{J}{j}q^{-Lj}(1-q^{-L})^{J-j}
\leq C_{q,R,T}d^{T-1}\beta^d
\]
for some \(\beta<q\). The first inequality is valid because each bad necklace has at least one rooted representation counted on the right. Consequently the generating function \(B_v(z)=\prod_{d\geq1}(1-z^d)^{-b_d}\) converges at some real \(r>q^{-1}\). Its coefficient at \(z^n\) counts structures containing **only** bad necklaces, so the probability of having no cycle with \(T\) occurrences of \(v\) is at most \(B_v(r)r^{-n}/u_{q,n}=O((qr)^{-n})\). A union bound makes this hold simultaneously for every length-\(L\) word. Thus, with exponentially high probability, every possible rooted radius-\(R\) neighbourhood type arising from sufficiently long cycles occurs at least \(T\) times.

**4. First-order locality.** Replace the unary function by its binary graph relation; this is a definitional translation, and the Gaifman graph of every permutation has degree at most two. The finite bounded-degree Hanf threshold-locality theorem supplies \(R,T\) such that the truth of the translated sentence is determined by the counts of rooted radius-\(R\) neighbourhood types truncated at \(T\). Radius-\(R\) neighbourhoods on cycles of size greater than \(2R+1\) are directed coloured paths with \(2R+1\) vertices; by Step 3 all such attainable types are saturated outside an exponentially unlikely event. The remaining neighbourhoods are contained in the finitely many necklaces of sizes at most \(2R+1\); their counts are finite linear combinations of the multiplicities \(M_w\) of these necklaces, with nonnegative integer coefficients. Their capped counts are determined by the capped multiplicities \(\min(M_w,T)\). Hence outside the exceptional event the sentence is a Boolean combination of finitely many exact/lower-bound multiplicity conditions. Step 2 proves that its probability has a rational limit and converges to it exponentially.

**5. The colour-one boundary and sampling distinction.** If \(q=1\), isomorphism types are integer partitions. Writing \(p(n)\) for the partition number, for each fixed cycle length \(d\) and threshold \(T\), \(\Pr(M_d\geq T)=p(n-Td)/p(n)\to1\) by classical partition asymptotics. Every finite list of rooted neighbourhood types is therefore saturated with probability tending to one, yielding the previously known unlabelled zero-one law. For the sentence \(\exists x\,(f(x)=x\wedge P_1(x))\), the uncoloured probability is \(p(n-1)/p(n)=1-\pi/\sqrt{6n}+O(n^{-1})\), so convergence need not be exponential there. For \(q\geq2\), Step 2 instead gives the limit \(q^{-1}\); for comparison the *labelled* uniform model yields \(1-e^{-1/q}\) from the Poisson fixed-point law. These are distinct sampling measures.

## Verification
The accompanying standalone `checker.py` evaluates the necklace counts independently by explicit rotation-orbit enumeration for \(q\in\{1,2,3\}\) and cycle lengths one through four. It computes the ordinary multiset Euler product to degree \(35\) by exact integer arithmetic and checks finite exact multiplicity identities, two-colour joint probabilities, known partition numbers, and convergence of the coloured fixed-point probability. Running `python checker.py` returns `ALL_CHECKS_OK`. These computations do not establish the infinite first-order claim; Steps 1–5 give the proof.

## Relationship to prior work
Kuželka (2026) supplies the timely unary-function/unlabelled-counting context, including a labelled automorphism-marking reduction, but his inspected full text does not state the first-order limit distribution of uniformly chosen unlabelled colour-decorated permutations. Albert, Bouvel and Féray (2018/2019) explicitly cite an unlabelled zero-one law for uncoloured bijections, due to Compton (1987): the \(q=1\) case here is **not** new. General component/ratio-test approaches of Compton and the account of Burris and Yeats are likewise antecedents. The claimed contribution is the \(q\geq2\) **complete rational first-order convergence law with an exponential error rate**, together with explicit independent geometric necklace statistics and the sharp contrast to \(q=1\). Standard necklace enumeration, Hanf locality and asymptotic coefficient techniques are used, not claimed as new. Previously reported labelled coloured-permutation automorphism-group limits do not imply the unlabelled first-order law because they use a different sampling measure and observable.

## Limitations
The proof assumes one bijective function, exactly one of \(q\) named colours at each vertex, a fixed number of colours and no built-in order. It does not cover arbitrary unary mappings, multiple functions, unlabeled sampling with nonuniform weights, or logical extensions with unbounded counting/modulo conditions. The locality theorem supplies formula-dependent \(R,T\), so the resulting exponential constant is not uniform across all formulas. The \(q=1\) zero-one conclusion is prior art. General combinatorial transfer theorems might subsume portions of the \(q\geq2\) statement under other terminology; historical priority has not been independently certified.

## References
1. O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580, first posted 2026-08-31. https://arxiv.org/abs/2608.30580.
2. M. Albert, M. Bouvel and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459v2 (2019), introduction and Sections 2 and 6. https://arxiv.org/html/1808.05459v2.
3. K. J. Compton, *A logical approach to asymptotic combinatorics I: First order properties*, Advances in Mathematics **65** (1987), 65–96, doi:10.1016/0001-8708(87)90019-3.
4. S. Burris and K. Yeats, *Sufficient Conditions for Labelled 0–1 Laws*, Discrete Mathematics and Theoretical Computer Science **10** (2008), 147–156, Section 6.1. https://dmtcs.episciences.org/430/pdf.
5. S. Lindell, H. Towsner and S. Weinstein, *Hanf Locality and Invariant Elementary Definability*, arXiv:2507.12450 (2025), discussion of the Fagin–Stockmeyer–Vardi bounded-degree threshold locality theorem. https://arxiv.org/abs/2507.12450.
