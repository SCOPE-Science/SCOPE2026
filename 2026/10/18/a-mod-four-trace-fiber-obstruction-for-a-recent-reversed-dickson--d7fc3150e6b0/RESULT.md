# A mod-four trace-fiber obstruction for a recent reversed-Dickson permutation question

## Finding

Let \(s\ge 2\), \(q=2^s\), \(K=\mathbb F_{q^4}\), and let \(\tau:K\to\mathbb F_q\) be the relative trace. Define
\[
G_q(X)=X+(X+X^q)^{q^2}+(X+X^q+X^{q^2}+X^{q^3})(X+X^q)^{q-1}.
\]
For each \(w\in\mathbb F_q\), the cardinality of the joint trace fiber
\[
N_q(w)=\#\{x\in K:\tau(x)=w,\ \tau(G_q(x))=0\}
\]
is exactly
\[
N_q(w)=\begin{cases}
q^3,&w=0,\\
4q,&w\ne0\text{ and }s\equiv3\pmod4,\\
0,&w\ne0\text{ and }s\not\equiv3\pmod4.
\end{cases}
\]
Consequently
\[
\#\{x\in K:\tau(G_q(x))=0\}=q^3+4q(q-1)\mathbf 1_{s\equiv3\pmod4}.
\]
For every \(s\equiv3\pmod4\), \(G_q\) is **not** a permutation of \(K\). The statement makes **no** permutation claim for the other congruence classes.

## Assumptions and scope

All operations are in characteristic two. The exponent \(q-1\) has its usual polynomial meaning (so \(0^{q-1}=0\)). This is the \(e=4\) specialization of Question 6.1 in Fernando--Kousik, with parameter \(n=(q-1)(1+q^2)+q^4\); their \(S_2(X)=X+X^q\) and \(S_4(X)=\tau(X)\). No assumption that \(G_q\) is a permutation is made. The domain is every integer \(s\ge2\), not merely tested small fields.

## Proof

Put \(z=x+x^q\) and \(w=\tau(x)\). As \(\tau(z)=0\), \(z^{q^2}+z=w\), and \(\tau(z^{q^2})=0\), direct substitution gives
\[
\tau(G_q(x))=w\bigl(1+\tau(z^{q-1})\bigr).
\]
If \(w=0\), this is zero. The relative trace has a kernel of size \(q^3\), proving \(N_q(0)=q^3\).

Suppose \(w\ne0\), and put \(y=z/w\). Then \(y^{q^2}+y=1\), and the trace condition is \(\tau(y^{q-1})=1\). The map \(x\mapsto x+x^q\) has kernel \(\mathbb F_q\) of size \(q\) and image \(\ker\tau\), since both have size \(q^3\). For each \(y\) satisfying \(y^{q^2}+y=1\), the \(q\) solutions of \(x+x^q=wy\) all have trace \(w\), because \(\tau(x)=(x+x^q)+(x+x^q)^{q^2}=w\). Thus \(N_q(w)=q\) times the number of qualifying \(y\).

Define
\[
t=y+y^q,\quad v=y^2+y,\quad h=t^2+t.
\]
From \(y^{q^2}=y+1\) we obtain \(t^q+t=1\), \(t\in\mathbb F_{q^2}\), and \(v\in\mathbb F_{q^2}\). Therefore \(h\in\mathbb F_q\) has absolute trace \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(h)=1\); equivalently, the quadratic \(T^2+T+h\) is irreducible over \(\mathbb F_q\). Also \(v^q+v=h\). In particular \(v\) and \(v+h=v^q\) are nonzero, since \(v=0\) would force \(h=0\).

By the tower trace and \(y^{q-1}=y^q/y=1+t/y\) (here \(y\ne0\)), noting that \(\tau(1)=0\) and \(\tau(1/y)=0\) is not assumed, we instead use the algebraic identity \(y^{q-1}=1+t/y\), and \(y^{-1}=(y+1)/v\). Hence
\[
\tau(y^{q-1})=\tau(t(y+1)/v).
\]
The first relative trace from \(K\) to \(\mathbb F_{q^2}\) sends \(t(y+1)/v\) to \(t/v\), since \(t^{q^2}=t\), \(v^{q^2}=v\), and \((y+1)^{q^2}=y\); thus
\[
\tau(y^{q-1})=\frac{t}{v}+\frac{t^q}{v^q}
=\frac{v+th}{v(v+h)}.
\]
Let \(b=v+th\in\mathbb F_q\), as its \(q\)-th power equals itself. Using \(v=b+th\) and \(t(t+1)=h\), the denominator is
\[
v(v+h)=b^2+bh+h^3.
\]
Consequently \(\tau(y^{q-1})=1\) if and only if
\[
b^2+(h+1)b+h^3=0.
\]
If \(h\ne1\), this equation becomes \(u^2+u=h^3/(h+1)^2\), with \(u=b/(h+1)\in\mathbb F_q\). But
\[
\frac{h^3}{(h+1)^2}
=h+\frac1{h+1}+\frac1{(h+1)^2},
\]
and its absolute trace is \(\operatorname{Tr}(h)=1\). This contradicts the fact that the absolute trace of \(u^2+u\) is zero. Therefore \(h=1\), and the displayed quadratic gives \(b=1\). Since \(\operatorname{Tr}(1)=1\), the extension degree \(s\) is odd.

Now \(t^2+t=1\), so \(t\in\mathbb F_4\setminus\mathbb F_2\). We also have \(v=b+th=1+t\), which is equivalent to \(y^2+y=t+1\). Thus \(y^4+y=t^2+t=1\), so \(y\in\mathbb F_{16}\), and \(y^8+y=t\). As \(s\) is odd, the \(q\)-Frobenius on \(\mathbb F_{16}\) is the square map when \(s\equiv1\pmod4\) and the eighth-power map when \(s\equiv3\pmod4\). The required equation \(y^q+y=t\) therefore holds exactly in the second case: in the first it equals \(y^2+y=t+1\ne t\).

If \(s\equiv3\pmod4\), there are exactly two possibilities for \(t\) (the roots of \(T^2+T+1\)), and exactly two corresponding roots of \(Y^2+Y=t+1\) in \(\mathbb F_{16}\). All four satisfy \(y^{q^2}+y=1\), \(y+y^q=t\), and \(\tau(y^{q-1})=1\) by the reversible identities above. Thus there are precisely four qualifying \(y\); for all other \(s\) there are none. Multiplication by the \(q\) lifts from \(x+x^q=wy\) yields the claimed \(N_q(w)\).

A bijection on \(K\) would have exactly \(q^3\) input elements mapping into the \(q^3\)-element set \(\ker\tau\). For \(s\equiv3\pmod4\), the displayed total is larger, so \(G_q\) cannot be bijective. This completes the proof.

## Verification

The independent integer-bit finite-field program `verify_trace.py` enumerates all \(x\in\mathbb F_{q^4}\) for \(q=4,8,16\), using explicit irreducible binary moduli and direct polynomial arithmetic. It checks the entire joint trace-zero fiber distribution by \(w=\tau(x)\). It prints `VERIFY_OK` after checking \(64\), \(736\), and \(4096\) respective total trace-zero preimages. These are consistency checks, not proof of the universal statement.

## Relationship to prior work

Fernando and Kousik (2026), Question 6.1, request permutation criteria for the general even extension-degree family containing this \(e=4\) polynomial. The present finding supplies a universal congruence-family obstruction and the exact first joint trace-fiber law. Fernando, Hou and Lappano (2012) develop the reversed-Dickson framework and multiple trace-based permutation criteria, but the particular \(e=4\) trace-zero fiber classification is not identified there. General Artin--Schreier solvability is used explicitly in the proof and not claimed as novel.

## Limitations

The formula determines only one output trace fiber, not the full distribution of \(G_q\), and does not establish whether \(G_q\) is a permutation for \(s\not\equiv3\pmod4\). It does not address \(e>4\). Implicit coverage in broader finite-field permutation results remains a literature risk. Independent validation is outstanding.

## References

- N. Fernando and B. Kousik, *A further study of polynomial \(g_{n,q}\) over finite fields*, arXiv:2606.01037v1 (submitted 31 May 2026), Question 6.1. https://arxiv.org/abs/2606.01037
- N. Fernando, X.-D. Hou and S. D. Lappano, *A New Approach to Permutation Polynomials over Finite Fields, II*, arXiv:1208.2942 (2012), especially introduction and trace-based constructions. https://arxiv.org/abs/1208.2942
