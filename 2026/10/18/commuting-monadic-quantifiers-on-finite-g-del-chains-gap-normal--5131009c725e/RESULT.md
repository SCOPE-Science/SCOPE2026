# Commuting monadic quantifiers on finite Gödel chains: gap normal form and exact census

## Finding

Let \(G_n=\{0<1<\cdots<n-1\}\) be the \(n\)-element Gödel (Heyting) algebra, \(n\ge2\), with implication \(a\to b=n-1\) when \(a\le b\), and \(a\to b=b\) otherwise. An ordered two-agent monadic expansion consists of two pairs \((\forall_1,\exists_1)\) and \((\forall_2,\exists_2)\), each of which separately makes \(G_n\) a monadic Gödel algebra in the usual sense. Impose exactly two additional equations:
\[
\forall_1\forall_2=\forall_2\forall_1,
\qquad
\exists_1\exists_2=\exists_2\exists_1.
\]
These are **same-polarity** commutation requirements; neither mixed-polarity equation is imposed.

Every such expansion is uniquely determined by an ordered pair \((B,C)\) of subsets with \(\{0,n-1\}\subseteq B,C\subseteq G_n\). The universal quantifiers round downward to \(B,C\), respectively, and the existential quantifiers round upward. Put \(I=B\cap C\). The following are equivalent:

1. The two universal quantifiers commute.
2. The two existential quantifiers commute.
3. In each open interval between consecutive points of \(I\), at least one of \(B\setminus C\) and \(C\setminus B\) is absent.
4. The composites are precisely the two roundings to \(I\):
   \[
   \forall_B\forall_C=\forall_C\forall_B=\forall_I,
   \qquad
   \exists_B\exists_C=\exists_C\exists_B=\exists_I.
   \]

If \(a_k\) counts these ordered commuting expansions for \(n=k+2\), then
\[
\sum_{k\ge0}a_k z^k=\frac{1}{1-4z+2z^2},\qquad
 a_0=1,\quad a_1=4,\quad a_k=4a_{k-1}-2a_{k-2}\ (k\ge2).
\]
Equivalently,
\[
\boxed{
 a_k=\frac{(2+\sqrt2)^{k+1}-(2-\sqrt2)^{k+1}}{2\sqrt2}
}
\quad (k\ge0).
\]
The first counts, for \(n=2,3,\ldots,12\), are
\[
1,4,14,48,164,560,1912,6528,22288,76096,259808.
\]
Because the underlying finite chain has no nonidentity automorphism, these are simultaneously labeled counts and isomorphism-class counts for the fixed chain reduct. Among all \(4^k\) ordered pairs of monadic expansions, the commuting fraction is asymptotic to
\[
\frac{2+\sqrt2}{2\sqrt2}\left(\frac{2+\sqrt2}{4}\right)^k,
\]
so same-polarity commutation is exponentially rare as the chain grows.

## Assumptions and scope

The monadic Gödel operations are the standard universal/existential pair on a Gödel reduct (the equations M1–M5 as in Castaño–Cimadamore–Díaz Varela–Rueda). One pair's two operations satisfy the usual monadic interaction equations; the two *distinct* pairs are not required to commute across polarities or to arise from a full polyadic algebra. The theorem only enumerates **ordered, named** pairs on a fixed finite chain. It does not identify expansions under interchange of agents; interchanging names is not a chain automorphism. No result for nonchains or infinite chains is asserted.

For any endpoint-containing subset \(F\subseteq G_n\), define
\[
L_F(x)=\max\{t\in F:t\le x\},\qquad
U_F(x)=\min\{t\in F:t\ge x\}.
\]
An open gap of \(I\) means \((u,v)\) for consecutive \(u<v\) in \(I\). Gaps may contain no chain points. The comparisons of operations are pointwise on the entire chain.

## Proof

**Step 1: Single-pair representation.** Lemma 1.1 of Castaño et al. and Theorem 3.4 of Cintula–Metcalfe–Tokuda identify a monadic quantifier pair by its common fixed-point Gödel subalgebra. On a finite Gödel chain every subset containing \(0\) and \(n-1\) is a subalgebra: \(\min\) and \(\max\) select arguments, and \(a\to b\) equals either \(n-1\) or \(b\). Every such subset is relatively complete, with lower and upper roundings as above. Thus all monadic pairs are uniquely \((L_F,U_F)\), and there are \(2^{n-2}\) of them. This single-pair statement is an established ingredient, not the novel assertion.

**Step 2: Commuting lower roundings.** Write \(I=B\cap C\). If \(L_B,L_C\) commute, their common composition \(T=L_BL_C=L_CL_B\) is monotone, regressive and idempotent. Its fixed-point set is exactly \(I\): if \(T(x)=x\), regressiveness forces \(L_C(x)=x\) and \(L_B(x)=x\); conversely any \(x\in I\) is fixed by both. For a monotone, regressive, idempotent map on a finite chain, the value at \(x\) is its greatest fixed point not exceeding \(x\), since \(y\le x\) fixed implies \(y=T(y)\le T(x)\). Consequently \(T=L_I\).

Now suppose no gap of \(I\) contains points of both \(B\setminus C\) and \(C\setminus B\). Fix \(x\) in the half-open interval \([u,v)\) between successive points \(u<v\) of \(I\). If the interval contains \(B\)-only points, it contains no \(C\)-only points; hence \(L_C(x)=u\), while \(L_B(x)\in[u,v)\), which gives \(L_BL_C(x)=L_CL_B(x)=u\). The symmetric case is identical, as is the case with no exclusive points. Since \(L_I(x)=u\), the lower maps commute and their composition is \(L_I\).

Conversely, if a gap \((u,v)\) contains both exclusive types, choose a \(B\)-only point \(b\) and a \(C\)-only point \(c\). If \(b<c\), take \(x=c\). Then \(t=L_B(c)\) is \(B\)-only with \(t\ge b>u\), so
\[
L_BL_C(c)=t>L_C(t)=L_CL_B(c).
\]
If \(c<b\), take \(x=b\): putting \(t=L_C(b)\) gives a \(C\)-only point in the gap and
\[
L_CL_B(b)=t>L_B(t)=L_BL_C(b).
\]
The exclusivity of \(t\) follows because the gap has no common points. Therefore commutation fails exactly when a gap contains both exclusive types.

**Step 3: Upper roundings.** Reverse the chain order. Upper roundings in the original order become lower roundings in the reversed order, and the common-point gaps and the condition on exclusive types are unchanged. Applying Step 2 in the reversed order proves that \(U_B,U_C\) commute under precisely the same condition and, in that case, their composition is \(U_I\). This also establishes the promised equivalence of the two same-polarity commutation equations.

**Step 4: Exact enumeration.** At each of the \(k=n-2\) interior points choose one of four membership symbols: neither set, \(B\) only, \(C\) only, or both. The symbol 'both' separates consecutive gaps of the common fixed set, whose endpoints are also 'both'. A gap of length \(j\) contains no internal 'both' and is valid exactly when its word over the other three symbols avoids simultaneously having a \(B\)-only and a \(C\)-only letter. It therefore has
\[
g_j=2^j+2^j-1=2^{j+1}-1
\]
possible words: any word over \(\{\text{neither},B\text{-only}\}\), or over \(\{\text{neither},C\text{-only}\}\), subtracting the all-neither word counted twice. Its ordinary generating function is
\[
G(z)=\sum_{j\ge0}g_j z^j
=\frac{2}{1-2z}-\frac{1}{1-z}
=\frac{1}{(1-z)(1-2z)}.
\]
A complete membership word consists of one such gap followed by any number of repetitions of a 'both' symbol and another gap. Thus
\[
A(z)=G(z)\sum_{r\ge0}(zG(z))^r
=\frac{G(z)}{1-zG(z)}
=\frac{1}{1-4z+2z^2}.
\]
Extracting coefficients proves the recurrence. Solving its characteristic equation with roots \(2\pm\sqrt2\) gives the displayed closed form. The probability follows on dividing by the \(4^k\) unrestricted ordered pairs and keeping the dominant root. This argument applies to every \(n\ge2\); finite computations are corroboration, not the proof.

## Verification

Run `python3 verify.py` from the directory containing this document and the supplied standalone checker. It uses only the Python standard library. It independently compares, for every pair of endpoint-containing subsets through \(n=12\), (i) lower commutation, (ii) upper commutation, and (iii) the mixed-exclusive gap criterion; it also verifies both composite equalities and the recurrence counts.

As a separate, more primitive check, it enumerates *all* ordered pairs of arbitrary unary maps on chain sizes \(n=2,3,4\), filters them by directly evaluating the defining monadic Gödel equations (M1)--(M5), and recovers precisely the endpoint-subset rounding pairs. The code reports `VERIFY_OK` on successful completion. This exhaustive computation stops at its stated bounds and is not an infinite proof.

## Relationship to prior work

Castaño et al. (arXiv:2006.10180, Lemma 1.1 and the relatively complete-subalgebra characterization in Section 1) establish the single-pair monadic Gödel structure. Cintula, Metcalfe and Tokuda (arXiv:2209.08566, Lemmas 3.2–3.3 and Theorem 3.4) give the general subalgebra representation of monadic lattice-valued quantifiers. Neither paper, in the inspected portions containing the definitions, structural results, applications and conclusions, classifies **ordered pairs of separately monadic structures with same-polarity commutation**, their intersection composite, or the number of such pairs.

The published result *Frobenius-adjoint and monadic expansions coincide on Gödel algebras* (2026, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-frobenius-adjoint-and-monadic-expansions-coincide-on-g-del-algeb--683f8d08b769`) supplies the one-pair \(2^{n-2}\) count and an additional comparison with Frobenius-adjoint operators. The present theorem does not claim either ingredient; it introduces a second named pair, determines their exact compatibility, and counts the compatible **ordered pairs**, rather than individual expansions. The separate published result *Finite criterion for commuting box and diamond condensations* concerns completion maps on modal **binary relations**, not commuting Gödel-chain monadic unary operations or pairs of their fixed-point subchains.

The integer sequence \(1,4,14,48,164,\ldots\) and its recurrence are already recorded as OEIS A007070, with unrelated interpretations. No novelty is claimed for the bare sequence or recurrence in isolation; the contribution is the precise correspondence and structural commutation theorem in monadic Gödel semantics. Searches for a formulation with compatible subchains, two commuting monadic quantifier pairs, or the intersection normal form did not identify prior coverage.

## Limitations

The two within-pair modalities need not commute with one another; the theorem does not assert \(\forall_B\exists_C=\exists_C\forall_B\) or any full two-variable cylindric identity. All statements depend on a fixed finite **linear** Gödel reduct, where each endpoint-containing subset is a Gödel subalgebra. They do not extend automatically to arbitrary finite Gödel algebras or Heyting algebras with branching order. The known occurrence of the numerical sequence in other settings is acknowledged rather than claimed as a new recurrence. The available searches cannot rule out an equivalent interpretation under different algebraic terminology; independent verification of originality remains valuable.

## References

1. Diego Castaño, Cecilia Cimadamore, José Patricio Díaz Varela, Laura Rueda, *An algebraic study of S5-modal Gödel logic*, arXiv:2006.10180, first submitted 17 June 2020; *Studia Logica* 109 (2021), 937–967. `https://arxiv.org/html/2006.10180v1`.
2. Petr Cintula, George Metcalfe, Naomi Tokuda, *Algebraic semantics for one-variable lattice-valued logics*, arXiv:2209.08566, first submitted 18 September 2022. `https://arxiv.org/pdf/2209.08566`.
3. *Frobenius-adjoint and monadic expansions coincide on Gödel algebras*, public mathematical record (2026). `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-frobenius-adjoint-and-monadic-expansions-coincide-on-g-del-algeb--683f8d08b769`.
4. *Finite criterion for commuting box and diamond condensations*, public mathematical record (2026). `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-criterion-for-commuting-box-and-diamond-condensations--c53088b3c02d`.
5. OEIS Foundation, *A007070*, recurrence and other interpretations. `https://oeis.org/A007070`.
