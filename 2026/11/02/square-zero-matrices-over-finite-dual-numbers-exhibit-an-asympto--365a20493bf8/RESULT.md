# Square-zero matrices over finite dual numbers exhibit an asymptotically uniform rank law

## Finding
For any prime power \(q\), put \(R_q=\mathbb F_q[\varepsilon]/(\varepsilon^2)\) and let \(n\ge1\). For each integer \(0\le r\le\lfloor n/2\rfloor\), denote by \(N_{n,r}(q)\) the number of matrices \(X\in M_n(R_q)\) such that \(X^2=0\) and the reduction \(\overline X\in M_n(\mathbb F_q)\) has rank \(r\). Write
\[
\Phi_m(q)=\prod_{j=1}^{m}(1-q^{-j}),\qquad \Phi_0(q)=1.
\]
Then the exact rank census is
\[
\boxed{N_{n,r}(q)=q^{n^2}\frac{\Phi_n(q)}{\Phi_r(q)\Phi_{n-2r}(q)}.}
\]
In particular, every allowed rank occurs, and the total number of solutions is the sum of these terms. Define \(\Phi_\infty(q)=\prod_{j\ge1}(1-q^{-j})>0\). For each fixed \(q\),
\[
\boxed{\#\{X\in M_n(R_q):X^2=0\}=q^{n^2}\left(\frac{\lfloor n/2\rfloor+1}{\Phi_\infty(q)}+O_q(1)\right).}
\]
If \(X\) is sampled uniformly among these solutions and \(R_n=\operatorname{rank}_{\mathbb F_q}(\overline X)\), then \(R_n/n\) converges weakly to the continuous uniform distribution on \([0,1/2]\). More quantitatively,
\[
\sup_{0\le t\le1/2}\left|\Pr(R_n/n\le t)-2t\right|=O_q(n^{-1}).
\]
The concentration change is substantive: over the residue field alone, the rank of a random square-zero matrix stays within bounded distance (in probability) of \(n/2\); over the split first-order thickening, every macroscopic rank interval has asymptotically its proportional length.

## Assumptions and scope
The coefficient ring is **exactly** the split finite dual-number ring \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\); it is not asserted for the possibly mixed-characteristic ring \(\mathbb Z/p^2\mathbb Z\). All prime powers \(q\) and all positive integers \(n\) are covered, including even characteristic. The rank is the rank of the reduction modulo \(\varepsilon\), not a rank assigned to a matrix over a nonfield. All counts are for labeled matrices, not similarity classes.

## Proof
**1. Reduction and tangent equation.** Every \(X\in M_n(R_q)\) is uniquely \(A+\varepsilon B\), with \(A,B\in M_n(\mathbb F_q)\). The condition \(X^2=0\) is equivalent to the pair of equations
\[
A^2=0,\qquad AB+BA=0.
\]
If \(\operatorname{rank}A=r\), then \(\operatorname{im}A\subseteq\ker A\), hence \(0\le r\le\lfloor n/2\rfloor\).

**2. Every tangent fiber has a computable size.** For any such \(A\) choose a Jordan basis with \(r\) blocks of size two and \(s=n-2r\) blocks of size one. Let \(P\) act by minus one on the images of the size-two blocks and by plus one on their preimages and on the remaining fixed vectors. Thus \(P\) is invertible and \(PA=-AP\) in all characteristics (in characteristic two this is the trivial sign identity). For \(C=BP\),
\[
AC-CA=(AB+BA)P.
\]
Therefore the allowed \(B\)'s are in bijection with the ordinary centralizer \(\{C:AC=CA\}\). Regarding the vector space as the \(\mathbb F_q[t]\)-module \((\mathbb F_q[t]/t^2)^r\oplus(\mathbb F_q[t]/t)^s\), the centralizer has dimension
\[
2r^2+2rs+s^2=(n-r)^2+r^2.
\]
Indeed the dimensions of the four block spaces of module homomorphisms are respectively \(2r^2\), \(rs\), \(rs\), and \(s^2\). Thus every rank-\(r\) reduction has exactly \(q^{(n-r)^2+r^2}\) square-zero lifts.

**3. Count the reductions.** A rank-\(r\) square-zero \(A\) is uniquely specified by its image \(U\) (dimension \(r\)), its kernel \(K\supseteq U\) (dimension \(n-r\)), and an isomorphism \(\mathbb F_q^n/K\to U\). Consequently the number of reductions of rank \(r\) equals
\[
{n\brack r}_q\,{n-r\brack r}_q\,|\operatorname{GL}_r(\mathbb F_q)|.
\]
Using \({m\brack r}_q=q^{r(m-r)}\Phi_m/(\Phi_r\Phi_{m-r})\) and \(|\operatorname{GL}_r(\mathbb F_q)|=q^{r^2}\Phi_r\), this number simplifies to
\[
q^{2r(n-r)}\frac{\Phi_n(q)}{\Phi_r(q)\Phi_{n-2r}(q)}.
\]
Multiplication by the tangent fiber count gives the claimed exact formula because
\[
2r(n-r)+(n-r)^2+r^2=n^2.
\]
This argument also covers \(r=0\) and \(n=1\) without exceptions.

**4. Uniform law and finite-size error.** Put \(w_{n,r}=\Phi_n/(\Phi_r\Phi_{n-2r})\) and \(\phi=\Phi_\infty(q)>0\). The finite products obey \(0\le\Phi_m-\phi\le C_q q^{-m}\). Since all products are at least \(\phi\), elementary bounds on reciprocals give, uniformly over the allowed ranks,
\[
|w_{n,r}-\phi^{-1}|\le C'_q\big(q^{-r}+q^{-(n-2r)}+q^{-n}\big).
\]
Summing over \(0\le r\le\lfloor n/2\rfloor\) makes the right side \(O_q(1)\): both geometric sums are bounded and \(nq^{-n}\) is bounded. Thus the total weight is \((\lfloor n/2\rfloor+1)/\phi+O_q(1)\). The same bound applies to *every initial segment* of rank weights. Since the number of ranks at most \(nt\) is \(\lfloor nt\rfloor+1\) for \(0\le t<1/2\), dividing initial weight by total weight proves \(\Pr(R_n/n\le t)=2t+O_q(1/n)\) uniformly, including the endpoint \(t=1/2\) where the probability is exactly one.

## Verification
Run `python3 verify.py` using standard Python (no third-party modules). The checker directly enumerates reduced matrices, computes the anti-commutator linear-map kernels by Gaussian elimination, and compares rank-stratified counts with the closed formula over \(\mathbb F_2\) for \(n=1,2,3,4\) and over \(\mathbb F_3\) for \(n=1,2,3\). For smaller cases it also independently enumerates all \(B\)'s. It additionally exhausts all square-zero matrices over \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\) at \(n=2\), implementing \(\mathbb F_4\) multiplication directly. The observed totals are respectively \(2,28,1184,226816\) for \(\mathbb F_2\), \(3,153,44955\) for \(\mathbb F_3\), and \(496\) for the \(\mathbb F_4\) case. All match the formula. These finite checks support but do not replace the proof for arbitrary \(q,n\).

## Relationship to prior work
The representation-scheme perspective makes the problem the first-jet point count of the square-zero matrix scheme: D'Alesio identifies the classical scheme associated to the dual-number algebra in the example in Section 2, but the inspected sections supply no rank-stratified finite-field jet counts or macroscopic uniform-rank limit. Cheong–Liang–Strand count matrix-polynomial roots over residue rings for polynomials whose reductions are square-free; their Theorem 1.1 explicitly excludes the repeated-root polynomial \(t^2\), and their coefficient ring differs from the split dual numbers here. Prasad–Singla–Spallone develop similarity-class and centralizer methods for local rings of length two, including split dual numbers, but their inspected normal-form and centralizer results are not an all-dimension formula for the square-zero locus. Classical field-level square-zero matrix counts and centralizer dimensions are antecedents and not claimed as new. The present stated contribution is the **joint explicit rank census and uniform macroscopic limiting law for first-order square-zero lifts**.

## Limitations
The result does not count similarity classes and does not apply automatically to nonsplit length-two rings, higher dual-number truncations, or higher nilpotence exponents. The all-dimensional proof is elementary but the global publication-priority assessment is provisional: a more general jet-scheme or representation-counting theorem may implicitly imply these formulas. The empirical verifier covers finite cases only. Independent mathematical validation is not claimed.

## References
1. G. Cheong, Y. Liang, and M. Strand, *Polynomial equations for matrices over integers modulo a prime power and the cokernel of a random matrix*, first posted September 8, 2022, arXiv:2209.03626, especially Introduction, Theorem 1.1, Remark 1.2.
2. A. Prasad, P. Singla, and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157, especially Sections 2–3.
3. S. D'Alesio, *Derived representation schemes and Nakajima quiver varieties*, Selecta Mathematica 28 (2022), article 20, DOI 10.1007/s00029-021-00724-4, especially Section 2, Example 1, and Section 5.1.
