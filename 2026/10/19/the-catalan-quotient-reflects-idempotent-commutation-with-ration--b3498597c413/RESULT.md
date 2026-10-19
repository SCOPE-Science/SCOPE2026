# The Catalan quotient reflects idempotent commutation, with rational higher-tuple counts

## Finding
Let \(H_n\) be the 0-Hecke monoid of type \(A_n\), with idempotent generators \(\pi_1,\ldots,\pi_n\) and Demazure multiplication. Let \(C_{n+1}\) denote the monoid of order-preserving, order-decreasing maps on \(\{1,\ldots,n+1\}\). The natural surjective homomorphism \(\Phi_n:H_n\to C_{n+1}\) sends \(\pi_i\) to the map lowering \(i+1\) to \(i\) and fixing all other points.

**Commutation reflection theorem.** For every \(n\ge0\), the restriction of \(\Phi_n\) to idempotents is bijective and reflects, as well as preserves, commutation:
\[
 e,f\in E(H_n),\qquad ef=fe\ \Longleftrightarrow\ \Phi_n(e)\Phi_n(f)=\Phi_n(f)\Phi_n(e).
\]
For every finite pairwise-commuting family of idempotents, the quotient also preserves its entire product diagram. Consequently the idempotent commuting graphs, all their clique complexes, and the partial semilattice operations defined on commuting families are canonically isomorphic. The monoids themselves are not asserted to be isomorphic.

For \(r\ge1\), let \(t_r(n)\) count **ordered, pairwise-commuting \(r\)-tuples of idempotents** of \(H_n\), equivalently of \(C_{n+1}\). For every fixed \(r\), the ordinary generating series \(T_r(z)=\sum_{n\ge0}t_r(n)z^n\) is rational, with an explicit finite transfer construction described below. In particular, the first genuinely higher-arity case has the closed form
\[
 \boxed{T_3(z)=\frac{1-2z^2+2z^3}{1-8z+16z^2-12z^3+2z^4}.}
\]
Its coefficients for \(0\le n\le11\) are
\[
 1,\ 8,\ 46,\ 254,\ 1390,\ 7592,\ 41452,\ 226316,\ 1235620,\ 6746144,\ 36832120,\ 201093464.
\]
For comparison, the pair counts \(t_2(n)\) have the previously tabulated series \(1/(1-4z+2z^2)\); these pair counts are not claimed as new.

## Assumptions and scope
The index \(n\) counts simple Coxeter generators, so \(H_0\) and \(C_1\) are one-element monoids. Every idempotent of \(H_n\) is \(\pi_I\), the Demazure element of the longest permutation of the standard parabolic subgroup corresponding to \(I\subseteq\{1,\ldots,n\}\). Products are associative and ordered as written; function composition applies the rightmost factor first. For a subset \(I\), set
\[
 F_I=\{1\}\cup\{i+1:1\le i\le n,\ i\notin I\},\qquad e_{F_I}(j)=\max\{h\in F_I:h\le j\}.
\]
The quotient satisfies \(\Phi_n(\pi_I)=e_{F_I}\). The statements are combinatorial over integers, without a ground-field restriction. The \(r\)-tuple condition means **all pairs** commute, not merely that their total products are independent of one chosen ordering.

## Proof
**1. Two idempotent commutation criteria.** For \(I,J\subseteq\{1,\ldots,n\}\), let \(U=I\cup J\), viewed as a subset of the path graph on the Coxeter generators. Then
\[
 \boxed{\pi_I\pi_J=\pi_J\pi_I\quad\Longleftrightarrow\quad
 \text{for each connected component }B\text{ of }U,\ B\subseteq I\text{ or }B\subseteq J.}
\]
Indeed, if every component is wholly in one factor, standard parabolic absorption \(\pi_A\pi_B=\pi_B\) for \(A\subseteq B\), together with commutation between different components, gives \(\pi_I\pi_J=\pi_U=\pi_J\pi_I\). Conversely, a commuting product is idempotent and has support \(U\). The standard classification of idempotents in the 0-Hecke monoid therefore forces it to equal \(\pi_U\). Suppose that a connected component \(B=[a,b]\) of \(U\) is contained in neither \(I\) nor \(J\). Choose \(i\in B\setminus I\) and \(j\in B\setminus J\); they cannot coincide. If \(i<j\), every ordinary product \(uv\) with \(u\in W_I\), \(v\in W_J\) maps the rightmost point \(b+1\) of the interval \([a,b+1]\) to a position greater than \(i\), because \(v\) preserves the cut \(j\) and \(u\) preserves the cut \(i\). The reversal \(w_B\) instead maps \(b+1\) to \(a\le i\). If \(i>j\), the same reasoning applied to the leftmost point \(a\) shows that every \(uv\) maps \(a\) to a position at most \(i\), whereas \(w_B(a)=b+1>i\). Thus \(w_U\notin W_IW_J\). The Demazure product of parabolic longest elements is an ordinary product of elements belonging to these two parabolic subgroups (He's Bruhat-maximal-product lemma), so it cannot be \(w_U\), contradiction. The criterion follows.

For Catalan idempotents \(e_F,e_G\), put \(D=F\cap G\). A direct evaluation on consecutive common-fixed-point intervals shows that they commute exactly when, between any two consecutive elements of \(D\) and after the last such element, at least one of \(F\setminus G\) and \(G\setminus F\) has no point. Sufficiency follows because, on an interval containing exclusively fixed points of one map, the other map sends everything to the preceding common fixed point; both compositions agree. For necessity, take the first exclusive point of each color in a single common gap, say \(f<g\), with \(f\in F\setminus G\), \(g\in G\setminus F\). Then \(e_F(e_G(g))=e_F(g)>d\), while \(e_G(e_F(g))=d\), where \(d\) is the preceding common fixed point, contradicting commutation.

**2. The quotient reflects commutation and products.** Under \(I\mapsto F_I\), common fixed points correspond to the vertices absent from both \(I\) and \(J\), and their intervening integer gaps correspond precisely to connected components of \(I\cup J\). Points fixed exclusively by the two Catalan idempotents correspond to positions lying in only one of \(I,J\). Hence the two criteria in Step 1 are equivalent. Moreover every commuting pair satisfies
\[
 \pi_I\pi_J=\pi_{I\cup J},\qquad e_{F_I}e_{F_J}=e_{F_I\cap F_J}=e_{F_{I\cup J}}.
\]
Induction supplies the product statement for every pairwise-commuting finite family, and the bijection of all commuting clique configurations follows.

**3. Finite-state enumerator for arbitrary arity.** Represent an ordered \(r\)-tuple by an \(n\)-column binary word, with the \(i\)-th bit of a column indicating membership in \(I_i\). For each unordered pair \(\{i,j\}\), keep one memory value in \(\{0,i,j\}\): zero means no exclusive membership has occurred since the latest column where both bits were zero; the other values remember which side, if any, has occurred exclusively. On reading a new column, reset to zero when both bits are zero; retain the state when both are one; when exactly one is one, record that side, rejecting the column if the opposite side is already recorded. Step 1 proves that an \(n\)-column word is accepted if and only if all \(r\) idempotents commute pairwise. The starting state is all zero and every reachable state is accepting. Thus \(T_r(z)\) is obtained from a finite integer transition matrix with at most \(3^{\binom r2}\) states, proving rationality for every fixed \(r\).

**4. Exact triple formula, with finite algebraic certificate.** For \(r=3\) there are exactly thirteen states reachable from the all-zero state. Let \(M\) be their transition matrix, with entry \(M_{uv}\) equal to the number of the eight binary columns carrying state \(u\) to state \(v\), and put \(\mathbf e\) for the starting row and \(\mathbf1\) for the all-ones column. Then \(t_3(n)=\mathbf e M^n\mathbf1\). The included exact-integer checker constructs all thirteen reachable states and their transitions and verifies the first four coefficients and the thirteen identities
\[
 \mathbf e M^j(M^4-8M^3+16M^2-12M+2I)\mathbf1=0,
 \qquad 0\le j\le12.
\]
By the Cayley–Hamilton theorem for the thirteen-dimensional matrix \(M\), these identities hold for every \(j\ge0\). Consequently the coefficients satisfy the fourth-order recurrence for every \(n\ge4\), with initial values \(1,8,46,254\). Multiplication by the recurrence polynomial yields exactly the displayed rational generating function. This is an exact finite matrix certificate for the infinite identity, not inference from finitely many coefficients.

## Verification
The standalone `verify.py` uses only the Python standard library. It independently constructs Demazure products of parabolic longest permutations in \(S_{n+1}\), tests the corresponding Catalan transformations and all pairwise commutation relations for \(0\le n\le6\), and exhausts ordered commuting triples for \(0\le n\le5\). Separately it constructs the thirteen-state integer transition system and verifies the Cayley–Hamilton recurrence certificate, the first twelve triple counts, and consistency checks for other arities. Run `python3 verify.py` to obtain `VERIFY_OK`. Finite Coxeter checks are corroboration; Steps 1–3 and the finite matrix certificate establish the stated infinite claims.

## Relationship to prior work
Xuhua He [1] gives a fundamental Bruhat-product lemma for 0-Hecke multiplication and studies a **different** commutative monoid on parabolic data. Denton, Hivert, Schilling and Thiéry [2] establish the 0-Hecke idempotent classification and explain the quotient to nondecreasing parking-function monoids. Ganyushkin and Mazorchuk [3] prove that a directed type-A Hecke–Kiselman quotient is the Catalan monoid and that the relevant monoids have one idempotent for each generator subset. Those antecedents do not, as stated in the inspected passages, assert that the noninjective monoid quotient **reflects idempotent commutation**. The pairwise Catalan idempotent gap criterion and pair counts have already been studied; no novelty is claimed for the pair totals. The new assessment concerns reflection of all commuting idempotent configurations, plus the higher-arity rational construction and explicit first triple series. Denton’s 2013 study of the 0-Hecke/Catalan quotient and pattern avoidance [4] is closely related; its full original text could not be retrieved, so its possible implications remain an explicit risk. The literature search does not prove global uniqueness.

## Limitations
The reflection property concerns idempotents, not all elements of the two monoids. The explicit rational function is for ordered triples; other fixed arities have a constructive matrix formula but no uniform small-degree closed denominator. The proof does not classify maximal pairwise-commuting families. The strongest adjacent primary source on idempotents is accessible, but equivalent statements might exist elsewhere. Independent validation has not been performed.

## References
[1] Xuhua He, *A Subalgebra of 0-Hecke Algebra*, arXiv:0904.1786v1 (11 April 2009), particularly §1 and Lemma 1.

[2] T. Denton, F. Hivert, A. Schilling, N. M. Thiéry, *On the Representation Theory of Finite \(\mathcal J\)-Trivial Monoids*, arXiv:1010.3455 (2010), §§2.4–2.5 and §3.6.

[3] O. Ganyushkin and V. Mazorchuk, *On Kiselman Quotients of 0-Hecke Monoids*, arXiv:1006.0316 (2010), Theorem 1 and §2.

[4] T. Denton, *Algebraic and Affine Pattern Avoidance*, arXiv:1303.3767 (2013), abstract inspected; full text not obtained.
