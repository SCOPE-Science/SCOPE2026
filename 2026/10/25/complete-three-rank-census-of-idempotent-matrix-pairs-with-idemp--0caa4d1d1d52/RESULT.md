# Complete three-rank census of idempotent matrix pairs with idempotent product

## Finding

Fix a finite field \(\mathbb F_q\), where \(q\) is any prime power, and an integer \(n\ge1\). The following gives the complete joint rank distribution for ordered pairs of idempotent matrices \(E,F\in M_n(\mathbb F_q)\) such that their product \(EF\) is also idempotent. **The factors are not required to commute.**

For integers \(m\ge0\) and \(0\le u\le m\), set
\[
 I_q(m,u)={m\brack u}_q q^{u(m-u)},
\]
where \({m\brack u}_q\) is the Gaussian binomial coefficient. Define the zero-product correction
\[
 Z_q(t,k)=\sum_{j=0}^{\min(t,k)}{k\brack j}_q
 \left(\prod_{i=0}^{j-1}(q^t-q^i)\right)q^{t(k-j)}.
\]
An empty product equals \(1\). For prescribed ranks
\[
 \operatorname{rank}E=r,\qquad \operatorname{rank}F=s,\qquad
 \operatorname{rank}(EF)=t,
\]
put \(h=s-t\) and \(k=n-r-s+t\). Their exact number is
\[
 \boxed{N_{n,q}(r,s,t)=I_q(n,r)I_q(r,t)
 {n-r\brack h}_q q^{h k+h(r-t)}Z_q(t,k).}
\]
The formula applies exactly when \(0\le r,s\le n\), \(0\le t\le\min(r,s)\), and \(r+s-t\le n\). All other rank triples occur zero times. Each feasible triple actually occurs.

For comparison, the number of pairs in the same rank stratum satisfying the *stronger* condition \(EF=FE\) is
\[
 \boxed{N^{\mathrm{comm}}_{n,q}(r,s,t)=I_q(n,r)I_q(r,t)I_q(n-r,s-t).}
\]
Thus the exact multiplicative enlargement upon replacing commutativity by mere idempotence of \(EF\) is
\[
 \boxed{\frac{N_{n,q}(r,s,t)}{N^{\mathrm{comm}}_{n,q}(r,s,t)}
 =q^{(s-t)(r-t)}Z_q(t,n-r-s+t).}
\]
For example, over \(\mathbb F_2\), the numbers of all ordered pairs with idempotent product in dimensions \(2,3,4\) are respectively \(58,2608,375244\); the corresponding commuting-pair totals are \(40,1012,65284\).

## Assumptions and scope

All matrices are labeled endomorphisms of the same \(n\)-dimensional vector space over \(\mathbb F_q\), and pairs are **ordered**. Idempotence means \(E^2=E\), \(F^2=F\), and \((EF)^2=EF\). The image rank is ordinary vector-space rank. No restrictions on the field characteristic or on commutativity are imposed. The count is not modulo simultaneous similarity. The formula also extends formally to \(n=0\) with the unique empty matrices, but the statement takes \(n\ge1\).

## Proof

**1. Standardize the first idempotent.** Every rank-\(r\) idempotent \(E\) determines a direct sum \(V=U\oplus W\) with \(U=\operatorname{im}E\), \(W=\ker E\), and \(\dim W=m=n-r\). There are \({n\brack r}_q q^{r(n-r)}=I_q(n,r)\) such \(E\): choose \(U\), then an arbitrary complement. Fix one, and write
\[
 E=\begin{pmatrix}I_U&0\\0&0_W\end{pmatrix},\qquad
 F=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
\]
Since \(EF=\begin{pmatrix}A&B\\0&0\end{pmatrix}\), its idempotence is equivalent to \(A^2=A\) and \(AB=B\). Consequently \(t=\operatorname{rank}A\); there are \(I_q(r,t)\) choices for \(A\). For each choice split \(U=T\oplus L\) into the image and kernel of \(A\), with dimensions \(t\) and \(r-t\), and use \(A=\operatorname{diag}(I_T,0_L)\). Thus \(B:W\to T\), while \(C\) has columns \(C_T:T\to W\) and \(C_L:L\to W\).

**2. Solve the remaining idempotence equations.** Expanding \(F^2=F\) using \(A^2=A\) and \(AB=B\) yields
\[
 B C_T=B C_L=0,\quad BD=0,\quad D C_T=0,\quad
 D C_L=C_L,\quad D^2+C_T B=D.
\]
Multiplication of the last equation by \(D\), using \(DC_T=0\), gives \(D^3=D^2\). Hence \(D^2\) is an idempotent. Set
\[
 H=\operatorname{im}(D^2),\quad K=\ker(D^2),\quad W=H\oplus K.
\]
On \(H\), \(D\) is the identity; on \(K\), the last equation forces \(D=C_T B\). The other equations imply
\[
 B(H)=0,\quad C_T(T)\subseteq K,\quad C_L(L)\subseteq H,
 \quad BC_T=0.
\]
Conversely, choose **any** splitting \(W=H\oplus K\), any linear maps \(C_L:L\to H\), \(C_T:T\to K\), and \(B:K\to T\) satisfying \(BC_T=0\). Extend \(B\) by zero on \(H\), and define \(D=I_H\oplus(C_T B)\). The constraint \(BC_T=0\) makes \((C_T B)^2=0\); substitution verifies every displayed idempotence equation. Thus the parametrization is reversible, not merely surjective.

**3. Determine the rank.** In the preceding splitting, the image of \(F\) is
\[
 \{(v,C_Tv+z):v\in T,\ z\in H\}.
\]
This has dimension \(t+\dim H\), hence \(\operatorname{rank}F=s\) precisely when \(\dim H=h=s-t\). Necessarily \(0\le h\le m\). Put \(k=m-h\). The number of ordered splittings \(W=H\oplus K\) is \({m\brack h}_q q^{hk}\). The map \(C_L:L\to H\) has \(q^{h(r-t)}\) independent choices.

**4. Count the zero-product pairs.** For \(C_T:T\to K\) of rank \(j\), the number of possible maps is
\[
 {k\brack j}_q\prod_{i=0}^{j-1}(q^t-q^i).
\]
Once \(C_T\) is chosen, a map \(B:K\to T\) satisfies \(BC_T=0\) exactly when it annihilates the \(j\)-dimensional image of \(C_T\); it therefore has \(q^{t(k-j)}\) choices. Summing over \(j\) gives \(Z_q(t,k)\). Multiplying the counts in Steps 1–4 proves the main formula and feasibility statement. The unique parametrization proves that there is no overcounting.

**5. Isolate commuting pairs.** The equality \(EF=FE\) holds exactly when the original off-diagonal blocks \(B=C=0\). Then \(A\) and \(D\) are arbitrary idempotents on \(U\) and \(W\), of ranks \(t\) and \(s-t=h\). The count is \(I_q(n,r)I_q(r,t)I_q(m,h)\). Substituting \(I_q(m,h)={m\brack h}_q q^{hk}\) proves both the commuting formula and the ratio. Since \(Z_q(t,k)>0\), every formally feasible triple occurs. \(\square\)

## Verification

The independent standalone script `verify_idempotent_products.py` enumerates all matrices, identifies idempotent factors directly, multiplies them, tests product idempotence, and compares **every** joint rank-stratum count with the formula. Exhaustive cases include \((n,q)=(1,2),(2,2),(3,2),(2,3),(3,3),(2,4),(2,5),(4,2)\). The last case contains \(802\) idempotent matrices and \(375244\) ordered pairs with idempotent product. The extension-field case uses an explicit arithmetic model for \(\mathbb F_4\), not integer arithmetic modulo \(4\). Additional independent integer checks compare the Gaussian formulas and commuting ratios through dimension \(7\) and several field orders. Running `python3 verify_idempotent_products.py` prints `VERIFY_OK_IDEMPOTENT_LINEAR_PRODUCT_RANKS` upon success. Finite checks corroborate, but do not establish, the universal theorem; the proof above provides that justification.

## Relationship to prior work

Erdős studied the existence of products of idempotent matrices, proving that singular matrices admit idempotent factorizations. Laffey continued the factorization theory over Euclidean rings. Alahmadi, Jain, Leroy and Sathaye addressed existence and decomposition questions involving products of idempotents, including nonnegative real matrices. Such results do not by themselves determine a *finite-field joint enumeration* restricted to two idempotent factors whose product is idempotent. The present formula distinguishes the one-sided product-idempotence property from commutativity, with a quantified zero-product correction. It should not be confused with enumeration of commuting idempotents alone or with idempotent–nilpotent factorizations.

An accessible full-text inspection of Erdős and of Alahmadi–Jain–Leroy–Sathaye did not identify the stated three-rank count; only abstract-level material for Laffey was accessible. These comparisons support best-knowledge originality rather than exhaustive priority certification. Analogous counts for total **set transformations** are not a derivation of this vector-space formula, which involves independent extension data and the nontrivial \(BC_T=0\) matrix-pair correction.

## Limitations

The result concerns full matrix monoids over finite fields, labeled ordered pairs, and exactly two idempotents whose product is idempotent. It does not classify simultaneous-similarity orbits, the individual product fibers over a specified idempotent, or products of three or more idempotents. The accessible source corpus may omit an older equivalent calculation, especially in inaccessible factorization literature. No independent mathematical audit has been performed.

## References

1. J. A. Erdős, *On products of idempotent matrices*, Glasgow Mathematical Journal **8** (1967), 118–122, doi:10.1017/S0017089500000173. Full primary text inspected.
2. T. J. Laffey, *Products of idempotent matrices*, Linear and Multilinear Algebra **14** (1983), 309–314, doi:10.1080/03081088308817567. Abstract and bibliographic information inspected; full text not accessible during this review.
3. A. Alahmadi, S. K. Jain, A. Leroy and A. Sathaye, *Decompositions into products of idempotents*, Electronic Journal of Linear Algebra **29** (2015), 74–88, doi:10.13001/1081-3810.2948. Full primary text inspected.
