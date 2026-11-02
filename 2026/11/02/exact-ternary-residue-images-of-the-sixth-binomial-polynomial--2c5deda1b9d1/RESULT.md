# Exact ternary residue images of the sixth binomial polynomial

## Finding
For every integer \(k\ge1\), define
\[
R_k=\#\left\{\binom n6\bmod 3^k:n=0,1,2,\ldots\right\}.
\]
Then \(R_1=2\), and for every \(k\ge2\),
\[
\boxed{R_k=\begin{cases}
(5\cdot3^{k-1}+5)/4,&k\text{ even},\\
(5\cdot3^{k-1}+7)/4,&k\text{ odd}.
\end{cases}}
\]
In particular the image has limiting density \(\lim_{k\to\infty}R_k/3^k=5/12\).

There is also an exact description of the infinite 3-adic image. Let
\[
P(X)=\frac{X(X-1)(X-2)(X-3)(X-4)(X-5)}{720}\in\mathbb Q[X],
\]
and let \(\alpha\in6+9\mathbb Z_3\) be the unique root of \(P'(\alpha)=0\) in this ball. Put \(c=P(\alpha)\in\mathbb Z_3\). With \(\mathbb Z_3^2=\{z^2:z\in\mathbb Z_3\}\),
\[
\boxed{P(\mathbb Z_3)=3\mathbb Z_3\;\sqcup\;
\bigl(c+18\mathbb Z_3^2\bigr)\;\sqcup\;
\bigl(-5/1024+18\mathbb Z_3^2\bigr).}
\]
The three sets are disjoint; their residue classes modulo nine are respectively \(\{0,3,6\}\), \(\{1\}\), and \(\{7\}\). The 3-adic Haar measure of this image is exactly \(5/12\).

## Assumptions and scope
The first parameter \(k\) is any positive integer; all binomial coefficients use nonnegative integral top indices. The polynomial \(P\) extends continuously from the nonnegative integers to \(\mathbb Z_3\), where it remains integer-valued. The expression \(c+18\mathbb Z_3^2\) means a translate of eighteen times the set of **squares**, not an additive ideal. The 3-adic root \(\alpha\), which is intrinsically defined and unique in its indicated ball, is not claimed to be a rational integer. Reduction modulo \(3^k\) of a 3-adic set means its set of residue classes; \(R_k\) is the number of these classes.

## Proof
**1. Exact finite-branch expansions.** For \(a\in\{0,\ldots,8\}\), define \(G_a(T)=P(a+9T)\). Direct expansion of the six linear factors, with denominators prime to three after the indicated division, yields the following *coefficientwise* congruences in \(\mathbb Z_3[T]\):
\[
\begin{aligned}
G_a(T)/3&\equiv T\pmod3&& (a=0,1,2),\\
G_a(T)/3&\equiv 2T\pmod3&&(a=3,4,5),\\
\frac{G_a(T)-P(a)}9&\equiv2T(T+1)\pmod3&&(a=6,7,8).
\end{aligned}
\]
Here \(P(a)=0\) for \(a\le5\), and \(P(6)=1\), \(P(7)=7\), \(P(8)=28\). These congruences are polynomial identities after division, not merely sampled congruences. Their coefficients can be independently reconstructed by multiplying \(\prod_{j=0}^{5}(a-j+9T)/720\); the accompanying standalone verifier checks every coefficient rationally.

**2. The six regular branches.** If \(H(T)\in\mathbb Z_3[T]\) satisfies \(H(T)\equiv uT\pmod3\) with \(u\) a unit, then \(H\) maps \(\mathbb Z_3\) bijectively onto \(\mathbb Z_3\). Indeed \(H(x)-H(y)=(x-y)(u+3A(x,y))\) for an integral polynomial \(A\), so \(H\) is an isometry. It induces injections, hence bijections, on each finite quotient \(\mathbb Z/3^m\mathbb Z\), and compactness gives surjectivity. Applying this to \(G_a/3\) for \(0\le a\le5\) gives \(G_a(\mathbb Z_3)=3\mathbb Z_3\).

**3. A square-image lemma.** Let \(H\in\mathbb Z_3[T]\) satisfy \(H(T)\equiv2T(T+1)\pmod3\). Since \(H'(T)\equiv T+2\pmod3\), Hensel's lemma gives a unique \(t_*\in\mathbb Z_3\) satisfying \(H'(t_*)=0\), with \(t_*\equiv1\pmod3\). Taylor expansion with integral coefficients gives
\[
H(t_*+u)=H(t_*)+u^2B(u),\qquad B\in\mathbb Z_3[u],\quad B(u)\equiv2\pmod3.
\]
Every element of \(B(u)/2\) is congruent to one modulo three and therefore has a unique square root \(S(u)\equiv1\pmod3\). Define \(\phi(u)=uS(u)\). The square-root map on \(1+3\mathbb Z_3\) is 1-Lipschitz because the sum of two roots congruent to one modulo three is a unit. As \(B(u)/2=1+3A(u)\) for \(A\in\mathbb Z_3[u]\), the map \(S(u)\) is 3-Lipschitz: \(S(u)-S(v)\in3(u-v)\mathbb Z_3\). Consequently \(\phi(u)-\phi(v)\) is \((u-v)\) times a unit. Thus \(\phi\) is an isometry and, by finite-quotient bijectivity, is onto. It follows that
\[
H(\mathbb Z_3)=H(t_*)+2\mathbb Z_3^2.
\]
This is an exact image identity, not a local approximation.

**4. The three ramified input classes.** Apply the lemma to \(H_a=(G_a-P(a))/9\), for \(a=6,7,8\). There is a unique critical point of \(P\) in each input ball \(a+9\mathbb Z_3\), and each image is the corresponding critical value plus \(18\mathbb Z_3^2\). The symmetry \(P(5-X)=P(X)\) interchanges \(6+9\mathbb Z_3\) with \(8+9\mathbb Z_3\); therefore their images agree exactly. The critical point in \(7+9\mathbb Z_3\) is \(5/2\), and direct substitution gives \(P(5/2)=-5/1024\). The other critical point \(\alpha\in6+9\mathbb Z_3\) is unique by the lemma. Its critical value satisfies \(c\equiv P(6)=1\pmod9\), while \(-5/1024\equiv P(7)=7\pmod9\). Together with the six regular branches, these facts give the claimed disjoint image decomposition.

**5. Squares modulo prime powers and exact cardinality.** For an integer \(m\ge1\), let \(Q_m\) denote the number of squares modulo \(3^m\), including zero, and set \(Q_0=1\). A nonzero square has even 3-adic valuation \(2j<m\), and for each such \(j\) there are exactly \(3^{m-2j-1}\) unit squares modulo \(3^{m-2j}\). Thus
\[
Q_m=1+\sum_{j=0}^{\lfloor(m-1)/2\rfloor}3^{m-2j-1}.
\]
For \(k\ge2\), the three output components remain disjoint modulo \(3^k\). The first occupies \(3^{k-1}\) residues; each square component occupies \(Q_{k-2}\) residues. Hence \(R_k=3^{k-1}+2Q_{k-2}\). Summing the finite geometric progression gives the two parity formulas in the finding. At \(k=1\) the two square components merge modulo three into the single class one, while \(3\mathbb Z_3\) gives zero: \(R_1=2\).

**6. Measure.** The set of unit squares in \(\mathbb Z_3\) has measure \(1/3\). Since a nonzero square has even valuation, \(\mu(\mathbb Z_3^2)=\frac13\sum_{j\ge0}3^{-2j}=3/8\). The components have measures \(1/3\), \((1/9)(3/8)\), and \((1/9)(3/8)\), for a total of \(5/12\). Equivalently the exact count above tends to the same density. This completes the proof.

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs the nine branch polynomials over the rationals, validates all coefficientwise congruences, Hensel-lifts the critical point, and compares both the predicted three-component image and cardinalities with direct enumeration of all \(\binom n6\) modulo \(3^k\) for \(1\le k\le9\). For each \(k\), enumeration through \(0\le n<3^{k+2}\) is exhaustive for that *finite* modulus because \(\nu_3(6!)=2\). These finite checks do not establish the statements for all \(k\); the unrestricted proof is above.

## Relationship to prior work
Sun and Zhang introduced the question of which binomial-coefficient sequences have dense images in \(\mathbb Z_p\), defined their finite residue sets \(R_m(k)\), and established broad universality criteria. Their main interval \(p^a\le k<2p^a\) excludes the lower index six at \(p=3\). Lucas's theorem immediately shows that \(\binom n6\) takes only the residues zero and one modulo three, so non-density is already known and **is not** the novelty claimed here. What is added is the evaluated all-level residue count, the exact three-component 3-adic image, and the density \(5/12\). Fiorot, Gilblas, and Tonolo study prime-power binomial recurrences mainly to understand periodic sequences, while Barat and Grabner investigate distributions of binomial coefficients and digital functions. Neither inspected material supplied the specific evaluated image decomposition and count. General polynomial-image and local Hensel techniques underlie the proof and are not claimed as new.

## Limitations
This result covers exactly the lower binomial index six and the prime three. It does not classify the images of all binomial polynomials or their input-fiber multiplicity distributions. No claim of absolute historical priority is made; an equivalent statement in specialized literature remains possible. The 3-adic constant \(c\) is defined by a unique Hensel root rather than a rational closed form. Finite verification is evidence only within its stated checked moduli.

## References
1. Zhi-Wei Sun and Wei Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089 (initial public posting 2008-12-16), *Proceedings of the American Mathematical Society* **139** (2011), 1569–1577. https://arxiv.org/abs/0812.3089 ; https://arxiv.org/html/0812.3089v5 .
2. Luisa Fiorot, Riccardo Gilblas, and Alberto Tonolo, *Periodic sequences, binomials modulo a prime power, and a math/music application*, *Advances in Applied Mathematics* **162** (2025), article 102786. https://doi.org/10.1016/j.aam.2024.102786 .
3. Guy Barat and Peter J. Grabner, *Distribution of binomial coefficients and digital functions*, *Journal of the London Mathematical Society*. https://doi.org/10.1112/S0024610701002630 .
