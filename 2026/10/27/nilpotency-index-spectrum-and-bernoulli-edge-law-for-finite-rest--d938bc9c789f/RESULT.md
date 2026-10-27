# Nilpotency-index spectrum and Bernoulli edge law for finite restricted-range endomorphisms

## Finding
Let \(q\) be any prime power. Fix integers \(k,c\ge1\), a \((k+c)\)-dimensional vector space \(V\) over \(\mathbb F_q\), and a fixed \(k\)-dimensional subspace \(W\). Consider the finite semigroup
\[
S(V,W)=\{X\in\operatorname{End}_{\mathbb F_q}(V):X(V)\subseteq W\}.
\]
For a nilpotent \(X\), its index \(\nu(X)\) is the least positive integer \(j\) with \(X^j=0\); in particular \(\nu(0)=1\). Let \(F_{k,c,q}(z)=\sum_{X\in S(V,W),\ X\text{ nilpotent}}z^{\nu(X)}\).

For a partition \(\lambda\vdash k\), write \(\lambda'\) for its conjugate, \(m_j(\lambda)\) for the multiplicity of \(j\), \(d=\lambda_1\), and \(r=m_d(\lambda)\). Put
\[
C_\lambda(q)=q^{\sum_{i\ge1}(\lambda'_i)^2}
\prod_{j\ge1}\prod_{a=1}^{m_j(\lambda)}(1-q^{-a}),
\qquad N_\lambda(q)=\frac{|\operatorname{GL}_k(\mathbb F_q)|}{C_\lambda(q)}.
\]
Then the **complete nilpotency-index enumerator**, including nonregular semigroup elements, is
\[
\boxed{F_{k,c,q}(z)=\sum_{\lambda\vdash k}N_\lambda(q)
\left[q^{(k-r)c}z^d+
\big(q^{kc}-q^{(k-r)c}\big)z^{d+1}\right].}
\]
In particular there are exactly \(q^{k(k+c-1)}\) nilpotent elements, no index exceeds \(k+1\), and the number of elements of maximal index \(k+1\) is
\[
\boxed{q^{k(k+c-1)}(1-q^{-c})\prod_{j=2}^{k}(1-q^{-j}).}
\]
The empty product is one.

There is also a uniform **top-edge law**. Choose \(X\) uniformly among all nilpotent elements and set \(D_{k,c}=k+1-\nu(X)\). Write \(\varphi_s(q)=\prod_{j=1}^s(1-q^{-j})\) (with \(\varphi_0(q)=1\)) and \(K_{q,k}=\prod_{j=2}^k(1-q^{-j})\). For every integer \(s\ge0\) with \(2s<k\), exactly
\[
\boxed{\Pr(D_{k,c}=s)=K_{q,k}\left[
(1-q^{-c})\frac{q^{-2s}}{\varphi_s(q)}+
\mathbf1_{s\ge1}\,q^{-c}\frac{q^{-2(s-1)}}{\varphi_{s-1}(q)}\right].}
\]
For fixed \(q\) and \(c\), as \(k\to\infty\), \(D_{k,c}\) converges in **total variation** to \(S_q+E_c\), with independent summands defined by
\[
\Pr(S_q=s)=K_q\frac{q^{-2s}}{\varphi_s(q)},\quad
K_q=\prod_{j=2}^{\infty}(1-q^{-j}),\quad
\Pr(E_c=1)=q^{-c},\quad \Pr(E_c=0)=1-q^{-c}.
\]
If \(c=c(k)\to\infty\), then \(D_{k,c(k)}\) converges in total variation to \(S_q\). Hence a growing codimension makes a typical nilpotent nonregular while still keeping its nilpotency index within a tight random distance of the algebraic maximum.

## Assumptions and scope
All linear maps, dimensions, ranks and Jordan partitions are over \(\mathbb F_q\); arbitrary prime powers and all characteristics are admitted. Both \(k\) and \(c\) are positive. The probability refers to uniform sampling from the nilpotent subset of \(S(V,W)\), not from all endomorphisms or from the regular subsemigroup. No ambient nilpotent Jordan-type classification is asserted: the invariant classified is the nilpotency **index**. The exact edge formula is asserted only when \(2s<k\); the full finite distribution for every index comes from the partition sum.

## Proof
Choose a vector-space complement \(U\) to \(W\) in \(V\), and use \(V=W\oplus U\). Every \(X\in S(V,W)\) has unique block form
\[
X=\begin{pmatrix}A&B\\0&0\end{pmatrix},
\quad A\in M_k(\mathbb F_q),\quad B\in M_{k\times c}(\mathbb F_q).
\]
The restriction of \(X\) to \(W\) is \(A\), while the induced map on \(V/W\) is zero. Thus \(X\) is nilpotent if and only if \(A\) is nilpotent. Direct multiplication gives, for all \(j\ge1\),
\[
X^j=\begin{pmatrix}A^j&A^{j-1}B\\0&0\end{pmatrix}.
\]
Suppose \(A\) has Jordan partition \(\lambda\), maximal block length \(d=\lambda_1\), and \(r=m_d(\lambda)\) longest blocks. Then \(A^d=0\), \(A^{d-1}\) has rank exactly \(r\), and \(X^{d+1}=0\). The index is \(d\) precisely when all \(c\) columns of \(B\) lie in \(\ker A^{d-1}\), and is otherwise \(d+1\). The kernel has dimension \(k-r\). Therefore exactly \(q^{(k-r)c}\) choices of \(B\) yield index \(d\), and the remaining \(q^{kc}-q^{(k-r)c}\) choices yield index \(d+1\). This includes the zero-matrix case \(d=1\). The regularity criterion for the restricted-range semigroup is \(X(V)\subseteq X(W)\), equivalent here to \(\operatorname{im}B\subseteq\operatorname{im}A\). Conditional on \(A\), this has probability \(q^{-c(k-\operatorname{rank}A)}\). As a nilpotent \(A\) has rank at most \(k-1\), the total regular-nilpotent proportion is at most \(q^{-c}\). Thus it tends to zero when \(c\to\infty\), even though the maximum-index probability tends to a positive constant.

To count \(A\) of each type, regard its nilpotent Jordan module as \(\bigoplus_{j\ge1}(\mathbb F_q[t]/t^j)^{m_j(\lambda)}\). The endomorphism algebra of this module has dimension \(\sum_i(\lambda'_i)^2\), and its semisimple quotient is \(\prod_j M_{m_j(\lambda)}(\mathbb F_q)\). Its units, the centralizer of \(A\) in \(\operatorname{GL}_k(\mathbb F_q)\), consequently have cardinality \(C_\lambda(q)\). Orbit-stabilizer gives precisely \(N_\lambda(q)\). Summing the two conditional counts over nilpotent partitions proves the displayed polynomial.

The classical finite-field nilpotent-matrix count is \(q^{k^2-k}\): equivalently, summing the standard nilpotent conjugacy-class sizes gives \(\sum_{\lambda\vdash k}N_\lambda(q)=q^{k^2-k}\). This identity is also immediate from the usual nilpotent cycle-index coefficient \(\sum_{\lambda\vdash k}C_\lambda(q)^{-1}=q^{-k}/\varphi_k(q)\) and \(|\operatorname{GL}_k(\mathbb F_q)|=q^{k^2}\varphi_k(q)\). Multiplying by the \(q^{kc}\) unconstrained choices of \(B\) yields the total. Index \(k+1\) requires \(\lambda=(k)\) and \(A^{k-1}B\ne0\). The fraction of all nilpotent \(A\) with partition \((k)\) is \(K_{q,k}\), and for each such \(A\), the nonvanishing probability is \(1-q^{-c}\). This proves the maximal-index count and its positive probability.

For the exact edge law, fix \(s\) with \(2s<k\). Any partition \(\lambda\vdash k\) whose largest part is \(k-s\) is uniquely \((k-s,\mu)\), where \(\mu\vdash s\), and the longest block is unique. For this partition,
\[
\sum_i(\lambda'_i)^2=k+s+\sum_i(\mu'_i)^2,
\quad C_\lambda(q)=q^{k+s}(1-q^{-1})C_\mu(q).
\]
The nilpotent cycle-index identity in dimension \(s\) gives \(\sum_{\mu\vdash s} C_\mu(q)^{-1}=q^{-s}/\varphi_s(q)\). Dividing the sum of the corresponding class sizes by \(q^{k^2-k}\) therefore shows
\[
\Pr(k-\nu(A)=s)=K_{q,k}\frac{q^{-2s}}{\varphi_s(q)}\qquad(2s<k).
\]
Here the term \(k-\nu(A)\) denotes the defect of the longest Jordan block of \(A\), not of \(X\). Conditional on any such \(A\), the rank of \(A^{\nu(A)-1}\) is one. Independently sampled columns in \(B\) therefore extend the nilpotency index by one with probability \(1-q^{-c}\), and leave it unchanged with probability \(q^{-c}\). To have \(D_{k,c}=s\), either the longest-block defect of \(A\) equals \(s\) and extension occurs, or it equals \(s-1\) and extension fails. These disjoint possibilities give the stated exact formula.

Finally the infinite product \(K_q\) is positive. The elementary \(q\)-binomial identity
\[
\sum_{s\ge0}\frac{u^s}{\varphi_s(q)}
=\prod_{j\ge0}(1-uq^{-j})^{-1},\quad |u|<1,
\]
with \(u=q^{-2}\) proves \(\sum_{s\ge0}K_q q^{-2s}/\varphi_s(q)=1\); it can be checked directly by the recurrence \(G(u)=G(u/q)/(1-u)\) and \(G(0)=1\). Thus the displayed limiting masses form a probability law. For each fixed \(s\), the exact edge identity applies for all sufficiently large \(k\), so the mass at \(s\) converges to that of \(S_q+E_c\) (or \(S_q\) when \(c\to\infty\)). Pointwise convergence of probability masses on the nonnegative integers to a mass-one limit implies convergence in total variation: choose a finite prefix containing all but arbitrarily little limiting mass, then compare that prefix and its complement. This proves both asymptotic assertions.

## Verification
The accompanying standalone \(\texttt{verify.py}\) enumerates every restricted-range matrix in seven small fields/dimensions, performs successive matrix multiplications directly in the relevant finite field, and compares the observed index counts against the partition formula. Fields of orders \(2,3,4,5\) are included, with \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). The cases \((q,k,c)\) are \((2,1,1)\), \((2,2,1)\), \((2,2,3)\), \((2,3,2)\), \((3,2,2)\), \((4,2,1)\) and \((5,1,2)\). A total of \(44,642\) matrices are examined (including nonnilpotent matrices, which are excluded from the counts). The reproducible result is \(\texttt{VERIFY_OK}\); the infinite-family claims rely on the preceding proof, not the finite checks.

## Relationship to prior work
Grau introduced the general independence-algebra restricted-range framework and analyzed Green relations and ideals; the cited preprint's first public date is 25 June 2022. Sullivan and Sommanee--Sangkhanan had studied linear restricted-range semigroups and their regular parts earlier. These structural foundations are not claimed anew. Standard nilpotent finite-field Jordan orbit counts and the nilpotent cycle index are classical inputs; Fulman--Guralnick explicitly recall these tools. Fulman's affine-group cycle-index paper treats a one-column affine analogue of this counting problem, so no independent priority is claimed for such specialized mechanisms.

A count restricted to **regular nilpotent** maps does not determine the unrestricted \(B\)-fibres: many nonregular maps have nilpotency index one greater than that of their restriction to \(W\). The full nilpotency-index enumerator and its codimension-dependent Bernoulli limit concern these omitted fibres. The full enumerator is not a claim about all ambient Jordan partitions.

## Limitations
The theorem does not enumerate full ambient Jordan types of \(X\), nor classify nilpotent conjugacy orbits within the restricted-range semigroup. A general parabolic cycle-index result could imply some of these formulas; this remains a literature-coverage risk. The affine one-column case, standard nilpotent orbit formulas, and known regular-restricted-range enumerations are prior ingredients, not independent contributions. Finite computational tests do not certify general identities or publication priority.

## References
1. A. Grau, *The semigroup of endomorphisms with restricted range of an independence algebra*, arXiv:2206.12526v1 (25 June 2022), DOI: 10.1007/s00233-022-10324-z.
2. R. P. Sullivan, *Semigroups of linear transformations with restricted range*, Bulletin of the Australian Mathematical Society 77 (2008), 441--453, DOI: 10.1017/S0004972708000385.
3. W. Sommanee and K. Sangkhanan, *The regular part of a semigroup of linear transformations with restricted range*, Journal of the Australian Mathematical Society 103 (2017), 402--419, DOI: 10.1017/S144678871600080X.
4. J. Fulman, *Finite Affine Groups: Cycle Indices, Hall--Littlewood Polynomials, and Probabilistic Algorithms*, arXiv:math/0009182 (2000).
5. J. Fulman and R. Guralnick, *Cohen Lenstra Partitions and Mutually Annihilating Matrices over a Finite Field*, arXiv:2111.09433 (2021), Section 3 (classical Jordan orbit counts).
