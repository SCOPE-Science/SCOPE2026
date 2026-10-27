# Frobenius-orbit rank spectra of finite Alexander quandle algebras

## Finding

Let \(A\) be a finite abelian group of cardinality \(N\), let \(\varphi\in\operatorname{Aut}(A)\), and let \(E=\mathbb F_q[\operatorname{Alex}(A,\varphi)]\) be the (generally nonassociative) quandle algebra whose basis products are \(e_x*e_y=e_{\varphi(x)+(1-\varphi)(y)}\). Assume \(\operatorname{char}\mathbb F_q\nmid N\). Define \(B=(1-\varphi)A\), \(r=|B|\), and \(f=N/r=|\ker(1-\varphi)|\).

For the character group \(\widehat B\) over an algebraic closure of \(\mathbb F_q\), let \(\mathcal O\) be the collection of orbits of the \(q\)-power Frobenius map, and write \(d_O=|O|\). For \(u\in E\), let \(L_u(v)=u*v\) and \(R_u(v)=v*u\), with ranks taken over \(\mathbb F_q\). Their **complete rank-distribution polynomials** are

\[
\boxed{\sum_{u\in E}t^{\operatorname{rank}L_u}=\prod_{O\in\mathcal O}\left(1+(q^{f d_O}-1)t^{d_O}\right)}
\]

and

\[
\boxed{\sum_{u\in E}t^{\operatorname{rank}R_u}=q^{N-r}\prod_{O\in\mathcal O}\left(1+(q^{d_O}-1)t^{f d_O}\right).}
\]

Consequently, the number of **ordered pairs**, including zero elements, satisfying \(u*v=0\) is

\[
\boxed{Z(E)=|\{(u,v)\in E^2:u*v=0\}|=q^{N-r}\prod_{O\in\mathcal O}\left(q^{d_O}+q^{f d_O}-1\right).}
\]

The number of ordered zero-product pairs with both factors nonzero is \(Z(E)-2q^N+1\), and the zero-product probability for independent uniform \(u,v\) is \(Z(E)/q^{2N}\). In particular, these entire spectra depend only on the coefficient-field order, \(N\), and the abstract isomorphism class of the displacement subgroup \(B\), not on other data of \(\varphi\).

If the field contains all roots of unity of orders dividing \(\exp(B)\), every orbit has size one. Then the formulas simplify to

\[
\sum_{u\in E}t^{\operatorname{rank}L_u}=(1+(q^f-1)t)^r,\quad
\sum_{u\in E}t^{\operatorname{rank}R_u}=q^{N-r}(1+(q-1)t^f)^r,\quad
Z(E)=q^{N-r}(q+q^f-1)^r.
\]

For a latin Alexander quandle, \(f=1\), so the left and right rank distributions agree. For a nonlatin quandle, left ranks cannot exceed \(r\), whereas right ranks can attain \(N\); this displays a systematic asymmetry.

## Assumptions and scope

The group \(A\) is arbitrary finite abelian (not necessarily cyclic), \(\varphi\) is any automorphism, and \(q\) is any prime power coprime to \(N\). We require neither the latin property nor that \(\mathbb F_q\) split the characters of \(A\). The algebra multiplication is exactly \(e_x*e_y=e_{\varphi(x)+(1-\varphi)(y)}\), so left and right operators must not be interchanged. The characteristic-coprimality assumption guarantees Fourier invertibility; no formula is asserted here in the modular case.

If \(m\) ranges over the positive divisors of \(\exp(B)\), let \(n_B(m)\) be the number of characters of exact order \(m\), and define \(d_m=\operatorname{ord}_m(q)\) for \(m>1\) and \(d_1=1\). Each displayed product may equivalently be taken over \(m\), raising its \(d_m\)-factor to the exponent \(n_B(m)/d_m\). This gives the formulas directly from invariant factors of \(B\), without constructing the character group explicitly.

## Proof

**1. Fourier multiplication.** Work temporarily over \(\overline{\mathbb F}_q\). Since \(N\) is invertible, the finite Fourier transform \(\widehat u(\chi)=\sum_{x\in A}u_x\chi(x)\) is an invertible linear transformation from \(E\) to functions on \(\widehat A\). Put \(\Phi(\chi)=\chi\circ\varphi\) and \(\Psi(\chi)=\chi\circ(1-\varphi)\). Directly expanding the basis multiplication gives

\[
\widehat{u*v}(\chi)=\widehat u(\Phi\chi)\,\widehat v(\Psi\chi).
\]

This is the established Fourier multiplication identity, not a new part of the result. The map \(\Phi\) permutes \(\widehat A\); the map \(\Psi\) has a kernel of size \(f\) and an image \(I\) of size \(r\). More precisely, \(I\) consists of the characters trivial on \(\ker(1-\varphi)\), canonically identified via \(1-\varphi\) with \(\widehat B\). The identification commutes with Frobenius \(\chi\mapsto\chi^q\).

**2. Left ranks.** For fixed \(u\), the Fourier-coordinate matrix of \(L_u\) maps the single input coordinate indexed by \(\eta\in I\) to the vector with coordinates \(\widehat u(\Phi\chi)\) for \(\chi\in\Psi^{-1}(\eta)\). Different \(\eta\) have disjoint row supports. Thus

\[
\operatorname{rank}L_u=\#\{\eta\in I:\widehat u\text{ is nonzero somewhere on }\Phi(\Psi^{-1}(\eta))\}.
\]

Every fiber contains \(f\) Fourier coordinates, and the disjoint fibers partition \(\widehat A\). Fix a Frobenius orbit \(O\subset I\) of size \(d_O\). Its union of \(f\)-element fibers contains \(f d_O\) character coordinates and is Frobenius-stable. Fourier vectors defined over \(\mathbb F_q\) are precisely those satisfying \(\widehat u(\chi^q)=\widehat u(\chi)^q\); the admissible assignments on this Frobenius-stable union form an \(\mathbb F_q\)-vector space of dimension \(f d_O\). Exactly one assignment is identically zero, whereas every other assignment activates every \(\eta\in O\) and contributes \(d_O\) to the rank. Independent orbit unions give the first product formula.

**3. Right ranks.** In the Fourier-coordinate matrix of \(R_u\), the \(\chi\)-row is \(\widehat u(\Psi\chi)\) times the unique input coordinate indexed by \(\Phi\chi\). Since \(\Phi\) is bijective, all nonzero rows are independent. Hence

\[
\operatorname{rank}R_u=f\,\#\{\eta\in I:\widehat u(\eta)\ne0\}.
\]

The \(N-r\) Fourier coordinates outside \(I\) are unconstrained and account for \(q^{N-r}\) choices. On a Frobenius orbit \(O\subset I\) of length \(d_O\), the values of \(\widehat u\) give one zero choice or \(q^{d_O}-1\) nonzero choices, contributing rank zero or \(f d_O\), respectively. This yields the second product formula.

**4. Zero products.** The kernel of \(L_u\) has dimension \(N-\operatorname{rank}L_u\). Therefore

\[
Z(E)=\sum_{u\in E}q^{N-\operatorname{rank}L_u}=q^N\prod_{O\in\mathcal O}\left(1+(q^{f d_O}-1)q^{-d_O}\right).
\]

There are \(\sum_Od_O=r\) characters in \(I\). Multiplying out the powers of \(q\) gives the claimed integer product \(q^{N-r}\prod_O(q^{d_O}+q^{f d_O}-1)\). The count with both factors nonzero follows by excluding the \(2q^N-1\) ordered pairs having at least one zero factor.

**5. Arithmetic description and invariance.** Every character of exact order \(m\) has Frobenius orbit length \(d_m\). Such characters contribute \(n_B(m)/d_m\) orbits, where \(n_B(m)=\sum_{d\mid m}\mu(m/d)|B[d]|\) and \(B[d]=\{b\in B:db=0\}\). Thus the orbit multiset is determined by the abstract group \(B\), and all three formulas depend only on \(N\), \(B\), and \(q\). This completes the proof.

Ranks computed after extension to the algebraic closure are unchanged because nonzero minors and vanishing minors are preserved under a field extension; the Frobenius-compatible assignment count converts the results back to \(\mathbb F_q\).

## Verification

The accompanying dependency-free Python 3 program `verify.py` independently constructs multiplication matrices from the defining quandle operation and computes every left and right matrix rank over the specified coefficient field. It enumerates all elements for eight nontrivial cyclic prime-field tests (plus the one-element case), three tests over the nonsplit/split extension field \(\mathbb F_4\), and three noncyclic tests on \(C_3\times C_3\), including a nonlatin case. Each exhaustive test checks every coefficient vector, both rank-distribution polynomials, and \(\sum_u q^{N-\operatorname{rank}L_u}\) against the claimed pair count. An additional larger prime-field parameter is checked symbolically by matching counts rather than exhaustively.

A key nonlatin, noncyclic example is \(A=C_3\times C_3\), \(\varphi(x,y)=(x,-y)\), and \(q=2\). Here \(N=9\), \(r=3\), \(f=3\), and the Frobenius orbit lengths are \(1,2\). The theorem yields

\[
\sum_u t^{\operatorname{rank}L_u}=(1+7t)(1+63t^2),\qquad
\sum_u t^{\operatorname{rank}R_u}=64(1+t^3)(1+3t^6),\qquad Z(E)=38592.
\]

Full enumeration over all \(512\) algebra elements verifies these three identities. A nonsplit latin example is \(A=C_5\), \(\varphi(x)=2x\), \(q=2\), with Frobenius orbit sizes \(1,4\) and \(Z(E)=93\). Exhaustive computations support, but do not replace, the unrestricted proof.

Reproduce from the two supplied files by running `python3 verify.py` in a directory containing the script; the expected terminal marker is `VERIFY_OK`.

## Relationship to prior work

The Fourier identity used in the proof is Proposition 5.1 of Lực Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1 (14 October 2026). That paper proves structural zero-divisor and augmentation statements and develops a Fourier approach to finite Alexander quandle rings; the exact all-element left/right rank distributions and ordered zero-product count here are separate, quantitative statements. The identity was previously established in the latin setting by Elhamdadi, Ta, and Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1. The original quandle-ring zero-divisor theory of Bardakov, Passi, and Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843, concerns existence and orderability rather than these finite-field counts. Churchill, Churchill, Fernando, and Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1, calculates zero-divisor graphs of particular extended quandle rings, a different construction from the algebra \(E\) considered here.

This result does not claim the Fourier identity, elementary finite-field character theory, or individual special-case counts as novel. Its subject is their complete synthesis into explicit rank enumerators and a uniform zero-product census for finite **nonlatin as well as latin** Alexander quandles over arbitrary semisimple-characteristic coefficient fields.

## Limitations

The formulas require \(\operatorname{char}\mathbb F_q\nmid |A|\); in defining characteristic, the Fourier decomposition used here is not invertible. The results count ordered zero products and multiplication-map ranks, not isomorphism classes of quandles or their algebras. Distinct \(\varphi\) with the same displacement subgroup may have equal enumerators without yielding isomorphic quandles. Existing general Fourier-coordinate methods may already make parts of the enumeration an implicit consequence; a comprehensive survey of all unpublished or unindexed literature is not asserted. No independent mathematical audit has been performed.

## References

1. Lực Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1, 14 October 2026. Full text: https://arxiv.org/html/2610.20306v1 (especially Proposition 5.1 and Sections 4–6).
2. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1, 3 September 2026. Full text: https://arxiv.org/html/2609.03799v1 (especially Theorem 3.2).
3. V. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (2020); *Osaka Journal of Mathematics* **59** (2022), 611–637. Preprint: https://arxiv.org/abs/2001.06843.
4. M. Churchill, L. Churchill, K. Fernando, and S. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1, 10 August 2026. Full text: https://arxiv.org/html/2608.09149v1 (especially Section 6).
