# Exact helical orbit censuses for nonlinear parallel-coset Yang–Baxter maps

## Finding

For every integer \(m\ge2\), let \(V\) be the additive group of \(\mathbb F_{2^m}\), put \(q=2^m\), choose \(d\in V\setminus\{0\}\), and form \(W=V/\langle d\rangle\) with quotient map \(\pi\). Choose any function \(\chi:W\to\mathbb F_2\) satisfying \(\chi(0)=0\) and any \(c\in V\). Define
\[
f(s)=s+c+\chi(\pi(s+c))d,\qquad
R(x,y)=(y+f(x+y),x+f(x+y)).
\]
The map \(f\) is bijective, \(R\) is an involution, and \(R\) satisfies the set-theoretic quantum Yang–Baxter identity \(R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}\). (The unswapped map \(R\) is not being asserted to satisfy the distinct braid identity.)

Let \(T_N\) be the permutation of the full state space \(V^{N+1}\), \(N\ge1\), obtained by passing a carrier \(b\) in order through sites \(x_1,\ldots,x_N\), applying \(R(x_i,b)\), retaining the first output as the new site, and using the final second output as next carrier. Then \(T_N^4=\operatorname{id}\) for all parameters and \(T_N^2=\operatorname{id}\) for odd \(N\).

Write \(m_a=|\chi^{-1}(a)|\) for \(a\in\{0,1\}\), \(h=\pi(c)\), and
\[
v_h=|\{u\in W:\chi(u)=\chi(u+h)\}|.
\]
For the whole site-plus-carrier phase space the exact fixed-point counts are
\[
F_1=|\operatorname{Fix}(T_N)|=
\begin{cases}
q(2m_0)^N,&c=0,\\
q(2m_1)^N,&c=d,\\
0,&c\notin\{0,d\},
\end{cases}
\qquad
F_2=|\operatorname{Fix}(T_N^2)|=
\begin{cases}
q^{N+1},&N\text{ odd},\\
q(2v_h)^N,&N\text{ even}.
\end{cases}
\]
Consequently the numbers of distinct primitive cycles of lengths one, two, and four are, respectively,
\[
C_1=F_1,\qquad C_2=(F_2-F_1)/2,\qquad C_4=(q^{N+1}-F_2)/4.
\]
There are no other primitive cycle lengths. For even \(N\), the global order is four precisely when \(\chi(u)\ne\chi(u+h)\) for at least one \(u\in W\); otherwise it is at most two. The global order is one precisely for \(c=0\) and \(\chi\equiv0\).

Counting *distinct functions* \(f\) across all \(d,c,\chi\), this family has exactly
\[
M(q)=q\left[1+(q-1)(2^{q/2-1}-1)\right]
\]
members, of which
\[
M_{\mathrm{nonaff}}(q)=q(q-1)(2^{q/2-1}-q/2)
\]
are non-affine. For every even site number, exactly
\[
(q-1)(q-2)(2^{q/2-1}-2^{q/4-1})
\]
of the distinct functions generate a global order-four permutation, including exactly
\[
(q-1)(q-2)(2^{q/2-1}-2^{q/4-1}-q/4)
\]
non-affine ones.

## Assumptions and scope

All additions are in characteristic two, hence can be implemented as bitwise XOR after choosing an additive basis. The function \(\chi\) is completely arbitrary on the \(q/2\) cosets except for \(\chi(0)=0\); it need not be linear or continuous in any extra topology. The dimension condition \(m\ge2\) makes the displayed combinatorial counts meaningful. The phase space includes the carrier; projected site-only itineraries are not separately counted. The boundary prescription is precisely a sequential helical sweep as defined above. The first source's general finite-field periodicity conjecture is **not** asserted for maps outside this subfamily.

## Proof

**1. Yang–Baxter family.** Put \(K(s)=c+\chi(\pi(s+c))d\), so \(R(x,y)=(x+K(x+y),y+K(x+y))\). On each two-element coset of \(\langle d\rangle\), the map \(s\mapsto s+\chi(\pi s)d\) is either the identity or the transposition, and therefore bijective. Composing it with translation by \(c\) proves bijectivity of \(f\). The sum \(x+y\) is invariant under \(R\), so applying \(R\) twice cancels its common increment.

The quotient \(\pi(K(s))=h\) is independent of \(s\); moreover \(K(s)\) depends only on \(\pi(s)\). For a triple \((x,y,z)\), the three pair increments in either side of \(R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}\) are exactly \(K(x+y)\), \(K(x+z+c)\), and \(K(y+z)\): the preceding one or two pair operations shift the relevant pair-sum quotients by respectively \(0\), \(h\), and \(0\). Both compositions add the same two increments to each coordinate, proving equality. Equivalently, direct substitution gives the characteristic-two functional identity \(f(x)+f(x+f(y))=f(x+f(y+f(x)))\).

**2. Exact sweeps.** At sweep time \(t\), the carrier quotient at the beginning is \(\pi(b(0))+Nt h\); the quotient of site \(i\) is \(\pi(x_i(0))+t h\). The carrier has crossed \(i-1\) earlier sites, each adding quotient \(h\). It follows that the flag used at site \(i\) is
\[
\epsilon_i(t)=\chi\!\left(\pi(x_i(0)+b(0)+ic+(N+1)tc)\right).
\]
The exact state recursion is
\[
x_i(t+1)=x_i(t)+c+\epsilon_i(t)d,\qquad
b(t+1)=b(t)+Nc+d\sum_{i=1}^N\epsilon_i(t).
\]
Since \(2c=0\), every flag has temporal period dividing two. Thus four sweeps cancel the constant terms and each flag twice, giving \(T_N^4=\operatorname{id}\). When \(N\) is odd, \(N+1\) is even and the flags do not change with time; already two sweeps cancel, proving \(T_N^2=\operatorname{id}\).

**3. Fixed sets.** A single sweep fixes a site iff \(c+\epsilon_i(0)d=0\). This is impossible unless \(c=0\) (all flags zero) or \(c=d\) (all flags one); in either case the carrier also returns. For fixed initial carrier, the quotients \(\pi(x_i(0)+b(0)+ic)\) vary independently and uniformly over \(W\), with two lifts per quotient. Therefore the numbers of fixed points are \(q(2m_0)^N\) and \(q(2m_1)^N\) in those two cases.

For even \(N\), the two successive flags at a site equal \(\chi(u_i)\) and \(\chi(u_i+h)\). Two sweeps restore every site exactly when these agree at every site; then the carrier is also restored because its two-sweep increment is the sum of the site increments. The same independent-quotient count gives \(q(2v_h)^N\) two-sweep fixed states. For odd \(N\) all states are two-sweep fixed. As every orbit length divides four, the asserted primitive-cycle formulas follow from \(F_1=C_1\), \(F_2=C_1+2C_2\), and \(q^{N+1}=C_1+2C_2+4C_4\). If \(v_h<|W|\), a nonfixed two-sweep state exists, so the global order is exactly four.

**4. Distinct-function census.** Every such \(f\) uniquely determines \(c\) because \(f(c)=0\) and \(f\) is bijective. For fixed \(c\) a nonzero \(\chi\) determines \(d\) uniquely: the nonzero values of \(f(s)+s+c\) consist of the singleton \(\{d\}\). The zero mask gives just one translation for each \(c\), independently of \(d\). There are \(2^{q/2-1}\) masks for each nonzero \(d\), producing the stated \(M(q)\). A function is affine iff \(\chi\) is additive-linear on \(W\); there are precisely \(q/2\) such normalized masks. For each \(c\notin\langle d\rangle\), invariance under the nonzero quotient shift \(h\) leaves \(2^{q/4-1}\) masks, since \(W/\langle h\rangle\) has \(q/4\) elements. Thus \(2^{q/2-1}-2^{q/4-1}\) masks give order four for each of the \((q-1)(q-2)\) possible \((d,c)\). Exactly \(q/4\) linear masks are noninvariant under \(h\). Subtracting these gives the non-affine order-four count. Every count is over distinct actual functions, not parameter tuples.

## Verification

The self-contained standard-library program `parallel_coset_verify.py` enumerates all distinct family maps for \(q=4\) and \(q=8\), independently verifies the characteristic-two functional identity and the three-coordinate *unbraided* Yang–Baxter identity, exhaustively tests helical states at site lengths one and two for both sizes (and length three for \(q=4\)), compares the fixed-state and order formulas, and tests further examples for \(q=16\). Run `python3 parallel_coset_verify.py`. Its checked output reports \(16\) and \(400\) distinct functions, respectively, including \(224\) non-affine maps at \(q=8\), with \(168\) non-affine order-four maps at even lengths. The verifier finishes with `VERIFY_OK: assertions = 1760824`.

For a concrete genuinely non-affine example, identify \(V\cong\mathbb F_2^3\) by XOR labels \(0,\ldots,7\), take \(d=1\), \(c=2\), and let \(\chi\) be one precisely on the coset \(\{2,3\}\). Then \(f\) has table `(3,2,0,1,6,7,4,5)`. At \(N=2\), the \(512\) site-plus-carrier states partition into **zero fixed cycles, 64 two-cycles, and 96 four-cycles**. The finite computations confirm instances of the theorem; the proof above, not sampling, establishes the unbounded dimensions and lengths.

## Relationship to prior work

Araoka and Tokihiro (arXiv:2602.17148v1, Sections 2–3) give the characteristic-two functional equation, full small-field enumerations and a period-divisibility conjecture. Their Proposition 19 and Corollary 20 treat additive-linear subclasses, while Propositions 21–27 analyze particular small-field transposition patterns; Table 1 tabulates maximal observed primitive periods by rule. These results do not state the arbitrary-dimension non-additive coset-mask construction together with an exact per-configuration primitive-cycle census and formula counting distinct maps. The present theorem settles the conjectured bound only for the explicitly defined family and refines it to a cycle census. Veselov's Yang–Baxter monodromy framework and the Etingof–Schedler–Soloviev set-theoretic theory are foundational context, not being claimed as new. Some masks are linear and overlap known affine models; the non-affine subclass is separated explicitly.

## Limitations

No claim is made that this family exhausts all finite-field Yang–Baxter solutions or resolves the full conjecture for arbitrary bijective solutions. The only possible primitive periods within this family are one, two, and four; this does not exclude longer periods in other classes. The theorem concerns full site-plus-carrier states, not the orbit count of the site projection after forgetting the carrier. Earlier equivalent descriptions of the same nonlinear family could exist in specialized literature; independent priority and proof assessment have not been performed.

## References

1. A. Araoka and T. Tokihiro, *Integrable cellular automata on finite fields of order \(2^n\)*, arXiv:2602.17148v1 (first public 2026-02-19), https://arxiv.org/html/2602.17148 .
2. A. P. Veselov, *Yang–Baxter maps and integrable dynamics*, arXiv:math/0205335, https://arxiv.org/abs/math/0205335 .
3. P. Etingof, T. Schedler, and A. Soloviev, *On set-theoretical solutions of the quantum Yang–Baxter equation*, arXiv:q-alg/9707027, https://arxiv.org/abs/q-alg/9707027 .
