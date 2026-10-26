# Antipodal square-root defect in edge-parity extinction on folded hypercubes

## Finding

For each integer \(d\ge3\), define the **augmented binary cube** \(H_d\) on vertex set \(\mathbb F_2^d\). A vertex \(v\) is joined to each \(v+e_i\), \(1\le i\le d\), and also to \(v+\mathbf1\), its bitwise complement. For \(d\ge3\) these are distinct neighbours. Let \(G_d=L(H_d)\) be its ordinary, loopless line graph: vertices of \(G_d\) are edges of \(H_d\), with two distinct edge-sites adjacent exactly when the corresponding edges share an endpoint.

Define the synchronous binary parity update \(F_d:\mathbb F_2^{E(H_d)}\to\mathbb F_2^{E(H_d)}\) by \((F_dx)_e=\sum_{f\sim e}x_f\pmod2\). It has \(M_d=(d+1)2^{d-1}\) coordinates. Put \(s_d=2^{\lfloor(d-1)/2\rfloor}\).

**Theorem (complete edge-parity transient law).** The operator satisfies \(F_d^3=0\). Its complete nilpotent Jordan block multiplicities over \(\mathbb F_2\) are
\[
\begin{aligned}
b_3(d)&=2^{d-1}-s_d-2,\\
b_2(d)&=2s_d+2,\\
b_1(d)&=(d-2)2^{d-1}+2-s_d.
\end{aligned}
\]
Here \(b_j(d)\) counts Jordan blocks of size \(j\); no other sizes occur. The maximum number of updates before extinction is exactly two for \(d=3\), and three for \(d\ge4\).

For an initial state \(x\), let \(\tau(x)=\min\{t\ge0:F_d^tx=0\}\). Write \(r_1=2^d-2\) and \(r_2=2^{d-1}-s_d-2\). The number of initial states of each exact extinction time is
\[
\begin{aligned}
\#\{\tau=0\}&=1,\\
\#\{\tau=1\}&=2^{M_d-r_1}-1,\\
\#\{\tau=2\}&=2^{M_d-r_2}-2^{M_d-r_1},\\
\#\{\tau=3\}&=2^{M_d}-2^{M_d-r_2}.
\end{aligned}
\]
For \(d\ge4\), the final stratum has density \(1-2^{-r_2}\). For \(d=3\), \(r_2=0\) and the four extinction-time counts are \(1,1023,64512,0\); thus the sharp last-step density is \(63/64\). On the line graph of the unaugmented cube, the known binary adjacency-code and hull dimensions imply \(\operatorname{rank}(F_d^2)=2^{d-1}-2\); the antipodal edges create an additional rank deficiency exactly \(s_d\), an unbounded square-root-scale correction in the number of cube vertices.

## Assumptions and scope

The graphs are finite, simple and undirected; the extra antipodal matching is added to the original cube without identifying antipodal vertices. This is distinct from the alternative convention that calls the quotient graph a folded cube. All matrix arithmetic and state values are over \(\mathbb F_2\). Time is counted in simultaneous updates; a state already zero has extinction time zero. The theorem concerns all \(d\ge3\), not a numerical cutoff, and makes no claim about other update rules, graph families, or asynchronous schedules.

## Proof

**1. Edge-to-vertex factorization.** Let \(n=2^d\) and \(m=M_d\), and let \(B\in\mathbb F_2^{n\times m}\) be the unoriented vertex–edge incidence matrix. Because \(H_d\) is simple, \(F_d=B^{\mathsf T}B\) exactly: every diagonal entry equals two and vanishes modulo two, and every off-diagonal entry is one precisely for incident distinct edges. Put \(Q=BB^{\mathsf T}\). Since \(H_d\) is connected, \(\operatorname{im}B\) is the even-coordinate-sum hyperplane \(J\) of dimension \(n-1\), and \(\ker B^{\mathsf T}\) is the span of the all-one vector \(u\). As \(n\) is even, \(u\in J\), giving \(\operatorname{rank}F_d=n-2\).

**2. Square-zero vertex operator.** Identify vertex functions with the group algebra of the elementary abelian group \(\mathbb F_2^d\), using translations \(g_i\) and truncated variables \(t_i=1+g_i\). This is the algebra
\[
R=\mathbb F_2[t_1,\ldots,t_d]/(t_1^2,\ldots,t_d^2).
\]
Write \(\mathfrak m=(t_1,\ldots,t_d)\); this is precisely the hyperplane \(J\) above. The complement translation is \(P=\prod_{i=1}^d(1+t_i)\). As \(H_d\) has degree \(d+1\), its vertex operator \(Q=BB^{\mathsf T}\) is multiplication by
\[
q=(d+1)+\sum_{i=1}^d(1+t_i)+\prod_{i=1}^d(1+t_i)=\sum_{j=2}^{d}e_j(t_1,\ldots,t_d).
\]
Every positive-degree element of \(R\) has square zero under Frobenius in characteristic two. Thus \(q^2=0\), so \(F_d^3=B^{\mathsf T}Q^2B=0\).

**3. A truncated quadratic normal-form lemma.** More generally, in this square-zero polynomial algebra, suppose \(f\in\mathfrak m^2\) has a quadratic part whose associated alternating form has corank at most one. Let \(h=\lfloor d/2\rfloor\). An invertible linear change of variables puts that quadratic part into \(\omega=\sum_{j=1}^{h}a_jb_j\), with at most one unused variable \(c\). All variables, including their invertible linear combinations, square to zero, so every invertible linear coordinate change acts on \(R\). We can remove successively all homogeneous terms of degrees three through \(d\). Indeed, each monomial of degree at least three contains at least one paired variable, since there is at most one unused variable. The derivatives of \(\omega\) with respect to paired variables span those paired variables. Consequently the degree-\(k\) correction is a sum of products of such derivatives by elements of degree \(k-1\). Replacing each appropriate paired variable by itself plus those degree-\(k-1\) corrections removes the degree-\(k\) part without affecting lower degrees; the substitution is invertible because its linear part is the identity. Corrections to the already higher-order part begin at degree \(k+1\). Inducting on \(k\) yields an algebra automorphism taking \(f\) to \(\omega\).

For \(q\), the quadratic part is \(e_2=\sum_{i<j}t_it_j\). Its alternating matrix has zero diagonal and all off-diagonal entries one, equivalently it is \(I+\mathbf1\mathbf1^{\mathsf T}\) over \(\mathbb F_2\). Its rank is \(d\) for even \(d\) and \(d-1\) for odd \(d\): the kernel consists of multiples of \(\mathbf1\) only when \(d\) is odd. The lemma therefore applies.

**4. Rank of multiplication by \(q\).** The change of variables preserves the rank of a multiplication operator. On each four-dimensional factor \(\mathbb F_2[a_j,b_j]/(a_j^2,b_j^2)\), multiplication by \(a_jb_j\) sends \(1\) to \(a_jb_j\) and kills \(a_j,b_j,a_jb_j\). This square-zero complex splits as a contractible two-dimensional summand and a zero-differential two-dimensional summand. Tensoring all \(h\) factors, the sum differential \(\omega=\sum a_jb_j\) has homology dimension \(2^h\); if \(d\) is odd the extra free variable doubles that dimension. (Every summand containing a contractible factor is contracted on that factor; in characteristic two the cross-differential terms cancel.) As \(\mu_\omega^2=0\), its rank is half the difference between total dimension and homology dimension. Hence
\[
\operatorname{rank}Q=2^{d-1}-2^{\lfloor(d-1)/2\rfloor}=2^{d-1}-s_d.
\]

**5. Rank of the second iterate.** Since \(q\) has a nonzero quadratic part, \(q\notin q\mathfrak m\): all elements of \(q\mathfrak m\) have degree at least three. Thus \(\dim(q\mathfrak m)=\operatorname{rank}Q-1\). The all-one vector \(u\) corresponds to the top monomial \(t_1\cdots t_d\). It belongs to \(q\mathfrak m\): in normal-form coordinates, multiplying \(\omega\) by the product of all variables except \(a_1,b_1\) yields the top monomial, and for \(d\ge3\) the multiplier has positive degree. Any invertible change of variables preserves the one-dimensional socle, whose generator is the top monomial. Therefore
\[
\operatorname{rank}F_d^2=\dim B^{\mathsf T}qJ=\dim(q\mathfrak m)-1=2^{d-1}-s_d-2.
\]

**6. Jordan and extinction counts.** If a nilpotent matrix has cube zero, the number of Jordan blocks of sizes three, two and one are respectively \(\operatorname{rank}F_d^2\), \(\operatorname{rank}F_d-2\operatorname{rank}F_d^2\), and \(m-2\operatorname{rank}F_d+\operatorname{rank}F_d^2\). Substituting the ranks in steps 1 and 5 gives the three claimed multiplicities. They are nonnegative for every \(d\ge3\), with \(b_3(3)=0\) and \(b_3(d)>0\) for \(d\ge4\), establishing sharpness. Finally, \(\{x:\tau(x)\le t\}=\ker(F_d^t)\) has size \(2^{m-\operatorname{rank}(F_d^t)}\), producing the exact counts and fractions.

## Verification

A standalone verifier `check_folded_cube.py` builds the actual augmented-cube edges from bitwise flips and bitwise complements, then independently constructs the *line graph* adjacency over \(\mathbb F_2\). It computes \(F_d\), \(F_d^2\) and \(F_d^3\) by exact binary row arithmetic and independently checks all stated ranks for \(3\le d\le7\), reaching 512 edge-sites. For \(d=3\), it exhaustively simulates all 65,536 labelled initial configurations and obtains time counts \(1,1023,64512,0\). Recorded output is in `folded_line_verification.txt`. These finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work

Fish, Key and Mwambene (2010) analyze binary codes of the line graphs \(L(Q_d)\) of the **unaugmented** cubes. Their indexed principal theorem gives the adjacency-code rank and hull dimension, implying \(\operatorname{rank}(A_{L(Q_d)}^2)=2^{d-1}-2\), but not the folded family in this theorem. The original authors' PDF was not available for complete text inspection in this investigation, so the comparison beyond its indexed principal theorem is qualified. Ghinelli, Key and McDonough (2014) describe general incidence-code hull relations; these do not evaluate the required folded-cube vertex operator. Liu, Pan and Cao (2014) calculate real spectra and Estrada indices of the **vertex graph** \(H_d\), not modular Jordan decompositions on its **line graph**. Related published results on parity cellular automata show why such operators are natural, but do not supply these formulas.

## Limitations

Historical priority is not certified: an unindexed or inaccessible equivalent construction may exist, and independent review has not been performed. The explicit Jordan law concerns only binary open-neighbour synchronous updates on \(L(H_d)\), not the original vertices, quotient folded cubes, nonbinary fields, or arbitrary augmented Cayley graphs. The computational tests are limited to \(3\le d\le7\), while the proof covers all \(d\ge3\). The known unaugmented-cube adjacency-code result is not claimed as new.

## References

- J.-B. Liu, X.-F. Pan, J. Cao, “Some Properties on Estrada Index of Folded Hypercubes Networks,” *Abstract and Applied Analysis* (2014), article 167623, DOI: 10.1155/2014/167623. First publicly dated 2014-02-05. Open publisher full text: https://onlinelibrary.wiley.com/doi/10.1155/2014/167623 .
- W. Fish, J. D. Key, E. Mwambene, “Binary codes from the line graph of the n-cube,” *Journal of Symbolic Computation* **45** (2010), 800–812, DOI: 10.1016/j.jsc.2010.03.012. Indexed Theorem 1 consulted; full author-hosted PDF unavailable.
- D. Ghinelli, J. D. Key, T. McDonough, “Hulls of codes from incidence matrices of connected regular graphs,” *Designs, Codes and Cryptography* **70** (2014), 35–54. Abstract and repository information consulted: https://research.aber.ac.uk/en/publications/hulls-of-codes-from-incidence-matrices-of-connected-regular-graph/ .
