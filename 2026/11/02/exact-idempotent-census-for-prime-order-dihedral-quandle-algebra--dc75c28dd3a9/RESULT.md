# Exact idempotent census for prime-order dihedral quandle algebras over every finite field

## Finding

Let \(p\geq3\) be an odd prime and \(q\) any prime power. The dihedral quandle \(R_p\) has underlying set \(\mathbb Z/p\mathbb Z\) and operation \(x*y=2y-x\). Its quandle algebra \(\mathbb F_q[R_p]\) is the (generally nonassociative) vector space with basis \(e_x\) and bilinear product \(e_xe_y=e_{2y-x}\). **Idempotents here include zero.**

Define \(m=\operatorname{ord}_p(2)\), \(h=\operatorname{lcm}(m,2)\), and \(s=(p-1)/h\). The exact number \(E_p(q)\) of idempotents is as follows.

**Modular characteristic:** If \(\operatorname{char}\mathbb F_q=p\), then
\[
E_p(q)=1+q^s.
\]
The nonzero idempotents form a set naturally parametrized, through truncated logarithmic coordinates, by a vector space of dimension \(s\) over \(\mathbb F_q\).

**Nonmodular characteristic:** If \(\operatorname{char}\mathbb F_q\ne p\), let \(H=\langle-1,2\rangle\leq(\mathbb Z/p\mathbb Z)^\times\), of order \(h\). Let \(d\) be the order of the image of \(q\bmod p\) in \((\mathbb Z/p\mathbb Z)^\times/H\). Put
\[
N=\begin{cases}2^{m/2}+1,&m\text{ even},\\2^m-1,&m\text{ odd}.\end{cases}
\]
Choose \(\sigma\in\{1,-1\}\) and \(0\leq e<m\) so that \(q^d\equiv\sigma 2^e\pmod p\), choosing \(\sigma=1\) when \(m\) is even. These choices are unique under the stated conventions. Set
\[
g=\gcd\!\left(N,\left|q^d-\sigma 2^e\right|\right),\quad \gcd(N,0)=N.
\]
Then
\[
\boxed{E_p(q)=2(1+g)^{s/d}.}
\]
The two-fold factor corresponds to the independent zero-frequency coefficient \(0\) or \(1\); each Frobenius orbit of nonzero \(H\)-cosets independently contributes either the inactive value or one of \(g\) nonzero root parameters.

For example, \(E_{11}(2)=68\), \(E_{11}(3)=24\), \(E_{17}(2)=648\), \(E_{17}(3)=36\), and \(E_{17}(17)=290\). The formula is uniform across both characteristics and all extension degrees.

## Assumptions and scope

All primes \(p\) are odd, all field sizes \(q\) are prime powers (including nonprime fields), and every equation is imposed inside the **quandle algebra**, not an associative group algebra. The associated ordinary group algebra is used as a calculational device; these two multiplications must not be confused. The idempotent equation means \(u\cdot u=u\) for the specified bilinear quandle product, without any associativity assumption. No restriction on \(\operatorname{char}\mathbb F_q\) is made in the final census.

## Proof

**1. Group-algebra transport.** Write \(C_p=\mathbb Z/p\mathbb Z\), and identify the vector space \(\mathbb F_q[R_p]\) with the underlying vector space of the ordinary associative group algebra \(B=\mathbb F_q[C_p]\), with basis \(X^x\). The quandle product transports to \(u\star v=\alpha(u)\beta(v)\), where juxtaposition denotes *ordinary* group-algebra multiplication and \(\alpha(X^x)=X^{-x}\), \(\beta(X^x)=X^{2x}\). Thus the idempotent equation is exactly
\[
u=\alpha(u)\beta(u).\tag{1}
\]
Both \(\alpha\) and \(\beta\) are commuting ordinary group-algebra automorphisms because \(p\) is odd.

**2. Nonmodular Fourier reduction.** Suppose \(\ell=\operatorname{char}\mathbb F_q\ne p\), and let \(K\) be an algebraic closure containing a primitive \(p\)-th root \(\zeta\). The Fourier transform \(c_i=\sum_{x\in C_p}a_x\zeta^{ix}\) is invertible since \(p\) is nonzero in \(K\). Equation (1) is equivalent, at every frequency \(i\in C_p\), to
\[
c_i=c_{-i}c_{2i}.\tag{2}
\]
At frequency zero, \(c_0^2=c_0\), so \(c_0\in\{0,1\}\). If \(i\ne0\) and \(c_i\ne0\), equation (2) forces \(c_{-i}\ne0\) and \(c_{2i}\ne0\). Iteration on the finite nonzero frequency set shows that the support of the nonzero Fourier coefficients is a union of complete \(H=\langle-1,2\rangle\)-orbits. At a supported \(i\), set \(P_i=c_ic_{-i}\); multiplying (2) at \(i\) and \(-i\) gives \(P_i=P_iP_{2i}\), hence \(P_{2i}=1\). As multiplication by \(2\) permutes a finite support orbit, \(P_i=1\) throughout it. Equation (2) is therefore equivalent on that orbit to
\[
c_{-i}=c_i^{-1},\qquad c_{2i}=c_i^2.\tag{3}
\]

**3. Orbit parameters and root equations.** Let \(m=\operatorname{ord}_p(2)\). If \(m\) is even, the unique element of order two in the cyclic subgroup \(\langle2\rangle\) equals \(-1\), so one \(H\)-orbit is one doubling orbit. Choosing \(t=c_i\ne0\), relations (3) consistently define the orbit precisely when \(t^{2^{m/2}+1}=1\) (which also implies \(t^{2^m-1}=1\)). If \(m\) is odd, the inversion orbit is disjoint from the doubling orbit, and consistency is precisely \(t^{2^m-1}=1\). In either case an \(H\)-orbit has exactly one inactive parameter \(t=0\) and, when active, one nonzero solution \(t\) of \(t^N=1\), with \(N\) as stated. Distinct \(H\)-orbits have independent choices over \(K\).

**4. Galois descent and exact count.** The inverse Fourier transform gives coefficients in \(\mathbb F_q\) exactly when
\[
c_{qi}=c_i^q\qquad(i\in C_p),\tag{4}
\]
by uniqueness of Fourier inversion and the \(q\)-Frobenius identity \(\zeta^q=\zeta^q\). Multiplication by \(q\) permutes the \(s=(p-1)/h\) nonzero \(H\)-cosets in cycles of common length \(d\), the order of \(qH\) in the cyclic quotient group \(C_p^\times/H\). For a representative \(i\) in a given cycle, \(q^di\equiv\sigma2^ei\pmod p\); equations (3) and (4) require
\[
t^{q^d}=t^{\sigma2^e}.\tag{5}
\]
If the orbit is inactive, this holds automatically. If active, (5) is equivalent to \(t^{q^d-\sigma2^e}=1\), together with \(t^N=1\). The number of such nonzero parameters in \(K\) is exactly \(g\): their common order divides \(g\), and \(\gcd(g,\ell)=1\), since \(q^d-\sigma2^e\) is nonzero modulo \(\ell\) when \(\ell\ne2\), while \(N\) is odd if \(\ell=2\). All these roots exist and are distinct in \(K\). Conversely, choosing \(0\) or any one of these \(g\) roots on each cycle, propagating by (3) and (4), is consistent with every relation; equation (5) closes each cycle and all relations commute. Each of the \(s/d\) cycles contributes \(1+g\) possibilities. Finally \(c_0\in\{0,1\}\) contributes a factor two. This proves the nonmodular formula.

**5. Modular characteristic.** Now let \(\operatorname{char}\mathbb F_q=p\). In the ordinary group algebra, put \(z=X-1\). Then \(B\cong\mathbb F_q[z]/(z^p)\), and the ordinary augmentation ideal \(I=(z)\) is nilpotent. Applying ordinary augmentation to (1), any idempotent has augmentation \(0\) or \(1\). If it is \(0\), then (1) gives \(u\in I^2\), and iteration gives \(u\in I^{2^k}=0\) for sufficiently large \(k\); hence \(u=0\). If its augmentation is \(1\), it lies in the ordinary multiplicative group \(1+I\), and equation (1) holds there. The truncated logarithm
\[
L(1+w)=\sum_{j=1}^{p-1}(-1)^{j+1}\frac{w^j}{j}\qquad(w\in I)
\]
is a bijective group homomorphism from \((1+I,\times)\) to \((I,+)\), with inverse the truncated exponential. The standard formal power-series logarithm identities hold modulo \(I^p\); every denominator used has degree less than \(p\) and is invertible in \(\mathbb F_q\). Moreover, \(L\) commutes with \(\alpha\) and \(\beta\). Thus (1) is equivalent to the **linear** equation
\[
v=\alpha(v)+\beta(v),\qquad v=L(u)\in I.\tag{6}
\]
The multiplicative group \(C_p^\times\) acts on \(I\) by \(X\mapsto X^a\). The filtration \(I\supset I^2\supset\cdots\supset I^p=0\) has one-dimensional successive quotients on which \(a\) acts by \(a^r\) for \(1\le r\le p-1\). Because \(p\nmid(p-1)\), the representation splits (averaging idempotents); its weight decomposition is the direct sum of these \(p-1\) distinct one-dimensional characters, all defined over \(\mathbb F_p\). On weight \(r\), equation (6) becomes
\[
1=(-1)^r+2^r\quad\text{in}\quad\mathbb F_p.
\]
When \(r\) is even this cannot hold, since it would require \(2^r=0\). When \(r\) is odd it becomes \(2^{r-1}=1\); equivalently \(r=1+kh\) for \(h=\operatorname{lcm}(\operatorname{ord}_p(2),2)\). Exactly \(s=(p-1)/h\) such integers lie in \([1,p-1]\). Equation (6) therefore has a solution space of dimension \(s\) over \(\mathbb F_q\), hence \(q^s\) nonzero-augmentation idempotents, plus the zero idempotent. This proves the modular formula.

## Verification

Run `python3 verify.py` beside this document. The verifier enumerates **all coefficient vectors**, builds their products directly from the original quandle multiplication, and tests idempotence; it does not use any Fourier parameterization or logarithmic argument to decide idempotence. It tests \((p,q)=(3,2),(3,3),(3,4),(3,5),(3,9),(5,2),(5,3),(5,4),(5,5),(7,2),(7,3),(7,4),(7,7),(11,2),(11,3),(13,2),(17,2)\). The last case exhaustively examines \(2^{17}=131072\) algebra elements. The field \(\mathbb F_4\) is implemented as \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), and \(\mathbb F_9\) as \(\mathbb F_3[\alpha]/(\alpha^2+1)\). It also evaluates further arithmetic instances without treating them as exhaustive matrix checks. Its passing terminal marker is `VERIFY_OK`.

The verifier is supporting finite evidence. The infinite-family assertions follow from the two symbolic proofs above, not from extrapolation of computations.

## Relationship to prior work

The Fourier quandle-product identity and resulting functional equation are previously established, in particular by Elhamdadi–Ta–Virgin (arXiv:2609.03799v1, Section 3) and Zhang (arXiv:2610.08204v1, Section 5). Their proofs concern general Fourier algebra structure and integral idempotent rigidity; those methods are credited and are **not** claimed as new here. Bardakov–Elhamdadi (arXiv:2601.07057v1, Section 4) treat related integral idempotent constraints. Sangare–Ta (arXiv:2608.01550v1) address automorphisms and integral-domain phenomena, not an exact finite-field census in the accessible material. The pre-existing mathematical record `2026/10/4/SCOPE-a-characteristic-three-idempotent-line-in-the-quandle-algebra-of--06aa9c19e539` gives the complete \(p=3\) characteristic split; that special case is acknowledged, not claimed new.

The present result's assessed contribution is the **uniform exact finite-field count for every odd prime order and every coefficient characteristic**, including Frobenius-root descent in coprime characteristic and the higher-dimensional modular idempotent families. Neither the finite-field root-gcd enumeration for general prime order nor its modular characteristic counterpart was located in the inspected sources. The absence of an identified identical statement is not a proof of global priority.

## Limitations

This theorem concerns prime-order dihedral quandles only; arbitrary Alexander parameters, composite quandle orders, and infinite coefficient fields are not counted. The count is of labeled algebra elements, not isomorphism classes or conjugacy classes. The proof is self-contained after the classical cyclic-character decomposition and truncated-logarithm facts explained above. An equivalent arithmetic enumeration may exist in other literature under different terminology; no independent audit has been performed. No claim about general quandle-ring idempotents beyond this family is made.

## References

- Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, first public 2026-10-06. https://arxiv.org/html/2610.08204v1
- Mohamed Elhamdadi, Lực Ta, Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1, first public 2026-09-03. https://arxiv.org/html/2609.03799v1
- Valeriy Bardakov, Mohamed Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057v1, first public 2026-01-11. https://arxiv.org/html/2601.07057v1
- Birama Sangare, Lực Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1, first public 2026-08-03. https://arxiv.org/abs/2608.01550
- Mohamed Elhamdadi, Dipali Swain, *State sum invariants of knots from idempotents in quandle rings*, arXiv:2402.14661v2. https://arxiv.org/html/2402.14661v2
