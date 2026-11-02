# Nilpotent-sampling invariance for random generation of the special linear Lie algebra

## Finding

Let \(q\) be any prime power, \(K=\mathbb F_q\), and \(L=\mathfrak{sl}_2(K)\) with the commutator Lie bracket. Fix \(x\in L\); sample \(Y_1,\ldots,Y_k\in L\) independently and uniformly, where \(k\ge1\). Write \(G_{x,k}\) for the event that \(x,Y_1,\ldots,Y_k\) generate \(L\) **as a Lie algebra over \(K\)**. The probability of this event depends on \(x\) only through the following types.

For odd \(q\), write \(x=\begin{pmatrix}a&b\\c&-a\end{pmatrix}\) and \(\Delta(x)=a^2+bc\). Then

\[
\Pr(G_{x,k})=\begin{cases}
(1-q^{-k})(1-q^{1-k}),&x=0,\\
1-q^{-k},&x\ne0,\ \Delta(x)=0,\\
(1-q^{-k})^2,&\Delta(x)\ne0\text{ a square in }K,\\
1-q^{-2k},&\Delta(x)\text{ a nonsquare in }K.
\end{cases}
\]

For even \(q\), the center is \(Z(L)=KI\) and

\[
\Pr(G_{x,k})=\begin{cases}
(1-q^{-k})(1-q^{1-k}),&x\in KI,\\
1-q^{-k},&x\notin KI.
\end{cases}
\]

For odd \(q\), the four seed classes have respectively \(1\), \(q^2-1\), \(q(q^2-1)/2\), and \(q(q-1)^2/2\) matrices. For even \(q\), the center has \(q\) matrices and its complement has \(q^3-q\). These disjoint classes exhaust the entire algebra.

Consequently, in odd characteristic **every nonzero traceless matrix has a generating partner**, but the number of such partners separates three determinant classes; in characteristic two a nonzero central matrix has no single generating partner. Moreover, the full law for an unrestricted independent random \(k\)-tuple is characteristic-independent:
\[
\Pr(\langle Y_1,\ldots,Y_k\rangle_{\rm Lie}=L)=(1-q^{-k})(1-q^{1-k}).
\]

**Nilpotent-sampling invariance (the principal assertion).** Let \(\mathcal N_q=\{u\in L:u^2=0\}\), which has exactly \(q^2\) elements. Replace each \(Y_i\) by an independent uniform \(N_i\in\mathcal N_q\), keeping the fixed seed \(x\) arbitrary. For **every** prime power \(q\), every \(x\in L\), and every \(k\ge1\), the probability of generating \(L\) is **unchanged**, and is given by the identical casewise formulas above. This remains true with no fixed seed, where both sampling schemes have success probability \((1-q^{-k})(1-q^{1-k})\). Yet the **generated-subalgebra dimension distributions differ sharply**: a tuple of nilpotent matrices generates only dimensions \(0\), \(1\), or \(3\), never dimension \(2\). More precisely, for uniform independent nilpotent \(N_1,\ldots,N_k\),
\[
\begin{aligned}
\Pr(\dim\langle N_1,\ldots,N_k\rangle_{\rm Lie}=0)&=q^{-2k},\\
\Pr(\dim\langle N_1,\ldots,N_k\rangle_{\rm Lie}=1)&=(q+1)(q^k-1)q^{-2k},\\
\Pr(\dim\langle N_1,\ldots,N_k\rangle_{\rm Lie}=2)&=0,\\
\Pr(\dim\langle N_1,\ldots,N_k\rangle_{\rm Lie}=3)&=(1-q^{-k})(1-q^{1-k}).
\end{aligned}
\]
By contrast, uniform full-algebra sampling assigns positive probability to dimension two as soon as \(k\ge2\): its exact count among \(q^{3k}\) ordered tuples is \((q+1)[q^{2k}-(q+1)q^k+q]\). Thus **the full-generation event is insensitive to the drastic restriction to the nilpotent cone, even though the intermediate generated-algebra statistics change**.

The conditional waiting time \(T_x=\min\{k\ge1:G_{x,k}\}\) is almost surely finite. Its mean is, for odd \(q\), respectively \(q(2q+1)/(q^2-1)\), \(q/(q-1)\), \(q(q+2)/(q^2-1)\), and \(q^2/(q^2-1)\) in the four displayed cases; for even \(q\), it is \(q(2q+1)/(q^2-1)\) on \(KI\) and \(q/(q-1)\) off the center.

## Assumptions and scope

All generation, dimensions, and randomness are over the **entire coefficient field** \(K=\mathbb F_q\), not over its prime subfield. Matrices have trace zero. The random samples are independent and uniform on the \(q^3\) matrices in \(L\). No restriction is imposed on the extension degree of \(K\). For odd \(q\), "square" explicitly means a nonzero square; the nilpotent case \(\Delta=0\) is separate. For even \(q\), all scalar matrices have trace zero, so the central case includes zero and nonzero scalars.

## Proof

**1. Proper two-dimensional subalgebras for odd characteristic.** Every nonzero \(x\in L\) has a one-dimensional centralizer in \(L\): its centralizer in \(M_2(K)\) is \(KI+Kx\), and the trace-zero part is \(Kx\) because \(2\ne0\). Hence any two-dimensional Lie subalgebra \(B\) is nonabelian. Its derived line is \(KE\), with \(E\ne0\), and there exists \(H\in B\) with \([H,E]=E\), after rescaling. Trace invariance yields \(\operatorname{tr}(E^2)=\operatorname{tr}([H,E]E)=0\). Since \(E\) is traceless and \(\operatorname{tr}(E^2)=-2\det E\), we get \(\det E=0\), so \(E\) is nonzero nilpotent. The relation \([H,E]=E\) implies \(H(\ker E)\subseteq\ker E\). Thus \(B\) stabilizes the unique line \(\ker E\subset K^2\), and, by dimension, equals its Borel stabilizer. Conversely each of the \(q+1\) projective lines has a two-dimensional Borel stabilizer. This proves all the required maximal proper-subalgebra assertions without invoking an algebraic-closure classification.

**2. Incidence determined by the quadratic type.** A nonzero traceless \(x\) has characteristic polynomial \(t^2-\Delta(x)\). Its number of \(K\)-rational eigenlines, hence of Borel subalgebras containing it, is respectively one when \(\Delta=0\), two when \(\Delta\) is a nonzero square, and zero when \(\Delta\) is nonsquare. Distinct Borels have intersection \(Kx\) when they share a split semisimple \(x\ne0\); the intersection has dimension one. Every proper Lie subalgebra containing a nonzero \(x\) is either \(Kx\) or one of these Borels. A random element lies in a given Borel with probability \(1/q\), and in a given one-dimensional line with probability \(1/q^2\). For \(k\) independent random elements, the probabilities multiply. In the nilpotent case, failure is membership of all \(Y_i\) in the unique Borel, hence \(q^{-k}\). In the split case failure is the union of membership in either of two Borels, giving \(2q^{-k}-q^{-2k}\). In the nonsplit case the only obstruction is that all \(Y_i\in Kx\), giving \(q^{-2k}\). This proves the three nonzero odd-characteristic formulas.

**3. The zero seed in odd characteristic.** There are \(q^2+q+1\) one-dimensional linear subspaces of \(L\). Exactly \(q+1\) two-dimensional linear subspaces are Lie subalgebras, by Step 1. Each contains \(q+1\) lines. For \(k\) ordered elements, exactly \(q^k-1\) tuples generate any prescribed one-dimensional subspace, and exactly \(q^{2k}-1-(q+1)(q^k-1)\) tuples generate any prescribed two-dimensional Lie subalgebra. All-zero tuples number one. Since the generated Lie algebra of any tuple is uniquely determined, summing the proper-dimensional strata gives
\[
1+(q^2+q+1)(q^k-1)+(q+1)\bigl[q^{2k}-1-(q+1)(q^k-1)\bigr]
=(q+1)q^{2k}-q^{k+1}.
\]
Subtracting from \(q^{3k}\) and dividing gives \((1-q^{-k})(1-q^{1-k})\).

**4. Characteristic two.** Write traceless matrices as \(x=\begin{pmatrix}a&b\\c&a\end{pmatrix}\). Then \([x,y]=(bc'-b'c)I\). The center and derived algebra both equal \(KI\), and \(L/KI\) is a two-dimensional abelian vector space with a nondegenerate alternating commutator form. A family generates \(L\) exactly when its image spans \(L/KI\): independence of two projections supplies a nonzero central bracket, and the converse follows from abelianness of the quotient. If the fixed \(x\) is central, the \(k\) random projections must span a two-dimensional space, whose exact probability is \((1-q^{-k})(1-q^{1-k})\). If \(x\) is noncentral, failure means all \(k\) projections lie on the line \(K\bar x\), of probability \(q^{-k}\). The same rank argument for an entirely random \(k\)-tuple gives the unconditional formula.

**5. Why nilpotent sampling has exactly the same generation law.** For odd \(q\), the square-zero cone is the disjoint union of the zero matrix and the \(q+1\) punctured nilpotent projective lines, each associated with a unique rational kernel line. Hence \(|\mathcal N_q|=1+(q+1)(q-1)=q^2\). Each Borel meets \(\mathcal N_q\) in its one-dimensional nilpotent radical, of size \(q\); the intersection of any two distinct Borels contains no nonzero nilpotent. Therefore a uniform nilpotent lies in a prescribed Borel with probability \(q^{-1}\), and in any pairwise Borel intersection with probability \(q^{-2}\), exactly the same as an unrestricted uniform matrix. The same one-/two-/zero-Borel obstruction calculation in Step 2 proves **every fixed-seed conditional generation probability is unchanged**. Without a seed, any proper subalgebra generated by nilpotent elements is contained in a single Borel, whose nilpotent part is a line, so the generated Lie algebra is at most one-dimensional. Exactly \(q+1\) distinct nilpotent lines contribute \(q^k-1\) nonzero ordered tuples each, with one all-zero tuple. This gives the four displayed dimension probabilities and the same full-generation probability.

For even \(q\), the condition \(u^2=0\), with \(u=\begin{psmallmatrix}a&b\\c&a\end{psmallmatrix}\), is \(a^2=bc\). Squaring is bijective on \(K\), so the quotient map \(\pi:\mathcal N_q\to L/KI\), \(u\mapsto (b,c)\), is a bijection. Consequently nilpotent-uniform and full-algebra-uniform samples have **identically distributed quotient projections**, and the fixed-seed generation event depends only on whether these projections span the two-dimensional quotient. This proves sampling invariance. On any quotient line \(K(b,c)\), the unique square-zero lift is \(t\mapsto (t\sqrt{bc},tb,tc)\), a **linear** one-dimensional subspace of \(L\). Hence a tuple whose projections span one line generates a one-dimensional Lie subalgebra, not a plane. Independent projections span two dimensions and yield the full Lie algebra through their nonzero central bracket. Counting the \(q+1\) lines yields the same exact \(0,1,3\)-dimensional distribution as in odd characteristic.

**6. Waiting times and sharpness.** Because success at step \(k\) is a nested event, \(\Pr(T_x>k)=1-\Pr(G_{x,k})\) for \(k\ge1\); at \(k=0\) failure is certain. Summing the geometric series \(\mathbb E T_x=\sum_{k\ge0}\Pr(T_x>k)\) yields the displayed means. In particular, for odd characteristic \(k=1\) gives a positive probability for every \(x\ne0\), while in characteristic two a nonzero central \(x\) gives zero probability for \(k=1\), but positive probability for \(k=2\).

## Verification

The standalone `verify.py` and `verify_nilpotent.py` independently implement finite-field arithmetic (including \(\mathbb F_4\)), the matrix commutator, row reduction, and generated-Lie-subalgebra dimension. It directly checks **every fixed matrix and every possible random additional tuple** for \(q=2,3,4,5,7\) at \(k=1\), and \(q=2,3\) at \(k=2\), against the exact formulas, without using the Borel-incidence proof as a decision procedure. It also checks the characteristic-dependent type counts. The associated `verify.log` and `verify_nilpotent.log` record `VERIFY_OK` and `NIL_VERIFY_OK`, including tests of every prescribed first matrix under the restricted sampling law. The nilpotent verifier also checks exact cardinalities of the square-zero cones. Exhaustive calculations are checks in these finite fields, not a proof of the unrestricted prime-power statement.

## Relationship to prior work

Jezernik and Zozaya's 2026 preprint establishes asymptotic random two-generation of \(\mathfrak{sl}_n(\mathbb F_q)\) over growing ranks or field sizes; it does not formulate this conditional, determinant-type-resolved all-\(k\) law in the inspected text. Jezernik and Miščič study a different random-bracket walk in \(\mathfrak{sl}_2(\mathbb F_p)\), assuming a generating pair. Cantor, Jezernik, and Zozaya establish two-generation existence, not an exact fixed-seed partner count in their accessible introductory material. An earlier three-dimensional subalgebra-count result records \(q+1\) Lie-subalgebra planes for perfect three-dimensional algebras. That total alone does **not** determine the incidence of planes with a prescribed nilpotent, split, or nonsplit element, which is the new conditional invariant treated here. These comparisons are not a claim of independently certified historical priority.

## Limitations

This calculation concerns \(\mathfrak{sl}_2\), not general \(\mathfrak{sl}_n\). Its sampling-invariance result is for the uniform square-zero cone and uniform full-algebra distributions, not arbitrary nonuniform laws, non-nilpotent conjugacy classes, or group generation. The probability of unrestricted generation and the plane count are elementary consequences of preexisting structural results; the asserted contribution is the complete fixed-seed type-resolved law, including characteristic two and all tuple lengths. Older literature on maximal Lie subalgebras and \(3/2\)-generation could potentially imply parts of the conditional classification, and no independent audit has been performed.

## References

1. U. Jezernik and A. Zozaya, *Random generation of the special linear Lie algebra over finite fields*, arXiv:2606.31747, first public 2026-06-30, https://arxiv.org/abs/2606.31747.
2. U. Jezernik and M. Miščič, *Random Lie bracket on \(\mathfrak{sl}_2(\mathbb F_p)\)*, Random Structures & Algorithms 68 (2026), e70042, https://doi.org/10.1002/rsa.70042.
3. O. Cantor, U. Jezernik, and A. Zozaya, *Two-generation of traceless matrices over finite fields*, arXiv:2404.11240 (2024), and Linear Algebra and its Applications 713 (2025), 1–17, https://arxiv.org/abs/2404.11240.
4. A. Chistopolskaya, *On nilpotent generators of the Lie algebra*, Linear Algebra and its Applications 559 (2018), 73–79, https://doi.org/10.1016/j.laa.2018.09.005.
5. *Plane counts control subalgebra commutativity in dimension three*, published mathematical record, 2026-09-18, https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c.
