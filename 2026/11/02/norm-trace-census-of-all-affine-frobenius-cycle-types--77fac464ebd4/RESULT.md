# Norm–trace census of all affine Frobenius cycle types

## Finding
For a prime \(p\), integers \(m,r\ge1\), and coefficients \(a\in\mathbb F_{p^m}^{\times}\), \(b\in\mathbb F_{p^m}\), consider the permutation \(f_{a,b}(x)=a x^{p^r}+b\). Put \(g=\gcd(m,r)\), \(Q=p^g\), \(q=p^m\), \(h=m/g\), and let \(\sigma:x\mapsto x^{p^r}\). Its fixed field is \(F=\mathbb F_Q\). For every integer \(n\ge1\), put \(d=\gcd(n,h)\).

Let \(A=N_{\mathbb F_q/F}(a)\). If \(A\ne1\), write \(t=\operatorname{ord}_{F^{\times}}(A)>1\). Then the number of fixed points of the \(n\)-th iterate is
\[
F_t(n)=1+(Q^d-1)\mathbf1_{t\mid n/d}.
\]
If \(A=1\), choose \(u\in\mathbb F_q^{\times}\) with \(a\sigma(u)=u\), and define \(\theta=\operatorname{Tr}_{\mathbb F_q/F}(b/u)\). Whether \(\theta=0\) is independent of the choice of \(u\). The two remaining fixed-point laws are
\[
F_{0}(n)=Q^d\qquad(\theta=0),\qquad
F_{*}(n)=Q^d\mathbf1_{p\mid n/d}\qquad(\theta\ne0).
\]
For each of these laws \(F_{\lambda}\) and every \(\ell\ge1\), the **exact number of cycles of length \(\ell\)** is
\[
C_{\lambda}(\ell)=\frac1\ell\sum_{j\mid\ell}\mu(\ell/j)F_{\lambda}(j).
\]
Only lengths dividing \(ht\), \(h\), or \(ph\), respectively, can occur.

All distinct possible graph isomorphism types are precisely one type for each divisor \(t>1\) of \(Q-1\), and two types for \(A=1\). Their coefficient-pair multiplicities are, respectively,
\[
\begin{aligned}
M_t&=q\,\varphi(t)\frac{q-1}{Q-1}&&(t>1,\ t\mid Q-1),\\
M_0&=\frac{q-1}{Q-1}\frac qQ,\\
M_*&=\frac{q-1}{Q-1}\frac{q(Q-1)}Q.
\end{aligned}
\]
Consequently the family contains exactly \(d_{\mathrm{div}}(Q-1)+1\) cycle-graph types, where \(d_{\mathrm{div}}(N)\) counts the positive divisors of \(N\), and the displayed multiplicities sum to \(q(q-1)\).

## Assumptions and scope
All parameters \(p,m,r,a,b\) range as above, without restrictions on characteristic or divisibility of \(h\) by \(p\). The norm and trace are the standard relative field norm and trace. The indicator \(\mathbf1_P\) equals one if \(P\) holds and zero otherwise. A cycle-graph type means an isomorphism class of finite directed functional graphs, equivalently a cycle-length multiset or symmetric-group conjugacy class. The coefficient pairs \((a,b)\) are distinct as polynomial functions because the exponent map \(\sigma\) is a bijection and \(f_{a,b}(0)=b\). The symbol \(\mu\) is the Möbius function, and \(\varphi\) is Euler's totient.

## Proof
**1. The semilinear part and its fixed subfields.** Since \(\gcd(r/g,m/g)=1\), \(\sigma\) generates the cyclic Galois group \(\operatorname{Gal}(\mathbb F_q/F)\) of order \(h\). Write \(L(x)=a\sigma(x)\). Repeated composition gives \(L^h(x)=Ax\). The field fixed by \(\sigma^n\) has order \(Q^d\), where \(d=\gcd(n,h)\), and \(\sigma^n\) generates its relative Galois group of order \(h/d\).

**2. Nontrivial norm.** If \(A\ne1\), then \(L-I\) has zero kernel: from \(L(x)=x\) with \(x\ne0\), iterating \(h\) times would give \(Ax=x\), contradiction. Thus the affine map \(f=L+b\) has a unique fixed point, so a translation conjugates it to \(L\). Write \(L^n(x)=a_n\sigma^n(x)\), where \(a_n=\prod_{j=0}^{n-1}\sigma^j(a)\). The relative norm to the fixed field of \(\sigma^n\) is
\[
N_{\mathbb F_q/\mathbb F_{Q^d}}(a_n)=A^{n/d},
\]
because \((L^n)^{h/d}=(L^h)^{n/d}\) and its scalar coefficient is exactly this relative norm. The multiplicative form of Hilbert's Theorem 90 states that \(a_n\sigma^n(x)=x\) admits a nonzero solution exactly when this norm is one; in that event the solution space is a one-dimensional \(\mathbb F_{Q^d}\)-space and has \(Q^d\) elements. Otherwise only zero is fixed. Since \(A\) has order \(t\), the result is \(F_t(n)=1+(Q^d-1)\mathbf1_{t\mid n/d}\).

**3. Norm one.** If \(A=1\), multiplicative Hilbert 90 supplies \(u\ne0\) satisfying \(a\sigma(u)=u\). Conjugating by multiplication by \(u\) gives \(T(y)=\sigma(y)+c\), where \(c=b/u\). Another admissible \(u\) differs by an element of \(F^{\times}\); it rescales \(\operatorname{Tr}(c)\) without changing whether it vanishes. The \(n\)-th iterate is \(T^n(y)=\sigma^n(y)+S_n(c)\), with \(S_n(c)=\sum_{j=0}^{n-1}\sigma^j(c)\). The additive Hilbert-90 identity \(\operatorname{im}(\sigma^n-I)=\ker\operatorname{Tr}_{\mathbb F_q/\mathbb F_{Q^d}}\) shows that the fixed-point equation is solvable exactly when
\[
0=\operatorname{Tr}_{\mathbb F_q/\mathbb F_{Q^d}}S_n(c)
=(n/d)\operatorname{Tr}_{\mathbb F_q/F}(c)
=(n/d)\theta.
\]
The middle identity follows by expanding both traces: every element of the cyclic Galois group occurs exactly \(n/d\) times. When solvable, solutions form an affine coset of the \(Q^d\)-element fixed field. Therefore \(F_0(n)=Q^d\) if \(\theta=0\), and \(F_*(n)=Q^d\mathbf1_{p\mid n/d}\) otherwise.

**4. Complete cycle spectra and distinctness.** For any permutation, the number of points fixed by its \(n\)-th iterate equals \(\sum_{\ell\mid n}\ell C(\ell)\); Möbius inversion yields the stated formula. The order of \(L\) with \(A\ne1\) is exactly \(ht\): if \(L^n=I\), evaluating at one forces \(a_n=1\) and therefore \(\sigma^n=I\), so \(h\mid n\), after which \(A^{n/h}=1\) forces \(t\mid n/h\). For \(A=1,\theta=0\), a translation conjugates \(T\) to \(\sigma\), giving order exactly \(h\). For \(A=1,\theta\ne0\), \(T^h(y)=y+\theta\), so its order is exactly \(ph\). Since every \(t\mid Q-1\) is coprime to \(p\), these orders are all distinct. Thus the types listed are pairwise distinct and exhaust the coefficient family.

**5. Parameter multiplicities.** The norm \(\mathbb F_q^{\times}\to F^{\times}\) is onto, with each fiber containing \((q-1)/(Q-1)\) elements. Exactly \(\varphi(t)\) elements of \(F^{\times}\) have order \(t\), and each such \(a\) allows \(q\) arbitrary \(b\), proving \(M_t\). For norm-one \(a\), multiplication by \(u^{-1}\) bijects all \(b\) with \(c\). The field trace is surjective with a kernel of size \(q/Q\), so \(q/Q\) values of \(b\) produce \(\theta=0\), while \(q(Q-1)/Q\) produce \(\theta\ne0\). This proves \(M_0,M_*\). Summing uses \(\sum_{t\mid Q-1}\varphi(t)=Q-1\); the type count is \(d_{\mathrm{div}}(Q-1)+1\).

## Verification
Running `python3 affine_frobenius_verifier.py` (Python standard library only) constructs finite fields independently, iterates every one of the \(q(q-1)\) affine maps for fifteen parameter triples, enumerates their entire cycle graphs, and compares every cycle count and each coefficient-class frequency against the formulas. It also checks class distinctness. It exhaustively covers \(28{,}076\) coefficient-pair cases (counted by parameter triple) and reports `VERIFY_OK all_cases= 15 all_affine_maps= 28076`. This finite calculation is supporting evidence; the preceding Hilbert-90 proof establishes the theorem for all parameters.

## Relationship to prior work
Mullen, Muratović-Ribić and Wang (2015) give general coefficient matrices for polynomial composition and relate cycle periods to matrix orders, but do not tabulate norm–trace cycle types and their coefficient multiplicities. Ugolini (2020) analyzes the same affine Frobenius form in characteristic two and therefore covers substantial characteristic-two dynamic behavior; the present all-prime coefficient census should not be construed as making those known binary cases new. Bian, Chen and Zheng (2026) prove cycle formulas for general linearized permutations, which already imply the cycle spectra here when the affine map is conjugate to a linear map; their result does not enumerate all translated coefficient pairs by type or treat the no-fixed-point branch explicitly. Gerike and Kyureghyan (2020) classify a different family of trace-type permutations via invariant affine lines. The specific combined norm–trace coefficient census and exact count of cycle-graph types were not found in the inspected sources; broader historical priority is not independently certified.

## Limitations
The classification is restricted to a single Frobenius monomial plus an affine constant, not arbitrary sums of linearized monomials. It determines symmetric-group cycle-graph equivalence, not conjugacy in the smaller affine semilinear group. Standard Hilbert-90 input is invoked rather than reproved. Closely related general matrix theorems may yield parts of the formulas after specialization, and unexamined older literature could contain the complete coefficient census. Independent mathematical audit has not been performed.

## References
1. G. L. Mullen, A. Muratović-Ribić, Q. Wang, *On coefficients of powers of polynomials and their compositions over finite fields*, arXiv:1503.07487, first posted 2015-03-25 (MSC 11T06).
2. S. Ugolini, *On the iterations of the maps \(a x^{2^k}+b\) and \((a x^{2^k}+b)^{-1}\) over finite fields of characteristic two*, arXiv:2008.07337, first posted 2020-08-17.
3. H. Bian, S. Chen, D. Zheng, *Cycle structures and parities of linearized permutation polynomials*, arXiv:2610.11574, first posted 2026-10-08.
4. D. Gerike, G. M. Kyureghyan, *Permutations on finite fields with invariant cycle structure on lines*, Designs, Codes and Cryptography (2020), DOI:10.1007/s10623-020-00721-2.
5. G. L. Mullen, T. P. Vaughan, *Cycles of linear permutations over a finite field*, Linear Algebra and its Applications (1988), DOI:10.1016/0024-3795(88)90179-6.
