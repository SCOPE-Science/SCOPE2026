# Independent theta coordinates for idempotents centralizing two-length Jordan forms

## Finding
The contribution asserted here is the parity-sensitive asymptotic independence theorem and its quantitative total-variation convergence. The exact finite profile formula below is a classical orbit-stabilizer input, and is not claimed as independently new.
Fix a prime power \(q\), distinct positive integers \(a<b\), and an integer \(m\ge 1\). Over \(\mathbb F_q\), let \(J_{a,b,m}\) be nilpotent with exactly \(m\) Jordan blocks of length \(a\) and \(m\) of length \(b\). Sample \(E\) uniformly among the matrices satisfying \(E^2=E\) and \(EJ_{a,b,m}=J_{a,b,m}E\). Its image is an invariant direct summand, with exactly \(r\) length-\(a\) and \(s\) length-\(b\) Jordan blocks, where \(0\le r,s\le m\).

Put \(\Phi_k(q)=\prod_{h=1}^k(1-q^{-h})\) (\(\Phi_0(q)=1\)) and \(D(x,y)=ax^2+2axy+by^2\). The exact number of such idempotents with profile \((r,s)\) is
\[
N_m(r,s)=q^{D(m,m)-D(r,s)-D(m-r,m-s)}
\frac{\Phi_m(q)^2}{\Phi_r(q)\Phi_s(q)\Phi_{m-r}(q)\Phi_{m-s}(q)}.
\]
In particular this expression is an integer and the probabilities are \(N_m(r,s)/\sum_{i,j=0}^m N_m(i,j)\).

Define the integer-valued coordinate \(W_m=r+s-m\) and the centered coordinate \(V_m=s-m/2\). Let \(\delta_m=0\) if \(m\) is even and \(\delta_m=1/2\) if \(m\) is odd. For \(c\ge1\) and \(\delta\in\{0,1/2\}\), set
\[
\Theta_{q,c}(\delta)=\sum_{k\in\mathbb Z+\delta}q^{-2ck^2}.
\]
As \(m\to\infty\) along either parity, the joint law of \((W_m,V_m)\) converges in total variation, with error \(O_{q,a,b}(q^{-m/4})\), to the independent pair \((W,V)\) with
\[
\Pr(W=w,V=v)=\frac{q^{-2aw^2}}{\Theta_{q,a}(0)}\frac{q^{-2(b-a)v^2}}{\Theta_{q,b-a}(\delta_m)},
\quad w\in\mathbb Z,\quad v\in\mathbb Z+\delta_m.
\]
Thus the two coordinates become independent, while the separate centered block multiplicities \(r-m/2=W_m-V_m\) and \(s-m/2=V_m\) become negatively correlated; their limiting covariance is \(-\operatorname{Var}(V)\).

## Assumptions and scope
All statements hold for every finite field (no restriction on characteristic), every fixed pair \(1\le a<b\), and all \(m\ge1\). The two theta limits differ on the two parities through the lattice of \(V_m\). A single limiting law without selecting parity is not claimed. Uniform sampling is from **idempotents in the centralizer**, not from all commuting matrices. An image profile records the Jordan decomposition of the restriction of \(J_{a,b,m}\) to \(\operatorname{im}E\); it is not merely matrix rank.

## Proof
Write \(R_j=\mathbb F_q[t]/(t^j)\) and regard the vector space as the \(\mathbb F_q[t]\)-module \(M=R_a^m\oplus R_b^m\), with \(t\) acting as \(J_{a,b,m}\). The commuting matrices form \(\operatorname{End}_{\mathbb F_q[t]}(M)\). For \(M_{x,y}=R_a^x\oplus R_b^y\), the homomorphism-space dimensions are \(\dim_{\mathbb F_q}\operatorname{Hom}(R_i,R_j)=\min(i,j)\); hence \(\dim\operatorname{End}(M_{x,y})=D(x,y)\).

An endomorphism of \(M_{x,y}\) is invertible precisely when the leading coefficient matrices on the two equal-length diagonal blocks are both invertible. Indeed, on \(M_{x,y}/tM_{x,y}\), the off-diagonal map from \(R_a^x\) to \(R_b^y\) vanishes because its image is divisible by \(t^{b-a}\). Consequently the induced matrix is block triangular, with diagonal constant-coefficient matrices of sizes \(x\) and \(y\). Invertibility on the quotient is equivalent to invertibility of these two matrices; the converse for \(M_{x,y}\) follows from the finite-length version of Nakayama's lemma, or by the descending \(t\)-adic filtration. Every diagonal pair occurs and all fibers of the leading-coefficient map have the same size. Therefore
\[
|\operatorname{Aut}(M_{x,y})|=q^{D(x,y)-x^2-y^2}|\operatorname{GL}_x(\mathbb F_q)||\operatorname{GL}_y(\mathbb F_q)|=q^{D(x,y)}\Phi_x(q)\Phi_y(q).
\]

Every commuting idempotent \(E\) specifies an ordered internal direct-sum decomposition \(M=\operatorname{im}E\oplus\ker E\). By uniqueness of cyclic-primary decomposition, the respective isomorphism types are \(M_{r,s}\) and \(M_{m-r,m-s}\). Conversely such a decomposition defines exactly one commuting projection. All decompositions of a specified pair of types form one orbit under \(\operatorname{Aut}(M)\), and the stabilizer is \(\operatorname{Aut}(M_{r,s})\times\operatorname{Aut}(M_{m-r,m-s})\). Orbit-stabilizer gives the displayed exact number.

For the limit, write \(u=r-m/2\), \(v=s-m/2\), \(w=u+v=r+s-m\). The quadratic identity
\[
D(m,m)-D(r,s)-D(m-r,m-s)=\tfrac12D(m,m)-2a w^2-2(b-a)v^2
\]
follows by expansion. After removing the common factor \(q^{D(m,m)/2}\), the exact weight at \((w,v)\) is
\[
q^{-2aw^2-2(b-a)v^2}\,H_m(r,s),\qquad H_m(r,s)=\frac{\Phi_m(q)^2}{\Phi_r(q)\Phi_s(q)\Phi_{m-r}(q)\Phi_{m-s}(q)}.
\]
Here \(w\in\mathbb Z\) and \(v\in\mathbb Z+\delta_m\); the admissible \((w,v)\) also satisfy \(0\le m/2+v\le m\) and \(0\le m/2+w-v\le m\). The infinite product \(\Phi_\infty(q)>0\) gives a uniform positive lower and upper bound on \(H_m\). In the central box \(|u|,|v|\le m/4\), uniformly
\[
H_m(r,s)=\Phi_\infty(q)^{-2}(1+O_q(q^{-m/4})),
\]
because \(\Phi_k(q)=\Phi_\infty(q)(1+O_q(q^{-k}))\). Outside that box, either \(|w|>m/8\) or \(|v|>m/8\), so the sum of the two-dimensional Gaussian weights is \(O_{q,a,b}(q^{-c m^2})\) for some \(c>0\). Summing and normalizing proves the claimed total-variation bound and factorization of the limiting theta series. Since these discrete Gaussian tails bound second moments uniformly, convergence of covariance follows too: \(u=W-V\), and independent centered \(W,V\) give \(\operatorname{Cov}(u,v)=-\operatorname{Var}(V)\).

## Verification
The standalone script `check_idempotent_jordan.py` constructs commutant bases or enumerates complete small matrix spaces, tests \(E^2=E\) directly, recovers each image Jordan profile using \(\operatorname{rank}(E)\) and \(\operatorname{rank}(J^aE)\), and compares every observed profile count with the exact formula. For \(q=2,a=1,b=2,m=2\), its independently enumerated nine profile counts (in row order of \(r,s\)) are \(1,384,256,96,2304,96,256,384,1\), totaling \(3778\) idempotents in a centralizer of \(1048576\) matrices. Over five configurations, it examines \(1049427\) centralizer matrices and finds \(3852\) idempotents. The script only verifies finite instances; it does not establish the infinite theta limit.

## Relationship to prior work
Wang's 2019 preprint gives explicit bases of matrix centralizers using module homomorphisms. De la Cruz and Misa (2022) identify the semisimple quotient of nilpotent-matrix centralizers using Weyr structure. Those are structural antecedents to the unit count; neither examined treatment states the two-length idempotent image-profile multiplicities or the independent parity-sensitive theta limit. Ellerman's 2016 direct-decomposition counts treat vector spaces (the single simple-module situation), not two distinct nilpotent Jordan lengths. An earlier published enumeration of retractions for almost-abelian Lie endomorphisms already uses the general quotient of module-automorphism orders to count invariant direct-summand decompositions; after shifting the nilpotent operator by the identity, that result includes the exact finite profile formula here. That finite formula is explicitly credited as prior coverage, not presented as new. The specifically isolated contribution is the **two-coordinate theta factorization, its even/odd lattice distinction, and quantitative convergence**.

## Limitations
No claim is made for arbitrary arrays of Jordan lengths, for a moving pair of lengths, or for uniformity in \(q,a,b\). The constants in the convergence estimate can depend on all three. Existing general finite-module counting identities could contain an equivalent exact formula, and an unindexed source could contain the asymptotic factorization. The originality comparison is therefore best-knowledge rather than a proof of priority. The computational tests are exhaustive only in the explicitly listed small configurations.

## References
1. T. Wang, *Explicit Description of Centralizers for a Matrix*, first public arXiv submission 2019-10-30, arXiv:1910.13666, https://arxiv.org/abs/1910.13666.
2. R. J. de la Cruz and E. Misa, *The Algebra Generated by Nilpotent Elements in a Matrix Centralizer*, Electronic Journal of Linear Algebra **38** (2022), 1–8, https://journals.uwyo.edu/index.php/ela/article/download/6503/5685/10645.
3. D. Ellerman, *The Number of Direct-Sum Decompositions of a Finite Vector Space*, arXiv:1603.07619 (2016), https://arxiv.org/abs/1603.07619.
