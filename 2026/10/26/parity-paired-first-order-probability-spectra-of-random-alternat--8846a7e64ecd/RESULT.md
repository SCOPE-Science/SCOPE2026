# Parity-paired first-order probability spectra of random alternating forms

## Finding
Fix a finite field \(\mathbb F_q\), with \(q\ge 2\), and use the first-order vector-space language consisting of addition, zero, each scalar-multiplication function, and predicates \(P_a(u,v)\) recording \(B(u,v)=a\) for each \(a\in\mathbb F_q\). On \(V_n=\mathbb F_q^n\), independently choose each strict upper-triangular entry of an alternating matrix uniformly in \(\mathbb F_q\), and extend by skew symmetry and zero diagonal. Thus every alternating bilinear form occurs with the same probability.

Put
\[
 C_q=\prod_{j=1}^{\infty}(1-q^{-(2j-1)}),\qquad
 \pi_q(m)=C_q\frac{q^{-m(m-1)/2}}{\prod_{j=1}^m(1-q^{-j})}\quad(m\in\mathbb N_0).
\]
The series of \(\pi_q(m)\) over the nonnegative even integers equals one, as does the series over the nonnegative odd integers. For every first-order sentence \(\varphi\), an effectively calculable finite or cofinite set \(F_\varphi\subseteq\mathbb N_0\) satisfies, for both \(\varepsilon\in\{0,1\}\),
\[
 \lim_{\substack{n\to\infty\\n\equiv\varepsilon\pmod2}}
 \Pr[(V_n,B)\models\varphi]
 =\sum_{\substack{m\in F_\varphi\\m\equiv\varepsilon\pmod2}}\pi_q(m).
\]
Moreover, the complete spectrum of ordered pairs of these two limits, ranging over all first-order sentences, is exactly
\[
 \left\{\left(\sum_{\substack{m\in F\\m\text{ even}}}\pi_q(m),
 \sum_{\substack{m\in F\\m\text{ odd}}}\pi_q(m)\right):
 F\subseteq\mathbb N_0\text{ finite or cofinite}\right\}.
\]
In particular, the unrestricted sequence of first-order probabilities need not converge: the sentence saying that the radical is zero has even-limit \(C_q>0\) and odd-limit zero.

## Assumptions and scope
The field is fixed while \(n\) tends to infinity. The predicates describe the actual alternating form, not an arbitrary free binary relation. Formula syntax is ordinary first-order logic over the indicated finite signature; no parity, counting, or fixed-point quantifiers are added. Empty products equal one. The radical is the definable subspace
\[
 R(B)=\{x\in V_n:\forall y\,P_0(x,y)\},\qquad M_n=\dim_{\mathbb F_q}R(B).
\]
The two components of the probability pair always refer respectively to even and odd ambient dimensions. An alternating form of rank \(2r\) and radical dimension \(m\) is isometric to the orthogonal direct sum of a zero form on \(\mathbb F_q^m\) and a nondegenerate symplectic form on \(\mathbb F_q^{2r}\). This classification holds also in characteristic two.

## Proof
**1. Exact radical law.** For \(n-m=2r\), choose the radical in \({n\brack m}_q\) ways and then choose a nondegenerate alternating form on the quotient in \(|\operatorname{GL}_{2r}(q)|/|\operatorname{Sp}_{2r}(q)|\) ways. Dividing by the \(q^{n(n-1)/2}\) equiprobable forms gives
\[
 \Pr(M_n=m)=q^{-m(m-1)/2}
 \frac{\prod_{j=n-m+1}^{n}(1-q^{-j})}{\prod_{j=1}^{m}(1-q^{-j})}
 \prod_{j=1}^{r}(1-q^{-(2j-1)}).
\]
This probability is zero when \(n-m\) is odd. For fixed \(m\) of the correct parity, its limit as \(n\to\infty\) is \(\pi_q(m)\). The limiting mass does not escape to infinity: for every nonzero vector \(x\), the independent alternating-matrix coefficients make \(B(x,\cdot)=0\) with probability \(q^{-(n-1)}\). Therefore
\[
 \mathbb E[q^{M_n}]=1+(q^n-1)q^{-(n-1)}<1+q,
 \qquad\Pr(M_n\ge L)\le(1+q)q^{-L}.
\]
By tightness, each parity-restricted limiting sequence \(\pi_q(m)\) sums to one.

**2. Finite-rank first-order stabilization lemma.** Let \(A_{m,r}\) denote a form with radical dimension \(m\) and nondegenerate symplectic rank \(2r\). For any integer \(d\ge1\), if \(r,r'\ge d\) and \(\min(m,d)=\min(m',d)\), then \(A_{m,r}\) and \(A_{m',r'}\) satisfy the same sentences of quantifier rank at most \(d\).

To prove this, play the \(d\)-round Ehrenfeucht–Fraïssé game. After \(j<d\) moves, maintain a linear isometry between the spans \(U,U'\) of the selected vectors, carrying \(U\cap R\) onto \(U'\cap R'\). This also maintains all atomic formulas, because the scalar operations and the predicates \(P_a\) are preserved. A selected vector already in \(U\) is matched by its image. If a new vector lies in \(U+R\), write it as \(u+z\) with \(z\in R\setminus U\); choose a new radical vector \(z'\in R'\setminus U'\) and answer with the image of \(u\) plus \(z'\). There is room: either the radicals have the same dimension below \(d\), or both have dimension at least \(d>j\). If the new vector lies outside \(U+R\), its pairings with \(U\) specify a linear functional annihilating \(U\cap R\). Nondegeneracy of the symplectic quotient on the opposite side realizes the corresponding functional. The affine space of realizations there has dimension at least \(2r'-j\ge2d-j>j\), so a realization can be chosen outside the image of \(U'\) in that quotient. It is consequently outside \(U'+R'\), preserves linear independence modulo radicals, and gives the required extended isometry. The same construction handles either player's move. Thus the duplicator wins all \(d\) rounds.

**3. Reduction of all sentences to a finite or cofinite radical event.** Given a sentence \(\varphi\) of rank \(d\ge1\), evaluate it in the finite canonical structures \(A_{m,d}\), for \(m=0,1,\ldots,d\). By the lemma, its eventual value for any radical dimension \(m\ge d\) is its value at \(m=d\), regardless of the symplectic rank once that rank is at least \(2d\). Let \(F_\varphi\) contain exactly the values \(m<d\) for which \(A_{m,d}\models\varphi\), and also all \(m\ge d\) if and only if \(A_{d,d}\models\varphi\). This is an effective finite or cofinite set. Quantifier-rank-zero sentences are handled identically by taking \(d=1\). For ambient dimensions tending through either parity, the probability that the symplectic half-rank is less than \(d\) tends to zero by the tight radical estimate. Summing the point probabilities in Step 1, with the uniform tail bound, proves both asserted limits.

**4. Realization of the entire pair spectrum.** For each fixed \(m\), the predicate saying \(\dim R(B)=m\) is first-order: demand \(m\) linearly independent radical vectors spanning every radical vector. Since \(\mathbb F_q\) is fixed and finite, linear independence and finite-span membership are first-order disjunctions over scalar tuples. A finite union of these exact-dimension predicates defines any finite \(F\), and its negation defines any cofinite \(F\). Both probabilities of the resulting formula equal the sums prescribed by \(F\). This proves exactness of the joint spectrum. The exact-zero-radical formula witnesses nonconvergence in the full dimension sequence.

## Verification
Run `python3 verify.py` from the same folder as this document. The checker enumerates all alternating forms for prime-field orders \(q=2\) and \(q=3\) through six and five ambient dimensions respectively, calculates the radical by elimination, and compares the resulting finite distributions with the exact symplectic counting formula. It also checks the normalization and exact expectation of radical size. The expected terminal line is `ALTERNATING_FORMS_FINITE_COUNT_OK 26 rank-cells`. These finite cases independently test the rank-count component; the first-order stabilization argument and limiting classification are mathematical proofs and are not established by the finite checker.

## Relationship to prior work
Fulman and Goldstein, *Stein's method and the rank distribution of random matrices over finite fields* (arXiv:1211.0504, Section 5), already establish the underlying even/odd rank-deficiency distributions and quantitative approximation estimates; those probability laws are not claimed as new. Koponen's *A characterization of the finite model property for omega-categorical theories* (arXiv:2610.16163, initially public 2026-10-12) motivates examining first-order convergence in random finite expansions, but does not state this concrete full joint spectrum for alternating forms. Demin and Zhukovskii (arXiv:2402.02567) discuss first-order behavior of other random finite structures. The contribution claimed here is the quantifier-rank stabilization plus the exact **paired** first-order probability spectrum, including the finite/cofinite coupling across ambient-dimension parities.

## Limitations
The result concerns only uniformly random alternating forms with the specified finite-field vector-space signature and fixed field. It does not imply analogous first-order classifications for arbitrary bilinear, Hermitian, or quadratic forms, for varying fields, or for logics with counting quantifiers. Prior model-theoretic literature not located in the comparison may already imply some or all of the classification; this limits historical-priority confidence. No independent mathematical audit has been performed. The finite executable check cannot certify arbitrary formula-rank assertions.

## References
1. V. Koponen, *A characterization of the finite model property for omega-categorical theories*, arXiv:2610.16163v1 (first submitted 2026-10-12). https://arxiv.org/html/2610.16163v1
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Annals of Probability 43 (2015), 1274–1314; arXiv:1211.0504v4, especially Section 5. https://arxiv.org/html/1211.0504v4
3. A. Demin and M. Zhukovskii, *First order complexity of finite random structures*, arXiv:2402.02567 (2024). https://arxiv.org/abs/2402.02567
