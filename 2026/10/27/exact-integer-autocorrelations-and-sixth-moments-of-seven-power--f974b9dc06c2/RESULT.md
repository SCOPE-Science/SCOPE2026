# Exact integer autocorrelations and sixth moments of seven-power very odd sequences

## Finding
Let \(k\ge1\) and \(N_k=(7^k+1)/2\). A binary word \(a=(a_0,\ldots,a_{N_k-1})\) is *very odd* when every integer aperiodic autocorrelation
\[
C_a(t)=\sum_{i=0}^{N_k-1-t}a_i a_{i+t}\qquad(0\le t<N_k)
\]
is odd. There are exactly \(2^k\) such words. **All of them have the same entire integer autocorrelation function**, not merely the same parity profile: if \(t\) has the unique balanced base-seven expansion
\[
t=\sum_{j=0}^{k-1}\delta_j7^j,\qquad \delta_j\in\{-3,-2,-1,0,1,2,3\},
\]
and \(z_k(t)=\#\{j:\delta_j=0\}\), then
\[
\boxed{C_a(t)=3^{z_k(t)}\quad(0\le t<N_k).}
\]
In particular, \(C_a(0)=3^k\), and for every \(0\le j<k\) exactly
\[
\boxed{\frac12\binom{k}{j}6^{k-j}}
\]
of the positive shifts have autocorrelation \(3^j\). Hence all \(2^k\) distinct supports are homometric (have identical signed difference multisets), and precisely \(2^{k-1}\) remain distinct up to translation and reflection. If \(T_k\) is uniform on \(\{1,\ldots,N_k-1\}\), then \(\log_3 C_a(T_k)\) is binomial \(\operatorname{Bin}(k,1/7)\) conditioned to be less than \(k\), and
\[
\frac{\log_3 C_a(T_k)-k/7}{\sqrt{6k/49}}\ \Longrightarrow\ \mathcal N(0,1).
\]
The common Fourier magnitude also has an **exact sixth-moment law**: for any associated support polynomial \(B_k(X)=\sum_i a_iX^i\), set
\[
M_k=\frac1{2\pi}\int_0^{2\pi}|B_k(e^{i\theta})|^6\,d\theta.
\]
Then \(M_0=1\), \(M_1=99\), and for every \(k\ge0\),
\[
\boxed{M_{k+2}=118M_{k+1}-873M_k,\qquad
\sum_{k\ge0}M_kz^k=\frac{1-19z}{1-118z+873z^2}.}
\]
Consequently \(M_k\sim(\tfrac12+5/\sqrt{163})(59+4\sqrt{163})^k\).

## Assumptions and scope
All words are finite and binary; autocorrelations are **ordinary integers**, not residues or periodic correlations. The parameter \(k\) ranges over every positive integer. Shifts are exactly \(0\le t\le(7^k-1)/2\). A signed-difference multiset counts ordered differences \(v-u\) of support positions; its positive differences are the displayed autocorrelations. No assertion about arbitrary very odd lengths is made.

## Proof
1. Set \(F(X)=1+X+X^3\) and \(G(X)=1+X^2+X^3\). Both are irreducible over \(\mathbb F_2\), reciprocal to each other, and
\[
F(X)G(X)=1+X+\cdots+X^6\quad\text{in }\mathbb F_2[X].
\]
For \(j\ge0\), the cyclotomic polynomial \(\Phi_{7^{j+1}}(X)\) splits into exactly two irreducible reciprocal factors \(F(X^{7^j})\) and \(G(X^{7^j})\). Indeed \(\operatorname{ord}_{7^{j+1}}(2)=3\cdot7^j\): \(2^3=1+7\), and lifting the exponent shows \(\nu_7(2^{3\cdot7^j}-1)=j+1\). Each displayed factor has degree \(3\cdot7^j\) and contains a primitive \(7^{j+1}\)-th root, so it is irreducible.

2. Because \(C_a(N_k-1)=a_0a_{N_k-1}\) must be odd, both endpoint bits are one. Thus for a very odd word its support polynomial \(B(X)\) has constant term one and degree \(N_k-1\). The very-odd condition is equivalent to
\[
B(X)B^*(X)=\frac{X^{7^k}+1}{X+1}\quad\text{over }\mathbb F_2[X],
\]
where \(B^*(X)=X^{N_k-1}B(X^{-1})\). This follows by reading the coefficients of \(B B^*\), which are precisely the autocorrelations modulo two. The cyclotomic factorization of the right-hand side and unique factorization force \(B\) to select exactly one member from each reciprocal pair \(F(X^{7^j}),G(X^{7^j})\). Conversely every such selection satisfies the identity. These \(2^k\) products have only coefficients zero or one over the integers, because every exponent has a unique representation in base seven with digits chosen independently from \(\{0,1,3\}\) or \(\{0,2,3\}\). Each digit-choice vector gives a different support, detected by projection onto its individual digit coordinate.

3. For either one-digit set \(D=\{0,1,3\}\) or \(D=\{0,2,3\}\), the number of ordered pairs \((u,v)\in D^2\) with difference \(v-u\) is \(3\) for difference zero and exactly \(1\) for each difference \(\pm1,\pm2,\pm3\). A difference of two full support positions therefore has a representation \(\sum_j(v_j-u_j)7^j\) with every digit difference in \([-3,3]\). Such balanced representations are unique: reduction modulo seven determines the bottom digit, and division by seven inductively determines all others. Consequently, the number of pairs realizing shift \(t\) is exactly \(\prod_j(3\text{ if }\delta_j=0\text{ else }1)=3^{z_k(t)}\). This also proves the integer autocorrelation is independent of every factor selection.

4. All \(7^k\) balanced digit vectors give distinct integers in \([-(7^k-1)/2,(7^k-1)/2]\). Exactly \(\binom{k}{j}6^{k-j}\) have \(j\) zero digits. For \(j<k\), negating all digits pairs positive with negative shifts without fixed points, giving half that many positive shifts. The sole all-zero vector represents \(t=0\), proving the histogram. Under a uniform positive shift, this is a \(\operatorname{Bin}(k,1/7)\) law conditioned away from its all-zero-digit outcome, whose probability is \(7^{-k}\); the classical binomial central limit theorem proves the asserted limit.

5. Put \(P(X)=3+\sum_{d=1}^3(X^d+X^{-d})\). Both one-digit factors satisfy \(F(X)F(X^{-1})=G(X)G(X^{-1})=P(X)\) over the integers, so every full support polynomial has \(|B_k(e^{i\theta})|^2=\prod_{j=0}^{k-1}P(e^{i7^j\theta})\). The sixth moment is the constant coefficient of \(\prod_{j=0}^{k-1}Q(X^{7^j})\), where \(Q=P^3\). The coefficients \(q_d=[X^d]Q\) for \(d=0,1,\ldots,9\) are respectively \(99,84,75,64,39,27,16,6,3,1\), with \(q_{-d}=q_d\) and other coefficients zero. A zero exponent in a product term is equivalent to a sequence of carries \(c_0=c_k=0\) and \(c_{j+1}=(c_j+d_j)/7\) with \(d_j\in[-9,9]\). All intermediate carries belong to \(\{-1,0,1\}\). The exact transfer matrix, ordered by carry \(-1,0,1\), is
\[
T=\begin{pmatrix}16&84&3\\6&99&6\\3&84&16\end{pmatrix},\qquad M_k=(T^k)_{0,0},
\]
where the subscript zero denotes the central carry state. On symmetric states, this is equivalent to \(\binom{u_{j+1}}{v_{j+1}}=\begin{pmatrix}19&6\\168&99\end{pmatrix}\binom{u_j}{v_j}\), initialized at \(u_0=0,v_0=1\), with \(M_j=v_j\). The characteristic polynomial is \(x^2-118x+873\), giving the sixth-moment recurrence and generating function. The eigenvalues are \(59\pm4\sqrt{163}\), and solving the initial conditions gives the displayed asymptotic (indeed an exact two-eigenvalue formula). This transfer is an infinite-depth identity, not a finite fitted recurrence.

6. Every support contains both endpoints \(0\) and \(N_k-1\), so a translation preserving the span of the finite support must be trivial. Reflection \(x\mapsto N_k-1-x\) exchanges the two digit sets at all \(k\) levels and hence complements every factor choice. No choice vector is fixed by full complementation for \(k\ge1\), giving \(2^{k-1}\) classes up to translation/reflection.

## Verification
The standalone `verify.py` enumerates all \(2^k\) digit-selection vectors for each \(1\le k\le5\), constructs supports as sets of integers, calculates all integer autocorrelations independently by pair enumeration, checks the closed formula and histogram for every shift, checks modular orders, and counts the reflection classes. It also computes selected sixth moments independently as sums of squares of coefficients of \(B_k(X)^3\), against the recurrence. It reports `VERIFY_OK`. This finite experiment is a consistency test only; the cyclotomic and balanced-radix arguments above prove the unbounded claim.

## Relationship to prior work
Moree and Solé (2004, first arXiv version) give the binary reciprocal-factor identity, an injective block-product construction, and the general formula for the *number* of very odd sequences. Those facts supply the factorization starting point here, but do not state or evaluate the **integer** autocorrelation at every shift, its complete distribution, or the resulting homometry classification. Ku and Wong (2015) characterize prescribed autocorrelation *congruences*, a different level of information: a residue class does not give the exact counts. OEIS A053006 records admissible lengths, not the present correlation invariant. The extensive known theory of homometric sets and factor switching is a background mechanism rather than a claim of a newly invented mechanism. These results are a quantitative extraction from established structural tools, not an independent new characterization of which lengths admit very odd words.

## Limitations
The sixth-moment statement is an exact Fourier energy for these supports, not a claim about optimality among general sets. The formulas are restricted to lengths \((7^k+1)/2\). The homometric ambiguity is specifically within the very-odd family; no uniqueness or maximality claim for arbitrary subsets is made. The derivation uses known factorization/count ideas, and a stronger statement in earlier specialized literature remains a priority risk: the full text of Inglis--Wiseman (1995) was not accessible in this review. Independent mathematical validation has not been carried out.

## References
- P. Moree and P. Solé, *Around Pelikán's conjecture on very odd sequences*, arXiv:math/0407084, first submitted 2004-07-06; see the construction in Lemma 3 and factor-count formula in Proposition 2. https://arxiv.org/html/math/0407084v2
- C. Y. Ku and K. B. Wong, *A Generalization of Very Odd Sequences*, Electronic Journal of Combinatorics 22(2) (2015), P2.12, doi:10.37236/5075. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p12/pdf/
- N. F. J. Inglis and J. D. A. Wiseman, *Very odd sequences*, Journal of Combinatorial Theory A 71 (1995), 89--96, doi:10.1016/0097-3165(95)90017-9 (bibliographic record and abstract consulted; full text unavailable).
- OEIS A053006, very odd sequence lengths. https://oeis.org/A053006
