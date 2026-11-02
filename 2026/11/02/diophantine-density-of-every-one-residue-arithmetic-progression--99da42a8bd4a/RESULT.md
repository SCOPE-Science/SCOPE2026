# Diophantine density of every one-residue arithmetic progression

## Finding

For integers \(m\ge 1\), \(0\le r<m\), and \(L\ge1\), let
\[
P_{m,r,L}=\{v\in\mathbb N:v\ge L,\ v\equiv r\pmod m\}.
\]
With the restricted-approximation Diophantine density \(\delta\) defined below, **every such progression has density exactly zero or one**, and
\[
\delta(P_{m,r,L})=\begin{cases}
1,&r=0\text{ or }(m,r)=(2,1),\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, the disjoint positive residue classes \(U=\{v\ge1:v\equiv1\pmod4\}\) and \(V=\{v\ge1:v\equiv3\pmod4\}\) satisfy \(\delta(U)=\delta(V)=0\), while \(\delta(U\cup V)=1\). This is an explicit periodic realization of maximal failure of subadditivity; failure of subadditivity itself is not claimed as a first discovery.

## Assumptions and scope

Here \(\mathbb N=\{1,2,\ldots\}\) and \(\|x\|\) is the distance from a real number to the nearest integer. For nonempty \(T\subseteq\mathbb N\), \(\delta(T)\) is the supremum of exponents \(s\ge0\) for which some \(C>0\) and \(q_0\) have the property that for **every** integer \(q\ge q_0\) and **every** integer \(p\) with \(\gcd(p,q)=1\), one has
\[
\min_{v\in T,\ 1\le v<q}\left\|\frac{vp}{q}\right\|\le Cq^{-s}.
\]
For these infinite progressions the minimum is nonempty for sufficiently large \(q\). As established for this density, \(0\le\delta(T)\le1\). The cutoff \(L\) is arbitrary but fixed; the statement requires all moduli and residues, not just coprime residues.

## Proof

**The zero residue class.** For \(r=0\), let \(M=m\lceil L/m\rceil\). Every positive multiple of \(M\) belongs to \(P_{m,0,L}\). For \(q>M\), set \(N=\lfloor(q-1)/M\rfloor\ge1\). Dirichlet's pigeonhole lemma applied to \(Mp/q\) supplies \(1\le j\le N\) with \(\|jMp/q\|\le1/(N+1)\le M/q\); also \(jM<q\). Thus \(\delta(P_{m,0,L})=1\).

**The exceptional odd class.** Let \((m,r)=(2,1)\). For every coprime \((p,q)\), choose the inverse \(u\) of \(p\) modulo \(q\), with \(1\le u<q\). If \(q\) is even, \(u\) is odd. If \(q\) is odd, exactly one of \(u,q-u\) is odd. Thus there is an odd \(v\), \(1\le v<q\), with \(vp\equiv\pm1\pmod q\). If \(v\ge L\), the approximation error is \(1/q\). Otherwise select the smallest positive odd integer \(j\) such that \(jv\ge L\); it satisfies \(j\le L+2\) and \(jv\le(L+2)L\). For all \(q>(L+2)L\), the odd integer \(jv\) belongs to \(P_{2,1,L}\), is smaller than \(q\), and satisfies \(\|jvp/q\|\le j/q\le(L+2)/q\). Hence this class also has density one.

**Every remaining nonzero residue class.** Now \(m\ge3\) and \(1\le r<m\). For arbitrarily large integers \(t\), choose the following coprime numerator-denominator pairs:
\[
(p_t,q_t)=\begin{cases}(t,mt-1),&r=1,\\(t,mt+1),&r\ge2.\end{cases}
\]
If \(r=1\), for every \(v\equiv1\pmod m\), \(1\le v<q_t\), writing \(v=mk+1\) gives
\[
\frac{vp_t}{q_t}=k+\frac1m+\frac{v}{mq_t},
\qquad \frac1m<\frac1m+\frac{v}{mq_t}<\frac2m.
\]
Because \(m\ge3\), the distance to the nearest integer is at least \(1/m\). If \(2\le r<m\), the choice \(q_t=mt+1\) and \(v=mk+r\) instead gives
\[
\frac{vp_t}{q_t}=k+\frac rm-\frac{v}{mq_t},
\qquad\frac{r-1}{m}<\frac rm-\frac{v}{mq_t}<\frac rm.
\]
This interval also lies at distance at least \(1/m\) from every integer. The same lower bound applies to the subset \(v\ge L\). Thus there are reduced rationals with denominators tending to infinity for which the defining minimum is bounded below by \(1/m\), excluding every exponent \(s>0\). Therefore \(\delta(P_{m,r,L})=0\).

**The periodic example.** The residue classes \(1\) and \(3\) modulo \(4\) both fall into the final case. Their union is precisely \(P_{2,1,1}\), whose density is one by the second case.

## Verification

The standalone Python 3 file `verify.py` tests \(81{,}675\) individual rational obstructions for moduli \(3\) through \(24\) and a range of numerators, tests \(13{,}412\) reduced numerator-denominator pairs for odd modular inverses, and checks the odd-union sharpness over further finite ranges. Run `python3 verify.py`; expected terminal line begins `VERIFY_OK`. The uniform infinite proof above, not the finite computations, establishes the classification.

## Relationship to prior work

Sanford's May 2026 note introduced a restricted-approximation density; his October 2026 expanded work specifies the supremum definition with \(v<q\), proves density one for multiples (Proposition 5), and gives density zero for a family of translated progressions (Proposition 6). Neither inspected text classifies every arithmetic progression or singles out the odd residue class as the unique nonzero class with density one. The argument here gives that complete classification, including arbitrary starting cutoffs. A separate existing covering-set construction realizes arbitrary prescribed density pairs whose union is all positive integers; therefore non-subadditivity as such is already covered. The additional assertion here is the rigid periodic classification and its explicit finite-state example.

## Limitations

The result concerns one complete residue class above a fixed cutoff; it does not classify arbitrary unions of residue classes, sparse subsets of progressions, or the densities of general periodic sets. An unindexed earlier calculation of these particular residue classes is a residual priority risk. The finite verifier alone is not an infinite proof.

## References

1. Chance Sanford, *A Note on Diophantine Approximation with Restricted Denominators*, arXiv:2606.02620v1, publicly submitted 2026-05-28, https://arxiv.org/abs/2606.02620.
2. Chance Sanford, *On a Notion of Density Related to Restricted Diophantine Approximation*, arXiv:2610.27497v1, publicly submitted 2026-10-20, https://arxiv.org/abs/2610.27497, especially Definition 1, Propositions 5–6, and Section 7.
3. *Prescribed Diophantine densities for two covering sets of upper density one*, related currently unpublished construction; cited solely for the stronger existential covering-set statement, not as a source for the arithmetic-progression classification.
