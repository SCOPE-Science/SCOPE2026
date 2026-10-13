# Joint spectra of lines and idempotents in modular differential Novikov algebras

## Finding

Let \(p\) be any prime, \(q\) any power of \(p\), \(K=\mathbb F_q\), and \(R=K[t]/(t^p)\). For **every** parameter \(a\in R\) define the Novikov product
\[
 f\circ_a g=f\bigl(g'+ag\bigr)\qquad(f,g\in R).
\]
Let \(\ell(a)\) be the number of one-dimensional \(K\)-subalgebras of \((R,\circ_a)\), and let \(e(a)\) be its number of **nonzero** idempotents. Put \(d=\lfloor(p-1)/2\rfloor\) and \(H=(q^d-1)/(q-1)\) (thus \(H=0\) when \(p=2\)). As \(a\) ranges over all \(q^p\) distinct labeled multiplications, the *complete joint distribution* of \((\ell(a),e(a))\) is

| \((\ell(a),e(a))\) | Number of parameters \(a\) |
| --- | ---: |
| \((1+H,1)\) | \((q-1)q^{p-2}\) |
| \((2+H,1)\) | \((q-1)q^{p-2}\) |
| \((2+H,2)\) | \((q-1)^2q^{p-2}\) |
| \((q+1+H,q)\) | \(q^{p-2}\) |

The row labels distinguish joint invariants, including when the two middle rows have equal line counts. More precisely, construct canonical \(h_a,g_a\in R\) by
\[
 h_a(0)=1,\quad g_a(0)=0,\qquad
 (\partial_t+a)h_a\equiv0\pmod{t^{p-1}},\quad
 (\partial_t+a)g_a\equiv1\pmod{t^{p-1}}.
\]
There are unique \(\sigma_a,\tau_a\in K\) such that
\[
 (\partial_t+a)h_a=\sigma_a t^{p-1},\qquad
 (\partial_t+a)g_a=1+\tau_a t^{p-1}.
\]
Every line subalgebra is **exactly one** of the following: \(Kg_a\); an arbitrary line in \(t^{\lceil(p+1)/2\rceil}R\); or \(K(h_a+\lambda g_a)\) for a unique \(\lambda\in K\) satisfying \(\sigma_a+\tau_a\lambda=0\). The map \(a\mapsto(\sigma_a,\tau_a)\) is surjective, and every fiber has exactly \(q^{p-2}\) parameters. The displayed joint distribution follows.

## Assumptions and scope

No assumptions beyond \(p\) prime, \(q=p^s\) for \(s\ge1\), and \(a\in R\) are imposed. Subalgebras are linear subspaces closed under the specified, generally nonassociative product, with no unitality requirement. The idempotent equation is \(x\circ_a x=x\) with \(x\ne0\). Distinct parameters give distinct labeled products because \(1\circ_a1=a\); the counts are **not** isomorphism-class counts. The case \(p=2\) is included; one member there need not be simple, and simplicity is not assumed.

## Proof

**1. Novikov identity.** Write \(T=\partial_t+M_a\), so \(f\circ_a g=fT(g)\). Associativity and commutativity of multiplication in \(R\) give
\[
 (f\circ_a g)\circ_a h=fT(g)T(h)=(f\circ_a h)\circ_a g
\]
and
\[
 (f\circ_a g)\circ_a h-f\circ_a(g\circ_a h)
 =-fg\,\partial_t(T(h)),
\]
which is symmetric in \(f,g\). These are the right-commutativity and left-symmetry identities.

**2. Canonical solutions.** Write \(a=\sum_{j=0}^{p-1}a_jt^j\). Given the constant coefficient of \(u\in R\), the coefficients of \(Tu\) through degree \(p-2\) determine each next coefficient of \(u\) uniquely: in the coefficient of \(t^i\), the new unknown occurs as \((i+1)u_{i+1}\), with \(1\le i+1<p\) invertible in \(K\). This proves existence and uniqueness of \(h_a,g_a\) and of the displayed \(\sigma_a,\tau_a\). For reproducibility, with \(h_0=1\), \(g_0=0\), and \(\delta_{i0}\) the Kronecker symbol, the recurrences are
\[
 h_{i+1}=-\frac{1}{i+1}\sum_{j=0}^{i}a_jh_{i-j},\qquad
 g_{i+1}=\frac{\delta_{i0}-\sum_{j=0}^{i}a_jg_{i-j}}{i+1},
 \quad 0\le i\le p-2.
\]

**3. Unit lines.** Suppose \(Kf\) is a line subalgebra with \(f(0)\ne0\); normalize \(f(0)=1\). As \(f\) is a unit of \(R\), the closure equation \(fT(f)=\lambda f\) is equivalent to \(T(f)=\lambda\) in \(R\). The recurrences imply \(f=h_a+\lambda g_a\), and its final coefficient equation is precisely \(\sigma_a+\lambda\tau_a=0\). Hence the number of unit lines is \(q\) if \(\sigma_a=\tau_a=0\), one if \(\tau_a\ne0\), and zero if \(\tau_a=0\ne\sigma_a\).

**4. Nonunit lines.** For \(f\ne0\) having \(t\)-adic order \(r\ge1\), write its lowest coefficient as \(ct^r\) with \(c\in K^\times\). If \(r=1\), comparing the order-one term in \(fT(f)=\lambda f\) gives \(\lambda=c\). After normalizing \(c=1\), canceling \(t\) modulo \(t^p\) leaves \(T(f)\equiv1\pmod{t^{p-1}}\), so the sole such line is \(Kg_a\). Moreover \(g_aT(g_a)=g_a\), because \(g_at^{p-1}=0\). If \(r\ge2\), the order of \(fT(f)\) exceeds \(r\), forcing \(\lambda=0\). Its leading possible coefficient is \(r c^2t^{2r-1}\), which is nonzero if \(2r-1<p\), since \(1\le r<p\). If \(2r-1\ge p\), both \(ff'\) and \(af^2\) vanish. Thus the remaining line subalgebras are precisely all lines of \(t^{\lceil(p+1)/2\rceil}R\), a \(d\)-dimensional vector space with \(H\) lines.

**5. Idempotents.** All nonunit lines except \(Kg_a\) have zero square, while \(g_a\) is a nonzero idempotent. A unit line \(K(h_a+\lambda g_a)\) has square \(\lambda(h_a+\lambda g_a)\), so it contains a unique nonzero idempotent exactly when \(\lambda\ne0\). Consequently \(e(a)=q\) when \(\sigma_a=\tau_a=0\), \(e(a)=2\) when \(\sigma_a\tau_a\ne0\), and \(e(a)=1\) in the other two cases.

**6. Exact parameter fibers.** The recurrence gives \(g_1=1\), \(g_0=0\); each \(g_j\) for \(j\ge2\) depends only on \(a_0,\ldots,a_{j-2}\). Taking the degree-\(p-1\) coefficient of \(Tg_a\) therefore gives
\[
 \tau_a=a_{p-2}+F(a_0,\ldots,a_{p-3}),
\]
for a polynomial expression \(F\), with the earlier list empty when \(p=2\). Similarly, since \(h_0=1\), taking the final coefficient of \(Th_a\) gives
\[
 \sigma_a=a_{p-1}+G(a_0,\ldots,a_{p-2}).
\]
For each fixed choice of \(a_0,\ldots,a_{p-3}\), the equations for any specified \((\tau_a,\sigma_a)\) uniquely determine first \(a_{p-2}\) and then \(a_{p-1}\). Thus each pair occurs for exactly \(q^{p-2}\) values of \(a\). The four possibilities for vanishing/nonvanishing of \(\sigma_a,\tau_a\) now give the table. Their parameter counts sum to \(q^p\).

## Verification

The standalone `checker.py` implements \(K\)-arithmetic, polynomial multiplication modulo \(t^p\), and direct enumeration of nonzero vectors/projective lines, independently of the classification step. It compares direct counts against the recurrence and the four-row formula. Successful tests cover all parameters for \((p,q)=(2,2),(2,4),(3,3)\), and 32 deliberately varied parameters for \((p,q)=(5,5)\). It also independently checks the **complete parameter-fiber distribution** for all \(a\) in each of these four settings, including all \(5^5\) parameter choices in the last case. Run `python checker.py` without dependencies beyond Python's standard library. Expected final line: `VERIFY_OK`. Such finite testing checks examples, not the proof for all primes and prime powers.

As explicit cases: for \(p=3,q=3\), the respective four table rows have frequencies \(6,6,12,3\) and line/idempotent pairs \((2,1),(3,1),(3,2),(5,3)\). For \(p=5,q=5\), they have frequencies \(500,500,2000,125\) and pairs \((7,1),(8,1),(8,2),(12,5)\).

## Relationship to prior work

The differential construction \(f\circ g=f(g'+ag)\) is established in work on Gelfand–Dorfman and Novikov–Poisson algebras and appears explicitly in Zhelyabin–Zakharov (2024, Section 1). Their main theorem concerns the structural representation of finite-dimensional simple Novikov algebras by truncated differential polynomial algebras. The present result does **not** claim that construction, its simplicity criterion, or a classification of Novikov algebras as novel. It supplies a different invariant: a full finite-field, all-parameter joint distribution of one-dimensional subalgebras and nonzero idempotents, with explicit necessary-and-sufficient line representatives. Earlier structural work of Osborn (1992) addresses simple Novikov algebras with an idempotent; its possible implications for individual idempotents remain a bibliographic limitation.

## Limitations

The theorem counts embedded one-dimensional subalgebras and nonzero idempotents, not higher-dimensional subalgebras, all ideals, automorphism orbits, or isomorphism classes. The general form of the construction is established prior literature; only the explicit joint census and its proof are asserted here. The independently checked cases are finite and cannot replace the general proof. An inaccessible earlier structural paper on Novikov idempotents prevents a categorical exclusion of equivalent published formulations. No independent audit has been performed.

## References

1. V. N. Zhelyabin and A. S. Zakharov, *On Finite-Dimensional Simple Novikov Algebras of Characteristic p*, Siberian Mathematical Journal 65 (2024), 680–687. DOI: 10.1134/S0037446624030169; publicly available online May 29, 2024.
2. J. M. Osborn, *Simple Novikov algebras with an idempotent*, Communications in Algebra 20 (1992), 2729–2753. DOI: 10.1080/00927879208824486.
3. P. S. Kolesnikov and A. A. Nesterenko, *Conformal Envelopes of Novikov–Poisson Algebras*, Siberian Mathematical Journal 64 (2023), 598–610. DOI: 10.1134/S0037446623030084.
4. A. P. Pozhidaev and V. N. Zhelyabin, *On simple and semisimple finite-dimensional Novikov algebras and their automorphisms*, Journal of Algebra 689 (2026), 1–26. DOI: 10.1016/j.jalgebra.2025.09.017; online October 10, 2025.
