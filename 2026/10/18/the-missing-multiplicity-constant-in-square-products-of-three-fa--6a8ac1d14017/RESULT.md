# The missing multiplicity constant in square products of three factorials

## Finding

Let \(s(m)\) denote the squarefree part of a positive integer \(m\), meaning the unique squarefree integer for which \(m/s(m)\) is a perfect square. Set
\[
\mathcal S=\{s(c!):c\ge1\},\qquad
C_0=\sum_{a\in\mathcal S}a^{-1/2},\qquad
b_t=s((t^2)!),\qquad
K=\sum_{t=2}^{\infty}b_t^{-1/2}.
\]
Both constants are finite and \(K>0\). Count positive integer triples by
\[
T(X)=\#\{(c,b,n):1\le c<b<n\le X,\ c!b!n!\text{ is a perfect square}\}.
\]
**Theorem.** For each \(\varepsilon>0\), as \(X\to\infty\),
\[
\boxed{T(X)=(C_0+K)\sqrt X+O_\varepsilon(X^{2/5+\varepsilon}).}
\]
Here \(C_0=3.709751\ldots\) is the existing *distinct-endpoint* constant; the additional, strictly positive \(K\) corrects the conjectural leading coefficient for counting triples stated in Tao's 2026 work (Remark 1.11 following Theorem 1.10). Its first eight terms total \(0.555541941\ldots\); this decimal is a finite partial sum, not a certified rounding of the infinite series.

More precisely, define the number of *consecutive-largest* representations
\[
r(n)=\#\{c:1\le c<n-1,\ c!(n-1)!n!\text{ is a perfect square}\}
\]
and \(M(X)=\#\{n\le X:r(n)=2\}\). Then \(r(n)\le2\) for all \(n\), and
\[
\boxed{M(X)=K\sqrt X+O(\sqrt{\log(2X)}).}
\]
Two such representations occur precisely when, for some integer \(t\ge2\) and positive integer \(u\),
\[
\{c:c!(n-1)!n!\text{ is square},\ 1\le c<n-1\}=\{t^2-1,t^2\},
\quad n=b_tu^2\ge t^2+2.
\]
The integers \(b_t\) are pairwise distinct. In particular, among nonsquare endpoints whose *minimum* number of distinct factorial factors is three, the asymptotic proportion with exactly two three-factor representations is \(K/(C_0-1)>0\); the proportion with three or more is zero.

## Assumptions and scope

Indices are positive integers, factorial arguments are strictly increasing in a counted triple, and the square is a positive integer square. The cutoff \(X\) tends to infinity through reals, with integers \(n\le X\). All implied constants may depend on \(\varepsilon\); the constant in the bound for \(M(X)\) is absolute. The statements concern the *number of triples*, rather than only the number of eligible largest arguments. The proof uses three published inputs: Erdős--Selfridge's consecutive-product theorem, Yudin's 2026 bound for exceptional largest arguments, and the uniform short-interval estimate for those representations recorded by Tao and by Yudin.

## Proof

**1. Collisions of squarefree factorial parts.** For \(1\le c<d\), equality \(s(c!)=s(d!)\) is equivalent to the product \((c+1)(c+2)\cdots d\) being a square. The Erdős--Selfridge theorem states that the product of at least two consecutive positive integers cannot be a proper perfect power. Consequently \(d=c+1\), and equality then requires \(d=t^2\) for an integer \(t\ge2\). Conversely, \((t^2)!=(t^2)(t^2-1)!\) gives equality. Thus each squarefree factorial part occurs once or exactly twice, and the repeated parts are exactly the pairwise distinct \(b_t=s((t^2)!)\) with indices \(t^2-1,t^2\). They exceed one: if \(s(c!)=1\) for \(c\ge2\), then \(c!\) would be a perfect square, contrary to Erdős--Selfridge applied to \(1\cdots c\) after removing its factor one, or directly to \(2\cdots c\).

**2. Two-representation classification.** The identity \(n!(n-1)!=n((n-1)!)^2\) makes the consecutive-largest square condition equivalent to \(s(n)=s(c!)\). A duplicated \(c\)-value must therefore be \(t^2-1,t^2\), and the largest permitted one satisfies \(t^2<n-1\), i.e. \(n\ge t^2+2\). Conversely \(n=b_tu^2\ge t^2+2\) satisfies both and no third \(c\). These \(n\)-families are disjoint because their squarefree parts \(b_t\) differ. Hence the exact counting identity, valid for all real \(X\ge1\), is
\[
M(X)=\sum_{t\ge2}\#\{u\in\mathbb Z_{\ge1}:t^2+2\le b_tu^2\le X\}.
\]

**3. Convergence and the sparse double-count law.** Yudin's Section 3.2 proves that for sufficiently large integers \(m\) one has \(s(m!)\ge\exp(\delta m)\) for some \(\delta>0\). Substituting \(m=t^2\) yields \(b_t\ge\exp(\delta t^2)\) for large \(t\). Thus \(K\) converges absolutely and \(b_t>t^2+2\) for all but finitely many \(t\), making the lower cutoff on \(u\) an \(O(1)\) total correction. For a sufficiently large absolute \(B\), split the sum at \(L=B\sqrt{\log(2X)}\). The terms \(t\le L\) have at most \(O(L)\) rounding error when replacing \(\lfloor\sqrt{X/b_t}\rfloor\) by \(\sqrt{X/b_t}\), including those with \(b_t>X\). By the exponential lower bound, choosing \(B\) large makes both the integral tail and the counting tail over \(t>L\) bounded by \(O(1)\). This proves the stated \(M(X)\) estimate.

**4. Count all consecutive-largest triples.** If distinct values of \(s(c!)\) are counted once, Yudin's Section 3.2 establishes
\[
\#\{n\le X:r(n)\ge1\}=C_0\sqrt X+O(\log(2X)).
\]
Since \(r(n)\in\{0,1,2\}\), the *number of representations* with second-largest argument \(n-1\) equals
\[
\sum_{n\le X}r(n)=(C_0+K)\sqrt X+O(\log(2X)).
\]

**5. Nonconsecutive-largest triples.** Yudin's Theorem 3.1 shows that the number of \(n\le X\) having any triple with second-largest argument at most \(n-2\) is \(O_\varepsilon(X^{2/5+\varepsilon})\). His Section 3.1, equation (3.2), together with Tao's earlier lemmas, shows more: for every fixed \(\eta>0\), all sufficiently large such triples satisfy \(n-b\le X^\eta\) and \(c\le X^\eta\). At most \(X^{2\eta}\) pairs \((c,n-b)\) are therefore available for any one exceptional \(n\). For a prescribed \(\varepsilon>0\), apply the endpoint bound with \(\varepsilon/2\), then take \(2\eta<\varepsilon/2\). The number of *nonconsecutive triples*, with multiplicity, is \(O_\varepsilon(X^{2/5+\varepsilon})\). Adding this to step 4 proves the theorem.

**6. Conditional multiplicity distribution.** For \(n\ge2\), the source paper characterizes endpoints having a two-factor representation as the squares, and gives \(D_3(X)=(C_0-1)\sqrt X+O_\varepsilon(X^{2/5+\varepsilon})\) for the nonsquare endpoints with a three-factor representation. The \(n\) counted by \(M(X)\) are nonsquares because \(b_t>1\), and hence belong to that class. Except for \(O_\varepsilon(X^{2/5+\varepsilon})\) endpoints, every triple has consecutive largest arguments. Removing those exceptions shows that the count with exactly two triples is \(K\sqrt X+O_\varepsilon(X^{2/5+\varepsilon})\), while the count with three or more is \(O_\varepsilon(X^{2/5+\varepsilon})\). Division by \(D_3(X)\) gives the claimed proportions. No statement is made that *every* endpoint has at most two triples; the unconditional upper bound two applies only to consecutive-largest triples.

## Verification

Run `python3 verify.py`. The standalone exact-arithmetic program enumerates factorial prime-exponent parity signatures through index \(260\), verifies all repeated squarefree parts in that finite range, enumerates every possible three-factor square triple with largest index at most \(260\), checks the maximal consecutive-largest multiplicity, directly checks integer square identities, and compares the exact double-family counting formula at several cutoffs. It also records the first eight exact \(b_t\) values. Its finite output is a cross-check, not a proof of either an asymptotic or the Erdős--Selfridge theorem.

## Relationship to prior work

Yudin, *Square products of factorials and a conjecture of Erdős and Graham* (arXiv:2610.01899v1, October 1, 2026), determines the leading constant \(C_0-1\) for the **number of nonsquare endpoints**, not the number of distinct triples. Section 3.2 deliberately counts each squarefree part once, while Section 3.1 controls the exceptional nonconsecutive-largest endpoints and their short parameters. Tao, *Products of consecutive integers with unusual anatomy* (arXiv:2603.27990v1, March 30, 2026), explicitly observes that the squarefree parts of factorials repeat at square indices (Section 1.3), and writes in Remark 1.11 that the number of **triple solutions** should be asymptotic to \(C_0\sqrt X\). Counting each repeated part a second time introduces \(K>0\) and therefore contradicts that precise conjectural coefficient. The repeated-index observation and Erdős--Selfridge theorem are prior ingredients, not novel lemmas. Dujella, Najman, Saradha and Shorey (2014) give individual doubled witnesses in the related three-factor problem but do not derive this asymptotic multiplicity correction.

## Limitations

The result depends on the published exceptional-endpoint and uniform-short-parameter estimates; it is not an independent reproving of those deep estimates. The decimal displayed for \(K\) is the value of a finite partial sum, not an independently certified high-precision constant. The result does not classify all possible nonconsecutive representations of individual endpoints and does not establish any universal bound of two for total triple multiplicity. Novelty is assessed against inspected work, with residual risk of an equivalent but differently indexed counting theorem outside those sources.

## References

1. F. Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899v1 (2026), Sections 3.1--3.2, Theorems 1.1 and 3.1. https://arxiv.org/html/2610.01899v1
2. T. Tao, *Products of consecutive integers with unusual anatomy*, arXiv:2603.27990v1 (2026), Section 1.3, Theorem 1.10, Remark 1.11, Lemmas 4.1--4.2. https://arxiv.org/html/2603.27990v1
3. P. Erdős and J. L. Selfridge, *The product of consecutive integers is never a power*, Illinois Journal of Mathematics 19 (1975), 292--301. (Classical theorem, also stated in References 1 and 2.)
4. A. Dujella, F. Najman, N. Saradha, T. N. Shorey, *Products of three factorials*, Publ. Math. Debrecen 85 (2014), 123--130. https://publi.math.unideb.hu/paper/1890/download/10_5486_PMD_2014_5835.pdf
