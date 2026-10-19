# Nilpotency-index distribution for arbitrary nilpotent Jordan types over finite dual numbers

## Finding
Let \(q\) be a prime power, let \(A\in M_n(\mathbb F_q)\) be nilpotent with Jordan-block partition \(\lambda=(\lambda_1,\ldots,\lambda_t)\) of \(n\), and let \(k=\max_i\lambda_i\). Put
\[
R_q=\mathbb F_q[\varepsilon]/(\varepsilon^2),\qquad
\rho_\ell(\lambda)=\sum_{i=1}^{t}\sum_{j=1}^{t}\max\{0,\lambda_i+\lambda_j-\ell\}.
\]
For every integer \(k\le\ell\le2k\), **the exact number** of matrices \(B\in M_n(\mathbb F_q)\) for which \(A+\varepsilon B\) has nilpotency index at most \(\ell\) is
\[
\boxed{q^{n^2-\rho_\ell(\lambda)}}.
\]
Equivalently, for uniformly sampled \(B\),
\[
\boxed{\Pr\!\left(\operatorname{ind}(A+\varepsilon B)\le\ell\right)=q^{-\rho_\ell(\lambda)}.}
\]
The mass at \(k\) equals \(q^{-\rho_k(\lambda)}\), and for \(k<\ell\le2k\) the probability of index exactly \(\ell\) is
\[
q^{-\rho_\ell(\lambda)}-q^{-\rho_{\ell-1}(\lambda)}.
\]
If \(s\) is the multiplicity of the largest Jordan block size \(k\), then
\[
\boxed{\Pr\!\left(\operatorname{ind}(A+\varepsilon B)=2k\right)=1-q^{-s^2}}.
\]

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary finite, including characteristic two and all nonprime prime powers. The matrix size \(n\ge1\) is unrestricted. The matrix \(A\) is **fixed**, nilpotent, and its Jordan-block partition is fixed; only the dual coefficient \(B\in M_n(\mathbb F_q)\) varies freely. The Jordan blocks have ones on the superdiagonal. The nilpotency index of a matrix over \(R_q\) is the least positive integer \(d\) for which its \(d\)-th power vanishes. This is a **conditional fiber distribution**, not an aggregate count over all nilpotent reductions.

The theorem includes reductions with one block, repeated blocks, mixed block sizes, and the zero matrix (whose Jordan partition is all ones). The powers of every lift vanish by index \(2k\), and no lift has index below \(k\).

## Proof
**Step 1: linearized powers.** Write \(N=A+\varepsilon B\). As \(\varepsilon\) is central and its square vanishes, multiplication gives, for every positive integer \(m\),
\[
N^m=A^m+\varepsilon T_m(B),\qquad
T_m(B)=\sum_{r=0}^{m-1}A^rBA^{m-1-r}.
\]
Since \(A^k=0\), whenever \(m\ge k\) the equality \(N^m=0\) is equivalent to the homogeneous linear condition \(T_m(B)=0\). Thus the desired number is determined by the \(\mathbb F_q\)-rank of \(T_m\). Also \(T_{2k}=0\), since in each summand one exponent is at least \(k\).

**Step 2: reduce to ordered block pairs.** Simultaneous conjugation by a matrix over \(\mathbb F_q\) is a bijection on the possible \(B\), so take \(A=\bigoplus_{i=1}^{t}J_{\lambda_i}\), where \(J_a\) is the zero-eigenvalue Jordan block. Each rectangular \((i,j)\)-block of \(B\) is acted on independently by
\[
T_m^{a,b}(X)=\sum_{r=0}^{m-1}J_a^r X J_b^{m-1-r}
\quad\text{on}\quad M_{a\times b}(\mathbb F_q),
\]
with \(a=\lambda_i\) and \(b=\lambda_j\). Therefore \(\operatorname{rank}T_m=\sum_{i,j}\operatorname{rank}T_m^{\lambda_i,\lambda_j}\).

**Step 3: rectangular rank lemma, valid over every field.** For arbitrary positive integers \(a,b\), every integer \(m\ge\max(a,b)\), and every field \(K\),
\[
\operatorname{rank}_K T_m^{a,b}=\max\{0,a+b-m\}.
\]
To prove this, let \(E_{ij}\), with \(1\le i\le a\), \(1\le j\le b\), be rectangular matrix units. Identify \(E_{ij}\) with the monomial \(u^{a-i}v^{j-1}\) in the \(ab\)-dimensional truncated polynomial algebra
\[
S=K[u,v]/(u^a,v^b).
\]
With the stated Jordan convention, left multiplication by \(J_a\) corresponds exactly to multiplication by \(u\), while right multiplication by \(J_b\) corresponds to multiplication by \(v\). Consequently \(T_m^{a,b}\) corresponds to multiplication by the complete homogeneous polynomial
\[
h_{m-1}(u,v)=\sum_{r=0}^{m-1}u^rv^{m-1-r}.
\]
For every \(d\ge m-1\), because \(m\ge\max(a,b)\) and hence \(u^{d+1}=v^{d+1}=0\) in \(S\), the elementary identities
\[
u h_d=h_{d+1}-v^{d+1}=h_{d+1},\qquad
v h_d=h_{d+1}-u^{d+1}=h_{d+1}
\]
hold in \(S\). Thus the ideal \((h_{m-1})\), which is the image of \(T_m^{a,b}\), is spanned by the consecutive homogeneous elements \(h_{m-1},h_m,\ldots,h_{a+b-2}\) (empty if \(m>a+b-1\)). Each listed element is nonzero: for each such total degree, at least one monomial lies within the rectangle \(0\le\deg_u<a\), \(0\le\deg_v<b\), with coefficient exactly one. They have distinct total degrees, so they are linearly independent, including in positive characteristic. Their number is \(\max(0,a+b-m)\), proving the lemma.

**Step 4: count the fibers.** Because \(m\ge k\ge\max(\lambda_i,\lambda_j)\), the lemma yields
\[
\operatorname{rank}_{\mathbb F_q}T_m=\sum_{i,j}\max\{0,\lambda_i+\lambda_j-m\}=\rho_m(\lambda).
\]
The source and target of \(T_m\) both have dimension \(n^2\). Hence \(\ker T_m\) has dimension \(n^2-\rho_m(\lambda)\), and has exactly \(q^{n^2-\rho_m(\lambda)}\) elements. This proves the cumulative law. Subtract consecutive cumulative counts to obtain each exact index class; all these differences are nonnegative by nesting of power-zero conditions.

Finally, at \(m=2k-1\) the term \(\max(0,\lambda_i+\lambda_j-m)\) is one precisely when both sizes equal \(k\), and zero otherwise. Therefore \(\rho_{2k-1}=s^2\), whereas \(\rho_{2k}=0\). The maximal-index probability is \(1-q^{-s^2}\).

## Verification
The accompanying self-contained `verify.py` reproduces the rank lemma and distribution using direct modular linear algebra, plus exhaustive matrix-power evaluation in the dual ring. It checks \(318\) rank identities for every partition of dimensions through \(6\), in characteristics \(2\), \(3\), and \(5\). It also exhaustively checks \(9\) prime-field cases and \(4\) tests over \(\mathbb F_4\). Both cumulative counts and exact-index counts agree in every test. These finite checks are sanity tests; the field-independent polynomial-ideal argument above proves the complete theorem.

For example, for \(\lambda=(2,1)\) and \(q=2\), the numbers at indices \(2,3,4\) are \(32,224,256\), respectively. For \(\lambda=(2,2)\) and \(q=2\), they are \(256,3840,61440\). The latter case has maximal-index probability \(15/16\), rather than the \(1/2\) associated with a single maximal Jordan block over \(\mathbb F_2\).

## Relationship to prior work
Şentürk and Özbay, *On the Regularity and Clean Properties of Matrices over Dual Numbers* (arXiv:2609.29468v1), prove in Theorem 2.5 that nilpotency of a matrix over dual numbers is detected by its reduction and establish the upper bound twice the nilpotency index of the reduction. Their manuscript does not give a conditional distribution by Jordan partition.

The earlier result *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers* (2026) determines the complete distribution when the reduction is **one** Jordan block; its limitations explicitly leave reductions with multiple blocks untreated. The present theorem genuinely extends that result to all nilpotent Jordan types, with nontrivial contributions from each ordered pair of blocks. For a one-block partition \(\lambda=(n)\), the formula specializes to \(\rho_m=\max(0,2n-m)\) and agrees with the known geometric distribution. The one-block case is not claimed as new.

Brawley's *Counting Matrices by Drazin Index* (1982) develops aggregate counts by Drazin index over finite fields and extensions to some finite rings. Aggregate Drazin-index enumeration is a distinct invariant from the **conditional** distribution of nilpotency indices across every lift of one prescribed nilpotent reduction with given partition. Its available abstract and introductory material do not settle that finer question; full-text comparison of the entire article remains a residual originality risk.

## Limitations
The formula conditions on a nilpotent reduction \(A\) and assumes a square-zero scalar extension. It does not classify Jordan types of the lifted operator as modules over the dual-number ring, and does not address higher nilpotency lengths such as \(\varepsilon^3=0\). The linearized-power rank mechanism may overlap with classical results about tangent maps of matrix powers. Exhaustive literature searches and database comparisons do not establish historical uniqueness. The full-text comparison with the 1982 Brawley article remains unresolved; its potential relationship to conditional counts must be kept as an explicit originality risk.

## References
1. Berrin Şentürk and Neslihan Ayşen Özbay, *On the Regularity and Clean Properties of Matrices over Dual Numbers*, arXiv:2609.29468v1, first publicly posted 2026-09-24, https://arxiv.org/abs/2609.29468 .
2. *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7 .
3. J. V. Brawley, *Counting Matrices by Drazin Index*, *SIAM Journal on Algebraic and Discrete Methods* **3** (1982), 30–34, https://doi.org/10.1137/0603003 .
