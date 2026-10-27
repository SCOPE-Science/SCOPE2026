# Cyclotomic nilpotency asymmetry of multiplication operators in odd dihedral quandle algebras

## Finding
Fix an odd integer \(n\ge3\) and a prime power \(q=p^e\). In the dihedral quandle algebra \(A=\mathbb F_q[R_n]\), take the basis \(e_i\) for \(i\in\mathbb Z/n\mathbb Z\), with multiplication \(e_i e_j=e_{2j-i}\). Define \(L_a(v)=av\) and \(R_a(v)=va\). Although \(\operatorname{rank}L_a=\operatorname{rank}R_a\) for **every** \(a\in A\), their nilpotency frequencies can differ, and both are determined exactly by cyclotomic orbit products.

Write \(n=p^s m\), with \(p\nmid m\), and factor \(X^m-1=\prod_{j\in I}f_j(X)\) into distinct monic irreducible polynomials over \(\mathbb F_q\), with \(d_j=\deg f_j\). The substitutions \(X\mapsto X^2\) and \(X\mapsto X^{-1}\) permute the index set \(I\); denote the cycles by \(\mathcal C_2\) and \(\mathcal C_{-1}\), respectively. Along any cycle \(C\), all factors have a common degree \(d_C\). Then the exact counts of \(a\in A\) having nilpotent left and right multiplication operators are
\[
N_L(n,q)=q^{n-m}\prod_{C\in\mathcal C_2}\left(q^{d_C|C|}-(q^{d_C}-1)^{|C|}\right),\qquad
N_R(n,q)=q^{n-m}\prod_{C\in\mathcal C_{-1}}\left(q^{d_C|C|}-(q^{d_C}-1)^{|C|}\right).
\]
These formulas include the modular case \(p\mid n\) and all finite extension fields. The counts concern **nilpotency of the linear operators**, not any ambiguous notion of a nonassociative power of \(a\).

For \((n,q)=(5,11)\), \(N_L=4641\) and \(N_R=441\). For \((n,q)=(7,2)\), the asymmetry reverses: \(N_L=1\) and \(N_R=15\). In both examples every individual left/right multiplication pair nevertheless has equal rank.

## Assumptions and scope
The algebra is the finite-field linearization of the standard odd dihedral quandle. No restrictions besides \(n\ge3\) odd and \(q\) a prime power are imposed. The zero linear operator counts as nilpotent. The finite-field characteristic is \(p\), and \(s\ge0\) is maximal with \(p^s\mid n\). The cycles are **cycles on distinct irreducible factors**, not on arbitrary polynomial roots. Their index-label direction is immaterial to cycle lengths.

## Proof
Identify the underlying vector space with \(B=\mathbb F_q[X]/(X^n-1)\) by \(e_i\leftrightarrow X^i\). Directly from \(e_i e_j=e_{2j-i}\), bilinearity gives the transported product \(f\star g=f(X^{-1})g(X^2)\). Consequently, with \(\sigma_u(f)(X)=f(X^u)\), ordinary multiplication \(M_b\) in \(B\) gives
\[
L_a=M_{\sigma_{-1}(a)}\sigma_2,\qquad R_a=M_{\sigma_2(a)}\sigma_{-1}.
\]
Both \(\sigma_2\) and \(\sigma_{-1}\) are automorphisms because \(n\) is odd. Therefore both multipliers have the rank of ordinary multiplication by \(a\); this proves the pointwise rank statement. The transported product itself is known in prior Alexander-quandle work and is not claimed as new.

We establish the following linear-algebra lemma. Let \(B\) be a finite commutative ring, \(J\) its nilpotent radical, and \(\sigma\) a ring automorphism which permutes the field factors of \(B/J=\prod_{j\in I}K_j\). For \(b\in B\), the linear map \(T=M_b\sigma\) is nilpotent if and only if the image of \(b\) has **at least one zero coordinate on every \(\sigma\)-orbit of field factors**. To prove necessity, on an orbit all of whose coordinates of \(b\) are nonzero, \(T\) is a bijective weighted permutation of the corresponding nonzero quotient vector space, so no power vanishes. For sufficiency, let \(h\) be the order of the permutation of factor indices. The map \(T^h\) preserves every factor and acts by multiplication by the product of the appropriately transported \(b\)-coordinates, followed by the factorwise automorphism \(\sigma^h\). If the original cycle has a zero, the multiplier is zero on every quotient coordinate in that cycle; hence \(T^h\) vanishes on \(B/J\). Thus \(T^h(B)\subseteq J\). Because \(T\) preserves each radical power \(J^k\), and because its induced action on each successive radical layer is given by the same product of \(b\)-coefficients, alternatively use the exact expression \(T^{h}=M_{b\sigma(b)\cdots\sigma^{h-1}(b)}\sigma^h\) to see the multiplier belongs to \(J\). Repeating \(T^h\) exactly \(p^s\) times gives multiplication by a product of \(p^s\) radical elements, hence zero because \(J^{p^s}=0\). This proves nilpotence without assuming semisimplicity.

For the present ring \(B\), the identity \(X^n-1=(X^m-1)^{p^s}\) gives \(J^{p^s}=0\), \(B/J\cong\prod_{j\in I}\mathbb F_{q^{d_j}}\), and the reduction map \(B\to B/J\) has \(q^{n-m}\) elements in every fiber. A cycle of length \(\ell\) and factor degree \(d\) has \(q^{d\ell}\) possible residue assignments, with exactly \((q^d-1)^\ell\) all-nonzero assignments. Therefore exactly \(q^{d\ell}-(q^d-1)^\ell\) assignments satisfy the lemma on that cycle. Multiply independently over cycles and by the uniform fiber size. For left multiplication \(b=\sigma_{-1}(a)\), the factor permutation is \(\sigma_2\); for right multiplication \(b=\sigma_2(a)\), it is \(\sigma_{-1}\). Both changes from \(a\) to \(b\) are bijections, giving the displayed formulas.

In the \((5,11)\) example, the five linear factors correspond to fifth roots: squaring has a fixed trivial orbit and one 4-cycle, whereas inversion has a fixed trivial orbit and two 2-cycles. Hence \(N_L=11^4-10^4=4641\) and \(N_R=(11^2-10^2)^2=441\). For \((7,2)\), the irreducible degrees are \(1,3,3\); squaring fixes all three factor labels (yielding \(N_L=1\)), and inversion exchanges the two cubic factors (yielding \(N_R=2\cdot 2^3-1=15\)).

## Verification
The independent standalone checker `nil_checker.py` builds the actual \(n\times n\) multiplication matrices using the quandle basis product, exponentiates them by finite-field matrix multiplication, and compares nilpotency of the matrices against the cyclotomic orbit formula. Its exhaustive configurations span \(q=2,3,4,5,7,8,9\) and \(n=3,5,7,9\), totaling 3,683 examined elements; at \((5,11)\), 100 further direct-matrix comparisons against the residue criterion pass and both exact counts are independently computed by finite-field factor permutations. The supporting `verify.py` independently checks left/right rank equality and polynomial gcd ranks, exhaustively over further small fields and sizes. All results and inputs are in the bundled code and text outputs. These finite checks corroborate the symbolic proof; no finite experiment is used to establish a universal claim.

## Relationship to prior work
The underlying quandle-ring construction and the study of zero divisors come from the established quandle-ring literature [1,2]. In particular, Zhang [4, Proposition 2.1] already writes the Alexander quandle product as a group-ring transport, and [4, Proposition 5.1 and Theorem 5.5] gives Fourier-coordinate treatments and **Peirce spectra for right multiplication by nonzero idempotents over \(\mathbb C\)**. Those transport and Fourier facts are acknowledged as prior work. The present statement instead counts *all coefficients yielding nilpotent left or right multiplication* over **every finite field, including inseparable modular group algebras**, and proves the direction-dependent disparity despite pointwise equality of ranks. The earlier quandle zero-divisor work [2] does not state this enumeration. Equivalent statements in general twisted group-algebra or finite-ring literature are a residual priority risk.

## Limitations
These formulas classify only whether the operators are nilpotent, not their full Jordan types or least nilpotency indices. Their proofs do not assert originality of the group-ring transport, of the factorization of \(X^m-1\), or of general counting of nonzero tuples. No independent mathematical audit has been performed. A related newer full text [5] treats other zero-divisor structures; completeness of novelty discovery cannot be guaranteed.

## References
[1] V. Bardakov and M. Elhamdadi, *Ring theoretic aspects of quandles*, arXiv:1805.05908 (first posted 2018-05-15), https://arxiv.org/abs/1805.05908.

[2] V. Bardakov and collaborators, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (first posted 2020-01-19), https://arxiv.org/abs/2001.06843.

[3] *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257 (2022), https://arxiv.org/abs/2207.09257.

[4] Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (2026), https://arxiv.org/pdf/2610.08204.

[5] *A further study of quandles and quandle rings*, arXiv:2608.09149 (2026), https://arxiv.org/abs/2608.09149.
