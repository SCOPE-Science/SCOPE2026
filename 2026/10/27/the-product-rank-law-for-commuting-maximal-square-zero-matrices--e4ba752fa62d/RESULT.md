# The product-rank law for commuting maximal square-zero matrices

## Finding

Let \(q\) be any prime power, let \(m\ge1\), and independently choose matrices \(E,F\in M_{2m}(\mathbb F_q)\), each uniformly from the matrices satisfying \(E^2=F^2=0\) and \(\operatorname{rank}E=\operatorname{rank}F=m\). For \(j\ge0\), set
\[
\Phi_j(q)=\prod_{k=1}^{j}(1-q^{-k}),\qquad \Phi_0(q)=1,\qquad \Phi_\infty(q)=\prod_{k\ge1}(1-q^{-k}).
\]
Writing \(R=\operatorname{rank}(EF)\), every possible commuting pair has \(0\le R\le\lfloor m/2\rfloor\), and the **exact joint distribution** is
\[
\boxed{\Pr(EF=FE,\ R=r)=q^{-m^2}\frac{\Phi_m(q)^2}{\Phi_{2m}(q)\Phi_r(q)}}
\qquad (0\le r\le\lfloor m/2\rfloor).
\]
Consequently,
\[
\Pr(EF=FE)=q^{-m^2}\frac{\Phi_m(q)^2}{\Phi_{2m}(q)}
\sum_{r=0}^{\lfloor m/2\rfloor}\Phi_r(q)^{-1},
\quad
\Pr(R=r\mid EF=FE)=\frac{\Phi_r(q)^{-1}}{\sum_{s=0}^{\lfloor m/2\rfloor}\Phi_s(q)^{-1}}.
\]
At fixed \(q\), write
\[
 c_q=\sum_{r\ge0}\left(\frac{\Phi_\infty(q)}{\Phi_r(q)}-1\right)<0.
\]
Then \(c_q\) converges absolutely, and as \(m\to\infty\),
\[
\boxed{q^{m^2}\Pr(EF=FE)=\lfloor m/2\rfloor+1+c_q+O_q(q^{-m/2}).}
\]
For the conditional law of \(R\), total-variation distance from the uniform law on \(\{0,\ldots,\lfloor m/2\rfloor\}\) is \(O_q(m^{-1})\). In particular, \(2R/m\) converges in distribution to the uniform law on \([0,1]\).

## Assumptions and scope

These results hold for every finite field, of even or odd characteristic, and every positive integer \(m\). The two matrices are uniform in the **same maximal-rank square-zero conjugacy class**, not uniform among all nilpotent matrices. The exact formulas involve joint probability before conditioning and conditional probability after imposing \(EF=FE\); they are not interchangeable. The asymptotics fix \(q\) and send \(m\) to infinity. No claim is made about a simultaneous large-field limit.

## Proof

1. **Reduction to a block centralizer.** Every rank-\(m\) square-zero matrix on \(\mathbb F_q^{2m}\) is conjugate to \(E=\begin{psmallmatrix}0&I_m\\0&0\end{psmallmatrix}\). Its commuting partners have the unique form
   \[
   F=\begin{pmatrix}A&B\\0&A\end{pmatrix},
   \qquad A,B\in M_m(\mathbb F_q).
   \]
   Here \(F^2=0\) is equivalent to \(A^2=0\) and \(AB+BA=0\), while \(EF=FE=\begin{psmallmatrix}0&A\\0&0\end{psmallmatrix}\). Thus \(R=\operatorname{rank}A\), and \(0\le R\le\lfloor m/2\rfloor\).

2. **The maximal-rank constraint.** Fix a square-zero \(A\) of rank \(r\), write \(I=\operatorname{im}A\subseteq\ker A=K\), and let \(H=K/I\) with \(h=\dim H=m-2r\). If \(AB+BA=0\), then \(B\) preserves both \(K\) and \(I\), so it induces \(\overline B\in\operatorname{End}(H)\). For a vector \((u,v)\in\mathbb F_q^m\oplus\mathbb F_q^m\) to lie in \(\ker F\), necessarily \(v\in K\) and \(Au=-Bv\). The latter equation is soluble precisely when \(\overline B(v+I)=0\), and for every such \(v\) it has \(q^{m-r}\) solutions \(u\). Therefore
   \[
   \dim\ker F=(m-r)+(r+\dim\ker\overline B)=m+\dim\ker\overline B.
   \]
   It follows that \(\operatorname{rank}F=m\) exactly when \(\overline B\) is invertible.

3. **Counting anticommuting blocks.** The vector space \(\mathcal V_A=\{B:AB+BA=0\}\) has dimension
   \[
   d=(m-r)^2+r^2,
   \]
   because \(-A\) is similar to \(A\) and the square-zero centralizer has this dimension. More directly, in the Jordan decomposition \((2^r,1^{m-2r})\), the centralizer dimension is the sum of squares of column lengths \((m-r,r)\). The natural linear map \(\mathcal V_A\to\operatorname{End}(H)\) is surjective: choose an invariant complement of the length-two Jordan summands and set \(B\) arbitrarily there, zero on the remaining summands. Hence exactly
   \[
   q^{d-h^2}|\operatorname{GL}_h(\mathbb F_q)|=q^d\Phi_h(q)
   \]
   matrices \(B\) satisfy both anticommutation and \(\operatorname{rank}F=m\). This includes the case \(h=0\), where the zero-dimensional map is invertible by convention.

4. **Counting diagonal blocks.** To choose a square-zero \(A\) with rank \(r\), choose its image \(I\) (dimension \(r\)), its kernel \(K\supset I\) (codimension \(r\)), and the induced isomorphism \(\mathbb F_q^m/K\to I\). These choices number
   \[
   {m\brack r}_q {m-r\brack r}_q |\operatorname{GL}_r(\mathbb F_q)|
   =q^{2r(m-r)}\frac{\Phi_m(q)}{\Phi_r(q)\Phi_{m-2r}(q)}.
   \]
   Multiplying by the count in Step 3 and using
   \[
   2r(m-r)+d=m^2
   \]
   gives precisely
   \[
   N_{m,q}(r)=q^{m^2}\frac{\Phi_m(q)}{\Phi_r(q)}
   \]
   commuting maximal-rank square-zero partners \(F\) at product rank \(r\), for **each fixed** \(E\).

5. **Normalization to probabilities.** The total number of maximal-rank square-zero matrices \(F\) on \(\mathbb F_q^{2m}\) is
   \[
   {2m\brack m}_q|\operatorname{GL}_m(\mathbb F_q)|
   =q^{2m^2}\frac{\Phi_{2m}(q)}{\Phi_m(q)}.
   \]
   Dividing \(N_{m,q}(r)\) by this count proves the joint probability and, on summing over \(r\), the conditional law. Conjugacy ensures that using fixed \(E\) is equivalent to independently sampling \(E\) uniformly.

6. **Limit and quantitative bounds.** Put \(M=\lfloor m/2\rfloor\) and \(a_r=\Phi_\infty(q)/\Phi_r(q)=\prod_{j>r}(1-q^{-j})\). For fixed \(q\),
   \[
   0\le1-a_r\le\sum_{j>r}q^{-j}=O_q(q^{-r}),\qquad
   \sum_{r>M}(1-a_r)=O_q(q^{-M}).
   \]
   Also \(\Phi_m(q)^2/(\Phi_{2m}(q)\Phi_\infty(q))=1+O_q(q^{-m})\). Thus the exact formula yields
   \[
   q^{m^2}\Pr(EF=FE)
   =\left(1+O_q(q^{-m})\right)\sum_{r=0}^{M}a_r
   =M+1+c_q+O_q(q^{-M})
   \]
   (absorbing \(O_q(mq^{-m})\)). Since \(\sum_{r\ge0}|a_r-1|<\infty\), the normalized weights \(a_r/\sum_{s=0}^{M}a_s\) differ in total variation by \(O_q((M+1)^{-1})\) from uniform weights \((M+1)^{-1}\). Uniform distribution on the integer interval rescales to \(\operatorname{Unif}[0,1]\), completing the proof.

## Verification

A standalone finite-field checker is included as `checker.py`, with recorded output `check_output.txt`. It constructs commuting block matrices, directly tests matrix rank and square-zero constraints, counts product ranks and compares all strata to the exact closed formulas. It enumerates nine configurations: \(m=1\) with prime fields of sizes \(2,3,5,7\); \(m=2\) with the same four fields; and \(m=3\) over \(\mathbb F_2\). Across these configurations it examines 145348 candidate block pairs. The final assertion is `ALL_MAXIMAL_SQUAREZERO_COMMUTATION_TESTS_PASSED`. The proof above, not finite enumeration, establishes the claims for every prime power and all \(m\).

## Relationship to prior work

Bogdanić–Đurić–Koljančić–Oblak–Šivic [1] classify possible nilpotent Jordan forms in a centralizer when the fixed nilpotent has two equal blocks; this motivates study of prescribed Jordan profiles, but their classification does not supply the present rank-resolved finite-field partner count or its uniform limit. Kokol Bukovšek–Košir–Novak–Oblak [2] analyze products of commuting nilpotent operators and establish restrictions on product Jordan types, including products of two square-zero matrices; possible rank strata alone do not specify multiplicities in the maximal-rank classes. Britnell–Wildon [3] study pairs of commuting similarity classes, chiefly the existence question. Huang [4] enumerates mutually annihilating pairs and Huang [5] develops broader module-counting methods; the presently derived exact rank-\(r\) law in two prescribed maximal square-zero classes is not asserted as a result of those works. Generic enumeration of commuting matrices does not immediately determine this conditional distribution. The counting tools themselves (centralizers, Gaussian coefficients, orbit counts) are classical; the assessed contribution is their exact combination and the limiting uniformity for this constrained joint invariant.

## Limitations

The claim is a rank statistic, not a classification of simultaneous similarity orbits for the pair. The statement applies only to two maximal-rank square-zero matrices of even common ambient dimension. The small cases corroborate but cannot prove the large-dimension limit. A possibly relevant 2024 thesis on commuting matrix varieties with prescribed ranks could not be inspected in full, and formulas from Hall-polynomial treatments or unindexed literature may contain equivalent specializations. No exhaustive originality or independent mathematical validation is asserted.

## References

[1] D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, K. Šivic, "Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size," arXiv:2212.08425 (first posted 2022-12-16). https://arxiv.org/abs/2212.08425

[2] D. Kokol Bukovšek, T. Košir, L. Novak, P. Oblak, "Products of commuting nilpotent operators," Electronic Journal of Linear Algebra 16 (2007), 237–247.

[3] J. R. Britnell, M. Wildon, "On types and classes of commuting matrices over finite fields," arXiv:1001.0811. https://arxiv.org/abs/1001.0811

[4] Y. Huang, "Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity," arXiv:2110.15566. https://arxiv.org/abs/2110.15566

[5] Y. Huang, "Commuting matrices via commuting endomorphisms," arXiv:2404.19483. https://arxiv.org/abs/2404.19483
