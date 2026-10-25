# Exact finite-field idempotent count for odd dihedral quandle algebras

## Finding

For every odd integer \(n\ge 3\) and every finite field \(\mathbb F_q\) whose characteristic does not divide \(n\), consider the (generally nonassociative) quandle algebra \(\mathbb F_q[R_n]\). Its distinguished basis is \(\{e_i:i\in\mathbb Z/n\mathbb Z\}\), with multiplication \(e_i e_j=e_{2j-i}\), subscripts understood modulo \(n\). An **idempotent** means an element \(u\) satisfying \(u^2=u\), including zero.

For each divisor \(t>1\) of \(n\), define the following finite arithmetic data:

* \(d_t\) is the multiplicative order of \(2\) modulo \(t\), and \(H_t=\langle 2,-1\rangle\le (\mathbb Z/t\mathbb Z)^\times\).
* If \(-1\in\langle 2\rangle\pmod t\), then \(d_t\) is even, \(|H_t|=d_t\), and \(N_t=2^{d_t/2}+1\). Otherwise \(|H_t|=2d_t\) and \(N_t=2^{d_t}-1\).
* There is a canonical injective homomorphism \(\rho_t:H_t\longrightarrow(\mathbb Z/N_t\mathbb Z)^\times\) with \(\rho_t(2)=2\) and \(\rho_t(-1)=-1\). In the first case \(\rho_t(2^{j})=2^j\), and in the second \(\rho_t(\pm2^j)=\pm2^j\), with exponents interpreted modulo \(N_t\). The statements here refer to residue classes.
* Let \(e_t\) be the order of the coset of \(q\) in \((\mathbb Z/t\mathbb Z)^\times/H_t\), let \(h_t=q^{e_t}\pmod t\in H_t\), and choose any integer \(a_t\) representing \(\rho_t(h_t)\pmod{N_t}\).
* Put \(g_t=\gcd(N_t,q^{e_t}-a_t)\) and \(c_t=\varphi(t)/(e_t|H_t|)\), where \(\varphi\) is Euler's totient function. The integer \(g_t\) is independent of the chosen representative \(a_t\).

**Theorem.** The full number of idempotents (zero included) is

\[
\boxed{\bigl|\{u\in\mathbb F_q[R_n]:u^2=u\}\bigr|
=2\prod_{\substack{t\mid n\\t>1}}(1+g_t)^{c_t}.}
\]

The proof also gives a complete parametrization: one independent binary choice at Fourier frequency zero and, for each of the \(c_t\) Frobenius orbits of \(H_t\)-cosets of frequencies of additive order \(t\), one independent choice of zero or an element of the cyclic group of \(g_t\)-th roots of unity.

For example, the exact counts over \(\mathbb F_2\) at \(n=9,15,17,21\) are respectively \(80,768,648,4096\); for \(n=11\) they are \(68\) over \(\mathbb F_2\) but \(24\) over \(\mathbb F_3\). The last comparison exhibits arithmetic sensitivity beyond quandle size alone.

## Assumptions and scope

The parameter \(n\) is odd and at least \(3\); \(q\) is any prime power with \(\gcd(q,n)=1\). This ensures that \(2\) and \(q\) act invertibly on all residue groups above and, crucially, that the Fourier transform on \(\mathbb Z/n\mathbb Z\) is invertible in characteristic \(\operatorname{char}\mathbb F_q\). Neither associative multiplication nor a power-associative convention is assumed: only the explicit bilinear product and the unambiguous equation \(u^2=u\) are used. All counts include the zero idempotent.

The case \(\operatorname{char}\mathbb F_q\mid n\) is **not claimed**, because ordinary semisimple Fourier inversion fails there. The necessity of distinguishing that regime is illustrated by previously reported characteristic-three behavior of \(R_3\).

## Proof

**1. Fourier idempotence equations.** Let \(f=\operatorname{ord}_n(q)\) and \(E=\mathbb F_{q^f}\); then \(E\) contains a primitive \(n\)-th root of unity \(\zeta\). Write \(u=\sum_{i\in\mathbb Z/n\mathbb Z}b_i e_i\) and define \(y_r=\sum_i b_i\zeta^{ri}\) for each residue \(r\pmod n\). The coefficient of \(e_k\) in \(u^2\) is \(\sum_{2j-i=k}b_i b_j\). Consequently,

\[
\widehat{u^2}(r)=\sum_{i,j}b_i b_j\zeta^{r(2j-i)}=y_{2r}y_{-r}.
\]

Since \(n\) is invertible in \(E\), Fourier inversion proves that \(u^2=u\) is equivalent to

\[y_r=y_{2r}y_{-r}\quad\text{for every }r\in\mathbb Z/n\mathbb Z.\tag{1}\]

The condition \(b_i\in\mathbb F_q\) is equivalent to \(y_{qr}=y_r^q\) for every \(r\), because the inverse transform also commutes with Frobenius. At \(r=0\), equation (1) says \(y_0^2=y_0\), giving exactly \(y_0=0\) or \(1\).

**2. Solve a nonzero-frequency orbit over \(E\).** The nonzero residues split according to additive order \(t\mid n\), \(t>1\). Those of exact order \(t\) are identified with units modulo \(t\). Equation (1) never mixes distinct \(H_t\)-orbits, where \(H_t=\langle2,-1\rangle\). If a coordinate in such an orbit is nonzero, equation (1) forces the coordinates at \(2r\) and \(-r\) nonzero; iterating shows that **all** coordinates of that orbit are nonzero. Thus each orbit is wholly zero or wholly nonzero.

On a nonzero orbit, apply (1) at \(r\) and \(-r\) and multiply. Cancellation gives \(y_{2r}y_{-2r}=1\). Since multiplication by \(2\) permutes the orbit, this yields \(y_ry_{-r}=1\) for all its coordinates, and (1) becomes

\[y_{-r}=y_r^{-1},\qquad y_{2r}=y_r^2.\tag{2}\]

Fixing a representative \(r\) and \(z=y_r\), equations (2) determine the orbit as \(y_{hr}=z^{\rho_t(h)}\). If \(-1\in\langle2\rangle\), then \(2^{d_t/2}=-1\pmod t\) and consistency requires \(z^{2^{d_t/2}+1}=1\). Otherwise the first return under doubling requires \(z^{2^{d_t}-1}=1\), and the separate negative half of the orbit uses the inverses. These are exactly the relations \(z^{N_t}=1\). Conversely every \(z\) satisfying this relation produces a solution of (1) on that orbit.

The map \(\rho_t\) in the statement is well defined: in the first case \(2^{d_t/2}=-1\pmod{N_t}\), and in the other case \(2^{d_t}=1\pmod{N_t}\), with the two signs independent. Moreover \(t\mid N_t\), so distinct \(H_t\) residues modulo \(t\) remain distinct modulo \(N_t\); \(\rho_t\) is injective. This also proves \(\rho_t(h)\) is a unit modulo \(N_t\).

**3. Frobenius descent.** The \(H_t\)-orbits of exact-order-\(t\) frequencies form the quotient \(G_t/H_t\), where \(G_t=(\mathbb Z/t\mathbb Z)^\times\). Multiplication by \(q\) permutes these cosets, with every cycle of length \(e_t\). There are exactly \(c_t=|G_t|/(|H_t|e_t)\) cycles. Along one such cycle, the condition \(y_{qr}=y_r^q\) propagates a chosen nonzero representative value \(z\). On returning after \(e_t\) steps, one encounters \(q^{e_t}r=h_tr\); therefore the precise compatibility condition is

\[z^{q^{e_t}}=z^{a_t},\quad\text{equivalently }z^{q^{e_t}-a_t}=1.\tag{3}\]

Together with \(z^{N_t}=1\), equation (3) leaves exactly \(g_t=\gcd(N_t,q^{e_t}-a_t)\) nonzero possibilities. To verify that these possibilities really lie in \(E\), set \(f_t=\operatorname{ord}_t(q)\) and \(m=f_t/e_t\). The element \(h_t\) has order \(m\) in \(H_t\), so \(a_t^m=1\pmod{N_t}\). Hence \(q^{f_t}=a_t^m=1\pmod{g_t}\), proving \(g_t\mid q^{f_t}-1\); all \(g_t\)-th roots of unity belong to \(\mathbb F_{q^{f_t}}\subseteq E\). Conversely the relation (3) is necessary, so the count is exact.

Each Frobenius cycle also permits the all-zero solution, independently of all others. Multiplying \(1+g_t\) over its \(c_t\) cycles, over all divisors \(t>1\), and by the two choices at frequency zero proves the theorem and its parameterization. Fourier inversion yields distinct elements of \(\mathbb F_q[R_n]\) for distinct compatible arrays.

## Verification

The standalone program `check_idempotents.py` evaluates the arithmetic formula and **independently** enumerates coefficients in the quandle basis, using the literal product \(e_i e_j=e_{2j-i}\) rather than Fourier equations. Its standard run checks eight prime-field cases and three cases over \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\); all eleven checks passed. Direct exhaustive independent C enumeration also gave the predicted totals for \(n=9,q=5\) (\(80\)), \(n=11,q=3\) (\(24\)), \(n=17,q=2\) (\(648\)), and \(n=21,q=2\) (\(4096\)). These enumerations confirm finite instances only; the general statement rests on the proof above.

Run `python3 check_idempotents.py`; `python3 check_idempotents.py --extended` activates further prime-field cases. Only the Python standard library is required.

## Relationship to prior work

Bardakov, Passi and Singh's *Zero-divisors and idempotents in quandle rings* (arXiv:2001.06843, first posted January 19, 2020) establishes the general quandle-ring setting and treats the integral \(R_3\) case and the binary \(R_3\) example. Elhamdadi, Nunez, Singh and Swain's *Idempotents, free products and quandle coverings* (arXiv:2204.11288, first posted April 24, 2022), with primary MSC \(17D99\), motivates idempotent sets as algebraic and knot-theoretic objects; its general covering statements do not count the finite-field idempotents of every odd dihedral quandle. Elhamdadi, Nunez and Singh's *Enhancements of link colorings via idempotents of quandle rings* (arXiv:2207.09257) provides small-order computations and related applications, not the all-order arithmetic formula.

Elhamdadi, Ta and Virgin's later *Fourier Analysis and Idempotents in Quandle Algebras* (arXiv:2609.03799, September 3, 2026), in particular Theorem 3.2 and Corollary 3.3/Proposition 3.4, proves the general complex Fourier multiplication identity underlying step 1. That identity already supplies the Fourier reformulation; **it is not claimed here as new**. Their published principal result concerns *integral* idempotents. The count and classification here solve the nonlinear Fourier-orbit relations and perform finite-field Frobenius descent, including composite odd \(n\), rather than restating the identity or integral case. A separate previously recorded classification for \(R_3\) in characteristic three is outside the coprime hypothesis, while its characteristic-not-three eight-idempotent special case is included but not asserted to be new. The present result is therefore a quantitative refinement with a substantial prior-method dependence, not a claim of a new Fourier-transform principle.

## Limitations

The theorem excludes \(\operatorname{char}\mathbb F_q\mid n\); such algebras can behave differently because the Fourier transform is not invertible. It does not classify multiplication among the idempotents, nor claim that they form a subquandle. The result requires no analytic limiting arguments. The near-term literature risk is that a cyclic-orbit and Frobenius-descent count equivalent to the displayed product may already appear under another terminology; in particular, the 2026 Fourier paper supplies a closely related general identity. The inspected material did not contain the displayed all-odd-order finite-field count, but this is not proof of exhaustive publication priority.

## References

1. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (first posted 2020-01-19), https://arxiv.org/abs/2001.06843.
2. M. Elhamdadi, B. Nunez, M. Singh and D. Swain, *Idempotents, free products and quandle coverings*, arXiv:2204.11288 (first posted 2022-04-24), https://arxiv.org/abs/2204.11288.
3. M. Elhamdadi, B. Nunez and M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257 (first posted 2022-07-19), https://arxiv.org/abs/2207.09257.
4. P. Narayanan and S. Panja, *Idempotents in integral ring of dihedral quandle*, arXiv:2206.10386 (first posted 2022-06-17), https://arxiv.org/abs/2206.10386.
5. M. Elhamdadi, L. Ta and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (first posted 2026-09-03), https://arxiv.org/abs/2609.03799.
