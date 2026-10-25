# Smooth Ciani quartics and diagonal conic-bundle presentations over finite fields

## Finding
Let \(q\) be **any odd prime power**, \(k=\mathbb F_q\), and consider the marked six-dimensional linear system of Ciani quartics
\[
C_{A,B,C,D,E,F}:\quad AX^4+BY^4+CZ^4+DX^2Y^2+EX^2Z^2+FY^2Z^2=0.
\]
Two coefficient sextuples differing by one nonzero scalar define the same member; no projective coordinate transformations are identified. The number of geometrically smooth members is **exactly**
\[
\boxed{N_q=(q-1)^2(q^3-4q^2+6q-5).}
\]
Moreover, every such marked smooth quartic has exactly \(q(q^2-1)=|\operatorname{PGL}_2(\mathbb F_q)|\) presentations, up to simultaneous nonzero scalar multiplication, as the discriminant of a **diagonal** bidegree-\((2,2)\) divisor
\[
R:\quad \sum_{i=1}^3 X_i^2(a_i s^2+2b_i st+c_i t^2)=0
\quad\subset\mathbb P^1_{[s:t]}\times\mathbb P^2_{[X_1:X_2:X_3]}.
\]
All these divisors \(R\) are geometrically smooth, and the presentations over a fixed quartic form one free, transitive \(\operatorname{PGL}_2(\mathbb F_q)\)-orbit (acting on \([s:t]\)). Consequently the number of scalar-normalized geometrically smooth diagonal branch divisors is
\[
\boxed{M_q=q(q-1)^3(q+1)(q^3-4q^2+6q-5).}
\]
Their smooth degree-two covers of \(\mathbb P^1\times\mathbb P^2\) are members of the conic-bundle Fano threefold family considered in the references, but the count is of **coordinate-marked branch divisors**, not of abstract threefold isomorphism classes.

## Assumptions and scope
The ground field has odd cardinality \(q\ge3\). Geometric smoothness means smoothness after extension to an algebraic closure. Coordinates \([X:Y:Z]\) and \([s:t]\) remain fixed for coefficient counting; the \(\operatorname{PGL}_2(k)\)-orbit statement is separate. The Ciani system here is the entire six-monomial subspace, not only the one-parameter symmetric Ciani pencil. The branch equation is written with \(q_i(s,t)=a_i s^2+2b_i st+c_i t^2\). Its discriminant is
\[
\Delta(X_1,X_2,X_3)=\left(\sum_i b_iX_i^2\right)^2-\left(\sum_i a_iX_i^2\right)\left(\sum_i c_iX_i^2\right).
\]
Multiplying \(\Delta\) by \(-1\) would make no difference to its projective curve. No claims are made in characteristic two, nor about arbitrary non-diagonal bidegree-\((2,2)\) forms.

## Proof
**1. Exact smoothness criterion.** Put \(V=\operatorname{Sym}^2(k^2)\) with nondegenerate quadratic form \(Q(a,b,c)=b^2-ac\) and its associated polar bilinear form \(\langle\, ,\,\rangle\). The three column vectors \(v_i=(a_i,b_i,c_i)\) correspond to the \(q_i\). Writing \(z_i=X_i^2\), the quartic discriminant is the quadratic form \(Q(\sum_i z_i v_i)\). Its symmetric Gram matrix is \(G=(\langle v_i,v_j\rangle)\). By the Jacobian criterion applied to \(Q(X_1^2v_1+X_2^2v_2+X_3^2v_3)\), this quartic is geometrically smooth if and only if all three diagonal entries of \(G\), all three principal \(2\times2\) determinants, and \(\det G\) are nonzero. Necessity is seen on coordinate vertices, on coordinate lines, and finally at an all-nonzero point corresponding to a kernel vector of \(G\); conversely these three cases exhaust the possible supports of a singular point. The diagonal entries are \(Q(v_i)\), and \(-4\) times the principal determinant at \(i,j\) is the binary-quadratic resultant \(\operatorname{Res}(q_i,q_j)\). Since \(Q\) is nondegenerate, \(\det G\ne0\) if and only if \(v_1,v_2,v_3\) are linearly independent. Thus smoothness is **equivalent** to: (i) all \(q_i\) are separable binary quadratics; (ii) each pair is coprime over \(\bar k\); and (iii) the three vectors are linearly independent.

Under (i)–(ii) the surface \(R\) is smooth: a singular point would require every \(q_i\) with \(X_i\ne0\) to vanish at the same \([s:t]\). If at least two \(X_i\)'s are nonzero, this contradicts coprimality; if exactly one is nonzero, the corresponding separable \(q_i\) has a nonzero derivative. In odd characteristic the double cover branched along \(R\) is smooth as well.

**2. Count independent projective quadratic triples.** A projective separable binary quadratic corresponds bijectively to an effective reduced \(k\)-rational divisor of degree \(2\) on \(\mathbb P^1\). There are \(q^2\) of them: \(S=q(q+1)/2\) consist of two distinct rational points, and \(N=q(q-1)/2\) consist of a Frobenius-conjugate pair. Two projective quadratics are coprime exactly when their degree-two divisors are disjoint.

A coprime ordered pair \((q_1,q_2)\) determines a separable degree-two map \([q_1:q_2]:\mathbb P^1\to\mathbb P^1\). Its unique deck involution \(\iota\in\operatorname{PGL}_2(k)\) exchanges the points in each fiber. The \(S\) split involutions have two rational fixed points and \(m=q-1\) distinct reduced rational degree-two fibers; the \(N\) nonsplit involutions have two conjugate fixed points and \(m=q+1\) such fibers. For either type, exactly \(s=m/2\) of the reduced rational fibers are split degree-two divisors and exactly \(s\) are nonsplit. Every ordered pair of distinct reduced rational fibers determines the involution uniquely.

For two disjoint divisors, let \(k_0\in\{0,1,2\}\) count how many of them are split. The number of reduced rational degree-two divisors disjoint from both is
\[
A_{k_0}=\binom{q+1-2k_0}{2}+\frac{q(q-1)}2-(2-k_0),
\]
so \(A_0=q^2-2\), \(A_1=q^2-2q\), and \(A_2=q^2-4q+6\). Among these third choices, precisely \(m-2\) lie in the projective pencil \(\langle q_1,q_2\rangle\); these must be discarded to require linear independence. Summing over ordered pairs of fibers of an involution with \(s=m/2\) yields
\[
T(m)=s(s-1)(A_0+A_2)+2s^2A_1-m(m-1)(m-2).
\]
The total number of ordered projective triples satisfying (i)–(iii) is therefore
\[
S\,T(q-1)+N\,T(q+1)
=q(q-1)(q+1)(q^3-4q^2+6q-5).
\]
Each projective triple admits \((q-1)^3\) independent scalar lifts, and quotienting the simultaneous scalar leaves \((q-1)^2\) lifts. This proves the formula \(M_q\) for diagonal branch divisors.

**3. Every smooth Ciani curve has one orbit of presentations.** The coefficient space of Ciani quartics is the space of symmetric ternary Gram forms \(G\), with the correspondence described in Step 1. A smooth quartic has nonsingular \(G\). Every nonsingular ternary quadratic form over \(k\) is similar to \(Q\): the two determinant square classes become equal after scaling one form because the dimension is odd. Thus every smooth Ciani quartic is the discriminant of a diagonal presentation defined over \(k\). If two ordered bases \(v_i\) give proportional Gram matrices, their transition map \(T\in\operatorname{GL}_3(k)\) is a similitude of \(Q\). For \(T^tJT=\lambda J\), determinants give \(\det(T)^2=\lambda^3\), so \(\lambda=(\det(T)/\lambda)^2\) is a square. Rescaling \(T\) gives an isometry; changing its sign, if needed, makes its determinant \(1\). The resulting element of \(\operatorname{SO}_3(k)\) is induced by the usual action of \(\operatorname{PGL}_2(k)\) on binary quadratic forms (the adjoint representation, an isomorphism in odd characteristic). The action on a projective ordered basis is free. Hence each smooth Ciani quartic has exactly \(|\operatorname{PGL}_2(k)|=q(q^2-1)\) projective diagonal presentations. Dividing \(M_q\) by this number gives \(N_q\).

## Verification
The standalone \(`verify.py`\) independently enumerates projective separable binary quadratics, coprimality, and the determinant condition for \(q=3,5,7,11\), obtaining respectively \(96,6000,61824,1198560\) projective ordered quadratic triples as predicted. A **separate** loop enumerates projective six-term Ciani coefficients and applies their Gram/Jacobian smoothness test for \(q=3,5,7\), obtaining \(16,800,6624\) smooth curves, also as predicted. An exhaustive enumeration of the \(3^9\) raw diagonal forms over \(\mathbb F_3\) finds exactly \(16\) smooth discriminants, each with \(48\) nonzero equations (\(24\) after common scalar quotient). The script prints \(`VERIFY_OK`\). These finite checks are independent corroboration, not a proof of the all-prime-power theorem.

## Relationship to prior work
DeVleming–Ji–Kennedy-Hunt–Quek establish the global discriminant map for bidegree-\((2,2)\) Fano conic-bundle models and recall the general \(63\) quadratic determinantal representations of a smooth plane quartic; that statement does not count coefficient-marked smooth Ciani forms over finite fields or determine the **diagonal** presentation fiber. Frei–Ji–Sankar–Viray–Vogt describe their discriminant covers and uniqueness of quadratic triples after fixing the relevant étale cover; this is a different equivalence datum from fixing a quartic and requiring a diagonal presentation. Janasz–Pokora–Zieliński study bitangents of the symmetric **one-parameter** Ciani pencil over \(\mathbb C\), not this entire marked six-term family or its uniform finite-field mass. The characteristic-three value \(16\) was already obtained in earlier finite-field work and is **not** claimed new in isolation. The new claim is the uniform odd-\(q\) formula together with the free transitive presentation fiber.

## Limitations
This is not an abstract isomorphism-class count, a count of arbitrary \((2,2)\) branch surfaces, or a statement in characteristic \(2\). The proof uses ordinary point-counting for the coordinate-marked diagonal locus and does not determine rationality or isomorphism classes of the associated conic-bundle threefolds. The literature comparison leaves the possibility of a previously unindexed equivalent finite-field mass formula; independent external validation has not been performed.

## References
1. K. DeVleming, L. Ji, P. Kennedy-Hunt, M. H. Quek, *The K-moduli space of a family of conic bundle threefolds*, arXiv:2403.09557, first posted 2024-03-14, especially Sections 1–2 and 9. https://arxiv.org/abs/2403.09557
2. S. Frei, L. Ji, S. Sankar, B. Viray, I. Vogt, *Curve classes on conic bundle threefolds and applications to rationality*, arXiv:2207.07093, first posted 2022-07-14, especially Theorem 2.6 and Section 4. https://arxiv.org/abs/2207.07093
3. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 2023-08-31, especially Section 3. https://arxiv.org/abs/2308.16514
