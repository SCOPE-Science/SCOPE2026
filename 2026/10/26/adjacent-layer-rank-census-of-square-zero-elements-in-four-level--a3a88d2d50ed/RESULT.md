# Adjacent-layer rank census of square-zero elements in four-level incidence radicals

## Finding
Let \(P=P_1\oplus P_2\oplus P_3\oplus P_4\) be the ordinal sum of four nonempty antichains, whose respective cardinalities are \(a,b,c,d\). Let \(J\) be the Jacobson radical of its incidence algebra over the finite field \(\mathbb F_q\), where \(q\) is any prime power. In the natural linear representation on the ordered basis of \(P\), every \(N\in J\) is uniquely
\[
N=\begin{pmatrix}
0&A&D&F\\
0&0&B&E\\
0&0&0&C\\
0&0&0&0
\end{pmatrix},
\]
where the adjacent blocks have sizes \(A:a\times b\), \(B:b\times c\), and \(C:c\times d\). Define the **joint adjacent-layer rank polynomial**
\[
\Phi_{a,b,c,d;q}(U,V,W)=\sum_{\substack{N\in J\\N^2=0}}
U^{\operatorname{rank}A}V^{\operatorname{rank}B}W^{\operatorname{rank}C}.
\]
For nonnegative integers \(m,n\), define the number of rank-\(j\) matrices
\[
R_q(m,n,j)={m\brack j}_q\prod_{i=0}^{j-1}(q^n-q^i),
\]
with \(R_q(m,n,j)=0\) outside \(0\le j\le\min(m,n)\) and the usual empty-product convention. Here \({m\brack j}_q\) is the Gaussian binomial coefficient. Then, for every \(a,b,c,d\ge1\) and every prime power \(q\),
\[
\boxed{\Phi_{a,b,c,d;q}(U,V,W)=
\sum_{t=0}^{\min(b,c)}
\sum_{r=0}^{\min(a,b-t)}
\sum_{s=0}^{\min(c-t,d)}
R_q(b,c,t)R_q(a,b-t,r)R_q(c-t,d,s)
q^{ad+ac+bd-as-rd+rs}U^rV^tW^s.}
\]
This is a joint distribution, not merely the total number of square-zero matrices or the distribution of their ambient Jordan types. Every coefficient is a nonnegative integer and counts exactly those radical elements with the prescribed ranks on the three adjacent layers.

## Assumptions and scope
The incidence algebra of the ordinal sum is isomorphic to the algebra of block upper-triangular matrices having arbitrary diagonal entries within each diagonal block only along its scalar coordinate idempotents, and arbitrary rectangular strictly upper blocks. Its radical consists of the displayed strictly upper block matrices. Matrix ranks are over \(\mathbb F_q\), and all elements are counted separately, not modulo conjugacy. The three adjacent ranks are invariant under the natural action by block-diagonal invertible changes of basis. No restriction on the characteristic is needed. The theorem does not classify conjugacy orbits and does not claim that adjacent ranks determine the ambient Jordan partition.

## Proof
Direct block multiplication yields exactly the three conditions
\[
N^2=0\quad\Longleftrightarrow\quad AB=0,\qquad BC=0,\qquad AE+DC=0.
\]
The outermost block \(F\in M_{a,d}(\mathbb F_q)\) is entirely free, contributing \(q^{ad}\).

Fix \(t\), the rank of \(B\). There are \(R_q(b,c,t)\) possibilities for \(B\). For each, \(AB=0\) means that \(A:\mathbb F_q^b\to\mathbb F_q^a\) vanishes on \(\operatorname{im}B\) and hence factors through a quotient of dimension \(b-t\). Exactly \(R_q(a,b-t,r)\) of the possible \(A\) have rank \(r\). Likewise \(BC=0\) means that \(C:\mathbb F_q^d\to\mathbb F_q^c\) has image inside \(\ker B\), a space of dimension \(c-t\), so exactly \(R_q(c-t,d,s)\) choices have rank \(s\).

For fixed \(A,B,C\) of these ranks, define the linear map
\[
\mathcal L:M_{b,d}(\mathbb F_q)\oplus M_{a,c}(\mathbb F_q)\longrightarrow M_{a,d}(\mathbb F_q),
\qquad (E,D)\longmapsto AE+DC.
\]
The image of \(E\mapsto AE\) consists of maps whose images lie inside \(\operatorname{im}A\), of dimension \(rd\). The image of \(D\mapsto DC\) consists of maps vanishing on \(\ker C\), of dimension \(as\). Their intersection is the space of maps that both vanish on \(\ker C\) and take values in \(\operatorname{im}A\), of dimension \(rs\). Consequently
\[
\operatorname{rank}\mathcal L=rd+as-rs,
\qquad
\dim\ker\mathcal L=bd+ac-rd-as+rs.
\]
Thus \(AE+DC=0\) admits exactly \(q^{bd+ac-rd-as+rs}\) pairs \((D,E)\). Multiplying by the free-\(F\) factor, the fixed-\((r,t,s)\) choices of \(A,B,C\), and summing over all admissible ranks proves the boxed formula. The argument is valid in every finite characteristic because it uses only linear subspaces, dimensions, and rank counts.

The smallest four-level instance \(a=b=c=d=1\) gives the explicit polynomial
\[
\Phi_{1,1,1,1;q}=q^3(1+(q-1)V)
+q^2(q-1)(U+W)+q^2(q-1)^2UW.
\]
This identity exhibits a rank-profile statistic that is finer than the univariate number of square-zero elements.

## Verification
The included standalone file `check_square_zero.py`, runnable with `python3 check_square_zero.py` using only the Python standard library, independently enumerates all radical elements for eleven dimension/field configurations. For each, it computes \(N^2\) through the three rectangular products, then computes the three matrix ranks by Gaussian elimination, and checks **every coefficient** against the formula. Tested field orders include \(2,3,4,5,7\), with the order-four field represented as \(\mathbb F_2[z]/(z^2+z+1)\). The checker additionally tests 196 finite-field rank-count identities. The recorded final output is `ALL_FOUR_LAYER_SQUARE_ZERO_CHECKS_PASSED 11 and 196 rank-count identities`. All these are finite corroborations; the proof above establishes the arbitrary-size statement.

## Relationship to prior work
Yip's work on rook placements and upper-triangular Jordan forms (2017), Fuchs--Kirillov's work on Jordan types of triangular matrices (2022), and Karp--Thomas's treatment of Jordan-form-tableau counts in parabolic nilradicals (2022, Theorem 5.13) provide extensive **pre-existing** Jordan-type counting theory. Bardestani--Mallahi-Karai--Ram--Salmasian (2025, Theorem 2.5) count square-zero matrices of each **ambient matrix rank** in general parabolic nilradicals; this already covers totals and ambient Jordan distributions for the four-block family. None of those results is claimed as new here.

The present invariant records the ranks of the **three specified adjacent blocks jointly**. Its coefficients cannot be obtained simply by reading off the ambient Jordan type, nor by reading off the Jordan types on the cumulative four-level flag. For example, take level sizes \((1,2,1,1)\). Let \(N_1\) have its sole nonzero entry in block \(C\), and let \(N_2\) have its sole nonzero entry in block \(E\), with all other blocks zero. Both have square zero and precisely one Jordan block of size two. Their ranks on every cumulative prefix space in the natural four-level flag agree: \((0,0,0,1)\), whereas their adjacent rank profiles are, respectively, \((0,0,1)\) and \((0,0,0)\). Thus the rank-profile census is not a relabeling of either Jordan-type or prefix-Jordan-tableau counts. General incidence-algebra polynomial-identity counts, such as Gargate--Gargate, likewise concern a different statistic.

## Limitations
This is an exact formula for four levels and ranks of their three immediate connecting blocks, not a classification of all square-zero orbits, all possible block-refined invariants, or analogous recurrences for arbitrarily many levels. The novelty comparison distinguishes the **joint adjacent-layer polynomial** from established Jordan-type and total square-zero formulas, but an equivalent rank-refined formula could exist in specialist literature outside the inspected texts. Computations do not certify the general proof; the preceding linear-map argument does. No independent mathematical review has been performed.

## References
- C. Yip, *Rook placements and Jordan forms of upper-triangular nilpotent matrices*, arXiv:1703.00057 (first publicly available 2017-02-28), https://arxiv.org/abs/1703.00057.
- J. Fuchs and A. Kirillov, *Jordan types of triangular matrices over a finite field*, arXiv:2204.00066 (2022), https://arxiv.org/abs/2204.00066.
- S. Karp and H. Thomas, *q-Whittaker functions, finite fields, and Jordan forms*, arXiv:2207.12590 (2022), especially Theorem 5.13, https://arxiv.org/abs/2207.12590.
- M. Bardestani, K. Mallahi-Karai, C. Ram, and H. Salmasian, *Counting \(\mathbb F_q\)-points of orbital varieties in ad-nilpotent ideals of type \(A_n\)*, arXiv:2503.15440 (2025), especially Theorem 2.5, https://arxiv.org/abs/2503.15440.
- P. Gargate and S. Gargate, *(k+1)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243 (2020), https://arxiv.org/abs/2009.04243.
