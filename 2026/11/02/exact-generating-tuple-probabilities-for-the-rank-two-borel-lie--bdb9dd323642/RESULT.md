# Exact generating-tuple probabilities for the rank-two Borel Lie algebra over finite fields

## Finding
Let \(q\) be any prime power, let \(K=\mathbb F_q\), and let \(\mathfrak b=\mathfrak b_3(K)\) be the Lie algebra of traceless upper-triangular \(3\times3\) matrices with commutator bracket. For every integer \(k\ge1\), sample independently and uniformly \(X_1,\ldots,X_k\in\mathfrak b\), and let \(P_{q,k}\) denote the probability that their **Lie subalgebra** (including arbitrary \(K\)-linear combinations and iterated brackets) equals \(\mathfrak b\). Then
\[
P_{q,k}=\begin{cases}
(1-q^{-k})(1-q^{1-k})^3,&\operatorname{char}K\ne3,\\
(1-q^{-k})(1-q^{1-k})^2(1-q^{2-k}),&\operatorname{char}K=3.
\end{cases}
\]
Consequently, the minimal number of Lie generators is two outside characteristic three and three in characteristic three. In particular, no pair generates this algebra in characteristic three, although a triple does. The formulas remain valid over nonprime finite fields.

## Assumptions and scope
All statements concern ordinary Lie algebra generation over \(K\), not restricted-Lie generation, group generation, or generation as an associative matrix algebra. The dimension is always five. Write a general element as
\[
X(a,b,u,v,w)=\begin{pmatrix}a&u&w\\0&b&v\\0&0&-a-b\end{pmatrix}.
\]
Let \(T\) be the diagonal torus (the \(a,b\) coordinates), let \(N\) be the strictly upper-triangular ideal, and let \(Z=[N,N]=K E_{13}\). The quotient \(\mathfrak b/Z\) is \(T\ltimes W\), where \(W=(K E_{12}\oplus K E_{23})\) is abelian and the two \(T\)-weights are
\[
\alpha(a,b)=a-b,\qquad\beta(a,b)=a+2b.
\]
The coefficient \(3\) in the determinant of these two weight functionals is the source of the characteristic-three transition.

## Proof
**1. A central-quotient generation criterion.** The quotient \(\mathfrak b/Z\) has abelian nilradical \(W\). If the images of a tuple generate this quotient, its generated subalgebra \(H\subseteq\mathfrak b\) surjects onto \(T\ltimes W\). Its derived subalgebra maps onto \(W\), so it contains two elements with linearly independent \(E_{12},E_{23}\) images. Their commutator has \(E_{13}\) component equal to the determinant of these two images, and hence is nonzero in \(Z\). Therefore \(Z\subseteq H\) and \(H=\mathfrak b\). The converse follows by taking the quotient. This argument works in every characteristic.

**2. Rank criterion outside characteristic three.** Write the sampled coordinates as rows \(A=(a_i)\), \(B=(b_i)\), \(U=(u_i)\), and \(V=(v_i)\) in \(K^k\); put \(a=A-B\) and \(b=A+2B\). Projection of the generated Lie algebra to \(T\) must be surjective, i.e. \(\operatorname{rank}(A,B)=2\). Under this condition both \(a\) and \(b\) are nonzero. In \(\mathfrak b/Z\), the simple-root components of pairwise brackets of generators are
\[
(a_i u_j-a_j u_i,\quad b_i v_j-b_j v_i).
\]
Thus the first root projection of the derived subalgebra is nonzero exactly when \(\operatorname{rank}(a,U)=2\), and similarly the second root projection is nonzero exactly when \(\operatorname{rank}(b,V)=2\). When the characteristic is not three, the two weights are independent; under the surjective torus projection, its adjoint action has these distinct simultaneous weight spaces, and a nonzero derived projection to each can be separated into its root line. Therefore all of \(W\) is generated if and only if both indicated ranks equal two. Conversely any generating tuple must pass all three rank tests. No division by two is used, so the argument includes characteristic two.

**3. Rank criterion in characteristic three.** Here \(\alpha=\beta\) because \(a+2b=a-b\) in characteristic three. Under \(\operatorname{rank}(A,B)=2\), their common row \(a\) is nonzero. The torus acts on both root coordinates by the same scalar. In the quotient, the \(W\)-part of the derived subalgebra is exactly the image of the kernel of the nonzero functional \(a:K^k\to K\) under the map \(t\mapsto(U\cdot t,V\cdot t)\). Indeed its generators are the root-coordinate vectors \(a_i(U_j,V_j)-a_j(U_i,V_i)\), which span that image, and the common-weight adjoint action does not enlarge the span. The image is two-dimensional precisely when
\[
\operatorname{rank}(a,U,V)=3.
\]
Thus this and the independent torus-rank condition characterize generation. In particular, \(k\ge3\) is necessary.

**4. Exact probabilities.** Independently uniform rows \(A,B,U,V\in K^k\) arise from the uniform matrices. The probability that \(A,B\) are independent is
\[
(1-q^{-k})(1-q^{1-k}).
\]
Conditioned on this event, \(a\) and \(b\) are each fixed nonzero rows. Outside characteristic three, each of the independent uniform rows \(U,V\) avoids its respective one-dimensional weight row with probability \(1-q^{1-k}\), so the conditional probability is \((1-q^{1-k})^2\). In characteristic three, the images of \(U,V\) in \(K^k/Ka\), a space of dimension \(k-1\), must be linearly independent. Their conditional probability is \((1-q^{1-k})(1-q^{2-k})\). Multiplication by the torus probability yields the asserted two formulas, including the zero factors for insufficient \(k\).

The root \(E_{13}\) and all corresponding coefficients have been accounted for in Step 1; no assumption on its sampled row is needed.

## Verification
The standalone file `check_borel.py` implements the full five-coordinate commutator and constructs the generated Lie subalgebra by repeated closure and exact row-echelon reduction. It separately implements the rank criteria and compares the two. Its output is `check_borel_output.txt`. Exhaustive enumeration over every ordered tuple covers \((q,k)=(2,1),(2,2),(2,3),(3,2)\); the exact respective counts of generating tuples are \(0/32\), \(96/1024\), \(12096/32768\), and \(0/59049\). Seeded independent samples cover \(q=3,5,7\) and an actual quadratic extension field of order four (with polynomial \(z^2+z+1\)). Sample frequencies are not claimed to equal exact theoretical fractions. The checker's final output is `VERIFY_OK`. These finite tests corroborate the proof but do not substitute for it.

## Relationship to prior work
Jezernik and Zozaya, *Random generation of the special linear Lie algebra over finite fields* (arXiv:2606.31747, first public 30 June 2026) study the whole \(\mathfrak{sl}_n(K)\) and high-probability two-generation, with exceptional behavior when \((n,p)=(3,3)\). Their theorem does not calculate generating-tuple probabilities for the fixed five-dimensional solvable Borel \(\mathfrak b_3(K)\). Cantor, Jezernik and Zozaya, *Two-generation of traceless matrices over finite fields* (arXiv:2404.11240) likewise address the full traceless algebra, not a Borel. Jezernik and Miščič, *Random Lie bracket on \(\mathfrak{sl}_2(\mathbb F_p)\)* (doi:10.1002/rsa.70042), analyze a random bracket process in a different three-dimensional Lie algebra. Bulois, *Very nilpotent basis and \(n\)-tuples in Borel subalgebras* (doi:10.1016/j.crma.2010.12.005), studies tuples belonging to some Borel, not uniform tuples generating one prescribed Borel. None of the inspected material explicitly supplies these exact formulas, but older generic finite solvable-Lie generation methods might imply them and priority has not been certified.

## Limitations
The result treats the split rank-two Borel inside \(\mathfrak{sl}_3\) only; it does not classify generating tuples of higher-rank Borels, arbitrary solvable Lie algebras, nonuniform sampling, or associative/subgroup generation. The literature comparison is bounded, not a global uniqueness proof. Independent mathematical audit has not been performed.

## References
1. U. Jezernik and A. Zozaya, *Random generation of the special linear Lie algebra over finite fields*, arXiv:2606.31747 (2026), first publicly submitted 2026-06-30.
2. G. Cantor, U. Jezernik and A. Zozaya, *Two-generation of traceless matrices over finite fields*, arXiv:2404.11240 (2024).
3. U. Jezernik and M. Miščič, *Random Lie bracket on \(\mathfrak{sl}_2(\mathbb F_p)\)*, *Random Structures & Algorithms* (2026), doi:10.1002/rsa.70042.
4. M. Bulois, *Very nilpotent basis and \(n\)-tuples in Borel subalgebras*, *C. R. Math.* (2011), doi:10.1016/j.crma.2010.12.005.
