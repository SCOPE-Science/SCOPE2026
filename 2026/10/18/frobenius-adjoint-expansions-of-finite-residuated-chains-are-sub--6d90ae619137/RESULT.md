# Frobenius-adjoint expansions of finite residuated chains are subalgebra roundings

## Finding

Let \(L=(L,\wedge,\vee,\otimes,\to,0,1)\) be any nontrivial **finite bounded integral commutative residuated chain**. The pairs of unary operations \((f,g)\) making \(L\) a Frobenius-adjoint residuated lattice in the sense of Wang–Shi–Wang are in bijection with its subalgebras \(S\) in the full bounded-residuated signature. The correspondence is
\[
 f_S(x)=\max\{s\in S:s\le x\},\qquad
 g_S(x)=\min\{s\in S:x\le s\}.
\]
In particular, every expansion is uniquely a simultaneous lower/upper rounding to a subset closed under both fusion and residuation; **every** such subalgebra gives an expansion, even when fusion is not idempotent.

This parametrization also describes the entire ordered family of expansions:
\[
 S\subseteq T\quad\Longleftrightarrow\quad
 f_S\le f_T\text{ pointwise}
 \quad\Longleftrightarrow\quad g_S\ge g_T\text{ pointwise}.
\]

For the standard \(n\)-element Łukasiewicz chain \(\mathsf{L}_n\), where \(n\ge2\), put \(N=n-1\) and
\[
 \mathsf{L}_n=\{0,1/N,2/N,\ldots,1\}.
\]
Its Frobenius-adjoint expansions are exactly the roundings to
\[
 S_d=\{0,1/d,2/d,\ldots,1\},\qquad d\mid N.
\]
Thus their number is the divisor-counting function
\[
 \boxed{\#\operatorname{FARL}(\mathsf{L}_n)=\tau(n-1)},
\]
and their pointwise-\(f\) order is isomorphic to the divisor lattice of \(n-1\): \(S_d\subseteq S_e\) precisely when \(d\mid e\). The first counts, for \(n=2,\ldots,10\), are \(1,2,2,3,2,4,2,4,3\).

For comparison, the Gödel-chain counterpart has \(2^{n-2}\) expansions, a count previously established; it is not claimed as a new consequence here.

## Assumptions and scope

A bounded integral commutative residuated lattice has bottom \(0\), top/monoidal identity \(1\), commutative associative fusion \(\otimes\), and adjoint residuation:
\[
 a\otimes b\le c\ \Longleftrightarrow\ b\le a\to c.
\]
The underlying order of \(L\) is finite and total; fusion need not equal meet. A subset \(S\subseteq L\) is a full-signature subalgebra when \(0,1\in S\) and \(S\) is closed under \(\otimes,\to,\wedge,\vee\). For a chain, the last two closure conditions are automatic.

The five Frobenius-adjoint axioms, with \(x,y\in L\), are:
\[
\begin{aligned}
\mathrm{F1}:&\quad f(x)\le x,\\
\mathrm{F2}:&\quad g(x)\le y\ \Longleftrightarrow\ x\le f(y),\\
\mathrm{F3}:&\quad f(g(x)\to y)=g(x)\to f(y),\\
\mathrm{F4}:&\quad f(g(x)\vee y)=g(x)\vee f(y),\\
\mathrm{F5}:&\quad g(x\wedge g(y))=g(x)\wedge g(y).
\end{aligned}
\]
Only the finite-chain theorem and the finite Łukasiewicz classification are asserted. The theorem is not a claim that arbitrary finite residuated lattices admit every subalgebra rounding pair.

## Proof

### 1. Every Frobenius-adjoint pair comes from a subalgebra

Assume F1–F5. By F2, \(g\) is the left adjoint of \(f\), so both are increasing, \(x\le f(g(x))\), and \(g(f(x))\le x\). From F1, \(f(0)=0\). Setting \(y=0\) in F4 therefore yields
\[
 f(g(x))=g(x)\vee f(0)=g(x).
\]
The adjunction unit now gives \(x\le g(x)\). Furthermore, since \(g(f(x))\le x\), monotonicity of \(f\) and the displayed identity give
\[
 g(f(x))=f(g(f(x)))\le f(x),
\]
while extensivity of \(g\) gives the reverse inequality. Thus
\[
 g(f(x))=f(x),\qquad f(g(x))=g(x).
\]
It follows that \(f\) and \(g\) are idempotent and share a common image/fixed-point set \(S\). Adjunction and F1 also give \(f(1)=1\) and \(g(0)=0\), hence \(0,1\in S\).

For every \(s\in S\), \(f(s)=g(s)=s\). Monotonicity and \(f(x)\le x\) imply that \(f(x)\) is the greatest member of \(S\) below \(x\). Similarly, \(g(x)\) is the least member of \(S\) above \(x\). This proves the rounding formula and uniqueness of \(S\).

We next verify closure. If \(s,t\in S\), apply F3 with \(g(s)=s\) and \(y=t\):
\[
 f(s\to t)=s\to f(t)=s\to t.
\]
Thus \(s\to t\in S\). To prove closure under fusion, put \(w=s\otimes t\). Residuation gives \(t\le s\to w\). Applying increasing \(f\) and F3,
\[
 t=f(t)\le f(s\to w)=s\to f(w).
\]
A second application of residuation gives \(w=s\otimes t\le f(w)\). By F1 the reverse inequality holds, hence \(f(w)=w\) and \(w\in S\). Because \(S\) lies in a chain, its binary minimum and maximum already lie in \(S\). Therefore \(S\) is a full-signature subalgebra.

### 2. Every subalgebra produces a Frobenius-adjoint pair

Conversely, fix a subalgebra \(S\subseteq L\) and define \(f=f_S\), \(g=g_S\) by the rounding formulas. Both exist since \(0,1\in S\). Contractivity F1 holds directly. For any \(x,y\in L\), the existence of an element of \(S\) between \(x\) and \(y\) is equivalent to either inequality
\[
 g(x)\le y\ \Longleftrightarrow\ x\le f(y),
\]
which proves F2.

Write \(s=g(x)\in S\). For F3, the element \(s\to f(y)\) belongs to \(S\) and satisfies \(s\to f(y)\le s\to y\), hence
\[
 s\to f(y)\le f(s\to y).
\]
For the reverse inequality set \(t=f(s\to y)\in S\). Since \(t\le s\to y\), residuation gives \(s\otimes t\le y\). Subalgebra closure makes \(s\otimes t\in S\), so \(s\otimes t\le f(y)\). Residuation gives \(t\le s\to f(y)\), proving F3.

In a chain, rounding to a fixed \(s\in S\) commutes with a maximum against \(s\):
\[
 f(s\vee y)=s\vee f(y).
\]
Indeed, for \(y\le s\) both sides equal \(s\); for \(y>s\), both equal \(f(y)\). This is F4. Dually, for \(t=g(y)\in S\), rounding upward commutes with a minimum against \(t\):
\[
 g(x\wedge t)=g(x)\wedge t,
\]
which is F5. Thus all five axioms hold, proving the bijection.

Finally, if \(S\subseteq T\), then lower rounding to \(S\) is at most lower rounding to \(T\), and upper rounding to \(S\) is at least upper rounding to \(T\). Conversely, if \(f_S\le f_T\), evaluating at each \(s\in S\) gives \(s=f_S(s)\le f_T(s)\le s\), so \(s\in T\). The converse from \(g_S\ge g_T\) is dual. This proves the asserted order isomorphism.

### 3. Exact Łukasiewicz-chain specialization

Set \(N=n-1\) and identify the elements of \(\mathsf{L}_n\) with \(i/N\) for integers \(0\le i\le N\). Its fusion and residuation are
\[
 x\otimes y=\max(0,x+y-1),\qquad x\to y=\min(1,1-x+y).
\]
Every subalgebra \(S\) contains \(0,1\), and is closed under negation \(\neg x=x\to0=1-x\), truncated addition \(x\oplus y=\neg(\neg x\otimes\neg y)=\min(1,x+y)\), and truncated subtraction \(x\ominus y=x\otimes\neg y=\max(0,x-y)\).

Let \(a\) be the smallest positive element of \(S\). Repeated truncated addition shows that every positive integer multiple \(ja\le1\) belongs to \(S\). If \(\lfloor1/a\rfloor a<1\), then \(1\ominus(\lfloor1/a\rfloor a)\) is a positive member of \(S\) smaller than \(a\), a contradiction. Therefore \(a=1/d\) for some positive integer \(d\) dividing \(N\). For any \(s\in S\), repeatedly subtract \(a\) until the remainder lies in \([0,a)\); closure under \(\ominus\) and minimality of \(a\) force remainder zero. Hence every member of \(S\) is an integer multiple of \(1/d\), and all these multiples occur by truncated addition. Thus \(S=S_d\).

Conversely each \(S_d\) with \(d\mid N\) is closed under the displayed operations and contains \(0,1\), so it is a subalgebra. The set \(S_d\) lies inside \(S_e\) exactly when \(d\mid e\). Therefore there are precisely \(\tau(N)\) Frobenius-adjoint expansions and they form the divisor lattice as claimed.

## Verification

The accompanying stand-alone `verify.py` implements F1–F5 directly on finite chains. Independently it enumerates every endpoint-containing subset closed under fusion and residuation, builds the corresponding rounding maps, and compares their complete sets of operator pairs to those obtained by enumerating all increasing contractive right adjoints \(f\) (recovering the unique left adjoint \(g\)). It checks every size \(2\le n\le10\) for both Łukasiewicz and Gödel chains, and two additional non-Gödel finite residuated-chain families (nilpotent-minimum and drastic fusion) for \(2\le n\le9\). It also exhausts eligible subalgebras through size 13 for the first two families and independently verifies the inclusion/pointwise-order equivalence on small Łukasiewicz chains.

Expected terminal marker: `FINITE_CHAIN_FROBENIUS_VERIFY_OK`. The finite replay corroborates, but does not replace, the arbitrary finite-chain proof above.

## Relationship to prior work

Wang, Shi, and Wang introduce F1–F5 and derive properties of the common fixed-point image (including Frobenius identities) in their 2026 paper. Those definitions and necessary identities are prior work. The present complete **if-and-only-if** subalgebra-rounding representation on arbitrary finite residuated chains, especially the construction from any subalgebra, and its exact non-idempotent Łukasiewicz specialization are the contribution asserted here.

A previously published account of Frobenius-adjoint **Gödel** algebras proves the Gödel-chain count \(2^{n-2}\) and identifies their subchain roundings. It is strictly a special (idempotent) case of the finite-chain direction; neither the non-idempotent classification nor the Łukasiewicz divisor-lattice formula follows from its Gödel-only statement. The Gödel count is given here solely as a contrast.

Finite Łukasiewicz subalgebras, viewed by themselves, are classically described by divisors. The novelty claim is **not** that this divisor fact is new: it is the identification of such subalgebras with exactly the admissible Frobenius-adjoint operator pairs, which yields the sharp expansion census and order in the newly defined algebraic semantics.

## Limitations

The theorem needs a finite chain. Its sufficiency proof exploits the linear order in F4–F5, and the result is not asserted for arbitrary residuated lattices, infinite chains, or unrelated monadic axiom systems. The arithmetic formula requires the **standard** finite Łukasiewicz chain, not arbitrary finite MV-algebras. The classification is an exact enumeration of expansions on each fixed reduct, not a claim about all models of the associated full logic or a decidability or complexity theorem.

The structural tools and MV-subalgebra arithmetic have substantial antecedents; historical priority cannot be certified by a finite literature search. Full originality of the combined Frobenius-adjoint classification would require broader specialist review. No independent verification has been performed.

## References

1. Juntao Wang, Jieqiong Shi, Mei Wang, *Frobenius–Galois expansions of substructural logics: Algebraization, Kalman equivalence and positive-cone semantics*, arXiv:2609.09529, first publicly posted September 8, 2026. In particular Definition 3.8, Proposition 3.13, and Example 3.17.
2. *Frobenius-adjoint and monadic expansions coincide on Gödel algebras*, publicly available research record, October 4, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-frobenius-adjoint-and-monadic-expansions-coincide-on-g-del-algeb--683f8d08b769 . Its Gödel-chain result is credited as prior coverage.
3. Bruno Teheux, *Lattice of subalgebras in the finitely generated varieties of MV-algebras*, Discrete Mathematics 307 (2007), 2261–2275, DOI:10.1016/j.disc.2006.08.006. Earlier MV-subalgebra theory is credited; the elementary divisor argument here is included self-contained.
