# A sharp rational first-order limit law for unlabelled coloured partial injections

## Finding
For every integer \(q\geq2\), sample uniformly from the isomorphism classes of \(n\)-element structures consisting of one binary directed relation whose in- and outdegrees are at most one and \(q\) named, exhaustive, mutually exclusive unary colours. For every first-order sentence \(\varphi\) in this language there is a **rational** number \(L_{q,\varphi}\) for which
\[
\Pr_n(\varphi)=L_{q,\varphi}+O_{q,\varphi}(n^{-1/2}).
\]
This error exponent is sharp, uniformly over first-order sentences for any fixed \(q\geq2\): the probability of an isolated vertex of one specified colour is
\[
\Pr_n(\exists x\,[P_1(x)\land\neg\exists y\,E(x,y)\land\neg\exists y\,E(y,x)])
=\frac1q-\frac1{q\sqrt n}+O_q(n^{-1}).
\]
The same family with \(q=1\) instead has a first-order **zero-one law**. The distinction is between *uniformly sampled isomorphism classes*; it is not a statement about a uniformly labelled partial injection.

More precisely, if \(M_\tau\) is the number of connected components of a fixed coloured directed chain-word or directed necklace type \(\tau\), then for every finite family of pairwise distinct types the joint component-count law tends, with error \(O(n^{-1/2})\) on every fixed cylinder event, to independent geometric distributions
\[
\Pr(M_\tau=j)=(1-q^{-\ell(\tau)})q^{-j\ell(\tau)},\qquad j=0,1,2,\ldots.
\]
These rational component limits give the first-order limits constructively via bounded-degree locality.

## Assumptions and scope
There is a finite nonempty carrier, a directed edge relation \(E\subseteq V\times V\) in which each vertex has at most one outgoing and at most one incoming edge, and unary predicates \(P_1,\dots,P_q\) forming an exact partition of \(V\). Loops are allowed and count as one-vertex directed cycles. A chain is an oriented finite directed path whose ends are not joined; isolated vertices are chains of length one. A cycle is directed and is identified under cyclic rotation, **not reversal**, of its colours. First-order formulas may quantify over vertices and refer to \(E\), equality and the colour predicates, but not to arithmetic, an external order, transitive closure or counting quantifiers. All \(n\)-element isomorphism classes receive equal probability.

Write \(c_q(\ell)=\ell^{-1}\sum_{d\mid\ell}\varphi(d)q^{\ell/d}\), the number of directed \(q\)-colour necklaces of length \(\ell\); \(\varphi\) in this definition denotes Euler's totient. There are exactly \(q^\ell\) chain types of that length. For \(a_{q,n}\), the total number of sampled classes, the ordinary generating function is
\[
A_q(z)=\sum_{n\ge0}a_{q,n}z^n
=\prod_{\ell\ge1}(1-z^\ell)^{-(q^\ell+c_q(\ell))}.
\]
For \(q\ge2\), set \(R=q^{-1}\). Define the analytic factor
\[
H_q(z)=\exp\!\left(
\sum_{\ell\ge1}\left(c_q(\ell)-\frac{q^\ell}{\ell}\right)z^\ell
+\sum_{j\ge2}\frac1j\sum_{\ell\ge1}(q^\ell+c_q(\ell))z^{j\ell}
\right).
\]
It is analytic and nonzero for \(\lvert z\rvert<q^{-1/2}\). The exact factorization and counting asymptotic are
\[
A_q(z)=\frac{H_q(z)}{1-qz}\exp\!\left(\frac{qz}{1-qz}\right),
\qquad
a_{q,n}=\frac{e^{-1/2}H_q(1/q)}{2\sqrt\pi}\,
q^n n^{-1/4}e^{2\sqrt n}(1+O_q(n^{-1/2})).
\]
No uniformity in \(q\) is asserted; it remains fixed as \(n\to\infty\).

## Proof
**1. Component species and enumeration.** A partial injection decomposes uniquely into oriented chains and oriented cycles. For each chain colour word or cyclic colour necklace, its isomorphism multiplicity is an arbitrary nonnegative integer. Taking an independent multiset factor \((1-z^\ell)^{-1}\) for each type proves the displayed Euler product. Burnside's rotation count proves the formula for \(c_q(\ell)\). Because
\[
c_q(\ell)=\frac{q^\ell}{\ell}+O_q(q^{\ell/2}),
\]
the singular part of the logarithm of the Euler product is \(qz/(1-qz)-\log(1-qz)\); the other terms converge analytically for \(\lvert z\rvert<q^{-1/2}\). This gives the factorization.

**2. Saddle-point coefficient transfer.** Put \(s=qz\). The base function
\[
(1-s)^{-1}\exp\!\left(\frac{s}{1-s}\right)
=\sum_{n\ge0}L_n(-1)s^n
\]
is the generating function of the ordinary Laguerre polynomials evaluated at \(-1\). Standard saddle-point expansion (or its positive real Cauchy integral at the saddle \(1-s\sim n^{-1/2}\)) gives
\[
L_n(-1)=\frac{e^{-1/2}}{2\sqrt\pi}n^{-1/4}e^{2\sqrt n}
(1+O(n^{-1/2})).
\]
Since \(H_q\) is analytic across the dominant positive singularity, Taylor expansion there and the same saddle-point estimates give, for every fixed polynomial \(P(z)\),
\[
\frac{[z^n]P(z)A_q(z)}{a_{q,n}}
=P(1/q)+O_{q,P}(n^{-1/2}).
\]
The smooth next-order saddle expansion, on replacing \(n\) with \(n-h\) for fixed \(h\), yields the sharper ratio
\[
\frac{a_{q,n-h}}{a_{q,n}}=q^{-h}
\left(1-\frac h{\sqrt n}+O_{q,h}(n^{-1})\right).
\]
The relevant coefficient errors are uniform over each fixed finite family of polynomial markings. For \(h=1\), this proves the sharp rate claimed below.

**3. Fixed component multiplicities.** A particular component type \(\tau\) of size \(\ell\) supplies a factor \((1-z^\ell)^{-1}\). Requiring exactly \(j\) copies replaces this factor by \(z^{j\ell}\), hence multiplies \(A_q(z)\) by \((1-z^\ell)z^{j\ell}\). For several distinct fixed types these polynomial factors multiply. The coefficient-ratio transfer in step 2 yields the claimed independent geometric laws, each with a \(O(n^{-1/2})\) fixed-event error. In particular, the event of at least one isolated vertex bearing colour \(1\) removes \((1-z)^{-1}\) from the generating function and has probability exactly \(a_{q,n-1}/a_{q,n}\). The ratio expansion proves its stated \(q^{-1}n^{-1/2}\) correction. This first-order sentence witnesses optimality of the general error exponent.

**4. First-order reduction to finitely many small components.** Fix a first-order sentence. Bounded-degree Hanf locality supplies a radius \(r\) and a threshold \(t\) such that its truth is determined by the numbers, truncated at \(t\), of realizations of all rooted, coloured, directed radius-\(r\) neighbourhoods. There are finitely many such types. A radius-\(r\) type containing both endpoints of a chain, or a cycle wrapping inside its radius, can occur only in a component of size at most \(2r+1\). Any other type is a *long-chain type*: it can be realized at a prescribed position of a sufficiently long chain whose initial or terminal finite colour word lies in a specified cylinder, as appropriate to whether the root lies near the left or right endpoint. Interior neighbourhoods use an initial cylinder with the root placed beyond its radius from either endpoint.

For such a fixed prefix or suffix cylinder of word length \(L\), exactly \(q^{\ell-L}\) chain types of each length \(\ell\ge L\) have the specified boundary word. The logarithm of the Euler product after forbidding those types has leading essential-singularity coefficient \(1-q^{-L}<1\), in place of \(1\). For a fixed number of marked cylinder components, the restricted generating function is bounded on the positive real interval by a fixed power of \((1-qz)^{-1}\) times \(\exp(\alpha qz/(1-qz))\), where \(\alpha=1-q^{-L}\). The elementary positive-coefficient Cauchy bound at \(qz=1-\sqrt{\alpha/n}\), divided by the lower asymptotic from step 2, implies that the chance of fewer than \(t\) components of that prefix/suffix class is at most
\[
O_{q,L,t}\bigl(n^{K}\exp(-2(1-\sqrt{1-q^{-L}})\sqrt n)\bigr)
\]
for some finite constant \(K=K(q,L,t)\). Indeed, marking a fixed number of exceptional boundary-word components contributes only a polynomial factor in \((1-qz)^{-1}\) to this restricted Euler product. Every realizable long-chain neighbourhood therefore occurs at least \(t\) times, outside an error that is smaller than \(n^{-1/2}\). The number of cylinder patterns used is finite.

Consequently the sentence, except on that negligible event, depends only on the truncated multiplicities of the finitely many chain and cycle types of size at most \(2r+1\). (Increasing this finite cutoff by one if necessary also handles borderline neighbourhoods.) The set of permitted tuples of truncated counts is finite. Step 3 gives every such event a rational limit, with an \(O(n^{-1/2})\) error. Summing finitely many disjoint events proves the first-order rational convergence assertion.

**5. The one-colour boundary.** When \(q=1\), for each size \(\ell\) there are exactly two component types (a chain and a cycle), so \(A_1(z)=\prod_{\ell\ge1}(1-z^\ell)^{-2}\). Classical partition asymptotics, or a direct saddle-point estimate at \(z\uparrow1\), give \(a_{1,n-h}/a_{1,n}\to1\) for every fixed \(h\). Thus the chance of at least \(t\) copies of any fixed component type of size \(\ell\) tends to one, because that probability is exactly \(a_{1,n-t\ell}/a_{1,n}\). Every realizable radius-\(r\) neighbourhood can be witnessed inside some fixed finite chain or cycle component and hence occurs at least \(t\) times with probability tending to one. Hanf locality makes each first-order sentence eventually constant with probability tending to one; therefore its limit belongs to \(\{0,1\}\).

## Verification
The independent finite checker included with this note enumerates every directed partial injection on labelled carriers through four vertices for one, two and three colours, canonicalizes chain words and directed necklaces, and compares the number of distinct isomorphism types with the integer Euler-product coefficient recurrence. For two colours it obtains the counts \(1,4,17,60,203,640,1959,5776,16650\) at sizes \(0\) through \(8\). It also checks the exact polynomial-component marking identities through size \(100\), including the singleton-event ratio. On execution the checker reports `ALL_CHECKS_OK`. These bounded tests are **not** a proof of the infinite asymptotic or of logical locality; the latter are addressed symbolically in the proof.

Reproduction: with Python 3, run `python checker.py` from the directory holding this note and the supplied `checker.py`; no nonstandard packages are used. The checker does not inspect unprovided files or require network access.

## Relationship to prior work
Kuželka (2026) motivates the distinction between labelled and unlabelled first-order model counting and proves exact counting reductions. The inspected full text concerns complexity, unary functions and automorphism marking; it does not state a rational quantitative first-order convergence theorem for partial injections. Compton (1987) develops general decomposable-class asymptotic logic machinery, and Burris, Compton, Odlyzko and Richmond (1997) develop general sufficient criteria for first-order zero-one laws. These classical techniques and bounded-degree Hanf locality are used, not claimed as new. Earlier rational first-order limit results for uniformly unlabelled **total** coloured permutations concern cycle-only components, and do not imply this chain-dominated regime, its sharp rate or the one-colour phase boundary.

## Limitations
The class is **partial injections** with both in- and outdegree at most one, not all partial unary maps, not total permutations and not all functional digraphs. Sampling is uniform over unlabelled structures. The result concerns ordinary first-order logic in the stated signature only, with \(q\) fixed. The constants in the error estimate are sentence-dependent and not optimized. The analysis uses standard Laguerre saddle-point transfer and a general Hanf locality theorem. Full text of Compton's 1987 paper was not available during this investigation; a semantically equivalent theorem in earlier decomposable-class literature remains a priority risk. No independent audit or historical priority certification is claimed.

## References
1. Ondřej Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting* (first submitted 2026-08-31), https://arxiv.org/abs/2608.30580 . Full arXiv HTML inspected (abstract, introduction, counting theorem, related work and searchable proofs).
2. K. J. Compton, *A logical approach to asymptotic combinatorics. I. First order properties*, Advances in Mathematics 65 (1987), DOI:10.1016/0001-8708(87)90019-3 . Abstract and bibliographic information checked; full text not accessed.
3. S. Burris, K. Compton, A. Odlyzko and B. Richmond, *Fine Spectra and Limit Laws, II. First-Order 0–1 Laws*, Canadian Journal of Mathematics 49 (1997), 641–652, DOI:10.4153/CJM-1997-030-6 . Abstract inspected.
4. D. Kuske and N. Schweikardt, *First-Order Logic with Counting: At Least, Weak Hanf Normal Forms Always Exist and Can Be Computed!* (2017), https://arxiv.org/abs/1703.01122 . Hanf normal form/locality for bounded-degree structures.
5. Classical generating function and saddle-point asymptotics for Laguerre polynomials \(L_n(-1)\), used solely as established analytic input.
