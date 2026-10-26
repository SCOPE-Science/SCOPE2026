# Random singular evolution algebras are asymptotically rigid over every finite field

## Finding
Fix a prime power \(q\ge2\). For each \(n\ge2\), choose \(M=(m_{ij})\) uniformly from the **whole** space \(M_n(\mathbb F_q)\), independently in every entry, and define the labelled evolution algebra \(E_M\) with \(e_ie_j=0\) for \(i\ne j\) and \(e_i^2=\sum_jm_{ij}e_j\). Write \(p=1-q^{-1}\) and \(\rho=p^2+(1-p)^2<1\). Then
\[
\Pr(\operatorname{Aut}_{\mathbb F_q}(E_M)\ne\{1\}\ \text{or }E_M\text{ has nonunique natural bases})=O_q(n^2\rho^n).
\]
The same estimate holds conditionally on \(M\) **singular**. Here uniqueness means that every natural basis is obtained from the specified basis by a permutation and nonzero individual scalings.

The exact probability that the \(n\) original squares are nonzero and **pairwise linearly independent** (the property called \(2\mathrm{LI}\)) is
\[
P_{n,q}=\prod_{j=0}^{n-1}\left(1-\frac{1+j(q-1)}{q^n}\right).
\]
This event always implies uniqueness of natural bases; when \(q>3\), it is also necessary and hence \(P_{n,q}\) is the exact probability of uniqueness. The exact small-field equivalence is **not** asserted for \(q\in\{2,3\}\). In particular,
\[
1-P_{n,q}=\frac{n+(q-1)\binom n2}{q^n}+O_q(n^4q^{-2n}).
\]
The singular matrices have probability \(1-\prod_{i=1}^n(1-q^{-i})\ge q^{-1}\), so this conclusion applies to a positive-density **nonperfect** subpopulation that was excluded from invertible-matrix results.

An explicit conservative all-\(n\) bound for the bad event is
\[
B_{n,q}=(1-P_{n,q})+q^{-n}+\sum_{s=1}^{n-1}\binom nsq^{-s(n-s)}
 +\sum_{k=2}^n n^k\rho^{nk/2}.
\]
The unconditional bad-event probability is at most \(B_{n,q}\), and its probability conditioned on singularity is at most \(B_{n,q}/[1-\prod_{i=1}^n(1-q^{-i})]\le qB_{n,q}\). An upper bound may exceed one for small \(n\); it remains mathematically valid.

## Assumptions and scope
A natural basis is a vector-space basis consisting of pairwise orthogonal vectors for the algebra product. An algebra automorphism means an invertible \(\mathbb F_q\)-linear multiplicative map. The structure matrix is uniformly sampled *with its basis fixed*, not uniformly over isomorphism classes. The graph \(\Gamma_M\) has vertices \(1,\ldots,n\) and arcs \(i\to j\) precisely when \(m_{ij}\ne0\), including loops. Its arcs are independent, present with probability \(p\).

## Proof
**1. A deterministic natural-basis criterion.** Suppose each original square is nonzero and any two distinct original squares are linearly independent. Let the columns \(v_1,\ldots,v_n\) of an invertible matrix \(P\) give another natural basis. For one fixed column \(v=v_j\), let \(S\) be its coordinate support. Multiplication by \(v\) sends the codimension-one span of the other columns into the zero subspace: \(v v_i=0\) for \(i\ne j\). In the original basis the multiplication map \(x\mapsto vx\) has image the span of \(\{e_i^2:i\in S\}\), since every coefficient of \(v\) on its support is nonzero. As \(v\) annihilates an \((n-1)\)-dimensional subspace, this map has rank at most one. If \(|S|\ge2\), the pairwise-square hypothesis forces rank at least two, a contradiction. Hence every column of \(P\) has singleton support; invertibility makes \(P\) monomial. This proof works in every characteristic. For \(q>3\), the converse follows by an explicit change of natural basis if two nonzero squares are proportional: writing \(e_j^2=\beta e_i^2\), choose nonzero \(a\) with \(1+a^2\beta\ne0\), possible because the nonzero field has at least three elements and the quadratic has at most two roots. Put \(u=e_i+a e_j\) and \(v=e_i-(a\beta)^{-1}e_j\). Then \(uv=e_i^2-e_i^2=0\), while \(u,v\) are independent exactly when \(1+a^2\beta\ne0\); replace \(e_i,e_j\) by \(u,v\). This is a nonmonomial natural basis. If one square is zero, an analogous independent mixing of its zero-square vector with another basis vector yields a nonmonomial natural basis whenever \(n\ge2\). This establishes the stated exact characterization for \(q>3\).

**2. Exact occupancy probability.** The square rows of \(M\) are independent and uniform vectors of \(\mathbb F_q^n\). There are \((q^n-1)/(q-1)\) one-dimensional subspaces. Successive choices that avoid zero and all previously used projective directions have respectively \(q^n-1-j(q-1)\) possibilities for \(j=0,\ldots,n-1\), out of \(q^n\) each time. This gives \(P_{n,q}\) exactly. Taylor expansion of the finite product, with \(\sum_j[1+j(q-1)]=n+(q-1)\binom n2\), gives the displayed uniform-in-\(n\) first-order expansion for fixed \(q\).

**3. A deterministic rigidity criterion.** Assume the property in Step 1, the digraph \(\Gamma_M\) has no nonidentity vertex permutation preserving arcs, is strongly connected, and contains a loop. By Step 1, any algebra automorphism is monomial: \(g(e_i)=t_i e_{\sigma(i)}\) with \(t_i\ne0\). Comparing squares gives, for every \(i,j\),
\[
 m_{ij}t_j=t_i^2m_{\sigma(i),\sigma(j)}.
\]
Thus \(\sigma\) preserves the zero/nonzero pattern, so it must be the identity. On each arc, \(t_j=t_i^2\). At a loop, \(t_i=t_i^2\), hence \(t_i=1\). Strong connectivity propagates \(1\) along paths to every vertex. Therefore \(g\) is the identity.

**4. Probability of the graph conditions.** The probability that no loop exists is \(q^{-n}\). A non-strongly-connected directed graph has a nonempty proper union of terminal strongly connected components with no outgoing arc; a union bound over the vertex set \(S\) gives \(\sum_{s=1}^{n-1}\binom ns q^{-s(n-s)}\).

For a fixed nonidentity permutation \(\sigma\) moving exactly \(k\ge2\) vertices, at least \(k(2n-k)\) of the \(n^2\) ordered positions \((i,j)\) move under simultaneous permutation. For each nontrivial orbit of length \(\ell\ge2\) of positions, invariance of the independent Bernoulli support requires identical bits; its probability is \(p^\ell+(1-p)^\ell\le\rho^{\ell/2}\), by monotonicity of finite-dimensional \(\ell^s\)-norms. Multiplying over disjoint orbits yields at most \(\rho^{k(2n-k)/2}\le\rho^{kn/2}\). There are at most \(n^k\) permutations with that support size. Union-bounding over \(k\) gives the last term of \(B_{n,q}\). These events depend only on the support, but independence from square relations is **not** assumed: one overall union bound suffices.

**5. Exponential decay and singular conditioning.** The first term is \(O_q(n^2q^{-n})\). The cut sum is \(O_q(nq^{-(n-1)})\) because the terms with \(s=1,n-1\) dominate the interior terms for fixed \(q\). For large \(n\), the permutation sum is \(O_q(n^2\rho^n)\) by comparison with a geometric series of ratio \(n\rho^{n/2}\to0\). Because \(\rho\ge q^{-1}\), their sum is \(O_q(n^2\rho^n)\). Finally, \(\Pr(M\text{ nonsingular})=\prod_{i=1}^n(1-q^{-i})\), by successively choosing independent rows. Hence \(\Pr(M\text{ singular})\ge q^{-1}\), and conditioning costs at most the fixed factor \(q\). This proves all claims.

## Verification
The standalone file `verify.py` exhaustively checks every binary structure matrix in dimensions two and three and every invertible binary change of basis for the implication that pairwise-independent nonzero squares force a monomial natural-basis change; it checks the exact occupancy counts \(6/16\) and \(210/512\). It also constructs a concrete singular five-dimensional binary example with rows encoded as integers \([25,4,17,27,10]\): its rank is four, its rows are distinct and nonzero, and its support graph is strongly connected, looped, and asymmetric. Running the script prints `VERIFY_OK`. These finite checks do not establish the general probability bounds; Steps 1–5 do.

## Relationship to prior work
Kaygorodov, Martín González and Viruel (arXiv:2610.22248, first public October 15, 2026) explicitly ask in Question 22 for the asymptotic probability of a trivial automorphism group under uniformly random finite-field structure matrices. Boudi, Cabrera Casado and Siles Molina (arXiv:2006.14460, Theorem 2.4 and Corollary 2.7) developed the underlying two-linearly-independent-square property and natural-basis criterion. Their deterministic criterion is **credited, not claimed as new**. The exact projective-direction occupancy law, graph-asymmetry bound and the resulting unconditional **and singular-conditioned** random-algebra rigidity statement are the contributions presented here. Earlier results confined to the invertible/perfect model do not imply the singular-conditioned conclusion. Random walk and graph-evolution papers concern structured graph matrices rather than independent uniform coefficients.

## Limitations
The theorem is asymptotic in dimension with fixed field size; it does not treat sparse directed graph models, real Gaussian matrices, uniform sampling over isomorphism classes, or exact finite-dimensional automorphism distributions. The explicit exact natural-basis uniqueness probability is restricted to fields with more than three elements; for the two smaller fields only the sufficiency bound is asserted. The result gives no exact asymptotic **constant** for the exceptional automorphism event. The searched literature may omit an equivalent probabilistic theorem; priority has not been independently established. Computational tests cannot substitute for the general proof.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (2026), especially Question 22, https://arxiv.org/abs/2610.22248.
2. N. Boudi, Y. Cabrera Casado and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460 (2020), especially Theorem 2.4 and Corollary 2.7, https://arxiv.org/abs/2006.14460.
3. M. L. Rodiño Montoya, N. A. Viana Bedoya and C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604 (2025), https://arxiv.org/abs/2505.15604.
