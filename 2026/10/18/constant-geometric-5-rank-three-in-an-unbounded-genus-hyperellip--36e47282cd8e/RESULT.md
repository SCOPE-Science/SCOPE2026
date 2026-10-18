# Constant geometric \(5\)-rank three in an unbounded-genus hyperelliptic tower

## Finding
For every integer \(r\ge1\), let \(k=\overline{\mathbb F}_5\), and let \(C_r/k\) be the smooth projective model of
\[
y^2=x^{2\cdot3^r+1}+x.
\]
Then \(g(C_r)=3^r\), and the geometric \(5\)-rank of its Jacobian is exactly
\[
f_5(C_r)=\dim_{\mathbb F_5}J(C_r)[5](k)=3.
\]
More precisely, in the standard hyperelliptic differential basis indexed by \(1\le i\le 3^r\), the only basis vectors belonging to the stable image of Cartier are those with odd labels \(t=2i-1\) equal to \(3^{r-1}\), \(3^r\), and \(5\cdot3^{r-1}\). Thus the geometric genus tends to infinity while the \(5\)-rank remains fixed.

## Assumptions and scope
All fields are algebraically closed of characteristic \(5\). Set \(g=3^r\), \(r\ge1\), and \(f(x)=x^{2g+1}+x=x(x^{2g}+1)\). Since \(5\nmid2g\), the polynomial \(f\) is squarefree: it has derivative \(1\) at \(0\), and at a nonzero root of \(x^{2g}+1\) its derivative equals \(-2g\ne0\). It defines a smooth genus-\(g\) hyperelliptic curve. The \(5\)-rank is the rank of a sufficiently high iterate of the semilinear Hasse–Witt/Cartier operator, *not* the rank of one Cartier matrix; the latter determines the \(a\)-number instead.

## Proof
Use \(\omega_i=x^{i-1}dx/y\) for \(1\le i\le g\). In characteristic \(5\), the Cartier–Manin matrix \(A=(c_{5i-j})_{1\le i,j\le g}\) is obtained from
\[
f(x)^{(5-1)/2}=f(x)^2=x^2+2x^{2g+2}+x^{4g+2}.
\]
Thus a nonzero entry \(A_{ij}\) occurs precisely when \(5i-j\) is one of \(2,2g+2,4g+2\); its value is respectively \(1,2,1\), all nonzero. Put \(t_i=2i-1\). Rearranging gives the unique possible transition
\[
t_j\equiv5t_i\pmod{4g},\qquad t_i,t_j\in B_g:=\{1,3,\ldots,2g-1\}.
\]
Because multiplication by \(5\) is a permutation modulo \(4g\), the restriction to \(B_g\) is a partial permutation: every row and every column has at most one nonzero entry. All coefficients lie in \(\mathbb F_5^\times\), so Frobenius twisting does not alter them. Therefore the stable Cartier rank is exactly the number of elements in full multiplication-by-\(5\) cycles that lie entirely in \(B_g\). A partial cycle that exits \(B_g\) contributes zero to the stable image; a full cycle contributes its entire length.

Write \(g=3^r\). If \(t\in B_g\) and \(v_3(t)=k<r\), divide by \(3^k\) and put \(q=r-k\). The multiplication-by-\(5\) orbit of \(t/3^k\) modulo \(4\cdot3^q\) is **every** unit having its fixed congruence class modulo \(4\). Indeed \(5\equiv1\pmod4\), and \(5\) generates \((\mathbb Z/3^q\mathbb Z)^\times\): \(5\) has order \(2\) modulo \(3\), and \(v_3(5^2-1)=1\), yielding order \(2\cdot3^{q-1}\) modulo \(3^q\).

For \(q\ge2\), the orbit cannot stay in the lower half \(1\le u<2\cdot3^q\). To see this, choose in the upper half \(u=2\cdot3^q+v\), where \(v=7\) if the fixed class modulo \(4\) is \(1\), and \(v=1\) if it is \(3\). Both choices satisfy \(2\cdot3^q<u<4\cdot3^q\), \(3\nmid u\), and the required fixed residue modulo \(4\); hence they belong to the full orbit. Such \(t\) gives no stable Cartier contribution.

For \(q=1\), the lower-half units modulo \(12\) are \(1,5\), and they form one complete orbit under multiplication by \(5\); the opposite fixed-modulo-\(4\) orbit \(7,11\) lies in the upper half. This gives precisely \(t=3^{r-1},5\cdot3^{r-1}\). Finally, \(v_3(t)=r\) gives the single lower-half odd label \(t=3^r\), fixed modulo \(4\cdot3^r\) because \(5t-t=4\cdot3^r\). There are no other cases. Therefore exactly three basis labels survive every Cartier iterate, proving \(f_5(C_r)=3\) for all \(r\ge1\).

## Verification
The dependency-free `VERIFY.py` directly expands the three nonzero monomials of \(f^2\), constructs the complete finite Cartier matrix, checks its partial-permutation property, and independently enumerates multiplication-by-\(5\) cycles for \(1\le r\le6\). It obtains stable rank \(3\) and surviving labels \(\{3^{r-1},3^r,5\cdot3^{r-1}\}\) in every tested case, returning `VERIFY_OK`. The unrestricted claim rests on the congruence and primitive-root argument above; checking finitely many genera does not prove it.

## Relationship to prior work
Pan (2026, Theorem 1.2 and Section 3) introduced over \(\mathbb C\) the family \(y^2=x^{12h-5}+x\) to study effective symmetric-group actions and equivariant derived categories. Taking \(h=(3^{r-1}+1)/2\) makes its exponent \(2\cdot3^r+1\); these integer equations admit the smooth reductions considered here. No positive-characteristic \(5\)-rank assertion is made in the originating complex-geometric study. Nourozi–Rahmati–Tafazolian (2019, Section 4 and Theorem 4.1) explicitly study **\(a\)-numbers** of curves of shape \(y^2=x^m+x\) for certain exponents; this is rank of a single Cartier operator, not the stable Frobenius rank computed here. Their general Cartier formula is one of the standard tools used in this proof, and is not claimed as new. Frei (2017, Section 2) also makes the distinction between \(a\)-number and \(p\)-rank explicit. The result refines the arithmetic properties of this natural prime-power subfamily rather than asserting novelty for the general Cartier formula or for the existence of fixed-rank curves in unrelated families.

## Limitations
This describes only the geometric \(5\)-rank of the stated prime-power tower. It does not determine Newton polygons, full Ekedahl–Oort types, isogeny factors, zeta functions, or the \(5\)-rank of all members of Pan's general family. The proof uses no assertion that the complex symmetric-group action specializes intact. Classical cyclic-cover/CM theory may implicitly recover this exact prime-power case; no such explicitly evaluated formula was located in the inspected sources, but unindexed coverage remains possible. Independent replication of the specific arithmetic conclusion is an open validation task.

## References
- Shengyong Pan, *Counterexamples to the Polishchuk–Van den Bergh conjecture on curves*, arXiv:2610.10147v1 (first public 2026-10-07), Theorem 1.2 and Section 3, https://arxiv.org/html/2610.10147v1 .
- Vahid Nourozi, Farhad Rahmati, Saeed Tafazolian, *The a-number of Certain Hyperelliptic Curves*, arXiv:1902.03672v2, Section 4 and Theorem 4.1, https://arxiv.org/abs/1902.03672 .
- Sarah Frei, *The a-number of hyperelliptic curves*, arXiv:1703.03516v2, Section 2, https://arxiv.org/html/1703.03516v2 .
- Noriko Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, Journal of Algebra 52 (1978), 378–410.
