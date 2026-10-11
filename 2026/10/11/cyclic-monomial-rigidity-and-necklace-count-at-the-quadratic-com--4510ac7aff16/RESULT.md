# Cyclic-monomial rigidity and necklace count at the quadratic commutator resonance threshold

## Finding
Let \(p,q\ge 1\) be relatively prime integers, \(c>0\), and \(n=p+q\). For \(A,T\in M_n(\mathbb C)\) define the inner derivation \(\Delta_A(X)=AX-XA\). Suppose \(T\) is invertible and
\[
(\Delta_A-pcI)(\Delta_A+qcI)T=0.
\]
Then there exist a complex scalar \(\alpha\), a cyclic word \(\epsilon=(\epsilon_0,\ldots,\epsilon_{n-1})\) with exactly \(q\) symbols \(+\) and \(p\) symbols \(-\), a basis \(e_0,\ldots,e_{n-1}\), and nonzero complex weights \(w_j\) for which
\[
Ae_j=(\alpha+cs_j)e_j,\qquad Te_j=w_je_{j+1\pmod n},
\]
where \(s_0=0\) and \(s_{j+1}-s_j=p\) for \(\epsilon_j=+\), whereas \(s_{j+1}-s_j=-q\) for \(\epsilon_j=-\), and \(s_n=0\). In particular, \(A\) has simple spectrum. Every displayed construction conversely satisfies the quadratic commutator equation with invertible \(T\).

Up to simultaneous similarity and scalar translation \(A\mapsto A+zI\), the **spectra of \(A\)** allowed by invertible solutions are classified bijectively by length-\(n\) necklaces of weight \(q\). Every such necklace is primitive, and the number of distinct spectral patterns is exactly
\[
\frac1n\binom{n}{q}.
\]
This is a classification of spectral patterns, **not** a count of similarity classes of pairs: the cyclic weights of \(T\) carry additional continuous invariants.

Writing \(D=\Delta_A(T)\), every such solution also satisfies
\[
T^n=(-1)^{n-1}\det(T)I,\qquad
\det(D)=(-1)^p p^q q^p c^n\det(T),
\]
\[
D^n=(-1)^{n-1+p}p^q q^p c^n\det(T)I.
\]

## Assumptions and scope
All matrices are over \(\mathbb C\). The scalar \(c\) is a strictly positive real number. The operators \(I\) in the commutator polynomial denote the identity on the matrix space, whereas the \(I\) in power identities is the identity \(n\times n\) matrix. Invertibility of \(T\) and the *minimal* dimension \(n=p+q\) are essential hypotheses. Equivalence of spectral patterns permits translating all eigenvalues by one complex scalar; it does not permit scaling the eigenvalues or changing \(p,q,c\).

## Proof
**Step 1: Reduction to a semisimple spectral graph.** Let \(A=S+K\) be the additive Jordan decomposition, with \(S\) semisimple, \(K\) nilpotent, and \(SK=KS\). The commuting derivations \(\Delta_S\) and \(\Delta_K\) have, respectively, semisimple and nilpotent actions on \(M_n(\mathbb C)\). For \(f(z)=(z-pc)(z+qc)\), decompose \(M_n(\mathbb C)\) into eigenspaces \(V_\lambda\) of \(\Delta_S\). On \(V_\lambda\) the operator \(f(\Delta_A)=f(\lambda I+\Delta_K)\) is invertible if \(\lambda\) is not a root of \(f\), since its constant term is nonzero and \(\Delta_K\) is nilpotent. Therefore \(T\) belongs to \(V_{pc}\oplus V_{-qc}\). (The roots are simple, so this also implies \(\Delta_K(T)=0\), although that extra assertion is not needed below.)

Choose an eigenbasis of \(S\) and denote its diagonal entries, with repetitions, by \(\lambda_1,\ldots,\lambda_n\). Every nonzero matrix entry \(T_{ij}\) obeys
\[
\lambda_i-\lambda_j\in\{pc,-qc\}.
\]
Invertibility of \(T\) gives a permutation \(\sigma\) with \(\prod_jT_{\sigma(j),j}\ne0\). Each cycle of \(\sigma\) traces spectral increments of \(+pc\) and \(-qc\), whose sum is zero. Thus if a cycle has \(u\) positive and \(v\) negative increments, then \(up=vq\); relative primality forces \((u,v)=(qt,pt)\) for some positive integer \(t\). Consequently every permutation cycle has length divisible by \(n=p+q\). Since the whole permutation acts on exactly \(n\) indices, it consists of one \(n\)-cycle, containing precisely \(q\) positive and \(p\) negative increments.

If two \(\lambda\)-values along that cycle coincide, the nonempty proper directed path between them would have zero increment sum and hence length a positive multiple of \(n\), an impossibility. Hence \(S\) has \(n\) distinct eigenvalues. As \(K\) commutes with \(S\), \(K\) must be diagonal in this eigenbasis. Its nilpotence implies \(K=0\). Therefore \(A=S\) itself has simple spectrum.

**Step 2: Forced support of the invertible operator.** Write the eigenvalues in the order of the nonzero permutation cycle: \(\alpha+cs_j\), for the integer partial sums in the statement. Since \(p\equiv-q\pmod n\), each step is congruent to \(p\pmod n\). Because \(\gcd(p,n)=1\), the integers \(s_0,\ldots,s_{n-1}\) occupy all \(n\) residue classes modulo \(n\). For any fixed eigenvalue \(\alpha+cs_j\), the two candidate target eigenvalues \(\alpha+c(s_j+p)\) and \(\alpha+c(s_j-q)\) belong to the *same* residue class modulo \(nc\). Exactly one eigenvalue in the available spectrum lies in that class, and the displayed permutation cycle ensures at least one of those two candidate numbers occurs. Thus **exactly one** allowed target occurs for each source. Every matrix entry of \(T\) outside the single cycle vanishes; each cycle entry is nonzero by invertibility. This proves the claimed cyclic monomial normal form. Conversely, the displayed cycle with any nonzero weights is invertible and every nonzero entry of \(T\) has derivation eigenvalue either \(pc\) or \(-qc\), so the quadratic polynomial annihilates it.

**Step 3: Spectral classification.** Any word of weight \(q\) and length \(n\) has no proper rotational period: if a shorter period \(d\) divides \(n\), the symbol count forces \(n\mid qd\), and coprimality of \(q,n\) forces \(n\mid d\). Therefore its rotation orbit has \(n\) members. For the spectrum associated with such a word, the sole allowed successor of each eigenvalue is determined intrinsically by the set of eigenvalues, as established in Step 2. Recovering successive positive/negative differences therefore recovers the word up to rotation. Scalar translation preserves these differences, and a rotation merely changes the starting vertex. Hence distinct necklaces give distinct spectral patterns up to translation, and the orbit count is \(\binom nq/n\).

**Step 4: Exact powers and determinant.** Let \(W=\prod_{j=0}^{n-1}w_j\). A full traversal of the monomial cycle yields \(T^n=WI\), and the sign of an \(n\)-cycle gives \(\det T=(-1)^{n-1}W\). The operator \(D=\Delta_A(T)\) uses the same cycle, multiplying exactly \(q\) weights by \(pc\) and exactly \(p\) by \(-qc\). Thus \(\det D=(-1)^p p^q q^p c^n\det T\) and \(D^n=(-1)^p p^q q^p c^n WI\), proving all formulas.

## Verification
A standalone Python 3 standard-library verifier, `verify_resonance.py`, enumerates every coprime ordered pair \((p,q)\) with \(1\le p,q\le5\). It checks the primitive-necklace counts, all distinct translation-normalized spectral sets, forced successors, and the quadratic commutator and power identities by exact integer arithmetic on explicit matrices. It reports `CYCLIC_RESONANCE_EXACT_FINITE_OK 19 coprime pairs`. Exhaustive finite testing is illustrative, **not** a proof of the quantified theorem; the proof is the four analytic steps above.

For example, at \((p,q)=(2,3)\) the two patterns are represented after translation by \(\{0,1,2,3,4\}\) and \(\{0,2,3,4,6\}\), each multiplied by \(c\).

## Relationship to prior work
Stanković's *Spectral Rigidity of Commutators: Dynamics, Resonance, and Nilpotency* (arXiv:2608.29574v1, first publicly submitted 2026-08-30) establishes the sharp dimension threshold for invertible solutions when the two real roots have opposite signs, and supplies a cyclic existence construction at and beyond that threshold. This finding concerns a different assertion: **every** invertible solution at the **threshold dimension** is forced into one cyclic monomial form with simple spectrum, the precise set of spectral patterns is counted by primitive necklaces, and every such solution obeys the explicit power identities. The motivating abstract alone does not assert this complete equality-case classification; inaccessible full text leaves a genuine overlap risk.

The ordinary finite-dimensional Jordan decomposition and permutation expansion of a determinant are classical ingredients, not novel claims.

## Limitations
The result does not classify noninvertible solutions, dimensions larger than \(p+q\), nonreal or repeated polynomial roots, or all simultaneous-similarity classes of the weights. The spectral-type count fixes the parameters \(p,q,c\), permits common translations only, and is not the number of distinct matrix pairs. General functional-analytic consequences and optimal quantitative perturbation bounds are not asserted. The complete primary manuscript could not be inspected, so implicit coverage in its proofs or appendices remains a literature-comparison risk; independent validation has not been performed.

## References
1. H. Stanković, *Spectral Rigidity of Commutators: Dynamics, Resonance, and Nilpotency*, arXiv:2608.29574v1 (public preprint, 2026-08-30), https://arxiv.org/abs/2608.29574.
2. Classical Jordan--Chevalley decomposition and finite-dimensional determinant/permutation expansion (standard linear algebra; used in the proof).
