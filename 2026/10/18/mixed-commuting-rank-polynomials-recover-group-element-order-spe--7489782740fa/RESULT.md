# Mixed commuting-rank polynomials recover group element-order spectra

## Finding

Let \(G\) be an arbitrary finite group of order \(N\geq 1\). For each integer \(m\geq1\), let \(X_m=G\times\{1,\ldots,m\}\), with \(G\) acting by left multiplication in every copy, and let \(M_m(G)\) be the inverse monoid consisting of all restrictions of those permutations, including the empty map. Its idempotents are \(e_S=\operatorname{id}_S\), for all \(S\subseteq X_m\). Write \(a_d(G)=|\{g\in G:\operatorname{ord}(g)=d\}|\) for each positive divisor \(d\mid N\), and put

\[
K(u,v)=\begin{pmatrix}1+v&u\\1&u(1+v)\end{pmatrix}.
\]

**Theorem.** The joint-rank polynomial of commuting idempotent--element pairs, with the idempotent's rank marked by \(u\) and the other element's rank by \(v\), satisfies, for every \(m\geq1\),

\[
\boxed{F_m(G;u,v)=\sum_{d\mid N}a_d(G)\left[\operatorname{tr}(K(u,v)^d)\right]^{mN/d}-(N-1)(1+u)^{mN}.}
\]

In particular, with \(C_m(G)=F_m(G;1,1)\),

\[
\boxed{C_m(G)=\sum_{d\mid N}a_d(G)(3^d+1)^{mN/d}-(N-1)2^{mN}.}
\]

For fixed \(N\), the \(\tau(N)\) integers \(C_1(G),\ldots,C_{\tau(N)}(G)\) uniquely determine *every* \(a_d(G)\). Conversely, groups of the same order and with the same element-order distribution have identical joint-rank polynomials for all \(m\). This is a precise equivalence between the mixed commuting profile and the element-order distribution, not a claim that this profile determines a finite group up to isomorphism.

For \(N>1\), let \(p\) be the least prime dividing \(N\). If \(\delta_m(G)\) is the probability that a uniformly chosen idempotent and an independently uniformly chosen element of \(M_m(G)\) commute, then

\[
\delta_m(G)=\frac1N+\frac{a_p(G)}N\left(\frac{(3^p+1)^{1/p}}4\right)^{mN}+o\!\left(\left(\frac{(3^p+1)^{1/p}}4\right)^{mN}\right)
\quad(m\to\infty).
\]

The case \(G\cong C_4\) has \(C_1(G)=472\), whereas \(G\cong C_2\times C_2\) has \(C_1(G)=508\), although both restriction monoids have \(61\) elements and \(16\) idempotents. For cyclic \(G\cong C_N\), the unrefined formula reads

\[
C_m(C_N)=\sum_{d\mid N}\varphi(d)(3^d+1)^{mN/d}-(N-1)2^{mN}.
\]

## Assumptions and scope

Composition is ordinary composition of partial maps. An element \(\alpha\in M_m(G)\) has rank \(|\operatorname{dom}\alpha|\), equal to its image size. A free action is essential: because left multiplication fixes no point for a nonidentity group element, every *nonempty* restriction \(g|_T\) has a unique group extension. Consequently

\[
|M_m(G)|=N(2^{mN}-1)+1,\qquad |E(M_m(G))|=2^{mN}.
\]

The polynomial includes zero, both idempotents and non-idempotents, and ordered pairs \((e,\alpha)\) with the first entry idempotent. It is *not* the full commuting-pair polynomial on \(M_m(G)^2\). The specialization at \(u=v=1\) is a genuine count rather than a normalized probability.

## Proof

**1. Unique extensions and the commutation condition.** Fix \(S,T\subseteq X_m\), \(g\in G\), and let \(e=e_S\), \(\alpha=g|_T\). On input \(x\), the composition \(e\circ\alpha\) is defined exactly when \(x\in T\) and \(gx\in S\); the composition \(\alpha\circ e\) is defined exactly when \(x\in T\cap S\). Where they are defined, both take the value \(gx\). Thus they commute if and only if

\[
\forall x\in T:\quad\mathbf1_S(gx)=\mathbf1_S(x).
\]

For fixed \(g,S\), each point with equal endpoint indicators may be independently included or excluded from \(T\), contributing \(1+v\), while other points must be omitted. A chosen \(S\) contributes \(u^{|S|}\).

**2. Transfer around a permutation cycle.** Write \(s_x=\mathbf1_S(x)\). On any directed cycle of \(g\) of length \(d\), the weighted sum over binary assignments \((s_1,\ldots,s_d)\) is

\[
\sum_{s_1,\ldots,s_d\in\{0,1\}}
\prod_{i=1}^{d}u^{s_{i+1}}(1+v)^{\mathbf1_{\{s_i=s_{i+1}\}}}
=\operatorname{tr}(K(u,v)^d),\qquad s_{d+1}=s_1.
\]

The displayed matrix has row index \(s_i\), column index \(s_{i+1}\): its entry is \(u^{s_{i+1}}(1+v)\) for equal indices and \(u^{s_{i+1}}\) otherwise. Therefore both weights and periodic closure are exact, including cycles of length one.

**3. Free orbit cycle structure and the zero correction.** For an element \(g\) of order \(d\), the permutation \(x\mapsto gx\) on \(X_m\) consists of exactly \(mN/d\) cycles of length \(d\). Thus its complete contribution to the sum over \((S,T)\) is \(\operatorname{tr}(K(u,v)^d)^{mN/d}\). Different \(g\)'s yield different nonempty partial transformations, but all \(N\) choices \(g|_\varnothing\) represent the same empty map. Its contribution, summed over \(S\), is exactly \((1+u)^{mN}\). Subtracting \(N-1\) extra empty-map representations gives the theorem's first formula. No other duplications are possible by freeness.

**4. Unrefined count and spectral reconstruction.** At \(u=v=1\), the transfer matrix is \(\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\) and has eigenvalues \(3,1\). Its \(d\)-th power has trace \(3^d+1\). Set \(b_d=(3^d+1)^{N/d}\). Then

\[
C_m(G)+(N-1)2^{mN}=\sum_{d\mid N}a_d(G)b_d^m.
\]

For real \(t>0\), the function \(t\mapsto (3^t+1)^{1/t}\) is strictly decreasing: indeed its logarithm equals \(\log3+t^{-1}\log(1+3^{-t})\), and the second term has strictly negative derivative. Consequently the \(b_d\) are positive and pairwise distinct. If \(d_1,\ldots,d_r\) list the positive divisors of \(N\), with \(r=\tau(N)\), the coefficient matrix \((b_{d_j}^{m})_{1\le m,j\le r}\) has determinant

\[
\left(\prod_{j=1}^{r}b_{d_j}\right)\prod_{1\le i<j\le r}(b_{d_j}-b_{d_i})\ne0.
\]

Hence the first \(r\) unrefined counts recover the vector \((a_{d_j})\) uniquely; equality of order distributions makes the entire refined formula identical.

**5. Asymptotic.** For \(N>1\), Cauchy's theorem ensures \(a_p(G)>0\), where \(p\) is the least prime divisor of \(N\). Every nonidentity element has order at least \(p\). The strict decrease just proved implies that \(b_p\) is the unique largest base among the nonidentity orders, and \(2^N<b_p<4^N\). Hence

\[
C_m(G)=4^{mN}+a_p(G)b_p^m+o(b_p^m).
\]

Dividing by \(2^{mN}[N(2^{mN}-1)+1]=N4^{mN}-(N-1)2^{mN}\), whose lower-order correction is negligible compared with \(b_p^m\), proves the stated probability asymptotic. For \(N=1\), the monoid is a semilattice and the probability is identically one.

## Verification

The accompanying independent enumeration code, `checker.py`, builds partial functions explicitly from multiplication tables and checks commutativity using both composition orders. It separately expands the transfer-cycle polynomial, compares all rank coefficients, and tests the unrefined order formula. Verified cases include \(C_1\), \(C_2\) with one through three regular orbits, \(C_3\) with one and two orbits, \(C_4\), \(C_2\times C_2\), \(S_3\), and the dihedral group of order eight. The largest direct comparison examines the \(2{,}041\) elements of the dihedral restriction monoid against all \(256\) idempotents. Exact rational Vandermonde reconstruction is additionally checked for the indicated finite groups. Run `python checker.py` using Python 3 with no third-party packages.

These finite tests corroborate the formula and independent small-case implementation. The arbitrary-group and all-parameter statements are proved by the preceding structural and transfer-matrix arguments, not by finite enumeration.

## Relationship to prior work

Fernandes, *On the cyclic inverse monoid on a finite set*, first posted on arXiv on 3 November 2022, develops the cyclic case \(\mathcal{CI}_N\), proves its size and generator rank, and gives monoid presentations. In particular, the regular action and unique-extension lemma provide the natural point of departure. The inspected full text does not enumerate mixed commuting pairs, their joint ranks, or their reconstruction properties. The present result applies to every finite group and arbitrary numbers of free orbits, with the cyclic result as a specialization.

Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup* (2020), investigates centralizers in the ambient full symmetric inverse semigroup and their Green structure. Its accessible abstract does not state the free-group-restriction transfer formula or element-order recovery, but the full text was not accessible; related general centralizer criteria might simplify part of the first step. Earlier work of Konieczny (2013) characterizes commuting partial injections in the full symmetric inverse semigroup, a broader ambient *structural* setting, not the same rank enumeration over free group-restriction monoids. The present proof independently verifies every reduction it uses, and no uninspected paper is asserted not to contain an equivalent result.

## Limitations

The inverse monoid's unit group is already isomorphic to \(G\); reconstruction of element-order multiplicities from the *single mixed commuting statistic across copy numbers* is an invariant-theoretic statement, not a new method for reconstructing \(G\) from an unknown complete monoid. Groups with identical order distributions are not distinguished by any of the displayed polynomials. The free-action assumption is essential to the unique-extension correction and does not extend without modification to permutation groups with nontrivial point stabilizers. No full commuting-pair enumeration is asserted. A potentially overlapping general centralizer treatment remains a bibliographic risk; no claim of exhaustive priority is made.

## References

1. V. H. Fernandes, *On the cyclic inverse monoid on a finite set*, arXiv:2211.02155v1 (publicly posted 2022-11-03), https://arxiv.org/html/2211.02155v1 .
2. J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, Communications in Algebra **48** (2020), 5181--5194, https://doi.org/10.1080/00927872.2020.1782926 .
3. J. Konieczny, *Centralisers in the infinite symmetric inverse semigroup*, Bulletin of the Australian Mathematical Society **87** (2013), 462--479, https://doi.org/10.1017/S0004972712000779 .
