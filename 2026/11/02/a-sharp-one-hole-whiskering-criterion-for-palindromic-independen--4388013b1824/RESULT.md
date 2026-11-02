# A sharp one-hole whiskering criterion for palindromic independence polynomials

## Finding

**Theorem.** Let \(H\) be a finite simple graph, let \(h\in V(H)\) have at least one neighbor, and put \(A=N_H(h)\), \(B=V(H)\setminus N_H[h]\), \(a=|A|\ge1\) and \(b=|B|\ge0\). Form \(W=W(H,h)\) by adjoining one degree-one leaf to each core vertex in \(A\), two degree-one leaves to each core vertex in \(B\), and no leaf to \(h\). The added leaves are distinct and have no additional edges. Let \(I(G;x)=\sum_{r\ge0}i_r(G)x^r\) be the ordinary independence polynomial, counting all independent vertex subsets. Let \(d=a+2b+1\). Then \(\alpha(W)=d\), the independent set of size \(d\) is unique, and, writing \(I(W;x)=\sum_{r=0}^d c_rx^r\),

\[
c_{d-1}-c_1=\sum_{r\ge2}i_r(H[A]). \tag{1}
\]

Consequently, \(I(W;x)\) is palindromic of degree \(d\) **if and only if** \(H[A]\) is a complete graph, equivalently the distinguished vertex \(h\) is simplicial. When this holds,

\[
I(W;x)=(1+x)^d I\!\left(H-h;\frac{x}{(1+x)^2}\right). \tag{2}
\]

In particular, the unique gamma-expansion \(I(W;x)=\sum_{j=0}^{\lfloor d/2\rfloor}\gamma_j x^j(1+x)^{d-2j}\) has \(\gamma_j=i_j(H-h)\ge0\). Thus \(I(W;x)\) is gamma-positive, symmetric and unimodal. Its zeros are all real exactly when the zeros of \(I(H-h;t)\) are all real.

## Assumptions and scope

All graphs are finite, simple and undirected; \(H\) may be disconnected, but \(h\) must have at least one neighbor. The multiplicities of the newly attached leaves are part of the definition and are not arbitrary. For an empty graph we set its independence polynomial equal to \(1\). Complete neighborhoods include the case \(a=1\). The degree of the zero polynomial does not arise because all independence polynomials have constant term \(1\). Palindromicity is with respect to the actual degree \(d\), not the number of vertices.

## Proof

**Maximum independent sets and the first asymmetry.** Let \(F=a+2b\) be the total number of new leaves. Any independent set meeting a core vertex \(v\in A\cup B\) cannot include its attached leaves. If an independent set includes \(h\), no vertex of \(A\) can be included. On \(B\), choosing a core vertex replaces two leaves by one vertex, decreasing cardinality. Hence among independent sets containing \(h\), the unique maximum is \(S=\{h\}\cup L\), where \(L\) is the set of all \(F\) new leaves, of size \(F+1=d\).

If the set omits \(h\), each vertex of \(A\) contributes at most one of its core vertex and its single leaf, and each vertex of \(B\) contributes at most two of its core vertex and its two leaves. Such a set has size at most \(a+2b=F=d-1\). This proves \(\alpha(W)=d\) and \(c_d=1\).

Count independent sets of size \(d-1=F\). When \(h\) is chosen, either exactly one of the \(F\) leaves is omitted, giving \(F\) choices, or precisely one core vertex of \(B\) replaces both its own leaves, giving \(b\) more choices. When \(h\) is omitted, every leaf pair at a vertex of \(B\) must be fully selected; at each vertex of \(A\) one must choose either its leaf or the core vertex. The chosen core vertices form exactly an independent subset of \(H[A]\), giving \(I(H[A];1)=\sum_{r\ge0}i_r(H[A])\) possibilities. Thus

\[
c_{d-1}=F+b+I(H[A];1),\qquad c_1=|V(W)|=F+a+b+1.
\]

Since \(I(H[A];1)=1+a+\sum_{r\ge2}i_r(H[A])\), equation (1) follows. Every summand is nonnegative; it vanishes precisely when no nonadjacent pair exists in \(A\), or \(H[A]\) is complete. Palindromicity demands \(c_{d-1}=c_1\), so the clique condition is necessary.

**Exact polynomial under the clique condition.** Assume \(A\) is a clique. Every independent set of the induced base graph \(H-h\) has the unique form \(U\) or \(U\cup\{v\}\), where \(U\) is independent in \(H[B]\) and \(v\in A\) has no neighbor in \(U\). Let \(k(U)=|\{v\in A:N_H(v)\cap U=\varnothing\}|\). Then

\[
I(H-h;t)=\sum_{U\in\operatorname{Ind}(H[B])}t^{|U|}(1+k(U)t). \tag{3}
\]

Independently classify an independent set of \(W\) by its selected core vertices from \(B\), again \(U\). Its contribution from those cores and their pendant leaves is \(x^{|U|}(1+x)^{2(b-|U|)}\). For the remaining core vertices, either select \(h\) and no vertices of \(A\), omit \(h\) and select no vertices of \(A\), or omit \(h\) and select exactly one allowable vertex of \(A\). Their combined weighted contribution is

\[
(1+x)^{a+1}+k(U)x(1+x)^{a-1}.
\]

Summing and using \(d=a+2b+1\) gives

\[
\begin{aligned}
I(W;x)&=\sum_{U\in\operatorname{Ind}(H[B])}x^{|U|}(1+x)^{2(b-|U|)}\left[(1+x)^{a+1}+k(U)x(1+x)^{a-1}\right]\\
&=(1+x)^d\sum_U\left(\frac{x}{(1+x)^2}\right)^{|U|}\left[1+k(U)\frac{x}{(1+x)^2}\right],
\end{aligned}
\]

which is (2) by (3). This is a polynomial identity, not an assertion requiring evaluation at the exceptional value \(x=-1\). Since \(\alpha(H-h)\le b+1\le\lfloor d/2\rfloor\), it expands into gamma-basis elements with nonnegative independent-set coefficients. Each \(x^j(1+x)^{d-2j}\) is symmetric with common degree \(d\) and unimodal, and the known nonnegative gamma-expansion implication gives unimodality (or compare the two adjacent binomial coefficients termwise). Necessity and sufficiency are established.

**Real-rootedness transfer.** Put \(P(t)=I(H-h;t)\), of degree \(r\le\lfloor d/2\rfloor\). Its nonzero roots are all strictly negative if real, because all its coefficients are nonnegative and its constant term is \(1\). The substitution gives a factor \((1+x)^{d-2r}\) and, for each root \(\tau\) of \(P\), a quadratic equation \(\tau(1+x)^2=x\). If \(\tau<0\), this quadratic has discriminant \(1-4\tau>0\), product of roots equal to \(1\), and negative sum; both roots are strictly negative. Conversely, if every root of \(I(W;x)\) is real, then each root \(\tau\) of \(P\) comes from a real \(x\ne-1\) satisfying \(\tau=x/(1+x)^2\), so \(\tau\) is real. Thus the two polynomials are simultaneously real-rooted.

## Verification

The standalone file `verify.py` constructs \(W\) directly as an adjacency-bitset graph and computes independence polynomials by a vertex-deletion recurrence. It checks \(\alpha(W)=d\), the uniqueness of the maximum independent set, the exact penultimate-coefficient deficit, the palindromicity equivalence, and equation (2) when the neighborhood is a clique. It independently enumerates literal independent subsets in a smaller range. Across all labelled base graphs on two through five vertices and all eligible distinguished vertices, it checks 5,044 cases, plus 244 literal enumerations and 5,167 deterministic larger randomized rooted graph checks for base orders six through eight. Output: `VERIFY_OK`. These finite checks support the proof but are not used to infer any infinite statement.

## Relationship to prior work

Hibi, Kara and Vien (2026, Proposition 3.1) give an all-profile leaf-attachment generating formula; their Theorem 3.2 completely classifies palindromicity when **each** base vertex has at least one attached leaf. The present one-hole profile is excluded from that theorem. Their general formula is compatible with the polynomial calculations here, and the present theorem does not claim a new general-purpose whiskering identity. Instead, the claim is the **sharp clique-neighborhood necessity and sufficiency**, its exact nonnegative penultimate-coefficient obstruction, and the resulting gamma-polynomial identification for this canonical balanced one-hole profile.

Stevanović's general sufficient neighborhood-count criterion, as reproduced by Levit and Mandrescu (2011, Theorem 2.2), already implies the **sufficiency** direction for this graph, and general two-whisker symmetry is classical. Neither that sufficiency criterion nor the full-whiskering classification yields a stated necessity criterion for this specified one-hole profile. The gamma-basis substitution is also a standard algebraic device; its exact identification with the base vertex-deleted independence polynomial is recorded here, not asserted as a new general transformation principle.

## Limitations

The theorem applies only to the indicated leaf multiplicities, with \(a\ge1\). It does not classify all partially whiskered graphs, all leaf-multiplicity profiles with one uncovered vertex, or the roots of arbitrary independence polynomials. The historical-priority comparison has not exhausted terminology for weighted coronas, clique-whiskering, simplicial vertices, or alpha-unique graphs. Independent mathematical audit is not claimed.

## References

1. T. Hibi, S. Kara, and D. Vien, *Independence Polynomials of Graphs*, arXiv:2603.16695v1 (public 17 March 2026), especially Proposition 3.1 and Theorem 3.2. https://arxiv.org/html/2603.16695v1
2. V. E. Levit and E. Mandrescu, *On Symmetry of Independence Polynomials*, arXiv:1105.2202v1 (2011), especially Theorem 2.2 (Stevanović sufficient condition) and the constructions in Section 2.3. https://arxiv.org/html/1105.2202v1
3. V. E. Levit and E. Mandrescu, *On f-Symmetries of the Independence Polynomials of Graphs*, arXiv:1303.2564v1 (2013), contextual background on symmetry transformations. https://arxiv.org/abs/1303.2564
